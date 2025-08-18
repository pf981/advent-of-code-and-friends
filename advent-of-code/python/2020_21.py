from aocd import get_data

inp = get_data(day=21, year=2020)

import re


foods = [tuple(frozenset(re.findall(r'[a-z]+', part)) for part in line.split('contains')) for line in inp.splitlines()]
all_ingredients, all_allergens = (frozenset.union(*part) for part in zip(*foods))

possible_allergens = {}
for ingredient in all_ingredients:
  possible_allergens[ingredient] = all_allergens
  for food_ingredients, food_allergens in foods:
    if ingredient in food_ingredients:
      continue
    possible_allergens[ingredient] -= food_allergens

non_allergen_ingredients = {ingredient for ingredient, candidate_allergens in possible_allergens.items() if not candidate_allergens}

answer = sum(non_allergen_ingredient in food_ingredients for food_ingredients, _ in foods for non_allergen_ingredient in non_allergen_ingredients)
print(answer)

for ingredient in non_allergen_ingredients:
  del possible_allergens[ingredient]

confirmed_allergens = {}
while possible_allergens:
  for ingredient, candidate_allergens in possible_allergens.items():
    if len(candidate_allergens) == 1:
      confirmed_allergen = next(iter(candidate_allergens))
      confirmed_allergens[ingredient] = confirmed_allergen
      del possible_allergens[ingredient]
      break
  
  for ingredient, candidate_allergens in possible_allergens.items():
    possible_allergens[ingredient] = candidate_allergens - {confirmed_allergen}

answer = ','.join(sorted(confirmed_allergens, key=confirmed_allergens.__getitem__))
print(answer)
