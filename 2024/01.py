with open("./2024/input/everybody_codes_e2024_q01_p1.txt") as f:
    enemies = f.read().splitlines()[0]

m = {"A": 0, "B": 1, "C": 3}
answer1 = sum(m[c] for c in enemies)
print(answer1)


with open("./2024/input/everybody_codes_e2024_q01_p2.txt") as f:
    enemies = f.read().splitlines()[0]

m = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
answer2 = 0
for i in range(0, len(enemies), 2):
    s = enemies[i:i + 2]
    answer2 += sum(m[c] for c in s)
    if s.count('x') == 0:
        answer2 += 2
print(answer2)


with open("./2024/input/everybody_codes_e2024_q01_p3.txt") as f:
    enemies = f.read().splitlines()[0]

m = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
answer3 = 0
for i in range(0, len(enemies), 3):
    s = enemies[i:i + 3]
    answer3 += sum(m[c] for c in s)
    if s.count('x') == 0:
        answer3 += 6
    elif s.count('x') == 1:
        answer3 += 2
print(answer3)
