import collections

with open("./input/2026/05.txt") as f:
    lines = f.read().splitlines()
lines = [list(line) for line in lines]


def solve():
    seen = collections.Counter()
    r, c = 0, 0
    illegal_turns = 3
    while illegal_turns and seen[(r, c)] < 3:
        ch = lines[r][c]

        if seen[(r, c)]:
            ch = {"^": ">", ">": "v", "v": "<", "<": "^"}[ch]
            illegal_turns -= 1

        seen[(r, c)] += 1

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
