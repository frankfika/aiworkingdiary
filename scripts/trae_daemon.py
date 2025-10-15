#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from datetime import datetime, timezone


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))
LOG_PATH = os.path.join(REPO_ROOT, "automation", "trae_daemon.log")
INTERVAL = int(os.getenv("INTERVAL_SECONDS", "900"))  # 默认每15分钟


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    line = f"[{now_utc()}] {msg}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)
    print(line, end="")


def run(cmd: str):
    return subprocess.run(cmd, shell=True, cwd=REPO_ROOT, capture_output=True, text=True)


def run_worker():
    res = run("python3 scripts/auto_worker.py")
    if res.stdout:
        log(res.stdout)
    if res.stderr:
        log(f"stderr: {res.stderr}")
    return res.returncode == 0


def commit_and_push_if_changed():
    status = run("git status --porcelain")
    if status.stdout.strip():
        log("Detected changes; committing and pushing...")
        cmds = [
            "git config user.name 'fangchen'",
            "git config user.email 'fangchen@users.noreply.github.com'",
            "git add -A",
            f"git commit -m 'chore(auto-worker): update at {now_utc()}'",
            "git push"
        ]
        for c in cmds:
            r = run(c)
            if r.stdout:
                log(r.stdout)
            if r.stderr:
                log(f"stderr: {r.stderr}")
            if r.returncode != 0:
                log(f"Command failed: {c}")
                return False
        return True
    else:
        log("No changes to commit.")
        return True


def main():
    log("Trae daemon started.")
    log(f"Interval seconds: {INTERVAL}")
    try:
        while True:
            log("Tick: executing auto_worker...")
            ok = run_worker()
            if not ok:
                log("Worker error; skipping commit/push this cycle.")
            else:
                commit_and_push_if_changed()
            log("Sleeping...")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        log("Trae daemon stopped by KeyboardInterrupt.")
    except Exception as e:
        log(f"Trae daemon crashed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()