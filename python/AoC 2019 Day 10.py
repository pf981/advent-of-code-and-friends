# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/10

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 10: Monitoring Station ---</h2><p>You fly into the asteroid belt and reach the Ceres monitoring station.  The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.</p>
# MAGIC <p>The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).</p>
# MAGIC <p>The map indicates whether each position is empty (<code>.</code>) or contains an asteroid (<code>#</code>).  The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position.  The asteroids can be described with <code>X,Y</code> coordinates where <code>X</code> is the distance from the left edge and <code>Y</code> is the distance from the top edge (so the top-left corner is <code>0,0</code> and the position immediately to its right is <code>1,0</code>).</p>
# MAGIC <p>Your job is to figure out which asteroid would be the best place to build a <em>new monitoring station</em>. A monitoring station can <em>detect</em> any asteroid to which it has <em>direct line of sight</em> - that is, there cannot be another asteroid <em>exactly</em> between them. This line of sight can be at any angle, not just lines aligned to the grid or <span title="The Elves on Ceres are clearly not concerned with honor.">diagonally</span>. The <em>best</em> location is the asteroid that can <em>detect</em> the largest number of other asteroids.</p>
# MAGIC <p>For example, consider the following map:</p>
# MAGIC <pre><code>.#..#
# MAGIC .....
# MAGIC #####
# MAGIC ....#
# MAGIC ...<em>#</em>#
# MAGIC </code></pre>
# MAGIC <p>The best location for a new monitoring station on this map is the highlighted asteroid at <code>3,4</code> because it can detect <code>8</code> asteroids, more than any other location. (The only asteroid it cannot detect is the one at <code>1,0</code>; its view of this asteroid is blocked by the asteroid at <code>2,2</code>.) All other asteroids are worse locations; they can detect <code>7</code> or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:</p>
# MAGIC <pre><code>.7..7
# MAGIC .....
# MAGIC 67775
# MAGIC ....7
# MAGIC ...87
# MAGIC </code></pre>
# MAGIC <p>Here is an asteroid (<code>#</code>) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:</p>
# MAGIC <pre><code>#.........
# MAGIC ...A......
# MAGIC ...B..a...
# MAGIC .EDCG....a
# MAGIC ..F.c.b...
# MAGIC .....c....
# MAGIC ..efd.c.gb
# MAGIC .......c..
# MAGIC ....f...c.
# MAGIC ...e..d..c
# MAGIC </code></pre>
# MAGIC <p>Here are some larger examples:</p>
# MAGIC <ul>
# MAGIC <li><p>Best is <code>5,8</code> with <code>33</code> other asteroids detected:</p>
# MAGIC <pre><code>......#.#.
# MAGIC #..#.#....
# MAGIC ..#######.
# MAGIC .#.#.###..
# MAGIC .#..#.....
# MAGIC ..#....#.#
# MAGIC #..#....#.
# MAGIC .##.#..###
# MAGIC ##...<em>#</em>..#.
# MAGIC .#....####
# MAGIC </code></pre></li>
# MAGIC <li><p>Best is <code>1,2</code> with <code>35</code> other asteroids detected:</p>
# MAGIC <pre><code>#.#...#.#.
# MAGIC .###....#.
# MAGIC .<em>#</em>....#...
# MAGIC ##.#.#.#.#
# MAGIC ....#.#.#.
# MAGIC .##..###.#
# MAGIC ..#...##..
# MAGIC ..##....##
# MAGIC ......#...
# MAGIC .####.###.
# MAGIC </code></pre></li>
# MAGIC <li><p>Best is <code>6,3</code> with <code>41</code> other asteroids detected:</p>
# MAGIC <pre><code>.#..#..###
# MAGIC ####.###.#
# MAGIC ....###.#.
# MAGIC ..###.<em>#</em>#.#
# MAGIC ##.##.#.#.
# MAGIC ....###..#
# MAGIC ..#.#..#.#
# MAGIC #..#.#.###
# MAGIC .##...##.#
# MAGIC .....#.#..
# MAGIC </code></pre></li>
# MAGIC <li><p>Best is <code>11,13</code> with <code>210</code> other asteroids detected:</p>
# MAGIC <pre><code>.#..##.###...#######
# MAGIC ##.############..##.
# MAGIC .#.######.########.#
# MAGIC .###.#######.####.#.
# MAGIC #####.##.#.##.###.##
# MAGIC ..#####..#.#########
# MAGIC ####################
# MAGIC #.####....###.#.#.##
# MAGIC ##.#################
# MAGIC #####.##.###..####..
# MAGIC ..######..##.#######
# MAGIC ####.##.####...##..#
# MAGIC .#####..#.######.###
# MAGIC ##...#.####<em>#</em>#####...
# MAGIC #.##########.#######
# MAGIC .####.#.###.###.#.##
# MAGIC ....##.##.###..#####
# MAGIC .#.#.###########.###
# MAGIC #.#.#.#####.####.###
# MAGIC ###.##.####.##.#..##
# MAGIC </code></pre></li>
# MAGIC </ul>
# MAGIC <p>Find the best location for a new monitoring station.  <em>How many other asteroids can be detected from that location?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''#.#................#..............#......#......
.......##..#..#....#.#.....##...#.........#.#...
.#...............#....#.##......................
......#..####.........#....#.......#..#.....#...
.....#............#......#................#.#...
....##...#.#.#.#.............#..#.#.......#.....
..#.#.........#....#..#.#.........####..........
....#...#.#...####..#..#..#.....#...............
.............#......#..........#...........#....
......#.#.........#...............#.............
..#......#..#.....##...##.....#....#.#......#...
...#.......##.........#.#..#......#........#.#..
#.............#..........#....#.#.....#.........
#......#.#................#.......#..#.#........
#..#.#.....#.....###..#.................#..#....
...............................#..........#.....
###.#.....#.....#.............#.......#....#....
.#.....#.........#.....#....#...................
........#....................#..#...............
.....#...#.##......#............#......#.....#..
..#..#..............#..#..#.##........#.........
..#.#...#.......#....##...#........#...#.#....#.
.....#.#..####...........#.##....#....#......#..
.....#..#..##...............................#...
.#....#..#......#.#............#........##...#..
.......#.....................#..#....#.....#....
#......#..###...........#.#....#......#.........
..............#..#.#...#.......#..#.#...#......#
.......#...........#.....#...#.............#.#..
..##..##.............#........#........#........
......#.............##..#.........#...#.#.#.....
#........#.........#...#.....#................#.
...#.#...........#.....#.........#......##......
..#..#...........#..........#...................
.........#..#.......................#.#.........
......#.#.#.....#...........#...............#...
......#.##...........#....#............#........
#...........##.#.#........##...........##.......
......#....#..#.......#.....#.#.......#.##......
.#....#......#..............#.......#...........
......##.#..........#..................#........
......##.##...#..#........#............#........
..#.....#.................###...#.....###.#..#..
....##...............#....#..................#..
.....#................#.#.#.......#..........#..
#........................#.##..........#....##..
.#.........#.#.#...#...#....#........#..#.......
...#..#.#......................#...............#'''

# COMMAND ----------

import cmath
import collections
import math

def find_max_asteroids(asteroids):
  distances = collections.defaultdict(lambda: collections.defaultdict(list))
  for x, y in asteroids:
    for x1, y1 in asteroids:
      if (x1, y1) == (x, y):
        continue
      r, theta = cmath.polar(complex(x - x1, y - y1))
      theta = (-math.pi / 2 + theta) % (2 * math.pi)
      distances[(x, y)][theta].append((r, x1, y1))
  return distances

asteroids = {(x, y) for y, line in enumerate(inp.splitlines()) for x, c in enumerate(line) if c == '#'}
distances = find_max_asteroids(asteroids)
best = max(distances.values(), key=lambda x: len(x))

answer = len(best)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover <span title="The Elves on Ceres just have a unique system of values, that's all.">the worst</span>: there are simply too many asteroids.</p>
# MAGIC <p>The only solution is <em>complete vaporization by giant laser</em>.</p>
# MAGIC <p>Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing <em>up</em> and always rotates <em>clockwise</em>, vaporizing any asteroid it hits.</p>
# MAGIC <p>If multiple asteroids are <em>exactly</em> in line with the station, the laser only has enough power to vaporize <em>one</em> of them before continuing its rotation. In other words, the same asteroids that can be <em>detected</em> can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.</p>
# MAGIC <p>For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked <code>X</code>:</p>
# MAGIC <pre><code>.#....#####...#..
# MAGIC ##...##.#####..##
# MAGIC ##...#...#.#####.
# MAGIC ..#.....X...###..
# MAGIC ..#.#.....#....##
# MAGIC </code></pre>
# MAGIC <p>The first nine asteroids to get vaporized, in order, would be:</p>
# MAGIC <pre><code>.#....###<em>2</em><em>4</em>...#..
# MAGIC ##...##.<em>1</em><em>3</em>#<em>6</em><em>7</em>..<em>9</em>#
# MAGIC ##...#...<em>5</em>.<em>8</em>####.
# MAGIC ..#.....X...###..
# MAGIC ..#.#.....#....##
# MAGIC </code></pre>
# MAGIC <p>Note that some asteroids (the ones behind the asteroids marked <code>1</code>, <code>5</code>, and <code>7</code>) won't have a chance to be vaporized until the next full rotation.  The laser continues rotating; the next nine to be vaporized are:</p>
# MAGIC <pre><code>.#....###.....#..
# MAGIC ##...##...#.....#
# MAGIC ##...#......<em>1</em><em>2</em><em>3</em><em>4</em>.
# MAGIC ..#.....X...<em>5</em>##..
# MAGIC ..#.<em>9</em>.....<em>8</em>....<em>7</em><em>6</em>
# MAGIC </code></pre>
# MAGIC <p>The next nine to be vaporized are then:</p>
# MAGIC <pre><code>.<em>8</em>....###.....#..
# MAGIC <em>5</em><em>6</em>...<em>9</em>#...#.....#
# MAGIC <em>3</em><em>4</em>...<em>7</em>...........
# MAGIC ..<em>2</em>.....X....##..
# MAGIC ..<em>1</em>..............
# MAGIC </code></pre>
# MAGIC <p>Finally, the laser completes its first full rotation (<code>1</code> through <code>3</code>), a second rotation (<code>4</code> through <code>8</code>), and vaporizes the last asteroid (<code>9</code>) partway through its third rotation:</p>
# MAGIC <pre><code>......<em>2</em><em>3</em><em>4</em>.....<em>6</em>..
# MAGIC ......<em>1</em>...<em>5</em>.....<em>7</em>
# MAGIC .................
# MAGIC ........X....<em>8</em><em>9</em>..
# MAGIC .................
# MAGIC </code></pre>
# MAGIC <p>In the large example above (the one with the best monitoring station location at <code>11,13</code>):</p>
# MAGIC <ul>
# MAGIC <li>The 1st asteroid to be vaporized is at <code>11,12</code>.</li>
# MAGIC <li>The 2nd asteroid to be vaporized is at <code>12,1</code>.</li>
# MAGIC <li>The 3rd asteroid to be vaporized is at <code>12,2</code>.</li>
# MAGIC <li>The 10th asteroid to be vaporized is at <code>12,8</code>.</li>
# MAGIC <li>The 20th asteroid to be vaporized is at <code>16,0</code>.</li>
# MAGIC <li>The 50th asteroid to be vaporized is at <code>16,9</code>.</li>
# MAGIC <li>The 100th asteroid to be vaporized is at <code>10,16</code>.</li>
# MAGIC <li>The 199th asteroid to be vaporized is at <code>9,6</code>.</li>
# MAGIC <li><em>The 200th asteroid to be vaporized is at <code>8,2</code>.</em></li>
# MAGIC <li>The 201st asteroid to be vaporized is at <code>10,9</code>.</li>
# MAGIC <li>The 299th and final asteroid to be vaporized is at <code>11,1</code>.</li>
# MAGIC </ul>
# MAGIC <p>The Elves are placing bets on which will be the <em>200th</em> asteroid to be vaporized.  Win the bet by determining which asteroid that will be; <em>what do you get if you multiply its X coordinate by <code>100</code> and then add its Y coordinate?</em> (For example, <code>8,2</code> becomes <em><code>802</code></em>.)</p>
# MAGIC </article>

# COMMAND ----------

objects = sorted([(i, angle, x, y) for angle, objects in best.items() for i, (d, x, y) in enumerate(objects)])
target_object = objects[199]

answer = 100 * target_object[2] + target_object[3]
print(answer)
