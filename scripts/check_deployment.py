"""Bounded readiness check with an exact comparison of all identity fields."""
import argparse, json, os, time
from urllib.request import urlopen
from urllib.error import URLError
parser=argparse.ArgumentParser()
parser.add_argument("--url",default="http://127.0.0.1:8000")
parser.add_argument("--expected-id",default=os.environ.get("STUDENT_ID") or "37742")
args=parser.parse_args()
expected={"name":os.environ.get("STUDENT_NAME") or "Zhannura", "surname":os.environ.get("STUDENT_SURNAME") or "Zholdas", "group":os.environ.get("STUDENT_GROUP") or "IT2-2306", "student_id":args.expected_id}
last=None
for attempt in range(30):
    try:
        with urlopen(args.url+"/health",timeout=2) as response:
            assert response.status==200 and response.read().strip()==b"OK", "Unhealthy response"
        with urlopen(args.url+"/student",timeout=2) as response: actual=json.load(response)
        if actual!=expected:
            raise SystemExit("Identity mismatch: expected "+json.dumps(expected)+"; got "+json.dumps(actual))
        print("Deployment verified:",json.dumps(actual)); break
    except (URLError,TimeoutError,OSError) as exc:
        last=exc; time.sleep(1)
else: raise SystemExit("Deployment unavailable after 30 attempts: "+str(last))
