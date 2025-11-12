# https://www.reddit.com/r/everybodycodes/comments/1outesz/2025_q6_part_4/
import functools


@functools.cache
def count_ways(prev: str, length: int) -> int:
    if length == 0:
        return 1
    return sum(count_ways(c, length - 1) for c in instructions.get(prev, []))


lines = """Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i""".splitlines()

MIN_LEN = 7
MAX_LEN = 98

prefixes = lines[0].split(",")
instructions = {}

for line in lines[2:]:
    a, b = line.split(" > ")
    instructions[a] = b.split(",")

answer3 = 0
for prefix in prefixes:
    if any(other != prefix and prefix.startswith(other) for other in prefixes):
        continue

    if any(b not in instructions[a] for a, b in zip(prefix[:-1], prefix[1:])):
        continue

    for length in range(MIN_LEN - len(prefix), MAX_LEN - len(prefix) + 1):
        answer3 += count_ways(prefix[-1], length)

print(answer3)
