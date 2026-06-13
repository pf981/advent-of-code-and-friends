# Based off caelum.intra's solution in Mathematics Discord
import collections
import functools
import time


@functools.cache
def look_and_say(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            result.append("2" + s[i])
            i += 2
        else:
            result.append("1" + s[i])
            i += 1

    return "".join(result)


@functools.cache
def get_counts(s: str, iterations: int) -> tuple[tuple[str, int], ...]:
    if not iterations:
        return ((s, 1),)
    if iterations == 1:
        return tuple(
            collections.Counter(look_and_say(s).replace("22", " 22").split()).items()
        )

    counts = collections.Counter()
    for p, count in get_counts(s, iterations // 2):
        for p2, count2 in get_counts(p, iterations - iterations // 2):
            counts[p2] += count * count2
    return tuple(counts.items())


def get_length(s: str, iterations: int) -> int:
    return sum(len(label) * count for label, count in get_counts(s, iterations))


def get_triples(s: str, iterations: int) -> int:
    return sum(
        (label.count("111") + label.count("222")) * count
        for label, count in get_counts(s, iterations)
    )


def trunc(val: int) -> str:
    s = str(val)
    if len(s) <= 10:
        return s
    return s[:5] + "..." + s[-5:]


with open("./input/2026/02/input1.txt") as f:
    in1 = f.read()
with open("./input/2026/02/input2.txt") as f:
    in2 = f.read()

t0 = time.perf_counter()
ITERATIONS = 10_000
print(trunc(get_length(in1, ITERATIONS)))
print(trunc(get_triples(in2, ITERATIONS)))
print(f"{(time.perf_counter() - t0) * 1000:.3f} ms")
# 76447...55004
# 55205...68778
# 3.476 ms
