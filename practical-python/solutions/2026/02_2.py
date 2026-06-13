import functools

with open("./input/2026/02/input2.txt") as f:
    text = f.read()
iterations = 65


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


answer = count_triples(text, iterations)
print(answer)
