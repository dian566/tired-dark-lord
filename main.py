#!/usr/bin/env python3
"""The Tired Dark Lord — writes a ~100-word villain monologue to /output/entry.txt.

The speaker is Veyra, ringer of the Hollow Bell: twelve rings in, each one
making the kingdom forget a little more of itself, one more ring at the
eclipse to make the sun forget to rise. Her tiredness never gets named —
it lives in the pauses, the abandoned kettle, the counting of chimes.
The program is fully deterministic: the same bytes come out on every run.
"""

import os

ENTRY = (
    "You came up the stair — good. Mind the third step. It bites.\n"
    "I have rung the Hollow Bell twelve times, hero, and each time the kingdom forgot a little more of itself. One more ring, at the eclipse, and the sun will forget to rise. That is the plan.\n"
    "Do you know what the bell takes from the ringer? Neither did I, the first eleven times.\n"
    "Sit, then. The kettle is — no. The kettle is empty.\n"
    "Draw your sword, if you must. I will be here, counting the chimes, waiting for the dark to finally keep me."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 600, "entry must be 1-600 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
