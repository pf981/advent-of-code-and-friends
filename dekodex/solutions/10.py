import heapq

with open("input/10.txt") as f:
    text = f.read()

MOD = 10**9 + 7
n, *grid = text.splitlines()
n = int(n)
grid = [[int(num) for num in line.split()] for line in grid]

heap = [(grid[0][0], 0, 0)]  # [(max_seen, r, c), ]
seen = set()
answer = None
while heap:
    max_seen, r, c = heapq.heappop(heap)

    if (r, c) in seen:
        continue
    seen.add((r, c))

    if (r, c) == (n - 1, n - 1):
        answer = max_seen % MOD

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if not (0 <= r2 < n and 0 <= c2 < n):
            continue
        if (r2, c2) in seen:
            continue
        heapq.heappush(heap, (max(max_seen, grid[r2][c2]), r2, c2))

assert answer is not None
print(answer)
