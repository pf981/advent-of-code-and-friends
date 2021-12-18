# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 18: Snailfish ---</h2><p>You descend into the ocean trench and encounter some <a href="https://en.wikipedia.org/wiki/Snailfish" target="_blank">snailfish</a>. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his <em><span title="Or 'maths', if you have more than one.">math</span> homework</em>.</p>
# MAGIC <p>Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a <em>pair</em> - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.</p>
# MAGIC <p>Pairs are written as <code>[x,y]</code>, where <code>x</code> and <code>y</code> are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:</p>
# MAGIC <pre><code>[1,2]
# MAGIC [[1,2],3]
# MAGIC [9,[8,7]]
# MAGIC [[1,9],[8,5]]
# MAGIC [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
# MAGIC [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
# MAGIC [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
# MAGIC </code></pre>
# MAGIC <p>This snailfish homework is about <em>addition</em>. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, <code>[1,2]</code> + <code>[[3,4],5]</code> becomes <code>[[1,2],[[3,4],5]]</code>.</p>
# MAGIC <p>There's only one problem: <em>snailfish numbers must always be reduced</em>, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.</p>
# MAGIC <p>To <em>reduce a snailfish number</em>, you must repeatedly do the first action in this list that applies to the snailfish number:</p>
# MAGIC <ul>
# MAGIC <li>If any pair is <em>nested inside four pairs</em>, the leftmost such pair <em>explodes</em>.</li>
# MAGIC <li>If any regular number is <em>10 or greater</em>, the leftmost such regular number <em>splits</em>.</li>
# MAGIC </ul>
# MAGIC <p>Once no action in the above list applies, the snailfish number is reduced.</p>
# MAGIC <p>During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if <em>split</em> produces a pair that meets the <em>explode</em> criteria, that pair <em>explodes</em> before other <em>splits</em> occur.</p>
# MAGIC <p>To <em>explode</em> a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number <code>0</code>.</p>
# MAGIC <p>Here are some examples of a single explode action:</p>
# MAGIC <ul>
# MAGIC <li><code>[[[[<em>[9,8]</em>,1],2],3],4]</code> becomes <code>[[[[<em>0</em>,<em>9</em>],2],3],4]</code> (the <code>9</code> has no regular number to its left, so it is not added to any regular number).</li>
# MAGIC <li><code>[7,[6,[5,[4,<em>[3,2]</em>]]]]</code> becomes <code>[7,[6,[5,[<em>7</em>,<em>0</em>]]]]</code> (the <code>2</code> has no regular number to its right, and so it is not added to any regular number).</li>
# MAGIC <li><code>[[6,[5,[4,<em>[3,2]</em>]]],1]</code> becomes <code>[[6,[5,[<em>7</em>,<em>0</em>]]],<em>3</em>]</code>.</li>
# MAGIC <li><code>[[3,[2,[1,<em>[7,3]</em>]]],[6,[5,[4,[3,2]]]]]</code> becomes <code>[[3,[2,[<em>8</em>,<em>0</em>]]],[<em>9</em>,[5,[4,[3,2]]]]]</code> (the pair <code>[3,2]</code> is unaffected because the pair <code>[7,3]</code> is further to the left; <code>[3,2]</code> would explode on the next action).</li>
# MAGIC <li><code>[[3,[2,[8,0]]],[9,[5,[4,<em>[3,2]</em>]]]]</code> becomes <code>[[3,[2,[8,0]]],[9,[5,[<em>7</em>,<em>0</em>]]]]</code>.</li>
# MAGIC </ul>
# MAGIC <p>To <em>split</em> a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded <em>down</em>, while the right element of the pair should be the regular number divided by two and rounded <em>up</em>. For example, <code>10</code> becomes <code>[5,5]</code>, <code>11</code> becomes <code>[5,6]</code>, <code>12</code> becomes <code>[6,6]</code>, and so on.</p>
# MAGIC <p>Here is the process of finding the reduced result of <code>[[[[4,3],4],4],[7,[[8,4],9]]]</code> + <code>[1,1]</code>:</p>
# MAGIC <pre><code>after addition: [[[[<em>[4,3]</em>,4],4],[7,[[8,4],9]]],[1,1]]
# MAGIC after explode:  [[[[0,7],4],[7,[<em>[8,4]</em>,9]]],[1,1]]
# MAGIC after explode:  [[[[0,7],4],[<em>15</em>,[0,13]]],[1,1]]
# MAGIC after split:    [[[[0,7],4],[[7,8],[0,<em>13</em>]]],[1,1]]
# MAGIC after split:    [[[[0,7],4],[[7,8],[0,<em>[6,7]</em>]]],[1,1]]
# MAGIC after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
# MAGIC </code></pre>
# MAGIC <p>Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: <code>[[[[0,7],4],[[7,8],[6,0]]],[8,1]]</code>.</p>
# MAGIC <p>The homework assignment involves adding up a <em>list of snailfish numbers</em> (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.</p>
# MAGIC <p>For example, the final sum of this list is <code>[[[[1,1],[2,2]],[3,3]],[4,4]]</code>:</p>
# MAGIC <pre><code>[1,1]
# MAGIC [2,2]
# MAGIC [3,3]
# MAGIC [4,4]
# MAGIC </code></pre>
# MAGIC <p>The final sum of this list is <code>[[[[3,0],[5,3]],[4,4]],[5,5]]</code>:</p>
# MAGIC <pre><code>[1,1]
# MAGIC [2,2]
# MAGIC [3,3]
# MAGIC [4,4]
# MAGIC [5,5]
# MAGIC </code></pre>
# MAGIC <p>The final sum of this list is <code>[[[[5,0],[7,4]],[5,5]],[6,6]]</code>:</p>
# MAGIC <pre><code>[1,1]
# MAGIC [2,2]
# MAGIC [3,3]
# MAGIC [4,4]
# MAGIC [5,5]
# MAGIC [6,6]
# MAGIC </code></pre>
# MAGIC <p>Here's a slightly larger example:</p>
# MAGIC <pre><code>[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# MAGIC [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# MAGIC [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# MAGIC [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# MAGIC [7,[5,[[3,8],[1,4]]]]
# MAGIC [[2,[2,2]],[8,[8,1]]]
# MAGIC [2,9]
# MAGIC [1,[[[9,3],9],[[9,0],[0,7]]]]
# MAGIC [[[5,[7,4]],7],1]
# MAGIC [[[[4,2],2],6],[8,7]]
# MAGIC </code></pre>
# MAGIC <p>The final sum <code>[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]</code> is found after adding up the above snailfish numbers:</p>
# MAGIC <pre><code>  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# MAGIC + [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# MAGIC = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
# MAGIC 
# MAGIC   [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
# MAGIC + [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# MAGIC = [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
# MAGIC 
# MAGIC   [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
# MAGIC + [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# MAGIC = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
# MAGIC 
# MAGIC   [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
# MAGIC + [7,[5,[[3,8],[1,4]]]]
# MAGIC = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
# MAGIC 
# MAGIC   [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
# MAGIC + [[2,[2,2]],[8,[8,1]]]
# MAGIC = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
# MAGIC 
# MAGIC   [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
# MAGIC + [2,9]
# MAGIC = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
# MAGIC 
# MAGIC   [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
# MAGIC + [1,[[[9,3],9],[[9,0],[0,7]]]]
# MAGIC = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
# MAGIC 
# MAGIC   [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
# MAGIC + [[[5,[7,4]],7],1]
# MAGIC = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
# MAGIC 
# MAGIC   [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
# MAGIC + [[[[4,2],2],6],[8,7]]
# MAGIC = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
# MAGIC </code></pre>
# MAGIC <p>To check whether it's the right answer, the snailfish teacher only checks the <em>magnitude</em> of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.</p>
# MAGIC <p>For example, the magnitude of <code>[9,1]</code> is <code>3*9 + 2*1 = <em>29</em></code>; the magnitude of <code>[1,9]</code> is <code>3*1 + 2*9 = <em>21</em></code>. Magnitude calculations are recursive: the magnitude of <code>[[9,1],[1,9]]</code> is <code>3*29 + 2*21 = <em>129</em></code>.</p>
# MAGIC <p>Here are a few more magnitude examples:</p>
# MAGIC <ul>
# MAGIC <li><code>[[1,2],[[3,4],5]]</code> becomes <code><em>143</em></code>.</li>
# MAGIC <li><code>[[[[0,7],4],[[7,8],[6,0]]],[8,1]]</code> becomes <code><em>1384</em></code>.</li>
# MAGIC <li><code>[[[[1,1],[2,2]],[3,3]],[4,4]]</code> becomes <code><em>445</em></code>.</li>
# MAGIC <li><code>[[[[3,0],[5,3]],[4,4]],[5,5]]</code> becomes <code><em>791</em></code>.</li>
# MAGIC <li><code>[[[[5,0],[7,4]],[5,5]],[6,6]]</code> becomes <code><em>1137</em></code>.</li>
# MAGIC <li><code>[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]</code> becomes <code><em>3488</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>So, given this example homework assignment:</p>
# MAGIC <pre><code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# MAGIC [[[5,[2,8]],4],[5,[[9,9],0]]]
# MAGIC [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# MAGIC [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# MAGIC [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# MAGIC [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# MAGIC [[[[5,4],[7,7]],8],[[8,3],8]]
# MAGIC [[9,3],[[9,9],[6,[4,9]]]]
# MAGIC [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# MAGIC [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# MAGIC </code></pre>
# MAGIC <p>The final sum is:</p>
# MAGIC <pre><code>[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]</code></pre>
# MAGIC <p>The magnitude of this final sum is <code><em>4140</em></code>.</p>
# MAGIC <p>Add up all of the snailfish numbers from the homework assignment in the order they appear. <em>What is the magnitude of the final sum?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''[1,[[9,[5,8]],[[2,0],0]]]
[[[6,4],6],[[1,[7,3]],[[0,1],[4,9]]]]
[[[7,3],[8,6]],[[4,[1,2]],7]]
[[[2,[4,5]],[[7,1],2]],1]
[[[[4,4],[4,6]],9],[[4,2],6]]
[[[9,8],[[4,0],0]],[[2,[5,1]],[[9,6],[9,2]]]]
[[[6,[9,0]],0],[6,[[5,8],3]]]
[[[[7,3],[5,4]],0],[3,[[0,6],3]]]
[5,[[0,0],[[4,8],[8,6]]]]
[[[3,[9,2]],9],[5,[0,6]]]
[[[[6,3],[3,2]],[5,9]],2]
[[[0,4],7],[8,[8,[4,2]]]]
[[[8,[8,0]],9],[[1,[6,3]],[4,2]]]
[[[[5,4],[1,5]],[1,3]],[[[9,0],[7,4]],9]]
[[[5,[4,2]],[[9,2],3]],[[[6,2],[6,8]],[[2,4],[9,4]]]]
[[9,6],[0,[[1,1],9]]]
[[[8,[5,9]],[2,9]],[0,[[7,6],[7,6]]]]
[[[5,[4,8]],[[7,7],[2,2]]],[[[2,6],[5,7]],[0,[6,2]]]]
[[[[9,3],5],3],[[[1,5],2],[3,3]]]
[[[2,[1,1]],[[5,8],[7,1]]],[[9,7],5]]
[[9,9],3]
[[[5,[6,1]],9],[1,[9,3]]]
[[[[1,2],7],[[6,8],[4,1]]],[[2,3],[6,3]]]
[[[[9,3],[7,9]],2],[[9,[3,4]],[[2,6],[7,0]]]]
[[8,[4,9]],[[2,[5,6]],6]]
[3,[[[9,7],7],[[2,6],4]]]
[[[[3,4],[0,8]],[[6,4],[2,6]]],[[[1,4],[5,4]],8]]
[8,[[0,[5,5]],[[1,2],1]]]
[[[5,[8,1]],[[1,8],[4,0]]],[8,8]]
[[[9,5],3],[[7,9],[1,6]]]
[[[[1,1],1],[[2,0],[2,5]]],5]
[[3,[[5,4],[7,4]]],[[4,4],[1,9]]]
[[0,[[7,4],[7,2]]],[[8,0],[5,9]]]
[0,[[[1,2],4],[[1,0],[6,4]]]]
[[[[6,6],[9,8]],3],[[[5,5],[1,6]],[8,[5,3]]]]
[[7,[[5,6],0]],[5,[[9,2],4]]]
[[[4,[4,5]],[7,[4,5]]],[[[9,8],8],[[8,2],[3,0]]]]
[[[8,[0,5]],[[0,4],[8,9]]],[8,[4,6]]]
[[[4,[9,7]],[[7,4],[7,1]]],[[[8,4],0],[[6,9],[9,0]]]]
[[3,6],[[3,[4,6]],[[6,0],0]]]
[3,[1,[[4,0],1]]]
[[[9,9],[0,[6,3]]],[3,2]]
[7,4]
[2,6]
[[[3,[7,8]],7],[[0,[2,5]],[1,1]]]
[0,5]
[8,[8,[[2,4],5]]]
[[[[8,2],1],[9,0]],[[[0,8],[3,0]],9]]
[[[[7,0],1],[[0,1],[6,7]]],[[[3,1],[8,3]],7]]
[8,0]
[[[7,[1,3]],[7,[7,2]]],[[9,0],4]]
[[[[0,3],5],[[1,0],8]],[[0,2],9]]
[[5,[[7,6],[7,2]]],5]
[[[[2,8],[5,4]],[1,6]],[[8,8],[[5,2],4]]]
[[[[1,5],[1,8]],1],[[6,[2,4]],5]]
[[[[9,7],[6,3]],2],[[3,[4,4]],[3,4]]]
[[[9,2],[2,9]],[[[0,7],[0,8]],[[0,2],[6,7]]]]
[[[[1,1],3],[[1,4],[8,9]]],[[8,[8,6]],[7,7]]]
[5,[[1,[8,8]],[6,3]]]
[[[1,4],3],7]
[[[[0,1],[2,0]],2],[[8,8],7]]
[[[[2,8],[4,4]],[[5,6],8]],[[[5,3],1],7]]
[[9,[0,[8,3]]],[5,6]]
[[[0,[8,9]],[6,[8,1]]],[[[2,3],8],[[4,0],8]]]
[[2,[5,4]],[[7,4],[[5,0],3]]]
[[[[1,1],2],[[3,0],[7,7]]],[[1,[3,8]],2]]
[[[1,4],[6,[2,4]]],[[5,5],0]]
[[[[4,4],8],[[4,3],[3,5]]],[[7,1],2]]
[[[4,[0,8]],9],[[[6,9],2],8]]
[[[[0,0],1],[1,1]],[2,[[0,0],[7,7]]]]
[[2,[5,5]],9]
[[[[5,8],[7,7]],[[9,8],5]],[[3,5],[8,8]]]
[[5,[3,[3,9]]],[3,[9,8]]]
[[8,[4,6]],[[5,0],[9,2]]]
[[[3,[1,8]],[4,5]],[[0,[5,9]],6]]
[9,[[1,1],0]]
[[[[6,1],[9,2]],4],[5,3]]
[[[[3,0],[0,5]],[1,[5,2]]],[[[2,0],[0,2]],[[6,4],4]]]
[[[[1,1],[4,6]],[[3,8],[3,2]]],[[[4,3],7],[2,[7,8]]]]
[4,[[1,5],5]]
[8,[[1,1],0]]
[[[[8,4],[9,9]],[3,[6,6]]],[[[7,9],[9,7]],7]]
[[2,5],[8,[3,8]]]
[[[6,1],[7,[3,5]]],9]
[[1,[[3,6],[1,0]]],[[[2,8],8],[4,[2,7]]]]
[[[3,[6,9]],[[9,6],[0,8]]],[[5,[6,4]],[[3,4],1]]]
[[[[7,7],1],[5,[2,5]]],[[3,7],[[4,7],3]]]
[[4,[3,[7,2]]],[[[8,8],[5,8]],8]]
[[3,[[9,9],6]],6]
[[6,7],[2,9]]
[[[9,7],[1,[4,0]]],[[[3,4],0],[1,2]]]
[9,[[8,[8,4]],3]]
[[[4,[4,1]],[[4,7],[2,3]]],[8,[5,[1,5]]]]
[7,[2,[4,1]]]
[[[[1,5],7],[5,9]],8]
[[[[1,5],[0,4]],8],[[[7,0],6],[8,3]]]
[[[7,[3,5]],0],[8,[9,[5,6]]]]
[[1,[[5,1],5]],[[5,1],[9,[3,0]]]]
[3,[[[8,5],[7,5]],[9,4]]]
[[[3,3],[2,[5,9]]],7]'''

# COMMAND ----------

import functools
import math


def parse_line(s):
  l = []
  num = ''
  for c in s:
    if c in '0123456789':
      num += c
    else:
      if num != '':
        l.append(int(num))
      num = ''
      l.append(c)
  return l


def sailfish_add(a, b):
  return snailfish_reduce(['['] + a + [','] + b + [']'])


def index_next_number_right(l, i):
  for index in range(i + 1, len(l)):
    if isinstance(l[index], int):
      return index


def index_next_number_left(l, i):
  for index in range(i - 1, -1, -1):
    if isinstance(l[index], int):
      return index


def explode(l):
  depth = -1
  for i, c in enumerate(l):
    if c == '[':
      depth += 1
    elif c == ']':
      depth -= 1
    elif c == ',':
      continue
    else:
      if depth == 4:
        index_left = i
        index_next_left = index_next_number_left(l, i)
        
        index_right = index_next_number_right(l, i)
        index_next_right = index_next_number_right(l, index_right)
        
        if index_next_left is not None:
          l[index_next_left] += l[index_left]
        if index_next_right is not None:
          l[index_next_right] += l[index_right]
          
        l[index_left] = 0
        del l[index_left + 1] # ,
        del l[index_left + 1] # right
        del l[index_left + 1] # ]
        del l[index_left - 1] # [
        return True
  return False


def split(l):
  for i, c in enumerate(l):
    if isinstance(c, int) and c >= 10:
      del l[i]
      l.insert(i, '[')
      l.insert(i+1, c // 2)
      l.insert(i+2, ',')
      l.insert(i+3, math.ceil(c / 2))
      l.insert(i+4, ']')
      return True
  return False


def snailfish_reduce(l):
  while True:
    if explode(l):
      continue
    if split(l):
      continue
    break
  return l


def get_magnitude_impl(l):
  if isinstance(l, int):
    return l
  return 3 * get_magnitude_impl(l[0]) + 2 * get_magnitude_impl(l[1])


def get_magnitude(l):
  return get_magnitude_impl(eval(''.join(str(s) for s in l)))
  

addends = [parse_line(line) for line in inp.splitlines()]

answer = get_magnitude(functools.reduce(sailfish_add, addends))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You notice a second question on the back of the homework assignment:</p>
# MAGIC <p>What is the largest magnitude you can get from adding only two of the snailfish numbers?</p>
# MAGIC <p>Note that snailfish addition is not <a href="https://en.wikipedia.org/wiki/Commutative_property" target="_blank">commutative</a> - that is, <code>x + y</code> and <code>y + x</code> can produce different results.</p>
# MAGIC <p>Again considering the last example homework assignment above:</p>
# MAGIC <pre><code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# MAGIC [[[5,[2,8]],4],[5,[[9,9],0]]]
# MAGIC [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# MAGIC [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# MAGIC [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# MAGIC [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# MAGIC [[[[5,4],[7,7]],8],[[8,3],8]]
# MAGIC [[9,3],[[9,9],[6,[4,9]]]]
# MAGIC [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# MAGIC [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# MAGIC </code></pre>
# MAGIC <p>The largest magnitude of the sum of any two snailfish numbers in this list is <code><em>3993</em></code>. This is the magnitude of <code>[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]</code> + <code>[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]</code>, which reduces to <code>[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]</code>.</p>
# MAGIC <p><em>What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?</em></p>
# MAGIC </article>

# COMMAND ----------

largest_magnitude = max(
  get_magnitude(sailfish_add(left, right))
  for left in addends
  for right in addends
  if left != right
)

answer = largest_magnitude
print(answer)
