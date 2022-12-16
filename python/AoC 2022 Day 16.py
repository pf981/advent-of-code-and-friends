# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/16

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: Proboscidea Volcanium ---</h2><p>The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.</p>
# MAGIC <p>The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!</p>
# MAGIC <p>You need to get the elephants out of here, quickly. Your device estimates that you have <em>30 minutes</em> before the volcano erupts, so you don't have time to go back out the way you came in.</p>
# MAGIC <p>You scan the cave for other options and discover a network of pipes and pressure-release <em>valves</em>. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's <em>flow rate</em> if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.</p>
# MAGIC <p>There's even a valve in the room you and the elephants are currently standing in labeled <code>AA</code>. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?</p>
# MAGIC <p>For example, suppose you had the following scan output:</p>
# MAGIC <pre><code>Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# MAGIC Valve BB has flow rate=13; tunnels lead to valves CC, AA
# MAGIC Valve CC has flow rate=2; tunnels lead to valves DD, BB
# MAGIC Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# MAGIC Valve EE has flow rate=3; tunnels lead to valves FF, DD
# MAGIC Valve FF has flow rate=0; tunnels lead to valves EE, GG
# MAGIC Valve GG has flow rate=0; tunnels lead to valves FF, HH
# MAGIC Valve HH has flow rate=22; tunnel leads to valve GG
# MAGIC Valve II has flow rate=0; tunnels lead to valves AA, JJ
# MAGIC Valve JJ has flow rate=21; tunnel leads to valve II
# MAGIC </code></pre>
# MAGIC <p>All of the valves begin <em>closed</em>. You start at valve <code>AA</code>, but it must be damaged or <span title="Wait, sir! The valve, sir! it appears to be... jammed!">jammed</span> or something: its flow rate is <code>0</code>, so there's no point in opening it. However, you could spend one minute moving to valve <code>BB</code> and another minute opening it; doing so would release pressure during the remaining <em>28 minutes</em> at a flow rate of <code>13</code>, a total eventual pressure release of <code>28 * 13 = <em>364</em></code>. Then, you could spend your third minute moving to valve <code>CC</code> and your fourth minute opening it, providing an additional <em>26 minutes</em> of eventual pressure release at a flow rate of <code>2</code>, or <code><em>52</em></code> total pressure released by valve <code>CC</code>.</p>
# MAGIC <p>Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:</p>
# MAGIC <pre><code>== Minute 1 ==
# MAGIC No valves are open.
# MAGIC You move to valve DD.
# MAGIC 
# MAGIC == Minute 2 ==
# MAGIC No valves are open.
# MAGIC You open valve DD.
# MAGIC 
# MAGIC == Minute 3 ==
# MAGIC Valve DD is open, releasing <em>20</em> pressure.
# MAGIC You move to valve CC.
# MAGIC 
# MAGIC == Minute 4 ==
# MAGIC Valve DD is open, releasing <em>20</em> pressure.
# MAGIC You move to valve BB.
# MAGIC 
# MAGIC == Minute 5 ==
# MAGIC Valve DD is open, releasing <em>20</em> pressure.
# MAGIC You open valve BB.
# MAGIC 
# MAGIC == Minute 6 ==
# MAGIC Valves BB and DD are open, releasing <em>33</em> pressure.
# MAGIC You move to valve AA.
# MAGIC 
# MAGIC == Minute 7 ==
# MAGIC Valves BB and DD are open, releasing <em>33</em> pressure.
# MAGIC You move to valve II.
# MAGIC 
# MAGIC == Minute 8 ==
# MAGIC Valves BB and DD are open, releasing <em>33</em> pressure.
# MAGIC You move to valve JJ.
# MAGIC 
# MAGIC == Minute 9 ==
# MAGIC Valves BB and DD are open, releasing <em>33</em> pressure.
# MAGIC You open valve JJ.
# MAGIC 
# MAGIC == Minute 10 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve II.
# MAGIC 
# MAGIC == Minute 11 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve AA.
# MAGIC 
# MAGIC == Minute 12 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve DD.
# MAGIC 
# MAGIC == Minute 13 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve EE.
# MAGIC 
# MAGIC == Minute 14 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve FF.
# MAGIC 
# MAGIC == Minute 15 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve GG.
# MAGIC 
# MAGIC == Minute 16 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You move to valve HH.
# MAGIC 
# MAGIC == Minute 17 ==
# MAGIC Valves BB, DD, and JJ are open, releasing <em>54</em> pressure.
# MAGIC You open valve HH.
# MAGIC 
# MAGIC == Minute 18 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You move to valve GG.
# MAGIC 
# MAGIC == Minute 19 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You move to valve FF.
# MAGIC 
# MAGIC == Minute 20 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You move to valve EE.
# MAGIC 
# MAGIC == Minute 21 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You open valve EE.
# MAGIC 
# MAGIC == Minute 22 ==
# MAGIC Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
# MAGIC You move to valve DD.
# MAGIC 
# MAGIC == Minute 23 ==
# MAGIC Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
# MAGIC You move to valve CC.
# MAGIC 
# MAGIC == Minute 24 ==
# MAGIC Valves BB, DD, EE, HH, and JJ are open, releasing <em>79</em> pressure.
# MAGIC You open valve CC.
# MAGIC 
# MAGIC == Minute 25 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC == Minute 26 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC == Minute 27 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC == Minute 28 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC == Minute 29 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC == Minute 30 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC </code></pre>
# MAGIC <p>This approach lets you release the most pressure possible in 30 minutes with this valve layout, <code><em>1651</em></code>.</p>
# MAGIC <p>Work out the steps to release the most pressure in 30 minutes. <em>What is the most pressure you can release?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Valve SW has flow rate=0; tunnels lead to valves LX, LD
Valve VS has flow rate=0; tunnels lead to valves JO, OO
Valve OO has flow rate=10; tunnels lead to valves KK, HD, VS, KI
Valve DZ has flow rate=8; tunnels lead to valves KV, GX, WQ, BA, PK
Valve GX has flow rate=0; tunnels lead to valves AA, DZ
Valve IF has flow rate=0; tunnels lead to valves OI, DW
Valve BO has flow rate=0; tunnels lead to valves UJ, ZT
Valve KI has flow rate=0; tunnels lead to valves OO, KU
Valve JT has flow rate=3; tunnels lead to valves FC, AM, KV, XP, XZ
Valve TQ has flow rate=0; tunnels lead to valves AA, DW
Valve KK has flow rate=0; tunnels lead to valves QW, OO
Valve NR has flow rate=0; tunnels lead to valves UG, XM
Valve VO has flow rate=0; tunnels lead to valves YR, AA
Valve MS has flow rate=17; tunnels lead to valves LT, LX
Valve JO has flow rate=0; tunnels lead to valves YR, VS
Valve ZB has flow rate=0; tunnels lead to valves UJ, LT
Valve ZT has flow rate=0; tunnels lead to valves XM, BO
Valve YR has flow rate=9; tunnels lead to valves VO, FY, WB, JO
Valve QS has flow rate=0; tunnels lead to valves QW, FY
Valve UD has flow rate=0; tunnels lead to valves CA, JB
Valve AP has flow rate=0; tunnels lead to valves CA, DW
Valve KV has flow rate=0; tunnels lead to valves JT, DZ
Valve JH has flow rate=0; tunnels lead to valves IK, UJ
Valve LD has flow rate=15; tunnels lead to valves IK, SW
Valve XK has flow rate=0; tunnels lead to valves XZ, BH
Valve XM has flow rate=11; tunnels lead to valves XP, CJ, ZT, NR
Valve FY has flow rate=0; tunnels lead to valves YR, QS
Valve GI has flow rate=22; tunnel leads to valve TI
Valve JB has flow rate=14; tunnels lead to valves WB, UD, WQ, HD
Valve DW has flow rate=6; tunnels lead to valves AP, TQ, NQ, IF, PK
Valve UJ has flow rate=13; tunnels lead to valves JH, ZB, BO
Valve KU has flow rate=0; tunnels lead to valves CA, KI
Valve WQ has flow rate=0; tunnels lead to valves JB, DZ
Valve BA has flow rate=0; tunnels lead to valves BH, DZ
Valve AA has flow rate=0; tunnels lead to valves YX, TQ, VO, GX, QP
Valve TI has flow rate=0; tunnels lead to valves GI, UG
Valve FC has flow rate=0; tunnels lead to valves QP, JT
Valve CA has flow rate=18; tunnels lead to valves KU, UD, AP
Valve QW has flow rate=25; tunnels lead to valves QS, KK
Valve XZ has flow rate=0; tunnels lead to valves JT, XK
Valve YX has flow rate=0; tunnels lead to valves AA, CJ
Valve OI has flow rate=0; tunnels lead to valves IF, BH
Valve NQ has flow rate=0; tunnels lead to valves AM, DW
Valve QP has flow rate=0; tunnels lead to valves AA, FC
Valve AM has flow rate=0; tunnels lead to valves NQ, JT
Valve XP has flow rate=0; tunnels lead to valves XM, JT
Valve BH has flow rate=12; tunnels lead to valves BA, XK, OI
Valve HD has flow rate=0; tunnels lead to valves OO, JB
Valve LT has flow rate=0; tunnels lead to valves MS, ZB
Valve LX has flow rate=0; tunnels lead to valves MS, SW
Valve CJ has flow rate=0; tunnels lead to valves XM, YX
Valve PK has flow rate=0; tunnels lead to valves DW, DZ
Valve IK has flow rate=0; tunnels lead to valves LD, JH
Valve WB has flow rate=0; tunnels lead to valves YR, JB
Valve UG has flow rate=21; tunnels lead to valves TI, NR'''

# COMMAND ----------

import collections
import functools
import re


@functools.cache
def shortest_path(start, end):
  if start == end:
    return 0
  
  queue = collections.deque([(0, start)])
  visited = set()
  while queue:
    t, pos = queue.pop()
    if pos in visited:
      continue
    visited.add(pos)
    
    if pos == end:
      return t
    
    for new_pos in valves[pos][1]:
      queue.appendleft((t + 1, new_pos))

  return float('inf')


@functools.cache
def maximize_pressure(pos, time_left, available_valves):
  max_pressure = 0

  for destination in available_valves:
    dt = min(shortest_path(pos, destination) + 1, time_left)
    new_time_left = time_left - dt
    pressure = new_time_left * valves[destination][0] + maximize_pressure(destination, new_time_left, available_valves - {destination})
    max_pressure = max(max_pressure, pressure)

  return max_pressure


valves = {}
for line in inp.splitlines():
  valve, *tunnel_to = re.findall(r'[A-Z][A-Z]', line)
  flow = re.findall(r'\d+', line)[0]
  valves[valve] = (int(flow), tunnel_to)

available_valves = frozenset({valve for valve, (pressure, _) in valves.items() if pressure > 0})
  
answer = maximize_pressure('AA', 30, available_valves)
answer # 6 seconds

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?</p>
# MAGIC <p>It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only <em>26 minutes</em> to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)</p>
# MAGIC <p>In the example above, you could teach the elephant to help you as follows:</p>
# MAGIC <pre><code>== Minute 1 ==
# MAGIC No valves are open.
# MAGIC You move to valve II.
# MAGIC The elephant moves to valve DD.
# MAGIC 
# MAGIC == Minute 2 ==
# MAGIC No valves are open.
# MAGIC You move to valve JJ.
# MAGIC The elephant opens valve DD.
# MAGIC 
# MAGIC == Minute 3 ==
# MAGIC Valve DD is open, releasing <em>20</em> pressure.
# MAGIC You open valve JJ.
# MAGIC The elephant moves to valve EE.
# MAGIC 
# MAGIC == Minute 4 ==
# MAGIC Valves DD and JJ are open, releasing <em>41</em> pressure.
# MAGIC You move to valve II.
# MAGIC The elephant moves to valve FF.
# MAGIC 
# MAGIC == Minute 5 ==
# MAGIC Valves DD and JJ are open, releasing <em>41</em> pressure.
# MAGIC You move to valve AA.
# MAGIC The elephant moves to valve GG.
# MAGIC 
# MAGIC == Minute 6 ==
# MAGIC Valves DD and JJ are open, releasing <em>41</em> pressure.
# MAGIC You move to valve BB.
# MAGIC The elephant moves to valve HH.
# MAGIC 
# MAGIC == Minute 7 ==
# MAGIC Valves DD and JJ are open, releasing <em>41</em> pressure.
# MAGIC You open valve BB.
# MAGIC The elephant opens valve HH.
# MAGIC 
# MAGIC == Minute 8 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You move to valve CC.
# MAGIC The elephant moves to valve GG.
# MAGIC 
# MAGIC == Minute 9 ==
# MAGIC Valves BB, DD, HH, and JJ are open, releasing <em>76</em> pressure.
# MAGIC You open valve CC.
# MAGIC The elephant moves to valve FF.
# MAGIC 
# MAGIC == Minute 10 ==
# MAGIC Valves BB, CC, DD, HH, and JJ are open, releasing <em>78</em> pressure.
# MAGIC The elephant moves to valve EE.
# MAGIC 
# MAGIC == Minute 11 ==
# MAGIC Valves BB, CC, DD, HH, and JJ are open, releasing <em>78</em> pressure.
# MAGIC The elephant opens valve EE.
# MAGIC 
# MAGIC (At this point, all valves are open.)
# MAGIC 
# MAGIC == Minute 12 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC == Minute 20 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC == Minute 26 ==
# MAGIC Valves BB, CC, DD, EE, HH, and JJ are open, releasing <em>81</em> pressure.
# MAGIC </code></pre>
# MAGIC <p>With the elephant helping, after 26 minutes, the best you could do would release a total of <code><em>1707</em></code> pressure.</p>
# MAGIC <p><em>With you and an elephant working together for 26 minutes, what is the most pressure you could release?</em></p>
# MAGIC </article>

# COMMAND ----------

import itertools


best = 0
for length in range(len(available_valves) // 2 + 1):
  for my_valves in itertools.combinations(available_valves, length):
    my_valves = frozenset(my_valves)
    elephant_valves = available_valves.difference(my_valves)
    total_pressure = maximize_pressure('AA', 26, my_valves) + maximize_pressure('AA', 26, elephant_valves)
    best = max(best, total_pressure)

answer = best
print(answer) # 1 minute
