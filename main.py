#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261117 bounty.

The submitted image is a newspaper-style infographic summing up the
world news of Tuesday 17 November 2026. It is built ahead of time and
ships in this repository as entry.png; this program only has to put an
exact copy of it where the grader looks.

Standard library only, no network, and the same bytes on every run, so
the grader's two runs agree byte for byte.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    # The image sits beside this file; resolve from our own location
    # instead of the working directory, which the grader does not fix.
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    # The grader sets MAKEFUN_OUTPUT_DIR; use /output, the directory
    # the rules name, when it is not set.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination = out_dir / "entry.png"

    if not source.is_file():
        print(f"entry.png not found next to {__file__}", file=sys.stderr)
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)

    # Check the copy landed whole before reporting success.
    if destination.stat().st_size != source.stat().st_size:
        print("copied entry.png has the wrong size", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
