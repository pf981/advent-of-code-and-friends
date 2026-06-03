import collections

with open("./input/2025/03/input1.txt") as f:
    lines = f.read().splitlines()

arm = int(lines[0])
hold = collections.deque()
qs = [collections.deque(c for c in line.split(",") if c) for line in lines[2:]]
for inst in lines[1].split(","):
    d = int(inst[1:])
    match inst[0]:
        case "L":
            arm -= d
        case "R":
            arm += d
        case "T":
            for _ in range(d):
                hold.appendleft(qs[arm].popleft())
        case "D":
            for _ in range(d):
                qs[arm].append(hold.pop())
        case _:
            assert False

print("".join(q[0] for q in qs if q))
