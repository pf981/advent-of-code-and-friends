import downloader

lines = downloader.get_puzzle(23).splitlines()

candidates = {(x, y) for x in range(100) for y in range(100)}
for line in lines:
    x, y, dx, dy = (int(s) for s in line.split())

    x += 3600 * dx
    y += 3600 * dy
    for _ in range(60):
        candidates.discard((x, y))
        x += dx
        y += dy

assert len(candidates) == 1

answer = ":".join(str(num) for num in list(candidates)[0])
print(answer)
