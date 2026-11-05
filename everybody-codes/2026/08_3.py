import itertools

with open("./2026/input/everybody_codes_e2026_q08_p3.txt") as f:
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
TARGET = 100000

nrows = len(lines)
ncols = len(lines[0])
ents = {
    (r, c): int(ch)
    for r, line in enumerate(lines)
    for c, ch in enumerate(line)
    if ch.isdigit()
}

growing_d1 = set()  # {(r, c), ...}
growing_d2 = set()  # {(r, c), ...}
growing_d3 = set()  # {(r, c), ...}


def process(round_index: int) -> tuple[int, int]:
    global growing_d1, growing_d2, growing_d3
    requires_energy = set()  # {(r, c), ...}
    warriors = energy = 0

    # FIXME: Hack to remove duplicates
    stack = round_stacks[round_index % len(round_stacks)].copy()
    growing = set()

    while stack:
        r, c, shadow, dr, dc = stack.pop()
        shadow = max(shadow, 0)

        # if (r, c) not in ents:
        #     continue
        if not (0 <= r < nrows and 0 <= c < ncols):
            continue

        if (r, c) in ents and ents[(r, c)] > shadow:
            assert ents[(r, c)] > 0
            shadow = ents[(r, c)]
            requires_energy.add((r, c))
            energy += 1
            ents[(r, c)] += 1  # TODO: Confirm this is in correct place

            if ents[(r, c)] == 10:
                warriors += 1
                ents[(r, c)] = 0
                growing.add((r, c))

        stack.append((r + dr, c + dc, shadow - 1, dr, dc))

    # Grow
    for r, c in growing_d3:
        assert ents[(r, c)] == 0
        ents[(r, c)] += 1

    growing_d1, growing_d2, growing_d3 = growing, growing_d1, growing_d2

    # for r in range(nrows):
    #     for c in range(ncols):
    #         ch = "."
    #         if (r, c) in requires_energy:
    #             ch = str(ents[(r, c)])
    #         if (r, c) in ents and ents[(r, c)] == 0:
    #             ch = "X"
    #         print(ch, end="")
    #     print()
    # print(f"{energy=} {warriors=}\n\n")
    return (energy, warriors)


answer = 0

round_stacks = []

# \>
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    if (0, c) in ents:
        stack.append((0, c, 0, 1, 1))
for r in range(1, nrows // 2 + 1):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, 1, 1))
round_stacks.append(stack)

# </
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    if (0, c) in ents:
        stack.append((0, c, 0, 1, -1))
for r in range(1, nrows // 2 + 1):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, 1, -1))
round_stacks.append(stack)

# <-
stack = []  # [(r, c, shadow, dr, dc), ...]
for r in range(nrows):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, 0, -2))
round_stacks.append(stack)

# <\
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    r = nrows - 1
    if (r, c) in ents:
        stack.append((r, c, 0, -1, -1))
for r in range(nrows // 2, nrows - 1):
    c = next(c for c in reversed(range(ncols)) if (r, c) in ents)
    stack.append((r, c, 0, -1, -1))
round_stacks.append(stack)

# />
stack = []  # [(r, c, shadow, dr, dc), ...]
for c in range(ncols):
    r = nrows - 1
    if (r, c) in ents:
        stack.append((r, c, 0, -1, 1))
for r in range(nrows // 2, nrows - 1):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, -1, 1))
round_stacks.append(stack)

# ->
stack = []  # [(r, c, shadow, dr, dc), ...]
for r in range(nrows):
    c = next(c for c in range(ncols) if (r, c) in ents)
    stack.append((r, c, 0, 0, 2))
round_stacks.append(stack)


# FIXME: Duplicates check
for i in range(len(round_stacks)):
    assert len(round_stacks[i]) == len(set(round_stacks[i]))
    # round_stacks[i] = list(set(round_stacks[i]))

warriors = energy = 0
# for i in range(10):
for i in itertools.count():
    e, w = process(i)
    energy += e
    warriors += w
    if warriors >= TARGET:
        break

answer = energy
print(answer)
