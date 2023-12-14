# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/14

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 14: Parabolic Reflector Dish ---</h2><p>You reach the place where all of the mirrors were pointing: a massive <a href="https://en.wikipedia.org/wiki/Parabolic_reflector" target="_blank">parabolic reflector dish</a> <span title="Why, where do you attach YOUR massive parabolic reflector dishes?">attached</span> to the side of another large mountain.</p>
# MAGIC <p>The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.</p>
# MAGIC <p>This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.</p>
# MAGIC <p>Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.</p>
# MAGIC <p>In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you <em>tilt</em> it in one of four directions! The rounded rocks (<code>O</code>) will roll when the platform is tilted, while the cube-shaped rocks (<code>#</code>) will stay in place. You note the positions of all of the empty spaces (<code>.</code>) and rocks (your puzzle input). For example:</p>
# MAGIC <pre><code>O....#....
# MAGIC O.OO#....#
# MAGIC .....##...
# MAGIC OO.#O....O
# MAGIC .O.....O#.
# MAGIC O.#..O.#.#
# MAGIC ..O..#O..O
# MAGIC .......O..
# MAGIC #....###..
# MAGIC #OO..#....
# MAGIC </code></pre>
# MAGIC <p>Start by tilting the lever so all of the rocks will slide <em>north</em> as far as they will go:</p>
# MAGIC <pre><code>OOOO.#.O..
# MAGIC OO..#....#
# MAGIC OO..O##..O
# MAGIC O..#.OO...
# MAGIC ........#.
# MAGIC ..#....#.#
# MAGIC ..O..#.O.O
# MAGIC ..O.......
# MAGIC #....###..
# MAGIC #....#....
# MAGIC </code></pre>
# MAGIC <p>You notice that the support beams along the north side of the platform are <em>damaged</em>; to ensure the platform doesn't collapse, you should calculate the <em>total load</em> on the north support beams.</p>
# MAGIC <p>The amount of load caused by a single rounded rock (<code>O</code>) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (<code>#</code>) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:</p>
# MAGIC <pre><code>OOOO.#.O.. 10
# MAGIC OO..#....#  9
# MAGIC OO..O##..O  8
# MAGIC O..#.OO...  7
# MAGIC ........#.  6
# MAGIC ..#....#.#  5
# MAGIC ..O..#.O.O  4
# MAGIC ..O.......  3
# MAGIC #....###..  2
# MAGIC #....#....  1
# MAGIC </code></pre>
# MAGIC <p>The total load is the sum of the load caused by all of the <em>rounded rocks</em>. In this example, the total load is <code><em>136</em></code>.</p>
# MAGIC <p>Tilt the platform so that the rounded rocks all roll north. Afterward, <em>what is the total load on the north support beams?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''...#O#O#.#...O...O...##...#..O#OO..OO....#.#OO....#.#.......O..O.#..#O.#......#.OO.....#....OO#....#
.#.##......O.O.#..#.OO..........#O.#....O.#..O............#.O.......#....OO.#.#..#O.O..#....O....O..
.#OO......O.O.O#O.#.##.....O...O....#O.O.OO.....OO...O..#O..O...O..#...O.#...#.....#O......O.....#..
O...##OO..O.O..##...O#..O#O.......#.OO..#....#...#.O....#.O..#O..#O...O.###.#....#.#..##.#...O...#.#
...#.#.....#....#O#...#..OO...#..#.......O.O..O##....O#.OOOOO.##.....O..#.O.OO..O.....O....#.O....OO
O#......O..#O##O........OO..#......#...#O..O..##.............O..#........O...##OOO.###O.O.##.O.#.O.O
.#O...OOO...#..O#.#.O.O..........#.O#..#.#....OO#O##.#...OO....#O.OO..#......#.......#...O..#.O.O##.
.#......#O..O..#..#.#.........O...#.#........O.#...O....#.O...#.......O#.O..#.#.....O...##....#.#O..
#..O..#OO...O##......#........O....O#..O.O..OO.OO....##O.OO...O##.#OO#...O..#..O....O.O.O.O...O.OO..
....##.O..OO.#.....##.#O#O.O.#..#...#..OO#......OO.......O.O.O.O..##..O.##......O...O.#..O...O.O.###
.O.#O......O.O.#....#......O#.......O......O#.O...#...O...#..#.#..#...##.#..##...O#O#.O.#.#...#.#.O.
#O.O....##....#..O.###..O.......OOOO#O#O.#OO.##...OO.O#........O..#OO.#.#...O.O.O....O....#O.##...#O
.OOO...O....#O.#....#..O#..OO.....#.#......#OO..#........O.O.O.....#....O.O#.O.....O.OO.##O..O##....
...O#....#O...O..##..O.#..O#..OOOO#..OOO.#O#..#OO.O...O..#.#..#..#..#O..O.OO..O...O.O..OO...........
..OO###..##..#.....O....O.....O.#O.......O..O..##...O#...O#..#...O..O....O#.O##..............#....O#
.##.###.....###O....O.O..O...O.O..O.#......#O.#..O.O#.#O##O..O#.....O.#...........O..O....O...O.O...
...O.................#...........#.O.......O.....#..O.O.O.....O........##.OOO.#.....O.OO...........#
..O.O#...#O...O.#....#.OO..#O..#.....#.##.....OO....O..O...#...#..OO..O.O....#OO........#O.##....O..
O..#..O.#.O....O..#OO##.OO...O.##O..#..#.##..O#.#.OO.O........O....#O.OO.O.#O.O.#...##O##..OO..#.O..
...#.O#..........O###...#.O.#.O#.#.OO...OO#...O.....O..O..#.OO.....##...O#........#.O.O......#.O....
OO#..O.##..##OO..#....O..#.O..#..O.#...#O#.O..O###....O#O#.#..O#.##.#......#.....O..OO..........#O..
#O.##..#.....###.#O#...#O.##....#...O..#..#..##...#.#..#.#O...O.#.#O....##O..O.O...O.#.OO.##..O#.O..
#O#.....#O.....#.##.O..O....#..O.........#....#.O#.O..........#...O.O#..#.O.#....#.O..O.O#O.O.#O.#..
.O#.O..O#...#......O..#O#.O#....#...###.#.#.##.O#...#..#O#O.O...#.#...O...##.O#.#O.....O....O.......
O........O....##..##.OO.....OO...O..#..O#...O..O..OOO...O...O......#..##....O.#...O#O............#..
..#OO.OO.O..##...#........O......O.#O..O#.#O#.#...#.#...O.O....O......#....#.#..#.#............#..OO
...##O.O.......#...#O#..OO..O.O.#.#..##.........O##O..O..O#..O#.#O..O...O.......##OO..OO..#O..###O#.
.....#..O..........O.....O#...O.O#....#O#...O..#.#O#....#.#O......O....##......O..OOO#O...#...##O..#
......O##...OO.OO#.OO#..#...#...#.#...#OO...O.......#..O.O.O.##..#......O##....#......OO.#O..#O.O...
....OO....O##..O..O.O.......#....O.O....#.OO...O..#O.#..#.#O.#.....O..#.OO.OO..#....O.....O.O#O...O.
OOOO.O.#.#O#.O.........#O..O#O...O.#..#...O...O.OO..OO...#O#.##O.O.#...OO##...O..##OO..#O...O..O.OOO
#O.O.#.O.OO.O...#O#.#O.OO..O#O...O###....O....O.O.O.....O...#.OO.##....O.O..#......#..#O.O##...#.O#.
O#......O.#...O.....O.O..#.##.OO...O...O.......O.O.#...#OO..OO...OO..O.##.O...#O#.O........OO#....##
OO......O#.#..O...O...O..##O...O.###..O..OO...OO..O.#O...#.#...O.#.OO.......#.##...O......O#.....O..
.#..##.....OO...O...O..#.......O.O.#....O..#...O....O..O#...OO.......O...O.O.#..O.O....O.O.#.O.O.OO.
....O....O.#O#....#O#O..O.....#..#.O.O.O..O...O.O..O...O..#O#....O.O.............O..O...O....O......
..#.O....OOOO#OO#.#.O..O....O....O.#.#..O....#.O#.O......O...#.............O##.......#....O..######.
......OO##O..##O#.....O..OO.#..#O..##..#.O#........O.O...##OO......OO.#.#...#.OO...O.OO......O.O...#
OO..O....O..#.#.O#..O#O...###.O#.....O...##....OOO...#O..O..#OO.O#....##.O..O.........OOO.........O#
..O.O.O#O...OO..##....#.#...O...#.##.......##...#O.#O..#...##.....O.....OOO..O...O......#...OO...#.O
#O...OO.........OO.O....#OO......O##.O..##....O..#.O.O.O#.O.OO#O..O...#.#...#.#...O.OO...##.....##.O
...OOOOO.O...O#.......OO#.O..OO..#OO......O...#..O##.#....O#....O.O...#.....##.O....#..##..O..#.....
.OO.....O#....#....#O..O..OO#OOO..O#.......#O#..O.O..O..O##..O.......OO.......O.##...O.O..#........O
....O#.O......#..O.OO...OO#.#..O#....O..O#.#..#...O#..OO...#O#.....O...O.....##.#..#O.O..O#OO.O.#O.O
..O.#.#.....O#.O.....OOOO.O..#..#O.#.#O.#OO.....O..#..O..O..#O......##O.#O..#.OOO....#O.O.#O...#..O.
......#.O...O.O#....OO#..O#....#..O...O.......#OO...#...##O#O##.O...O...O......O##.O.O#.#OO.OO.O#...
....O...O.O..#..O........O..OO...OO#...OO.......O#.OOO#...OO#OO#O.O.O#OO.....O.###O..O#.O...#.......
#O.#OO.....##O.O....O..O.OO.#...O...#.O.O..O.OOO#.....O....#.....O...##...#...#..#........#..#.O..O.
...O#......O..O.#.......#....#O...OOOO...O..O.O.O.#O....#.....O..#...O..#..O..............#O....OO..
OO....O.#..O.#..#.#OO#...OO...O.#O...OO......#..O#..O..O#O...#OOO#..#.O...##.......#.#OO.O.###.O...#
.OO...#.O...#O.O.....O...##.#..O.#O.O.....O..O.....##...OO...O..#O..........#OO.#......O#...O#...O..
.O.#.O.O..........O...O.#.##OO....##........O.#.....O#O...#.O.....OOO#..........#..O..#..O.#O.#..O..
.O..#.....#O......O....O....O....#..#.....O...O...OO#...O..#...O...#...O.##OO.#.O#.OOO#OO#...#....#.
.OOO#.....O.O.#.OO.........#O##.OO##O..#..#OO.OOOO...O..#.#..O#....OO..#...O#O....#OOO.#...O.#..#...
...O#...#..#.#...O.#O..#.......#...#...O#......#O.O.#.OO.O#O.O.#.O....##..O#O.##.#.....OO..O......O.
..#.#.O.O.#..O..#.O....OO....O##.O.#...#O...O.OO.O......#..O.....#........O.#......O.#.##..OO...OO.#
....O...##....OO#O#O..#.O.##..O....##OO....O..OOO..#O..#.O...#.......O#.......OO.O.#..#.OO.O..#OO...
.#.....#O#.#OO#.#.#O##.O#....#.....#.##..O...#.....O#.O.O...O.O....#........#O...#..OO..O.#.OOOOO.O#
O....#O......O...O..O#..#.O..O.OO.....#.O.OO.O...#O.OOO....O.........#....#.#.O.##.#O...O.O#O.O#..#.
.OO.O..OOOO#.#.......O..................O......#..#...O.#O#O.....#..O..#O.#..........##.#O#.O..##...
..O...O.OO#.O##.##.#O....O....#...#...O...OOO........O.O..#.##......###.........##...O..O...OO...O.#
OOOO......#.O..OO.OO#..#...O.##.#O..O#.OO#.......#.O.O.OO.O.#OO#O.#...#......O#O..O.O....#O##.O..O.#
.......O..O...OO.#O..O....O#..#.##.......O...........#..#.....O......#.#..O.......O.O#..#.O.#O.OOO#.
#.#.O...##.......O...O..O.#..#....O##......O.##OO......OO.....O.O.##.#....#...O....#O#.#....#.O#..#.
O.O......O#.....#...#..#.O#..##O..O#O......O.......##..O.....#O.O...O..#..O..O...#.O.#..O..#.O#.#.O.
.#...OO#.O#.#.O.O.O..OO....OO....O...O#.O.#......#.O#.OO#.O..O.OO.O.#.O...OO.....###O..#.O.....O.O#O
..##OO...#..##.O#.......#......#.......O..OO.....O...OO...#..O..O..O..OO.O.O.O......O#...O.#..O.O#..
...#.O..#...O.#.##.O.OO..OO.....#..#..O..#..O.#..O..OO..O.#.#...##......#...#O.#....#O#...OOO#...#..
.......#O...#......O..O...#..O..#....#.O..O.##........#.....O....O...#O#OOOOOO..O.....##..O..#O.O...
#.O...OOO..O.O.###.#..O..OO.O....O##...#.O....OO.......O..........##...O...#.#.OO.###...O..........O
#....O#OO.OO#O..............#.#.#...O#OO.##.#...O.O....O....#O.#..#......O.....O..O.O#O......OO....O
...O.OO....OO.O..O#O.O.O.....O.#.O.#..O....#.O#O.#.......OO....#.#.O...O.#.#..#O.O##..#.#...#....O#.
..#.O...OOO..O..#..O#.O....#O#O.O##....O.O.....O...........O#...##.....#....O....O.OOO#O..##O..O.O..
O#..........#..O#OO....OOO..O#..O..OO.....O....#.....OOOOO.#....O#O..O.....#....#..O....O...#.O#..#.
.O.#.#.O..#.O#O...#.O.O...#..#...#.....#....##O.OOO#...OO..O..................O.#OO...O#.....O...#O.
##..#.#..#.#.O###O#.O..###.......#O..O......#..#.#......O..OO#..#OO...O#...#..OO#O.#.OO#..#..O...O..
........O....O..#..#..O.OOO....O.#O.....#O......O..OO##O#O.#.OO........O.#...OOO..O#...O..O.....#...
..OO.O.O..O...#.......O#.O.O.#O..O..#...#......#.#O#.O....#...#..O......O#...O.##.O....O.O.O.O..O#..
..#..O..#.#O.O...O.#..#..#.##...O.#..#.O..O.#..O....#..OO..OO.#.#...O..OO.......O...#.O#OO..O...#.#O
.#......OO#...##.#.#.....O...#.................O....#....##.O#O.#...O...O#....#O....O....O....###...
...OO.##.OOO...OO..O.O...#......O.....O.......O.O.OO..#O#O.O#....#....#..O##O....#OO#.......O..#...#
O.O..O#O....O.O#O.OO.O.....OOO..O...O.O.##.O.#O.O#.#.#O#......O.#.O..O.#.O....OO##.....#...O.#OOO...
#.#.....#.O.O#.O..O...#OO....O#.......#.#..O..##..#O..O...##.##..O..O#....#...OO...O..OO...#..#..O..
#.O.#.O#..#...O....O..O.O.OO##..........#..O...#.O#OO..O.O.#.........O#.O...O.....#O.O.O...#O...O.##
....#O...O....##.#.O.##O...#..#.#..O.O#..O..#O.#......#.......OO..O.....OOO#O....OO..#O.....O..#..O.
.OO#.....#.OOO....#.....#O###....O.##O...#.##..O.....O......O..O.OOOO.#...O.#..#.###...O..#..O..OO.#
...#O#..O#.O....O.OO.O.#.O..#...........O..#O.....O.....#OO.O#.O....O...#..O..O.#.O..##....##....O.O
###....#..O..#....O.............O#O..........O.O...#.O........#...#.O.....O##...O.#O#...O.O.#O.....O
..O.#.......O.....#..#....O.O.#.O#OO...#.#.#.....#OO.#..#......#...#...#..#.......O#.....O####OO.#.O
.O#....O..O.......#O..#.O#.#..OO.#...#.#.O.O.....O.O.#......#O.#O........O.OO.....OO..O..#OO.....#..
...#.#...O#O.##....O.#....OO..O.OO#...O.OO.OO..O....OO..#..O..O.##.#.OO.#OO..#..O.O.O#.O..OO.O.O#.O.
...#...O.....O...#....O...#...OO#.O#..#....O...........###.O#.....O.##O.O....O...O#....#...#.O...#..
...#..#....#.O.O..#O.#O.........##O....O.#OOO#.O##.#..O....#..#.O....O...OO#O..O.O.#....#.....#O#O#O
..#..#...#.#O......OOO..#.OOO..OO.O#...OO....#O.O.#.#....O...OO#...OO....O..##...#.#O....#.#OO.OO.O.
O.O...#..#O...O##..#..O.#............#..#...##O.O.O....O..O.O...O##.#..O...O..OO..#...O........#....
#.O##..#.....OOO.O..##O...#.O...####.OOO...#...O..#..#......O...#.....#.O.O.O...O##......#...O....#.
...###O.#.O.OO.........O##.#...O..#......O#.#...##O........O.O..O#....O..#.#.O.#.##.O.O#O#....O#.O#O
O...O.O..O.#.......O..O.O....O..O..#..#.........#O.OO..O..O.#O..O.....O.....#O.........#..O.#.#..O..
..O#...#......O..OO...O.#.##O.OO.#...OO..#OO#....#.#.O#..#O.#.OO..O...O#.OO.O...O.#.#.....O..#O....#
....O..#.....#..#.#O.O.OO.#...#.O...#.....##.#..#...OO........O#..O.OO..O.O..O.#...#....O..##..O....
'''

# COMMAND ----------

def tilt_north(grid):
    for col in range(len(grid[0])):
        free = None
        for row in range(len(grid)):
            if grid[row][col] == '.':
                if free is None:
                    free = row
            elif grid[row][col] == 'O':
                if free is not None:
                    grid[row][col] = '.'
                    grid[free][col] = 'O'

                    # Find next free spot
                    for r2 in range(free + 1, len(grid)):
                        if grid[r2][col] == '.':
                            free = r2
                            break
                    else:
                        free = None
            elif grid[row][col] == '#':
                free = None


grid = [list(line) for line in inp.splitlines()]
tilt_north(grid)
answer = sum(len(grid) - row for row, line in enumerate(grid) for c in line if c == 'O')
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "<em>spin cycle</em>" attempts to do just that!</p>
# MAGIC <p>Each <em>cycle</em> tilts the platform four times so that the rounded rocks roll <em>north</em>, then <em>west</em>, then <em>south</em>, then <em>east</em>. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.</p>
# MAGIC <p>Here's what happens in the example above after each of the first few cycles:</p>
# MAGIC <pre><code>After 1 cycle:
# MAGIC .....#....
# MAGIC ....#...O#
# MAGIC ...OO##...
# MAGIC .OO#......
# MAGIC .....OOO#.
# MAGIC .O#...O#.#
# MAGIC ....O#....
# MAGIC ......OOOO
# MAGIC #...O###..
# MAGIC #..OO#....
# MAGIC
# MAGIC After 2 cycles:
# MAGIC .....#....
# MAGIC ....#...O#
# MAGIC .....##...
# MAGIC ..O#......
# MAGIC .....OOO#.
# MAGIC .O#...O#.#
# MAGIC ....O#...O
# MAGIC .......OOO
# MAGIC #..OO###..
# MAGIC #.OOO#...O
# MAGIC
# MAGIC After 3 cycles:
# MAGIC .....#....
# MAGIC ....#...O#
# MAGIC .....##...
# MAGIC ..O#......
# MAGIC .....OOO#.
# MAGIC .O#...O#.#
# MAGIC ....O#...O
# MAGIC .......OOO
# MAGIC #...O###.O
# MAGIC #.OOO#...O
# MAGIC </code></pre>
# MAGIC <p>This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the <em>total load</em> on the north support beams after <code>1000000000</code> cycles.</p>
# MAGIC <p>In the above example, after <code>1000000000</code> cycles, the total load on the north support beams is <code><em>64</em></code>.</p>
# MAGIC <p>Run the spin cycle for <code>1000000000</code> cycles. Afterward, <em>what is the total load on the north support beams?</em></p>
# MAGIC </article>

# COMMAND ----------

def rotate_clockwise(grid):
    return [list(z)[::-1] for z in zip(*grid)]


def cycle(grid):
    for _ in range(4):
        tilt_north(grid)
        grid = rotate_clockwise(grid)
    return grid


def to_string(grid):
    return '\n'.join(''.join(line) for line in grid)


grid = [list(line) for line in inp.splitlines()]
seen = {}
loads = []
i = 0
while to_string(grid) not in seen:
    seen[to_string(grid)] = i
    loads.append(sum(len(grid) - row for row, line in enumerate(grid) for c in line if c == 'O'))
    grid = cycle(grid)
    i += 1

cycle_length = i - seen[to_string(grid)]
cycle_start = i - cycle_length
i_answer = cycle_start + ((1000000000 - i) % cycle_length)
answer = loads[i_answer]
print(answer)
