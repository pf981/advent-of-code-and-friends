from aocd import get_data

inp = get_data(day=6, year=2021)

def count_fishes(fishes, days):
  timers = [0] * 9

  for fish in fishes:
    timers[fish] += 1

  for _ in range(days):
    new_timers = timers.pop(0)
    timers += [new_timers]
    timers[6] += new_timers

  return sum(timers)

fishes = [int(fish) for fish in inp.split(',')]

answer = count_fishes(fishes, 80)
print(answer)

answer = count_fishes(fishes, 256)
print(answer)
