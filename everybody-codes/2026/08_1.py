with open("./2026/input/everybody_codes_e2026_q08_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """....1.9.6.1.7....
# ...9.2.3.3.8.1...
# ..7.8.3.5.1.4.3..
# .4.6.7.4.1.1.8.9.
# 4.5.3.6.5.8.9.4.9
# .9.5.1.5.6.2.8.9.
# ..7.7.6.4.6.2.4..
# ...9.3.8.3.8.4...
# ....1.6.6.2.8....""".splitlines()

nrows = len(lines)
ncols = len(lines[0])
ents = {
    (r, c): int(ch)
    for r, line in enumerate(lines)
    for c, ch in enumerate(line)
    if ch.isdigit()
}

stack = []  # [(r, c, shadow), ...]
for c in range(ncols):
    if (0, c) in ents:
        stack.append((0, c, 0))
for r in range(1, nrows // 2 + 1):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0))

# print()
answer = 0
while stack:
    r, c, shadow = stack.pop()
    # print(f"{r, c, shadow}")

    if (r, c) not in ents:
        continue

    if ents[(r, c)] > shadow:
        # print(f"{r=} {c=} {ents[(r,c)]=}")
        shadow = ents[(r, c)]
        answer += 1

    stack.append((r + 1, c + 1, shadow - 1))

print(answer)
