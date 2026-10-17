import json
import os
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.request import urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
from app.main import DEFAULTS, Handler, read_port, student_info

class ConfigurationTests(unittest.TestCase):
    def test_defaults(self):
        with patch.dict(os.environ, {}, clear=True): self.assertEqual(student_info(), DEFAULTS)
    def test_all_environment_overrides(self):
        with patch.dict(os.environ, dict(STUDENT_NAME="Test", STUDENT_SURNAME="User", STUDENT_GROUP="DEMO", STUDENT_ID="0007"), clear=True):
            self.assertEqual(student_info(), dict(name="Test", surname="User", group="DEMO", student_id="0007"))
    def test_empty_identity_uses_defaults(self):
        with patch.dict(os.environ, {"STUDENT_NAME":"", "STUDENT_ID":""}, clear=True): self.assertEqual(student_info(), DEFAULTS)
    def test_default_port(self):
        with patch.dict(os.environ, {}, clear=True): self.assertEqual(read_port(),8000)
    def test_configuration_file_and_environment_precedence(self):
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder)/"app.conf"; config.write_text("APP_PORT=9123\n")
            with patch.dict(os.environ, {"APP_CONFIG":str(config)}, clear=True):
                self.assertEqual(read_port(),9123)
                with patch.dict(os.environ, {"APP_PORT":"9234"}): self.assertEqual(read_port(),9234)
                with patch.dict(os.environ, {"APP_PORT":""}): self.assertEqual(read_port(),9123)
    def test_invalid_ports(self):
        for raw in ["0", "65536", "abc", "-1", "1.5"]:
            with self.subTest(raw=raw), patch.dict(os.environ, {"APP_PORT":raw}, clear=True):
                with self.assertRaises(ValueError): read_port()
    def test_missing_configuration_falls_back(self):
        with patch.dict(os.environ, {"APP_CONFIG":"/nonexistent-devops.conf"}, clear=True): self.assertEqual(read_port(),8000)

class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(("127.0.0.1",0),Handler)
        self.thread = threading.Thread(target=self.server.serve_forever,daemon=True); self.thread.start()
        self.base = "http://127.0.0.1:"+str(self.server.server_port)
    def tearDown(self):
        self.server.shutdown(); self.thread.join(timeout=3); self.server.server_close()
    def test_health(self):
        with urlopen(self.base+"/health") as response:
            self.assertEqual(response.status,200); self.assertEqual(response.read(),b"OK\n")
    def test_json_all_identity_fields(self):
        with patch.dict(os.environ, {}, clear=True), urlopen(self.base+"/student") as response:
            self.assertEqual(json.load(response),DEFAULTS)
    def test_html_escapes_input(self):
        with patch.dict(os.environ, {"STUDENT_NAME":"<script>alert(1)</script>"}), urlopen(self.base+"/") as response:
            body=response.read().decode(); self.assertIn("&lt;script&gt;",body); self.assertNotIn("<script>",body)
    def test_missing_route(self):
        with self.assertRaises(HTTPError) as error: urlopen(self.base+"/missing")
        self.assertEqual(error.exception.code,404)

if __name__ == "__main__": unittest.main()
