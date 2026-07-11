with open("./input/2026/06.txt") as f:
    lines = f.read().splitlines()
# lines = """;&%,&/<.%~&|-!-;-+`.
# =#######:@#=*3333,%!
# @*+;|.|####.!3,33A&^
# -<a|*!~#`!#~`3*-3|/;
# S##########*@/!`-|`-
# ,,|@:#./,@#,,@B=@!%@
# <3C!*#`~=*#;./333*.@
# %3@&/#*:`~#^|/+3<!&=
# |33*><:b###<<c333*~|
# <&&@/:!|``:/:&:&&`,&""".splitlines()

nrows = len(lines)
ncols = len(lines[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
gears = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "#"}
lights = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "*"}

seen = {start}
stack = [(*start, False)]
result = []
while stack:
    r, c, is_clockwise = stack.pop()
    # print(f"{r=} {c=}")
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) in seen:
            continue
        seen.add((r2, c2))

        if (r2, c2) in lights:
            result.append((r2, c2, is_clockwise))
        if (r2, c2) not in gears:
            continue
        stack.append((r2, c2, not is_clockwise))

result.sort()
answer = int("".join(str(int(c)) for _, _, c in result), 2)
print(answer)
