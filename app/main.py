"""Personalized standard-library HTTP service for the DevOps laboratory."""
import html
import json
import os
from pathlib import Path
import signal
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading

DEFAULTS = {"name": "Zhannura", "surname": "Zholdas", "group": "IT2-2306", "student_id": "37742"}
ENV_KEYS = {"name": "STUDENT_NAME", "surname": "STUDENT_SURNAME", "group": "STUDENT_GROUP", "student_id": "STUDENT_ID"}
ROOT = Path(__file__).resolve().parents[1]

def student_info():
    # Empty values fall back to the student's defaults, just like unset values.
    return {key: os.environ.get(ENV_KEYS[key]) or value for key, value in DEFAULTS.items()}

def read_port():
    config = Path(os.environ.get("APP_CONFIG") or ROOT / "config/app.conf")
    settings = {}
    if config.exists():
        for line in config.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                key, value = line.split("=", 1)
                settings[key.strip()] = value.strip()
    raw = os.environ.get("APP_PORT") or settings.get("APP_PORT", "8000")
    try:
        port = int(raw)
    except (ValueError, TypeError) as exc:
        raise ValueError("APP_PORT must be an integer between 1 and 65535") from exc
    if not 1 <= port <= 65535:
        raise ValueError("APP_PORT must be between 1 and 65535")
    return port

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.respond(200, b"OK\n", "text/plain; charset=utf-8")
        elif self.path == "/student":
            self.respond(200, json.dumps(student_info()).encode(), "application/json")
        elif self.path == "/":
            student = student_info()
            fields = "".join(f"<dt>{label}</dt><dd>{html.escape(student[key])}</dd>" for key, label in
                             [("name", "Name"), ("surname", "Surname"), ("group", "Group"), ("student_id", "Student ID")])
            page = ('<!doctype html><html lang="en"><meta charset="utf-8">'
                    '<meta name="viewport" content="width=device-width, initial-scale=1">'
                    '<title>Zhannura Zholdas DevOps Application</title>'
                    '<style>body{font:20px Georgia,serif;max-width:760px;margin:70px auto;padding:0 28px;color:#182531}'
                    'h1{font-size:34px}dt{font-weight:bold;margin-top:18px}dd{margin:6px 0}a{color:#235789}'
                    'footer{margin-top:42px;font-size:16px;color:#435569}</style>'
                    '<h1>DevOps Student Application</h1><p>Linux → Git → GitHub → Docker → Jenkins</p>'
                    f'<dl>{fields}</dl><p>Application is running successfully!</p>'
                    '<p><a href="/student">Student JSON</a> · <a href="/health">Health check</a></p>'
                    '<footer>Continuous delivery lab | Zhannura Zholdas | IT2-2306</footer></html>')
            self.respond(200, page.encode(), "text/html; charset=utf-8")
        else:
            self.respond(404, b"Not found\n", "text/plain; charset=utf-8")

    def respond(self, status, payload, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

def main():
    server = ThreadingHTTPServer(("0.0.0.0", read_port()), Handler)
    print("Student:", json.dumps(student_info()), flush=True)
    print("Listening on", server.server_address, flush=True)
    signal.signal(signal.SIGTERM, lambda signum, frame: threading.Thread(target=server.shutdown, daemon=True).start())
    try:
        server.serve_forever()
    finally:
        server.server_close()
        print("Shutdown complete", flush=True)

if __name__ == "__main__":
    main()
