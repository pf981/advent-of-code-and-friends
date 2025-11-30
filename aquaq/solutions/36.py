import math


def solve_quadratic(S: int, P: int) -> tuple[int, int] | None:
    """
    Integer roots (a, b) for x^2 - Sx + P = 0 if they exist.
    """
    D = S * S - 4 * P
    if D < 0:
        return None
    d_sqrt = int(math.isqrt(D))
    if d_sqrt * d_sqrt != D:
        return None

    if (S - d_sqrt) % 2 != 0:
        return None

    r1 = (S - d_sqrt) // 2
    r2 = (S + d_sqrt) // 2

    result = tuple(sorted((r1, r2)))
    assert len(result) == 2
    return result


def sum_differences(grid_nums: list[int], pattern: list[int | None]) -> int:
    n = len(grid_nums)

    adj: list[list[tuple[int, tuple[int, int]]]] = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            res1 = solve_quadratic(grid_nums[i], grid_nums[j])
            if res1:
                adj[i].append((j, res1))
                adj[j].append((i, res1))

            res2 = solve_quadratic(grid_nums[j], grid_nums[i])
            if res2:
                adj[i].append((j, res2))
                adj[j].append((i, res2))

    def check_pattern(collected_pairs: list[tuple[int, int]]) -> bool:
        nums: list[int] = []
        for p in collected_pairs:
            nums.extend(p)
        nums.sort()

        for k, val in enumerate(pattern):
            if val is not None:
                if nums[k] != val:
                    return False
        return True

    def backtrack(mask: int, current_pairs: list[tuple[int, int]]):
        if mask == (1 << n) - 1:
            if check_pattern(current_pairs):
                return current_pairs
            return None

        u = 0
        while (mask >> u) & 1:
            u += 1

        for v, pair_vals in adj[u]:
            if not ((mask >> v) & 1):
                res = backtrack(mask | (1 << u) | (1 << v), current_pairs + [pair_vals])
                if res:
                    return res
        return None

    pairs = backtrack(0, [])

    if pairs:
        return sum(abs(a - b) for a, b in pairs)
    return 0


with open("./input/36.txt") as f:
    text = f.read()

answer = 0
for part in text.split("\n\n"):
    g_str, pattern_str = part.strip().splitlines()
    grid_nums = [int(s) for s in g_str[2:].split()]
    pattern = [int(s) if s != "*" else None for s in pattern_str[2:].split()]

    answer += sum_differences(grid_nums, pattern)

print(answer)
