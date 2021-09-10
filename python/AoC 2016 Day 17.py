# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: Two Steps Forward ---</h2><p>You're trying to access a secure vault protected by a <code>4x4</code> grid of small rooms connected by doors. You start in the top-left room (marked <code>S</code>), and you can access the vault (marked <code>V</code>) once you reach the bottom-right room:</p>
# MAGIC <pre><code>#########
# MAGIC #S| | | #
# MAGIC #-#-#-#-#
# MAGIC # | | | #
# MAGIC #-#-#-#-#
# MAGIC # | | | #
# MAGIC #-#-#-#-#
# MAGIC # | | |  
# MAGIC ####### V
# MAGIC </code></pre>
# MAGIC <p>Fixed walls are marked with <code>#</code>, and doors are marked with <code>-</code> or <code>|</code>.</p>
# MAGIC <p>The doors in your <em>current room</em> are either open or closed (and locked) based on the hexadecimal <a href="https://en.wikipedia.org/wiki/MD5">MD5</a> hash of a passcode (your puzzle input) followed by a sequence of uppercase characters representing the <em>path you have taken so far</em> (<code>U</code> for up, <code>D</code> for down, <code>L</code> for left, and <code>R</code> for right).</p>
# MAGIC <p>Only the first four characters of the hash are used; they represent, respectively, the doors <em>up, down, left, and right</em> from your current position. Any <code>b</code>, <code>c</code>, <code>d</code>, <code>e</code>, or <code>f</code> means that the corresponding door is <em>open</em>; any other character (any number or <code>a</code>) means that the corresponding door is <em>closed and locked</em>.</p>
# MAGIC <p>To access the vault, all you need to do is reach the bottom-right room; reaching this room opens the vault and all doors in the maze.</p>
# MAGIC <p>For example, suppose the passcode is <code>hijkl</code>. Initially, you have taken no steps, and so your path is empty: you simply find the MD5 hash of <code>hijkl</code> alone. The first four characters of this hash are <code>ced9</code>, which indicate that up is open (<code>c</code>), down is open (<code>e</code>), left is open (<code>d</code>), and right is closed and locked (<code>9</code>). Because you start in the top-left corner, there are no "up" or "left" doors to be open, so your only choice is <em>down</em>.</p>
# MAGIC <p>Next, having gone only one step (down, or <code>D</code>), you find the hash of <code>hijkl<em>D</em></code>. This produces <code>f2bc</code>, which indicates that you can go back up, left (but that's a wall), or right. Going right means hashing <code>hijkl<em>DR</em></code> to get <code>5745</code> - all doors closed and locked. However, going <em>up</em> instead is worthwhile: even though it returns you to the room you started in, your path would then be <code>DU</code>, opening a <em>different set of doors</em>.</p>
# MAGIC <p>After going <code>DU</code> (and then hashing <code>hijkl<em>DU</em></code> to get <code>528e</code>), only the right door is open; after going <code>DUR</code>, all doors lock. (Fortunately, your actual passcode is <span title="It took four days to rescue the engineer that tried this.">not <code>hijkl</code></span>).</p>
# MAGIC <p>Passcodes actually used by Easter Bunny Vault Security do allow access to the vault if you know the right path.  For example:</p>
# MAGIC <ul>
# MAGIC <li>If your passcode were <code>ihgpwlah</code>, the shortest path would be <code>DDRRRD</code>.</li>
# MAGIC <li>With <code>kglvqrro</code>, the shortest path would be <code>DDUDRLRRUDRD</code>.</li>
# MAGIC <li>With <code>ulqzkmiv</code>, the shortest would be <code>DRURDRUDDLLDLUURRDULRLDUUDDDRR</code>.</li>
# MAGIC </ul>
# MAGIC <p>Given your vault's passcode, <em>what is the shortest path</em> (the actual path, not just the length) to reach the vault?</p>
# MAGIC </article>

# COMMAND ----------

inp = 'awrkjxxr'

# COMMAND ----------

import hashlib
import heapq

def solve(passcode):
  states = [(0, 0, 0, '')]
  while states:
    d, row, col, path = heapq.heappop(states)

    for direction, is_open in enumerate(x in 'bcedf' for x in hashlib.md5((passcode + path).encode()).hexdigest()[:4]):
      if not is_open:
        continue
      new_row = row + (direction == 1) - (direction == 0)
      new_col = col + (direction == 3) - (direction == 2)
      new_path = path + ['U', 'D', 'L', 'R'][direction]
      
      if new_row < 0 or new_col < 0 or new_row > 3 or new_col > 3:
        continue
      
      if new_row == 3 and new_col == 3:
        return new_path

      heapq.heappush(states, (d + 1, new_row, new_col, new_path))

answer = solve(inp)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You're curious how robust this security solution really is, and so you decide to find longer and longer paths which still provide access to the vault. You remember that paths always end the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>If your passcode were <code>ihgpwlah</code>, the longest path would take <code>370</code> steps.</li>
# MAGIC <li>With <code>kglvqrro</code>, the longest path would be <code>492</code> steps long.</li>
# MAGIC <li>With <code>ulqzkmiv</code>, the longest path would be <code>830</code> steps long.</li>
# MAGIC </ul>
# MAGIC <p></p>
# MAGIC <p>What is the <em>length of the longest path</em> that reaches the vault?</p>
# MAGIC </article>

# COMMAND ----------

def longest_path(row, col, s):
  if row == 3 and col == 3:
    return 0
  
  longest = float('-inf')
  for direction, is_open in enumerate(x in 'bcedf' for x in hashlib.md5(s.encode()).hexdigest()[:4]):
    if not is_open:
      continue
    new_row = row + (direction == 1) - (direction == 0)
    new_col = col + (direction == 3) - (direction == 2)
    new_s = s + ['U', 'D', 'L', 'R'][direction]

    if new_row < 0 or new_col < 0 or new_row > 3 or new_col > 3:
      continue
    longest = max(longest, 1 + longest_path(new_row, new_col, new_s))
  return longest

answer = longest_path(0, 0, inp)
answer
