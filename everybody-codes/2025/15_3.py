with open("./2025/input/everybody_codes_e2025_q15_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3""".splitlines()

heading = "N"
turn = {
    ("N", "R"): "E",  # from, turn -> to
    ("N", "L"): "W",
    ("E", "R"): "S",
    ("E", "L"): "N",
    ("S", "R"): "W",
    ("S", "L"): "E",
    ("W", "R"): "N",
    ("W", "L"): "S",
}

r = 0
c = 0
walls = set()
for a, *b in lines[0].split(","):
    b = int("".join(b))
    heading = turn[(heading, a)]

    for _ in range(b):
        r = r + ((heading == "S") - (heading == "N"))
        c = c + ((heading == "E") - (heading == "W"))
        walls.add((r, c))
target = (r, c)


for r in range(-30, 20):
    for c in range(-30, 20):
        ch = "#" if (r, c) in walls else "."
        if (r, c) == target:
            ch = "E"
        if (r, c) == (0, 0):
            ch = "S"
        print(ch, end="")
    print()

#     print(f"{r=} {c=}")
# print(r, c)

# answer = "TODO"
# print(answer)

import collections

q = collections.deque([(0, 0)])
d = 0
answer = None
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        # print(f"{r=} {c=}")
        if (r, c) == target:
            answer = d
            # print(f"{answer=}")
            break
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            # print(f"{r2, c2}")
            if (r2, c2) != target and (r2, c2) in walls:
                continue
            walls.add((r2, c2))
            q.append((r2, c2))
    else:
        d += 1
        continue
    break

print(answer)

# 105

# Your answer length is: correct
# The first character of your answer is: correct
