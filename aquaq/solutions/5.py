with open("./input/5.txt") as f:
    text = f.read()


def left(die: list[int]) -> list[int]:
    front, left, top, right, back, bottom = die
    return [right, front, top, back, left, bottom]


def right(die: list[int]) -> list[int]:
    front, left, top, right, back, bottom = die
    return [left, back, top, front, right, bottom]


def up(die: list[int]) -> list[int]:
    front, left, top, right, back, bottom = die
    return [bottom, left, front, right, top, back]


def down(die: list[int]) -> list[int]:
    front, left, top, right, back, bottom = die
    return [top, left, back, right, bottom, front]


die1 = [1, 2, 3, 5, 6, 4]
die2 = [1, 3, 2, 4, 6, 5]
m = {"U": up, "D": down, "L": left, "R": right}

answer = 0
for i, instruction in enumerate(text.strip()):
    func = m[instruction]
    die1 = func(die1)
    die2 = func(die2)
    if die1[0] == die2[0]:
        answer += i

print(answer)
