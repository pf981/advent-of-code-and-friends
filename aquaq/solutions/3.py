with open("./input/3.txt") as f:
    text = f.read()

grid = """  ##
 ####
######
######
 ####
  ##"""

valid = {
    (r, c)
    for r, line in enumerate(grid.splitlines())
    for c, ch in enumerate(line)
    if ch == "#"
}

answer = 0
r, c = 0, 2
for d in text.strip():
    r2 = r + (d == "D") - (d == "U")
    c2 = c + (d == "R") - (d == "L")

    if (r2, c2) in valid:
        r, c = r2, c2

    answer += r + c

print(answer)
