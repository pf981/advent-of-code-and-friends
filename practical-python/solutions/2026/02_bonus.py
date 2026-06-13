import functools
import time


@functools.cache
def get_length(s: str, iterations: int) -> int:
    if not iterations or not s:
        return len(s)

    parts = s.replace("22", " 22").split()

    return sum(get_length(look_and_say(part), iterations - 1) for part in parts)


@functools.cache
def count_triples(s: str, iterations: int) -> int:
    if not iterations or not s:
        return s.count("111") + s.count("222")

    parts = s.replace("22", " 22").split()

    return sum(count_triples(look_and_say(part), iterations - 1) for part in parts)


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


t = time.time()
print(get_length(open("./input/2026/02/input1.txt").read(), 65))
print(count_triples(open("./input/2026/02/input2.txt").read(), 65))
print(f"Ran in {time.time() - t}s")
# Ran in 0.0015673637390136719s
