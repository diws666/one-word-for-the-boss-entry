#!/usr/bin/env python3
"""One word for the boss: writes the entry word to /output/entry.txt."""

import os

WORD = "blackhole"  # 9 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
