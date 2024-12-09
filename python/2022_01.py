from aocd import get_data

inp = get_data(day=1, year=2022)

elves = [sum(int(num) for num in lines.splitlines()) for lines in inp.split('\n\n')]
answer = max(elves)
print(answer)

answer = sum(sorted(elves)[-3:])
print(answer)
