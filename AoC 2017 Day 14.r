# Databricks notebook source
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

# install.packages("binaryLogic")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "nbysizxe"

# COMMAND ----------

hash_step <- function(nums, lengths) {
  skip_size <- 0
  w_total <- 0
  for (l in lengths) {
    nums[seq_len(l)] <- nums[rev(seq_len(l))]

    w <- l + skip_size
    while (w > length(nums)) w <- w - length(nums)

    nums <- c(
      tail(nums, -w),
      head(nums, w)
    )
    skip_size <- skip_size + 1
    w_total <- w_total + w
  }
  while (w_total > length(nums)) w_total <- w_total - length(nums)
  lst(nums, w_total)
  c(
    tail(nums, w_total),
    head(nums, -w_total)
  )
}

hash <- function(x, nums = seq(from = 0, to = 255, by = 1)) {
  lengths <- rep(
    c(utf8ToInt(x), 17, 31, 73, 47, 23),
    64
  )
  
  result <- hash_step(nums, lengths)
  
  result %>%
    enframe() %>%
    mutate(name = (name - 1) %/% 16) %>%
    group_by(name) %>%
    summarise(
      output = reduce(value, bitwXor),
      hex = format(as.hexmode(output), width = 2)
    ) %>%
    pull(hex) %>%
    str_c(collapse = "")
}

# COMMAND ----------

get_row <- function(i, key) {
  str_c(key, "-", i) %>%
    hash() %>%
    str_split("") %>%
    first() %>%
    as.hexmode() %>%
    binaryLogic::as.binary(n = 4) %>%
    unlist()
}

get_grid <- function(key) {
  map(seq(from = 0, to = 127, by = 1), get_row, key)
}

# COMMAND ----------

grid <- get_grid(input)

# COMMAND ----------

answer <- grid %>% unlist() %>% sum()
answer

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

set_group <- function(row, col) {
  if (visited[row, col] || !m[row, col]) return(NULL)
  
  visited[row, col] <<- TRUE
  
  result <- c(
      if (row > 1) group[row - 1, col],
      if (row < nrow(group)) group[row + 1, col],
      if (col > 1) group[row, col - 1],
      if (col < ncol(group)) group[row, col + 1]
    ) %>% max(na.rm = TRUE)
  if (!is.finite(result)) {
    result <- max(group, na.rm = TRUE) + 1
    if (!is.finite(result)) result <- 1
  }
  group[row, col] <<- result
  if (row > 1) set_group(row - 1, col)
  if (row < nrow(group)) set_group(row + 1, col)
  if (col > 1) set_group(row, col - 1)
  if (col < ncol(group)) set_group(row, col + 1)
  
  NULL
}

# COMMAND ----------

m <- simplify2array(grid) %>% t()

visited <- m
visited[] <- FALSE

group <- m
group[] <- NA

for (row in seq_len(nrow(m))) {
  for (col in seq_len(ncol(m))) {
    set_group(row, col)
  }
}

# COMMAND ----------

answer <- max(group, na.rm = TRUE)
answer
