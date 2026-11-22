"""Count exact repeated lines while preserving their first-seen order."""
import argparse
from collections import Counter
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('file', type=Path)
a = p.parse_args()

lines = a.file.read_text(encoding='utf-8').splitlines()
for line, count in Counter(lines).items():
    if count > 1:
        print(f'{count}\t{line}')
