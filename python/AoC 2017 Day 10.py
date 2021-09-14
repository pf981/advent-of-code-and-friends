# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/10

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 10: Knot Hash ---</h2><p>You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind the Elves later not to <span title="NEW CRYPTOSYSTEM WHO DIS">invent their own cryptographic functions</span>.</p>
# MAGIC <p>This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed, the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting hash.</p>
# MAGIC <pre><code>  4--5   pinch   4  5           4   1
# MAGIC  /    \  5,0,1  / \/ \  twist  / \ / \
# MAGIC 3      0  --&gt;  3      0  --&gt;  3   X   0
# MAGIC  \    /         \ /\ /         \ / \ /
# MAGIC   2--1           2  1           2   5
# MAGIC </code></pre>
# MAGIC <p>To achieve this, begin with a <em>list</em> of numbers from <code>0</code> to <code>255</code>, a <em>current position</em> which begins at <code>0</code> (the first element in the list), a <em>skip size</em> (which starts at <code>0</code>), and a sequence of <em>lengths</em> (your puzzle input).  Then, for each length:</p>
# MAGIC <ul>
# MAGIC <li><em>Reverse</em> the order of that <em>length</em> of elements in the <em>list</em>, starting with the element at the <em>current position</em>.</li>
# MAGIC <li><em>Move</em> the <em>current position</em> forward by that <em>length</em> plus the <em>skip size</em>.</li>
# MAGIC <li><em>Increase</em> the <em>skip size</em> by one.</li>
# MAGIC </ul>
# MAGIC <p>The <em>list</em> is circular; if the <em>current position</em> and the <em>length</em> try to reverse elements beyond the end of the list, the operation reverses using as many extra elements as it needs from the front of the list. If the <em>current position</em> moves past the end of the list, it wraps around to the front. <em>Lengths</em> larger than the size of the <em>list</em> are invalid.</p>
# MAGIC <p>Here's an example using a smaller list:</p>
# MAGIC <p>Suppose we instead only had a circular list containing five elements, <code>0, 1, 2, 3, 4</code>, and were given input lengths of <code>3, 4, 1, 5</code>.</p>
# MAGIC <ul>
# MAGIC <li>The list begins as <code>[0] 1 2 3 4</code> (where square brackets indicate the <em>current position</em>).</li>
# MAGIC <li>The first length, <code>3</code>, selects <code>([0] 1 2) 3 4</code> (where parentheses indicate the sublist to be reversed).</li>
# MAGIC <li>After reversing that section (<code>0 1 2</code> into <code>2 1 0</code>), we get <code>([2] 1 0) 3 4</code>.</li>
# MAGIC <li>Then, the <em>current position</em> moves forward by the <em>length</em>, <code>3</code>, plus the <em>skip size</em>, 0: <code>2 1 0 [3] 4</code>. Finally, the <em>skip size</em> increases to <code>1</code>.</li>
# MAGIC </ul>
# MAGIC <ul>
# MAGIC <li>The second length, <code>4</code>, selects a section which wraps: <code>2 1) 0 ([3] 4</code>.</li>
# MAGIC <li>The sublist <code>3 4 2 1</code> is reversed to form <code>1 2 4 3</code>: <code>4 3) 0 ([1] 2</code>.</li>
# MAGIC <li>The <em>current position</em> moves forward by the <em>length</em> plus the <em>skip size</em>, a total of <code>5</code>, causing it not to move because it wraps around: <code>4 3 0 [1] 2</code>. The <em>skip size</em> increases to <code>2</code>.</li>
# MAGIC </ul>
# MAGIC <ul>
# MAGIC <li>The third length, <code>1</code>, selects a sublist of a single element, and so reversing it has no effect.</li>
# MAGIC <li>The <em>current position</em> moves forward by the <em>length</em> (<code>1</code>) plus the <em>skip size</em> (<code>2</code>): <code>4 [3] 0 1 2</code>. The <em>skip size</em> increases to <code>3</code>.</li>
# MAGIC </ul>
# MAGIC <ul>
# MAGIC <li>The fourth length, <code>5</code>, selects every element starting with the second: <code>4) ([3] 0 1 2</code>. Reversing this sublist (<code>3 0 1 2 4</code> into <code>4 2 1 0 3</code>) produces: <code>3) ([4] 2 1 0</code>.</li>
# MAGIC <li>Finally, the <em>current position</em> moves forward by <code>8</code>: <code>3 4 2 1 [0]</code>. The <em>skip size</em> increases to <code>4</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the first two numbers in the list end up being <code>3</code> and <code>4</code>; to check the process, you can multiply them together to produce <code>12</code>.</p>
# MAGIC <p>However, you should instead use the standard list size of <code>256</code> (with values <code>0</code> to <code>255</code>) and the sequence of <em>lengths</em> in your puzzle input. Once this process is complete, <em>what is the result of multiplying the first two numbers in the list</em>?</p>
# MAGIC </article>

# COMMAND ----------

inp = '83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100'

# COMMAND ----------

import collections
import math

def reverse(nums, n):
  rev = collections.deque()

  for _ in range(n):
    rev.append(nums.popleft())
  
  while rev:
    nums.appendleft(rev.popleft())

def hash_lengths(lengths, n_rounds=1):
  nums = collections.deque(range(256))
  skip_size = 0
  total_rotation = 0
  
  for _ in range(n_rounds):
    for length in lengths:
      reverse(nums, length)

      rotation = length + skip_size
      total_rotation += rotation
      nums.rotate(-rotation)

      skip_size += 1
  
  nums.rotate(total_rotation)
  return list(nums)

lengths = [int(x) for x in inp.split(',')]

answer = math.prod(hash_lengths(lengths)[:2])
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The logic you've constructed forms a single <em>round</em> of the <em>Knot Hash</em> algorithm; running the full thing requires many of these rounds. Some input and output processing is also required.</p>
# MAGIC <p>First, from now on, your input should be taken not as a list of numbers, but as a string of bytes instead. Unless otherwise specified, convert characters to bytes using their <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters">ASCII codes</a>. This will allow you to handle arbitrary ASCII strings, and it also ensures that your input lengths are never larger than <code>255</code>. For example, if you are given <code>1,2,3</code>, you should convert it to the ASCII codes for each character: <code>49,44,50,44,51</code>.</p>
# MAGIC <p>Once you have determined the sequence of lengths to use, add the following lengths to the end of the sequence: <code>17, 31, 73, 47, 23</code>. For example, if you are given <code>1,2,3</code>, your final sequence of lengths should be <code>49,44,50,44,51,17,31,73,47,23</code> (the ASCII codes from the input string combined with the standard length suffix values).</p>
# MAGIC <p>Second, instead of merely running one <em>round</em> like you did above, run a total of <code>64</code> rounds, using the same <em>length</em> sequence in each round. The <em>current position</em> and <em>skip size</em> should be preserved between rounds. For example, if the previous example was your first round, you would start your second round with the same <em>length</em> sequence (<code>3, 4, 1, 5, 17, 31, 73, 47, 23</code>, now assuming they came from ASCII codes and include the suffix), but start with the previous round's <em>current position</em> (<code>4</code>) and <em>skip size</em> (<code>4</code>).</p>
# MAGIC <p>Once the rounds are complete, you will be left with the numbers from <code>0</code> to <code>255</code> in some order, called the <em>sparse hash</em>. Your next task is to reduce these to a list of only <code>16</code> numbers called the <em>dense hash</em>. To do this, use numeric bitwise <a href="https://en.wikipedia.org/wiki/Bitwise_operation#XOR">XOR</a> to combine each consecutive block of <code>16</code> numbers in the sparse hash (there are <code>16</code> such blocks in a list of <code>256</code> numbers). So, the first element in the dense hash is the first sixteen elements of the sparse hash XOR'd together, the second element in the dense hash is the second sixteen elements of the sparse hash XOR'd together, etc.</p>
# MAGIC <p>For example, if the first sixteen elements of your sparse hash are as shown below, and the XOR operator is <code>^</code>, you would calculate the first output number like this:</p>
# MAGIC <pre><code>65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22 = 64</code></pre>
# MAGIC <p>Perform this operation on each of the sixteen blocks of sixteen numbers in your sparse hash to determine the sixteen numbers in your dense hash.</p>
# MAGIC <p>Finally, the standard way to represent a Knot Hash is as a single <a href="https://en.wikipedia.org/wiki/Hexadecimal">hexadecimal</a> string; the final output is the dense hash in hexadecimal notation. Because each number in your dense hash will be between <code>0</code> and <code>255</code> (inclusive), always represent each number as two hexadecimal digits (including a leading zero as necessary). So, if your first three numbers are <code>64, 7, 255</code>, they correspond to the hexadecimal numbers <code>40, 07, ff</code>, and so the first six characters of the hash would be <code>4007ff</code>. Because every Knot Hash is sixteen such numbers, the hexadecimal representation is always <code>32</code> hexadecimal digits (<code>0</code>-<code>f</code>) long.
# MAGIC </p><p>Here are some example hashes:</p>
# MAGIC <ul>
# MAGIC <li>The empty string becomes <code>a2582a3a0e66e6e86e3812dcb672a272</code>.</li>
# MAGIC <li><code>AoC 2017</code> becomes <code>33efeb34ea91902bb2f59c9920caa6cd</code>.</li>
# MAGIC <li><code>1,2,3</code> becomes <code>3efbe78a8d82f29979031a4aa0b16a9d</code>.</li>
# MAGIC <li><code>1,2,4</code> becomes <code>63960835bcdc130f0b66d7ff4f6a5a8e</code>.</li>
# MAGIC </ul>
# MAGIC <p>Treating your puzzle input as a string of ASCII characters, <em>what is the Knot Hash of your puzzle input?</em> Ignore any leading or trailing whitespace you might encounter.</p>
# MAGIC </article>

# COMMAND ----------

import functools
import operator

def get_knot_hash(s):
  lengths = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
  sparse_hash = hash_lengths(lengths, n_rounds=64)
  dense_hash = [functools.reduce(operator.xor, l) for l in zip(*[iter(sparse_hash)] * 16)]
  return ''.join(f'{i:0>2x}' for i in dense_hash)

answer = get_knot_hash(inp)
print(answer)
