#!/usr/bin/env python3
"""news-image-20261120 entry: deliver the bundled front page as the output.

The front page (entry.png, 1024x1024) sums up Friday 20 November 2026 in
ten verified stories plus a five-item ticker. It is drawn in advance and
shipped beside this program; this script only places it at
$MAKEFUN_OUTPUT_DIR/entry.png (default /output).

Standard library only, no network, fully deterministic: the same input bytes
always produce the same output bytes.
"""
import hashlib
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
SIZE_CAP = 1_048_576


def fail(message):
    print("error:", message, file=sys.stderr)
    raise SystemExit(1)


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = target_dir / "entry.png"

    if not source.is_file():
        fail("entry.png is missing from the repository")

    blob = source.read_bytes()
    if blob[:8] != PNG_MAGIC:
        fail("entry.png does not start with the PNG magic bytes")
    if len(blob) > SIZE_CAP:
        fail("entry.png is larger than the 1 MiB cap")

    target_dir.mkdir(parents=True, exist_ok=True)
    target.write_bytes(blob)
    digest = hashlib.sha256(blob).hexdigest()
    print(f"wrote {target} ({len(blob)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
