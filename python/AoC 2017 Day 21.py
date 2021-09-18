# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Fractal Art ---</h2><p>You find a program trying to generate some art. It uses a strange process that involves <span title="This technique is also often used on TV.">repeatedly enhancing</span> the detail of an image through a set of rules.</p>
# MAGIC <p>The image consists of a two-dimensional square grid of pixels that are either on (<code>#</code>) or off (<code>.</code>). The program always begins with this pattern:</p>
# MAGIC <pre><code>.#.
# MAGIC ..#
# MAGIC ###
# MAGIC </code></pre>
# MAGIC <p>Because the pattern is both <code>3</code> pixels wide and <code>3</code> pixels tall, it is said to have a <em>size</em> of <code>3</code>.</p>
# MAGIC <p>Then, the program repeats the following process:</p>
# MAGIC <ul>
# MAGIC <li>If the size is evenly divisible by <code>2</code>, break the pixels up into <code>2x2</code> squares, and convert each <code>2x2</code> square into a <code>3x3</code> square by following the corresponding <em>enhancement rule</em>.</li>
# MAGIC <li>Otherwise, the size is evenly divisible by <code>3</code>; break the pixels up into <code>3x3</code> squares, and convert each <code>3x3</code> square into a <code>4x4</code> square by following the corresponding <em>enhancement rule</em>.</li>
# MAGIC </ul>
# MAGIC <p>Because each square of pixels is replaced by a larger one, the image gains pixels and so its <em>size</em> increases.</p>
# MAGIC <p>The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules.  The artist explains that sometimes, one must <em>rotate</em> or <em>flip</em> the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:</p>
# MAGIC <pre><code>../.#  =  ..
# MAGIC           .#
# MAGIC 
# MAGIC                 .#.
# MAGIC .#./..#/###  =  ..#
# MAGIC                 ###
# MAGIC 
# MAGIC                         #..#
# MAGIC #..#/..../#..#/.##.  =  ....
# MAGIC                         #..#
# MAGIC                         .##.
# MAGIC </code></pre>
# MAGIC <p>When searching for a rule to use, rotate and flip the pattern as necessary.  For example, all of the following patterns match the same rule:</p>
# MAGIC <pre><code>.#.   .#.   #..   ###
# MAGIC ..#   #..   #.#   ..#
# MAGIC ###   ###   ##.   .#.
# MAGIC </code></pre>
# MAGIC <p>Suppose the book contained the following two rules:</p>
# MAGIC <pre><code>../.# =&gt; ##./#../...
# MAGIC .#./..#/### =&gt; #..#/..../..../#..#
# MAGIC </code></pre>
# MAGIC <p>As before, the program begins with this pattern:</p>
# MAGIC <pre><code>.#.
# MAGIC ..#
# MAGIC ###
# MAGIC </code></pre>
# MAGIC <p>The size of the grid (<code>3</code>) is not divisible by <code>2</code>, but it is divisible by <code>3</code>. It divides evenly into a single square; the square matches the second rule, which produces:</p>
# MAGIC <pre><code>#..#
# MAGIC ....
# MAGIC ....
# MAGIC #..#
# MAGIC </code></pre>
# MAGIC <p>The size of this enhanced grid (<code>4</code>) is evenly divisible by <code>2</code>, so that rule is used. It divides evenly into four squares:</p>
# MAGIC <pre><code>#.|.#
# MAGIC ..|..
# MAGIC --+--
# MAGIC ..|..
# MAGIC #.|.#
# MAGIC </code></pre>
# MAGIC <p>Each of these squares matches the same rule (<code>../.# =&gt; ##./#../...</code>), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:</p>
# MAGIC <pre><code>##.|##.
# MAGIC #..|#..
# MAGIC ...|...
# MAGIC ---+---
# MAGIC ##.|##.
# MAGIC #..|#..
# MAGIC ...|...
# MAGIC </code></pre>
# MAGIC <p>Finally, the squares are joined into a new grid:</p>
# MAGIC <pre><code>##.##.
# MAGIC #..#..
# MAGIC ......
# MAGIC ##.##.
# MAGIC #..#..
# MAGIC ......
# MAGIC </code></pre>
# MAGIC <p>Thus, after <code>2</code> iterations, the grid contains <code>12</code> pixels that are <em>on</em>.</p>
# MAGIC <p><em>How many pixels stay on</em> after <code>5</code> iterations?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''../.. => ..#/#../.#.
#./.. => #../#../...
##/.. => ###/#.#/#..
.#/#. => ###/##./.#.
##/#. => .../.#./..#
##/## => ##./#.#/###
.../.../... => ##../.#../#.#./....
#../.../... => ..../##.#/...#/##.#
.#./.../... => ###./####/#.../#..#
##./.../... => ###./.##./...#/..##
#.#/.../... => .###/.##./#.../#.##
###/.../... => ##.#/#..#/#.#./#.##
.#./#../... => #.#./.###/#.../#.##
##./#../... => #.../####/#.##/....
..#/#../... => #.##/..#./...#/...#
#.#/#../... => #.##/####/.#.#/#.#.
.##/#../... => #.../##../##.#/.##.
###/#../... => ..../#.#./.###/#...
.../.#./... => .#.#/#..#/##../#.##
#../.#./... => ###./.###/.#.#/..#.
.#./.#./... => ..##/.##./..##/.#.#
##./.#./... => ..#./##../###./...#
#.#/.#./... => ..##/.##./.###/###.
###/.#./... => ..#./.###/###./#.##
.#./##./... => ###./..../.#../#...
##./##./... => .#.#/##../##.#/...#
..#/##./... => ##.#/.##./.###/..##
#.#/##./... => .###/..#./#.##/####
.##/##./... => ##.#/..#./..##/###.
###/##./... => ..../.#.#/.#../#...
.../#.#/... => ###./.#.#/.#../#.##
#../#.#/... => ####/#..#/..../....
.#./#.#/... => #.../..##/#.##/#.#.
##./#.#/... => #.#./###./##../#.#.
#.#/#.#/... => ...#/.##./.##./.#..
###/#.#/... => ..../.##./####/#.#.
.../###/... => .###/.#../.###/#.##
#../###/... => ..##/..##/.##./##..
.#./###/... => .#.#/..#./..##/##.#
##./###/... => ...#/#.##/#.#./##.#
#.#/###/... => #.##/.##./...#/###.
###/###/... => ##../...#/..##/####
..#/.../#.. => #.##/#.../.#../#.#.
#.#/.../#.. => .##./.##./.#.#/.##.
.##/.../#.. => .#.#/#.##/...#/##.#
###/.../#.. => ##../..#./...#/##..
.##/#../#.. => ##../..##/#..#/#..#
###/#../#.. => ##../..#./#.#./....
..#/.#./#.. => .##./##.#/##../####
#.#/.#./#.. => ####/...#/.#.#/..#.
.##/.#./#.. => .#.#/..#./##.#/.#..
###/.#./#.. => #.../#.##/..../##.#
.##/##./#.. => #.#./#.#./#.##/#.#.
###/##./#.. => ...#/###./.##./.#.#
#../..#/#.. => ####/####/..../.##.
.#./..#/#.. => #.##/...#/..#./####
##./..#/#.. => ..#./#.../..##/####
#.#/..#/#.. => #.../#.##/#.##/..##
.##/..#/#.. => ####/..../##../####
###/..#/#.. => ..../##.#/.##./####
#../#.#/#.. => ...#/..##/###./#..#
.#./#.#/#.. => #..#/..#./.###/##.#
##./#.#/#.. => ###./####/#.##/..#.
..#/#.#/#.. => ##../##.#/..##/.##.
#.#/#.#/#.. => .#.#/.##./#.../##.#
.##/#.#/#.. => .#.#/#..#/.##./..#.
###/#.#/#.. => ...#/.#../.##./##.#
#../.##/#.. => ###./##../#.#./####
.#./.##/#.. => .#../##../#.#./.#.#
##./.##/#.. => ##.#/.#../.#.#/####
#.#/.##/#.. => ####/.#.#/..../....
.##/.##/#.. => ####/##../#..#/####
###/.##/#.. => .###/##.#/.#../#.##
#../###/#.. => #..#/###./####/.#.#
.#./###/#.. => ..##/##../##.#/.#.#
##./###/#.. => #..#/.#../####/...#
..#/###/#.. => ##../##.#/...#/#..#
#.#/###/#.. => ..#./.##./#..#/....
.##/###/#.. => #..#/#.../..../.#..
###/###/#.. => ..#./#.##/.##./#...
.#./#.#/.#. => .#.#/.##./##.#/.##.
##./#.#/.#. => #..#/.###/.#.#/.##.
#.#/#.#/.#. => #.../##../#.../.###
###/#.#/.#. => ###./.###/###./....
.#./###/.#. => .#../####/...#/##..
##./###/.#. => ####/###./..../....
#.#/###/.#. => ...#/.###/..../####
###/###/.#. => ..../#.../..#./.###
#.#/..#/##. => #.#./#.../####/#.##
###/..#/##. => .#.#/#..#/.###/#...
.##/#.#/##. => ..##/..#./..../##..
###/#.#/##. => #.#./##.#/####/#..#
#.#/.##/##. => ..../.#../#.#./##.#
###/.##/##. => ..../..../.#../##.#
.##/###/##. => #.#./.###/#.#./#.##
###/###/##. => ##.#/##.#/.###/..#.
#.#/.../#.# => #..#/.#../#.../...#
###/.../#.# => ##../.#../##.#/..#.
###/#../#.# => ..##/#.#./####/.#..
#.#/.#./#.# => ...#/...#/#..#/#.#.
###/.#./#.# => ..../####/.##./.#.#
###/##./#.# => #..#/.#.#/..##/####
#.#/#.#/#.# => #.#./..#./...#/.#..
###/#.#/#.# => ...#/##.#/.###/.#..
#.#/###/#.# => .#.#/###./.#../.##.
###/###/#.# => ...#/.###/.#.#/###.
###/#.#/### => #.##/.#.#/...#/.#..
###/###/### => ..##/.#../#.#./.#..'''

# COMMAND ----------

import numpy as np

def str_to_np(s):
  nrows = s.count('/') + 1
  return np.array([c == '#' for c in s.replace('/', '')]).reshape(nrows, nrows)

def split(grid):
  size = grid.shape[0]
  split_size = size / (2 if size % 2 == 0 else 3)
  return [np.hsplit(g, split_size) for g in np.vsplit(grid, split_size)]

def expand(grid, rules):
  return rules[grid.tobytes()]
  
def combine(grids):
  return np.vstack([np.hstack(row) for row in grids])

def solve(rules, iterations):
  grid = str_to_np('.#./..#/###')
  for _ in range(iterations):
    grid = combine([expand(g, rules) for g in row] for row in split(grid))
  return grid.sum()


rules = {}
for line in inp.split('\n'):
  a, b = (str_to_np(s) for s in line.split(' => '))
  rules[a.tobytes()] = b
  rules[np.flipud(a).tobytes()] = b
  rules[np.fliplr(a).tobytes()] = b
  rules[np.rot90(a, k=1).tobytes()] = b
  rules[np.rot90(a, k=2).tobytes()] = b
  rules[np.rot90(a, k=3).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=1)).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=2)).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=3)).tobytes()] = b


answer = solve(rules, 5)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many pixels stay on</em> after <code>18</code> iterations?</p>
# MAGIC </article>

# COMMAND ----------

answer = solve(rules, 18)
print(answer)
