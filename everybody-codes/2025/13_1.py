import collections

with open("./2025/input/everybody_codes_e2025_q13_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """72
# 58
# 47
# 61
# 67""".splitlines()
turns = 2025

q = collections.deque([1])

nums = [int(line) for line in lines]
res = 0
# i = 0
for i, num in enumerate(nums):
    if i % 2 == 0:
        q.append(num)
    else:
        q.appendleft(num)

i = q.index(1)
ans = q[(i + turns) % len(q)]

# answer1 = "todo"
# print(answer1)
