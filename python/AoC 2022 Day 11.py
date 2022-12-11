# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/11

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 11: Monkey in the Middle ---</h2><p>As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing <a href="https://en.wikipedia.org/wiki/Keep_away" target="_blank">Keep Away</a> with your missing things!</p>
# MAGIC <p>To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on <em>how worried you are about each item</em>.</p>
# MAGIC <p>You take some notes (your puzzle input) on the items each monkey currently has, how worried you are about those items, and how the monkey makes decisions based on your worry level. For example:</p>
# MAGIC <pre><code>Monkey 0:
# MAGIC   Starting items: 79, 98
# MAGIC   Operation: new = old * 19
# MAGIC   Test: divisible by 23
# MAGIC     If true: throw to monkey 2
# MAGIC     If false: throw to monkey 3
# MAGIC 
# MAGIC Monkey 1:
# MAGIC   Starting items: 54, 65, 75, 74
# MAGIC   Operation: new = old + 6
# MAGIC   Test: divisible by 19
# MAGIC     If true: throw to monkey 2
# MAGIC     If false: throw to monkey 0
# MAGIC 
# MAGIC Monkey 2:
# MAGIC   Starting items: 79, 60, 97
# MAGIC   Operation: new = old * old
# MAGIC   Test: divisible by 13
# MAGIC     If true: throw to monkey 1
# MAGIC     If false: throw to monkey 3
# MAGIC 
# MAGIC Monkey 3:
# MAGIC   Starting items: 74
# MAGIC   Operation: new = old + 3
# MAGIC   Test: divisible by 17
# MAGIC     If true: throw to monkey 0
# MAGIC     If false: throw to monkey 1
# MAGIC </code></pre>
# MAGIC <p>Each monkey has several attributes:</p>
# MAGIC <ul>
# MAGIC <li><code>Starting items</code> lists your <em>worry level</em> for each item the monkey is currently holding in the order they will be inspected.</li>
# MAGIC <li><code>Operation</code> shows how your worry level changes as that monkey inspects an item. (An operation like <code>new = old * 5</code> means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)</li>
# MAGIC <li><code>Test</code> shows how the monkey uses your worry level to decide where to throw an item next.
# MAGIC   <ul>
# MAGIC   <li><code>If true</code> shows what happens with an item if the <code>Test</code> was true.</li>
# MAGIC   <li><code>If false</code> shows what happens with an item if the <code>Test</code> was false.</li>
# MAGIC   </ul>
# MAGIC </li>
# MAGIC </ul>
# MAGIC <p>After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be <em>divided by three</em> and rounded down to the nearest integer.</p>
# MAGIC <p>The monkeys take turns inspecting and throwing items. On a single monkey's <em>turn</em>, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey <code>0</code> goes first, then monkey <code>1</code>, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a <em>round</em>.</p>
# MAGIC <p>When a monkey throws an item to another monkey, the item goes on the <em>end</em> of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.</p>
# MAGIC <p>In the above example, the first round proceeds as follows:</p>
# MAGIC <pre><code>Monkey 0:
# MAGIC   Monkey inspects an item with a worry level of 79.
# MAGIC     Worry level is multiplied by 19 to 1501.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 500.
# MAGIC     Current worry level is not divisible by 23.
# MAGIC     Item with worry level 500 is thrown to monkey 3.
# MAGIC   Monkey inspects an item with a worry level of 98.
# MAGIC     Worry level is multiplied by 19 to 1862.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 620.
# MAGIC     Current worry level is not divisible by 23.
# MAGIC     Item with worry level 620 is thrown to monkey 3.
# MAGIC Monkey 1:
# MAGIC   Monkey inspects an item with a worry level of 54.
# MAGIC     Worry level increases by 6 to 60.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 20.
# MAGIC     Current worry level is not divisible by 19.
# MAGIC     Item with worry level 20 is thrown to monkey 0.
# MAGIC   Monkey inspects an item with a worry level of 65.
# MAGIC     Worry level increases by 6 to 71.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 23.
# MAGIC     Current worry level is not divisible by 19.
# MAGIC     Item with worry level 23 is thrown to monkey 0.
# MAGIC   Monkey inspects an item with a worry level of 75.
# MAGIC     Worry level increases by 6 to 81.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 27.
# MAGIC     Current worry level is not divisible by 19.
# MAGIC     Item with worry level 27 is thrown to monkey 0.
# MAGIC   Monkey inspects an item with a worry level of 74.
# MAGIC     Worry level increases by 6 to 80.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 26.
# MAGIC     Current worry level is not divisible by 19.
# MAGIC     Item with worry level 26 is thrown to monkey 0.
# MAGIC Monkey 2:
# MAGIC   Monkey inspects an item with a worry level of 79.
# MAGIC     Worry level is multiplied by itself to 6241.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 2080.
# MAGIC     Current worry level is divisible by 13.
# MAGIC     Item with worry level 2080 is thrown to monkey 1.
# MAGIC   Monkey inspects an item with a worry level of 60.
# MAGIC     Worry level is multiplied by itself to 3600.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 1200.
# MAGIC     Current worry level is not divisible by 13.
# MAGIC     Item with worry level 1200 is thrown to monkey 3.
# MAGIC   Monkey inspects an item with a worry level of 97.
# MAGIC     Worry level is multiplied by itself to 9409.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 3136.
# MAGIC     Current worry level is not divisible by 13.
# MAGIC     Item with worry level 3136 is thrown to monkey 3.
# MAGIC Monkey 3:
# MAGIC   Monkey inspects an item with a worry level of 74.
# MAGIC     Worry level increases by 3 to 77.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 25.
# MAGIC     Current worry level is not divisible by 17.
# MAGIC     Item with worry level 25 is thrown to monkey 1.
# MAGIC   Monkey inspects an item with a worry level of 500.
# MAGIC     Worry level increases by 3 to 503.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 167.
# MAGIC     Current worry level is not divisible by 17.
# MAGIC     Item with worry level 167 is thrown to monkey 1.
# MAGIC   Monkey inspects an item with a worry level of 620.
# MAGIC     Worry level increases by 3 to 623.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 207.
# MAGIC     Current worry level is not divisible by 17.
# MAGIC     Item with worry level 207 is thrown to monkey 1.
# MAGIC   Monkey inspects an item with a worry level of 1200.
# MAGIC     Worry level increases by 3 to 1203.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 401.
# MAGIC     Current worry level is not divisible by 17.
# MAGIC     Item with worry level 401 is thrown to monkey 1.
# MAGIC   Monkey inspects an item with a worry level of 3136.
# MAGIC     Worry level increases by 3 to 3139.
# MAGIC     Monkey gets bored with item. Worry level is divided by 3 to 1046.
# MAGIC     Current worry level is not divisible by 17.
# MAGIC     Item with worry level 1046 is thrown to monkey 1.
# MAGIC </code></pre>
# MAGIC <p>After round 1, the monkeys are holding items with these worry levels:</p>
# MAGIC <pre><code>Monkey 0: 20, 23, 27, 26
# MAGIC Monkey 1: 2080, 25, 167, 207, 401, 1046
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC </code></pre>
# MAGIC <p>Monkeys 2 and 3 aren't holding any items at the end of the round; they both inspected items during the round and threw them all before the round ended.</p>
# MAGIC <p>This process continues for a few more rounds:</p>
# MAGIC <pre><code>After round 2, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 695, 10, 71, 135, 350
# MAGIC Monkey 1: 43, 49, 58, 55, 362
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 3, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 16, 18, 21, 20, 122
# MAGIC Monkey 1: 1468, 22, 150, 286, 739
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 4, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 491, 9, 52, 97, 248, 34
# MAGIC Monkey 1: 39, 45, 43, 258
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 5, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 15, 17, 16, 88, 1037
# MAGIC Monkey 1: 20, 110, 205, 524, 72
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 6, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 8, 70, 176, 26, 34
# MAGIC Monkey 1: 481, 32, 36, 186, 2190
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 7, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 162, 12, 14, 64, 732, 17
# MAGIC Monkey 1: 148, 372, 55, 72
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 8, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 51, 126, 20, 26, 136
# MAGIC Monkey 1: 343, 26, 30, 1546, 36
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 9, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 116, 10, 12, 517, 14
# MAGIC Monkey 1: 108, 267, 43, 55, 288
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC After round 10, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 91, 16, 20, 98
# MAGIC Monkey 1: 481, 245, 22, 26, 1092, 30
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After round 15, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 83, 44, 8, 184, 9, 20, 26, 102
# MAGIC Monkey 1: 110, 36
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After round 20, the monkeys are holding items with these worry levels:
# MAGIC Monkey 0: 10, 12, 14, 26, 34
# MAGIC Monkey 1: 245, 93, 53, 199, 115
# MAGIC Monkey 2: 
# MAGIC Monkey 3: 
# MAGIC </code></pre>
# MAGIC <p>Chasing all of the monkeys at once is impossible; you're going to have to focus on the <em>two most active</em> monkeys if you want any hope of getting your stuff back. Count the <em>total number of times each monkey inspects items</em> over 20 rounds:</p>
# MAGIC <pre><code><em>Monkey 0 inspected items 101 times.</em>
# MAGIC Monkey 1 inspected items 95 times.
# MAGIC Monkey 2 inspected items 7 times.
# MAGIC <em>Monkey 3 inspected items 105 times.</em>
# MAGIC </code></pre>
# MAGIC <p>In this example, the two most active monkeys inspected items 101 and 105 times. The level of <em>monkey business</em> in this situation can be found by multiplying these together: <code><em>10605</em></code>.</p>
# MAGIC <p>Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. <em>What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Monkey 0:
  Starting items: 50, 70, 89, 75, 66, 66
  Operation: new = old * 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 1:
  Starting items: 85
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 66, 51, 71, 76, 58, 55, 58, 60
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 79, 52, 55, 51
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 69, 92
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 5:
  Starting items: 71, 76, 73, 98, 67, 79, 99
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 6:
  Starting items: 82, 76, 69, 69, 57
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 65, 79, 86
  Operation: new = old + 5
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 0'''

# COMMAND ----------

import collections
import copy
import math
import re

monkeys_start = []
for lines in inp.split('\n\n'):
  lines = lines.splitlines()
  
  monkey_id = int(re.findall(r'\d+', lines[0])[0])
  starting_items = [int(item) for item in re.findall(r'\d+', lines[1])]
  op = eval('lambda old: ' + lines[2].split(' = ')[1])
  div = int(re.findall(r'\d+', lines[3])[0])
  monkey_true = int(re.findall(r'\d+', lines[4])[0])
  monkey_false = int(re.findall(r'\d+', lines[5])[0])
  
  monkeys_start.append((starting_items, op, div, monkey_true, monkey_false))

monkeys = copy.deepcopy(monkeys_start)
activity = collections.Counter()
for _ in range(20):
  for monkey, (items, op, div, monkey_true, monkey_false) in enumerate(monkeys):
    while items:
      activity[monkey] += 1
      item = items.pop(0)
      item = op(item)
      item //= 3
      if item % div == 0:
        monkeys[monkey_true][0].append(item)
      else:
        monkeys[monkey_false][0].append(item)

most_active = [monkey for _, monkey in activity.most_common(2)]
monkey_business = math.prod(most_active)
answer = monkey_business
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item <em>no longer causes your worry level to be divided by three</em>.</p>
# MAGIC <p>Unfortunately, that relief was all that was keeping your worry levels from reaching <em>ridiculous levels</em>. You'll need to <em>find another way to keep your worry levels manageable</em>.</p>
# MAGIC <p>At this rate, you might be putting up with these monkeys for a <em>very long time</em> - possibly <em><code>10000</code> rounds</em>!</p>
# MAGIC <p>With these new rules, you can still figure out the <span title="Monkey business monkey business monkey business, monkey numbers... is this working?">monkey business</span> after 10000 rounds. Using the same example above:</p>
# MAGIC <pre><code>== After round 1 ==
# MAGIC Monkey 0 inspected items 2 times.
# MAGIC Monkey 1 inspected items 4 times.
# MAGIC Monkey 2 inspected items 3 times.
# MAGIC Monkey 3 inspected items 6 times.
# MAGIC 
# MAGIC == After round 20 ==
# MAGIC Monkey 0 inspected items 99 times.
# MAGIC Monkey 1 inspected items 97 times.
# MAGIC Monkey 2 inspected items 8 times.
# MAGIC Monkey 3 inspected items 103 times.
# MAGIC 
# MAGIC == After round 1000 ==
# MAGIC Monkey 0 inspected items 5204 times.
# MAGIC Monkey 1 inspected items 4792 times.
# MAGIC Monkey 2 inspected items 199 times.
# MAGIC Monkey 3 inspected items 5192 times.
# MAGIC 
# MAGIC == After round 2000 ==
# MAGIC Monkey 0 inspected items 10419 times.
# MAGIC Monkey 1 inspected items 9577 times.
# MAGIC Monkey 2 inspected items 392 times.
# MAGIC Monkey 3 inspected items 10391 times.
# MAGIC 
# MAGIC == After round 3000 ==
# MAGIC Monkey 0 inspected items 15638 times.
# MAGIC Monkey 1 inspected items 14358 times.
# MAGIC Monkey 2 inspected items 587 times.
# MAGIC Monkey 3 inspected items 15593 times.
# MAGIC 
# MAGIC == After round 4000 ==
# MAGIC Monkey 0 inspected items 20858 times.
# MAGIC Monkey 1 inspected items 19138 times.
# MAGIC Monkey 2 inspected items 780 times.
# MAGIC Monkey 3 inspected items 20797 times.
# MAGIC 
# MAGIC == After round 5000 ==
# MAGIC Monkey 0 inspected items 26075 times.
# MAGIC Monkey 1 inspected items 23921 times.
# MAGIC Monkey 2 inspected items 974 times.
# MAGIC Monkey 3 inspected items 26000 times.
# MAGIC 
# MAGIC == After round 6000 ==
# MAGIC Monkey 0 inspected items 31294 times.
# MAGIC Monkey 1 inspected items 28702 times.
# MAGIC Monkey 2 inspected items 1165 times.
# MAGIC Monkey 3 inspected items 31204 times.
# MAGIC 
# MAGIC == After round 7000 ==
# MAGIC Monkey 0 inspected items 36508 times.
# MAGIC Monkey 1 inspected items 33488 times.
# MAGIC Monkey 2 inspected items 1360 times.
# MAGIC Monkey 3 inspected items 36400 times.
# MAGIC 
# MAGIC == After round 8000 ==
# MAGIC Monkey 0 inspected items 41728 times.
# MAGIC Monkey 1 inspected items 38268 times.
# MAGIC Monkey 2 inspected items 1553 times.
# MAGIC Monkey 3 inspected items 41606 times.
# MAGIC 
# MAGIC == After round 9000 ==
# MAGIC Monkey 0 inspected items 46945 times.
# MAGIC Monkey 1 inspected items 43051 times.
# MAGIC Monkey 2 inspected items 1746 times.
# MAGIC Monkey 3 inspected items 46807 times.
# MAGIC 
# MAGIC == After round 10000 ==
# MAGIC <em>Monkey 0 inspected items 52166 times.</em>
# MAGIC Monkey 1 inspected items 47830 times.
# MAGIC Monkey 2 inspected items 1938 times.
# MAGIC <em>Monkey 3 inspected items 52013 times.</em>
# MAGIC </code></pre>
# MAGIC <p>After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of <em>monkey business</em> in this situation is now <code><em>2713310158</em></code>.</p>
# MAGIC <p>Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, <em>what is the level of monkey business after 10000 rounds?</em></p>
# MAGIC </article>

# COMMAND ----------

lcm = math.lcm(*(div for _, _, div, _, _ in monkeys))

monkeys = copy.deepcopy(monkeys_start)
activity = collections.Counter()
for _ in range(10000):
  for monkey, (items, op, div, monkey_true, monkey_false) in enumerate(monkeys):
    while items:
      activity[monkey] += 1
      item = items.pop(0)
      item = op(item)
      if item % div == 0:
        monkeys[monkey_true][0].append(item % lcm)
      else:
        monkeys[monkey_false][0].append(item % lcm)

most_active = [monkey for _, monkey in activity.most_common(2)]
monkey_business = math.prod(most_active)
answer = monkey_business
print(answer)
