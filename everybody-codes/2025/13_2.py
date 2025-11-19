import collections

with open("./2025/input/everybody_codes_e2025_q13_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """72
# 58
# 47
# 61
# 67""".splitlines()
turns = 20252025

q = collections.deque([1])

res = 0
for i, lines in enumerate(lines):
    a, b = lines.split("-")
    a = int(a)
    b = int(b)
    r = range(a, b + 1)
    for num in r:
        if i % 2 == 0:
            q.append(num)
        else:
            q.appendleft(num)

i = q.index(1)
ans = q[(i + turns) % len(q)]
print(ans)

# answer1 = "todo"
# print(answer1)
