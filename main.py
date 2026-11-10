import os
from pathlib import Path

source = Path(__file__).resolve().parent / "sticker.png"
destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
destination.parent.mkdir(parents=True, exist_ok=True)
image = source.read_bytes()
if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) > 1_048_576:
    raise ValueError("sticker must be a PNG no larger than one MiB")
destination.write_bytes(image)
