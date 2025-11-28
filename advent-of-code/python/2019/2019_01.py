from aocd import get_data

inp = get_data(day=1, year=2019)

fuel_needed = [int(x) for x in inp.splitlines()]

answer = sum(module // 3 - 2 for module in fuel_needed)
print(answer)

def fuel_requirements(fuel):
  total_fuel = 0
  while (fuel := fuel // 3 - 2) > 0:
    total_fuel += fuel
  return total_fuel

answer = sum(fuel_requirements(module) for module in fuel_needed)
print(answer)
