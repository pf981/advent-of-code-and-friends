# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: Blizzard Basin ---</h2><p>With everything replanted for next year (and with elephants and monkeys to tend the grove), you and the Elves leave for the extraction point.</p>
# MAGIC <p>Partway up the mountain that shields the grove is a flat, open area that serves as the extraction point. It's a bit of a climb, but nothing the expedition can't handle.</p>
# MAGIC <p>At least, that would normally be true; now that the mountain is covered in snow, things have become more difficult than the Elves are used to.</p>
# MAGIC <p>As the expedition reaches a valley that must be traversed to reach the extraction site, you find that strong, turbulent winds are pushing small <em>blizzards</em> of snow and sharp ice around the valley. It's a good thing everyone packed warm clothes! To make it across safely, you'll need to find a way to avoid them.</p>
# MAGIC <p>Fortunately, it's easy to see all of this from the entrance to the valley, so you make a map of the valley and the blizzards (your puzzle input). For example:</p>
# MAGIC <pre><code>#.#####
# MAGIC #.....#
# MAGIC #&gt;....#
# MAGIC #.....#
# MAGIC #...v.#
# MAGIC #.....#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>The walls of the valley are drawn as <code>#</code>; everything else is ground. Clear ground - where there is currently no blizzard - is drawn as <code>.</code>. Otherwise, blizzards are drawn with an arrow indicating their direction of motion: up (<code>^</code>), down (<code>v</code>), left (<code>&lt;</code>), or right (<code>&gt;</code>).</p>
# MAGIC <p>The above map includes two blizzards, one moving right (<code>&gt;</code>) and one moving down (<code>v</code>). In one minute, each blizzard moves one position in the direction it is pointing:</p>
# MAGIC <pre><code>#.#####
# MAGIC #.....#
# MAGIC #.&gt;...#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #...v.#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>Due to <span title="I think, anyway. Do I look like a theoretical blizzacist?">conservation of blizzard energy</span>, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction. After another minute, the bottom downward-moving blizzard has been replaced with a new downward-moving blizzard at the top of the valley instead:</p>
# MAGIC <pre><code>#.#####
# MAGIC #...v.#
# MAGIC #..&gt;..#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>Because blizzards are made of tiny snowflakes, they pass right through each other. After another minute, both blizzards temporarily occupy the same position, marked <code>2</code>:</p>
# MAGIC <pre><code>#.#####
# MAGIC #.....#
# MAGIC #...2.#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>After another minute, the situation resolves itself, giving each blizzard back its personal space:</p>
# MAGIC <pre><code>#.#####
# MAGIC #.....#
# MAGIC #....&gt;#
# MAGIC #...v.#
# MAGIC #.....#
# MAGIC #.....#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>Finally, after yet another minute, the rightward-facing blizzard on the right is replaced with a new one on the left facing the same direction:</p>
# MAGIC <pre><code>#.#####
# MAGIC #.....#
# MAGIC #&gt;....#
# MAGIC #.....#
# MAGIC #...v.#
# MAGIC #.....#
# MAGIC #####.#
# MAGIC </code></pre>
# MAGIC <p>This process repeats at least as long as you are observing it, but probably forever.</p>
# MAGIC <p>Here is a more complex example:</p>
# MAGIC <pre><code>#.######
# MAGIC #&gt;&gt;.&lt;^&lt;#
# MAGIC #.&lt;..&lt;&lt;#
# MAGIC #&gt;v.&gt;&lt;&gt;#
# MAGIC #&lt;^v^^&gt;#
# MAGIC ######.#
# MAGIC </code></pre>
# MAGIC <p>Your expedition begins in the only non-wall position in the top row and needs to reach the only non-wall position in the bottom row. On each minute, you can <em>move</em> up, down, left, or right, or you can <em>wait</em> in place. You and the blizzards act <em>simultaneously</em>, and you cannot share a position with a blizzard.</p>
# MAGIC <p>In the above example, the fastest way to reach your goal requires <code><em>18</em></code> steps. Drawing the position of the expedition as <code>E</code>, one way to achieve this is:</p>
# MAGIC <pre><code>Initial state:
# MAGIC #<em>E</em>######
# MAGIC #&gt;&gt;.&lt;^&lt;#
# MAGIC #.&lt;..&lt;&lt;#
# MAGIC #&gt;v.&gt;&lt;&gt;#
# MAGIC #&lt;^v^^&gt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 1, move down:
# MAGIC #.######
# MAGIC #<em>E</em>&gt;3.&lt;.#
# MAGIC #&lt;..&lt;&lt;.#
# MAGIC #&gt;2.22.#
# MAGIC #&gt;v..^&lt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 2, move down:
# MAGIC #.######
# MAGIC #.2&gt;2..#
# MAGIC #<em>E</em>^22^&lt;#
# MAGIC #.&gt;2.^&gt;#
# MAGIC #.&gt;..&lt;.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 3, wait:
# MAGIC #.######
# MAGIC #&lt;^&lt;22.#
# MAGIC #<em>E</em>2&lt;.2.#
# MAGIC #&gt;&lt;2&gt;..#
# MAGIC #..&gt;&lt;..#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 4, move up:
# MAGIC #.######
# MAGIC #<em>E</em>&lt;..22#
# MAGIC #&lt;&lt;.&lt;..#
# MAGIC #&lt;2.&gt;&gt;.#
# MAGIC #.^22^.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 5, move right:
# MAGIC #.######
# MAGIC #2<em>E</em>v.&lt;&gt;#
# MAGIC #&lt;.&lt;..&lt;#
# MAGIC #.^&gt;^22#
# MAGIC #.2..2.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 6, move right:
# MAGIC #.######
# MAGIC #&gt;2<em>E</em>&lt;.&lt;#
# MAGIC #.2v^2&lt;#
# MAGIC #&gt;..&gt;2&gt;#
# MAGIC #&lt;....&gt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 7, move down:
# MAGIC #.######
# MAGIC #.22^2.#
# MAGIC #&lt;v<em>E</em>&lt;2.#
# MAGIC #&gt;&gt;v&lt;&gt;.#
# MAGIC #&gt;....&lt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 8, move left:
# MAGIC #.######
# MAGIC #.&lt;&gt;2^.#
# MAGIC #.<em>E</em>&lt;&lt;.&lt;#
# MAGIC #.22..&gt;#
# MAGIC #.2v^2.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 9, move up:
# MAGIC #.######
# MAGIC #&lt;<em>E</em>2&gt;&gt;.#
# MAGIC #.&lt;&lt;.&lt;.#
# MAGIC #&gt;2&gt;2^.#
# MAGIC #.v&gt;&lt;^.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 10, move right:
# MAGIC #.######
# MAGIC #.2<em>E</em>.&gt;2#
# MAGIC #&lt;2v2^.#
# MAGIC #&lt;&gt;.&gt;2.#
# MAGIC #..&lt;&gt;..#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 11, wait:
# MAGIC #.######
# MAGIC #2^<em>E</em>^2&gt;#
# MAGIC #&lt;v&lt;.^&lt;#
# MAGIC #..2.&gt;2#
# MAGIC #.&lt;..&gt;.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 12, move down:
# MAGIC #.######
# MAGIC #&gt;&gt;.&lt;^&lt;#
# MAGIC #.&lt;<em>E</em>.&lt;&lt;#
# MAGIC #&gt;v.&gt;&lt;&gt;#
# MAGIC #&lt;^v^^&gt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 13, move down:
# MAGIC #.######
# MAGIC #.&gt;3.&lt;.#
# MAGIC #&lt;..&lt;&lt;.#
# MAGIC #&gt;2<em>E</em>22.#
# MAGIC #&gt;v..^&lt;#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 14, move right:
# MAGIC #.######
# MAGIC #.2&gt;2..#
# MAGIC #.^22^&lt;#
# MAGIC #.&gt;2<em>E</em>^&gt;#
# MAGIC #.&gt;..&lt;.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 15, move right:
# MAGIC #.######
# MAGIC #&lt;^&lt;22.#
# MAGIC #.2&lt;.2.#
# MAGIC #&gt;&lt;2&gt;<em>E</em>.#
# MAGIC #..&gt;&lt;..#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 16, move right:
# MAGIC #.######
# MAGIC #.&lt;..22#
# MAGIC #&lt;&lt;.&lt;..#
# MAGIC #&lt;2.&gt;&gt;<em>E</em>#
# MAGIC #.^22^.#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 17, move down:
# MAGIC #.######
# MAGIC #2.v.&lt;&gt;#
# MAGIC #&lt;.&lt;..&lt;#
# MAGIC #.^&gt;^22#
# MAGIC #.2..2<em>E</em>#
# MAGIC ######.#
# MAGIC 
# MAGIC Minute 18, move down:
# MAGIC #.######
# MAGIC #&gt;2.&lt;.&lt;#
# MAGIC #.2v^2&lt;#
# MAGIC #&gt;..&gt;2&gt;#
# MAGIC #&lt;....&gt;#
# MAGIC ######<em>E</em>#
# MAGIC </code></pre>
# MAGIC <p><em>What is the fewest number of minutes required to avoid the blizzards and reach the goal?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''#.####################################################################################################
#<<<><>.>>vvv>vv.>.>>^>^v>>^<.vv^.v>>v<><^^><^<^<v<^>>v>vv^^<v^><v.v<>^<<^.vv.v<..<.^v<..>>v<.<><v<.>#
#<<^>.><>v<^<>.^>>>>vv.v>>^.^v>v^v>v^>v^^><.<vv<^<v>^^>.><vvv>^v..>.>>v^<<.<v^v>^.^^<^<^^^.<>v.vvv>v>#
#<v<<^vv.^^<^v.v<>><^>v^v^^<<>v^^vvv..<>^v><<<>v^^<^>v><.v>^^^>v^<.<>v>^><v^v^<>>.<v<<^<^.>>><<v>v.>.#
#>>v^^<.<<v>^v<^><<<.^^>..v^>>v^<>vv^.^<><..v<^><>^<v<^vv>^.<^<<^>>>v^^^<<v<<^>>v^>>>>..v>^..<.><>>>>#
#>>v^>..^>^>v><><<^<^.<v<.<<><v^<^v^^>v>.v.v>>.<<^^>v<<vv<>><^.<..>.v^<vv^v.v<v^<^.<<>^>.<<<>^<>>^^^>#
#<>^.^<>v^>^^>>^>v<v^<^v^<.v<>^<^^^v.^vv^<>>v>>>vvv>v<v<vv<v<>.>^<.vv<vvv>>v<<><.<v..^>>.v^v<^v<..^<>#
#<<v>^v<^.v>v^v.<^^.vv<^>^><<v>>>.>^<v><^.><><<^>^^<<^^v>v>><vv>v^v^>^>v<v.v^<v>v>v<v.><v^.^v^.v>.>^<#
#<^<^<.<v.>>v.>>^v.<>^><v>><^v^..<.v><>>vv>v^vvv><>>>v<<><><^>v>>^>v..^v^v>v>>v>.v^^<v>^^.<><>^^>>>^>#
#>>v^>>v^>.vv<<>.>>>vv<<v<^^>vv<<vvv>v<.<<<><v><^v>>v<.<.^<.^.<><v.<.<vv>>>>^><>v><v<<<v^v.^v>>^v>.v>#
#>.^<>^^<<^v^>>^^><v.>v^.<v.<^^>>v^^v<^^>v.v<^<>v>.v^vvv^.^>>v^><.^^>.<^v>v<.>v^.>>v>.v<^>.^^v<<^<<<>#
#<>v>v.v>v<<>>.^>^<^^>vv>>v.><^<><^^<^^.<<vv^>^<v>>^^<v>vv^^v<<.<vv<<v<<<<>v>>.><<^v>.<>>.<>.^^>v<<>>#
#<vv>^^>^<^v.^<><><<^^>>>^vv>>>^^<><>^vv^<v<^>v^<^>.>>^^^<>^v>v.^<..v^>v>^<>^v^^^..>^<.v.vv<<><^^><.>#
#>v^<<.<<<<.v><><>^>^^.v>>..>>^v><><v<v^v^>^v<<v>v^<^<<>^<.<<^.^^<.>v<<>^.<.vv>^<^v^^>>>>><<<^><^v<.>#
#<<^^.>^^v>^<v<^^<^.<<^^^>^>vvv>><<.<^>^>>.>^>.v^^v>v<^^<vv^^v.><^>>.^.<>v>>><<^>><.><>^^>.vv<<^<<^>>#
#<><^v.><v<^^.v^v<.v^v<><v^<<<.v<^^.>>vv<<^><^^.><^^^^v>vv>><^>>^><><^<vv^^>^.v^^^<v><v^v<.v>vv^vvv><#
#<.>^v^v.v^^><.v<v<<^>^v>^^vv<>vv>>..>v^v<v.>^^>^.<^>^v^<><v>.>vvvv>>v>^>^<v^<.>>><v><>^.^>v^^.^>^^><#
#>>^.v>v.<>v^v^v^<^>v>>><>^^>^>.v>>>vv><<v.>v>v><v<<<>^<^^.><vvvvvvv^<>..<>.<><>v<<<<>>vvvv^<><<^vv>>#
#>..><>v<v>><<.v><v^v<<^vv<^.<v>v^<^v>vv>^^v<^<<<v.<^^>>v<vvvvv^<v^<.<<v<>vv>.v<>^><v^<^vv^.<vv>v<<^.#
#>....<v>^v^>>^<>><v>v^>vv<vvv.vv<>>^v<<><v^vv.v>v.v><^v<.>^v.^><>v>^v<<<v<v^<v>>v^>.^<v<v<^^v>.><^v<#
#>>>>.><>^>><vv^<<^v><>^>.<>>>^^>^vv>v>v.v>^vvvvvv^>^<>>.^>v>^^^^.v^^v<v<v^<<<v^<>>v.^^^>v.>.^v<><<.>#
#<.>.><>><v^v<<>v<>>^>^>>v<v>><^v<^>>..v<v^<>>>>vvvv<<^.>v><>^^v<<.^v<v.v^>v^>>^^>^>>^v>^.^^v^^<v^<^<#
#<..v^.^>vv^<vv^^v.>vvv<><v.>v.^^<vv^<<vv^^<^.^>>v.<vvv^^^>^^^v>>^v><>v^<>.<.>^>^v>^<vv>><<>^><v^><^<#
#.^v^<^^v>.>^^>>^v>v<<>>>^<<v><>^vv<v<^.v.^<v><>^><.>>>^^v^>>vv<>v<.^^v<<>>>^^<^>v<v^v^<v>>^><^^>^v^>#
#<<>>^>^v><.<>^vv..vvv>^<^<<^vv.v.<<><.^.>>>>>vv<>^><^v<><^v^^vv^.v><^>vv.^v.<vvvv><^v^v>>v<^v<<>>.^<#
#><<^<v<>>>^<.^^>vv<<^^>^<v<.^vv.>.v<<^>>>>^<.^^>>>.v<>.^.v<<^^<>^v<<<vv^.^>v.>^v><vv<.^>v>v^.<.^vvv<#
#<^>v.^..^vv^<>v<^v..v^><<<^<><<.^>.>vv<v>>v^>><><^^vv.>v^v^>>v.vv>^^<v.^v<v>^>><<vv<^v^.>>>^^v><>><>#
#<^>v>.^<^<>^^v>v^>.><^><.<<vv>v.^<>><<<^.<.v^<>><vv><<vvvv^v^^.><>><v^>>>^v>^<<>^<>>^>v<.v>.>^v^v><>#
#>><>v^<vv.<.v<vv..v<>.>^vv^.>vv>^>v^v^.vv.<.<><>><<^vvvv^v>>.<>^v>^>^><v^.v>^.<....>><vvv^<v.<v>.<..#
#>v^v<>v^>v.^^v><<<v>>^<>.v^^>>^<<.vv.v<<><^.>^>vvv><<><v<>v>^<^<^v^>^>^>..<>v.<^^v>^v>^v^^^.<><^^<^>#
#>>v<.<^>^v^^<>.^v...v<>v>>v>^><.v^^^v>v.v>>.^^^^<v<^<<>v<^v^>>.vv>^<v>^<^^^...<<<v<<<<.<^>.v^>>v.>>>#
#>>^^<>>^v^v>.^>vvv^>>^<><..>>v>^<vvvvv.^>^vv^v<>>vvvv<.<.^v>v>v>..v^vv>v>.vv<v^<>v^<>^><<><^^vvv>v<<#
#>^>vv.<v^^v>v<>v<.v^^>v^^^<v>v^<>><..<^><<v>>v.<.>^><^^<^v^>>^<v><v^^.v..^vv>^<>^v^>>^^vvv.>v^^^.<v.#
#<>^<.vvvvv<.<^<<.>^>>vv<<<.^v<vv^.<v^^.^v^<v<>^>>^>>^>^>v>^vv<><^<^<.>.^v<>>^.v^.<vv.>>><.v.<>^<<>v>#
#<^^v^><<v>>>^><.<<v^<>>v<>..<<^>^^.>..^^^<^v<>^.><<v>v>v>>^<<v^^<>^<><v<><^v>v.>>>.<v<><<><>^>^v<><>#
#<v<>^<>>.<v^^v>^^<<><>vvvv^^><<v^>v^v><v^<>.v^>v><^v^>^vv.^v><^v^><<^.<>^vv.vv<<^<.^v>^<v^>v^<^<>^<<#
####################################################################################################.#'''

# COMMAND ----------

import collections
import functools


@functools.cache
def get_blizzards(t):
  if t == 0:
    return blizzards_start
  
  blizzards = {}
  for pos, l in get_blizzards(t - 1).items():
    for c in l:
      new_pos = [
        pos[0] + (c == 'v') - (c == '^'),
        pos[1] + (c == '>') - (c == '<')
      ]
      if tuple(new_pos) not in free:
        if c == '^':
          new_pos[0] = bottom_side
        elif c == '>':
          new_pos[1] = left_side
        elif c == 'v':
          new_pos[0] = top_side
        elif c == '<':
          new_pos[1] = right_side

      blizzards[tuple(new_pos)] = blizzards.get(tuple(new_pos), '') + c
    
  return blizzards


def solve(start, target, t_start):
  seen = set()
  queue = collections.deque([(start, t_start)])
  while queue:
    pos, t = queue.popleft()

    if (pos, t) in seen:
      continue
    seen.add((pos, t))

    if pos == target:
      return t
    
    if pos in get_blizzards(t):
      continue
    
    for d in ['up', 'down', 'left', 'right', 'none']:
      new_pos = (
        pos[0] + (d == 'down') - (d == 'up'),
        pos[1] + (d == 'right') - (d == 'left')
      )
      if new_pos not in free:
        continue
      queue.append((new_pos, t + 1))


grid = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}

free = {pos for pos, c in grid.items() if c != '#'}
left_side = 1
right_side = max(col for row, col in free)
top_side = 1
bottom_side = max(row for row, col in free) - 1

start = (0, 1)
target = (len(inp.splitlines()) - 1, len(inp.splitlines()[0]) - 2)
blizzards_start = {pos: c for pos, c in grid.items() if c in '^>v<'}

time_to_goal = solve(start, target, 0)
answer = time_to_goal
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As the expedition reaches the far side of the valley, one of the Elves looks especially dismayed:</p>
# MAGIC <p>He <em>forgot his snacks</em> at the entrance to the valley!</p>
# MAGIC <p>Since you're so good at dodging blizzards, the Elves humbly request that you go back for his snacks. From the same initial conditions, how quickly can you make it from the start to the goal, then back to the start, then back to the goal?</p>
# MAGIC <p>In the above example, the first trip to the goal takes <code>18</code> minutes, the trip back to the start takes <code>23</code> minutes, and the trip back to the goal again takes <code>13</code> minutes, for a total time of <code><em>54</em></code> minutes.</p>
# MAGIC <p><em>What is the fewest number of minutes required to reach the goal, go back to the start, then reach the goal again?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = solve(
  start,
  target,
  solve(target, start, time_to_goal)
)
print(answer)
