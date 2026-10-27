import itertools

with open("./2026/input/everybody_codes_e2026_q02_p3.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    parts = line.split()
    for order in itertools.permutations("123456789", 9):
        for a, b, c in parts:
            if b == ">":
                a, c = c, a
            if order.index(a) < order.index(c):
                break
        else:
            answer += int("".join(order))
            break

print(answer)
