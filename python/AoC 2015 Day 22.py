# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Wizard Simulator 20XX ---</h2><p>Little Henry Case decides that defeating bosses with <a href="21">swords and stuff</a> is boring.  Now he's playing the game with a <span title="Being a !@#$% Sorcerer.">wizard</span>.  Of course, he gets stuck on another boss and needs your help again.</p>
# MAGIC <p>In this version, combat still proceeds with the player and the boss taking alternating turns.  The player still goes first.  Now, however, you don't get any equipment; instead, you must choose one of your spells to cast.  The first character at or below <code>0</code> hit points loses.</p>
# MAGIC <p>Since you're a wizard, you don't get to wear armor, and you can't attack normally.  However, since you do <em>magic damage</em>, your opponent's armor is ignored, and so the boss effectively has zero armor as well.  As before, if armor (from a spell, in this case) would reduce damage below <code>1</code>, it becomes <code>1</code> instead - that is, the boss' attacks always deal at least <code>1</code> damage.</p>
# MAGIC <p>On each of your turns, you must select one of your spells to cast.  If you cannot afford to cast any spell, you lose.  Spells cost <em>mana</em>; you start with <em>500</em> mana, but have no maximum limit.  You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it.  Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.</p>
# MAGIC <ul>
# MAGIC <li><em>Magic Missile</em> costs <code>53</code> mana.  It instantly does <code>4</code> damage.</li>
# MAGIC <li><em>Drain</em> costs <code>73</code> mana.  It instantly does <code>2</code> damage and heals you for <code>2</code> hit points.</li>
# MAGIC <li><em>Shield</em> costs <code>113</code> mana.  It starts an <em>effect</em> that lasts for <code>6</code> turns.  While it is active, your armor is increased by <code>7</code>.</li>
# MAGIC <li><em>Poison</em> costs <code>173</code> mana.  It starts an <em>effect</em> that lasts for <code>6</code> turns.  At the start of each turn while it is active, it deals the boss <code>3</code> damage.</li>
# MAGIC <li><em>Recharge</em> costs <code>229</code> mana.  It starts an <em>effect</em> that lasts for <code>5</code> turns.  At the start of each turn while it is active, it gives you <code>101</code> new mana.</li>
# MAGIC </ul>
# MAGIC <p><em>Effects</em> all work the same way.  Effects apply at the start of both the player's turns and the boss' turns.  Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one.  If this decreases the timer to zero, the effect ends.  You cannot cast a spell that would start an effect which is already active.  However, effects can be started on the same turn they end.</p>
# MAGIC <p>For example, suppose the player has <code>10</code> hit points and <code>250</code> mana, and that the boss has <code>13</code> hit points and <code>8</code> damage:</p>
# MAGIC <pre><code>-- Player turn --
# MAGIC - Player has 10 hit points, 0 armor, 250 mana
# MAGIC - Boss has 13 hit points
# MAGIC Player casts Poison.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 10 hit points, 0 armor, 77 mana
# MAGIC - Boss has 13 hit points
# MAGIC Poison deals 3 damage; its timer is now 5.
# MAGIC Boss attacks for 8 damage.
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 0 armor, 77 mana
# MAGIC - Boss has 10 hit points
# MAGIC Poison deals 3 damage; its timer is now 4.
# MAGIC Player casts Magic Missile, dealing 4 damage.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 0 armor, 24 mana
# MAGIC - Boss has 3 hit points
# MAGIC Poison deals 3 damage. This kills the boss, and the player wins.
# MAGIC </code></pre>
# MAGIC <p>Now, suppose the same initial conditions, except that the boss has <code>14</code> hit points instead:</p>
# MAGIC <pre><code>-- Player turn --
# MAGIC - Player has 10 hit points, 0 armor, 250 mana
# MAGIC - Boss has 14 hit points
# MAGIC Player casts Recharge.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 10 hit points, 0 armor, 21 mana
# MAGIC - Boss has 14 hit points
# MAGIC Recharge provides 101 mana; its timer is now 4.
# MAGIC Boss attacks for 8 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 0 armor, 122 mana
# MAGIC - Boss has 14 hit points
# MAGIC Recharge provides 101 mana; its timer is now 3.
# MAGIC Player casts Shield, increasing armor by 7.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 7 armor, 110 mana
# MAGIC - Boss has 14 hit points
# MAGIC Shield's timer is now 5.
# MAGIC Recharge provides 101 mana; its timer is now 2.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 1 hit point, 7 armor, 211 mana
# MAGIC - Boss has 14 hit points
# MAGIC Shield's timer is now 4.
# MAGIC Recharge provides 101 mana; its timer is now 1.
# MAGIC Player casts Drain, dealing 2 damage, and healing 2 hit points.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 3 hit points, 7 armor, 239 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 3.
# MAGIC Recharge provides 101 mana; its timer is now 0.
# MAGIC Recharge wears off.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 7 armor, 340 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 2.
# MAGIC Player casts Poison.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 7 armor, 167 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 1.
# MAGIC Poison deals 3 damage; its timer is now 5.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 1 hit point, 7 armor, 167 mana
# MAGIC - Boss has 9 hit points
# MAGIC Shield's timer is now 0.
# MAGIC Shield wears off, decreasing armor by 7.
# MAGIC Poison deals 3 damage; its timer is now 4.
# MAGIC Player casts Magic Missile, dealing 4 damage.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 1 hit point, 0 armor, 114 mana
# MAGIC - Boss has 2 hit points
# MAGIC Poison deals 3 damage. This kills the boss, and the player wins.
# MAGIC </code></pre>
# MAGIC <p>You start with <em>50 hit points</em> and <em>500 mana points</em>. The boss's actual stats are in your puzzle input. What is the <em>least amount of mana</em> you can spend and still win the fight?  (Do not include mana recharge effects as "spending" negative mana.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''Hit Points: 51
Damage: 9'''

# COMMAND ----------

def update_timers(state):
  if state['shield_timer'] > 0:
    state['shield_timer'] -= 1
    if state['shield_timer'] == 0:
      state['armor'] -= 7

  if state['poison_timer'] > 0:
    state['boss_hp'] -= 3
    state['poison_timer'] -= 1
    
    if state['boss_hp'] <= 0:
      return 'Win'

  if state['recharge_timer'] > 0:
    state['mana'] += 101
    state['recharge_timer'] -= 1
  
  return 'Pending'

def simulate(state, is_hard = False):
  # Player Turn
  if is_hard:
    state['hp'] -= 1
    if state['hp'] <= 0:
      return 'Lose'

  if (result := update_timers(state)) != 'Pending':
    return result
  
  state['mana'] -= spells[state['spell']]
  if state['mana'] < 0:
    return 'Lose'
  
  if state['spell'] == 'Magic Missile':
    state['boss_hp'] -= 4
  elif state['spell'] == 'Drain':
    state['boss_hp'] -= 2
    state['hp'] += 2
  elif state['spell'] == 'Shield':
    if state['shield_timer'] > 0:
      return 'Lose'
    
    state['shield_timer'] = 6
    state['armor'] += 7
  elif state['spell'] == 'Poison':
    if state['poison_timer'] > 0:
      return 'Lose'
    
    state['poison_timer'] = 6
  elif state['spell'] == 'Recharge':
    if state['recharge_timer'] > 0:
      return 'Lose'
    
    state['recharge_timer'] = 5
  
  if state['boss_hp'] <= 0:
    return 'Win'
  
  # Boss Turn
  if (result := update_timers(state)) != 'Pending':
    return result
  
  state['hp'] -= state['boss_damage'] - state['armor']
  
  if state['hp'] <= 0:
    return 'Lose'
  
  return 'Pending'

# COMMAND ----------

import random
from heapq import heappush, heappop

spells = {
  'Magic Missile': 53,
  'Drain': 73,
  'Shield': 113,
  'Poison': 173,
  'Recharge': 229
}

def find_win(boss_hp, boss_damage, is_hard = False):
  states = []
  for spell, mana_cost in spells.items():
    new_state = {
      'spell': spell,
      'hp': 50, 'armor': 0, 'mana': 500,
      'boss_hp': boss_hp, 'boss_damage': boss_damage,
      'shield_timer': 0, 'poison_timer': 0, 'recharge_timer': 0
    }
    # Need the random number so that ties are settled without needing to compare the state dict
    heappush(states, (mana_cost, random.randint(0, 10000000000), new_state))
  
  while states:
    mana_spent, _, state = heappop(states)
    result = simulate(state, is_hard)

    if result == 'Win':
      return mana_spent
    
    if result == 'Pending':
      for spell, mana_cost in spells.items():
        new_state = state.copy()
        new_state['spell'] = spell
        heappush(states, (mana_spent + mana_cost, random.randint(0, 10000000000), new_state))

# COMMAND ----------

import re

boss_hp, boss_damage = (int(x) for x in re.findall(r'\d+', inp))

answer = find_win(boss_hp, boss_damage)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>On the next run through the game, you increase the difficulty to <em>hard</em>.</p>
# MAGIC <p>At the start of each <em>player turn</em> (before any other effects apply), you lose <code>1</code> hit point. If this brings you to or below <code>0</code> hit points, you lose.</p>
# MAGIC <p>With the same starting stats for you and the boss, what is the <em>least amount of mana</em> you can spend and still win the fight?</p>
# MAGIC </article>

# COMMAND ----------

answer = find_win(boss_hp, boss_damage, is_hard = True)
answer
