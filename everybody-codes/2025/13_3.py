with open("./2025/input/everybody_codes_e2025_q13_p3.txt") as f:
    lines = f.read().splitlines()
turns = 202520252025

ranges = [range(1, 2)]
left: list[range] = []
for i, line in enumerate(lines):
    start, end = (int(s) for s in line.split("-"))

    if i % 2 == 0:
        ranges.append(range(start, end + 1))
    else:
        left.append(range(end, start - 1, -1))

left.reverse()
ranges.extend(left)
ranges.reverse()

remaining = turns % sum(len(rng) for rng in ranges)
answer = None
while remaining >= 0:
    rng = ranges.pop()
    if remaining < len(rng):
        answer = rng[remaining]
        break
    remaining -= len(rng)

assert answer is not None
print(answer)
