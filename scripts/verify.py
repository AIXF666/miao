#!/usr/bin/env python3
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = "喵".encode() * 10000
commands = {
    "Python": ["python3", "languages/python/miao.py"],
    "JavaScript": ["node", "languages/javascript/miao.js"],
    "Bash": ["bash", "languages/bash/miao.sh"],
    "Ruby": ["ruby", "languages/ruby/miao.rb"],
    "Go": ["go", "run", "languages/go/miao.go"],
}
failed = False

def check(name, output):
    global failed
    ok = output == EXPECTED
    print(f"{name}: {'PASS' if ok else 'FAIL'}")
    failed |= not ok

check("Markdown", (ROOT / "markdown/miao.md").read_bytes())
with tempfile.TemporaryDirectory() as tmp:
    if shutil.which("cc"):
        binary = str(Path(tmp) / "miao")
        build = subprocess.run(["cc", "languages/c/miao.c", "-o", binary], cwd=ROOT)
        if build.returncode:
            failed = True
            print("C: FAIL (compilation)")
        else:
            commands["C"] = [binary]
    else:
        print("C: SKIP (cc unavailable)")
    for name, command in commands.items():
        if not shutil.which(command[0]):
            print(f"{name}: SKIP ({command[0]} unavailable)")
            continue
        result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE)
        if result.returncode:
            failed = True
            print(f"{name}: FAIL (exit {result.returncode})")
        else:
            check(name, result.stdout)
sys.exit(1 if failed else 0)
