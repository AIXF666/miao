#!/usr/bin/env python3
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = "喵".encode() * 10000
failed = False

def check(name, output):
    global failed
    ok = output == EXPECTED
    print(f"{name}: {'PASS' if ok else 'FAIL'}", flush=True)
    failed |= not ok

for name in ("README.md", "markdown/miao.md"):
    check(name, (ROOT / name).read_bytes())
commands = json.loads((ROOT / "scripts/commands.json").read_text())
with tempfile.TemporaryDirectory() as tmp:
    for name, compiler, source in [("C", "cc", "languages/c/miao.c"), ("C++", "c++", "languages/cpp/miao.cpp"), ("Rust", "rustc", "languages/rust/miao.rs"), ("Fortran", "gfortran", "languages/fortran/miao.f90")]:
        if not shutil.which(compiler):
            print(f"{name}: SKIP ({compiler} unavailable)")
            continue
        binary = str(Path(tmp) / name.replace('+', 'p'))
        result = subprocess.run([compiler, source, "-o", binary], cwd=ROOT)
        if result.returncode:
            failed = True
            print(f"{name}: FAIL (compilation)")
        else:
            commands[name] = [binary]
    for name, command in commands.items():
        if not shutil.which(command[0]):
            print(f"{name}: SKIP ({command[0]} unavailable)")
            continue
        if command[0] == "java" and subprocess.run(["java", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
            print(f"{name}: SKIP (Java runtime unavailable)")
            continue
        try:
            result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, timeout=120)
            if result.returncode:
                failed = True
                print(f"{name}: FAIL (exit {result.returncode})")
            else:
                check(name, result.stdout)
        except subprocess.TimeoutExpired:
            failed = True
            print(f"{name}: FAIL (timeout)")
sys.exit(1 if failed else 0)
