import itertools

n = 1_000_001
divisor_sums = [1] * n

for i in range(2, n):
    for j in range(i + i, n, i):
        divisor_sums[j] += i

best = (0, 0)  # (length, start)
visited = set()
for i in range(1, n):
    visiting = {}
    for d in itertools.count():
        if i >= n:
            break
        if i in visited:
            break
        if i in visiting:
            length = d - visiting[i]
            best = max(best, (length, i))
            break
        visiting[i] = d

        i = divisor_sums[i]

    visited.update(visiting)

i = divisor_sums[best[1]]
smallest = best[1]
while i != best[1]:
    smallest = min(smallest, i)
    i = divisor_sums[i]

answer = smallest
print(answer)
