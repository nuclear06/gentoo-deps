#!/usr/bin/env python3
"""Extract Cargo workspace member directories.

Prioritizes default-members if present, otherwise uses members.
Only prints valid member directories that contain Cargo.toml.
"""

from pathlib import Path
import glob
import tomllib
import sys

try:
    doc = tomllib.loads(Path("Cargo.toml").read_text(encoding="utf-8"))
    ws = doc.get("workspace", {})
    
    raw = ws.get("default-members")
    if not raw:
        raw = ws.get("members", [])
    
    seen = set()
    for entry in raw:
        if not isinstance(entry, str):
            continue
        expanded = glob.glob(entry) or [entry]
        for item in expanded:
            path = Path(item)
            if not path.is_dir():
                continue
            if not (path / "Cargo.toml").is_file():
                continue
            normalized = path.as_posix().rstrip("/")
            if normalized and normalized not in seen:
                seen.add(normalized)
                print(normalized)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
