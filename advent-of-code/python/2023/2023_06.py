from aocd import get_data, submit
import math
import re


def count_ways(T, D):
    #     D = w * (T - w)
    # =>  0 = -w**2 + T*w - D
    # =>  zeroes at (-T +- sqrt(T**2 - 4*(-1)*(-D))) / 2*(-1)  (quadratic formula)
    upper = (-T - math.sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    lower = (-T + math.sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    return math.ceil(upper) - math.floor(lower) - 1


inp = get_data(day=6, year=2023)
times, distances = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.splitlines()]
answer1 = math.prod(count_ways(time, distance) for time, distance in zip(times, distances))
print(answer1)

submit(answer1, part='a', day=6, year=2023)


# Part 2


time, distance = [int(''.join(str(x) for x in dim)) for dim in [times, distances]]
answer2 = count_ways(time, distance)
print(answer2)

submit(answer2, part='b', day=6, year=2023)
