import collections


def shortest_path(lines: list[str]) -> int:
    start_r = 0
    start_c = lines[0].index('.')

    to_collect = tuple(sorted({ch for line in lines for ch in line if ch not in '#.~'}))

    q = collections.deque([(start_r, start_c, tuple())])
    d = 0
    seen = {(start_r, start_c)}
    while q:
        # Prune
        if len(q) >= 15000:
            q = list(q)
            q.sort(key=lambda state: -10000*len(state[2]) + state[0])
            q = collections.deque(q[:2000])

        for _ in range(len(q)):
            r, c, collected = q.popleft()

            if collected == to_collect and (r, c) == (0, start_c):
                return d
                
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc
                if r2 < 0 or lines[r2][c2] in '#~' or (r2, c2, collected) in seen:
                    continue
                
                new_collected = collected
                if lines[r2][c2] != '.' and lines[r2][c2] not in collected:
                    new_collected = tuple(sorted(collected + (lines[r2][c2],)))

                seen.add((r2, c2, new_collected))
                q.append((r2, c2, new_collected))
        d += 1


with open("./2024/input/everybody_codes_e2024_q15_p1.txt") as f:
    lines = f.read().splitlines()

answer1 = shortest_path(lines)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q15_p2.txt") as f:
    lines = f.read().splitlines()

answer2 = shortest_path(lines)
print(answer2)



# Part 3


with open("./2024/input/everybody_codes_e2024_q15_p3.txt") as f:
    lines = f.read().splitlines()

answer3 = shortest_path(lines)
print(answer3)
