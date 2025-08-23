import itertools


def is_pentagonal(num):
    n = ((num * 24 + 1) ** 0.5 + 1) / 6
    return n == int(n)


pentagonals: set[int] = set()

for pentagonal in (n * (3 * n - 1) // 2 for n in itertools.count(1)):
    for pentagonal2 in pentagonals:
        if pentagonal - pentagonal2 in pentagonals and is_pentagonal(
            pentagonal + pentagonal2
        ):
            answer = pentagonal - pentagonal2
            break
    else:
        pentagonals.add(pentagonal)
        continue
    break

print(answer)
