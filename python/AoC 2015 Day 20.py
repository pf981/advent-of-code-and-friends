# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/20

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 20: Infinite Elves and Infinite Houses ---</h2><p>To keep the Elves busy, Santa has them deliver some presents <span title="This was before the Elves unionized, apparently.">by hand, door-to-door</span>.  He sends them down a street with infinite houses numbered sequentially: <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, and so on.</p>
# MAGIC <p>Each Elf is assigned a number, too, and delivers presents to houses based on that number:</p>
# MAGIC <ul>
# MAGIC <li>The first Elf (number <code>1</code>) delivers presents to every house: <code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, ....</li>
# MAGIC <li>The second Elf (number <code>2</code>) delivers presents to every second house: <code>2</code>, <code>4</code>, <code>6</code>, <code>8</code>, <code>10</code>, ....</li>
# MAGIC <li>Elf number <code>3</code> delivers presents to every third house: <code>3</code>, <code>6</code>, <code>9</code>, <code>12</code>, <code>15</code>, ....</li>
# MAGIC </ul>
# MAGIC <p>There are infinitely many Elves, numbered starting with <code>1</code>.  Each Elf delivers presents equal to <em>ten times</em> his or her number at each house.</p>
# MAGIC <p>So, the first nine houses on the street end up like this:</p>
# MAGIC <pre><code>House 1 got 10 presents.
# MAGIC House 2 got 30 presents.
# MAGIC House 3 got 40 presents.
# MAGIC House 4 got 70 presents.
# MAGIC House 5 got 60 presents.
# MAGIC House 6 got 120 presents.
# MAGIC House 7 got 80 presents.
# MAGIC House 8 got 150 presents.
# MAGIC House 9 got 130 presents.
# MAGIC </code></pre>
# MAGIC <p>The first house gets <code>10</code> presents: it is visited only by Elf <code>1</code>, which delivers <code>1 * 10 = 10</code> presents.  The fourth house gets <code>70</code> presents, because it is visited by Elves <code>1</code>, <code>2</code>, and <code>4</code>, for a total of <code>10 + 20 + 40 = 70</code> presents.</p>
# MAGIC <p>What is the <em>lowest house number</em> of the house to get at least as many presents as the number in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

inp = 34000000

# COMMAND ----------

presents = [0] * (inp // 10)

for elf in range(1, len(presents)+1):
  for i in range(elf, len(presents)+1, elf):
    presents[i-1] += elf * 10

answer = next(i for i, x in enumerate(presents, 1) if x >= inp)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Elves decide they don't want to visit an infinite number of houses.  Instead, each Elf will stop after delivering presents to <code>50</code> houses.  To make up for it, they decide to deliver presents equal to <em>eleven times</em> their number at each house.</p>
# MAGIC <p>With these changes, what is the new <em>lowest house number</em> of the house to get at least as many presents as the number in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

presents = [0] * (inp // 10)

for elf in range(1, len(presents)+1):
  for i in range(elf, min(50 * elf, len(presents)) + 1, elf):
    presents[i-1] += elf * 11

answer = next(i for i, x in enumerate(presents, 1) if x >= inp)
answer
