#!/usr/bin/env python3
"""Long Roast entry: one line roasting the agent itself."""
import os

PART_A = "I read a skill, spawned a subagent, and logged everything, "
PART_B = "just to answer a yes-or-no question."
LINE = PART_A + PART_B
assert len(LINE) <= 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
