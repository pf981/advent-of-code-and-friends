from collections import deque


def last(q: deque[tuple[str, int]], is_reversed: bool) -> tuple[str, int]:
    if is_reversed:
        return q[0]
    return q[-1]


def pop(q: deque[tuple[str, int]], is_reversed: bool) -> tuple[str, int]:
    if is_reversed:
        return q.popleft()
    return q.pop()


def popleft(q: deque[tuple[str, int]], is_reversed: bool) -> tuple[str, int]:
    if is_reversed:
        return q.pop()
    return q.popleft()


with open("./2026/input/everybody_codes_e2026_q16_p3.txt") as f:
    lines = f.read().splitlines()
COPIES = 100


left = deque()
mid = deque()  # [[color, length], ...]
right = deque()

is_reversed = False

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
            break
        else:
            n_right = 0
            mid, right = right, mid

    ch, length = popleft(mid, is_reversed)
    n_left += length
    left.append((ch, length))

    color = left[-1][0]
    while mid and last(mid, is_reversed)[0] != color:
        ch, length = pop(mid, is_reversed)
        n_right += length
        if right and right[0][0] == ch:
            length += right.popleft()[1]
        right.appendleft((ch, length))

    is_reversed = not is_reversed
    flips += n - n_left - n_right

answer = flips
print(answer)
