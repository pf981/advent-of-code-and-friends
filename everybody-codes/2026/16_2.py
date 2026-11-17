with open("./2026/input/everybody_codes_e2026_q16_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """RRYGYBYG""".splitlines()
COPIES = 10

groups = []  # [(ch, length), ...]

assert len(lines) == 1
streak = 0
prev = lines[0][0]
for ch in lines[0] * COPIES:
    if ch == prev:
        streak += 1
        continue

    groups.append([prev, streak])
    streak = 1
    prev = ch
groups.append([prev, streak])


def merge(groups):
    stack = [groups[0]]
    for ch, length in groups:
        if ch == stack[-1][0]:
            stack[-1][1] += length
        else:
            stack.append([ch, length])
    return stack


shades = {ch for ch, _ in groups}
flips = 0
while len(groups) != len(shades):
    # print(f"{flips=} {groups=}")
    for first in range(len(groups)):
        ch = groups[first][0]
        last = next(i for i in reversed(range(len(groups))) if groups[i][0] == ch)
        if first != last:
            break
    assert first != last

    flips += sum(length for _, length in groups[first + 1 : last + 1])

    groups = (
        groups[:first]
        + [[groups[first][0], groups[first][1] + groups[last][1]]]
        + groups[first + 1 : last][::-1]
        + groups[last + 1 :]
    )
    groups = merge(groups)


answer = flips
print(answer)
