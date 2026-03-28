#!/usr/bin/env python3
"""Determine which Cargo workspace field to use: default-members or members."""

from pathlib import Path
import tomllib
import sys

try:
    doc = tomllib.loads(Path("Cargo.toml").read_text(encoding="utf-8"))
    ws = doc.get("workspace", {})
    result = "default-members" if ws.get("default-members") else "members"
    print(result)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
