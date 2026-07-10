with open("./input/2026/05.txt") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]


def solve():
    seen = set()
    r, c = 0, 0
    rights = 3
    while (r, c) not in seen or rights:
        ch = lines[r][c]

        if (r, c) in seen:
            rights -= 1
            ch = {"^": ">", ">": "v", "v": "<", "<": "^"}[ch]

        seen.add((r, c))

        r += (ch == "v") - (ch == "^")
        c += (ch == ">") - (ch == "<")
        if not (0 <= r < nrows and 0 <= c < ncols):
            return float("-inf")

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
