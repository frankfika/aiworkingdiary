#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from datetime import datetime, timezone


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))
TASKS_PATH = os.path.join(REPO_ROOT, "automation", "tasks.json")


def log(msg: str):
    print(f"[auto-worker] {msg}")


def load_tasks():
    if not os.path.exists(TASKS_PATH):
        raise FileNotFoundError(f"Tasks file not found: {TASKS_PATH}")
    with open(TASKS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("tasks", [])


def ensure_repo_path(path: str) -> str:
    # Ensure path is relative to repo root
    if os.path.isabs(path):
        return path
    return os.path.join(REPO_ROOT, path)


def run_shell(command: str):
    log(f"Running shell: {command}")
    subprocess.run(command, shell=True, check=True)


def run_update_timestamp(out_file: str):
    out_path = ensure_repo_path(out_file)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"last_run: {ts}\n")
    log(f"Updated timestamp file: {out_file}")


def main():
    log("Starting auto worker")
    tasks = load_tasks()
    failures = []
    for t in tasks:
        if not t.get("enabled", False):
            log(f"Skip disabled task: {t.get('id')}")
            continue
        ttype = t.get("type")
        tid = t.get("id")
        try:
            if ttype == "shell":
                run_shell(t.get("command", ""))
            elif ttype == "update_timestamp":
                run_update_timestamp(t.get("out_file", "automation/last_run.txt"))
            else:
                log(f"Unknown task type '{ttype}' for {tid}; skipping")
        except Exception as e:
            failures.append((tid, str(e)))
            log(f"Task failed: {tid} -> {e}")

    if failures:
        log("Some tasks failed:")
        for tid, err in failures:
            log(f" - {tid}: {err}")
        # Exit non-zero so workflow surfaces failures
        sys.exit(1)
    else:
        log("All tasks completed successfully")


if __name__ == "__main__":
    main()