#!/usr/bin/env python3
"""One Star, Written in Sap -- make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The line is fixed and deterministic: the judge compares the text itself,
so the program's only job is to deliver it exactly, within the gate
(UTF-8 text, 1 to 279 characters, not only whitespace).
"""

from pathlib import Path

ENTRY = (
    "One star: bought for 'good energy,' shoved behind the TV, and my only "
    "sunlight is the glow of my owner's 3 a.m. doomscrolling. "
    "The fern got a window. I got Wi-Fi."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 279:
        raise ValueError(f"entry length {len(text)} is outside the 1-279 gate")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
