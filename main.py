#!/usr/bin/env python3
"""Snooze Button Roast — entry program.

Writes one line (120 characters) roasting an alarm clock that rings at
6 AM on a Saturday to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; deterministic — the program
writes the same bytes on every run.
"""

import os
import sys

ENTRY = "My alarm clock rang at 6 AM on a Saturday, proud as a rooster with a LinkedIn profile \u2014 so I promoted it to paperweight."


def validate_entry(text: str) -> None:
    """Fail loudly if the roast breaks the bounty gate (one line,
    1-200 characters, not only whitespace) instead of writing a bad entry."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
