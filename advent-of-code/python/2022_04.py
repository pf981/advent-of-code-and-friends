from aocd import get_data

inp = get_data(day=4, year=2022)

pairs = [[elf.split('-') for elf in line.split(',')] for line in inp.splitlines()]
set_pairs = [[set(range(int(start), int(end) + 1)) for start, end in pair] for pair in pairs]

answer = sum(a.issubset(b) or b.issubset(a) for a, b in set_pairs)
print(answer)

answer = sum(bool(a.intersection(b)) for a, b in set_pairs)
print(answer)
