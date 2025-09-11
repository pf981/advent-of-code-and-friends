with open("./input/27.txt") as f:
    text = f.read()

grid = text.splitlines()

answer = 0
for row in grid + ["".join(col) for col in zip(*grid)]:
    answer += sum(
        sum(ord(c) - ord("a") + 1 for c in word) * len(word)
        for word in row.split()
        if len(word) > 1
    )

print(answer)
