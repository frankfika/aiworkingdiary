#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from typing import List


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


def run_generate_report(paths: List[str], out_file: str):
    out_path = ensure_repo_path(out_file)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    lines = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines.append(f"# Auto Worker Report\n")
    lines.append(f"Generated at: {ts} (UTC)\n\n")
    total_files = 0
    for rel in paths:
        dir_path = ensure_repo_path(rel)
        count = 0
        file_list = []
        if os.path.isdir(dir_path):
            for root, _, files in os.walk(dir_path):
                for fn in files:
                    count += 1
                    total_files += 1
                    file_list.append(os.path.relpath(os.path.join(root, fn), REPO_ROOT))
        lines.append(f"## {rel} ({count} files)\n")
        if file_list:
            for fp in sorted(file_list)[:50]:
                lines.append(f"- {fp}\n")
        lines.append("\n")

    lines.append(f"Total files across sections: {total_files}\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    log(f"Generated report: {out_file}")


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
            elif ttype == "generate_report":
                paths = t.get("paths", [])
                if not isinstance(paths, list):
                    paths = []
                run_generate_report(paths, t.get("out_file", "automation/test_report.md"))
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