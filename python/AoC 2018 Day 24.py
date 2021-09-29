# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: Immune System Simulator 20XX ---</h2><p>After <a href="https://www.youtube.com/watch?v=NDVjLt_QHL8&amp;t=7" target="_blank">a weird buzzing noise</a>, you appear back at the man's cottage. He seems relieved to see his friend, but quickly notices that the little reindeer caught some kind of cold while out exploring.</p>
# MAGIC <p>The portly man explains that this reindeer's immune system isn't similar to regular reindeer immune systems:</p>
# MAGIC <p>The <em>immune system</em> and the <em>infection</em> each have <span title="On second thought, it's pretty similar to regular reindeer immune systems.">an army</span> made up of several <em>groups</em>; each <em>group</em> consists of one or more identical <em>units</em>.  The armies repeatedly <em>fight</em> until only one army has units remaining.</p>
# MAGIC <p><em>Units</em> within a group all have the same <em>hit points</em> (amount of damage a unit can take before it is destroyed), <em>attack damage</em> (the amount of damage each unit deals), an <em>attack type</em>, an <em>initiative</em> (higher initiative units attack first and win ties), and sometimes <em>weaknesses</em> or <em>immunities</em>. Here is an example group:</p>
# MAGIC <pre><code>18 units each with 729 hit points (weak to fire; immune to cold, slashing)
# MAGIC  with an attack that does 8 radiation damage at initiative 10
# MAGIC </code></pre>
# MAGIC <p>Each group also has an <em>effective power</em>: the number of units in that group multiplied by their attack damage. The above group has an effective power of <code>18 * 8 = 144</code>. Groups never have zero or negative units; instead, the group is removed from combat.</p>
# MAGIC <p>Each <em>fight</em> consists of two phases: <em>target selection</em> and <em>attacking</em>.</p>
# MAGIC <p>During the <em>target selection</em> phase, each group attempts to choose one target. In decreasing order of effective power, groups choose their targets; in a tie, the group with the higher initiative chooses first. The attacking group chooses to target the group in the enemy army to which it would deal the most damage (after accounting for weaknesses and immunities, but not accounting for whether the defending group has enough units to actually receive all of that damage).</p>
# MAGIC <p>If an attacking group is considering two defending groups to which it would deal equal damage, it chooses to target the defending group with the largest effective power; if there is still a tie, it chooses the defending group with the highest initiative.  If it cannot deal any defending groups damage, it does not choose a target.  Defending groups can only be chosen as a target by one attacking group.</p>
# MAGIC <p>At the end of the target selection phase, each group has selected zero or one groups to attack, and each group is being attacked by zero or one groups.</p>
# MAGIC <p>During the <em>attacking</em> phase, each group deals damage to the target it selected, if any. Groups attack in decreasing order of initiative, regardless of whether they are part of the infection or the immune system. (If a group contains no units, it cannot attack.)</p>
# MAGIC <p>The damage an attacking group deals to a defending group depends on the attacking group's attack type and the defending group's immunities and weaknesses.  By default, an attacking group would deal damage equal to its <em>effective power</em> to the defending group.  However, if the defending group is <em>immune</em> to the attacking group's attack type, the defending group instead takes <em>no damage</em>; if the defending group is <em>weak</em> to the attacking group's attack type, the defending group instead takes <em>double damage</em>.</p>
# MAGIC <p>The defending group only loses <em>whole units</em> from damage; damage is always dealt in such a way that it kills the most units possible, and any remaining damage to a unit that does not immediately kill it is ignored. For example, if a defending group contains <code>10</code> units with <code>10</code> hit points each and receives <code>75</code> damage, it loses exactly <code>7</code> units and is left with <code>3</code> units at full health.</p>
# MAGIC <p>After the fight is over, if both armies still contain units, a new fight begins; combat only ends once one army has lost all of its units.</p>
# MAGIC <p>For example, consider the following armies:</p>
# MAGIC <pre><code>Immune System:
# MAGIC 17 units each with 5390 hit points (weak to radiation, bludgeoning) with
# MAGIC  an attack that does 4507 fire damage at initiative 2
# MAGIC 989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
# MAGIC  slashing) with an attack that does 25 slashing damage at initiative 3
# MAGIC 
# MAGIC Infection:
# MAGIC 801 units each with 4706 hit points (weak to radiation) with an attack
# MAGIC  that does 116 bludgeoning damage at initiative 1
# MAGIC 4485 units each with 2961 hit points (immune to radiation; weak to fire,
# MAGIC  cold) with an attack that does 12 slashing damage at initiative 4
# MAGIC </code></pre>
# MAGIC <p>If these armies were to enter combat, the following fights, including details during the target selection and attacking phases, would take place:</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 1 contains 17 units
# MAGIC Group 2 contains 989 units
# MAGIC Infection:
# MAGIC Group 1 contains 801 units
# MAGIC Group 2 contains 4485 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 1 185832 damage
# MAGIC Infection group 1 would deal defending group 2 185832 damage
# MAGIC Infection group 2 would deal defending group 2 107640 damage
# MAGIC Immune System group 1 would deal defending group 1 76619 damage
# MAGIC Immune System group 1 would deal defending group 2 153238 damage
# MAGIC Immune System group 2 would deal defending group 1 24725 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 84 units
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Immune System group 1 attacks defending group 2, killing 51 units
# MAGIC Infection group 1 attacks defending group 1, killing 17 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 905 units
# MAGIC Infection:
# MAGIC Group 1 contains 797 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 184904 damage
# MAGIC Immune System group 2 would deal defending group 1 22625 damage
# MAGIC Immune System group 2 would deal defending group 2 22625 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Infection group 1 attacks defending group 2, killing 144 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 761 units
# MAGIC Infection:
# MAGIC Group 1 contains 793 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 183976 damage
# MAGIC Immune System group 2 would deal defending group 1 19025 damage
# MAGIC Immune System group 2 would deal defending group 2 19025 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Infection group 1 attacks defending group 2, killing 143 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 618 units
# MAGIC Infection:
# MAGIC Group 1 contains 789 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 183048 damage
# MAGIC Immune System group 2 would deal defending group 1 15450 damage
# MAGIC Immune System group 2 would deal defending group 2 15450 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 3 units
# MAGIC Infection group 1 attacks defending group 2, killing 143 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 475 units
# MAGIC Infection:
# MAGIC Group 1 contains 786 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 182352 damage
# MAGIC Immune System group 2 would deal defending group 1 11875 damage
# MAGIC Immune System group 2 would deal defending group 2 11875 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 2 units
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 333 units
# MAGIC Infection:
# MAGIC Group 1 contains 784 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181888 damage
# MAGIC Immune System group 2 would deal defending group 1 8325 damage
# MAGIC Immune System group 2 would deal defending group 2 8325 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 1 unit
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 191 units
# MAGIC Infection:
# MAGIC Group 1 contains 783 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181656 damage
# MAGIC Immune System group 2 would deal defending group 1 4775 damage
# MAGIC Immune System group 2 would deal defending group 2 4775 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 1 unit
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 49 units
# MAGIC Infection:
# MAGIC Group 1 contains 782 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181424 damage
# MAGIC Immune System group 2 would deal defending group 1 1225 damage
# MAGIC Immune System group 2 would deal defending group 2 1225 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 0 units
# MAGIC Infection group 1 attacks defending group 2, killing 49 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC No groups remain.
# MAGIC Infection:
# MAGIC Group 1 contains 782 units
# MAGIC Group 2 contains 4434 units
# MAGIC </code></pre>
# MAGIC <p>In the example above, the winning army ends up with <code>782 + 4434 = <em>5216</em></code> units.</p>
# MAGIC <p>You scan the reindeer's condition (your puzzle input); the white-bearded man looks nervous.  As it stands now, <em>how many units would the winning army have</em>?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''Immune System:
1432 units each with 7061 hit points (immune to cold; weak to bludgeoning) with an attack that does 41 slashing damage at initiative 17
3387 units each with 9488 hit points (weak to bludgeoning) with an attack that does 27 slashing damage at initiative 20
254 units each with 3249 hit points (immune to fire) with an attack that does 89 cold damage at initiative 1
1950 units each with 8201 hit points with an attack that does 39 fire damage at initiative 15
8137 units each with 3973 hit points (weak to slashing; immune to radiation) with an attack that does 4 radiation damage at initiative 6
4519 units each with 7585 hit points (weak to fire) with an attack that does 15 radiation damage at initiative 8
763 units each with 7834 hit points (immune to radiation, slashing, cold; weak to fire) with an attack that does 91 radiation damage at initiative 18
935 units each with 10231 hit points (immune to slashing, cold) with an attack that does 103 bludgeoning damage at initiative 12
4557 units each with 7860 hit points (immune to slashing) with an attack that does 15 slashing damage at initiative 11
510 units each with 7363 hit points (weak to fire, radiation) with an attack that does 143 fire damage at initiative 5

Infection:
290 units each with 29776 hit points (weak to cold, radiation) with an attack that does 204 bludgeoning damage at initiative 16
7268 units each with 14114 hit points (immune to radiation; weak to bludgeoning) with an attack that does 3 bludgeoning damage at initiative 19
801 units each with 5393 hit points with an attack that does 13 slashing damage at initiative 13
700 units each with 12182 hit points with an attack that does 29 cold damage at initiative 4
531 units each with 16607 hit points (immune to slashing) with an attack that does 53 bludgeoning damage at initiative 10
23 units each with 24482 hit points (weak to cold, fire) with an attack that does 2095 bludgeoning damage at initiative 7
8025 units each with 43789 hit points (weak to cold; immune to radiation) with an attack that does 8 radiation damage at initiative 9
1405 units each with 53896 hit points with an attack that does 70 slashing damage at initiative 14
566 units each with 7820 hit points (immune to cold) with an attack that does 26 cold damage at initiative 2
1641 units each with 7807 hit points (weak to fire; immune to slashing, bludgeoning) with an attack that does 7 radiation damage at initiative 3'''

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Things aren't looking good for the reindeer. The man asks whether more milk and cookies would help you think.</p>
# MAGIC <p>If only you could give the reindeer's immune system a boost, you might be able to change the outcome of the combat.</p>
# MAGIC <p>A <em>boost</em> is an integer increase in immune system units' attack damage. For example, if you were to boost the above example's immune system's units by <code>1570</code>, the armies would instead look like this:</p>
# MAGIC <pre><code>Immune System:
# MAGIC 17 units each with 5390 hit points (weak to radiation, bludgeoning) with
# MAGIC  an attack that does <em>6077</em> fire damage at initiative 2
# MAGIC 989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
# MAGIC  slashing) with an attack that does <em>1595</em> slashing damage at initiative 3
# MAGIC 
# MAGIC Infection:
# MAGIC 801 units each with 4706 hit points (weak to radiation) with an attack
# MAGIC  that does 116 bludgeoning damage at initiative 1
# MAGIC 4485 units each with 2961 hit points (immune to radiation; weak to fire,
# MAGIC  cold) with an attack that does 12 slashing damage at initiative 4
# MAGIC </code></pre>
# MAGIC <p>With this boost, the combat proceeds differently:</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 989 units
# MAGIC Group 1 contains 17 units
# MAGIC Infection:
# MAGIC Group 1 contains 801 units
# MAGIC Group 2 contains 4485 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 185832 damage
# MAGIC Infection group 1 would deal defending group 1 185832 damage
# MAGIC Infection group 2 would deal defending group 1 53820 damage
# MAGIC Immune System group 2 would deal defending group 1 1577455 damage
# MAGIC Immune System group 2 would deal defending group 2 1577455 damage
# MAGIC Immune System group 1 would deal defending group 2 206618 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 1, killing 9 units
# MAGIC Immune System group 2 attacks defending group 1, killing 335 units
# MAGIC Immune System group 1 attacks defending group 2, killing 32 units
# MAGIC Infection group 1 attacks defending group 2, killing 84 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 905 units
# MAGIC Group 1 contains 8 units
# MAGIC Infection:
# MAGIC Group 1 contains 466 units
# MAGIC Group 2 contains 4453 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 108112 damage
# MAGIC Infection group 1 would deal defending group 1 108112 damage
# MAGIC Infection group 2 would deal defending group 1 53436 damage
# MAGIC Immune System group 2 would deal defending group 1 1443475 damage
# MAGIC Immune System group 2 would deal defending group 2 1443475 damage
# MAGIC Immune System group 1 would deal defending group 2 97232 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 1, killing 8 units
# MAGIC Immune System group 2 attacks defending group 1, killing 306 units
# MAGIC Infection group 1 attacks defending group 2, killing 29 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 876 units
# MAGIC Infection:
# MAGIC Group 2 contains 4453 units
# MAGIC Group 1 contains 160 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 106872 damage
# MAGIC Immune System group 2 would deal defending group 2 1397220 damage
# MAGIC Immune System group 2 would deal defending group 1 1397220 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 83 units
# MAGIC Immune System group 2 attacks defending group 2, killing 427 units
# MAGIC </code></pre>
# MAGIC <p>After a few fights...</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 64 units
# MAGIC Infection:
# MAGIC Group 2 contains 214 units
# MAGIC Group 1 contains 19 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 5136 damage
# MAGIC Immune System group 2 would deal defending group 2 102080 damage
# MAGIC Immune System group 2 would deal defending group 1 102080 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 4 units
# MAGIC Immune System group 2 attacks defending group 2, killing 32 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 60 units
# MAGIC Infection:
# MAGIC Group 1 contains 19 units
# MAGIC Group 2 contains 182 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 4408 damage
# MAGIC Immune System group 2 would deal defending group 1 95700 damage
# MAGIC Immune System group 2 would deal defending group 2 95700 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 19 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 60 units
# MAGIC Infection:
# MAGIC Group 2 contains 182 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 4368 damage
# MAGIC Immune System group 2 would deal defending group 2 95700 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 3 units
# MAGIC Immune System group 2 attacks defending group 2, killing 30 units
# MAGIC </code></pre>
# MAGIC <p>After a few more fights...</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC Group 2 contains 40 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 960 damage
# MAGIC Immune System group 2 would deal defending group 2 81345 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 0 units
# MAGIC Immune System group 2 attacks defending group 2, killing 27 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC Group 2 contains 13 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 312 damage
# MAGIC Immune System group 2 would deal defending group 2 81345 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 0 units
# MAGIC Immune System group 2 attacks defending group 2, killing 13 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC No groups remain.
# MAGIC </code></pre>
# MAGIC <p>This boost would allow the immune system's armies to win! It would be left with <code><em>51</em></code> units.</p>
# MAGIC <p>You don't even know <em>how</em> you could boost the reindeer's immune system or what effect it might have, so you need to be cautious and find the <em>smallest boost</em> that would allow the immune system to win.</p>
# MAGIC <p><em>How many units does the immune system have left</em> after getting the smallest boost it needs to win?</p>
# MAGIC </article>

# COMMAND ----------

import itertools

def solve(squads):
  for boost in itertools.count():
    winning_army, winning_units = get_winner(squads, boost=boost)
    if winning_army == 'Immune System':
      return winning_units

answer = solve(squads)
print(answer)
