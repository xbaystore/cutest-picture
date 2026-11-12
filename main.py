#!/usr/bin/env python3
"""Cutest Picture entry (make.fun cutest-picture-01).

The picture is the picture.png bundled beside this file: a 3D-rendered baby
otter hugging a pink heart. The program's whole job is to deliver those exact
bytes to the output directory as entry.png — the judge sees precisely the
file that ships in the repository, and two runs write identical bytes because
the copy is a pure function of the bundled asset.
"""

import os
from pathlib import Path

ASSET_NAME = "picture.png"
OUTPUT_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def read_asset(source: Path) -> bytes:
    """Return the asset's bytes, refusing anything that is not a whole
    PNG or JPEG — the gate turns the entry away on a bad header."""
    data = source.read_bytes()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise ValueError(f"{source.name}: not a PNG or JPEG image")
    return data


def main() -> None:
    source = Path(__file__).resolve().parent / ASSET_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write to a sibling temp file, then rename: a reader of entry.png only
    # ever sees the whole picture, never a half-copied one.
    target = out_dir / OUTPUT_NAME
    tmp = out_dir / (OUTPUT_NAME + ".tmp")
    tmp.write_bytes(read_asset(source))
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
