import functools

with open("./input/2026/09/input2.txt") as f:
    text = f.read()

colors = [part.split(":")[1] for part in text.split(",")]


@functools.cache
def count_ways(i: int, used: int) -> int:
    if i == len(colors):
        return 1

    ways = 0
    for j in range(len(colors)):
        if used & (1 << j) or colors[j] == colors[i]:
            continue
        ways += count_ways(i + 1, used | (1 << j))
    return ways


answer = count_ways(0, 0)
print(answer)
