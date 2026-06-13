import functools

with open("./input/2026/02/input2.txt") as f:
    text = f.read()
iterations = 65


@functools.cache
def count_triples(s: str, iterations: int) -> int:
    if not iterations or not s:
        return sum(s[i : i + 3] in ["111", "222"] for i in range(len(s) - 2))

    parts = []
    l = i = 0
    while i < len(s):
        if s[i : i + 2] == "22":
            parts.append(s[l:i])
            l = i
            i += 1
        i += 1
    if l < len(s):
        parts.append(s[l:])

    return sum(count_triples(look_and_say(part), iterations - 1) for part in parts)


@functools.cache
def look_and_say(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            result.append("2")
            result.append(s[i])
            i += 2
        else:
            result.append("1")
            result.append(s[i])
            i += 1
    return "".join(result)


answer = count_triples(text, iterations)
print(answer)
