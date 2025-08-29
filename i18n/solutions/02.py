import collections
from datetime import datetime, timezone

with open("./input/02.txt", encoding="utf-8") as f:
    text = f.read()

counts: collections.Counter[str] = collections.Counter()
for line in text.splitlines():
    utc = datetime.fromisoformat(line).astimezone(timezone.utc)
    counts[utc.isoformat()] += 1

answer = next(dt for dt, count in counts.items() if count == 4)
print(answer)
