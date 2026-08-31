def count_hits(burn: int, asteroids: list[list[int]]) -> int:
    hits = 0
    for x, y, dx, dy in asteroids:
        x -= burn
        if x % dx:
            continue
        d = x // dx
        hits += y - d * (dy - 1) == 0
    return hits


with open("./input/6.txt") as f:
    lines = f.read().splitlines()

asteroids = [
    [int(x) for part in line.split() for x in part.split(",")] for line in lines
]
answer = min(count_hits(burn, asteroids) for burn in range(-10, 11))
print(answer)
