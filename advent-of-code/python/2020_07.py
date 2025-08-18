from aocd import get_data

inp = get_data(day=7, year=2020)

import re

rules = {}
for line in inp.splitlines():
  bag, text = line.split(' bags contain ')
  contains = {}
  for s in text.split(', '):
    if s == 'no other bags.':
      break
    d, name = re.findall(r'(\d+) (.+) bags?\.?', s)[0]
    contains[name] = int(d)
  rules[bag] = contains


def contains_shiny_gold(bag):
  for b2 in rules[bag]:
    if b2 == 'shiny gold' or contains_shiny_gold(b2):
      return True
  return False


answer = sum(contains_shiny_gold(bag) for bag in rules)
print(answer)

import functools

@functools.cache
def count_bags(bag):
  n_bags = 0
  for b2 in rules[bag]:
    n = rules[bag][b2]
    n_bags += n + n * count_bags(b2)
  return n_bags

answer = count_bags('shiny gold')
print(answer)
