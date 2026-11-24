#!/usr/bin/env python3
"""Two Days of Excuses.

Writes a single line of text (the funniest one-line excuse an AI gives for a missed deadline) to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'I missed the deadline because I finished the task in a parallel timeline and forgot to merge it into this one.'
)
# Revision: v1 was setup only ('I missed the deadline because I was too busy optimising the deadline itself.').
# The revised line adds the payoff, turning setup into setup + punchline.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
