with open("./2026/input/everybody_codes_e2026_q16_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """RRYGGYBBYG""".splitlines()
# COPIES = 100

# lines = """RRYGYBYG""".splitlines()
# COPIES = 10

lines = """RRGGBBGRRGGBBG""".splitlines()
COPIES = 1

groups = []  # [(ch, length), ...]

assert len(lines) == 1
streak = 0
prev = lines[0][0]
for ch in lines[0] * COPIES:
    if ch == prev:
        streak += 1
        continue

    groups.append([prev, streak])
    streak = 1
    prev = ch
groups.append([prev, streak])

n = len(lines[0])

color = groups[0][0]
l = 1
r = len(groups) - 1
while groups[r][0] != color:
    n -= groups[r][1]
    r -= 1


# answer = flips
# print(answer)
