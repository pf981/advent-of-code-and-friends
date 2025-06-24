import itertools

import downloader

lines = downloader.get_puzzle(25).splitlines()

n = len(lines)
m = [[int(s) for s in line.split()] for line in lines]

answer = float("inf")
for path in itertools.permutations(range(1, n), n - 1):
    i = d = 0
    for j in path:
        d += m[i][j]
        i = j
    d += m[i][0]
    answer = min(answer, d)

print(answer)
