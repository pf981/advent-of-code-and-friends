import collections
import itertools

with open("./2025/input/everybody_codes_e2025_q20_p3.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """T####T#TTT##T##T#T#
# .T#####TTTT##TTT##.
# ..TTTT#T###TTTT#T..
# ...T#TTT#ETTTT##...
# ....#TT##T#T##T....
# .....#TT####T#.....
# ......T#TT#T#......
# .......T#TTT.......
# ........TT#........
# .........S.........""".splitlines()


def rot120(lines):
    l = list(itertools.zip_longest(*[line.strip(".") for line in lines], fillvalue="."))
    result = []
    for row in l:
        result.append("".join(reversed(row)))

    if len(result) % 2:
        result.append("." * len(result[0]))
    # Interleave row pairs
    result2 = []
    for row1, row2 in itertools.batched(result, 2):
        final_row = []
        for a, b in zip(row1, row2):
            if b != ".":
                final_row.append(b)
            if a != ".":
                final_row.append(a)
        result2.append("".join(final_row))

    # Add back "."
    for r, row in enumerate(result2):
        result2[r] = "." * r + row.strip(".") + "." * r

    return result2


rot120(lines)
rot120(rot120(lines))


pairs = 0
# (r, c) -> (r, c)
ms = []  # Todo: use set, but duplicates shouldn't matter
all_lines = []
lines2 = lines
for _ in range(3):
    nrows = len(lines2)  # FIXME: depends on rotation
    ncols = len(lines2[0])
    all_lines.append(lines2)
    # print("\n".join(lines2))

    m = collections.defaultdict(list)  # (r, c) -> (r, c)
    for r, row in enumerate(lines2):
        # print("." * r + row.strip("."))
        for c, ch in enumerate("." * r + row.strip(".")):
            # if ch not in "EST":
            #     continue

            p1 = (r, c)

            if True:
                # Stay
                m[p1].append(p1)

                # UR
                if True:  # if c + 1 < ncols and True:  # lines2[r][c + 1] in "EST":
                    # print(f"{r=} {c+1=}")
                    pairs += 1
                    p2 = (r, c + 1)
                    m[p1].append(p2)
                    m[p2].append(p1)
                if True:  # if c - 1 >= 0:
                    # print(f"{r=} {c+1=}")
                    pairs += 1
                    p2 = (r, c - 1)
                    m[p1].append(p2)
                    m[p2].append(p1)

                parity = r % 2
                if c % 2 == parity:
                    # if True:
                    # Check parity first
                    if True:  # if r - 1 >= 0 and True:  # lines2[r - 1][c] in "EST":
                        # print(f"{r-1=} {c=}")
                        pairs += 1
                        p2 = (r - 1, c)
                        m[p1].append(p2)
                        m[p2].append(p1)
                else:
                    if True:  # if r + 1 < nrows:
                        p2 = (r + 1, c)
                        m[p1].append(p2)
                        m[p2].append(p1)

    ms.append(m)
    # TODO: Rotate 120 deg
    lines2 = rot120(lines2)

q = collections.deque()  # (r, c)
for r, row in enumerate(lines):  # FIXME: not lines
    for c, ch in enumerate("." * r + row.strip(".")):
        if ch == "S":
            q.append((r, c))
            break
    else:
        continue
    break


def is_valid_square(r, c, rot_index):
    cur_lines = all_lines[rot_index]
    nrows = len(cur_lines)
    ncols = len(cur_lines[0])
    if not (0 <= r < nrows and 0 <= c < ncols):
        return False
    if cur_lines[r][c] not in "EST":
        return False
    return True


def print_state(jumps, r1, c1):
    rot_index = jumps % 3
    cur_lines = all_lines[rot_index]
    nrows = len(cur_lines)
    ncols = len(cur_lines[0])
    print(f"\n({r1}, {c1})\t{jumps=}")
    for r, row in enumerate(cur_lines):
        for c, ch in enumerate(row):
            if (r, c) == (r1, c1):
                ch = "✯"
            print(ch, end="")
        print()
    print()
    print()


def get_nei(r, c):
    result = {(r, c)}
    result.add((r, c + 1))
    result.add((r, c - 1))
    parity = r % 2
    if c % 2 == parity:
        result.add((r - 1, c))
    else:
        result.add((r + 1, c))

    return list(result)


# jumps = 0
# # seen = {(*q[0], 0)}  # r, c, rot_index
# seen_counts = collections.defaultdict(set)

# while q:
#     for _ in range(len(q)):
#         r, c = q.popleft()
#         # print(f"{r=} {c=} {jumps=}")
#         # print_state(jumps, r, c)
#         if all_lines[jumps % 3][r][c] == "E":
#             print("FOUND")
#             print(jumps)
#             break

#         if len(seen_counts[(r, c)]) >= 3:
#             continue
#         seen_counts[(r, c)].add(jumps % 3)

#         # for r2, c2 in ms[jumps % 3][(r, c)]:
#         for r2, c2 in get_nei(r, c):
#             # if (r2, c2, (jumps + 1) % 3) in seen:
#             #     continue
#             # seen.add((r2, c2, (jumps + 1) % 3))

#             if not is_valid_square(r2, c2, (jumps + 1) % 3):
#                 continue

#             q.append((r2, c2))
#     else:
#         jumps += 1
#         continue
#     break


jumps = 0
seen = {(*q[0], 0)}  # r, c, rot_index
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        # print(f"{r=} {c=} {jumps=}")
        # print_state(jumps, r, c)
        if all_lines[jumps % 3][r][c] == "E":
            print("FOUND")
            print(jumps)
            break

        # for r2, c2 in ms[jumps % 3][(r, c)]:
        for r2, c2 in get_nei(r, c):
            if (r2, c2, (jumps + 1) % 3) in seen:
                continue
            seen.add((r2, c2, (jumps + 1) % 3))

            if not is_valid_square(r2, c2, (jumps + 1) % 3):
                continue

            q.append((r2, c2))
    else:
        jumps += 1
        continue
    break

answer = jumps
print(jumps)

# ms[0][(3, 9)]
# ms[0][(3, 8)]
# is_valid_square(3, 7, 2)
# all_lines[2]
# all_lines[2][3][7]
# ms[4 % 3][(7, 10)]

# 214
# Your answer length is: correct
# The first character of your answer is: incorrect

# 114
# Your answer length is: correct
# The first character of your answer is: incorrect

# So at least 300


# for lines2 in all_lines:
#     print(len(lines2), len(lines2[0]))

# for lines2 in all_lines:
#     for r, row in enumerate(lines2):
#         for c, ch in enumerate("." * r + row.strip(".")):
#             if ch == "E":
#                 print((r, c))
#                 break
#         else:
#             continue
#         break
