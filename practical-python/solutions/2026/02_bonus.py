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
def split1(s: str) -> list[str]:
    return s.replace("22", " 22 ").split()


@functools.cache
def split2(s: str) -> list[str]:
    return s.replace("22", " 22").split()


def get_length(s: str, iterations: int) -> int:
    counts = collections.Counter([s])
    for _ in range(iterations):
        counts2 = collections.Counter()
        for s, count in counts.items():
            for part in split1(s):
                counts2[look_and_say(part)] += count
        counts = counts2
    return sum(len(s) * count for s, count in counts.items())


def get_triples(s: str, iterations: int) -> int:
    counts = collections.Counter([s])
    for _ in range(iterations):
        counts2 = collections.Counter()
        for s, count in counts.items():
            for part in split2(s):
                counts2[look_and_say(part)] += count
        counts = counts2
    return sum((s.count("111") + s.count("222")) * count for s, count in counts.items())


def trunc(val: int) -> str:
    s = str(val)
    if len(s) <= 10:
        return s
    return s[:5] + "..." + s[-5:]


t = time.time()
ITERATIONS = 10_000
print(trunc(get_length(open("./input/2026/02/input1.txt").read(), ITERATIONS)))
print(trunc(get_triples(open("./input/2026/02/input2.txt").read(), ITERATIONS)))
print(f"Ran in {time.time() - t}s")
# 76447...55004
# 55205...68778
# Ran in 0.09727859497070312s
