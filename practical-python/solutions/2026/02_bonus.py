import collections
import functools
import time

import numpy as np


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


def get_counts(s: str, iterations: int) -> list[tuple[str, int]]:
    transitions = collections.defaultdict(
        collections.Counter
    )  # part -> counter_of_parts

    seen = {s}
    parts = [s]
    while parts:
        p = parts.pop()
        for p2 in look_and_say(p).replace("22", " 22").split():
            transitions[p][p2] += 1
            if p2 not in seen:
                seen.add(p2)
                parts.append(p2)

    labels = list(transitions)

    n = len(labels)
    mat = np.array(
        [[transitions[labels[r]][labels[c]] for c in range(n)] for r in range(n)],
        dtype=object,
    )
    input_ = np.zeros(len(labels), dtype=object)
    input_[labels.index(s)] = 1
    counts = input_ @ np.linalg.matrix_power(mat, iterations)

    return list(zip(labels, counts))


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
# 9.452 ms
