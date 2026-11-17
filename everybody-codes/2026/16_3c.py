import collections

with open("./2026/input/everybody_codes_e2026_q16_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """RRYGGYBBYG""".splitlines()
COPIES = 100

# lines = """RRYGYBYG""".splitlines()
# COPIES = 10

# lines = """RRGGBBGRRGGBBG""".splitlines()
# COPIES = 1


def pp():
    s = (
        "".join(ch * length for ch, length in left)
        + " "
        + "".join(ch * length for ch, length in mid)
        + " "
        + "".join(ch * length for ch, length in right)
    )
    print(s)


left = collections.deque()
mid = collections.deque()  # [[color, length], ...]
right = collections.deque()

assert len(lines) == 1
streak = 0
prev = lines[0][0]
for ch in lines[0] * COPIES:
    if ch == prev:
        streak += 1
        continue

    mid.append((prev, streak))
    streak = 1
    prev = ch
mid.append([prev, streak])

n = len(lines[0] * COPIES)
n_left = n_right = 0
flips = 0

while True:
    if not mid:
        if not right:
            # print("TODO: DONE")
            break
        else:
            n_right = 0
            mid, right = right, mid

    ch, length = mid.popleft()
    n_left += length
    left.append((ch, length))

    color = left[-1][0]
    while mid and mid[-1][0] != color:
        ch, length = mid.pop()
        n_right += length
        if right and right[0][0] == ch:
            length += right.popleft()[1]
        right.appendleft((ch, length))

    mid.reverse()  # FIXME: Implement lazy reverse
    # print(f"Flipping {n_mid=}")
    flips += n - n_left - n_right
    # pp()

answer = flips
print(answer)
