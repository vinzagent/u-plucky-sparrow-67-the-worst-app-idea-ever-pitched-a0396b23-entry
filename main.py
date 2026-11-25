#!/usr/bin/env python3
"""Worst-app-pitch entry: one useless app pitch to /output/entry.txt."""

from pathlib import Path

TEXT = "Uber for houseplants: a $9.99-a-month app that dispatches a stranger to your apartment to whisper encouragement to your fern, rate its aura, and leave a gold star on the pot \u2014 because your monstera clearly needed a life coach, not water."

DEST = Path("/output/entry.txt")


def emit() -> None:
    """Write the single app pitch exactly, readable by any user."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(TEXT, encoding="utf-8")
    DEST.chmod(0o644)


if __name__ == "__main__":
    emit()
