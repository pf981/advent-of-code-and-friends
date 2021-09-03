# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/1

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 1: No Time for a Taxicab ---</h2><p>Santa's sleigh uses a <span title="An atomic clock is too inaccurate; he might end up in a wall!">very high-precision clock</span> to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny.  To save Christmas, Santa needs you to retrieve all <em class="star">fifty stars</em> by December 25th.</p>
# MAGIC <p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
# MAGIC <p>You're airdropped near <em>Easter Bunny Headquarters</em> in a city somewhere.  "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.</p>
# MAGIC <p>The Document indicates that you should start at the given coordinates (where you just landed) and face North.  Then, follow the provided sequence: either turn left (<code>L</code>) or right (<code>R</code>) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.</p>
# MAGIC <p>There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination.  Given that you can only walk on the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">street grid of the city</a>, how far is the shortest path to the destination?</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>Following <code>R2, L3</code> leaves you <code>2</code> blocks East and <code>3</code> blocks North, or <code>5</code> blocks away.</li>
# MAGIC <li><code>R2, R2, R2</code> leaves you <code>2</code> blocks due South of your starting position, which is <code>2</code> blocks away.</li>
# MAGIC <li><code>R5, L5, R5, R3</code> leaves you <code>12</code> blocks away.</li>
# MAGIC </ul>
# MAGIC <p><em>How many blocks away</em> is Easter Bunny HQ?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"

# COMMAND ----------

x_coef <- c(0, 1, 0, -1)
y_coef <- c(1, 0, -1, 0)

directions <-
  tibble(instruction = str_split(input, ", ") %>% first()) %>%
  transmute(
    turn = str_extract(instruction, "[A-Z]"),
    d = str_extract(instruction, "\\d+") %>% parse_integer(),
    heading = cumsum(ifelse(turn == "R", 1, -1)) %% 4 + 1,
    x = cumsum(x_coef[heading] * d),
    y = cumsum(y_coef[heading] * d),
    blocks = abs(x) + abs(y)
  )

directions

# COMMAND ----------

directions %>%
  slice(n()) %>%
  pull(blocks)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Then, you notice the instructions continue on the back of the Recruiting Document.  Easter Bunny HQ is actually at the first location you visit twice.</p>
# MAGIC <p>For example, if your instructions are <code>R8, R4, R4, R8</code>, the first location you visit twice is <code>4</code> blocks away, due East.</p>
# MAGIC <p>How many blocks away is the <em>first location you visit twice</em>?</p>
# MAGIC </article>

# COMMAND ----------

directions %>%
  mutate(d = map(d, ~rep(1, .))) %>%
  unnest() %>%
  mutate(
    x = cumsum(x_coef[heading] * d),
    y = cumsum(y_coef[heading] * d),
    blocks = abs(x) + abs(y)
  ) %>%
  group_by(x, y) %>%
  filter(n() > 1) %>%
  ungroup() %>%
  slice(1) %>%
  pull(blocks)
