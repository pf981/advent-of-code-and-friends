with open("./input/12.txt") as f:
    text = f.read()

floors = [[int(x) for x in line.split()] for line in text.splitlines()]

floor = 0
answer = d = 1
while 0 <= floor < len(floors):
    cont, move = floors[floor]
    if not cont:
        d = -d

    floor += d * move
    answer += 1

print(answer)
