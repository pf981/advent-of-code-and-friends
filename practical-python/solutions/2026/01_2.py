with open("./input/2026/01/input2.txt") as f:
    text = f.read()

alph1, alph2, alph3, alph4, _, *lines = text.splitlines()

m = {}
for a, b, c, d in zip(alph1, alph2, alph3, alph4):
    m[a] = (a, 0, 1)
    m[b] = (a, 1, 0)
    m[c] = (a, -1, 0)
    m[d] = (a, 0, -1)

result = []
r, c = 0, 0
dr, dc = 0, 1
while 0 <= r < len(lines) and 0 <= c < len(lines[0]):
    ch = lines[r][c]
    ch, dr, dc = m.get(ch, (ch, dr, dc))
    result.append(ch)
    r += dr
    c += dc

story = "".join(result)
words = story.split()
answer = words[words.index("NAMED") + 1]
print(answer)
