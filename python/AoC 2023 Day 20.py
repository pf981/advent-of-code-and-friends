# Databricks notebook source
# MAGIC %pip install z3-solver

# COMMAND ----------

inp = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''

# COMMAND ----------

inp = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''

# COMMAND ----------

inp = '''%jr -> mq, xn
%zl -> tz, cm
&lh -> nr
%hx -> jx, tz
%cm -> tz, ls
&fk -> nr
broadcaster -> sj, pf, kh, cn
%gz -> mq, lq
%gb -> xf, kr
%zc -> rq
%ln -> qj, xf
%gq -> pp
%fb -> xf
%pf -> tg, nv
%bc -> cf
&tz -> cn, fk, ls
%cq -> fb, xf
%rq -> tg, dx
%km -> gq
&mq -> gq, xn, fv, km, lh, xv, sj
%zp -> mq, xv
%jx -> tz, np
&tg -> mm, rp, zc, pf, bc
%cv -> sq, xf
%nv -> ht, tg
%sq -> gb
%kr -> ln
%dk -> cv
%xn -> zp
%sx -> xf, cq
%zt -> tz, fq
%dx -> tg, qn
&ff -> nr
%bn -> hx, tz
%fj -> zt, tz
%ht -> rr, tg
%fq -> tz, bn
%kh -> dk, xf
%sj -> mq, fv
%vm -> zl, tz
&mm -> nr
%rp -> bc
%fh -> sx
%ls -> fj
%xz -> mq, gz
%fv -> km
&nr -> rx
%lq -> mq
%xv -> xz
%cn -> tz, vm
%pp -> jr, mq
%hn -> tg
%qn -> hn, tg
%rr -> rp, tg
%cf -> tg, zc
%qj -> fh, xf
&xf -> sq, dk, fh, ff, kh, kr
%np -> tz
'''

# COMMAND ----------

import collections
m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}
pulses = {'high': 0, 'low': 0}

def push_button():
  q = collections.deque([('broadcaster', 'low')])
  while q:
    cur, signal = q.popleft()
    # print(cur, signal)
    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
      if signal == 'high':
        continue
      # However, if a flip-flop module receives a low pulse, it flips between on and off.
      if cur in on_flipflops:
        on_flipflops.remove(cur)
      else:
        on_flipflops.add(cur)
      
      output = 'high' if cur in on_flipflops else 'low'
    
    if cur[0] == '&':
      output = 'low' if signal == 'high' else 'high'
      
    for nxt in m[cur]:
      if f'%{nxt}' in m:
        nxt = f'%{nxt}'
      else:
        nxt = f'&{nxt}'
      q.append((nxt, output))



on_flipflops = set()
for _ in range(1000):
  push_button()
pulses['low'] * pulses['high']

# COMMAND ----------

import functools

# I think cache based on q and on_flipflps
@functools.cache
def count_pulses(q, on_flipflops):
  if not q:
    return 0, 0
  
  cur, signal = q[0]
  q = q[1:]

  pulses = {'high': 0, 'low': 0}
  pulses[signal] += 1

  if cur not in m:
    return pulses[low], pulses[high]

  output = 'low'

  if cur[0] == '%':
    # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
    if signal == 'high':
      return pulses[low], pulses[high]
    # However, if a flip-flop module receives a low pulse, it flips between on and off.
    if cur in on_flipflops:
      on_flipflops = on_flipflops.difference({cur})
    else:
      on_flipflops = on_flipflops.union({cur})
    
    output = 'high' if cur in on_flipflops else 'low'
  
  if cur[0] == '&':
    output = 'low' if signal == 'high' else 'high'
    
  for nxt in m[cur]:
    if f'%{nxt}' in m:
      nxt = f'%{nxt}'
    else:
      nxt = f'&{nxt}'
    q = q + [(nxt, output)]
  
  next_low, next_high = count_pulses(q, on_flipflops)
  return pulses[low] + next_low, pulses[high] + next_high

count_pulses((('broadcaster', 'low'),), frozenset())

# COMMAND ----------


inp = '''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''


inp = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''

import functools

import collections
m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}



# I think cache based on q and on_flipflps
#@functools.cache
def count_pulses(q, on_flipflops):
    if not q:
        return 0, 0, on_flipflops

    cur, signal = q[0]
    #print(cur, signal, q)
    q = q[1:]

    pulses = {'high': 0, 'low': 0}
    pulses[signal] += 1

    if cur not in m:
        next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
        return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops

    output = 'low'

    if cur[0] == '%':
        # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
        if signal == 'high':
            next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
            return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops
        # However, if a flip-flop module receives a low pulse, it flips between on and off.
        if cur in on_flipflops:
            on_flipflops = on_flipflops.difference({cur})
        else:
            on_flipflops = on_flipflops.union({cur})

        output = 'high' if cur in on_flipflops else 'low'

    if cur[0] == '&': # FIXME THIS IS WRONG
        output = 'low' if signal == 'high' else 'high'

    for nxt in m[cur]:
        if f'%{nxt}' in m:
            nxt = f'%{nxt}'
        else:
            nxt = f'&{nxt}'
        q = q + ((nxt, output),)

    next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
    return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops

high = low = 0
on_flipflops = frozenset()
for _ in range(1000):
    h, l, on_flipflops = count_pulses((('broadcaster', 'low'),), on_flipflops)
    high += h
    low += l
print(high * low)

# COMMAND ----------

import collections
m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}

conjunction_inputs = collections.defaultdict(dict)

for name, parts in m.items():
  for part in parts:
    if f'&{part}' in m:
      conjunction_inputs[f'&{part}'][name] = 'low'
conjunction_inputs

pulses = {'high': 0, 'low': 0}

def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()
    # print(cur, signal)
    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
      if signal == 'high':
        continue
      # However, if a flip-flop module receives a low pulse, it flips between on and off.
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



on_flipflops = set()
for _ in range(1000):
  push_button()
pulses['low'] * pulses['high']

# COMMAND ----------

# # PART 2
# import collections
# import itertools

# m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}

# conjunction_inputs = collections.defaultdict(dict)

# for name, parts in m.items():
#   for part in parts:
#     if f'&{part}' in m:
#       conjunction_inputs[f'&{part}'][name] = 'low'
# conjunction_inputs

# pulses = {'high': 0, 'low': 0}

# def push_button():
#   q = collections.deque([('broadcaster', 'low', 'button')])
#   while q:
#     cur, signal, parent = q.popleft()

#     if cur in ('&rx', '%rx', 'rx') and signal == 'low':
#       return True

#     # print(cur, signal)
#     pulses[signal] += 1

#     if cur not in m:
#       continue

#     output = 'low'

#     if cur[0] == '%':
#       # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
#       if signal == 'high':
#         continue
#       # However, if a flip-flop module receives a low pulse, it flips between on and off.
#       if cur in on_flipflops:
#         on_flipflops.remove(cur)
#       else:
#         on_flipflops.add(cur)
      
#       output = 'high' if cur in on_flipflops else 'low'
    
#     if cur[0] == '&':
#       conjunction_inputs[cur][parent] = signal
#       output = 'low' if all(sig == 'high' for sig in conjunction_inputs[cur].values()) else 'high'
      
#     for nxt in m[cur]:
#       if f'%{nxt}' in m:
#         nxt = f'%{nxt}'
#       else:
#         nxt = f'&{nxt}'
#       q.append((nxt, output, cur))



# on_flipflops = set()
# for presses in itertools.count(1):
#   if push_button():
#     break
# presses
## Too slow

# COMMAND ----------

# PART 2
import collections
import itertools

m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}

conjunction_inputs = collections.defaultdict(dict)

for name, parts in m.items():
  for part in parts:
    if f'&{part}' in m:
      conjunction_inputs[f'&{part}'][name] = 'low'
conjunction_inputs

pulses = {'high': 0, 'low': 0}
required_lows = ['&lh', '&mm', '&ff', '&fk']
def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()

    if cur in required_lows and signal == 'low':
      print(cur, presses)

    if cur in ('&rx', '%rx', 'rx') and signal == 'low':
      return True

    # print(cur, signal)
    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
      if signal == 'high':
        continue
      # However, if a flip-flop module receives a low pulse, it flips between on and off.
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



on_flipflops = set()
for presses in itertools.count(1):
  push_button()
  # for name, signal in conjunction_inputs['&nr'].items():
  #   if signal == 'high':
  #     print(presses, name)
  # for name, _ in conjunction_inputs['&nr'].items():
  #   signal = list(conjunction_inputs[name].values())[0]
  #   if signal == 'low':
  #     print(presses, name)
  
  if presses == 10000:
   break
presses

# COMMAND ----------

import math

math.lcm(3761,
3797,
3919,
4079)

# COMMAND ----------



# COMMAND ----------

conjunction_inputs['&lh'].values()

# COMMAND ----------

conjunction_inputs['&nr']

# COMMAND ----------

for name, signal in conjunction_inputs['&nr'].items():
  if signal == 'high':
    print(presses, name)

# COMMAND ----------

# import functools

# #@functools.cache
# def count_pulses(q, on_flipflops, conjunction_inputs):
#     if not q:
#         return 0, 0, on_flipflops

#     cur, signal = q[0]
#     print(cur, signal, q)
#     q = q[1:]

#     pulses = {'high': 0, 'low': 0}
#     pulses[signal] += 1

#     if cur not in m:
#         next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
#         return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops

#     output = 'low'

#     if cur[0] == '%':
#         # If a flip-flop module receives a high pulse, it is ignored and nothing happens.
#         if signal == 'high':
#             next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
#             return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops
#         # However, if a flip-flop module receives a low pulse, it flips between on and off.
#         if cur in on_flipflops:
#             on_flipflops = on_flipflops.difference({cur})
#         else:
#             on_flipflops = on_flipflops.union({cur})

#         output = 'high' if cur in on_flipflops else 'low'

#     if cur[0] == '&':
#         output = 'low' if signal == 'high' else 'high'

#     for nxt in m[cur]:
#         if f'%{nxt}' in m:
#             nxt = f'%{nxt}'
#         else:
#             nxt = f'&{nxt}'
#         q = q + ((nxt, output),)

#     next_low, next_high, on_flipflops = count_pulses(q, on_flipflops)
#     return pulses['low'] + next_low, pulses['high'] + next_high, on_flipflops

# high = low = 0
# on_flipflops = frozenset()
# # for _ in range(1000):
# #     l, h, on_flipflops = count_pulses((('broadcaster', 'low'),), on_flipflops)
# #     print(on_flipflops)
# #     high += h
# #     low += l
# # print(high * low)

# l, h, on_flipflops = count_pulses((('broadcaster', 'low'),), on_flipflops)
# print(l, h, on_flipflops)
