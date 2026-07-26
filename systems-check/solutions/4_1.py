with open("./input/4.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    s, expected = line.rsplit("|", 1)
    s += "|"
    expected = int(expected)
    actual = 0
    for c in s:
        actual ^= ord(c)

    if actual != expected:
        answer += expected

print(answer)
