from aocd import get_data

inp = get_data(day=19, year=2022)

import dataclasses
import functools
import re


@dataclasses.dataclass(frozen=True)
class Mats:
  ore: int
  clay: int
  obsidian: int
  geode: int
  
  def __add__(self, other):
    return Mats(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)
  
  def __sub__(self, other):
    return Mats(self.ore - other.ore, self.clay - other.clay, self.obsidian - other.obsidian, self.geode - other.geode)


@dataclasses.dataclass(frozen=True)
class Blueprint:
  id: int
  ore_cost_ore: int
  clay_cost_ore: int
  obsidian_cost_ore: int
  obsidian_cost_clay: int
  geode_cost_ore: int
  geode_cost_obsidian: int


@functools.cache
def maximize_geodes(time_remaining: int, mats: Mats, robots: Mats, blueprint: Blueprint) -> int:
  time_remaining -= 1
  next_mats = mats + robots
  
  if time_remaining == 0:
    return next_mats.geode
  
  # If you can buy geode robot, then do it
  if mats.ore >= blueprint.geode_cost_ore and mats.obsidian >= blueprint.geode_cost_obsidian:
    return maximize_geodes(
      time_remaining,
      next_mats - Mats(blueprint.geode_cost_ore, 0, blueprint.geode_cost_obsidian, 0),
      robots + Mats(0, 0, 0, 1),
      blueprint
    )
    
  outcomes = []
  
  # Only buy obsidian robot if the number of obsidian robots is less than the obsidian cost of a geode robot
  if robots.obsidian < blueprint.geode_cost_obsidian:
    if mats.ore >= blueprint.obsidian_cost_ore and mats.clay >= blueprint.obsidian_cost_clay:
      outcomes.append(maximize_geodes(
        time_remaining,
        next_mats - Mats(blueprint.obsidian_cost_ore, blueprint.obsidian_cost_clay, 0, 0),
        robots + Mats(0, 0, 1, 0),
        blueprint
      ))

  # Only buy ore robot if the number of ore robots is less than the ore cost of other robots
  if robots.ore < max(blueprint.ore_cost_ore, blueprint.clay_cost_ore, blueprint.obsidian_cost_ore, blueprint.geode_cost_ore):
    if mats.ore >= blueprint.ore_cost_ore:
      outcomes.append(maximize_geodes(
        time_remaining,
        next_mats - Mats(blueprint.ore_cost_ore, 0, 0, 0),
        robots + Mats(1, 0, 0, 0),
        blueprint
      ))
  
  # Only buy clay robot if the number of clay robots is less than the clay cost of an obsidian robot
  if robots.clay < blueprint.obsidian_cost_clay:
    if mats.ore >= blueprint.clay_cost_ore:
      outcomes.append(maximize_geodes(
        time_remaining,
        next_mats - Mats(blueprint.clay_cost_ore, 0, 0, 0),
        robots + Mats(0, 1, 0, 0),
        blueprint
      ))
    
  # Only do nothing if you have < 4 ore or if you chose not to make the other robots
  if mats.ore < 4 or not outcomes:
    outcomes.append(maximize_geodes(
      time_remaining,
      next_mats,
      robots,
      blueprint
    ))
  
  return max(outcomes)


blueprints = [Blueprint(*(int(x) for x in re.findall(r'\d+', line))) for line in inp.splitlines()]
quality = [blueprint.id * maximize_geodes(24, Mats(0, 0, 0, 0), Mats(1, 0, 0, 0), blueprint) for blueprint in blueprints]

answer = sum(quality)
print(answer) # 20 seconds

import math


most_geodes = [maximize_geodes(32, Mats(0, 0, 0, 0), Mats(1, 0, 0, 0), blueprint) for blueprint in blueprints[:3]]

answer = math.prod(most_geodes)
print(answer) # 48 seconds
