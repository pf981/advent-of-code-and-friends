import functools

with open("./input/2026/09/input2.txt") as f:
    text = f.read()

colors = [part.split(":")[1] for part in text.split(",")]


@functools.cache
def count_ways(i: int, used: frozenset[int]) -> int:
    if i == len(colors):
        return 1

    ways = 0
    for j in range(len(colors)):
        if j in used or colors[j] == colors[i]:
            continue
        ways += count_ways(i + 1, used | {j})
    return ways


answer = count_ways(0, frozenset())
print(answer)
