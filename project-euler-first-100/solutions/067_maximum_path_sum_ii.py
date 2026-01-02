with open("data/0067_triangle.txt") as f:
    text = f.read()

triangle = [[int(num) for num in line.split()] for line in text.splitlines()]

for r in reversed(range(len(triangle) - 1)):
    for c in range(len(triangle[r])):
        triangle[r][c] += max(triangle[r + 1][c], triangle[r + 1][c + 1])

answer = triangle[0][0]
print(answer)
