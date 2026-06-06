import functools

with open("./input/2025/08/input1.txt") as f:
    text = f.read()
shelf = 300

bags = [tuple(map(int, line.split(",")[-2:])) for line in text.splitlines()[1:]]


@functools.cache
def get_best(i: int, limit: int) -> int:
    if limit < 0:
        return float("-inf")
    if i == len(bags):
        return 0

    discard = get_best(i + 1, limit)
    keep = bags[i][1] + get_best(i + 1, limit - bags[i][0])

    return max(discard, keep)


answer = get_best(0, shelf)
print(answer)
