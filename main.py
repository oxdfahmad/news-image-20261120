#!/usr/bin/env python3
"""news-image-20261120 entry: deliver the bundled front page as the output.

The front page (entry.png) sums up Friday 20 November 2026 in ten
verified stories plus a five-item ticker. It is drawn in advance and
shipped beside this program; this script only validates it and places it
at $MAKEFUN_OUTPUT_DIR/entry.png (default /output).

Standard library only, no network, fully deterministic: the same input
bytes always produce the same output bytes.
"""
import hashlib
import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
SIZE_CAP = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("error:", message, file=sys.stderr)
    raise SystemExit(1)


def read_dimensions(blob):
    """Parse the PNG IHDR chunk and return (width, height).

    Layout after the 8-byte magic: 4-byte big-endian chunk length,
    4-byte chunk type ("IHDR"), then width and height as 4-byte
    big-endian unsigned integers.
    """
    if len(blob) < 33:
        # 8 magic + 4 length + 4 type + 13 IHDR data + 4 CRC.
        fail("entry.png is too short to hold a complete IHDR chunk")
    length, chunk_type = struct.unpack(">I4s", blob[8:16])
    if chunk_type != b"IHDR" or length != 13:
        fail("entry.png has no valid IHDR chunk")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


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

    width, height = read_dimensions(blob)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(
            f"entry.png is {width}x{height}, "
            f"expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )

    target_dir.mkdir(parents=True, exist_ok=True)
    target.write_bytes(blob)
    digest = hashlib.sha256(blob).hexdigest()
    print(
        f"wrote {target} ({len(blob)} bytes, {width}x{height}, "
        f"sha256 {digest})"
    )


if __name__ == "__main__":
    main()
