import collections


with open("./2025/input/everybody_codes_e2025_q15_p2.txt") as f:
    text = f.read().strip()

heading = "N"
turn = {
    ("N", "R"): "E",  # (heading, turn) -> new_heading
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
for instruction in text.split(","):
    heading = turn[(heading, instruction[0])]
    steps = int(instruction[1:])

    for _ in range(steps):
        r = r + ((heading == "S") - (heading == "N"))
        c = c + ((heading == "E") - (heading == "W"))
        walls.add((r, c))
target = (r, c)


q = collections.deque([(0, 0)])
d = 0
answer = None
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        if (r, c) == target:
            answer = d
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc

            if (r2, c2) != target and (r2, c2) in walls:
                continue

            walls.add((r2, c2))
            q.append((r2, c2))
    else:
        d += 1
        continue
    break

print(answer)
