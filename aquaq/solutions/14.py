with open("./input/14.txt") as f:
    text = f.read()

board_str = """6  17 34 50 68
10 21 45 53 66
5  25 36 52 69
14 30 33 54 63
15 23 41 51 62"""

m = {
    int(num_str): (r, c)
    for r, line in enumerate(board_str.splitlines())
    for c, num_str in enumerate(line.split())
}  # num -> (r, c)
n = 5

answer = 0
for line in text.splitlines():
    rows = [0] * n
    cols = [0] * n
    diag1 = 0
    diag2 = 0

    for num_str in line.split():
        num = int(num_str)
        answer += 1

        if num not in m:
            continue

        r, c = m[num]

        rows[r] += 1
        cols[c] += 1

        if num in [6, 21, 36, 54, 62]:
            diag1 += 1
        if num in [15, 30, 36, 53, 68]:
            diag2 += 1

        if cols[c] == n or rows[r] == n or diag1 == n or diag2 == n:
            break

print(answer)
