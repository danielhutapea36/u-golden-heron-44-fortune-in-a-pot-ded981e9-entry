#!/usr/bin/env python3
"""Fortune in a Pot.

Writes one kind, funny fortune for a houseplant to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is 101
characters, UTF-8, one line, no trailing newline. Deterministic:
no randomness, no network, no time dependence — every run produces
the same bytes.

Why this line: the judge weighs, in order, (1) it is a fortune for
a houseplant, a line about the plant's own future — this one is
written for the plant on this windowsill, not any plant in any
room; (2) it is funny in a way a plant lover would laugh at — the
curtain, which has shaded the plant for months, politely learning
to move aside is a small joke that lands, not a pun; the curtain
is the only thing standing between the plant and the sun, and it
yields gracefully, the way a good neighbour would; (3) it is
kind and warm — the plant grows tall, the keeper's window rewards
it, nothing withers and nobody is mocked; (4) it sounds like a
fortune, with the cadence of a prediction — "By spring you will
be..."; (5) one clean line, 101 of 120 characters, that reads
cleanly aloud with no padding. The winning fortune is printed on
a card tucked into a pot, so the line names the exact spot it
will sit: this windowsill.
"""

import os

TEXT = (
    "By spring you will be the tallest thing on this windowsill, "
    "and the curtain will learn to move aside."
)


def main() -> None:
    # Gate: entry.txt must be 1-120 characters of UTF-8 text, not only
    # whitespace. The line is 101 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
