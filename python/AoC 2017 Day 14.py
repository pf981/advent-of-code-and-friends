# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/14

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 14: Disk Defragmentation ---</h2><p>Suddenly, a scheduled job activates the system's <a href="https://en.wikipedia.org/wiki/Defragmentation">disk defragmenter</a>. Were the situation different, you might <a href="https://www.youtube.com/watch?v=kPv1gQ5Rs8A&amp;t=37">sit and watch it for a while</a>, but today, you just don't have that kind of time. It's soaking up valuable system resources that are needed elsewhere, and so the only option is to help it finish its task as soon as possible.</p>
# MAGIC <p>The disk in question consists of a 128x128 grid; each square of the grid is either <em>free</em> or <em>used</em>. On this disk, the state of the grid is tracked by the bits in a sequence of <a href="10">knot hashes</a>.</p>
# MAGIC <p>A total of 128 knot hashes are calculated, each corresponding to a single row in the grid; each hash contains 128 bits which correspond to individual grid squares. Each bit of a hash indicates whether that square is <em>free</em> (<code>0</code>) or <em>used</em> (<code>1</code>).</p>
# MAGIC <p>The hash inputs are a key string (your puzzle input), a dash, and a number from <code>0</code> to <code>127</code> corresponding to the row.  For example, if your key string were <code>flqrgnkx</code>, then the first row would be given by the bits of the knot hash of <code>flqrgnkx-0</code>, the second row from the bits of the knot hash of <code>flqrgnkx-1</code>, and so on until the last row, <code>flqrgnkx-127</code>.</p>
# MAGIC <p>The output of a knot hash is traditionally represented by 32 hexadecimal digits; each of these digits correspond to 4 bits, for a total of <code>4 * 32 = 128</code> bits. To convert to bits, turn each hexadecimal digit to its equivalent binary value, high-bit first: <code>0</code> becomes <code>0000</code>, <code>1</code> becomes <code>0001</code>, <code>e</code> becomes <code>1110</code>, <code>f</code> becomes <code>1111</code>, and so on; a hash that begins with <code>a0c2017...</code> in hexadecimal would begin with <code>10100000110000100000000101110000...</code> in binary.</p>
# MAGIC <p>Continuing this process, the <em>first 8 rows and columns</em> for key <code>flqrgnkx</code> appear as follows, using <code>#</code> to denote used squares, and <code>.</code> to denote free ones:</p>
# MAGIC <pre><code>##.#.#..--&gt;
# MAGIC .#.#.#.#   
# MAGIC ....#.#.   
# MAGIC #.#.##.#   
# MAGIC .##.#...   
# MAGIC ##..#..#   
# MAGIC .#...#..   
# MAGIC ##.#.##.--&gt;
# MAGIC |      |   
# MAGIC V      V   
# MAGIC </code></pre>
# MAGIC <p>In this example, <code>8108</code> squares are used across the entire 128x128 grid.</p>
# MAGIC <p>Given your actual key string, <em>how many squares are used</em>?</p>
# MAGIC </article>

# COMMAND ----------

inp = 'nbysizxe'

# COMMAND ----------

import collections
import functools
import math
import operator


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


def get_knot_hash(s):
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    sparse_hash = hash_lengths(lengths, n_rounds=64)
    dense_hash = [
        functools.reduce(operator.xor, l) for l in zip(*[iter(sparse_hash)] * 16)
    ]
    return ''.join(f'{i:0>8b}' for i in dense_hash)


def get_grid(s):
    grid = collections.defaultdict(bool)
    for row in range(128):
        for col, value in enumerate(get_knot_hash(f'{s}-{row}')):
            if value == '1':
                grid[(row, col)] = True
    return grid


grid = get_grid(inp)

answer = sum(grid.values())
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, <span title="This is exactly how it works in real life.">all the defragmenter needs to know</span> is the number of <em>regions</em>. A region is a group of <em>used</em> squares that are all <em>adjacent</em>, not including diagonals. Every used square is in exactly one region: lone used squares form their own isolated regions, while several adjacent squares all count as a single region.</p>
# MAGIC <p>In the example above, the following nine regions are visible, each marked with a distinct digit:</p>
# MAGIC <pre><code>11.2.3..--&gt;
# MAGIC .1.2.3.4   
# MAGIC ....5.6.   
# MAGIC 7.8.55.9   
# MAGIC .88.5...   
# MAGIC 88..5..8   
# MAGIC .8...8..   
# MAGIC 88.8.88.--&gt;
# MAGIC |      |   
# MAGIC V      V   
# MAGIC </code></pre>
# MAGIC <p>Of particular interest is the region marked <code>8</code>; while it does not appear contiguous in this small view, all of the squares marked <code>8</code> are connected when considering the whole 128x128 grid. In total, in this example, <code>1242</code> regions are present.</p>
# MAGIC <p><em>How many regions</em> are present given your key string?</p>
# MAGIC </article>

# COMMAND ----------

def set_group(groups, grid, row, col):
    if not grid[(row, col)] or groups.get((row, col)):
        return

    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
    group = functools.reduce(
        (lambda a, b: a or b), (groups.get((row + dr, col + dc)) for dr, dc in offsets)
    )
    groups[(row, col)] = group or max(groups.values() or [0]) + 1

    for dr, dc in offsets:
        set_group(groups, grid, row + dr, col + dc)


groups = {}
for row in range(128):
    for col in range(128):
        set_group(groups, grid, row, col)

answer = len(set(groups.values()))
print(answer)
