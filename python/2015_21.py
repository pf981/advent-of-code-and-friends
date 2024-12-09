from aocd import get_data

inp = get_data(day=21, year=2015)

inp2 = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

import re

boss = [int(x) for x in re.findall(r'\d+', inp)]
shop = [[[int(x) for x in re.findall(r'(?<= )\d+', line[1:])] for line in table.split('\n')[1:]] for table in inp2.split('\n\n')]

from itertools import chain, combinations
from heapq import heappush, heappop

def comb(l, take_min, take_max):
  return chain.from_iterable(combinations(l, r) for r in range(take_min, take_max+1))

loadouts = []
loadouts_rev = []

for weapons in comb(shop[0], 1, 1):
  for armors in comb(shop[1], 0, 1):
    for rings in comb(shop[2], 0, 2):
      cost, damage, armor = [sum(x) for x in zip(*(weapons + armors + rings))]
      heappush(loadouts, (cost, damage, armor))
      heappush(loadouts_rev, (-cost, damage, armor))

def does_win(loadout, boss):
  _, damage, armor = loadout
  boss_hp, boss_damage, boss_armor = boss
  
  damage = max(damage - boss_armor, 1)
  boss_damage = max(boss_damage - armor, 1)
  hp = 100
  
  while True:
    boss_hp -= damage
    hp -= boss_damage
    
    if boss_hp <= 0:
      return True
    if hp <= 0:
      return False

while True:
  loadout = heappop(loadouts)
  if does_win(loadout, boss):
    break

answer = loadout[0]
answer

while True:
  loadout = heappop(loadouts_rev)
  if not does_win(loadout, boss):
    break

answer = -loadout[0]
answer
