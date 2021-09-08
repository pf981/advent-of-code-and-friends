# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/13

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 13: A Maze of Twisty Little Cubicles ---</h2><p>You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one.  Instead, you are in a maze of <span title="You are in a twisty alike of little cubicles, all maze.">twisty little cubicles</span>, all alike.</p>
# MAGIC <p>Every location in this area is addressed by a pair of non-negative integers (<code>x,y</code>). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at <code>0,0</code> and seems to extend infinitely toward <em>positive</em> <code>x</code> and <code>y</code>; negative values are <em>invalid</em>, as they represent a location outside the building. You are in a small waiting area at <code>1,1</code>.</p>
# MAGIC <p>While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given <code>x,y</code> coordinate will be a wall or an open space using a simple system:</p>
# MAGIC <ul>
# MAGIC <li>Find <code>x*x + 3*x + 2*x*y + y + y*y</code>.</li>
# MAGIC <li>Add the office designer's favorite number (your puzzle input).</li>
# MAGIC <li>Find the <a href="https://en.wikipedia.org/wiki/Binary_number">binary representation</a> of that sum; count the <em>number</em> of <a href="https://en.wikipedia.org/wiki/Bit">bits</a> that are <code>1</code>.
# MAGIC <ul>
# MAGIC <li>If the number of bits that are <code>1</code> is <em>even</em>, it's an <em>open space</em>.</li>
# MAGIC <li>If the number of bits that are <code>1</code> is <em>odd</em>, it's a <em>wall</em>.</li>
# MAGIC </ul>
# MAGIC </li>
# MAGIC </ul>
# MAGIC <p>For example, if the office designer's favorite number were <code>10</code>, drawing walls as <code>#</code> and open spaces as <code>.</code>, the corner of the building containing <code>0,0</code> would look like this:</p>
# MAGIC <pre><code>  0123456789
# MAGIC 0 .#.####.##
# MAGIC 1 ..#..#...#
# MAGIC 2 #....##...
# MAGIC 3 ###.#.###.
# MAGIC 4 .##..#..#.
# MAGIC 5 ..##....#.
# MAGIC 6 #...##.###
# MAGIC </code></pre>
# MAGIC <p>Now, suppose you wanted to reach <code>7,4</code>. The shortest route you could take is marked as <code>O</code>:</p>
# MAGIC <pre><code>  0123456789
# MAGIC 0 .#.####.##
# MAGIC 1 .O#..#...#
# MAGIC 2 #OOO.##...
# MAGIC 3 ###O#.###.
# MAGIC 4 .##OO#OO#.
# MAGIC 5 ..##OOO.#.
# MAGIC 6 #...##.###
# MAGIC </code></pre>
# MAGIC <p>Thus, reaching <code>7,4</code> would take a minimum of <code>11</code> steps (starting from your current location, <code>1,1</code>).</p>
# MAGIC <p>What is the <em>fewest number of steps required</em> for you to reach <code>31,39</code>?</p>
# MAGIC </article>

# COMMAND ----------

inp = 1364

# COMMAND ----------

from dataclasses import dataclass
from heapq import heappop, heappush

def is_open(x, y):
  if x < 0 or y < 0:
    return False
  
  num = x*x + 3*x + 2*x*y + y + y*y + inp
  return bin(num).count('1') % 2 == 0

def solve():
  visited = set()
  states = [(0, 1, 1)] # d, x, y
  
  while states:
    d, x, y = heappop(states)
    visited.add((x, y))
    
    for direction in ['N', 'E', 'S', 'W']:
      new_d = d + 1
      new_x = x + (direction == 'E') - (direction == 'W')
      new_y = y + (direction == 'S') - (direction == 'N')
      
      if is_open(new_x, new_y) and (new_x, new_y) not in visited:
        if new_x == 31 and new_y == 39:
          return new_d
        
        heappush(states, (new_d, new_x, new_y))

answer = solve()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many locations</em> (distinct <code>x,y</code> coordinates, including your starting location) can you reach in at most <code>50</code> steps?</p>
# MAGIC </article>

# COMMAND ----------

def solve2():
  visited = set()
  states = [(0, 1, 1)] # d, x, y
  
  while states:
    d, x, y = heappop(states)
    visited.add((x, y))
    
    for direction in ['N', 'E', 'S', 'W']:
      new_d = d + 1
      new_x = x + (direction == 'E') - (direction == 'W')
      new_y = y + (direction == 'S') - (direction == 'N')
      
      if new_d <= 50 and is_open(new_x, new_y) and (new_x, new_y) not in visited:        
        heappush(states, (new_d, new_x, new_y))
  return len(visited)

answer = solve2()
answer
