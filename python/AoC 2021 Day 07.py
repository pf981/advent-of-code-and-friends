from aocd import get_data

inp = get_data(day=7, year=2021)

def calc_min_fuel(crabs, fuel_cost_f):
  min_fuel = float('inf')
  for target in range(min(crabs), max(crabs) + 1):
    fuel = sum(fuel_cost_f(abs(crab - target)) for crab in crabs)
    min_fuel = min(min_fuel, fuel)
  
  return min_fuel

crabs = [int(x) for x in inp.split(',')]

answer = calc_min_fuel(crabs, lambda d: d)
print(answer)

answer = calc_min_fuel(crabs, lambda d: d * (d + 1) // 2)
print(answer)
