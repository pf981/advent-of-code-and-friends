from collections import deque

with open("./2026/input/everybody_codes_e2026_q16_p3.txt") as f:
    text = f.read().strip()
COPIES = 100

left = deque()
mid = deque()  # [(color, length), ...]
right = deque()

is_reversed = False

streak = 0
prev = text[0]
for ch in text * COPIES:
    if ch == prev:
        streak += 1
        continue

    mid.append((prev, streak))
    streak = 1
    prev = ch
mid.append([prev, streak])

n = len(text) * COPIES
n_left = n_right = 0
flips = 0

while True:
    if not mid:
        if not right:
            break
        else:
            n_right = 0
            is_reversed = False
            mid, right = right, mid

    ch, length = mid.pop() if is_reversed else mid.popleft()
    n_left += length
    left.append((ch, length))

    color = left[-1][0]
    while mid and mid[0 if is_reversed else -1][0] != color:
        ch, length = mid.popleft() if is_reversed else mid.pop()
        n_right += length
        if right and right[0][0] == ch:
            length += right.popleft()[1]
        right.appendleft((ch, length))

    is_reversed = not is_reversed
    flips += n - n_left - n_right

answer = flips
print(answer)
