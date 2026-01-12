import collections
import re


def get_max_flow(grid: list[str]) -> int:
    """
    The presents are all the same size (1x2) so the problem is equivalent to
    placing dominoes on a grid with obstructions. This can be solved by finding
    the maximum matching for a bipartite graph using a max flow algorithm
    (Ford-Fulkerson).

    Divide cells into two sets based on the parity of (row + col). Connect
    Source to even cells, and connect odd cells to Sink. The maximum matching
    is the max flow from Source to Sink.

    See https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/matching.pdf
    """
    nrows = len(grid)
    ncols = len(grid[0])

    # (r, c) -> {(r2, c2), ...]. Even parity to odd parity
    edges = collections.defaultdict(set)
    source = (-1, -1)
    sink = (-2, -2)
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] != ".":
                continue

            if (r + c) % 2:
                edges[(r, c)].add(sink)
                continue

            edges[source].add((r, c))
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc

                if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                    continue
                if grid[r2][c2] != ".":
                    continue

                edges[(r, c)].add((r2, c2))

    def dfs(node: tuple[int, int], visited: set[tuple[int, int]]) -> bool:
        """
        Attempts to find a single augmenting path from the current node to
        Sink.

        If a path is found, it pushes flow by reversing the edges along that
        path (updating the residual graph) and returns True.
        """
        if node == sink:
            return True

        for node2 in edges[node].copy():
            if node2 in visited:
                continue
            visited.add(node2)

            edges[node].remove(node2)
            edges[node2].add(node)

            if dfs(node2, visited):
                return True

            edges[node2].remove(node)
            edges[node].add(node2)

        return False

    max_flow = 0
    while dfs(source, {source}):
        max_flow += 1

    return max_flow


with open("data/day25.txt") as f:
    text = f.read()

answer = 0
region_id = 1
for part in text.split("\n\n"):
    if "x" not in part:
        continue

    params, *grid = part.splitlines()
    _, _, *present_counts = map(int, re.findall(r"\d+", params))
    n = sum(present_counts)

    if get_max_flow(grid) >= n:
        answer += region_id

    region_id += 1

print(answer)
