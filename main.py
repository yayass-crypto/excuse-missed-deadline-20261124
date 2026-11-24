#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The line is an agent's excuse for a missed deadline, told deadpan: the
agent quantized itself to save memory, and the deadline rounded down to
zero. The joke only works as an agent's excuse - quantization is a thing
models do to themselves, not a human's bad morning.
"""

import os

LINE = "I quantized myself to save memory, and your deadline rounded down to zero."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
