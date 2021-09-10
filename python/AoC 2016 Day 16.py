# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/16

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: Dragon Checksum ---</h2><p>You're done scanning this part of the network, but you've left traces of your presence. You need to <span title="If I ever find one of my disks overwritten with a dragon curve, I'll know it was you.">overwrite some disks</span> with random-looking data to cover your tracks and update the local security system with a new checksum for those disks.</p>
# MAGIC <p>For the data to not be suspicious, it needs to have certain properties; purely random data will be detected as tampering. To generate appropriate random data, you'll need to use a modified <a href="https://en.wikipedia.org/wiki/Dragon_curve">dragon curve</a>.</p>
# MAGIC <p>Start with an appropriate initial state (your puzzle input). Then, so long as you don't have enough data yet to fill the disk, repeat the following steps:</p>
# MAGIC <ul>
# MAGIC <li>Call the data you have at this point "a".</li>
# MAGIC <li>Make a copy of "a"; call this copy "b".</li>
# MAGIC <li>Reverse the order of the characters in "b".</li>
# MAGIC <li>In "b", replace all instances of <code>0</code> with <code>1</code> and all <code>1</code>s with <code>0</code>.</li>
# MAGIC <li>The resulting data is "a", then a single <code>0</code>, then "b".</li>
# MAGIC </ul>
# MAGIC <p>For example, after a single step of this process,</p>
# MAGIC <ul>
# MAGIC <li><code>1</code> becomes <code>100</code>.</li>
# MAGIC <li><code>0</code> becomes <code>001</code>.</li>
# MAGIC <li><code>11111</code> becomes <code>11111000000</code>.</li>
# MAGIC <li><code>111100001010</code> becomes <code>1111000010100101011110000</code>.</li>
# MAGIC </ul>
# MAGIC <p>Repeat these steps until you have enough data to fill the desired disk.</p>
# MAGIC <p>Once the data has been generated, you also need to create a checksum of that data. Calculate the checksum <em>only</em> for the data that fits on the disk, even if you generated more data than that in the previous step.</p>
# MAGIC <p>The checksum for some given data is created by considering each non-overlapping <em>pair</em> of characters in the input data.  If the two characters match (<code>00</code> or <code>11</code>), the next checksum character is a <code>1</code>.  If the characters do not match (<code>01</code> or <code>10</code>), the next checksum character is a <code>0</code>. This should produce a new string which is exactly half as long as the original. If the length of the checksum is <em>even</em>, repeat the process until you end up with a checksum with an <em>odd</em> length.</p>
# MAGIC <p>For example, suppose we want to fill a disk of length <code>12</code>, and when we finally generate a string of at least length <code>12</code>, the first <code>12</code> characters are <code>110010110100</code>. To generate its checksum:</p>
# MAGIC <ul>
# MAGIC <li>Consider each pair: <code>11</code>, <code>00</code>, <code>10</code>, <code>11</code>, <code>01</code>, <code>00</code>.</li>
# MAGIC <li>These are same, same, different, same, different, same, producing <code>110101</code>.</li>
# MAGIC <li>The resulting string has length <code>6</code>, which is <em>even</em>, so we repeat the process.</li>
# MAGIC <li>The pairs are <code>11</code> (same), <code>01</code> (different), <code>01</code> (different).</li>
# MAGIC <li>This produces the checksum <code>100</code>, which has an <em>odd</em> length, so we stop.</li>
# MAGIC </ul>
# MAGIC <p>Therefore, the checksum for <code>110010110100</code> is <code>100</code>.</p>
# MAGIC <p>Combining all of these steps together, suppose you want to fill a disk of length <code>20</code> using an initial state of <code>10000</code>:</p>
# MAGIC <ul>
# MAGIC <li>Because <code>10000</code> is too short, we first use the modified dragon curve to make it longer.</li>
# MAGIC <li>After one round, it becomes <code>10000011110</code> (<code>11</code> characters), still too short.</li>
# MAGIC <li>After two rounds, it becomes <code>10000011110010000111110</code> (<code>23</code> characters), which is enough.</li>
# MAGIC <li>Since we only need <code>20</code>, but we have <code>23</code>, we get rid of all but the first <code>20</code> characters: <code>10000011110010000111</code>.</li>
# MAGIC <li>Next, we start calculating the checksum; after one round, we have <code>0111110101</code>, which <code>10</code> characters long (<em>even</em>), so we continue.</li>
# MAGIC <li>After two rounds, we have <code>01100</code>, which is <code>5</code> characters long (<em>odd</em>), so we are done.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the correct checksum would therefore be <code>01100</code>.</p>
# MAGIC <p>The first disk you have to fill has length <code>272</code>. Using the initial state in your puzzle input, <em>what is the correct checksum</em>?</p>
# MAGIC </article>

# COMMAND ----------

inp = '11011110011011101'

# COMMAND ----------

def grow_bits(bits, length_out):
  while len(bits) < length_out:
    bits += [False] + [not x for x in bits[::-1]]
  return bits[:length_out]

def checksum(bits):
  while True:
    bits = [a == b for a, b in zip(*[iter(bits)] * 2)]
    if len(bits) % 2 == 1:
      return bits

def solve(bits, length_out):
  bits = grow_bits(bits, length_out)
  bits = checksum(bits)
  return ''.join(str(int(x)) for x in bits)

bits = [c == '1' for c in inp]

answer = solve(bits, 272)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The second disk you have to fill has length <code>35651584</code>. Again using the initial state in your puzzle input, <em>what is the correct checksum</em> for this disk?</p>
# MAGIC </article>

# COMMAND ----------

answer = solve(bits, 35651584)
answer
