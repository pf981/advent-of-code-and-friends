def merge(groups: list[tuple[str, int]]) -> list[tuple[str, int]]:
    stack = [groups[0]]
    for ch, length in groups:
        if ch == stack[-1][0]:
            length += stack.pop()[1]
        stack.append([ch, length])
    return stack


with open("./2026/input/everybody_codes_e2026_q16_p1.txt") as f:
    text = f.read().strip()

groups = []  # [(ch, length), ...]
streak = 0
prev = text[0]
for ch in text:
    if ch == prev:
        streak += 1
        continue
    groups.append((prev, streak))
    streak = 1
    prev = ch
groups.append((prev, streak))

n_colors = len({ch for ch, _ in groups})
flips = 0
while len(groups) != n_colors:
    for first in range(len(groups)):
        ch = groups[first][0]
        last = next(i for i in reversed(range(len(groups))) if groups[i][0] == ch)
        if first != last:
            break

    assert first != last
    groups = groups[: first + 1] + groups[first + 1 : last][::-1] + groups[last + 1 :]
    groups = merge(groups)

    flips += 1

answer = flips
print(answer)
