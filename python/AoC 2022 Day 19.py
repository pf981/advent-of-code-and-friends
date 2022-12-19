# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/19

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 19: Not Enough Minerals ---</h2><p>Your scans show that the lava did indeed form obsidian!</p>
# MAGIC <p>The wind has changed direction enough to stop sending lava droplets toward you, so you and the elephants exit the cave. As you do, you notice a collection of <a href="https://en.wikipedia.org/wiki/Geode" target="_blank">geodes</a> around the pond. Perhaps you could use the obsidian to create some <em>geode-cracking robots</em> and break them open?</p>
# MAGIC <p>To collect the obsidian from the bottom of the pond, you'll need waterproof <em>obsidian-collecting robots</em>. Fortunately, there is an abundant amount of clay nearby that you can use to make them waterproof.</p>
# MAGIC <p>In order to harvest the clay, you'll need special-purpose <em>clay-collecting robots</em>. To make any type of robot, you'll need <em>ore</em>, which is also plentiful but in the opposite direction from the clay.</p>
# MAGIC <p>Collecting ore requires <em>ore-collecting robots</em> with big drills. Fortunately, <em>you have exactly one ore-collecting robot</em> in your pack that you can use to <span title="If You Give A Mouse An Ore-Collecting Robot">kickstart</span> the whole operation.</p>
# MAGIC <p>Each robot can collect 1 of its resource type per minute. It also takes one minute for the robot factory (also conveniently from your pack) to construct any type of robot, although it consumes the necessary resources available when construction begins.</p>
# MAGIC <p>The robot factory has many <em>blueprints</em> (your puzzle input) you can choose from, but once you've configured it with a blueprint, you can't change it. You'll need to work out which blueprint is best.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>Blueprint 1:
# MAGIC   Each ore robot costs 4 ore.
# MAGIC   Each clay robot costs 2 ore.
# MAGIC   Each obsidian robot costs 3 ore and 14 clay.
# MAGIC   Each geode robot costs 2 ore and 7 obsidian.
# MAGIC 
# MAGIC Blueprint 2:
# MAGIC   Each ore robot costs 2 ore.
# MAGIC   Each clay robot costs 3 ore.
# MAGIC   Each obsidian robot costs 3 ore and 8 clay.
# MAGIC   Each geode robot costs 3 ore and 12 obsidian.
# MAGIC </code></pre>
# MAGIC <p>(Blueprints have been line-wrapped here for legibility. The robot factory's actual assortment of blueprints are provided one blueprint per line.)</p>
# MAGIC <p>The elephants are starting to look hungry, so you shouldn't take too long; you need to figure out which blueprint would maximize the number of opened geodes after <em>24 minutes</em> by figuring out which robots to build and when to build them.</p>
# MAGIC <p>Using blueprint 1 in the example above, the largest number of geodes you could open in 24 minutes is <code><em>9</em></code>. One way to achieve that is:</p>
# MAGIC <pre><code>== Minute 1 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 
# MAGIC == Minute 2 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 
# MAGIC == Minute 3 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC The new clay-collecting robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 4 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 1 clay-collecting robot collects 1 clay; you now have 1 clay.
# MAGIC 
# MAGIC == Minute 5 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 1 clay-collecting robot collects 1 clay; you now have 2 clay.
# MAGIC The new clay-collecting robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 6 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 2 clay-collecting robots collect 2 clay; you now have 4 clay.
# MAGIC 
# MAGIC == Minute 7 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 2 clay-collecting robots collect 2 clay; you now have 6 clay.
# MAGIC The new clay-collecting robot is ready; you now have 3 of them.
# MAGIC 
# MAGIC == Minute 8 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 9 clay.
# MAGIC 
# MAGIC == Minute 9 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 12 clay.
# MAGIC 
# MAGIC == Minute 10 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 15 clay.
# MAGIC 
# MAGIC == Minute 11 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 4 clay.
# MAGIC The new obsidian-collecting robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 12 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 7 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
# MAGIC The new clay-collecting robot is ready; you now have 4 of them.
# MAGIC 
# MAGIC == Minute 13 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 11 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
# MAGIC 
# MAGIC == Minute 14 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 15 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 3 obsidian.
# MAGIC 
# MAGIC == Minute 15 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 5 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 4 obsidian.
# MAGIC The new obsidian-collecting robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 16 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 9 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
# MAGIC 
# MAGIC == Minute 17 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 13 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
# MAGIC 
# MAGIC == Minute 18 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 17 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 3 obsidian.
# MAGIC The new geode-cracking robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 19 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 21 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 5 obsidian.
# MAGIC 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
# MAGIC 
# MAGIC == Minute 20 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 25 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 7 obsidian.
# MAGIC 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
# MAGIC 
# MAGIC == Minute 21 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 29 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 2 obsidian.
# MAGIC 1 geode-cracking robot cracks 1 geode; you now have 3 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 22 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 33 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
# MAGIC 2 geode-cracking robots crack 2 geodes; you now have 5 open geodes.
# MAGIC 
# MAGIC == Minute 23 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 5 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 37 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 6 obsidian.
# MAGIC 2 geode-cracking robots crack 2 geodes; you now have 7 open geodes.
# MAGIC 
# MAGIC == Minute 24 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 6 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 41 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 8 obsidian.
# MAGIC 2 geode-cracking robots crack 2 geodes; you now have 9 open geodes.
# MAGIC </code></pre>
# MAGIC <p>However, by using blueprint 2 in the example above, you could do even better: the largest number of geodes you could open in 24 minutes is <code><em>12</em></code>.</p>
# MAGIC <p>Determine the <em>quality level</em> of each blueprint by <em>multiplying that blueprint's ID number</em> with the largest number of geodes that can be opened in 24 minutes using that blueprint. In this example, the first blueprint has ID 1 and can open 9 geodes, so its quality level is <code><em>9</em></code>. The second blueprint has ID 2 and can open 12 geodes, so its quality level is <code><em>24</em></code>. Finally, if you <em>add up the quality levels</em> of all of the blueprints in the list, you get <code><em>33</em></code>.</p>
# MAGIC <p>Determine the quality level of each blueprint using the largest number of geodes it could produce in 24 minutes. <em>What do you get if you add up the quality level of all of the blueprints in your list?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 2: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 19 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 5: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 6: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 7: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 2 ore and 18 obsidian.
Blueprint 8: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 9: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 10: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 11: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 12: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 14: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 15: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 16: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 17: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 19: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 4 ore and 20 obsidian.
Blueprint 20: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 21: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 22: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 9 clay. Each geode robot costs 2 ore and 20 obsidian.
Blueprint 24: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 25: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 26: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 14 clay. Each geode robot costs 4 ore and 10 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 2 ore and 11 obsidian.
Blueprint 29: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 4 ore and 11 obsidian.
Blueprint 30: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 17 obsidian.'''

# COMMAND ----------

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

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>While you were choosing the best blueprint, the elephants found some food on their own, so you're not in as much of a hurry; you figure you probably have <em>32 minutes</em> before the wind changes direction again and you'll need to get out of range of the erupting volcano.</p>
# MAGIC <p>Unfortunately, one of the elephants <em>ate most of your blueprint list</em>! Now, only the first three blueprints in your list are intact.</p>
# MAGIC <p>In 32 minutes, the largest number of geodes blueprint 1 (from the example above) can open is <code><em>56</em></code>. One way to achieve that is:</p>
# MAGIC <pre><code>== Minute 1 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC 
# MAGIC == Minute 2 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 2 ore.
# MAGIC 
# MAGIC == Minute 3 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 3 ore.
# MAGIC 
# MAGIC == Minute 4 ==
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 4 ore.
# MAGIC 
# MAGIC == Minute 5 ==
# MAGIC Spend 4 ore to start building an ore-collecting robot.
# MAGIC 1 ore-collecting robot collects 1 ore; you now have 1 ore.
# MAGIC The new ore-collecting robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 6 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 
# MAGIC == Minute 7 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC The new clay-collecting robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 8 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 1 clay-collecting robot collects 1 clay; you now have 1 clay.
# MAGIC The new clay-collecting robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 9 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 2 clay-collecting robots collect 2 clay; you now have 3 clay.
# MAGIC The new clay-collecting robot is ready; you now have 3 of them.
# MAGIC 
# MAGIC == Minute 10 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 3 clay-collecting robots collect 3 clay; you now have 6 clay.
# MAGIC The new clay-collecting robot is ready; you now have 4 of them.
# MAGIC 
# MAGIC == Minute 11 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 4 clay-collecting robots collect 4 clay; you now have 10 clay.
# MAGIC The new clay-collecting robot is ready; you now have 5 of them.
# MAGIC 
# MAGIC == Minute 12 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 5 clay-collecting robots collect 5 clay; you now have 15 clay.
# MAGIC The new clay-collecting robot is ready; you now have 6 of them.
# MAGIC 
# MAGIC == Minute 13 ==
# MAGIC Spend 2 ore to start building a clay-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 6 clay-collecting robots collect 6 clay; you now have 21 clay.
# MAGIC The new clay-collecting robot is ready; you now have 7 of them.
# MAGIC 
# MAGIC == Minute 14 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# MAGIC The new obsidian-collecting robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 15 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 21 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 1 obsidian.
# MAGIC 
# MAGIC == Minute 16 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# MAGIC 1 obsidian-collecting robot collects 1 obsidian; you now have 2 obsidian.
# MAGIC The new obsidian-collecting robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 17 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# MAGIC 2 obsidian-collecting robots collect 2 obsidian; you now have 4 obsidian.
# MAGIC The new obsidian-collecting robot is ready; you now have 3 of them.
# MAGIC 
# MAGIC == Minute 18 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# MAGIC 3 obsidian-collecting robots collect 3 obsidian; you now have 7 obsidian.
# MAGIC 
# MAGIC == Minute 19 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# MAGIC 3 obsidian-collecting robots collect 3 obsidian; you now have 10 obsidian.
# MAGIC The new obsidian-collecting robot is ready; you now have 4 of them.
# MAGIC 
# MAGIC == Minute 20 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 3 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# MAGIC 4 obsidian-collecting robots collect 4 obsidian; you now have 7 obsidian.
# MAGIC The new geode-cracking robot is ready; you now have 1 of them.
# MAGIC 
# MAGIC == Minute 21 ==
# MAGIC Spend 3 ore and 14 clay to start building an obsidian-collecting robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 7 clay.
# MAGIC 4 obsidian-collecting robots collect 4 obsidian; you now have 11 obsidian.
# MAGIC 1 geode-cracking robot cracks 1 geode; you now have 1 open geode.
# MAGIC The new obsidian-collecting robot is ready; you now have 5 of them.
# MAGIC 
# MAGIC == Minute 22 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 14 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
# MAGIC 1 geode-cracking robot cracks 1 geode; you now have 2 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 2 of them.
# MAGIC 
# MAGIC == Minute 23 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 21 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
# MAGIC 2 geode-cracking robots crack 2 geodes; you now have 4 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 3 of them.
# MAGIC 
# MAGIC == Minute 24 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 2 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 28 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
# MAGIC 3 geode-cracking robots crack 3 geodes; you now have 7 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 4 of them.
# MAGIC 
# MAGIC == Minute 25 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 35 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
# MAGIC 4 geode-cracking robots crack 4 geodes; you now have 11 open geodes.
# MAGIC 
# MAGIC == Minute 26 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 42 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 8 obsidian.
# MAGIC 4 geode-cracking robots crack 4 geodes; you now have 15 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 5 of them.
# MAGIC 
# MAGIC == Minute 27 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 4 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 49 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 6 obsidian.
# MAGIC 5 geode-cracking robots crack 5 geodes; you now have 20 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 6 of them.
# MAGIC 
# MAGIC == Minute 28 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 56 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 11 obsidian.
# MAGIC 6 geode-cracking robots crack 6 geodes; you now have 26 open geodes.
# MAGIC 
# MAGIC == Minute 29 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 63 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 9 obsidian.
# MAGIC 6 geode-cracking robots crack 6 geodes; you now have 32 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 7 of them.
# MAGIC 
# MAGIC == Minute 30 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 70 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 7 obsidian.
# MAGIC 7 geode-cracking robots crack 7 geodes; you now have 39 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 8 of them.
# MAGIC 
# MAGIC == Minute 31 ==
# MAGIC Spend 2 ore and 7 obsidian to start building a geode-cracking robot.
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 6 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 77 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 5 obsidian.
# MAGIC 8 geode-cracking robots crack 8 geodes; you now have 47 open geodes.
# MAGIC The new geode-cracking robot is ready; you now have 9 of them.
# MAGIC 
# MAGIC == Minute 32 ==
# MAGIC 2 ore-collecting robots collect 2 ore; you now have 8 ore.
# MAGIC 7 clay-collecting robots collect 7 clay; you now have 84 clay.
# MAGIC 5 obsidian-collecting robots collect 5 obsidian; you now have 10 obsidian.
# MAGIC 9 geode-cracking robots crack 9 geodes; you now have 56 open geodes.
# MAGIC </code></pre>
# MAGIC <p>However, blueprint 2 from the example above is still better; using it, the largest number of geodes you could open in 32 minutes is <code><em>62</em></code>.</p>
# MAGIC <p>You <em>no longer have enough blueprints to worry about quality levels</em>. Instead, for each of the first three blueprints, determine the largest number of geodes you could open; then, multiply these three values together.</p>
# MAGIC <p>Don't worry about quality levels; instead, just determine the largest number of geodes you could open using each of the first three blueprints. <em>What do you get if you multiply these numbers together?</em></p>
# MAGIC </article>

# COMMAND ----------

import math


most_geodes = [maximize_geodes(32, Mats(0, 0, 0, 0), Mats(1, 0, 0, 0), blueprint) for blueprint in blueprints[:3]]

answer = math.prod(most_geodes)
print(answer) # 48 seconds
