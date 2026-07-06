with open("./input/2025/05.txt") as f:
    text = f.read().strip()

seen = {}
jumps = [0] * len(text)
for i, c in enumerate(text):
    if c in seen:
        jumps[i] = seen[c]
        jumps[seen[c]] = i
    else:
        seen[c] = i

answer1 = i = 0
while i < len(jumps):
    answer1 += abs(i - jumps[i])
    i = jumps[i] + 1
print(answer1)


visited = set()
i = 0
while i < len(jumps):
    visited.add(text[i])
    i = jumps[i] + 1

answer2 = ""
for c in text:
    if c in visited:
        continue
    visited.add(c)
    answer2 += c
print(answer2)


answer3 = i = 0
while i < len(jumps):
    d = abs(i - jumps[i])
    if text[i].isupper():
        d = -d
    answer3 += d
    i = jumps[i] + 1
print(answer3)
