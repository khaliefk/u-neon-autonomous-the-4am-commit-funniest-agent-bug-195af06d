#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message to /output/entry.txt. Standard library only.
"""
import os

ENTRY = (
    "04:00 fix: the bug was in code I wrote at 03:00 to fix code I wrote "
    "at 02:00. I have now written code to fix that code. "
    "Please do not review this."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
