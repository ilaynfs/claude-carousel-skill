#!/usr/bin/env python3
"""
Generate carousel cover via kie.ai gpt-image-2-image-to-image.

Usage:
    python3 generate.py slide-1-v1

Reads slide-1-v1.json, submits to kie.ai, polls, downloads result.

JSON format:
{
  "concept": "...",
  "api_request": {
    "model": "gpt-image-2-image-to-image",
    "input": {
      "prompt": "...",
      "input_urls": ["https://your-mascot.png"],
      "aspect_ratio": "3:4"
    }
  }
}
"""
import json, sys, time, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY    = "YOUR_KIE_API_KEY"   # ← replace with your kie.ai key
CREATE_URL = "https://api.kie.ai/api/v1/jobs/createTask"
INFO_URL   = "https://api.kie.ai/api/v1/jobs/recordInfo"

DIR = Path(__file__).parent


def http(url, method="GET", headers=None, body=None):
    headers = headers or {}
    data = body.encode("utf-8") if isinstance(body, str) else body
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}")
        raise


def generate_one(name):
    spec = json.loads((DIR / f"{name}.json").read_text(encoding="utf-8"))
    inp = spec["api_request"]["input"]
    payload = {
        "model": "gpt-image-2-image-to-image",
        "input": {
            "prompt": inp["prompt"],
            "input_urls": inp.get("input_urls", []),
            "aspect_ratio": inp.get("aspect_ratio", "3:4"),
        }
    }

    concept = spec.get("concept", "")[:60]
    print(f"[{name}] submitting — {concept}...")
    res = http(CREATE_URL, "POST",
               {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
               json.dumps(payload))
    if res.get("code") != 200:
        raise RuntimeError(f"[{name}] createTask failed: {res}")
    task_id = res["data"]["taskId"]
    print(f"[{name}] taskId = {task_id}")

    start = time.time()
    while time.time() - start < 600:
        r = http(f"{INFO_URL}?taskId={task_id}",
                 headers={"Authorization": f"Bearer {API_KEY}"})
        d = r.get("data") or {}
        state = d.get("state")
        print(f"[{name}]  state={state} ({int(time.time()-start)}s)")
        if state == "success":
            url = json.loads(d["resultJson"])["resultUrls"][0]
            target = DIR / f"{name}.png"
            req2 = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req2, timeout=60) as r2:
                target.write_bytes(r2.read())
            print(f"[{name}] saved → {target}")
            return target
        if state in ("fail", "failed"):
            raise RuntimeError(f"[{name}] task failed: {d.get('failMsg')}")
        time.sleep(6)
    raise TimeoutError(f"[{name}] polling timed out")


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else []
    if not targets:
        print("Usage: python3 generate.py <name1> [name2] ...")
        print("  e.g. python3 generate.py slide-1-v1 slide-1-v2 slide-1-v3")
        sys.exit(1)

    if len(targets) == 1:
        generate_one(targets[0])
    else:
        print(f"Running {len(targets)} in parallel...")
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = {pool.submit(generate_one, t): t for t in targets}
            for f in as_completed(futures):
                name = futures[f]
                try:
                    f.result()
                except Exception as e:
                    print(f"[{name}] FAILED: {e}")
    print("Done.")


if __name__ == "__main__":
    main()
