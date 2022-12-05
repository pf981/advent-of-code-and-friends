# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/5

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 5: Supply Stacks ---</h2><p>The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked <em>crates</em>, but because the needed supplies are buried under many other crates, the crates need to be rearranged.</p>
# MAGIC <p>The ship has a <em>giant cargo crane</em> capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.</p>
# MAGIC <p>The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her <em>which</em> crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.</p>
# MAGIC <p>They do, however, have a drawing of the starting stacks of crates <em>and</em> the rearrangement procedure (your puzzle input). For example:</p>
# MAGIC <pre><code>    [D]    
# MAGIC [N] [C]    
# MAGIC [Z] [M] [P]
# MAGIC  1   2   3 
# MAGIC 
# MAGIC move 1 from 2 to 1
# MAGIC move 3 from 1 to 3
# MAGIC move 2 from 2 to 1
# MAGIC move 1 from 1 to 2
# MAGIC </code></pre>
# MAGIC <p>In this example, there are three stacks of crates. Stack 1 contains two crates: crate <code>Z</code> is on the bottom, and crate <code>N</code> is on top. Stack 2 contains three crates; from bottom to top, they are crates <code>M</code>, <code>C</code>, and <code>D</code>. Finally, stack 3 contains a single crate, <code>P</code>.</p>
# MAGIC <p>Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:</p>
# MAGIC <pre><code>[D]        
# MAGIC [N] [C]    
# MAGIC [Z] [M] [P]
# MAGIC  1   2   3 
# MAGIC </code></pre>
# MAGIC <p>In the second step, three crates are moved from stack 1 to stack 3. Crates are moved <em>one at a time</em>, so the first crate to be moved (<code>D</code>) ends up below the second and third crates:</p>
# MAGIC <pre><code>        [Z]
# MAGIC         [N]
# MAGIC     [C] [D]
# MAGIC     [M] [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved <em>one at a time</em>, crate <code>C</code> ends up below crate <code>M</code>:</p>
# MAGIC <pre><code>        [Z]
# MAGIC         [N]
# MAGIC [M]     [D]
# MAGIC [C]     [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>Finally, one crate is moved from stack 1 to stack 2:</p>
# MAGIC <pre><code>        [<em>Z</em>]
# MAGIC         [N]
# MAGIC         [D]
# MAGIC [<em>C</em>] [<em>M</em>] [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>The Elves just need to know <em>which crate will end up on top of each stack</em>; in this example, the top crates are <code>C</code> in stack 1, <code>M</code> in stack 2, and <code>Z</code> in stack 3, so you should combine these together and give the Elves the message <code><em>CMZ</em></code>.</p>
# MAGIC <p><em>After the rearrangement procedure completes, what crate ends up on top of each stack?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''            [J] [Z] [G]            
            [Z] [T] [S] [P] [R]    
[R]         [Q] [V] [B] [G] [J]    
[W] [W]     [N] [L] [V] [W] [C]    
[F] [Q]     [T] [G] [C] [T] [T] [W]
[H] [D] [W] [W] [H] [T] [R] [M] [B]
[T] [G] [T] [R] [B] [P] [B] [G] [G]
[S] [S] [B] [D] [F] [L] [Z] [N] [L]
 1   2   3   4   5   6   7   8   9 

move 4 from 2 to 1
move 1 from 6 to 9
move 6 from 4 to 7
move 1 from 2 to 5
move 3 from 6 to 3
move 4 from 3 to 9
move 2 from 1 to 3
move 6 from 7 to 5
move 5 from 7 to 6
move 6 from 8 to 7
move 6 from 7 to 6
move 1 from 8 to 3
move 15 from 6 to 4
move 7 from 5 to 6
move 1 from 7 to 2
move 2 from 5 to 3
move 5 from 9 to 8
move 5 from 5 to 6
move 1 from 7 to 4
move 5 from 6 to 5
move 3 from 3 to 8
move 4 from 5 to 8
move 1 from 2 to 8
move 7 from 1 to 2
move 2 from 6 to 2
move 2 from 5 to 8
move 1 from 1 to 8
move 8 from 2 to 6
move 3 from 3 to 4
move 4 from 9 to 3
move 5 from 3 to 6
move 5 from 6 to 8
move 3 from 4 to 8
move 13 from 6 to 5
move 14 from 4 to 8
move 1 from 2 to 6
move 1 from 4 to 2
move 12 from 5 to 4
move 30 from 8 to 6
move 1 from 8 to 9
move 1 from 9 to 4
move 15 from 4 to 5
move 1 from 2 to 9
move 1 from 4 to 2
move 1 from 2 to 1
move 1 from 9 to 3
move 8 from 5 to 7
move 2 from 5 to 6
move 7 from 8 to 1
move 1 from 3 to 4
move 1 from 7 to 3
move 1 from 4 to 6
move 26 from 6 to 7
move 1 from 3 to 7
move 3 from 7 to 2
move 1 from 1 to 9
move 16 from 7 to 5
move 2 from 7 to 4
move 12 from 7 to 6
move 1 from 1 to 9
move 4 from 6 to 1
move 7 from 1 to 5
move 2 from 1 to 8
move 1 from 7 to 2
move 1 from 1 to 4
move 2 from 4 to 5
move 1 from 9 to 4
move 3 from 6 to 9
move 8 from 6 to 5
move 5 from 5 to 9
move 19 from 5 to 8
move 1 from 9 to 8
move 3 from 8 to 7
move 1 from 7 to 3
move 8 from 5 to 2
move 2 from 4 to 2
move 4 from 9 to 8
move 1 from 2 to 3
move 2 from 3 to 2
move 4 from 9 to 5
move 8 from 8 to 4
move 9 from 8 to 5
move 5 from 8 to 4
move 5 from 5 to 7
move 12 from 2 to 3
move 2 from 2 to 8
move 1 from 8 to 6
move 1 from 8 to 7
move 10 from 4 to 3
move 1 from 2 to 9
move 13 from 5 to 3
move 1 from 7 to 5
move 27 from 3 to 4
move 1 from 8 to 7
move 3 from 5 to 2
move 6 from 6 to 3
move 2 from 4 to 1
move 27 from 4 to 2
move 2 from 7 to 8
move 23 from 2 to 4
move 2 from 1 to 4
move 2 from 7 to 2
move 4 from 2 to 9
move 10 from 3 to 4
move 1 from 3 to 5
move 1 from 5 to 1
move 5 from 2 to 5
move 30 from 4 to 2
move 1 from 8 to 9
move 1 from 8 to 1
move 27 from 2 to 3
move 2 from 4 to 2
move 1 from 9 to 4
move 2 from 1 to 3
move 8 from 3 to 7
move 19 from 3 to 1
move 1 from 4 to 7
move 5 from 9 to 1
move 4 from 2 to 9
move 4 from 3 to 4
move 1 from 3 to 5
move 1 from 2 to 7
move 1 from 9 to 3
move 1 from 9 to 1
move 5 from 5 to 4
move 5 from 7 to 3
move 1 from 5 to 6
move 23 from 1 to 6
move 1 from 9 to 2
move 1 from 2 to 5
move 24 from 6 to 9
move 6 from 4 to 7
move 4 from 4 to 8
move 1 from 4 to 9
move 4 from 7 to 4
move 4 from 3 to 4
move 4 from 9 to 8
move 6 from 7 to 9
move 4 from 7 to 6
move 1 from 1 to 4
move 2 from 6 to 4
move 1 from 6 to 2
move 1 from 1 to 8
move 1 from 7 to 3
move 1 from 6 to 9
move 13 from 4 to 2
move 3 from 3 to 2
move 15 from 9 to 8
move 1 from 5 to 9
move 5 from 9 to 1
move 4 from 1 to 7
move 4 from 7 to 3
move 8 from 2 to 7
move 9 from 8 to 2
move 1 from 1 to 2
move 7 from 9 to 2
move 4 from 3 to 1
move 4 from 1 to 4
move 2 from 9 to 1
move 20 from 2 to 8
move 3 from 4 to 8
move 1 from 2 to 3
move 4 from 2 to 7
move 1 from 3 to 4
move 1 from 9 to 3
move 1 from 4 to 7
move 1 from 2 to 5
move 1 from 4 to 3
move 2 from 1 to 6
move 1 from 5 to 6
move 1 from 7 to 1
move 12 from 7 to 2
move 12 from 2 to 6
move 9 from 6 to 2
move 1 from 6 to 8
move 1 from 3 to 9
move 8 from 2 to 4
move 1 from 9 to 6
move 1 from 4 to 6
move 4 from 4 to 9
move 1 from 4 to 9
move 1 from 1 to 5
move 2 from 6 to 3
move 1 from 5 to 4
move 1 from 2 to 8
move 10 from 8 to 6
move 10 from 8 to 3
move 1 from 3 to 4
move 8 from 8 to 1
move 3 from 9 to 8
move 2 from 9 to 1
move 11 from 6 to 7
move 1 from 1 to 7
move 8 from 1 to 4
move 3 from 6 to 7
move 1 from 1 to 4
move 14 from 8 to 6
move 1 from 8 to 7
move 1 from 6 to 8
move 6 from 4 to 1
move 1 from 8 to 5
move 4 from 1 to 8
move 2 from 7 to 1
move 1 from 6 to 7
move 5 from 4 to 2
move 2 from 4 to 3
move 4 from 2 to 8
move 15 from 7 to 3
move 3 from 3 to 6
move 1 from 5 to 2
move 21 from 3 to 6
move 2 from 8 to 7
move 1 from 7 to 8
move 32 from 6 to 9
move 1 from 7 to 8
move 5 from 8 to 4
move 2 from 8 to 7
move 14 from 9 to 8
move 14 from 8 to 1
move 2 from 6 to 1
move 2 from 7 to 4
move 1 from 9 to 3
move 17 from 9 to 5
move 6 from 1 to 8
move 4 from 4 to 6
move 2 from 2 to 5
move 2 from 8 to 2
move 1 from 6 to 7
move 2 from 2 to 6
move 4 from 3 to 2
move 7 from 6 to 3
move 6 from 5 to 7
move 1 from 8 to 9
move 1 from 6 to 7
move 4 from 8 to 6
move 1 from 9 to 3
move 4 from 1 to 4
move 12 from 5 to 9
move 7 from 7 to 8
move 3 from 4 to 2
move 8 from 9 to 4
move 2 from 6 to 2
move 1 from 7 to 4
move 2 from 6 to 9
move 1 from 5 to 3
move 1 from 8 to 1
move 2 from 8 to 7
move 2 from 2 to 9
move 7 from 2 to 3
move 8 from 4 to 1
move 2 from 8 to 4
move 4 from 9 to 7
move 2 from 9 to 5
move 16 from 1 to 3
move 3 from 7 to 4
move 1 from 7 to 6
move 1 from 6 to 2
move 2 from 5 to 3
move 10 from 4 to 2
move 2 from 8 to 7
move 19 from 3 to 8
move 17 from 3 to 9
move 3 from 1 to 7
move 17 from 9 to 2
move 1 from 7 to 5
move 1 from 7 to 5
move 2 from 5 to 7
move 2 from 9 to 2
move 6 from 7 to 6
move 3 from 6 to 7
move 1 from 8 to 9
move 1 from 9 to 3
move 4 from 2 to 5
move 17 from 2 to 3
move 3 from 7 to 5
move 1 from 5 to 3
move 7 from 2 to 3
move 2 from 2 to 4
move 1 from 7 to 1
move 1 from 1 to 5
move 2 from 5 to 3
move 1 from 4 to 5
move 1 from 4 to 3
move 14 from 3 to 5
move 17 from 8 to 7
move 2 from 6 to 2
move 12 from 3 to 5
move 15 from 5 to 9
move 7 from 7 to 3
move 7 from 7 to 6
move 1 from 2 to 3
move 11 from 9 to 6
move 13 from 5 to 7
move 10 from 6 to 8
move 6 from 8 to 3
move 2 from 5 to 8
move 1 from 2 to 9
move 10 from 7 to 6
move 9 from 6 to 8
move 1 from 5 to 1
move 10 from 6 to 4
move 8 from 4 to 5
move 1 from 1 to 2
move 3 from 9 to 1
move 10 from 3 to 7
move 1 from 4 to 7
move 12 from 7 to 9
move 7 from 3 to 5
move 13 from 8 to 7
move 3 from 9 to 5
move 5 from 5 to 6
move 3 from 1 to 9
move 5 from 9 to 6
move 10 from 6 to 4
move 15 from 7 to 5
move 3 from 9 to 4
move 1 from 4 to 3
move 3 from 8 to 9
move 6 from 9 to 6
move 2 from 5 to 1
move 1 from 2 to 7
move 12 from 5 to 8
move 3 from 9 to 5
move 11 from 5 to 6
move 1 from 1 to 2
move 1 from 2 to 8
move 3 from 7 to 8
move 10 from 8 to 3
move 1 from 1 to 7
move 10 from 4 to 9
move 1 from 7 to 8
move 5 from 5 to 3
move 15 from 6 to 5
move 8 from 3 to 9
move 3 from 4 to 5
move 1 from 7 to 8
move 8 from 8 to 9
move 1 from 6 to 5
move 5 from 3 to 2
move 5 from 2 to 3
move 5 from 9 to 8
move 1 from 6 to 8
move 2 from 5 to 1
move 4 from 3 to 2
move 16 from 5 to 6
move 3 from 5 to 9
move 4 from 8 to 5
move 8 from 6 to 4
move 4 from 2 to 3
move 1 from 1 to 4
move 6 from 3 to 6
move 24 from 9 to 2
move 1 from 1 to 9
move 1 from 9 to 4
move 2 from 4 to 5
move 1 from 3 to 2
move 10 from 6 to 8
move 22 from 2 to 6
move 1 from 2 to 7
move 1 from 7 to 5
move 10 from 8 to 9
move 7 from 9 to 3
move 6 from 4 to 8
move 3 from 9 to 2
move 5 from 8 to 3
move 1 from 4 to 1
move 1 from 8 to 3
move 3 from 6 to 2
move 5 from 5 to 1
move 1 from 5 to 3
move 5 from 6 to 3
move 1 from 2 to 7
move 16 from 3 to 2
move 1 from 8 to 1
move 1 from 4 to 7
move 1 from 5 to 3
move 6 from 6 to 4
move 14 from 2 to 8
move 3 from 3 to 5
move 2 from 3 to 6
move 3 from 5 to 6
move 4 from 6 to 4
move 3 from 4 to 8
move 7 from 2 to 9
move 2 from 2 to 1
move 9 from 8 to 4
move 7 from 1 to 7
move 8 from 7 to 5
move 2 from 8 to 4
move 3 from 9 to 6
move 4 from 4 to 6
move 1 from 7 to 3
move 4 from 8 to 2
move 2 from 9 to 8
move 9 from 6 to 7
move 1 from 9 to 8
move 1 from 1 to 5
move 3 from 4 to 5
move 1 from 3 to 2
move 5 from 8 to 2
move 9 from 2 to 7
move 1 from 6 to 7
move 1 from 6 to 2
move 9 from 7 to 4
move 2 from 5 to 9
move 10 from 4 to 6
move 1 from 8 to 6
move 5 from 4 to 3
move 5 from 4 to 9
move 5 from 9 to 5
move 1 from 1 to 7
move 4 from 7 to 8
move 8 from 5 to 3
move 3 from 3 to 8
move 6 from 7 to 6
move 3 from 3 to 1
move 5 from 3 to 7
move 1 from 9 to 6
move 2 from 7 to 6
move 1 from 9 to 3
move 4 from 6 to 9
move 2 from 2 to 6
move 1 from 7 to 3
move 6 from 5 to 4
move 7 from 6 to 9
move 6 from 6 to 8
move 2 from 1 to 2
move 1 from 5 to 1
move 5 from 8 to 5
move 1 from 3 to 9
move 4 from 4 to 5
move 10 from 9 to 2
move 14 from 6 to 4
move 1 from 3 to 8
move 1 from 8 to 5
move 2 from 7 to 9
move 1 from 1 to 2
move 14 from 4 to 7
move 1 from 1 to 4
move 3 from 4 to 1
move 3 from 5 to 1
move 6 from 5 to 1
move 10 from 7 to 3
move 6 from 1 to 5
move 6 from 1 to 7
move 3 from 8 to 3
move 1 from 5 to 1
move 3 from 9 to 6
move 1 from 9 to 3
move 6 from 5 to 9
move 2 from 6 to 1
move 9 from 2 to 1
move 6 from 9 to 6
move 2 from 8 to 7
move 5 from 7 to 3
move 7 from 7 to 5
move 4 from 2 to 8
move 6 from 8 to 3
move 1 from 9 to 4
move 1 from 7 to 3
move 2 from 5 to 3
move 7 from 6 to 4
move 28 from 3 to 4
move 1 from 3 to 8
move 1 from 5 to 9
move 9 from 4 to 5
move 12 from 4 to 5
move 2 from 4 to 6
move 5 from 4 to 6
move 1 from 3 to 8
move 10 from 5 to 8
move 10 from 5 to 4
move 5 from 5 to 9
move 3 from 4 to 1
move 5 from 6 to 9
move 2 from 6 to 7
move 2 from 7 to 5
move 10 from 9 to 4
move 1 from 8 to 5
move 5 from 1 to 5
move 8 from 8 to 7
move 8 from 5 to 3
move 8 from 7 to 8
move 2 from 8 to 2
move 7 from 3 to 2
move 21 from 4 to 7
move 10 from 1 to 9
move 3 from 4 to 5
move 1 from 4 to 8
move 1 from 8 to 3
move 7 from 8 to 5
move 2 from 3 to 1
move 7 from 7 to 2
move 1 from 1 to 4
move 1 from 1 to 6
move 8 from 9 to 3
move 2 from 8 to 4
move 3 from 3 to 1
move 3 from 4 to 7
move 1 from 6 to 7
move 5 from 2 to 4
move 2 from 1 to 6'''

# COMMAND ----------

import copy
import re

stack_lines, moves = inp.split('\n\n')

moves = [[int(x) for x in re.findall(r'\d+', line)] for line in moves.splitlines()]

*stack_lines, last = stack_lines.splitlines()
n_stacks = int(last.rstrip(' ').split(' ')[-1])
stacks = [[] for _ in range(n_stacks)]

for s in stack_lines:
  for i_stack, i in enumerate(range(0, len(s), 4)):
    c = s[i+1]
    if c != ' ':
      stacks[i_stack].insert(0, c)

cur_stacks = copy.deepcopy(stacks)
for n, move_from, move_to in moves:
  move_from -= 1
  move_to -= 1
  for _ in range(n):
    cur_stacks[move_to].append(cur_stacks[move_from].pop())

answer = ''.join(stack[-1] for stack in cur_stacks)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.</p>
# MAGIC <p>Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a <em><span title="It's way better than the old CrateMover 1006.">CrateMover 9001</span></em>.</p>
# MAGIC <p>The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and <em>the ability to pick up and move multiple crates at once</em>.</p>
# MAGIC <p>Again considering the example above, the crates begin in the same configuration:</p>
# MAGIC <pre><code>    [D]    
# MAGIC [N] [C]    
# MAGIC [Z] [M] [P]
# MAGIC  1   2   3 
# MAGIC </code></pre>
# MAGIC <p>Moving a single crate from stack 2 to stack 1 behaves the same as before:</p>
# MAGIC <pre><code>[D]        
# MAGIC [N] [C]    
# MAGIC [Z] [M] [P]
# MAGIC  1   2   3 
# MAGIC </code></pre>
# MAGIC <p>However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates <em>stay in the same order</em>, resulting in this new configuration:</p>
# MAGIC <pre><code>        [D]
# MAGIC         [N]
# MAGIC     [C] [Z]
# MAGIC     [M] [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>Next, as both crates are moved from stack 2 to stack 1, they <em>retain their order</em> as well:</p>
# MAGIC <pre><code>        [D]
# MAGIC         [N]
# MAGIC [C]     [Z]
# MAGIC [M]     [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate <code>C</code> that gets moved:</p>
# MAGIC <pre><code>        [<em>D</em>]
# MAGIC         [N]
# MAGIC         [Z]
# MAGIC [<em>M</em>] [<em>C</em>] [P]
# MAGIC  1   2   3
# MAGIC </code></pre>
# MAGIC <p>In this example, the CrateMover 9001 has put the crates in a totally different order: <code><em>MCD</em></code>.</p>
# MAGIC <p>Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. <em>After the rearrangement procedure completes, what crate ends up on top of each stack?</em></p>
# MAGIC </article>

# COMMAND ----------

cur_stacks = copy.deepcopy(stacks)
for n, move_from, move_to in moves:
  move_from -= 1
  move_to -= 1
  moved = []
  for _ in range(n):
    moved.append(cur_stacks[move_from].pop())
  cur_stacks[move_to].extend(moved[::-1])

answer = ''.join(stack[-1] for stack in cur_stacks)
print(answer)
