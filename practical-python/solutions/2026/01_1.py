with open("./input/2026/01/input1.txt") as f:
    text = f.read()

alph1, alph2, _, *lines = text.splitlines()

m = dict(zip(alph2, alph1))
result = []
for i, line in enumerate(lines):
    if i % 2 == 0:
        result.append(line)
        continue
    result.append("".join(m.get(c, c) for c in line[::-1]))

words = "".join(
    c for c in "".join(result) if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
).split()
fives = sorted({w for w in words if len(w) == 5})
answer = fives[19]
print(answer)
