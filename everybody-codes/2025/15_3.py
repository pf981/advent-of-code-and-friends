import heapq


with open("./2025/input/everybody_codes_e2025_q15_p3.txt") as f:
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

r = c = 0
segments: list[tuple[int, int, int, int]] = []  # [(r1, c1, r2, c2), ...]
interesting_r = [-1, 0, 1]
interesting_c = [-1, 0, 1]

for instruction in text.split(","):
    heading = turn[(heading, instruction[0])]
    steps = int(instruction[1:])

    r2 = r + ((heading == "S") - (heading == "N")) * steps
    c2 = c + ((heading == "E") - (heading == "W")) * steps

    segments.append((r, c, r2, c2))

    interesting_r.extend([r2 - 1, r2, r2 + 1])
    interesting_c.extend([c2 - 1, c2, c2 + 1])

    r, c = r2, c2


end = (r, c)
start = (0, 0)

interesting_r = sorted(set(interesting_r))
interesting_c = sorted(set(interesting_c))

vertical_walls: dict[int, list[tuple[int, int]]] = {}  # c -> {(r1, r2), ...}
horizontal_walls: dict[int, list[tuple[int, int]]] = {}  # r -> {(c1, c2), ...}

for r1, c1, r2, c2 in segments:
    if c1 == c2:
        if c1 not in vertical_walls:
            vertical_walls[c1] = []
        vertical_walls[c1].append((min(r1, r2), max(r1, r2)))
    else:
        if r1 not in horizontal_walls:
            horizontal_walls[r1] = []
        horizontal_walls[r1].append((min(c1, c2), max(c1, c2)))


def is_on_wall(r: int, c: int) -> bool:
    if (r, c) in [start, end]:
        return False

    if c in vertical_walls:
        for r1, r2 in vertical_walls[c]:
            if r1 <= r <= r2:
                return True

    if r in horizontal_walls:
        for c1, c2 in horizontal_walls[r]:
            if c1 <= c <= c2:
                return True

    return False


start_i_r = interesting_r.index(start[0])
start_i_c = interesting_c.index(start[1])
end_i_r = interesting_r.index(end[0])
end_i_c = interesting_c.index(end[1])

heap = [(0, start_i_r, start_i_c)]  # [(d, i_r, i_c), ...)

visited = set()
answer = None

while heap:
    d, i_r, i_c = heapq.heappop(heap)

    if (i_r, i_c) == (end_i_r, end_i_c):
        answer = d
        break

    if (i_r, i_c) in visited:
        continue
    visited.add((i_r, i_c))

    r = interesting_r[i_r]
    c = interesting_c[i_c]

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        i_r2 = i_r + dr
        i_c2 = i_c + dc

        if not (0 <= i_r2 < len(interesting_r) and 0 <= i_c2 < len(interesting_c)):
            continue

        if (i_r2, i_c2) in visited:
            continue

        r2 = interesting_r[i_r2]
        c2 = interesting_c[i_c2]

        if is_on_wall(r2, c2):
            continue

        d2 = d + abs(r2 - r) + abs(c2 - c)

        heapq.heappush(heap, (d2, i_r2, i_c2))

assert answer is not None
print(answer)
