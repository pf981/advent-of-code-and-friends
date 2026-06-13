import functools

with open("./input/2026/02/input1.txt") as f:
    text = f.read()
iterations = 65

# text = "121"
# iterations = 10

# parts = []
# l = 0
# s = text
# for i in range(len(s)):
#     if s[i : i + 2] == "22":
#         parts.append(s[l : i + 1])
#         l = i + 1
# if l < len(s):
#     parts.append(s[l:])


@functools.cache
def get_length(s: str, iterations: int) -> int:
    # print(f"{s=} {iterations=}")
    if not iterations or not s:
        return len(s)

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
    # print(f"{parts=}")

    return sum(get_length(look_and_say(part), iterations - 1) for part in parts)


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


answer = get_length(text, iterations)
print(answer)
