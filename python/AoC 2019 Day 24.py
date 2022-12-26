# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: Planet of Discord ---</h2><p>You land on <a href="https://en.wikipedia.org/wiki/Eris_(dwarf_planet)">Eris</a>, your last stop before reaching Santa.  As soon as you do, your sensors start picking up strange life forms moving around: Eris is infested with <a href="https://www.nationalgeographic.org/thisday/sep9/worlds-first-computer-bug/">bugs</a>! With an <span title="For a sad version of this story, look up Voices of a Distant Star.">over 24-hour roundtrip</span> for messages between you and Earth, you'll have to deal with this problem on your own.</p>
# MAGIC <p>Eris isn't a very large place; a scan of the entire area fits into a 5x5 grid (your puzzle input). The scan shows <em>bugs</em> (<code>#</code>) and <em>empty spaces</em> (<code>.</code>).</p>
# MAGIC <p>Each <em>minute</em>, The bugs live and die based on the number of bugs in the <em>four adjacent tiles</em>:</p>
# MAGIC <ul>
# MAGIC <li>A bug <em>dies</em> (becoming an empty space) unless there is <em>exactly one</em> bug adjacent to it.</li>
# MAGIC <li>An empty space <em>becomes infested</em> with a bug if <em>exactly one or two</em> bugs are adjacent to it.</li>
# MAGIC </ul>
# MAGIC <p>Otherwise, a bug or empty space remains the same.  (Tiles on the edges of the grid have fewer than four adjacent tiles; the missing tiles count as empty space.) This process happens in every location <em>simultaneously</em>; that is, within the same minute, the number of adjacent bugs is counted for every tile first, and then the tiles are updated.</p>
# MAGIC <p>Here are the first few minutes of an example scenario:</p>
# MAGIC <pre><code>Initial state:
# MAGIC ....#
# MAGIC #..#.
# MAGIC #..##
# MAGIC ..#..
# MAGIC #....
# MAGIC 
# MAGIC After 1 minute:
# MAGIC #..#.
# MAGIC ####.
# MAGIC ###.#
# MAGIC ##.##
# MAGIC .##..
# MAGIC 
# MAGIC After 2 minutes:
# MAGIC #####
# MAGIC ....#
# MAGIC ....#
# MAGIC ...#.
# MAGIC #.###
# MAGIC 
# MAGIC After 3 minutes:
# MAGIC #....
# MAGIC ####.
# MAGIC ...##
# MAGIC #.##.
# MAGIC .##.#
# MAGIC 
# MAGIC After 4 minutes:
# MAGIC ####.
# MAGIC ....#
# MAGIC ##..#
# MAGIC .....
# MAGIC ##...
# MAGIC </code></pre>
# MAGIC <p>To understand the nature of the bugs, watch for the first time a layout of bugs and empty spaces <em>matches any previous layout</em>. In the example above, the first layout to appear twice is:</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC .....
# MAGIC #....
# MAGIC .#...
# MAGIC </code></pre>
# MAGIC <p>To calculate the <em>biodiversity rating</em> for this layout, consider each tile left-to-right in the top row, then left-to-right in the second row, and so on. Each of these tiles is worth biodiversity points equal to <em>increasing powers of two</em>: 1, 2, 4, 8, 16, 32, and so on.  Add up the biodiversity points for tiles with bugs; in this example, the 16th tile (<code>32768</code> points) and 22nd tile (<code>2097152</code> points) have bugs, a total biodiversity rating of <code><em>2129920</em></code>.</p>
# MAGIC <p><em>What is the biodiversity rating for the first layout that appears twice?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''.....
...#.
.#..#
.#.#.
...##'''

# COMMAND ----------

import collections


def get_biodiversity(bugs):
  biodiversity = 0
  for row in range(5):
    for col in range(5):
      if (row, col) in bugs:
        biodiversity += 2 ** (5 * row + col)
  return biodiversity


def simulate(bugs):
  neighbors = collections.Counter()
  for bug in bugs:
    for delta in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
      pos = tuple(x + dx for x, dx in zip(bug, delta))
      if not all(0 <= x < 5 for x in pos):
        continue
      neighbors[pos] += 1
  
  return {pos for pos, cnt in neighbors.items() if cnt == 1 or (pos not in bugs and cnt == 2)}


bugs_start = {(row, col) for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line) if c == '#'}

bugs = bugs_start
biodiversities = set()
while True:
  biodiversity = get_biodiversity(bugs)
  if biodiversity in biodiversities:
    break
  biodiversities.add(biodiversity)
  
  bugs = simulate(bugs)

answer = biodiversity
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After careful analysis, one thing is certain: <em>you have no idea where all these bugs are coming from</em>.</p>
# MAGIC <p>Then, you remember: Eris is an old <a href="20">Plutonian</a> settlement! Clearly, the bugs are coming from recursively-folded space.</p>
# MAGIC <p>This 5x5 grid is <em>only one</em> level in an <em>infinite</em> number of recursion levels. The tile in the middle of the grid is actually another 5x5 grid, the grid in your scan is contained as the middle tile of a larger 5x5 grid, and so on. Two levels of grids look like this:</p>
# MAGIC <pre><code>     |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | |?| | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC </code></pre>
# MAGIC <p>(To save space, some of the tiles are not drawn to scale.)  Remember, this is only a small part of the infinitely recursive grid; there is a 5x5 grid that contains this diagram, and a 5x5 grid that contains that one, and so on.  Also, the <code>?</code> in the diagram contains another 5x5 grid, which itself contains another 5x5 grid, and so on.</p>
# MAGIC <p>The scan you took (your puzzle input) shows where the bugs are <em>on a single level</em> of this structure. The middle tile of your scan is empty to accommodate the recursive grids within it. Initially, no other levels contain bugs.</p>
# MAGIC <p>Tiles still count as <em>adjacent</em> if they are directly <em>up, down, left, or right</em> of a given tile. Some tiles have adjacent tiles at a recursion level above or below its own level. For example:</p>
# MAGIC <pre><code>     |     |         |     |     
# MAGIC   1  |  2  |    3    |  4  |  5  
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC   6  |  7  |    8    |  9  |  10 
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |A|B|C|D|E|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |F|G|H|I|J|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC  11  | 12  |K|L|?|N|O|  14 |  15 
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |P|Q|R|S|T|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |U|V|W|X|Y|     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC  16  | 17  |    18   |  19 |  20 
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC  21  | 22  |    23   |  24 |  25 
# MAGIC      |     |         |     |     
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Tile 19 has four adjacent tiles: 14, 18, 20, and 24.</li>
# MAGIC <li>Tile G has four adjacent tiles: B, F, H, and L.</li>
# MAGIC <li>Tile D has four adjacent tiles: 8, C, E, and I.</li>
# MAGIC <li>Tile E has four adjacent tiles: 8, D, 14, and J.</li>
# MAGIC <li>Tile 14 has <em>eight</em> adjacent tiles: 9, E, J, O, T, Y, 15, and 19.</li>
# MAGIC <li>Tile N has <em>eight</em> adjacent tiles: I, O, S, and five tiles within the sub-grid marked <code>?</code>.</li>
# MAGIC </ul>
# MAGIC <p>The rules about bugs living and dying are the same as before.</p>
# MAGIC <p>For example, consider the same initial state as above:</p>
# MAGIC <pre><code>....#
# MAGIC #..#.
# MAGIC #.?##
# MAGIC ..#..
# MAGIC #....
# MAGIC </code></pre>
# MAGIC <p>The center tile is drawn as <code>?</code> to indicate the next recursive grid. Call this level 0; the grid within this one is level 1, and the grid that contains this one is level -1.  Then, after <em>ten</em> minutes, the grid at each level would look like this:</p>
# MAGIC <pre><code>Depth -5:
# MAGIC ..#..
# MAGIC .#.#.
# MAGIC ..?.#
# MAGIC .#.#.
# MAGIC ..#..
# MAGIC 
# MAGIC Depth -4:
# MAGIC ...#.
# MAGIC ...##
# MAGIC ..?..
# MAGIC ...##
# MAGIC ...#.
# MAGIC 
# MAGIC Depth -3:
# MAGIC #.#..
# MAGIC .#...
# MAGIC ..?..
# MAGIC .#...
# MAGIC #.#..
# MAGIC 
# MAGIC Depth -2:
# MAGIC .#.##
# MAGIC ....#
# MAGIC ..?.#
# MAGIC ...##
# MAGIC .###.
# MAGIC 
# MAGIC Depth -1:
# MAGIC #..##
# MAGIC ...##
# MAGIC ..?..
# MAGIC ...#.
# MAGIC .####
# MAGIC 
# MAGIC Depth 0:
# MAGIC .#...
# MAGIC .#.##
# MAGIC .#?..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC Depth 1:
# MAGIC .##..
# MAGIC #..##
# MAGIC ..?.#
# MAGIC ##.##
# MAGIC #####
# MAGIC 
# MAGIC Depth 2:
# MAGIC ###..
# MAGIC ##.#.
# MAGIC #.?..
# MAGIC .#.##
# MAGIC #.#..
# MAGIC 
# MAGIC Depth 3:
# MAGIC ..###
# MAGIC .....
# MAGIC #.?..
# MAGIC #....
# MAGIC #...#
# MAGIC 
# MAGIC Depth 4:
# MAGIC .###.
# MAGIC #..#.
# MAGIC #.?..
# MAGIC ##.#.
# MAGIC .....
# MAGIC 
# MAGIC Depth 5:
# MAGIC ####.
# MAGIC #..#.
# MAGIC #.?#.
# MAGIC ####.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>In this example, after 10 minutes, a total of <code><em>99</em></code> bugs are present.</p>
# MAGIC <p>Starting with your scan, <em>how many bugs are present after 200 minutes?</em></p>
# MAGIC </article>

# COMMAND ----------

def simulate(bugs):
  neighbors = collections.Counter()
  for bug, depth in bugs:
    for delta in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
      pos = tuple(x + dx for x, dx in zip(bug, delta))

      if pos == (2, 2):
        if bug[0] == 1:
          inner_positions = [(0, x) for x in range(5)]
        elif bug[1] == 3:
          inner_positions = [(x, 4) for x in range(5)]
        elif bug[0] == 3:
          inner_positions = [(4, x) for x in range(5)]
        elif bug[1] == 1:
          inner_positions = [(x, 0) for x in range(5)]
        
        for inner_position in inner_positions:
          neighbors[(inner_position, depth + 1)] += 1
      elif not all(0 <= x < 5 for x in pos):
        if pos[0] == -1:
          pos = (1, 2)
        elif pos[1] == 5:
          pos = (2, 3)
        elif pos[0] == 5:
          pos = (3, 2)
        elif pos[1] == -1:
          pos = (2, 1)

        neighbors[(pos, depth - 1)] += 1
      else:
        neighbors[(pos, depth)] += 1

  return {pos for pos, cnt in neighbors.items() if cnt == 1 or (pos not in bugs and cnt == 2)}


bugs = {(pos, 0) for pos in bugs_start}
for _ in range(200):
  bugs = simulate(bugs)

answer = len(bugs)
print(answer)
