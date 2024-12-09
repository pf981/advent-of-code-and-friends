from aocd import get_data

inp = get_data(day=15, year=2023)

from aocd import get_data, submit


def get_hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

inp = get_data(day=15, year=2023)
answer1 = sum(get_hash(s) for s in inp.split(','))
print(answer1)

submit(answer1, part='a', day=15, year=2023)


# Part 2


boxes = [[] for _ in range(256)]

for instruction in inp.split(','):
    if '=' in instruction:
        target, num = instruction.split('=')
        box = get_hash(target)
        
        for i, (t, n) in enumerate(boxes[box]):
            if t == target:
                boxes[box][i] = (target, num)
                break
        else:
            boxes[box].append((target, num))
    else: # -
        target = instruction[:-1]
        box = get_hash(target)
        for i, (t, n) in enumerate(boxes[box]):
            if t == target:
                del boxes[box][i]
                break

answer2 = 0
for i_box, box in enumerate(boxes, 1):
    for i_slot, (_, num) in enumerate(box, 1):
        answer2 += i_box * i_slot * int(num)
print(answer2)

submit(answer2, part='b', day=15, year=2023)
