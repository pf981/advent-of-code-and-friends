import math


def twist_faces(faces, twist):
    match twist:
        # FDBULR
        case "D":
            order = [1, 2, 3, 0, 4, 5]
        case "U":
            order = [3, 0, 1, 2, 4, 5]
        case "L":
            order = [4, 1, 5, 3, 2, 0]
        case "R":
            order = [5, 1, 4, 3, 0, 2]
        case "":
            order = list(range(6))
        case _:
            assert False, f"Unknown twist: {twist}"

    faces[:] = [faces[i] for i in order]


with open("2025_contest/16.txt") as f:
    inp = f.read()

side = 80

instructions, twists = inp.split("\n\n")
instructions = instructions.splitlines()
twists = twists.splitlines()[0]

faces = list(range(6))  # FDBULR
powers = [0] * 6
grids = [[[1 for _ in range(side)] for _ in range(side)] for _ in range(6)]

for instruction, twist in zip(instructions, list(twists) + [""]):
    match instruction.split():
        case ["FACE", "-", "VALUE", value]:
            powers[faces[0]] += int(value) * side * side
        case ["ROW", row, "-", "VALUE", value]:
            powers[faces[0]] += int(value) * side
            grid = grids[faces[0]]
            for c in range(side):
                grid[int(row) - 1][c] += int(value)
        case ["COL", col, "-", "VALUE", value]:
            powers[faces[0]] += int(value) * side
            grid = grids[faces[0]]
            for r in range(side):
                grid[r][int(col) - 1] += int(value)
        case _:
            assert False, f"Unknown instruction: {instruction}"

    for r in range(side):
        for c in range(side):
            while grid[r][c] > 100:
                grid[r][c] -= 100

    if twist:
        twist_faces(faces, twist)


answer1 = math.prod(sorted(powers)[-2:])
print(answer1)


# Part 2


def rot_cw(grid):
    grid2 = [list(reversed(x)) for x in zip(*grid)]
    for row, row2 in zip(grid, grid2):
        row[:] = row2


def rot_ccw(grid):
    rot_cw(grid)
    rot_cw(grid)
    rot_cw(grid)


def twist_grids(grids, faces, twist):
    match twist:
        case "D":
            rot_cw(grids[faces[5]])
            rot_ccw(grids[faces[4]])

            rot_cw(grids[faces[2]])
            rot_cw(grids[faces[2]])

            rot_cw(grids[faces[3]])
            rot_cw(grids[faces[3]])
        case "U":
            rot_cw(grids[faces[4]])
            rot_ccw(grids[faces[5]])

            rot_cw(grids[faces[2]])
            rot_cw(grids[faces[2]])

            rot_cw(grids[faces[1]])
            rot_cw(grids[faces[1]])
        case "L":
            rot_cw(grids[faces[1]])
            rot_ccw(grids[faces[3]])
        case "R":
            rot_cw(grids[faces[3]])
            rot_ccw(grids[faces[1]])
        case "":
            pass
        case _:
            assert False, f"Unknown twist: {twist}"


def do_twist(grids, faces, twist):
    twist_grids(grids, faces, twist)
    twist_faces(faces, twist)


def modify_row(grid, row, value):
    for c in range(side):
        r = row - 1
        grid[r][c] += int(value)

        while grid[r][c] > 100:
            grid[r][c] -= 100


def modify_col(grid, col, value):
    for r in range(side):
        c = col - 1
        grid[r][c] += int(value)

        while grid[r][c] > 100:
            grid[r][c] -= 100


def modify_face(grid, value):
    for r in range(side):
        for c in range(side):
            grid[r][c] += int(value)

            while grid[r][c] > 100:
                grid[r][c] -= 100


def get_dominant_sum(grid):
    return max(
        max(sum(row) for row in grid),
        max(sum(col) for col in zip(*grid)),
    )


faces = list(range(6))  # FDBULR
powers = [0] * 6
grids = [[[1 for _ in range(side)] for _ in range(side)] for _ in range(6)]

for instruction, twist in zip(instructions, list(twists) + [""]):
    match instruction.split():
        case ["FACE", "-", "VALUE", value]:
            modify_face(grids[faces[0]], int(value))
        case ["ROW", row, "-", "VALUE", value]:
            modify_row(grids[faces[0]], int(row), int(value))
        case ["COL", col, "-", "VALUE", value]:
            modify_col(grids[faces[0]], int(col), int(value))
        case _:
            assert False, f"Unknown instruction: {instruction}"

    if twist:
        do_twist(grids, faces, twist)

dominant_sums = [get_dominant_sum(grid) for grid in grids]
answer2 = math.prod(dominant_sums)
print(answer2)


# Part 3

faces = list(range(6))  # FDBULR
powers = [0] * 6
grids = [[[1 for _ in range(side)] for _ in range(side)] for _ in range(6)]

for instruction, twist in zip(instructions, list(twists) + [""]):
    match instruction.split():
        case ["FACE", "-", "VALUE", value]:
            modify_face(grids[faces[0]], int(value))
        case ["ROW", row, "-", "VALUE", value]:
            for _ in range(4):
                do_twist(grids, faces, "R")
                modify_row(grids[faces[0]], int(row), int(value))
        case ["COL", col, "-", "VALUE", value]:
            for _ in range(4):
                do_twist(grids, faces, "U")
                modify_col(grids[faces[0]], int(col), int(value))
        case _:
            assert False, f"Unknown instruction: {instruction}"

    if twist:
        do_twist(grids, faces, twist)

dominant_sums = [get_dominant_sum(grid) for grid in grids]
answer3 = math.prod(dominant_sums)
print(answer3)
