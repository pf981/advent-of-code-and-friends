import collections

with open("./2025/input/everybody_codes_e2025_q20_p2.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """TTTTTTTTTTTTTTTTT
# .TTTT#T#T#TTTTTT.
# ..TT#TTTETT#TTT..
# ...TT#T#TTT#TT...
# ....TTT#T#TTT....
# .....TTTTTT#.....
# ......TT#TT......
# .......#TT.......
# ........S........""".splitlines()

nrows = len(lines)
ncols = len(lines[0])

pairs = 0
m = collections.defaultdict(list)  # (r, c) -> (r, c)
for r, row in enumerate(lines):
    # print("." * r + row.strip("."))
    for c, ch in enumerate("." * r + row.strip(".")):
        if ch not in "EST":
            continue

        p1 = (r, c)

        # if r % 2 == 0:
        #     # R
        #     if c + 1 < ncols and lines[r][c + 1] == "T":
        #         print(f"{r=} {c+1=}")
        #         pairs += 1
        # else:
        if True:
            # UR
            if c + 1 < ncols and lines[r][c + 1] in "EST":
                # print(f"{r=} {c+1=}")
                pairs += 1
                p2 = (r, c + 1)
                m[p1].append(p2)
                m[p2].append(p1)

            parity = r % 2
            if c % 2 == parity:
                # if True:
                # Check parity first
                if r - 1 >= 0 and lines[r - 1][c] in "EST":
                    # print(f"{r-1=} {c=}")
                    pairs += 1
                    p2 = (r - 1, c)
                    m[p1].append(p2)
                    m[p2].append(p1)


q = collections.deque()
# for c in range(ncols):
#     if lines[0][c] != "T":
#         continue
#     q.append((0, c))
for r, row in enumerate(lines):
    for c, ch in enumerate("." * r + row.strip(".")):
        if ch == "E":
            q.append((r, c))
            break
    else:
        continue
    break


jumps = 0
seen = set(q)
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        # print(f"{r=} {c=}")
        if lines[r][c] == "S":
            print("FOUND")
            print(jumps)
            break

        for r2, c2 in m[(r, c)]:
            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    else:
        jumps += 1
        continue
    break

answer = jumps
print(jumps)
