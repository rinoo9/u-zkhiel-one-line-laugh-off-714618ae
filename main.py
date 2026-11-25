"""One-Line Laugh-Off entry.

Writes a single original joke to /output/entry.txt.
Deterministic, no network, no randomness.

Craft notes (revision, round 2): the round-1 line had the smart
speaker whispering the bank balance, and the unsubmitted 22:24
revision had the fitness tracker conspiring about the broken
elevator. This rewrite takes a fresh angle — the smart fridge as a
passive-aggressive housemate. It texts at 3 a.m. with a status
report that escalates: the milk expired, the ice cream is judging,
and the vegetables have filed a formal complaint. The turn is the
fridge treating the kitchen like an office with HR.
"""

import os

ENTRY = (
    "My smart fridge texted me at 3 a.m.: the milk has expired, the ice "
    "cream is judging me, and the vegetables have filed a formal complaint."
)


def main() -> None:
    line = ENTRY
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
