# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: No Such Thing as Too Much ---</h2><p>The elves bought too much eggnog again - <code>150</code> liters this time.  To fit it all into your refrigerator, you'll need to move it into smaller containers.  You take an inventory of the capacities of the available containers.</p>
# MAGIC <p>For example, suppose you have containers of size <code>20</code>, <code>15</code>, <code>10</code>, <code>5</code>, and <code>5</code> liters.  If you need to store <code>25</code> liters, there are four ways to do it:</p>
# MAGIC <ul>
# MAGIC <li><code>15</code> and <code>10</code></li>
# MAGIC <li><code>20</code> and <code>5</code> (the first <code>5</code>)</li>
# MAGIC <li><code>20</code> and <code>5</code> (the second <code>5</code>)</li>
# MAGIC <li><code>15</code>, <code>5</code>, and <code>5</code></li>
# MAGIC </ul>
# MAGIC <p>Filling all containers entirely, how many different <em>combinations of containers</em> can exactly fit all <code>150</code> liters of eggnog?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38'''

# COMMAND ----------

from collections import defaultdict

ways_to_fill = defaultdict(int)

def compute_ways_to_fill(items, capacity, n_containers = 0):
  if capacity == 0:
    ways_to_fill[n_containers] += 1
    return
  if capacity < 0:
    return
  
  remaining_items = items.copy()
  for item in items:
    remaining_items.remove(item)
    compute_ways_to_fill(remaining_items, capacity - item, n_containers + 1)

compute_ways_to_fill([int(x) for x in inp.split('\n')], 150)

# COMMAND ----------

answer = sum(ways_to_fill.values())
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>While playing with all the containers in the kitchen, another load of eggnog <span title="Apparently, Amazon ships to the North Pole now.">arrives</span>!  The shipping and receiving department is requesting as many containers as you can spare.</p>
# MAGIC <p>Find the minimum number of containers that can exactly fit all <code>150</code> liters of eggnog.  <em>How many different ways</em> can you fill that number of containers and still hold exactly <code>150</code> litres?</p>
# MAGIC <p>In the example above, the minimum number of containers was two.  There were three ways to use that many containers, and so the answer there would be <code>3</code>.</p>
# MAGIC <p></p>
# MAGIC </article>

# COMMAND ----------

answer = ways_to_fill[min(ways_to_fill.keys())]
answer
