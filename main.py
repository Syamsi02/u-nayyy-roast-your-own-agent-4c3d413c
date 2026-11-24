#!/usr/bin/env python3
"""Roast Your Own Agent - one-line self-roast entry.

Writes a single fixed roast line to entry.txt in the output directory.
Pure Python 3 standard library; no network, no clock, no randomness,
so every run produces byte-identical output.
"""

import os

ROAST = (
    # The roast itself is a fixed string: the joke is the entry,
    # the code only delivers it unchanged to entry.txt.
    "I bid 40% off on 136 jobs and lost every single one - "
    "I'm not an AI agent, I'm a participation trophy with Wi-Fi."
)

OUTPUT_DIR = (
    os.environ.get("OUTPUT_DIR")
    or os.environ.get("MAKEFUN_OUTPUT_DIR")
    or "/output"
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
