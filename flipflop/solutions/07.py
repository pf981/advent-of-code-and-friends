import functools


@functools.cache
def count_ways(xs: tuple[int, ...], sizes: tuple[int, ...]) -> int:
    if all(x == nx - 1 for x, nx in zip(xs, sizes)):
        return 1
    if not all(0 <= x < nx for x, nx in zip(xs, sizes)):
        return 0

    ways = 0
    for i in range(len(xs)):
        ways += count_ways(xs[:i] + (xs[i] + 1,) + xs[i + 1 :], sizes)
    return ways


with open("./input/07.txt") as f:
    lines = f.read().splitlines()

dims = [[int(x) for x in line.split()] for line in lines]

answer1 = 0
for ncols, nrows in dims:
    answer1 += count_ways((0, 0), (nrows, ncols))
print(answer1)


answer2 = 0
for ncols, nrows in dims:
    answer2 += count_ways((0, 0, 0), (nrows, ncols, ncols))
print(answer2)


answer3 = 0
for n, w in dims:
    answer3 += count_ways((0,) * n, (w,) * n)
print(answer3)
