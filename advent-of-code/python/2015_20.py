from aocd import get_data

inp = get_data(day=20, year=2015)

inp = 34000000

presents = [0] * (inp // 10)

for elf in range(1, len(presents)+1):
  for i in range(elf, len(presents)+1, elf):
    presents[i-1] += elf * 10

answer = next(i for i, x in enumerate(presents, 1) if x >= inp)
answer

presents = [0] * (inp // 10)

for elf in range(1, len(presents)+1):
  for i in range(elf, min(50 * elf, len(presents)) + 1, elf):
    presents[i-1] += elf * 11

answer = next(i for i, x in enumerate(presents, 1) if x >= inp)
answer
