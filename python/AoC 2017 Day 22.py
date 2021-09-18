# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Sporifica Virus ---</h2><p>Diagnostics indicate that the local <em>grid computing cluster</em> has been contaminated with the <em>Sporifica Virus</em>. The grid computing cluster is a seemingly-<span title="The infinite is possible at AdventOfCodeCom.">infinite</span> two-dimensional grid of compute nodes.  Each node is either <em>clean</em> or <em>infected</em> by the virus.</p><p>
# MAGIC </p><p>To <a href="https://en.wikipedia.org/wiki/Morris_worm#The_mistake">prevent overloading</a> the nodes (which would render them useless to the virus) or detection by system administrators, exactly one <em>virus carrier</em> moves through the network, infecting or cleaning nodes as it moves. The virus carrier is always located on a single node in the network (the <em>current node</em>) and keeps track of the <em>direction</em> it is facing.</p>
# MAGIC <p>To avoid detection, the virus carrier works in bursts; in each burst, it <em>wakes up</em>, does some <em>work</em>, and goes back to <em>sleep</em>. The following steps are all executed <em>in order</em> one time each burst:</p>
# MAGIC <ul>
# MAGIC <li>If the <em>current node</em> is <em>infected</em>, it turns to its <em>right</em>.  Otherwise, it turns to its <em>left</em>. (Turning is done in-place; the <em>current node</em> does not change.)</li>
# MAGIC <li>If the <em>current node</em> is <em>clean</em>, it becomes <em>infected</em>.  Otherwise, it becomes <em>cleaned</em>. (This is done <em>after</em> the node is considered for the purposes of changing direction.)</li>
# MAGIC <li>The virus carrier <a href="https://www.youtube.com/watch?v=2vj37yeQQHg">moves</a> <em>forward</em> one node in the direction it is facing.</li>
# MAGIC </ul>
# MAGIC <p>Diagnostics have also provided a <em>map of the node infection status</em> (your puzzle input).  <em>Clean</em> nodes are shown as <code>.</code>; <em>infected</em> nodes are shown as <code>#</code>.  This map only shows the center of the grid; there are many more nodes beyond those shown, but none of them are currently infected.</p>
# MAGIC <p>The virus carrier begins in the middle of the map facing <em>up</em>.</p>
# MAGIC <p>For example, suppose you are given a map like this:</p>
# MAGIC <pre><code>..#
# MAGIC #..
# MAGIC ...
# MAGIC </code></pre>
# MAGIC <p>Then, the middle of the infinite grid looks like this, with the virus carrier's position marked with <code>[ ]</code>:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . . #[.]. . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on a <em>clean</em> node, so it turns <em>left</em>, <em>infects</em> the node, and moves left:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . .[#]# . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on an <em>infected</em> node, so it turns <em>right</em>, <em>cleans</em> the node, and moves up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . .[.]. # . . .
# MAGIC . . . . # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Four times in a row, the virus carrier finds a <em>clean</em>, <em>infects</em> it, turns <em>left</em>, and moves forward, ending in the same place and still facing up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . #[#]. # . . .
# MAGIC . . # # # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Now on the same node as before, it sees an infection, which causes it to turn <em>right</em>, <em>clean</em> the node, and move forward:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . # .[.]# . . .
# MAGIC . . # # # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>After the above actions, a total of <code>7</code> bursts of activity had taken place. Of them, <code>5</code> bursts of activity caused an infection.</p>
# MAGIC <p>After a total of <code>70</code>, the grid looks like this, with the virus carrier facing up:</p>
# MAGIC <pre><code>. . . . . # # . .
# MAGIC . . . . # . . # .
# MAGIC . . . # . . . . #
# MAGIC . . # . #[.]. . #
# MAGIC . . # . # . . # .
# MAGIC . . . . . # # . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>By this time, <code>41</code> bursts of activity caused an infection (though most of those nodes have since been cleaned).</p>
# MAGIC <p>After a total of <code>10000</code> bursts of activity, <code>5587</code> bursts will have caused an infection.</p>
# MAGIC <p>Given your actual map, after <code>10000</code> bursts of activity, <em>how many bursts cause a node to become infected</em>? (Do not count nodes that begin infected.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''.....###..#....#.#..##...
......##.##...........##.
.#..#..#.#.##.##.........
...#..###..##.#.###.#.#.#
##....#.##.#..####.####..
#..##...#.##.##.....##..#
.#.#......#...####...#.##
###....#######...#####.#.
##..#.####...#.#.##......
##.....###....#.#..#.##.#
.#..##.....#########.##..
##...##.###..#.#..#.#...#
...####..#...#.##.#..####
.#..##......#####..#.###.
...#.#.#..##...#####.....
#..###.###.#.....#.#.###.
##.##.#.#.##.#..#..######
####.##..#.###.#...#..###
.........#####.##.###..##
..#.##.#..#..#...##..#...
###.###.#.#..##...###....
##..#.#.#.#.#.#.#...###..
#..#.#.....#..#..#..##...
........#######.#...#.#..
..##.###.#.##.#.#.###..##'''

# COMMAND ----------

import collections

nodes = collections.defaultdict(bool)
for row, line in enumerate(inp.splitlines()):
  for col, s in enumerate(line):
    nodes[(row, col)] = s == '#'
    
def solve(nodes):
  nodes = nodes.copy()
  direction = 'N'
  row = col = max(nodes)[0] // 2
  infected_count = 0
  
  for _ in range(10000):
    if nodes[(row, col)]:
      direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]
      nodes[(row, col)] = False
    else:
      direction = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}[direction]
      nodes[(row, col)] = True
      infected_count += 1

    row += (direction == 'S') - (direction == 'N')
    col += (direction == 'E') - (direction == 'W')
  return infected_count

answer = solve(nodes)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you go to remove the virus from the infected nodes, it <em>evolves</em> to resist your attempt.</p>
# MAGIC <p>Now, before it infects a clean node, it will <em>weaken</em> it to disable your defenses. If it encounters an infected node, it will instead <em>flag</em> the node to be cleaned in the future.  So:</p>
# MAGIC <ul>
# MAGIC <li><em>Clean</em> nodes become <em>weakened</em>.</li>
# MAGIC <li><em>Weakened</em> nodes become <em>infected</em>.</li>
# MAGIC <li><em>Infected</em> nodes become <em>flagged</em>.</li>
# MAGIC <li><em>Flagged</em> nodes become <em>clean</em>.</li>
# MAGIC </ul>
# MAGIC <p>Every node is always in exactly one of the above states.</p>
# MAGIC <p>The virus carrier still functions in a similar way, but now uses the following logic during its bursts of action:</p>
# MAGIC <ul>
# MAGIC <li>Decide which way to turn based on the <em>current node</em>:
# MAGIC   <ul>
# MAGIC   <li>If it is <em>clean</em>, it turns <em>left</em>.</li>
# MAGIC   <li>If it is <em>weakened</em>, it does <em>not</em> turn, and will continue moving in the same direction.</li>
# MAGIC   <li>If it is <em>infected</em>, it turns <em>right</em>.</li>
# MAGIC   <li>If it is <em>flagged</em>, it <em>reverses</em> direction, and will go back the way it came.</li>
# MAGIC   </ul>
# MAGIC </li>
# MAGIC <li>Modify the state of the <em>current node</em>, as described above.</li>
# MAGIC <li>The virus carrier moves <em>forward</em> one node in the direction it is facing.</li>
# MAGIC </ul>
# MAGIC <p>Start with the same map (still using <code>.</code> for <em>clean</em> and <code>#</code> for infected) and still with the virus carrier starting in the middle and facing <em>up</em>.</p>
# MAGIC <p>Using the same initial state as the previous example, and drawing <em>weakened</em> as <code>W</code> and <em>flagged</em> as <code>F</code>, the middle of the infinite grid looks like this, with the virus carrier's position again marked with <code>[ ]</code>:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . . #[.]. . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>This is the same as before, since no initial nodes are <em>weakened</em> or <em>flagged</em>.  The virus carrier is on a clean node, so it still turns left, instead <em>weakens</em> the node, and moves left:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . .[#]W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on an infected node, so it still turns right, instead <em>flags</em> the node, and moves up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . .[.]. # . . .
# MAGIC . . . F W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>This process repeats three more times, ending on the previously-flagged node and facing right:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC . . W[F]W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Finding a flagged node, it reverses direction and <em>cleans</em> the node:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC . .[W]. W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The <em>weakened</em> node becomes infected, and it continues in the same direction:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC .[.]# . W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Of the first <code>100</code> bursts, <code>26</code> will result in <em>infection</em>. Unfortunately, another feature of this evolved virus is <em>speed</em>; of the first <code>10000000</code> bursts, <code>2511944</code> will result in <em>infection</em>.</p>
# MAGIC <p>Given your actual map, after <code>10000000</code> bursts of activity, <em>how many bursts cause a node to become infected</em>? (Do not count nodes that begin infected.)</p>
# MAGIC </article>

# COMMAND ----------

def solve2(nodes):
  nodes = nodes.copy()
  direction = 'N'
  row = col = max(nodes)[0] // 2
  infected_count = 0
  
  for _ in range(10000000):
    if nodes[(row, col)] == 0:
      direction = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}[direction]
    elif nodes[(row, col)] == 2:
      direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]
    elif nodes[(row, col)] == 3:
      direction = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}[direction]
      
    nodes[(row, col)] = (nodes[(row, col)] + 1) % 4
    if nodes[(row, col)] == 2:
      infected_count += 1

    row += (direction == 'S') - (direction == 'N')
    col += (direction == 'E') - (direction == 'W')
  return infected_count

answer = solve2(collections.defaultdict(int, {k: v*2 for k, v in nodes.items()}))
print(answer)
