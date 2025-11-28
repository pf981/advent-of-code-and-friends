from aocd import get_data, submit


inp = get_data(day=15, year=2024)
txt, ops = inp.split('\n\n')
lines = txt.splitlines()
ops = ops.replace('\n', '')

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


txt, ops = inp.split('\n\n')

for a, b in [('#', '##'), ('O', '[]'),('.', '..'),('@', '@.')]:
    txt = txt.replace(a, b)
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

    return {(r, c)} | left | right


r, c = robot
for op in ops:
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
            moving_boxes = get_boxes(r2, c2, dr)

            if not moving_boxes:
                continue
            
            new_box_positions = {(box_r + dr, box_c) for box_r, box_c in moving_boxes}
            for box_r, box_c in moving_boxes:
                boxes.remove((box_r, box_c))
            boxes.update(new_box_positions)
                
            r = r2
            c = c2
            continue

    if (r2, c2) in walls:
        continue
    
    r = r2
    c = c2

answer2 = 0
for r, c in boxes:
    answer2 += 100 * r + c
print(answer2)

submit(answer2, part='b', day=15, year=2024)
