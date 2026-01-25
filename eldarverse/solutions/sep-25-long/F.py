import functools
import heapq


def get_bases(distances: list[int]) -> tuple[int, ...]:
    @functools.cache
    def get_min_delta(i: int, delta: int):
        if i == len(distances):
            return tuple(), delta

        keep_path, keep_delta = get_min_delta(i + 1, delta + distances[i])

        discard_path, discard_delta = get_min_delta(i + 1, delta - distances[i])

        if abs(keep_delta) < abs(discard_delta):
            return (i,) + keep_path, keep_delta
        return discard_path, discard_delta

    return get_min_delta(0, 0)[0]


with open("./input/problem-sep-25-long-F-input.txt") as f:
    text = f.read()

lines = text.splitlines()[::-1]
n_cases = int(lines.pop())

# Takes a few minutes to run
result = []
for case in range(1, n_cases + 1):
    nrows, ncols, k = map(int, lines.pop().split())
    grid = [lines.pop() for _ in range(nrows)]

    print(f"{nrows=} {ncols=} {k=}")

    missile = None
    distances = {}  # (r, c) -> distance

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == "M":
                missile = (r, c)
                break
        else:
            continue
        break

    assert missile

    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] != ".":
                continue
            distances[(r, c)] = (r - missile[0]) ** 2 + (c - missile[1]) ** 2

    to_build = heapq.nlargest(k, distances, key=lambda p: distances[p])
    bases = {to_build[i] for i in get_bases([distances[p] for p in to_build])}
    power_plants = {p for p in to_build if p not in bases}

    value = min(
        sum(distances[p] for p in bases),
        sum(distances[p] for p in power_plants),
    )

    result.append(f"Case #{case}: {value}")

    for r in range(nrows):
        line = []
        for c in range(ncols):
            ch = grid[r][c]
            if (r, c) in bases:
                ch = "B"
            elif (r, c) in power_plants:
                ch = "E"
            line.append(ch)
        result.append("".join(line))


with open("./output/problem-sep-25-long-F.txt", "w") as f:
    f.write("\n".join(result))
