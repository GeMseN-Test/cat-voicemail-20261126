#!/usr/bin/env python3
"""Cat voicemail greeting entry for make.fun.

Writes the one-line voicemail greeting to /output/entry.txt.
The line is the whole entry: a cat's voicemail, first-person voice,
one concrete cat crime, judgement at the end.
"""

import os

LINE = "You've reached Beans. Your mug's on the floor — 4 a.m. felt right. Leave a message. I'll sit on it."

# The gate requires 1 to 120 characters of UTF-8 text.
assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
