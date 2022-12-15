# Databricks notebook source
# MAGIC %pip install z3-solver

# COMMAND ----------

# MAGIC %md https://adventofcode.com/2022/day/15

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 15: Beacon Exclusion Zone ---</h2><p>You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable <em>sensors</em> that you imagine were originally built to locate lost Elves.</p>
# MAGIC <p>The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.</p>
# MAGIC <p>Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source <em>beacon</em>. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can <em>determine the position of a beacon precisely</em>; however, sensors can only lock on to the one beacon <em>closest to the sensor</em> as measured by the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry" target="_blank">Manhattan distance</a>. (There is never a tie where two beacons are the same distance to a sensor.)</p>
# MAGIC <p>It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:</p>
# MAGIC <pre><code>Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# MAGIC Sensor at x=9, y=16: closest beacon is at x=10, y=16
# MAGIC Sensor at x=13, y=2: closest beacon is at x=15, y=3
# MAGIC Sensor at x=12, y=14: closest beacon is at x=10, y=16
# MAGIC Sensor at x=10, y=20: closest beacon is at x=10, y=16
# MAGIC Sensor at x=14, y=17: closest beacon is at x=10, y=16
# MAGIC Sensor at x=8, y=7: closest beacon is at x=2, y=10
# MAGIC Sensor at x=2, y=0: closest beacon is at x=2, y=10
# MAGIC Sensor at x=0, y=11: closest beacon is at x=2, y=10
# MAGIC Sensor at x=20, y=14: closest beacon is at x=25, y=17
# MAGIC Sensor at x=17, y=20: closest beacon is at x=21, y=22
# MAGIC Sensor at x=16, y=7: closest beacon is at x=15, y=3
# MAGIC Sensor at x=14, y=3: closest beacon is at x=15, y=3
# MAGIC Sensor at x=20, y=1: closest beacon is at x=15, y=3
# MAGIC </code></pre>
# MAGIC <p>So, consider the sensor at <code>2,18</code>; the closest beacon to it is at <code>-2,15</code>. For the sensor at <code>9,16</code>, the closest beacon to it is at <code>10,16</code>.</p>
# MAGIC <p>Drawing sensors as <code>S</code> and beacons as <code>B</code>, the above arrangement of sensors and beacons looks like this:</p>
# MAGIC <pre><code>               1    1    2    2
# MAGIC      0    5    0    5    0    5
# MAGIC  0 ....S.......................
# MAGIC  1 ......................S.....
# MAGIC  2 ...............S............
# MAGIC  3 ................SB..........
# MAGIC  4 ............................
# MAGIC  5 ............................
# MAGIC  6 ............................
# MAGIC  7 ..........S.......S.........
# MAGIC  8 ............................
# MAGIC  9 ............................
# MAGIC 10 ....B.......................
# MAGIC 11 ..S.........................
# MAGIC 12 ............................
# MAGIC 13 ............................
# MAGIC 14 ..............S.......S.....
# MAGIC 15 B...........................
# MAGIC 16 ...........SB...............
# MAGIC 17 ................S..........B
# MAGIC 18 ....S.......................
# MAGIC 19 ............................
# MAGIC 20 ............S......S........
# MAGIC 21 ............................
# MAGIC 22 .......................B....
# MAGIC </code></pre>
# MAGIC <p>This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at <code>8,7</code>:</p>
# MAGIC <pre><code>               1    1    2    2
# MAGIC      0    5    0    5    0    5
# MAGIC -2 ..........#.................
# MAGIC -1 .........###................
# MAGIC  0 ....S...#####...............
# MAGIC  1 .......#######........S.....
# MAGIC  2 ......#########S............
# MAGIC  3 .....###########SB..........
# MAGIC  4 ....#############...........
# MAGIC  5 ...###############..........
# MAGIC  6 ..#################.........
# MAGIC  7 .#########<em>S</em>#######S#........
# MAGIC  8 ..#################.........
# MAGIC  9 ...###############..........
# MAGIC 10 ....<em>B</em>############...........
# MAGIC 11 ..S..###########............
# MAGIC 12 ......#########.............
# MAGIC 13 .......#######..............
# MAGIC 14 ........#####.S.......S.....
# MAGIC 15 B........###................
# MAGIC 16 ..........#SB...............
# MAGIC 17 ................S..........B
# MAGIC 18 ....S.......................
# MAGIC 19 ............................
# MAGIC 20 ............S......S........
# MAGIC 21 ............................
# MAGIC 22 .......................B....
# MAGIC </code></pre>
# MAGIC <p>This sensor's closest beacon is at <code>2,10</code>, and so you know there are no beacons that close or closer (in any positions marked <code>#</code>).</p>
# MAGIC <p>None of the detected beacons seem to be producing the distress signal, so you'll need to <span title="&quot;When you have eliminated all which is impossible, then whatever remains, however improbable, must be where the missing beacon is.&quot; - Sherlock Holmes">work out</span> where the distress beacon is by working out where it <em>isn't</em>. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.</p>
# MAGIC <p>So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where <code>y=10</code>, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:</p>
# MAGIC <pre><code>                 1    1    2    2
# MAGIC        0    5    0    5    0    5
# MAGIC  9 ...#########################...
# MAGIC <em>10 ..####B######################..</em>
# MAGIC 11 .###S#############.###########.
# MAGIC </code></pre>
# MAGIC <p>In this example, in the row where <code>y=10</code>, there are <code><em>26</em></code> positions where a beacon cannot be present.</p>
# MAGIC <p>Consult the report from the sensors you just deployed. <em>In the row where <code>y=2000000</code>, how many positions cannot contain a beacon?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Sensor at x=2765643, y=3042538: closest beacon is at x=2474133, y=3521072
Sensor at x=2745662, y=2324735: closest beacon is at x=2491341, y=1883354
Sensor at x=2015742, y=2904055: closest beacon is at x=2474133, y=3521072
Sensor at x=3375262, y=3203288: closest beacon is at x=3321219, y=3415236
Sensor at x=3276468, y=3892409: closest beacon is at x=3321219, y=3415236
Sensor at x=952573, y=3147055: closest beacon is at x=-41010, y=2905006
Sensor at x=1823659, y=1779343: closest beacon is at x=1592718, y=2000000
Sensor at x=1156328, y=865741: closest beacon is at x=1592718, y=2000000
Sensor at x=3938443, y=271482: closest beacon is at x=4081274, y=1177185
Sensor at x=2815232, y=1641178: closest beacon is at x=2491341, y=1883354
Sensor at x=3984799, y=3424711: closest beacon is at x=3321219, y=3415236
Sensor at x=1658825, y=3999931: closest beacon is at x=2474133, y=3521072
Sensor at x=3199859, y=1285962: closest beacon is at x=4081274, y=1177185
Sensor at x=3538649, y=2788193: closest beacon is at x=3725736, y=2414539
Sensor at x=3522208, y=3336284: closest beacon is at x=3321219, y=3415236
Sensor at x=3093758, y=3492396: closest beacon is at x=3321219, y=3415236
Sensor at x=2464979, y=562119: closest beacon is at x=2491341, y=1883354
Sensor at x=3665010, y=1556840: closest beacon is at x=3735739, y=2128164
Sensor at x=207525, y=3893957: closest beacon is at x=-41010, y=2905006
Sensor at x=3894678, y=1974599: closest beacon is at x=3735739, y=2128164
Sensor at x=2185146, y=3822275: closest beacon is at x=2474133, y=3521072
Sensor at x=31166, y=1467978: closest beacon is at x=-41010, y=2905006
Sensor at x=3242364, y=3335961: closest beacon is at x=3321219, y=3415236
Sensor at x=3773718, y=3999789: closest beacon is at x=3321219, y=3415236
Sensor at x=423046, y=2227938: closest beacon is at x=-41010, y=2905006
Sensor at x=1600225, y=2529059: closest beacon is at x=1592718, y=2000000
Sensor at x=3291752, y=2241389: closest beacon is at x=3735739, y=2128164
Sensor at x=2741333, y=3984346: closest beacon is at x=2474133, y=3521072
Sensor at x=3935288, y=2292902: closest beacon is at x=3725736, y=2414539
Sensor at x=291635, y=140996: closest beacon is at x=212146, y=-1154950
Sensor at x=3966296, y=2600346: closest beacon is at x=3725736, y=2414539
Sensor at x=2228916, y=1461096: closest beacon is at x=2491341, y=1883354'''

# COMMAND ----------

import re

sensors = [[int(x) for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]

target_y = 2000000
target_in_range = set()
target_beacons = set()
for x, y, bx, by in sensors:
  if by == target_y:
    target_beacons.add(bx)
    
  d = abs(x - bx) + abs(y - by)
  dx = d - abs(y - target_y)
  for x2 in range(x - dx, x + dx + 1):
    target_in_range.add(x2)
    
answer = len(target_in_range.difference(target_beacons))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have <code>x</code> and <code>y</code> coordinates each no lower than <code>0</code> and no larger than <code>4000000</code>.</p>
# MAGIC <p>To isolate the distress beacon's signal, you need to determine its <em>tuning frequency</em>, which can be found by multiplying its <code>x</code> coordinate by <code>4000000</code> and then adding its <code>y</code> coordinate.</p>
# MAGIC <p>In the example above, the search space is smaller: instead, the <code>x</code> and <code>y</code> coordinates can each be at most <code>20</code>. With this reduced search area, there is only a single position that could have a beacon: <code>x=14, y=11</code>. The tuning frequency for this distress beacon is <code><em>56000011</em></code>.</p>
# MAGIC <p>Find the only possible position for the distress beacon. <em>What is its tuning frequency?</em></p>
# MAGIC </article>

# COMMAND ----------

import z3

def Abs(X):
  return z3.If(X >= 0, X, -X)

X = z3.Int('X')
Y = z3.Int('Y')

o = z3.Optimize()
o.add(X >= 0)
o.add(Y >= 0)
o.add(X <= 4000000)
o.add(Y <= 4000000)

for x, y, bx, by in sensors:
  d = abs(x - bx) + abs(y - by)
  o.add(Abs(X - x) + Abs(Y - y) > d)

o.check()
answer = o.model().eval(X * 4000000 + Y)
print(answer)
