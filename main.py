"""One-Line Laugh-Off entry.

Writes a single original joke to /output/entry.txt.
Deterministic, no network, no randomness.
"""

import os

ENTRY = "My fitness tracker congratulated me on climbing 12 flights of stairs, so I told it the elevator was broken and we both agreed to lie."


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
