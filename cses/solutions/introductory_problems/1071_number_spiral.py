_, *tests = open(0)

result = []
for test in tests:
    y, x = (int(s) for s in test.split())

    ring = max(x, y)
    if ring % 2:
        x, y = y, x

    d = x + (ring - y)
    result.append(ring * ring - d + 1)

print(*result, sep="\n")
