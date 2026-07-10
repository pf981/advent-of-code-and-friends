with open("./input/2026/05.txt") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]


def solve():
    seen = set()
    r, c = 0, 0
    while (r, c) not in seen:
        seen.add((r, c))
        ch = lines[r][c]
        r += (ch == "v") - (ch == "^")
        c += (ch == ">") - (ch == "<")

        # r...
    return len(seen)


answer = 0
nrows = len(lines)
ncols = len(lines[0])
for r in range(1, nrows - 1):
    for c in range(1, ncols - 1):
        original = lines[r][c]
        for ch in "^>v<":
            if ch == original:
                continue
            lines[r][c] = ch
            answer = max(answer, solve())
        lines[r][c] = original

print(answer)
