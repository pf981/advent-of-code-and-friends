with open("./input/2026/05.txt") as f:
    lines = f.read().splitlines()

seen = set()
r, c = 0, 0
while (r, c) not in seen:
    seen.add((r, c))
    ch = lines[r][c]
    r += (ch == "v") - (ch == "^")
    c += (ch == ">") - (ch == "<")

answer = len(seen)
print(answer)
