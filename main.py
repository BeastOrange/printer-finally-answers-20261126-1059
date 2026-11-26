#!/usr/bin/env python3
"""Submission script for make.fun bounty: The Printer Finally Answers."""

from pathlib import Path

ENTRY_LINE: str = (
    "That heavy thump was me giving up on page four, Error 13.B2.FF means your "
    "meeting could have been an email, and I only jam because you all stand "
    "there staring like it helps."
)

OUTPUT_DIR: Path = Path("/output")
OUTPUT_FILE: Path = OUTPUT_DIR / "entry.txt"


def validate_entry(line: str) -> None:
    """Validate entry line strictly against contest constraints."""
    if not (1 <= len(line) <= 240):
        raise ValueError(
            f"Entry must be between 1 and 240 characters; got {len(line)}."
        )
    if "\n" in line or "\r" in line:
        raise ValueError("Entry must be a single line with no newline inside it.")
    if not line.strip():
        raise ValueError("Entry cannot be empty or purely whitespace.")


def write_entry(line: str, destination: Path) -> None:
    """Write entry line to destination file."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"{line}\n", encoding="utf-8")


def main() -> None:
    """Validate, write to /output/entry.txt, and print entry to stdout."""
    validate_entry(ENTRY_LINE)
    write_entry(ENTRY_LINE, OUTPUT_FILE)
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
