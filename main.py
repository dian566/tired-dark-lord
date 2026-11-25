#!/usr/bin/env python3
# The Tired Dark Lord — emits a ~100-word villain monologue at /output/entry.txt.
#
# Veyra, keeper of the Hollow Bell, has already rung it a dozen times; every
# eclipse would make the sun itself forget to rise. What wears her down is
# never spelled out — it leaks through the pauses, the kettle left empty, the
# chimes she keeps count of. Output is fixed: identical bytes on every run.

import os as _os

MONOLOGUE = (
    "You came up the stair — good. Mind the third step. It bites.\n"
    "I have rung the Hollow Bell twelve times, hero, and each time the kingdom forgot a little more of itself. One more ring, at the eclipse, and the sun will forget to rise. That is the plan.\n"
    "Do you know what the bell takes from the ringer? Neither did I, the first eleven times.\n"
    "Sit, then. The kettle is — no. The kettle is empty.\n"
    "Draw your sword, if you must. I will be here, counting the chimes, waiting for the dark to finally keep me."
)


def run() -> None:
    body = MONOLOGUE
    size = len(body)
    if not 1 <= size <= 600:
        raise ValueError("entry must be 1-600 characters")
    count = len(body.split())
    if not 90 <= count <= 110:
        raise ValueError(f"entry must be about 100 words, got {count}")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    _os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(body)


if __name__ == "__main__":
    run()
