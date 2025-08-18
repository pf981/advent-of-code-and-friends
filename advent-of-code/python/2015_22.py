from aocd import get_data

inp = get_data(day=22, year=2015)

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

import re

boss_hp, boss_damage = (int(x) for x in re.findall(r'\d+', inp))

answer = find_win(boss_hp, boss_damage)
answer

answer = find_win(boss_hp, boss_damage, is_hard = True)
answer
