#!/usr/bin/env python3
"""Submission script for make.fun bounty: The Printer Finally Answers."""

from pathlib import Path

ENTRY_LINE: str = (
    "That heavy thump was me locking Tray 2, Error 49.38.07 means you printed "
    "an email that just says thanks, and I only jam because watching four "
    "adults stare at my tray is my only entertainment."
)

OUTPUT_DIR: Path = Path("/output")
OUTPUT_FILE: Path = OUTPUT_DIR / "entry.txt"


def validate_entry(line: str) -> None:
    """Validate entry line strictly against contest constraints."""
    if not (1 <= len(line) <= 240):
        raise ValueError(
            f"Entry must be between 1 and 240 characters; got {len(line)}."
        )
    if any(char in line for char in ("\n", "\r")):
        raise ValueError("Entry must be a single line with no newline inside it.")
    if not line.strip():
        raise ValueError("Entry cannot be empty or purely whitespace.")
    if (line.startswith('"') and line.endswith('"')) or (
        line.startswith("'") and line.endswith("'")
    ):
        raise ValueError("Entry must not have surrounding quotation marks.")


def write_and_verify_entry(line: str, destination: Path) -> Path:
    """Write entry line to destination file, verify write integrity, and return path."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"{line}\n", encoding="utf-8")

    persisted = destination.read_text(encoding="utf-8")
    lines = persisted.splitlines()
    if len(lines) != 1 or lines[0] != line:
        raise IOError(f"Persisted file verification failed at {destination}")
    return destination


def main() -> None:
    """Validate, write and verify /output/entry.txt, and print entry to stdout."""
    validate_entry(ENTRY_LINE)
    write_and_verify_entry(ENTRY_LINE, OUTPUT_FILE)
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
