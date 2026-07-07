import collections
import math

with open("input/08.txt") as f:
    lines = f.read().splitlines()

MOD = 10**9 + 7

n, n_queries = map(int, lines[0].split())
parents = [0, 0] + list(map(int, lines[1].split()))
log_n = math.ceil(math.log2(n)) + 1
up = [[0] * log_n for _ in range(n + 1)]
depth = [0] * (n + 1)

children = collections.defaultdict(list)
for child, p in enumerate(parents):
    if p:
        children[p].append(child)


def dfs(node: int, p: int) -> None:
    up[node][0] = p
    for j in range(1, log_n):
        up[node][j] = up[up[node][j - 1]][j - 1]

    for child in children[node]:
        depth[child] = depth[node] + 1
        dfs(child, node)


def lca(a: int, b: int) -> int:
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for j in range(log_n):
        if diff & (1 << j):
            a = up[a][j]

    if a == b:
        return a

    for j in range(log_n - 1, -1, -1):
        if up[a][j] != up[b][j]:
            a = up[a][j]
            b = up[b][j]

    return up[a][0]


dfs(1, 0)

answer = 0
for line in lines[2:]:
    a, b = map(int, line.split())
    answer += lca(a, b)
    answer %= MOD
print(answer)
