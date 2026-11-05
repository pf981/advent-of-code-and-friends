with open("./2026/input/everybody_codes_e2026_q08_p2.txt") as f:
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


def process(stack: list[tuple[int, int, int, int, int]]) -> int:
    requires_energy = set()  # {(r, c), ...}

    # FIXME: Hack to remove duplicates
    stack = list(set(stack))

    while stack:
        r, c, shadow, dr, dc = stack.pop()

        # if (r, c) not in ents:
        #     continue
        if not (0 <= r < nrows and 0 <= c < ncols):
            continue

        if (r, c) in ents and ents[(r, c)] > shadow:
            shadow = ents[(r, c)]
            requires_energy.add((r, c))

        stack.append((r + dr, c + dc, shadow - 1, dr, dc))

    for r in range(nrows):
        for c in range(ncols):
            ch = "."
            if (r, c) in requires_energy:
                ch = lines[r][c]
            print(ch, end="")
        print()
    print(f"{len(requires_energy)}")
    return len(requires_energy)


answer = 0
# TODO: Consider duplicates

# \>
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    if (0, c) in ents:
        stack.append((0, c, 0, 1, 1))
for r in range(1, nrows // 2 + 1):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, 1, 1))
answer += process(stack)

# </
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    if (0, c) in ents:
        stack.append((0, c, 0, 1, -1))
for r in range(1, nrows // 2 + 1):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, 1, -1))
answer += process(stack)

# <-
stack = []  # [(r, c, shadow, dr, dc), ...]
for r in range(nrows):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, 0, -2))
answer += process(stack)

# <\
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    r = nrows - 1
    if (r, c) in ents:
        stack.append((r, c, 0, -1, -1))
for r in range(nrows // 2, nrows - 1):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, -1, -1))
answer += process(stack)

# />
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    r = nrows - 1
    if (r, c) in ents:
        stack.append((r, c, 0, -1, 1))
for r in range(nrows // 2, nrows - 1):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, -1, 1))
answer += process(stack)

# ->
stack = []  # [(r, c, shadow, dr, dc), ...]
for r in range(nrows):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, 0, 2))
answer += process(stack)

print(answer)
