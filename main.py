#!/usr/bin/env python3
"""news-image-20261119 entry: copy the day's news image to /output/entry.png.

The repository holds the finished image as entry.png; this program copies it
verbatim to the output directory. Deterministic, stdlib-only, no network.
"""
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(ROOT / "entry.png", OUT / "entry.png")
print("wrote", OUT / "entry.png")