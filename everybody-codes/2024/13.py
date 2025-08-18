import heapq


def solve(lines: list[str]) -> int:
    m = {}
    heap = []
    end = None # r, c
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c in '# ':
                continue
            if c == 'S':
                heap.append((0, row, col))
                m[(row, col)] = 0
            elif c == 'E':
                end = row, col
                m[(row, col)] = 0
            else:
                m[(row, col)] = int(c)

    seen = set()
    while heap:
        d, r, c = heapq.heappop(heap)

        if (r, c) == end:
            return d

        if (r, c) in seen:
            continue
        seen.add((r, c))

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) not in m:
                continue
            d2 = min(
                abs(m[(r, c)] - m[(r2, c2)]),
                abs(m[(r, c)] - m[(r2, c2)] - 10),
                abs(m[(r, c)] - m[(r2, c2)] + 10)
            )
            heapq.heappush(heap, (1 + d + d2, r2, c2))


with open("./2024/input/everybody_codes_e2024_q13_p1.txt") as f:
    lines = f.read().splitlines()

answer1 = solve(lines)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q13_p2.txt") as f:
    lines = f.read().splitlines()

answer2 = solve(lines)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q13_p3.txt") as f:
    lines = f.read().splitlines()

answer3 = solve(lines)
print(answer3)
