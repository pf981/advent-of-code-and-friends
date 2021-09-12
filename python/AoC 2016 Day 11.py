# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/11

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 11: Radioisotope Thermoelectric Generators ---</h2><p>You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby.  There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".</p>
# MAGIC <p>According to the project status board, this facility is currently being used to experiment with <a href="https://en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator">Radioisotope Thermoelectric Generators</a> (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.</p>
# MAGIC <p>The <span title="The previous version, model number PB-NUK, used Blutonium.">experimental RTGs</span> have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to <em>generate an electromagnetic radiation shield when powered</em>.  Unfortunately, they can <em>only</em> be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.</p>
# MAGIC <p>In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be <em>fried</em>. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.</p>
# MAGIC <p>These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them.  The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.</p>
# MAGIC <p>Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)</p>
# MAGIC <p>You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.</p>
# MAGIC <p>When you enter the containment area, you and the elevator will start on the first floor.</p>
# MAGIC <p>For example, suppose the isolated area has the following arrangement:</p>
# MAGIC <pre class="wrap"><code>The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# MAGIC The second floor contains a hydrogen generator.
# MAGIC The third floor contains a lithium generator.
# MAGIC The fourth floor contains nothing relevant.
# MAGIC </code></pre>
# MAGIC <p>As a diagram (<code>F#</code> for a Floor number, <code>E</code> for Elevator, <code>H</code> for Hydrogen, <code>L</code> for Lithium, <code>M</code> for Microchip, and <code>G</code> for Generator), the initial state looks like this:</p>
# MAGIC <pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  .  .  LG .  
# MAGIC F2 .  HG .  .  .  
# MAGIC F1 E  .  HM .  LM 
# MAGIC </code></pre>
# MAGIC <p>Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:</p>
# MAGIC <ul>
# MAGIC <li><p>Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  .  .  LG .  
# MAGIC F2 E  HG HM .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 E  HG HM LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 E  .  HM .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 E  .  HM .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips up one floor, where there is nothing to fry them:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 E  .  HM .  LM 
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 E  HG HM LG LM 
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips to the fourth floor:</p><pre><code>F4 E  .  HM .  LM 
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:</p><pre><code>F4 .  .  .  .  LM 
# MAGIC F3 E  HG HM LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:</p><pre><code>F4 E  HG .  LG LM 
# MAGIC F3 .  .  HM .  .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring the Lithium Microchip with you to the third floor so you can use the elevator:</p><pre><code>F4 .  HG .  LG .  
# MAGIC F3 E  .  HM .  LM 
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips to the fourth floor:</p><pre><code>F4 E  HG HM LG LM 
# MAGIC F3 .  .  .  .  .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC </ul>
# MAGIC <p>In this arrangement, it takes <code>11</code> steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)</p>
# MAGIC <p>In your situation, what is the <em>minimum number of steps</em> required to bring all of the objects to the fourth floor?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.'''

# COMMAND ----------

import collections
import copy
import heapq
import itertools

def comb(l, take_min, take_max):
  return itertools.chain.from_iterable(itertools.combinations(l, r) for r in range(take_min, take_max+1))

def is_valid(floors):
  for floor in floors:
    contains_generator = False
    contains_exposed_microchip = False
    
    for element, object_type in floor:
      if object_type == 'generator':
        contains_generator = True
      if object_type == 'microchip' and (element, 'generator') not in floor:
        contains_exposed_microchip = True
      
    if contains_generator and contains_exposed_microchip:
      return False
  
  return True

def hashable_floors(floors):
  d = collections.defaultdict(lambda: [None]*2)
  for i, floor in enumerate(floors):
    for element, object_type in floor:
      d[element][object_type == 'microchip'] = i
  return tuple(sorted(tuple(x) for x in d.values()))

def solve(start_floors):
  visited = set((hashable_floors(start_floors), 0))
  states = [(0, copy.deepcopy(start_floors), 0)]
  min_solution = float('inf')
  
  while states:
    n_moves, floors, elevator = heapq.heappop(states)

    for new_elevator in (elevator - 1, elevator + 1):
      if new_elevator < 0 or new_elevator >= len(floors):
        continue
      
      for items in comb(floors[elevator], 1, 2):
        new_floors = copy.deepcopy(floors)
        for item in items:
          new_floors[elevator].remove(item)
          new_floors[new_elevator].add(item)
        
        if not is_valid(new_floors) or (hashable_floors(new_floors), new_elevator) in visited:
          continue
        visited.add((hashable_floors(new_floors), new_elevator))
        
        if all(len(floor) == 0 for floor in new_floors[:-1]):
          min_solution = min(n_moves + 1, min_solution)
        
        heapq.heappush(states, (n_moves + 1, new_floors, new_elevator))
  return min_solution

# COMMAND ----------

import re

start_floors = [set(re.findall(r'([\w+-]+?)(?:-compatible)?(?: )(microchip|generator)', line)) for line in inp.split('\n')]

answer = solve(start_floors)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.</p>
# MAGIC <p>Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:</p>
# MAGIC <ul>
# MAGIC <li>An elerium generator.</li>
# MAGIC <li>An elerium-compatible microchip.</li>
# MAGIC <li>A dilithium generator.</li>
# MAGIC <li>A dilithium-compatible microchip.</li>
# MAGIC </ul>
# MAGIC <p>These work just like the other generators and microchips. You'll have to get them up to assembly as well.</p>
# MAGIC <p>What is the <em>minimum number of steps</em> required to bring all of the objects, including these four new ones, to the fourth floor?</p>
# MAGIC </article>

# COMMAND ----------

start_floors[0].add(('elerium', 'generator'))
start_floors[0].add(('elerium', 'microchip'))
start_floors[0].add(('dilithium', 'generator'))
start_floors[0].add(('dilithium', 'microchip'))

answer = solve(start_floors)
answer
