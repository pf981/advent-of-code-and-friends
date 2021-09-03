# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/8

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 8: Two-Factor Authentication ---</h2><p>You come across a door implementing what you can only assume is an implementation of <a href="https://en.wikipedia.org/wiki/Multi-factor_authentication">two-factor authentication</a> after a long game of <a href="https://en.wikipedia.org/wiki/Requirement">requirements</a> <a href="https://en.wikipedia.org/wiki/Chinese_whispers">telephone</a>.</p>
# MAGIC <p>To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a <a href="https://www.google.com/search?q=tiny+lcd&amp;tbm=isch">little screen</a>, and you type that code on a keypad. Then, presumably, the door unlocks.</p>
# MAGIC <p>Unfortunately, the screen has been <span title="BUT BY WHOM?!">smashed</span>. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen <em>would</em> have displayed.</p>
# MAGIC <p>The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is <em><code>50</code> pixels wide and <code>6</code> pixels tall</em>, all of which start <em>off</em>, and is capable of three somewhat peculiar operations:</p>
# MAGIC <ul>
# MAGIC <li><code>rect AxB</code> turns <em>on</em> all of the pixels in a rectangle at the top-left of the screen which is <code>A</code> wide and <code>B</code> tall.</li>
# MAGIC <li><code>rotate row y=A by B</code> shifts all of the pixels in row <code>A</code> (0 is the top row) <em>right</em> by <code>B</code> pixels. Pixels that would fall off the right end appear at the left end of the row.</li>
# MAGIC <li><code>rotate column x=A by B</code> shifts all of the pixels in column <code>A</code> (0 is the left column) <em>down</em> by <code>B</code> pixels. Pixels that would fall off the bottom appear at the top of the column.</li>
# MAGIC </ul>
# MAGIC <p>For example, here is a simple sequence on a smaller screen:</p>
# MAGIC <ul>
# MAGIC <li><p><code>rect 3x2</code> creates a small rectangle in the top-left corner:</p><pre><code>###....
# MAGIC ###....
# MAGIC .......</code></pre></li>
# MAGIC <li><p><code>rotate column x=1 by 1</code> rotates the second column down by one pixel:</p><pre><code>#.#....
# MAGIC ###....
# MAGIC .#.....</code></pre></li>
# MAGIC <li><p><code>rotate row y=0 by 4</code> rotates the top row right by four pixels:</p><pre><code>....#.#
# MAGIC ###....
# MAGIC .#.....</code></pre></li>
# MAGIC <li><p><code>rotate column x=1 by 1</code> again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:</p><pre><code>.#..#.#
# MAGIC #.#....
# MAGIC .#.....</code></pre></li>
# MAGIC </ul>
# MAGIC <p>As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market.  That's what the advertisement on the back of the display tries to convince you, anyway.</p>
# MAGIC <p>There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, <em>how many pixels should be lit?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 5
rotate row y=0 by 3
rect 1x2
rotate column x=30 by 1
rotate column x=25 by 1
rotate column x=10 by 1
rotate row y=1 by 5
rotate row y=0 by 2
rect 1x2
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 18
rotate row y=0 by 5
rotate column x=0 by 1
rect 3x1
rotate row y=2 by 12
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=20 by 1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 15
rotate row y=0 by 15
rotate column x=10 by 1
rotate column x=5 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=37 by 1
rotate column x=23 by 1
rotate column x=7 by 2
rotate row y=3 by 20
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 5
rotate row y=2 by 2
rotate row y=1 by 4
rotate row y=0 by 4
rect 1x4
rotate column x=35 by 3
rotate column x=18 by 3
rotate column x=13 by 3
rotate row y=3 by 5
rotate row y=2 by 3
rotate row y=1 by 1
rotate row y=0 by 1
rect 1x5
rotate row y=4 by 20
rotate row y=3 by 10
rotate row y=2 by 13
rotate row y=0 by 10
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 10
rotate row y=3 by 10
rotate row y=1 by 10
rotate row y=0 by 10
rotate column x=7 by 2
rotate column x=5 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 20
rotate row y=3 by 12
rotate row y=1 by 15
rotate row y=0 by 10
rotate column x=8 by 2
rotate column x=7 by 1
rotate column x=6 by 2
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=46 by 2
rotate column x=43 by 2
rotate column x=24 by 2
rotate column x=14 by 3
rotate row y=5 by 15
rotate row y=4 by 10
rotate row y=3 by 3
rotate row y=2 by 37
rotate row y=1 by 10
rotate row y=0 by 5
rotate column x=0 by 3
rect 3x3
rotate row y=5 by 15
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=7 by 3
rotate column x=6 by 3
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=19 by 1
rotate column x=10 by 3
rotate column x=5 by 4
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 40
rotate row y=2 by 35
rotate row y=1 by 15
rotate row y=0 by 30
rotate column x=48 by 4
rotate column x=47 by 3
rotate column x=46 by 3
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=42 by 5
rotate column x=41 by 5
rotate column x=40 by 1
rotate column x=33 by 2
rotate column x=32 by 3
rotate column x=31 by 2
rotate column x=28 by 1
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=25 by 1
rotate column x=23 by 5
rotate column x=22 by 5
rotate column x=21 by 5
rotate column x=18 by 5
rotate column x=17 by 5
rotate column x=16 by 5
rotate column x=13 by 5
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 1
rotate column x=2 by 5
rotate column x=1 by 5
rotate column x=0 by 1'''

# COMMAND ----------

import numpy as np
import re

screen = np.zeros((6, 50), bool)

for line in inp.split('\n'):
  command = re.findall(r'\w+(?: [a-z]+)?', line)[0]
  args = [int(x) for x in re.findall(r'\d+', line)]
  
  if command == 'rect':
    screen[:args[1], :args[0]] = True
  elif command == 'rotate row':
    screen[args[0], :] = np.roll(screen[args[0], :], args[1])
  elif command == 'rotate column':
    screen[:, args[0]] = np.roll(screen[:, args[0]], args[1])

answer = screen.sum()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is <code>5</code> pixels wide and <code>6</code> tall.</p>
# MAGIC <p>After you swipe your card, <em>what code is the screen trying to display?</em></p>
# MAGIC </article>

# COMMAND ----------

for line in screen:
  print(''.join('#' if x else ' ' for x in line))

# COMMAND ----------

answer = 'CFLELOYFCS'
answer
