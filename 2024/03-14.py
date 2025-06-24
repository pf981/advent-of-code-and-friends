import collections

import downloader

text = downloader.get_puzzle(36)


def solve(grids: list[list[str]]) -> int:
    ncols = len(grids[0][0])

    q = collections.deque([(0, 1, 0)])
    seen = {(0, 1, 0)}
    d = 0
    while q:
        nodes = len(q)
        while nodes:
            z, r, c = q.popleft()

            if grids[z][r][c] == "$":
                new_pos = (int(not z), r, c)
                if new_pos not in seen:
                    q.appendleft(new_pos)
                    nodes += 1

            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc

                if c2 < 0:
                    continue

                new_pos = (z, r2, c2)
                if new_pos in seen:
                    continue
                seen.add(new_pos)

                if c2 == ncols:
                    return d

                if grids[z][r2][c2] == "#":
                    continue

                q.append((z, r2, c2))
            nodes -= 1
        d += 1

    return -1  # Stop mypy complaining


grids = [grid.split() for grid in text.split("\n\n")]
answer = solve(grids)
print(answer)
