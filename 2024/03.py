import collections


def count_blocks(lines: list[str], directions: list[tuple]) -> int:
    nrows = len(lines)
    ncols = len(lines[0])
    seen = set()

    q = collections.deque()
    for r in range(nrows):
        for c in range(ncols):
            if lines[r][c] == '.':
                seen.add((r, c))
                q.append((r, c))

    
    for r in range(nrows):
        q.append((r, -1))
        q.append((r, ncols))
    for c in range(ncols):
        q.append((-1, c))
        q.append((nrows, c))

    d = 0
    blocks = 0
    while q:
        blocks += d * len(q)
        for _ in  range(len(q)):
            r, c = q.popleft()
            
            for dr, dc in directions:
                r2 = r + dr
                c2 = c + dc
                if (r2, c2) in seen or not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
                    continue
                seen.add((r2, c2))
                q.append((r2, c2))
        d += 1
    
    return blocks


with open("./2024/input/everybody_codes_e2024_q03_p1.txt") as f:
    lines = f.read().splitlines()

answer1 = count_blocks(lines, [(-1, 0), (0, -1), (0, 1), (1, 0)])
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q03_p2.txt") as f:
    lines = f.read().splitlines()

answer2 = count_blocks(lines, [(-1, 0), (0, -1), (0, 1), (1, 0)])
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q03_p3.txt") as f:
    lines = f.read().splitlines()

answer3 = count_blocks(lines, [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
print(answer3)
