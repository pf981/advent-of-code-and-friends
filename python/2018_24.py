from aocd import get_data

inp = get_data(day=24, year=2018)

import dataclasses
import re

@dataclasses.dataclass
class Squad:
  army: str
  units: int
  hit_points: int
  attack_damage: int
  initiative: int 
  attack_type: str
  weaknesses: list 
  immunities: list
  
  @property
  def effective_power(self):
    return self.units * self.attack_damage

def parse_army(lines):
  result = []
  army = None
  for line in lines.splitlines():
    if not army:
      army = line.replace(':', '')
      continue
    damage_type = re.findall(r'[a-z]+(?= damage)', line)[0]
    
    weaknesses = re.findall(r'(?<=weak to )[a-z, ]+', line)
    weaknesses = weaknesses[0].split(', ') if weaknesses else []
    
    immunities = re.findall(r'(?<=immune to )[a-z, ]+', line)
    immunities = immunities[0].split(', ') if immunities else []
    
    nums = [int(x) for x in re.findall(r'\d+', line)]
    result.append(Squad(army, *nums, damage_type, weaknesses, immunities))
    
  return result

immune, infection = [parse_army(army) for army in inp.split('\n\n')]
squads = {squad.initiative: squad for squad in immune + infection}

import copy


def calculate_damage(attacker, defender):
  weakness_multiplier = 2 if attacker.attack_type in defender.weaknesses else 1
  immunity_multiplier = 0 if attacker.attack_type in defender.immunities else 1
  return attacker.units * attacker.attack_damage * weakness_multiplier * immunity_multiplier


def target_selection(squads):
  remaining_defenders = set(squads.keys())
  attack_pairs = []
  for attacker in sorted(squads.values(), key=lambda x: (x.effective_power, x.initiative), reverse=True):
    candidates = [(calculate_damage(attacker, defender), defender.effective_power, defender.initiative)
                  for defender in squads.values()
                  if defender.army != attacker.army and defender.initiative in remaining_defenders]
    if not candidates:
      continue
    damage, defender_effective_power, defender_initiative = max(candidates)
    
    if damage:
      attack_pairs.append((attacker.initiative, defender_initiative))
      remaining_defenders.remove(defender_initiative)

  return attack_pairs


def attack(squads, attack_pairs):
  for attacker_i, defender_i in sorted(attack_pairs, reverse=True):
    if attacker_i not in squads or defender_i not in squads:
      continue
    attacker = squads[attacker_i]
    defender = squads[defender_i]
    
    damage = calculate_damage(attacker, defender)
    lost_units = damage // defender.hit_points
    defender.units -= lost_units
    if defender.units <= 0:
      del squads[defender_i]


def get_winner(squads, boost=0):
  squads = copy.deepcopy(squads)
  total_units = sum(squad.units for squad in squads.values())
  
  for immune in squads.values():
    if immune.army == 'Immune System':
      immune.attack_damage += boost

  while len({squad.army for squad in squads.values()}) == 2:
    attack_pairs = target_selection(squads)
    attack(squads, attack_pairs)
    
    # Stalemate check
    if total_units == (total_units := sum(squad.units for squad in squads.values())):
      return None, None
    
  winning_army = next(squad.army for squad in squads.values())
  winning_units = sum(squad.units for squad in squads.values())
  return winning_army, winning_units

  
answer = get_winner(squads)[1]
print(answer)

import itertools

def solve(squads):
  for boost in itertools.count():
    winning_army, winning_units = get_winner(squads, boost=boost)
    if winning_army == 'Immune System':
      return winning_units

answer = solve(squads)
print(answer)
