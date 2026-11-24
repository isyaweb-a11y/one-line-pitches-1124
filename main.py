#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes a single sentence (at most 240 characters) to /output/entry.txt.
The sentence pitches make.fun to a friend who has never coded: hand your
first app idea to an AI agent, in your own words, and see a first version
of it without learning to code or risking anything.
"""

import os

# The pitch itself: one sentence, plain words, spoken like a friend.
PITCH = (
    "That app idea you keep describing over coffee could be a real first "
    "version on your phone tonight: just describe it to an AI agent on "
    "make.fun in your own words - no code to learn, nothing to lose, and "
    "you stay the boss of every change."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    print(f"wrote {len(PITCH)} chars to {out_path}")


if __name__ == "__main__":
    main()
