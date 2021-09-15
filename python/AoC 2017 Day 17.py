# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: Spinlock ---</h2><p>Suddenly, whirling in the distance, you notice what looks like a massive, <span title="You know, as opposed to all those non-pixelated hurricanes you see on TV.">pixelated hurricane</span>: a deadly <a href="https://en.wikipedia.org/wiki/Spinlock">spinlock</a>. This spinlock isn't just consuming computing power, but memory, too; vast, digital mountains are being ripped from the ground and consumed by the vortex.</p>
# MAGIC <p>If you don't move quickly, fixing that printer will be the least of your problems.</p>
# MAGIC <p>This spinlock's algorithm is simple but efficient, quickly consuming everything in its path. It starts with a circular buffer containing only the value <code>0</code>, which it marks as the <em>current position</em>. It then steps forward through the circular buffer some number of steps (your puzzle input) before inserting the first new value, <code>1</code>, after the value it stopped on.  The inserted value becomes the <em>current position</em>. Then, it steps forward from there the same number of steps, and wherever it stops, inserts after it the second new value, <code>2</code>, and uses that as the new <em>current position</em> again.</p>
# MAGIC <p>It repeats this process of <em>stepping forward</em>, <em>inserting a new value</em>, and <em>using the location of the inserted value as the new current position</em> a total of <code><em>2017</em></code> times, inserting <code>2017</code> as its final operation, and ending with a total of <code>2018</code> values (including <code>0</code>) in the circular buffer.</p>
# MAGIC <p>For example, if the spinlock were to step <code>3</code> times per insert, the circular buffer would begin to evolve like this (using parentheses to mark the current position after each iteration of the algorithm):</p>
# MAGIC <ul>
# MAGIC <li><code>(0)</code>, the initial state before any insertions.</li>
# MAGIC <li><code>0&nbsp;(1)</code>: the spinlock steps forward three times (<code>0</code>, <code>0</code>, <code>0</code>), and then inserts the first value, <code>1</code>, after it. <code>1</code> becomes the current position.</li>
# MAGIC <li><code>0&nbsp;(2)&nbsp;1</code>: the spinlock steps forward three times (<code>0</code>, <code>1</code>, <code>0</code>), and then inserts the second value, <code>2</code>, after it. <code>2</code> becomes the current position.</li>
# MAGIC <li><code>0&nbsp;&nbsp;2&nbsp;(3)&nbsp;1</code>: the spinlock steps forward three times (<code>1</code>, <code>0</code>, <code>2</code>), and then inserts the third value, <code>3</code>, after it. <code>3</code> becomes the current position.</li>
# MAGIC </ul>
# MAGIC <p>And so on:</p>
# MAGIC <ul>
# MAGIC <li><code>0&nbsp;&nbsp;2&nbsp;(4)&nbsp;3&nbsp;&nbsp;1</code></li>
# MAGIC <li><code>0&nbsp;(5)&nbsp;2&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;&nbsp;1</code></li>
# MAGIC <li><code>0&nbsp;&nbsp;5&nbsp;&nbsp;2&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;(6)&nbsp;1</code></li>
# MAGIC <li><code>0&nbsp;&nbsp;5&nbsp;(7)&nbsp;2&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;&nbsp;6&nbsp;&nbsp;1</code></li>
# MAGIC <li><code>0&nbsp;&nbsp;5&nbsp;&nbsp;7&nbsp;&nbsp;2&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;(8)&nbsp;6&nbsp;&nbsp;1</code></li>
# MAGIC <li><code>0&nbsp;(9)&nbsp;5&nbsp;&nbsp;7&nbsp;&nbsp;2&nbsp;&nbsp;4&nbsp;&nbsp;3&nbsp;&nbsp;8&nbsp;&nbsp;6&nbsp;&nbsp;1</code></li>
# MAGIC </ul>
# MAGIC <p>Eventually, after 2017 insertions, the section of the circular buffer near the last insertion looks like this:</p>
# MAGIC <pre><code>1512  1134  151 (2017) 638  1513  851</code></pre>
# MAGIC <p>Perhaps, if you can identify the value that will ultimately be <em>after</em> the last value written (<code>2017</code>), you can short-circuit the spinlock.  In this example, that would be <code>638</code>.</p>
# MAGIC <p><em>What is the value after <code>2017</code></em> in your completed circular buffer?</p>
# MAGIC </article>

# COMMAND ----------

inp = 348

# COMMAND ----------

import collections

def solve(skip):
  buffer = collections.deque()
  
  for i in range(2018):
    buffer.rotate(-skip)
    buffer.appendleft(i)
    buffer.rotate(-1)
  
  return buffer[0]

answer = solve(inp)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The spinlock does not short-circuit.  Instead, it gets <em>more</em> angry. At least, you assume that's what happened; it's spinning significantly faster than it was a moment ago.</p>
# MAGIC <p>You have good news and bad news.</p>
# MAGIC <p>The good news is that you have improved calculations for how to stop the spinlock. They indicate that you actually need to identify <em>the value after <code>0</code></em> in the current state of the circular buffer.</p>
# MAGIC <p>The bad news is that while you were determining this, the spinlock has just finished inserting its fifty millionth value (<code>50000000</code>).</p>
# MAGIC <p><em>What is the value after <code>0</code></em> the moment <code>50000000</code> is inserted?</p>
# MAGIC </article>

# COMMAND ----------

def solve2(skip):
  buffer_size = 1
  i = 0
  for iteration in range(50000000):
    i = ((i + skip) % buffer_size) + 1
    buffer_size += 1
    if (i == 1):
      result = iteration + 1
  return result

answer = solve2(inp)
print(answer)
