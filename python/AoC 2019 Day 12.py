# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/12

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 12: The N-Body Problem ---</h2><p>The space near Jupiter is not a very safe place; you need to be careful of a <a href="https://en.wikipedia.org/wiki/Great_Red_Spot">big distracting red spot</a>, extreme <a href="https://en.wikipedia.org/wiki/Magnetosphere_of_Jupiter">radiation</a>, and a <a href="https://en.wikipedia.org/wiki/Moons_of_Jupiter#List">whole lot of moons</a> swirling around.  You decide to start by tracking the four largest moons: <em>Io</em>, <em>Europa</em>, <em>Ganymede</em>, and <em>Callisto</em>.</p>
# MAGIC <p>After a brief scan, you calculate the <em>position of each moon</em> (your puzzle input). You just need to <em>simulate their motion</em> so you can <span title="Or you could just leave, but where's the fun in that?">avoid them</span>.</p>
# MAGIC <p>Each moon has a 3-dimensional position (<code>x</code>, <code>y</code>, and <code>z</code>) and a 3-dimensional velocity.  The position of each moon is given in your scan; the <code>x</code>, <code>y</code>, and <code>z</code> velocity of each moon starts at <code>0</code>.</p>
# MAGIC <p>Simulate the motion of the moons in <em>time steps</em>. Within each time step, first update the velocity of every moon by applying <em>gravity</em>. Then, once all moons' velocities have been updated, update the position of every moon by applying <em>velocity</em>. Time progresses by one step once all of the positions are updated.</p>
# MAGIC <p>To apply <em>gravity</em>, consider every <em>pair</em> of moons. On each axis (<code>x</code>, <code>y</code>, and <code>z</code>), the velocity of each moon changes by <em>exactly +1 or -1</em> to pull the moons together.  For example, if Ganymede has an <code>x</code> position of <code>3</code>, and Callisto has a <code>x</code> position of <code>5</code>, then Ganymede's <code>x</code> velocity <em>changes by +1</em> (because <code>5 &gt; 3</code>) and Callisto's <code>x</code> velocity <em>changes by -1</em> (because <code>3 &lt; 5</code>). However, if the positions on a given axis are the same, the velocity on that axis <em>does not change</em> for that pair of moons.</p>
# MAGIC <p>Once all gravity has been applied, apply <em>velocity</em>: simply add the velocity of each moon to its own position. For example, if Europa has a position of <code>x=1, y=2, z=3</code> and a velocity of <code>x=-2, y=0,z=3</code>, then its new position would be <code>x=-1, y=2, z=6</code>. This process does not modify the velocity of any moon.</p>
# MAGIC <p>For example, suppose your scan reveals the following positions:</p>
# MAGIC <pre><code>&lt;x=-1, y=0, z=2&gt;
# MAGIC &lt;x=2, y=-10, z=-7&gt;
# MAGIC &lt;x=4, y=-8, z=8&gt;
# MAGIC &lt;x=3, y=5, z=-1&gt;
# MAGIC </code></pre>
# MAGIC <p>Simulating the motion of these moons would produce the following:</p>
# MAGIC <pre><code>After 0 steps:
# MAGIC pos=&lt;x=-1, y=  0, z= 2&gt;, vel=&lt;x= 0, y= 0, z= 0&gt;
# MAGIC pos=&lt;x= 2, y=-10, z=-7&gt;, vel=&lt;x= 0, y= 0, z= 0&gt;
# MAGIC pos=&lt;x= 4, y= -8, z= 8&gt;, vel=&lt;x= 0, y= 0, z= 0&gt;
# MAGIC pos=&lt;x= 3, y=  5, z=-1&gt;, vel=&lt;x= 0, y= 0, z= 0&gt;
# MAGIC 
# MAGIC After 1 step:
# MAGIC pos=&lt;x= 2, y=-1, z= 1&gt;, vel=&lt;x= 3, y=-1, z=-1&gt;
# MAGIC pos=&lt;x= 3, y=-7, z=-4&gt;, vel=&lt;x= 1, y= 3, z= 3&gt;
# MAGIC pos=&lt;x= 1, y=-7, z= 5&gt;, vel=&lt;x=-3, y= 1, z=-3&gt;
# MAGIC pos=&lt;x= 2, y= 2, z= 0&gt;, vel=&lt;x=-1, y=-3, z= 1&gt;
# MAGIC 
# MAGIC After 2 steps:
# MAGIC pos=&lt;x= 5, y=-3, z=-1&gt;, vel=&lt;x= 3, y=-2, z=-2&gt;
# MAGIC pos=&lt;x= 1, y=-2, z= 2&gt;, vel=&lt;x=-2, y= 5, z= 6&gt;
# MAGIC pos=&lt;x= 1, y=-4, z=-1&gt;, vel=&lt;x= 0, y= 3, z=-6&gt;
# MAGIC pos=&lt;x= 1, y=-4, z= 2&gt;, vel=&lt;x=-1, y=-6, z= 2&gt;
# MAGIC 
# MAGIC After 3 steps:
# MAGIC pos=&lt;x= 5, y=-6, z=-1&gt;, vel=&lt;x= 0, y=-3, z= 0&gt;
# MAGIC pos=&lt;x= 0, y= 0, z= 6&gt;, vel=&lt;x=-1, y= 2, z= 4&gt;
# MAGIC pos=&lt;x= 2, y= 1, z=-5&gt;, vel=&lt;x= 1, y= 5, z=-4&gt;
# MAGIC pos=&lt;x= 1, y=-8, z= 2&gt;, vel=&lt;x= 0, y=-4, z= 0&gt;
# MAGIC 
# MAGIC After 4 steps:
# MAGIC pos=&lt;x= 2, y=-8, z= 0&gt;, vel=&lt;x=-3, y=-2, z= 1&gt;
# MAGIC pos=&lt;x= 2, y= 1, z= 7&gt;, vel=&lt;x= 2, y= 1, z= 1&gt;
# MAGIC pos=&lt;x= 2, y= 3, z=-6&gt;, vel=&lt;x= 0, y= 2, z=-1&gt;
# MAGIC pos=&lt;x= 2, y=-9, z= 1&gt;, vel=&lt;x= 1, y=-1, z=-1&gt;
# MAGIC 
# MAGIC After 5 steps:
# MAGIC pos=&lt;x=-1, y=-9, z= 2&gt;, vel=&lt;x=-3, y=-1, z= 2&gt;
# MAGIC pos=&lt;x= 4, y= 1, z= 5&gt;, vel=&lt;x= 2, y= 0, z=-2&gt;
# MAGIC pos=&lt;x= 2, y= 2, z=-4&gt;, vel=&lt;x= 0, y=-1, z= 2&gt;
# MAGIC pos=&lt;x= 3, y=-7, z=-1&gt;, vel=&lt;x= 1, y= 2, z=-2&gt;
# MAGIC 
# MAGIC After 6 steps:
# MAGIC pos=&lt;x=-1, y=-7, z= 3&gt;, vel=&lt;x= 0, y= 2, z= 1&gt;
# MAGIC pos=&lt;x= 3, y= 0, z= 0&gt;, vel=&lt;x=-1, y=-1, z=-5&gt;
# MAGIC pos=&lt;x= 3, y=-2, z= 1&gt;, vel=&lt;x= 1, y=-4, z= 5&gt;
# MAGIC pos=&lt;x= 3, y=-4, z=-2&gt;, vel=&lt;x= 0, y= 3, z=-1&gt;
# MAGIC 
# MAGIC After 7 steps:
# MAGIC pos=&lt;x= 2, y=-2, z= 1&gt;, vel=&lt;x= 3, y= 5, z=-2&gt;
# MAGIC pos=&lt;x= 1, y=-4, z=-4&gt;, vel=&lt;x=-2, y=-4, z=-4&gt;
# MAGIC pos=&lt;x= 3, y=-7, z= 5&gt;, vel=&lt;x= 0, y=-5, z= 4&gt;
# MAGIC pos=&lt;x= 2, y= 0, z= 0&gt;, vel=&lt;x=-1, y= 4, z= 2&gt;
# MAGIC 
# MAGIC After 8 steps:
# MAGIC pos=&lt;x= 5, y= 2, z=-2&gt;, vel=&lt;x= 3, y= 4, z=-3&gt;
# MAGIC pos=&lt;x= 2, y=-7, z=-5&gt;, vel=&lt;x= 1, y=-3, z=-1&gt;
# MAGIC pos=&lt;x= 0, y=-9, z= 6&gt;, vel=&lt;x=-3, y=-2, z= 1&gt;
# MAGIC pos=&lt;x= 1, y= 1, z= 3&gt;, vel=&lt;x=-1, y= 1, z= 3&gt;
# MAGIC 
# MAGIC After 9 steps:
# MAGIC pos=&lt;x= 5, y= 3, z=-4&gt;, vel=&lt;x= 0, y= 1, z=-2&gt;
# MAGIC pos=&lt;x= 2, y=-9, z=-3&gt;, vel=&lt;x= 0, y=-2, z= 2&gt;
# MAGIC pos=&lt;x= 0, y=-8, z= 4&gt;, vel=&lt;x= 0, y= 1, z=-2&gt;
# MAGIC pos=&lt;x= 1, y= 1, z= 5&gt;, vel=&lt;x= 0, y= 0, z= 2&gt;
# MAGIC 
# MAGIC After 10 steps:
# MAGIC pos=&lt;x= 2, y= 1, z=-3&gt;, vel=&lt;x=-3, y=-2, z= 1&gt;
# MAGIC pos=&lt;x= 1, y=-8, z= 0&gt;, vel=&lt;x=-1, y= 1, z= 3&gt;
# MAGIC pos=&lt;x= 3, y=-6, z= 1&gt;, vel=&lt;x= 3, y= 2, z=-3&gt;
# MAGIC pos=&lt;x= 2, y= 0, z= 4&gt;, vel=&lt;x= 1, y=-1, z=-1&gt;
# MAGIC </code></pre>
# MAGIC <p>Then, it might help to calculate the <em>total energy in the system</em>. The total energy for a single moon is its <em>potential energy</em> multiplied by its <em>kinetic energy</em>. A moon's <em>potential energy</em> is the sum of the <a href="https://en.wikipedia.org/wiki/Absolute_value">absolute values</a> of its <code>x</code>, <code>y</code>, and <code>z</code> position coordinates. A moon's <em>kinetic energy</em> is the sum of the absolute values of its velocity coordinates.  Below, each line shows the calculations for a moon's potential energy (<code>pot</code>), kinetic energy (<code>kin</code>), and total energy:</p>
# MAGIC <pre><code>Energy after 10 steps:
# MAGIC pot: 2 + 1 + 3 =  6;   kin: 3 + 2 + 1 = 6;   total:  6 * 6 = 36
# MAGIC pot: 1 + 8 + 0 =  9;   kin: 1 + 1 + 3 = 5;   total:  9 * 5 = 45
# MAGIC pot: 3 + 6 + 1 = 10;   kin: 3 + 2 + 3 = 8;   total: 10 * 8 = 80
# MAGIC pot: 2 + 0 + 4 =  6;   kin: 1 + 1 + 1 = 3;   total:  6 * 3 = 18
# MAGIC Sum of total energy: 36 + 45 + 80 + 18 = <em>179</em>
# MAGIC </code></pre>
# MAGIC <p>In the above example, adding together the total energy for all moons after 10 steps produces the total energy in the system, <code><em>179</em></code>.</p>
# MAGIC <p>Here's a second example:</p>
# MAGIC <pre><code>&lt;x=-8, y=-10, z=0&gt;
# MAGIC &lt;x=5, y=5, z=10&gt;
# MAGIC &lt;x=2, y=-7, z=3&gt;
# MAGIC &lt;x=9, y=-8, z=-3&gt;
# MAGIC </code></pre>
# MAGIC <p>Every ten steps of simulation for 100 steps produces:</p>
# MAGIC <pre><code>After 0 steps:
# MAGIC pos=&lt;x= -8, y=-10, z=  0&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  5, y=  5, z= 10&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  2, y= -7, z=  3&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  9, y= -8, z= -3&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC 
# MAGIC After 10 steps:
# MAGIC pos=&lt;x= -9, y=-10, z=  1&gt;, vel=&lt;x= -2, y= -2, z= -1&gt;
# MAGIC pos=&lt;x=  4, y= 10, z=  9&gt;, vel=&lt;x= -3, y=  7, z= -2&gt;
# MAGIC pos=&lt;x=  8, y=-10, z= -3&gt;, vel=&lt;x=  5, y= -1, z= -2&gt;
# MAGIC pos=&lt;x=  5, y=-10, z=  3&gt;, vel=&lt;x=  0, y= -4, z=  5&gt;
# MAGIC 
# MAGIC After 20 steps:
# MAGIC pos=&lt;x=-10, y=  3, z= -4&gt;, vel=&lt;x= -5, y=  2, z=  0&gt;
# MAGIC pos=&lt;x=  5, y=-25, z=  6&gt;, vel=&lt;x=  1, y=  1, z= -4&gt;
# MAGIC pos=&lt;x= 13, y=  1, z=  1&gt;, vel=&lt;x=  5, y= -2, z=  2&gt;
# MAGIC pos=&lt;x=  0, y=  1, z=  7&gt;, vel=&lt;x= -1, y= -1, z=  2&gt;
# MAGIC 
# MAGIC After 30 steps:
# MAGIC pos=&lt;x= 15, y= -6, z= -9&gt;, vel=&lt;x= -5, y=  4, z=  0&gt;
# MAGIC pos=&lt;x= -4, y=-11, z=  3&gt;, vel=&lt;x= -3, y=-10, z=  0&gt;
# MAGIC pos=&lt;x=  0, y= -1, z= 11&gt;, vel=&lt;x=  7, y=  4, z=  3&gt;
# MAGIC pos=&lt;x= -3, y= -2, z=  5&gt;, vel=&lt;x=  1, y=  2, z= -3&gt;
# MAGIC 
# MAGIC After 40 steps:
# MAGIC pos=&lt;x= 14, y=-12, z= -4&gt;, vel=&lt;x= 11, y=  3, z=  0&gt;
# MAGIC pos=&lt;x= -1, y= 18, z=  8&gt;, vel=&lt;x= -5, y=  2, z=  3&gt;
# MAGIC pos=&lt;x= -5, y=-14, z=  8&gt;, vel=&lt;x=  1, y= -2, z=  0&gt;
# MAGIC pos=&lt;x=  0, y=-12, z= -2&gt;, vel=&lt;x= -7, y= -3, z= -3&gt;
# MAGIC 
# MAGIC After 50 steps:
# MAGIC pos=&lt;x=-23, y=  4, z=  1&gt;, vel=&lt;x= -7, y= -1, z=  2&gt;
# MAGIC pos=&lt;x= 20, y=-31, z= 13&gt;, vel=&lt;x=  5, y=  3, z=  4&gt;
# MAGIC pos=&lt;x= -4, y=  6, z=  1&gt;, vel=&lt;x= -1, y=  1, z= -3&gt;
# MAGIC pos=&lt;x= 15, y=  1, z= -5&gt;, vel=&lt;x=  3, y= -3, z= -3&gt;
# MAGIC 
# MAGIC After 60 steps:
# MAGIC pos=&lt;x= 36, y=-10, z=  6&gt;, vel=&lt;x=  5, y=  0, z=  3&gt;
# MAGIC pos=&lt;x=-18, y= 10, z=  9&gt;, vel=&lt;x= -3, y= -7, z=  5&gt;
# MAGIC pos=&lt;x=  8, y=-12, z= -3&gt;, vel=&lt;x= -2, y=  1, z= -7&gt;
# MAGIC pos=&lt;x=-18, y= -8, z= -2&gt;, vel=&lt;x=  0, y=  6, z= -1&gt;
# MAGIC 
# MAGIC After 70 steps:
# MAGIC pos=&lt;x=-33, y= -6, z=  5&gt;, vel=&lt;x= -5, y= -4, z=  7&gt;
# MAGIC pos=&lt;x= 13, y= -9, z=  2&gt;, vel=&lt;x= -2, y= 11, z=  3&gt;
# MAGIC pos=&lt;x= 11, y= -8, z=  2&gt;, vel=&lt;x=  8, y= -6, z= -7&gt;
# MAGIC pos=&lt;x= 17, y=  3, z=  1&gt;, vel=&lt;x= -1, y= -1, z= -3&gt;
# MAGIC 
# MAGIC After 80 steps:
# MAGIC pos=&lt;x= 30, y= -8, z=  3&gt;, vel=&lt;x=  3, y=  3, z=  0&gt;
# MAGIC pos=&lt;x= -2, y= -4, z=  0&gt;, vel=&lt;x=  4, y=-13, z=  2&gt;
# MAGIC pos=&lt;x=-18, y= -7, z= 15&gt;, vel=&lt;x= -8, y=  2, z= -2&gt;
# MAGIC pos=&lt;x= -2, y= -1, z= -8&gt;, vel=&lt;x=  1, y=  8, z=  0&gt;
# MAGIC 
# MAGIC After 90 steps:
# MAGIC pos=&lt;x=-25, y= -1, z=  4&gt;, vel=&lt;x=  1, y= -3, z=  4&gt;
# MAGIC pos=&lt;x=  2, y= -9, z=  0&gt;, vel=&lt;x= -3, y= 13, z= -1&gt;
# MAGIC pos=&lt;x= 32, y= -8, z= 14&gt;, vel=&lt;x=  5, y= -4, z=  6&gt;
# MAGIC pos=&lt;x= -1, y= -2, z= -8&gt;, vel=&lt;x= -3, y= -6, z= -9&gt;
# MAGIC 
# MAGIC After 100 steps:
# MAGIC pos=&lt;x=  8, y=-12, z= -9&gt;, vel=&lt;x= -7, y=  3, z=  0&gt;
# MAGIC pos=&lt;x= 13, y= 16, z= -3&gt;, vel=&lt;x=  3, y=-11, z= -5&gt;
# MAGIC pos=&lt;x=-29, y=-11, z= -1&gt;, vel=&lt;x= -3, y=  7, z=  4&gt;
# MAGIC pos=&lt;x= 16, y=-13, z= 23&gt;, vel=&lt;x=  7, y=  1, z=  1&gt;
# MAGIC 
# MAGIC Energy after 100 steps:
# MAGIC pot:  8 + 12 +  9 = 29;   kin: 7 +  3 + 0 = 10;   total: 29 * 10 = 290
# MAGIC pot: 13 + 16 +  3 = 32;   kin: 3 + 11 + 5 = 19;   total: 32 * 19 = 608
# MAGIC pot: 29 + 11 +  1 = 41;   kin: 3 +  7 + 4 = 14;   total: 41 * 14 = 574
# MAGIC pot: 16 + 13 + 23 = 52;   kin: 7 +  1 + 1 =  9;   total: 52 *  9 = 468
# MAGIC Sum of total energy: 290 + 608 + 574 + 468 = <em>1940</em>
# MAGIC </code></pre>
# MAGIC <p><em>What is the total energy in the system</em> after simulating the moons given in your scan for <code>1000</code> steps?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''<x=-7, y=-8, z=9>
<x=-12, y=-3, z=-4>
<x=6, y=-17, z=-9>
<x=4, y=-10, z=-6>'''

# COMMAND ----------

import copy
import re

def update_dimension(dimension):
  for pos_vel in dimension:
    pos_vel[1] += sum(1 if pos2 > pos_vel[0] else -1 for pos2, _ in dimension if pos2 != pos_vel[0])

  for pos_vel in dimension:
    pos_vel[0] += pos_vel[1]

start_state = list(zip(*[[[int(x), 0] for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]))

state = copy.deepcopy(start_state)
for _ in range(1000):
  for dimension in state:
    update_dimension(dimension)

answer = sum(sum(abs(pos) for pos, _ in moon) * sum(abs(vel) for _, vel in moon) for moon in zip(*state))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>All this drifting around in space makes you wonder about the nature of the universe.  Does history really repeat itself?  You're curious whether the moons will ever return to a previous state.</p>
# MAGIC <p>Determine <em>the number of steps</em> that must occur before all of the moons' <em>positions and velocities</em> exactly match a previous point in time.</p>
# MAGIC <p>For example, the first example above takes <code>2772</code> steps before they exactly match a previous point in time; it eventually returns to the initial state:</p>
# MAGIC <pre><code>After 0 steps:
# MAGIC pos=&lt;x= -1, y=  0, z=  2&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  2, y=-10, z= -7&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  4, y= -8, z=  8&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  3, y=  5, z= -1&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC 
# MAGIC After 2770 steps:
# MAGIC pos=&lt;x=  2, y= -1, z=  1&gt;, vel=&lt;x= -3, y=  2, z=  2&gt;
# MAGIC pos=&lt;x=  3, y= -7, z= -4&gt;, vel=&lt;x=  2, y= -5, z= -6&gt;
# MAGIC pos=&lt;x=  1, y= -7, z=  5&gt;, vel=&lt;x=  0, y= -3, z=  6&gt;
# MAGIC pos=&lt;x=  2, y=  2, z=  0&gt;, vel=&lt;x=  1, y=  6, z= -2&gt;
# MAGIC 
# MAGIC After 2771 steps:
# MAGIC pos=&lt;x= -1, y=  0, z=  2&gt;, vel=&lt;x= -3, y=  1, z=  1&gt;
# MAGIC pos=&lt;x=  2, y=-10, z= -7&gt;, vel=&lt;x= -1, y= -3, z= -3&gt;
# MAGIC pos=&lt;x=  4, y= -8, z=  8&gt;, vel=&lt;x=  3, y= -1, z=  3&gt;
# MAGIC pos=&lt;x=  3, y=  5, z= -1&gt;, vel=&lt;x=  1, y=  3, z= -1&gt;
# MAGIC 
# MAGIC After 2772 steps:
# MAGIC pos=&lt;x= -1, y=  0, z=  2&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  2, y=-10, z= -7&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  4, y= -8, z=  8&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC pos=&lt;x=  3, y=  5, z= -1&gt;, vel=&lt;x=  0, y=  0, z=  0&gt;
# MAGIC </code></pre>
# MAGIC <p>Of course, the universe might last for a <em>very long time</em> before repeating.  Here's a copy of the second example from above:</p>
# MAGIC <pre><code>&lt;x=-8, y=-10, z=0&gt;
# MAGIC &lt;x=5, y=5, z=10&gt;
# MAGIC &lt;x=2, y=-7, z=3&gt;
# MAGIC &lt;x=9, y=-8, z=-3&gt;
# MAGIC </code></pre>
# MAGIC <p>This set of initial positions takes <code>4686774924</code> steps before it repeats a previous state! Clearly, you might need to <em>find a more efficient way to simulate the universe</em>.</p>
# MAGIC <p><em>How many steps does it take</em> to reach the first state that exactly matches a previous state?</p>
# MAGIC </article>

# COMMAND ----------

import functools
import itertools

def gcd(a, b):
  while b:      
    a, b = b, a % b
  return a

def lcm(a, b):
  return a * b // gcd(a, b)

def find_cycle(dimension):
  seen = set()
  for i in itertools.count():
    t = tuple(tuple(x) for x in dimension)
    if t in seen:
      return i
    seen.add(t)
    update_dimension(dimension)

cycles = [find_cycle(dimension) for dimension in copy.deepcopy(start_state)]

answer = functools.reduce(lcm, cycles)
print(answer)
