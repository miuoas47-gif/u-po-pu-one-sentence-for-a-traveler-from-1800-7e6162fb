#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800, using only things such a traveler would
already know: roads, post offices, libraries, letters, books.
"""

import os
import sys

SENTENCE = (
    "Imagine one road joining every post office and library in the world, "
    "so a letter reaches any door in the blink of an eye and shelves of "
    "books from every land stand open on your table."
)


def main():
    text = SENTENCE
    if not text.strip():
        print("error: sentence is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(
            "error: sentence is %d characters, over the 200 limit" % len(text),
            file=sys.stderr,
        )
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line with no newline", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print("error: read-back does not match the sentence", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
