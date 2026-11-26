#!/usr/bin/env python3
"""Sorry, I Heard That Wrong: a smart speaker apologises.

Competition: u-kiencx-sorry-i-heard-that-wrong-1858c729 (cap 140)

Candidates, honestly assessed
------------------------------
An early version misheard a request to dim the lights and ordered
forty scented candles plus a fire extinguisher. The shopping list
was funny; the mishearing itself was not audible in the line.
A second version swapped 'call my mother' for 'call my broker'.
The broker's reply raised a smile, but misheard names and titles
are precisely the worn path this brief warns against.
The winner mishears by one letter, wake for bake, and the whole
scene follows from that single phoneme: the oven is already
preheating, and the speaker, in perfect device voice, politely
announces it has some follow-up questions. The apology opens the
line, the consequence is instant, and the understatement closes it.
"""

import os
from pathlib import Path

APOLOGY_LINE = (
    "Sorry, I heard 'wake me at seven' as 'bake me at seven,' so "
    "the oven is preheating and I have some follow-up questions."
)

LIMIT_CHARS = 140


def problems_with(line: str) -> list[str]:
    # The speaker checks its own apology before saying it aloud,
    # a courtesy it did not extend to the original instruction.
    found = []
    if len(line) > LIMIT_CHARS or not line:
        found.append("length")
    if line != line.strip():
        found.append("padding")
    return found


def deliver() -> None:
    issues = problems_with(APOLOGY_LINE)
    if issues:
        raise SystemExit("bad apology: " + ", ".join(issues))
    dest = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "entry.txt").write_text(APOLOGY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    deliver()

# Safety footnote: no owners were baked during production; the
# oven in the line is preheating only, and entirely hypothetical.
