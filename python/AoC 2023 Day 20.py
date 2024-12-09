from aocd import get_data

inp = get_data(day=20, year=2023)

from aocd import get_data, submit
import collections


def initialise_conjunction_inputs(m):
  conjunction_inputs = collections.defaultdict(dict)
  for name, parts in m.items():
    for part in parts:
      if f'&{part}' in m:
        conjunction_inputs[f'&{part}'][name] = 'low'
  return conjunction_inputs


def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()
    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      if signal == 'high':
        continue

      if cur in on_flipflops:
        on_flipflops.remove(cur)
      else:
        on_flipflops.add(cur)
      
      output = 'high' if cur in on_flipflops else 'low'
    
    if cur[0] == '&':
      conjunction_inputs[cur][parent] = signal
      output = 'low' if all(sig == 'high' for sig in conjunction_inputs[cur].values()) else 'high'
      
    for nxt in m[cur]:
      if f'%{nxt}' in m:
        nxt = f'%{nxt}'
      else:
        nxt = f'&{nxt}'
      q.append((nxt, output, cur))


inp = get_data(day=20, year=2023)
m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}
conjunction_inputs = initialise_conjunction_inputs(m)

pulses = {'high': 0, 'low': 0}
on_flipflops = set()
for _ in range(1000):
  push_button()

answer1 = pulses['low'] * pulses['high']
print(answer1)

submit(answer1, part='a', day=20, year=2023)


# Part 2


import collections
import itertools
import math


# Export it to Draw.io
#   Arrange -> Insert -> Advanced -> From Text... -> Diagram
#   Arrange -> Layout -> Vertical Tree
for name, parts in m.items():
  for part in parts:
    if f'&{part}' in m:
      part = f'&{part}'
    if f'%{part}' in m:
      part = f'%{part}'
    print(f'{name}->{part}')


def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()

    if cur in required_lows_periods and signal == 'low':
      required_lows_periods[cur] = presses

    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      if signal == 'high':
        continue

      if cur in on_flipflops:
        on_flipflops.remove(cur)
      else:
        on_flipflops.add(cur)
      
      output = 'high' if cur in on_flipflops else 'low'
    
    if cur[0] == '&':
      conjunction_inputs[cur][parent] = signal
      output = 'low' if all(sig == 'high' for sig in conjunction_inputs[cur].values()) else 'high'
      
    for nxt in m[cur]:
      if f'%{nxt}' in m:
        nxt = f'%{nxt}'
      else:
        nxt = f'&{nxt}'
      q.append((nxt, output, cur))


conjunction_inputs = initialise_conjunction_inputs(m)
on_flipflops = set()

# From the graph, `rx` receives a low pulse when all of the inputs of `&nr` receive a low pulse.
# The required number of presses is the lowest common multiple of the periods
required_lows_periods = {name: None for name in conjunction_inputs['&nr']}

for presses in itertools.count(1):
  push_button()

  if all(required_lows_periods.values()):
   break

answer2 = math.lcm(*required_lows_periods.values())
print(answer2)

submit(answer2, part='b', day=20, year=2023)
