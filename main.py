from pathlib import Path

source = Path("/bot") / "sticker.png"
output = Path("/output/entry.png")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_bytes(source.read_bytes())
