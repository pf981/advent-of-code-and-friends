import itertools
import functools


with open("./input/02.txt") as f:
    text = f.read().strip()

answer1 = h = 0
for c in text:
    h += (c == "^") - (c == "v")
    answer1 = max(answer1, h)
print(answer1)

answer2 = h = streak = 0
for c in text:
    dh = (c == "^") - (c == "v")
    if streak == 0 or streak // abs(streak) != dh:
        streak = 0
    streak += dh
    h += streak
    answer2 = max(answer2, h)
print(answer2)


@functools.cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


answer3 = h = 0
for c, grouper in itertools.groupby(text):
    h += fib(len(list(grouper))) * ((c == "^") - (c == "v"))
    answer3 = max(answer3, h)
print(answer3)
