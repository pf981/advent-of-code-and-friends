# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 21: Fractal Art ---</h2><p>You find a program trying to generate some art. It uses a strange process that involves <span title="This technique is also often used on TV.">repeatedly enhancing</span> the detail of an image through a set of rules.</p>
# MAGIC <p>The image consists of a two-dimensional square grid of pixels that are either on (<code>#</code>) or off (<code>.</code>). The program always begins with this pattern:</p>
# MAGIC <pre><code>.#.
# MAGIC ..#
# MAGIC ###
# MAGIC </code></pre>
# MAGIC <p>Because the pattern is both <code>3</code> pixels wide and <code>3</code> pixels tall, it is said to have a <em>size</em> of <code>3</code>.</p>
# MAGIC <p>Then, the program repeats the following process:</p>
# MAGIC <ul>
# MAGIC <li>If the size is evenly divisible by <code>2</code>, break the pixels up into <code>2x2</code> squares, and convert each <code>2x2</code> square into a <code>3x3</code> square by following the corresponding <em>enhancement rule</em>.</li>
# MAGIC <li>Otherwise, the size is evenly divisible by <code>3</code>; break the pixels up into <code>3x3</code> squares, and convert each <code>3x3</code> square into a <code>4x4</code> square by following the corresponding <em>enhancement rule</em>.</li>
# MAGIC </ul>
# MAGIC <p>Because each square of pixels is replaced by a larger one, the image gains pixels and so its <em>size</em> increases.</p>
# MAGIC <p>The artist's book of enhancement rules is nearby (your puzzle input); however, it seems to be missing rules.  The artist explains that sometimes, one must <em>rotate</em> or <em>flip</em> the input pattern to find a match. (Never rotate or flip the output pattern, though.) Each pattern is written concisely: rows are listed as single units, ordered top-down, and separated by slashes. For example, the following rules correspond to the adjacent patterns:</p>
# MAGIC <pre><code>../.#  =  ..
# MAGIC           .#
# MAGIC 
# MAGIC                 .#.
# MAGIC .#./..#/###  =  ..#
# MAGIC                 ###
# MAGIC 
# MAGIC                         #..#
# MAGIC #..#/..../#..#/.##.  =  ....
# MAGIC                         #..#
# MAGIC                         .##.
# MAGIC </code></pre>
# MAGIC <p>When searching for a rule to use, rotate and flip the pattern as necessary.  For example, all of the following patterns match the same rule:</p>
# MAGIC <pre><code>.#.   .#.   #..   ###
# MAGIC ..#   #..   #.#   ..#
# MAGIC ###   ###   ##.   .#.
# MAGIC </code></pre>
# MAGIC <p>Suppose the book contained the following two rules:</p>
# MAGIC <pre><code>../.# =&gt; ##./#../...
# MAGIC .#./..#/### =&gt; #..#/..../..../#..#
# MAGIC </code></pre>
# MAGIC <p>As before, the program begins with this pattern:</p>
# MAGIC <pre><code>.#.
# MAGIC ..#
# MAGIC ###
# MAGIC </code></pre>
# MAGIC <p>The size of the grid (<code>3</code>) is not divisible by <code>2</code>, but it is divisible by <code>3</code>. It divides evenly into a single square; the square matches the second rule, which produces:</p>
# MAGIC <pre><code>#..#
# MAGIC ....
# MAGIC ....
# MAGIC #..#
# MAGIC </code></pre>
# MAGIC <p>The size of this enhanced grid (<code>4</code>) is evenly divisible by <code>2</code>, so that rule is used. It divides evenly into four squares:</p>
# MAGIC <pre><code>#.|.#
# MAGIC ..|..
# MAGIC --+--
# MAGIC ..|..
# MAGIC #.|.#
# MAGIC </code></pre>
# MAGIC <p>Each of these squares matches the same rule (<code>../.# =&gt; ##./#../...</code>), three of which require some flipping and rotation to line up with the rule. The output for the rule is the same in all four cases:</p>
# MAGIC <pre><code>##.|##.
# MAGIC #..|#..
# MAGIC ...|...
# MAGIC ---+---
# MAGIC ##.|##.
# MAGIC #..|#..
# MAGIC ...|...
# MAGIC </code></pre>
# MAGIC <p>Finally, the squares are joined into a new grid:</p>
# MAGIC <pre><code>##.##.
# MAGIC #..#..
# MAGIC ......
# MAGIC ##.##.
# MAGIC #..#..
# MAGIC ......
# MAGIC </code></pre>
# MAGIC <p>Thus, after <code>2</code> iterations, the grid contains <code>12</code> pixels that are <em>on</em>.</p>
# MAGIC <p><em>How many pixels stay on</em> after <code>5</code> iterations?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "../.. => ..#/#../.#.
#./.. => #../#../...
##/.. => ###/#.#/#..
.#/#. => ###/##./.#.
##/#. => .../.#./..#
##/## => ##./#.#/###
.../.../... => ##../.#../#.#./....
#../.../... => ..../##.#/...#/##.#
.#./.../... => ###./####/#.../#..#
##./.../... => ###./.##./...#/..##
#.#/.../... => .###/.##./#.../#.##
###/.../... => ##.#/#..#/#.#./#.##
.#./#../... => #.#./.###/#.../#.##
##./#../... => #.../####/#.##/....
..#/#../... => #.##/..#./...#/...#
#.#/#../... => #.##/####/.#.#/#.#.
.##/#../... => #.../##../##.#/.##.
###/#../... => ..../#.#./.###/#...
.../.#./... => .#.#/#..#/##../#.##
#../.#./... => ###./.###/.#.#/..#.
.#./.#./... => ..##/.##./..##/.#.#
##./.#./... => ..#./##../###./...#
#.#/.#./... => ..##/.##./.###/###.
###/.#./... => ..#./.###/###./#.##
.#./##./... => ###./..../.#../#...
##./##./... => .#.#/##../##.#/...#
..#/##./... => ##.#/.##./.###/..##
#.#/##./... => .###/..#./#.##/####
.##/##./... => ##.#/..#./..##/###.
###/##./... => ..../.#.#/.#../#...
.../#.#/... => ###./.#.#/.#../#.##
#../#.#/... => ####/#..#/..../....
.#./#.#/... => #.../..##/#.##/#.#.
##./#.#/... => #.#./###./##../#.#.
#.#/#.#/... => ...#/.##./.##./.#..
###/#.#/... => ..../.##./####/#.#.
.../###/... => .###/.#../.###/#.##
#../###/... => ..##/..##/.##./##..
.#./###/... => .#.#/..#./..##/##.#
##./###/... => ...#/#.##/#.#./##.#
#.#/###/... => #.##/.##./...#/###.
###/###/... => ##../...#/..##/####
..#/.../#.. => #.##/#.../.#../#.#.
#.#/.../#.. => .##./.##./.#.#/.##.
.##/.../#.. => .#.#/#.##/...#/##.#
###/.../#.. => ##../..#./...#/##..
.##/#../#.. => ##../..##/#..#/#..#
###/#../#.. => ##../..#./#.#./....
..#/.#./#.. => .##./##.#/##../####
#.#/.#./#.. => ####/...#/.#.#/..#.
.##/.#./#.. => .#.#/..#./##.#/.#..
###/.#./#.. => #.../#.##/..../##.#
.##/##./#.. => #.#./#.#./#.##/#.#.
###/##./#.. => ...#/###./.##./.#.#
#../..#/#.. => ####/####/..../.##.
.#./..#/#.. => #.##/...#/..#./####
##./..#/#.. => ..#./#.../..##/####
#.#/..#/#.. => #.../#.##/#.##/..##
.##/..#/#.. => ####/..../##../####
###/..#/#.. => ..../##.#/.##./####
#../#.#/#.. => ...#/..##/###./#..#
.#./#.#/#.. => #..#/..#./.###/##.#
##./#.#/#.. => ###./####/#.##/..#.
..#/#.#/#.. => ##../##.#/..##/.##.
#.#/#.#/#.. => .#.#/.##./#.../##.#
.##/#.#/#.. => .#.#/#..#/.##./..#.
###/#.#/#.. => ...#/.#../.##./##.#
#../.##/#.. => ###./##../#.#./####
.#./.##/#.. => .#../##../#.#./.#.#
##./.##/#.. => ##.#/.#../.#.#/####
#.#/.##/#.. => ####/.#.#/..../....
.##/.##/#.. => ####/##../#..#/####
###/.##/#.. => .###/##.#/.#../#.##
#../###/#.. => #..#/###./####/.#.#
.#./###/#.. => ..##/##../##.#/.#.#
##./###/#.. => #..#/.#../####/...#
..#/###/#.. => ##../##.#/...#/#..#
#.#/###/#.. => ..#./.##./#..#/....
.##/###/#.. => #..#/#.../..../.#..
###/###/#.. => ..#./#.##/.##./#...
.#./#.#/.#. => .#.#/.##./##.#/.##.
##./#.#/.#. => #..#/.###/.#.#/.##.
#.#/#.#/.#. => #.../##../#.../.###
###/#.#/.#. => ###./.###/###./....
.#./###/.#. => .#../####/...#/##..
##./###/.#. => ####/###./..../....
#.#/###/.#. => ...#/.###/..../####
###/###/.#. => ..../#.../..#./.###
#.#/..#/##. => #.#./#.../####/#.##
###/..#/##. => .#.#/#..#/.###/#...
.##/#.#/##. => ..##/..#./..../##..
###/#.#/##. => #.#./##.#/####/#..#
#.#/.##/##. => ..../.#../#.#./##.#
###/.##/##. => ..../..../.#../##.#
.##/###/##. => #.#./.###/#.#./#.##
###/###/##. => ##.#/##.#/.###/..#.
#.#/.../#.# => #..#/.#../#.../...#
###/.../#.# => ##../.#../##.#/..#.
###/#../#.# => ..##/#.#./####/.#..
#.#/.#./#.# => ...#/...#/#..#/#.#.
###/.#./#.# => ..../####/.##./.#.#
###/##./#.# => #..#/.#.#/..##/####
#.#/#.#/#.# => #.#./..#./...#/.#..
###/#.#/#.# => ...#/##.#/.###/.#..
#.#/###/#.# => .#.#/###./.#../.##.
###/###/#.# => ...#/.###/.#.#/###.
###/#.#/### => #.##/.#.#/...#/.#..
###/###/### => ..##/.#../#.#./.#..
"

# COMMAND ----------

# input <- "../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#
# "

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("from", "to"))
df

# COMMAND ----------

flip_x <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    stringi::stri_reverse() %>%
    str_c(collapse = "/")
}

flip_y <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    rev() %>%
    str_c(collapse = "/")
}

# Counter-clockwise
rotate <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    str_split("") %>%
    map(rev) %>%
    simplify2array() %>%
    asplit(1) %>%
    map_chr(str_c, collapse = "") %>%
    str_c(collapse = "/")
}

rotate_n <- function(s, n) {
  for (i in seq_len(n)) {
    s <- rotate(s)
  }
  s
}

# COMMAND ----------

df <- df %>% rowwise()
df <-
  bind_rows(
    df,
    df %>% mutate(from = from %>% flip_x()),
    df %>% mutate(from = from %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(1)),
    df %>% mutate(from = from %>% rotate_n(2)),
    df %>% mutate(from = from %>% rotate_n(3)),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x() %>% flip_y())
  ) %>%
  ungroup()
df

# COMMAND ----------

enhance <- function(s) {
  df$to[which(df$from == s)[1]]
}

break_rows <- function(s, break_size) {
  s %>%
    str_split("/") %>%
    first() %>%
    enframe() %>%
    mutate(name = (name - 1) %/% break_size) %>%
    group_by(name) %>%
    summarise(value = str_c(value, collapse = "/")) %>%
    pull(value)
}

break_cols <- function(s, break_size) {
  s %>%
    str_split("/") %>%
    first() %>%
    map(str_extract_all, str_c(".{", break_size, "}")) %>%
    pmap(str_c, sep = "/") %>%
    unlist()
}

break_pixels <- function(s) {
  rows <- str_count(s, "/") + 1
  
  if (rows %% 2 == 0) {
    break_size <- 2
  } else if (rows %% 3 == 0) {
    break_size <- 3
  } else {
    stop(str_c("Unable to break rows: ", rows))
  }
  
  s %>%
    break_rows(break_size) %>%
    map(break_cols, break_size)
}

combine_rows <- function(s_vec) {
  str_c(s_vec, collapse = "/")
}

combine_cols <- function(s_vec) {
  s_vec %>%
    str_split("/") %>%
    pmap_chr(str_c, collapse = "") %>%
    str_c(collapse = "/")
}

combine_pixels <- function(s_grid) {
  s_grid %>% map_chr(combine_cols) %>% combine_rows()
}

simulate <- function(n, s = ".#./..#/###") {
  for (i in seq_len(n)) {
    s <-
      s %>%
      break_pixels() %>%
      map(map_chr, enhance) %>%
      combine_pixels()
  }
  s
}

# COMMAND ----------

result <- simulate(5)
answer <- str_count(result, "#")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many pixels stay on</em> after <code>18</code> iterations?</p>
# MAGIC </article>

# COMMAND ----------

result <- simulate(18)
answer <- str_count(result, "#")
answer
