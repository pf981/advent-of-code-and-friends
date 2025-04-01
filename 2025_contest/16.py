import copy
import math

with open("2025_contest/16.txt") as f:
    inp = f.read()
side = 80

# inp = """FACE - VALUE 38
# COL 32 - VALUE 39
# COL 72 - VALUE 12
# COL 59 - VALUE 56
# COL 77 - VALUE 31
# FACE - VALUE 43
# COL 56 - VALUE 47
# ROW 73 - VALUE 83
# COL 15 - VALUE 87
# COL 76 - VALUE 57

# ULDLRLLRU
# """
# side = 80

# inp = """FACE - VALUE 38
# ROW 2 - VALUE 71
# ROW 1 - VALUE 57
# ROW 3 - VALUE 68
# COL 1 - VALUE 52

# LURD
# """
# side = 3





# instructions, twists = inp.split("\n\n")
# instructions = instructions.splitlines()
# twists = twists.splitlines()[0]
# faces = list(range(6))  # FDBULR
# powers = [0] * 6
# grids = [[[1 for _ in range(side)] for _ in range(side)] for _ in range(6)]


# # g = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]]
# # rot_cw(g)
# # rot_ccw(g)
# # g


def rot_cw(grid):
    grid2 = [list(reversed(x)) for x in zip(*grid)]
    for row, row2 in zip(grid, grid2):
        row[:] = row2


def rot_ccw(grid):
    rot_cw(grid)
    rot_cw(grid)
    rot_cw(grid)

def print_grids(grids):
    print('-----')
    for grid in grids:
        for row in grid:
            print(row)
        print('--')
    print('-----')

# for instruction, twist in zip(instructions, list(twists) + [""]):
#     # print(instruction)
#     match instruction.split():
#         case ["FACE", "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side * side
#             grid = grids[faces[0]]
#             for r in range(side):
#                 for c in range(side):
#                     grid[r][c] += int(value)
#         case ["ROW", row, "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side
#             grid = grids[faces[0]]
#             for c in range(side):
#                 grid[int(row) - 1][c] += int(value)
#         case ["COL", col, "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side
#             grid = grids[faces[0]]
#             for r in range(side):
#                 grid[r][int(col) - 1] += int(value)
#         case _:
#             assert False, f"Unknown instruction: {instruction}"

#     for r in range(side):
#         for c in range(side):
#             while grid[r][c] > 100:
#                 grid[r][c] -= 100

#     # print_grids(grids)

#     if not twist:
#         continue

#     # print(twist)
#     match twist:
#         case "D":
#             # FDBULR
#             order = [1, 2, 3, 0, 4, 5]
#             rot_cw(grids[faces[5]])
#             rot_ccw(grids[faces[4]])

#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

#             rot_cw(grids[faces[3]])
#             rot_cw(grids[faces[3]])
#         case "U":
#             # FDBULR
#             order = [3, 0, 1, 2, 4, 5]
#             rot_cw(grids[faces[4]])
#             rot_ccw(grids[faces[5]])

#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

#             rot_cw(grids[faces[1]])
#             rot_cw(grids[faces[1]])
#         case "L":
#             # FDBULR
#             order = [4, 1, 5, 3, 2, 0]
#             rot_cw(grids[faces[1]])
#             rot_ccw(grids[faces[3]])
#         case "R":
#             # FDBULR
#             order = [5, 1, 4, 3, 0, 2]
#             rot_cw(grids[faces[3]])
#             rot_ccw(grids[faces[1]])
#         case "":
#             order = list(range(6))
#         case _:
#             assert False, f"Unknown twist: {twist}"

#     # FDBULR
#     faces = [faces[i] for i in order]

# answer1 = math.prod(sorted(powers)[-2:])
# print(answer1)


# # Part 2

def get_dominant_sum(grid):
    return max(
        max(sum(row) for row in grid),
        max(sum(col) for col in zip(*grid)),
    )

# dominant_sums = [get_dominant_sum(grid) for grid in grids]
# answer2 = math.prod(dominant_sums)
# print(answer2)
# # 59937121117711486063800 incorrect
# # 59937121117711486063800
# # 59336866583580282111800 incorrect
# # 58485578185116293274000 correct


# Part 3


instructions, twists = inp.split("\n\n")
instructions = instructions.splitlines()
twists = twists.splitlines()[0]
faces = list(range(6))  # FDBULR
powers = [0] * 6
grids = [[[1 for _ in range(side)] for _ in range(side)] for _ in range(6)]


def do_twist(grids, faces, twist):
    match twist:
        case "D":
            # FDBULR
            order = [1, 2, 3, 0, 4, 5]
            rot_cw(grids[faces[5]])
            rot_ccw(grids[faces[4]])

            rot_cw(grids[faces[2]])
            rot_cw(grids[faces[2]])

            rot_cw(grids[faces[3]])
            rot_cw(grids[faces[3]])
        case "U":
            # FDBULR
            order = [3, 0, 1, 2, 4, 5]
            rot_cw(grids[faces[4]])
            rot_ccw(grids[faces[5]])

            rot_cw(grids[faces[2]])
            rot_cw(grids[faces[2]])

            rot_cw(grids[faces[1]])
            rot_cw(grids[faces[1]])
        case "L":
            # FDBULR
            order = [4, 1, 5, 3, 2, 0]
            rot_cw(grids[faces[1]])
            rot_ccw(grids[faces[3]])
        case "R":
            # FDBULR
            order = [5, 1, 4, 3, 0, 2]
            rot_cw(grids[faces[3]])
            rot_ccw(grids[faces[1]])
        case "":
            order = list(range(6))
        case _:
            assert False, f"Unknown twist: {twist}"

    # FDBULR
    faces[:] = [faces[i] for i in order]

def modify_row(grids, faces, row, value):
    grid = grids[faces[0]]
    for c in range(side):
        grid[int(row) - 1][c] += int(value)
    for r in range(side):
        for c in range(side):
            while grid[r][c] > 100:
                grid[r][c] -= 100

def modify_col(grids, faces, col, value):
    grid = grids[faces[0]]
    for r in range(side):
        grid[r][int(col) - 1] += int(value)
    for r in range(side):
        for c in range(side):
            while grid[r][c] > 100:
                grid[r][c] -= 100

for instruction, twist in zip(instructions, list(twists) + [""]):
    # print(instruction)
    match instruction.split():
        case ["FACE", "-", "VALUE", value]:
            grid = grids[faces[0]]
            for r in range(side):
                for c in range(side):
                    grid[r][c] += int(value)
            for r in range(side):
                for c in range(side):
                    while grid[r][c] > 100:
                        grid[r][c] -= 100
        case ["ROW", row, "-", "VALUE", value]:
            for _ in range(4):
                do_twist(grids, faces, 'R')
                modify_row(grids, faces, int(row), int(value))
        case ["COL", col, "-", "VALUE", value]:
            for _ in range(4):
                do_twist(grids, faces, 'U')
                modify_col(grids, faces, int(col), int(value))
        case _:
            assert False, f"Unknown instruction: {instruction}"

    # print_grids(grids)

    if not twist:
        continue

    # print(twist)
    do_twist(grids, faces, twist)

# for instruction, twist in zip(instructions, list(twists) + [""]):
#     print(instruction)
#     match instruction.split():
#         case ["FACE", "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side * side
#             grid = grids[faces[0]]
#             for r in range(side):
#                 for c in range(side):
#                     grid[r][c] += int(value)
#         case ["ROW", row, "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side
#             for i in [0, 4, 5, 2]:
#                 grid = grids[faces[i]]
#                 for c in range(side):
#                     grid[int(row) - 1][c] += int(value)
#         case ["COL", col, "-", "VALUE", value]:
#             powers[faces[0]] += int(value) * side

            
#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

#             for i in [0, 4, 1, 2]:
#                 grid = grids[faces[i]]
#                 for r in range(side):
#                     grid[r][int(col) - 1] += int(value)

#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

                    
#             # grid = grids[faces[2]]
#             # for r in range(side):
#             #     grid[r][side - 1 - (int(col) - 1)] += int(value)
#         case _:
#             assert False, f"Unknown instruction: {instruction}"

#     for grid in grids:
#         for r in range(side):
#             for c in range(side):
#                 while grid[r][c] > 100:
#                     grid[r][c] -= 100

#     print_grids(grids)

#     if not twist:
#         continue

#     # print(twist)
#     match twist:
#         case "D":
#             # FDBULR
#             order = [1, 2, 3, 0, 4, 5]
#             rot_cw(grids[faces[5]])
#             rot_ccw(grids[faces[4]])

#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

#             rot_cw(grids[faces[3]])
#             rot_cw(grids[faces[3]])
#         case "U":
#             # FDBULR
#             order = [3, 0, 1, 2, 4, 5]
#             rot_cw(grids[faces[4]])
#             rot_ccw(grids[faces[5]])

#             rot_cw(grids[faces[2]])
#             rot_cw(grids[faces[2]])

#             rot_cw(grids[faces[1]])
#             rot_cw(grids[faces[1]])
#         case "L":
#             # FDBULR
#             order = [4, 1, 5, 3, 2, 0]
#             rot_cw(grids[faces[1]])
#             rot_ccw(grids[faces[3]])
#         case "R":
#             # FDBULR
#             order = [5, 1, 4, 3, 0, 2]
#             rot_cw(grids[faces[3]])
#             rot_ccw(grids[faces[1]])
#         case "":
#             order = list(range(6))
#         case _:
#             assert False, f"Unknown twist: {twist}"

#     # FDBULR
#     faces = [faces[i] for i in order]

dominant_sums = [get_dominant_sum(grid) for grid in grids]
answer3 = math.prod(dominant_sums)
print(answer3)
