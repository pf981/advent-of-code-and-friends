def can_empty(a: int, b: int) -> bool:
    if (2 * b - a) % 3 != 0:
        return False
    x = (2 * b - a) // 3
    y = b - 2 * x
    return x >= 0 and y >= 0


_, *lines = open(0)
for line in lines:
    a, b = (int(x) for x in line.split())
    print("YES" if can_empty(a, b) else "NO")
