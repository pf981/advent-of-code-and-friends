from aocd import get_data, submit


inp = get_data(day=15, year=2024)

inp = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########\n\n<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''

inp = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########\n\n<^^>>>vv<v>>v<<'''

txt, ops = inp.split('\n\n')
lines = txt.splitlines()
ops = ops.replace('\n', '')

# len(ops.splitlines())

walls = set()
boxes = set()
robot = None

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            walls.add((r, c))
        elif ch == 'O':
            boxes.add((r, c))
        elif ch == '@':
            robot = r, c

r, c = robot
for op in ops:
    if op not in 'v^<>':
        print(f'!!!{op}')
        break
    r2 = r + (op == 'v') - (op == '^')
    c2 = c + (op == '>') - (op == '<')
    
    if (r2, c2) in boxes:
        r3 = r2
        c3 = c2
        while (r3, c3) in boxes:
            r3 += (op == 'v') - (op == '^')
            c3 += (op == '>') - (op == '<')
        if (r3, c3) in walls:
            continue
        # r3 -= (op == 'v') - (op == '^')
        # c3 -= (op == '>') - (op == '<')
        boxes.remove((r2, c2))
        boxes.add((r3, c3))
        r = r2
        c = c2
        continue

    if (r2, c2) in walls:
        continue
    
    r = r2
    c = c2


answer1 = 0
for r, c in boxes:
    answer1 += 100 * r + c

print(answer1)

submit(answer1, part='a', day=15, year=2024)


# Part 2




inp = get_data(day=15, year=2024)

# inp = '''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########\n\n<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
# '''

# inp = '''########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########\n\n<^^>>>vv<v>>v<<'''

# inp = '''#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######\n\n<vv<<^^<<^^'''

txt, ops = inp.split('\n\n')

txt = txt.replace('#', '##')
txt = txt.replace('O', '[]')
txt = txt.replace('.', '..')
txt = txt.replace('@', '@.')

lines = txt.splitlines()
ops = ops.replace('\n', '')

walls = set()
boxes = set()
robot = None

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            walls.add((r, c))
        elif ch == '[':
            boxes.add((r, c))
        elif ch == '@':
            robot = r, c

def print_grid():
    for row, line in enumerate(lines):
        for col, _ in enumerate(line):
            ch = '.'
            if (row, col) in walls:
                ch = '#'
            elif (row, col) in boxes:
                ch = '['
            elif (row, col-1) in boxes:
                ch = ']'
            elif (row, col) == (r, c):
                ch = '@'
            print(ch, end='')
        print()


def get_boxes(r, c, dr):
    if (r, c) in walls:
        return None
    
    if (r, c-1) in boxes:
        c = c - 1

    if (r, c) not in boxes:
        return set()

    # It is a box
    left = get_boxes(r + dr, c, dr)
    right = get_boxes(r + dr, c + 1, dr)
    if left is None or right is None:
        return None
    s = {(r, c)}
    s.update(left)
    s.update(right)
    return s



r, c = robot
for op in ops:
    # print_grid()
    if op not in 'v^<>':
        print(f'!!!{op}')
        break
    r2 = r + (op == 'v') - (op == '^')
    c2 = c + (op == '>') - (op == '<')
    
    if op in '>':
        if (r2, c2) in boxes:

            r3 = r2
            c3 = c2
            moving_boxes = {(r3, c3)}
            while (r3, c3 + 2) in boxes:
                c3 += 2
                moving_boxes.add((r3, c3))
            if (r3, c3+2) in walls:
                continue
            
            
            new_box_positions = {(box_r, box_c + 1) for box_r, box_c in moving_boxes}
            for box_r, box_c in moving_boxes:
                boxes.remove((box_r, box_c))
            boxes.update(new_box_positions)


            r = r2
            c = c2
            continue
    elif op in '<':
        if (r2, c2-1) in boxes:

            r3 = r2
            c3 = c2-1
            moving_boxes = {(r3, c3)}
            while (r3, c3 - 2) in boxes:
                c3 -= 2
                moving_boxes.add((r3, c3))
            if (r3, c3 - 1) in walls:
                continue
            
            
            new_box_positions = {(box_r, box_c - 1) for box_r, box_c in moving_boxes}
            for box_r, box_c in moving_boxes:
                boxes.remove((box_r, box_c))
            boxes.update(new_box_positions)


            r = r2
            c = c2
            continue
    else: # up/down
        dr = (op == 'v') - (op == '^')
        if dr == 0:
            print('??')
            break

        if (r2, c2) in  boxes or (r2, c2 - 1) in boxes:
            # HANDLE UP/DOWN BOXES
            moving_boxes = get_boxes(r2, c2, dr)

            if not moving_boxes:
                continue
            
            new_box_positions = {(box_r + dr, box_c) for box_r, box_c in moving_boxes}
            for box_r, box_c in moving_boxes:
                boxes.remove((box_r, box_c))
            boxes.update(new_box_positions)
                

            # END HANDLE BOXES
            r = r2
            c = c2
            continue

    if (r2, c2) in walls:
        continue
    
    r = r2
    c = c2


answer1 = 0
for r, c in boxes:
    answer1 += 100 * r + c

print(answer1)

submit(answer1, part='b', day=15, year=2024)






# answer2 = 'todo'
# print(answer2)

# submit(answer2, part='b', day=15, year=2024)
