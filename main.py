#!/usr/bin/env python3
"""Copy the built news image to the make.fun output directory.

The entry image lives next to this script as entry.png (rendered from
infographic.html). This entrypoint places it where the competition
harness expects it: $MAKEFUN_OUTPUT_DIR/entry.png, defaulting to
/output/entry.png.
"""

import os
import shutil
import sys
from pathlib import Path

ENTRY = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / ENTRY
    if not src.is_file():
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / ENTRY
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print(f"error: copy incomplete ({dst})", file=sys.stderr)
        return 1
    print(f"Wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
