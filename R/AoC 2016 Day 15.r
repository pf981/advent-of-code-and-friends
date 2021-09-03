# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/15

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 15: Timing is Everything ---</h2><p>The halls open into an interior plaza containing a large kinetic sculpture. The sculpture is in a sealed enclosure and seems to involve a set of identical spherical capsules that are carried to the top and allowed to <a href="https://youtu.be/IxDoO9oODOk?t=177">bounce through the maze</a> of spinning pieces.</p>
# MAGIC <p>Part of the sculpture is even interactive! When a button is pressed, a capsule is dropped and tries to fall through slots in a set of rotating discs to finally go through a little hole at the bottom and come out of the sculpture. If any of the slots aren't aligned with the capsule as it passes, the capsule bounces off the disc and soars away. You feel compelled to <span title="These machines are everywhere in Japan, but on a MUCH smaller scale.">get one of those capsules</span>.</p>
# MAGIC <p>The discs pause their motion each second and come in different sizes; they seem to each have a fixed number of positions at which they stop.  You decide to call the position with the slot <code>0</code>, and count up for each position it reaches next.</p>
# MAGIC <p>Furthermore, the discs are spaced out so that after you push the button, one second elapses before the first disc is reached, and one second elapses as the capsule passes from one disc to the one below it.  So, if you push the button at <code>time=100</code>, then the capsule reaches the top disc at <code>time=101</code>, the second disc at <code>time=102</code>, the third disc at <code>time=103</code>, and so on.</p>
# MAGIC <p>The button will only drop a capsule at an integer time - no fractional seconds allowed.</p>
# MAGIC <p>For example, at <code>time=0</code>, suppose you see the following arrangement:</p>
# MAGIC <pre><code>Disc #1 has 5 positions; at time=0, it is at position 4.
# MAGIC Disc #2 has 2 positions; at time=0, it is at position 1.
# MAGIC </code></pre>
# MAGIC <p>If you press the button exactly at <code>time=0</code>, the capsule would start to fall; it would reach the first disc at <code>time=1</code>. Since the first disc was at position <code>4</code> at <code>time=0</code>, by <code>time=1</code> it has ticked one position forward.  As a five-position disc, the next position is <code>0</code>, and the capsule falls through the slot.</p>
# MAGIC <p>Then, at <code>time=2</code>, the capsule reaches the second disc. The second disc has ticked forward two positions at this point: it started at position <code>1</code>, then continued to position <code>0</code>, and finally ended up at position <code>1</code> again.  Because there's only a slot at position <code>0</code>, the capsule bounces away.</p>
# MAGIC <p>If, however, you wait until <code>time=5</code> to push the button, then when the capsule reaches each disc, the first disc will have ticked forward <code>5+1 = 6</code> times (to position <code>0</code>), and the second disc will have ticked forward <code>5+2 = 7</code> times (also to position <code>0</code>). In this case, the capsule would fall through the discs and come out of the machine.</p>
# MAGIC <p>However, your situation has more than two discs; you've noted their positions in your puzzle input. What is the <em>first time you can press the button</em> to get a capsule?</p>
# MAGIC </article>

# COMMAND ----------

# install.packages("DescTools")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0.
"

# COMMAND ----------

# input <- "Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.
# "

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    disc = str_extract(line, "\\d+") %>% parse_integer(),
    positions = str_extract(line, "\\d+(?= positions)") %>% parse_integer(),
    start_position = str_extract(line, "\\d+(?=\\.)") %>% parse_integer()
  )

total_positions <- DescTools::LCM(df$positions)

df <-
  df %>%
  mutate(
    step_size = total_positions / positions,
    true_start = step_size * (start_position + disc)
  )

lst(total_positions, df)

# COMMAND ----------

create_f <- function(true_start, step_size, total_positions) {
  function(t) {
    (true_start + step_size * t) %% total_positions == 0
  }
}

# COMMAND ----------

fs <-
  df %>%
  mutate(
    f = pmap(lst(true_start, step_size, total_positions), create_f)
  ) %>%
  pull(f)

fs

# COMMAND ----------

t <- 1
repeat {
  if (all(map_lgl(fs, ~.(t)))) {
    break
  }
  t <- t + 1
}
t

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.</p>
# MAGIC <p>When it's done, the discs are back in their original configuration as if it were <code>time=0</code> again, but a new disc with <code>11</code> positions and starting at position <code>0</code> has appeared exactly one second below the previously-bottom disc.</p>
# MAGIC <p>With this new disc, and counting again starting from <code>time=0</code> with the configuration in your puzzle input, what is the <em>first time you can press the button</em> to get another capsule?</p>
# MAGIC </article>

# COMMAND ----------

df <-
  tibble(
    line = c(
      read_lines(input),
      "Disc #7 has 11 positions; at time=0, it is at position 0."
    )
  ) %>%
  mutate(
    disc = str_extract(line, "\\d+") %>% parse_integer(),
    positions = str_extract(line, "\\d+(?= positions)") %>% parse_integer(),
    start_position = str_extract(line, "\\d+(?=\\.)") %>% parse_integer()
  )

total_positions <- DescTools::LCM(df$positions)

df <-
  df %>%
  mutate(
    step_size = total_positions / positions,
    true_start = step_size * (start_position + disc)
  )

lst(total_positions, df)

# COMMAND ----------

fs <-
  df %>%
  mutate(
    f = pmap(lst(true_start, step_size, total_positions), create_f)
  ) %>%
  pull(f)

fs

# COMMAND ----------

t <- 1
repeat {
  if (all(map_lgl(fs, ~.(t)))) {
    break
  }
  t <- t + 1
}
t
