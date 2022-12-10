# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/10

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 10: Cathode-Ray Tube ---</h2><p>You avoid the ropes, plunge into the river, and swim to shore.</p>
# MAGIC <p>The Elves yell something about meeting back up with them upriver, but the river is too loud to tell exactly what they're saying. They finish crossing the bridge and disappear from view.</p>
# MAGIC <p>Situations like this must be why the Elves prioritized getting the communication system on your handheld device working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen tells you it probably won't be of much immediate use.</p>
# MAGIC <p><em>Unless</em>, that is, you can design a replacement for the device's video system! It seems to be some kind of <a href="https://en.wikipedia.org/wiki/Cathode-ray_tube" target="_blank">cathode-ray tube</a> screen and simple CPU that are both driven by a precise <em>clock circuit</em>. The clock circuit ticks at a constant rate; each tick is called a <em>cycle</em>.</p>
# MAGIC <p>Start by figuring out the signal being sent by the CPU. The CPU has a single register, <code>X</code>, which starts with the value <code>1</code>. It supports only two instructions:</p>
# MAGIC <ul>
# MAGIC <li><code>addx V</code> takes <em>two cycles</em> to complete. <em>After</em> two cycles, the <code>X</code> register is increased by the value <code>V</code>. (<code>V</code> can be negative.)</li>
# MAGIC <li><code>noop</code> takes <em>one cycle</em> to complete. It has no other effect.</li>
# MAGIC </ul>
# MAGIC <p>The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.</p>
# MAGIC <p>Consider the following small program:</p>
# MAGIC <pre><code>noop
# MAGIC addx 3
# MAGIC addx -5
# MAGIC </code></pre>
# MAGIC <p>Execution of this program proceeds as follows:</p>
# MAGIC <ul>
# MAGIC <li>At the start of the first cycle, the <code>noop</code> instruction begins execution. During the first cycle, <code>X</code> is <code>1</code>. After the first cycle, the <code>noop</code> instruction finishes execution, doing nothing.</li>
# MAGIC <li>At the start of the second cycle, the <code>addx 3</code> instruction begins execution. During the second cycle, <code>X</code> is still <code>1</code>.</li>
# MAGIC <li>During the third cycle, <code>X</code> is still <code>1</code>. After the third cycle, the <code>addx 3</code> instruction finishes execution, setting <code>X</code> to <code>4</code>.</li>
# MAGIC <li>At the start of the fourth cycle, the <code>addx -5</code> instruction begins execution. During the fourth cycle, <code>X</code> is still <code>4</code>.</li>
# MAGIC <li>During the fifth cycle, <code>X</code> is still <code>4</code>. After the fifth cycle, the <code>addx -5</code> instruction finishes execution, setting <code>X</code> to <code>-1</code>.</li>
# MAGIC </ul>
# MAGIC <p>Maybe you can learn something by looking at the value of the <code>X</code> register throughout execution. For now, consider the <em>signal strength</em> (the cycle number multiplied by the value of the <code>X</code> register) <em>during</em> the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).</p>
# MAGIC <p>For example, consider this larger program:</p>
# MAGIC <pre><code>addx 15
# MAGIC addx -11
# MAGIC addx 6
# MAGIC addx -3
# MAGIC addx 5
# MAGIC addx -1
# MAGIC addx -8
# MAGIC addx 13
# MAGIC addx 4
# MAGIC noop
# MAGIC addx -1
# MAGIC addx 5
# MAGIC addx -1
# MAGIC addx 5
# MAGIC addx -1
# MAGIC addx 5
# MAGIC addx -1
# MAGIC addx 5
# MAGIC addx -1
# MAGIC addx -35
# MAGIC addx 1
# MAGIC addx 24
# MAGIC addx -19
# MAGIC addx 1
# MAGIC addx 16
# MAGIC addx -11
# MAGIC noop
# MAGIC noop
# MAGIC addx 21
# MAGIC addx -15
# MAGIC noop
# MAGIC noop
# MAGIC addx -3
# MAGIC addx 9
# MAGIC addx 1
# MAGIC addx -3
# MAGIC addx 8
# MAGIC addx 1
# MAGIC addx 5
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx -36
# MAGIC noop
# MAGIC addx 1
# MAGIC addx 7
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx 2
# MAGIC addx 6
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx 1
# MAGIC noop
# MAGIC noop
# MAGIC addx 7
# MAGIC addx 1
# MAGIC noop
# MAGIC addx -13
# MAGIC addx 13
# MAGIC addx 7
# MAGIC noop
# MAGIC addx 1
# MAGIC addx -33
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx 2
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx 8
# MAGIC noop
# MAGIC addx -1
# MAGIC addx 2
# MAGIC addx 1
# MAGIC noop
# MAGIC addx 17
# MAGIC addx -9
# MAGIC addx 1
# MAGIC addx 1
# MAGIC addx -3
# MAGIC addx 11
# MAGIC noop
# MAGIC noop
# MAGIC addx 1
# MAGIC noop
# MAGIC addx 1
# MAGIC noop
# MAGIC noop
# MAGIC addx -13
# MAGIC addx -19
# MAGIC addx 1
# MAGIC addx 3
# MAGIC addx 26
# MAGIC addx -30
# MAGIC addx 12
# MAGIC addx -1
# MAGIC addx 3
# MAGIC addx 1
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx -9
# MAGIC addx 18
# MAGIC addx 1
# MAGIC addx 2
# MAGIC noop
# MAGIC noop
# MAGIC addx 9
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC addx -1
# MAGIC addx 2
# MAGIC addx -37
# MAGIC addx 1
# MAGIC addx 3
# MAGIC noop
# MAGIC addx 15
# MAGIC addx -21
# MAGIC addx 22
# MAGIC addx -6
# MAGIC addx 1
# MAGIC noop
# MAGIC addx 2
# MAGIC addx 1
# MAGIC noop
# MAGIC addx -10
# MAGIC noop
# MAGIC noop
# MAGIC addx 20
# MAGIC addx 1
# MAGIC addx 2
# MAGIC addx 2
# MAGIC addx -6
# MAGIC addx -11
# MAGIC noop
# MAGIC noop
# MAGIC noop
# MAGIC </code></pre>
# MAGIC <p>The interesting signal strengths can be determined as follows:</p>
# MAGIC <ul>
# MAGIC <li>During the 20th cycle, register <code>X</code> has the value <code>21</code>, so the signal strength is 20 * 21 = <em>420</em>. (The 20th cycle occurs in the middle of the second <code>addx -1</code>, so the value of register <code>X</code> is the starting value, <code>1</code>, plus all of the other <code>addx</code> values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)</li>
# MAGIC <li>During the 60th cycle, register <code>X</code> has the value <code>19</code>, so the signal strength is 60 * 19 = <code><em>1140</em></code>.</li>
# MAGIC <li>During the 100th cycle, register <code>X</code> has the value <code>18</code>, so the signal strength is 100 * 18 = <code><em>1800</em></code>.</li>
# MAGIC <li>During the 140th cycle, register <code>X</code> has the value <code>21</code>, so the signal strength is 140 * 21 = <code><em>2940</em></code>.</li>
# MAGIC <li>During the 180th cycle, register <code>X</code> has the value <code>16</code>, so the signal strength is 180 * 16 = <code><em>2880</em></code>.</li>
# MAGIC <li>During the 220th cycle, register <code>X</code> has the value <code>18</code>, so the signal strength is 220 * 18 = <code><em>3960</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>The sum of these signal strengths is <code><em>13140</em></code>.</p>
# MAGIC <p>Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. <em>What is the sum of these six signal strengths?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''addx 1
noop
addx 2
noop
addx 3
addx 3
addx 1
addx 5
addx 1
noop
noop
addx 4
noop
noop
addx -9
addx 16
addx -1
noop
addx 5
addx -2
addx 4
addx -35
addx 2
addx 28
noop
addx -23
addx 3
addx -2
addx 2
addx 5
addx -8
addx 19
addx -8
addx 2
addx 5
addx 5
addx -14
addx 12
addx 2
addx 5
addx 2
addx -13
addx -23
noop
addx 1
addx 5
addx -1
addx 2
addx 4
addx -9
addx 10
noop
addx 6
addx -11
addx 12
addx 5
addx -25
addx 30
addx -2
addx 2
addx -5
addx 12
addx -37
noop
noop
noop
addx 24
addx -17
noop
addx 33
addx -32
addx 3
addx 1
noop
addx 6
addx -13
addx 17
noop
noop
noop
addx 12
addx -4
addx -2
addx 2
addx 3
addx 4
addx -35
addx -2
noop
addx 20
addx -13
addx -2
addx 5
addx 2
addx 23
addx -18
addx -2
addx 17
addx -10
addx 17
noop
addx -12
addx 3
addx -2
addx 2
noop
addx 3
addx 2
noop
addx -13
addx -20
noop
addx 1
addx 2
addx 5
addx 2
addx 5
noop
noop
noop
noop
noop
addx 1
addx 2
addx -18
noop
addx 26
addx -1
addx 6
noop
noop
noop
addx 4
addx 1
noop
noop
noop
noop'''

# COMMAND ----------

x = 1
signal_strengths = []
xs = []
cycle = 0
for line in inp.splitlines():
  args = line.split(' ')
  cycle += 1
  signal_strengths.append(x * cycle)
  xs.append(x)
  
  if args[0] == 'noop':
    continue
  
  cycle += 1
  signal_strengths.append(x * cycle)
  xs.append(x)
  x += int(args[1])

answer = sum(signal_strengths[i - 1] for i in [20, 60, 100, 140, 180, 220])
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It seems like the <code>X</code> register controls the horizontal position of a <a href="https://en.wikipedia.org/wiki/Sprite_(computer_graphics)" target="_blank">sprite</a>. Specifically, the sprite is 3 pixels wide, and the <code>X</code> register sets the horizontal position of the <em>middle</em> of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)</p>
# MAGIC <p>You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. The left-most pixel in each row is in position <code>0</code>, and the right-most pixel in each row is in position <code>39</code>.</p>
# MAGIC <p>Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws <em>a single pixel during each cycle</em>. Representing each pixel of the screen as a <code>#</code>, here are the cycles during which the first and last pixel in each row are drawn:</p>
# MAGIC <pre><code>Cycle   1 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle  40
# MAGIC Cycle  41 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle  80
# MAGIC Cycle  81 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 120
# MAGIC Cycle 121 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 160
# MAGIC Cycle 161 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 200
# MAGIC Cycle 201 -&gt; <em>#</em>######################################<em>#</em> &lt;- Cycle 240
# MAGIC </code></pre>
# MAGIC <p>So, by <a href="https://en.wikipedia.org/wiki/Racing_the_Beam" target="_blank">carefully</a> <a href="https://www.youtube.com/watch?v=sJFnWZH5FXc" target="_blank"><span title="While you're at it, go watch everything else by Retro Game Mechanics Explained, too.">timing</span></a> the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a <em>lit</em> pixel (<code>#</code>); otherwise, the screen leaves the pixel <em>dark</em> (<code>.</code>).
# MAGIC </p><p>The first few pixels from the larger example above are drawn as follows:</p>
# MAGIC <pre><code>Sprite position: ###.....................................
# MAGIC 
# MAGIC Start cycle   1: begin executing addx 15
# MAGIC During cycle  1: CRT draws pixel in position 0
# MAGIC Current CRT row: #
# MAGIC 
# MAGIC During cycle  2: CRT draws pixel in position 1
# MAGIC Current CRT row: ##
# MAGIC End of cycle  2: finish executing addx 15 (Register X is now 16)
# MAGIC Sprite position: ...............###......................
# MAGIC 
# MAGIC Start cycle   3: begin executing addx -11
# MAGIC During cycle  3: CRT draws pixel in position 2
# MAGIC Current CRT row: ##.
# MAGIC 
# MAGIC During cycle  4: CRT draws pixel in position 3
# MAGIC Current CRT row: ##..
# MAGIC End of cycle  4: finish executing addx -11 (Register X is now 5)
# MAGIC Sprite position: ....###.................................
# MAGIC 
# MAGIC Start cycle   5: begin executing addx 6
# MAGIC During cycle  5: CRT draws pixel in position 4
# MAGIC Current CRT row: ##..#
# MAGIC 
# MAGIC During cycle  6: CRT draws pixel in position 5
# MAGIC Current CRT row: ##..##
# MAGIC End of cycle  6: finish executing addx 6 (Register X is now 11)
# MAGIC Sprite position: ..........###...........................
# MAGIC 
# MAGIC Start cycle   7: begin executing addx -3
# MAGIC During cycle  7: CRT draws pixel in position 6
# MAGIC Current CRT row: ##..##.
# MAGIC 
# MAGIC During cycle  8: CRT draws pixel in position 7
# MAGIC Current CRT row: ##..##..
# MAGIC End of cycle  8: finish executing addx -3 (Register X is now 8)
# MAGIC Sprite position: .......###..............................
# MAGIC 
# MAGIC Start cycle   9: begin executing addx 5
# MAGIC During cycle  9: CRT draws pixel in position 8
# MAGIC Current CRT row: ##..##..#
# MAGIC 
# MAGIC During cycle 10: CRT draws pixel in position 9
# MAGIC Current CRT row: ##..##..##
# MAGIC End of cycle 10: finish executing addx 5 (Register X is now 13)
# MAGIC Sprite position: ............###.........................
# MAGIC 
# MAGIC Start cycle  11: begin executing addx -1
# MAGIC During cycle 11: CRT draws pixel in position 10
# MAGIC Current CRT row: ##..##..##.
# MAGIC 
# MAGIC During cycle 12: CRT draws pixel in position 11
# MAGIC Current CRT row: ##..##..##..
# MAGIC End of cycle 12: finish executing addx -1 (Register X is now 12)
# MAGIC Sprite position: ...........###..........................
# MAGIC 
# MAGIC Start cycle  13: begin executing addx -8
# MAGIC During cycle 13: CRT draws pixel in position 12
# MAGIC Current CRT row: ##..##..##..#
# MAGIC 
# MAGIC During cycle 14: CRT draws pixel in position 13
# MAGIC Current CRT row: ##..##..##..##
# MAGIC End of cycle 14: finish executing addx -8 (Register X is now 4)
# MAGIC Sprite position: ...###..................................
# MAGIC 
# MAGIC Start cycle  15: begin executing addx 13
# MAGIC During cycle 15: CRT draws pixel in position 14
# MAGIC Current CRT row: ##..##..##..##.
# MAGIC 
# MAGIC During cycle 16: CRT draws pixel in position 15
# MAGIC Current CRT row: ##..##..##..##..
# MAGIC End of cycle 16: finish executing addx 13 (Register X is now 17)
# MAGIC Sprite position: ................###.....................
# MAGIC 
# MAGIC Start cycle  17: begin executing addx 4
# MAGIC During cycle 17: CRT draws pixel in position 16
# MAGIC Current CRT row: ##..##..##..##..#
# MAGIC 
# MAGIC During cycle 18: CRT draws pixel in position 17
# MAGIC Current CRT row: ##..##..##..##..##
# MAGIC End of cycle 18: finish executing addx 4 (Register X is now 21)
# MAGIC Sprite position: ....................###.................
# MAGIC 
# MAGIC Start cycle  19: begin executing noop
# MAGIC During cycle 19: CRT draws pixel in position 18
# MAGIC Current CRT row: ##..##..##..##..##.
# MAGIC End of cycle 19: finish executing noop
# MAGIC 
# MAGIC Start cycle  20: begin executing addx -1
# MAGIC During cycle 20: CRT draws pixel in position 19
# MAGIC Current CRT row: ##..##..##..##..##..
# MAGIC 
# MAGIC During cycle 21: CRT draws pixel in position 20
# MAGIC Current CRT row: ##..##..##..##..##..#
# MAGIC End of cycle 21: finish executing addx -1 (Register X is now 20)
# MAGIC Sprite position: ...................###..................
# MAGIC </code></pre>
# MAGIC <p>Allowing the program to run to completion causes the CRT to produce the following image:</p>
# MAGIC <pre><code>##..##..##..##..##..##..##..##..##..##..
# MAGIC ###...###...###...###...###...###...###.
# MAGIC ####....####....####....####....####....
# MAGIC #####.....#####.....#####.....#####.....
# MAGIC ######......######......######......####
# MAGIC #######.......#######.......#######.....
# MAGIC </code></pre>
# MAGIC <p>Render the image given by your program. <em>What eight capital letters appear on your CRT?</em></p>
# MAGIC </article>

# COMMAND ----------

for i, sprite in enumerate(xs):
  pixel_position = i % 40
  if pixel_position == 0:
    print()

  c = '.'
  if sprite - 1 <= pixel_position <= sprite + 1:
    c = '#'
  print(c, end='')

# COMMAND ----------

answer = 'EHPZPJGL'
print(answer)
