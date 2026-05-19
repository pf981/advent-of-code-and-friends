import itertools


def is_valid(d1: tuple[int, ...], d2: tuple[int, ...]) -> bool:
    if 9 in d1:
        d1 = d1 + (6,)
    if 9 in d2:
        d2 = d2 + (6,)

    targets = [[0, 1], [0, 4], [0, 6], [1, 6], [2, 5], [3, 6], [4, 6], [6, 4], [8, 1]]
    for a, b in targets:
        if not ((a in d1 and b in d2) or (a in d2 and b in d1)):
            return False

    return True


answer = 0
for d1 in itertools.combinations(range(10), 6):
    for d2 in itertools.combinations(range(10), 6):
        if d1 > d2:
            continue
        answer += is_valid(d1, d2)

print(answer)
