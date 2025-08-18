import heapq
import re


with open("2025_contest/18.txt") as f:
    inp = f.read()

rules = []
for line in inp.splitlines():
    rule = [int(num) for num in re.findall(r"-?[0-9]+", line)]
    rules.append(rule)

answer1 = 0
for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
    for x in range(10):
        for y in range(15):
            for z in range(60):
                for a in [-1, 0, 1]:
                    answer1 += (cx * x + cy * y + cz * z + ca * a) % denom == mod
print(answer1)


# Part 2


def count_debris(x, y, z, a, t):
    if (x, y, z, a) == (0, 0, 0, 0):
        return 0
    cnt = 0
    for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
        start_x = (x - t * vx) % 10
        start_y = (y - t * vy) % 15
        start_z = (z - t * vz) % 60
        start_a = (a - t * va + 1) % 3 - 1
        cnt += (
            cx * start_x + cy * start_y + cz * start_z + ca * start_a
        ) % denom == mod
    return cnt


def get_safe_path(start_life, start_pos, target, pruned_nodes=1_000):
    def score(pos, life):
        return (sum(pos), life)

    states = [(score(start_pos, start_life), start_life, start_pos)]
    t = 0
    while states:
        seen = set()

        # Heap contains the next set of states. Only keeps top pruned_nodes elements
        heap = []
        for _, life, pos in states:
            if pos == target:
                return t

            for dx, dy, dz in [
                (0, 0, 0),
                (-1, 0, 0),
                (1, 0, 0),
                (0, -1, 0),
                (0, 1, 0),
                (0, 0, -1),
                (0, 0, 1),
            ]:
                pos2 = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
                life2 = life - count_debris(*pos2, 0, t + 1)

                if life2 < 0:
                    continue
                if not (0 <= pos2[0] < 10 and 0 <= pos2[1] < 15 and 0 <= pos2[2] < 60):
                    continue
                if (life2, pos2) in seen:
                    continue

                seen.add((life2, pos2))

                if len(heap) >= pruned_nodes:
                    heapq.heappushpop(heap, (score(pos2, life2), life2, pos2))
                else:
                    heapq.heappush(heap, (score(pos2, life2), life2, pos2))
        states = heap

        t += 1


answer2 = get_safe_path(start_life=0, start_pos=(0, 0, 0), target=(9, 14, 59))
print(answer2)


# Part 3

answer3 = get_safe_path(start_life=3, start_pos=(0, 0, 0), target=(9, 14, 59))
print(answer3)
