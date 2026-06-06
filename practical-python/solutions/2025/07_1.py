import collections
import itertools

with open("./input/2025/07/input1.txt") as f:
    text = f.read()

counts = collections.Counter(itertools.batched(text, 4))
targets = [1081, 1055, 965]
result = [
    "".join(next(code for code in counts if counts[code] == target))
    for target in targets
]

answer = "".join(result)
print(answer)
