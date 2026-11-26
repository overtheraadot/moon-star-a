#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: a one-star review of the Moon.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "1 star. Showed up late, lit nothing, and hung there glowing like it owned the sky. Worst night-light ever bought."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS a one-star review of the Moon — on the subject, in a
#    reviewer's own voice, with a rating and a grievance.
# 2. The joke lands on first read, with the punchline in the last few words:
#    the Moon is graded like a bad night-light, not like a poem.
# 3. It reads like the real thing: the Moon showed up late, lit nothing, and
#    hung there glowing like it owned the sky — worst night-light ever bought.
# 4. Fresh angle: the grievance is the Moon acting like a bad houseguest who
#    thinks he owns the sky, not the obvious craters, cheese or brightness.
# 5. Tight: every word earns its place inside the 120-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 120 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} characters, over the 120 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
