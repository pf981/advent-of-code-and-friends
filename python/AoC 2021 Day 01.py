from aocd import get_data

inp = get_data(day=1, year=2021)

depths = [int(depth) for depth in inp.splitlines()]

answer = sum(cur > prev for prev, cur in zip(depths[0:-1], depths[1:]))
print(answer)

sums = [sum(window) for window in zip(depths[0:-2], depths[1:-1], depths[2:])]

answer = sum(cur > prev for prev, cur in zip(sums[0:-1], sums[1:]))
print(answer)
