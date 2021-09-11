# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/19

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 19: An Elephant Named Joseph ---</h2><p>The Elves contact you over a highly secure emergency channel. Back at the North Pole, the Elves are busy <span title="Eggnoggedly misunderstanding them, actually.">misunderstanding</span> <a href="https://en.wikipedia.org/wiki/White_elephant_gift_exchange">White Elephant parties</a>.</p>
# MAGIC <p>Each Elf brings a present. They all sit in a circle, numbered starting with position <code>1</code>. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left.  An Elf with no presents is removed from the circle and does not take turns.</p>
# MAGIC <p>For example, with five Elves (numbered <code>1</code> to <code>5</code>):</p>
# MAGIC <pre><code>  1
# MAGIC 5   2
# MAGIC  4 3
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Elf <code>1</code> takes Elf <code>2</code>'s present.</li>
# MAGIC <li>Elf <code>2</code> has no presents and is skipped.</li>
# MAGIC <li>Elf <code>3</code> takes Elf <code>4</code>'s present.</li>
# MAGIC <li>Elf <code>4</code> has no presents and is also skipped.</li>
# MAGIC <li>Elf <code>5</code> takes Elf <code>1</code>'s two presents.</li>
# MAGIC <li>Neither Elf <code>1</code> nor Elf <code>2</code> have any presents, so both are skipped.</li>
# MAGIC <li>Elf <code>3</code> takes Elf <code>5</code>'s three presents.</li>
# MAGIC </ul>
# MAGIC <p>So, with <em>five</em> Elves, the Elf that sits starting in position <code>3</code> gets all the presents.</p>
# MAGIC <p>With the number of Elves given in your puzzle input, <em>which Elf gets all the presents?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = 3014603

# COMMAND ----------

import collections

def solve(n_elves):
  elves = collections.deque(range(n_elves))
  
  while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()

  return elves.pop() + 1

answer = solve(inp)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Realizing the folly of their present-exchange rules, the Elves agree to instead steal presents from the Elf <em>directly across the circle</em>. If two Elves are across the circle, the one on the left (from the perspective of the stealer) is stolen from.  The other rules remain unchanged: Elves with no presents are removed from the circle entirely, and the other elves move in slightly to keep the circle evenly spaced.</p>
# MAGIC <p>For example, with five Elves (again numbered <code>1</code> to <code>5</code>):</p>
# MAGIC <ul>
# MAGIC <li>The Elves sit in a circle; Elf <code>1</code> goes first:
# MAGIC <pre><code>  <em>1</em>
# MAGIC 5   2
# MAGIC  4 3
# MAGIC </code></pre></li>
# MAGIC <li>Elves <code>3</code> and <code>4</code> are across the circle; Elf <code>3</code>'s present is stolen, being the one to the left. Elf <code>3</code> leaves the circle, and the rest of the Elves move in:
# MAGIC <pre><code>  <em>1</em>           1
# MAGIC 5   2  --&gt;  5   2
# MAGIC  4 -          4
# MAGIC </code></pre></li>
# MAGIC <li>Elf <code>2</code> steals from the Elf directly across the circle, Elf <code>5</code>:
# MAGIC <pre><code>  1         1 
# MAGIC -   <em>2</em>  --&gt;     2
# MAGIC   4         4 
# MAGIC </code></pre></li>
# MAGIC <li>Next is Elf <code>4</code> who, choosing between Elves <code>1</code> and <code>2</code>, steals from Elf <code>1</code>:
# MAGIC <pre><code> -          2  
# MAGIC     2  --&gt;
# MAGIC  <em>4</em>          4
# MAGIC </code></pre></li>
# MAGIC <li>Finally, Elf <code>2</code> steals from Elf <code>4</code>:
# MAGIC <pre><code> <em>2</em>
# MAGIC     --&gt;  2  
# MAGIC  -
# MAGIC </code></pre></li>
# MAGIC </ul>
# MAGIC <p>So, with <em>five</em> Elves, the Elf that sits starting in position <code>2</code> gets all the presents.</p>
# MAGIC <p>With the number of Elves given in your puzzle input, <em>which Elf now gets all the presents?</em></p>
# MAGIC </article>

# COMMAND ----------

def solve2(n_elves):
  left = collections.deque(range(n_elves // 2))
  right = collections.deque(reversed(range(n_elves // 2, n_elves)))

  while left and right:
    (left if len(left) > len(right) else right).pop()
    right.appendleft(left.popleft())
    left.append(right.pop())
  
  return (left or right).pop() + 1

answer = solve2(inp)
answer
