# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: Conway Cubes ---</h2><p>As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.</p>
# MAGIC <p>The experimental energy source is based on cutting-edge technology: a set of <span title="Rest in peace, Conway.">Conway</span> Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.</p>
# MAGIC <p>The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (<code>x,y,z</code>), there exists a single cube which is either <em>active</em> or <em>inactive</em>.</p>
# MAGIC <p>In the initial state of the pocket dimension, almost all cubes start <em>inactive</em>. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified <em>active</em> (<code>#</code>) or <em>inactive</em> (<code>.</code>) state.</p>
# MAGIC <p>The energy source then proceeds to boot up by executing six <em>cycles</em>.</p>
# MAGIC <p>Each cube only ever considers its <em>neighbors</em>: any of the 26 other cubes where any of their coordinates differ by at most <code>1</code>. For example, given the cube at <code>x=1,y=2,z=3</code>, its neighbors include the cube at <code>x=2,y=2,z=2</code>, the cube at <code>x=0,y=2,z=3</code>, and so on.</p>
# MAGIC <p>During a cycle, <em>all</em> cubes <em>simultaneously</em> change their state according to the following rules:</p>
# MAGIC <ul>
# MAGIC <li>If a cube is <em>active</em> and <em>exactly <code>2</code> or <code>3</code></em> of its neighbors are also active, the cube remains <em>active</em>. Otherwise, the cube becomes <em>inactive</em>.</li>
# MAGIC <li>If a cube is <em>inactive</em> but <em>exactly <code>3</code></em> of its neighbors are active, the cube becomes <em>active</em>. Otherwise, the cube remains <em>inactive</em>.</li>
# MAGIC </ul>
# MAGIC <p>The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.</p>
# MAGIC <p>For example, consider the following initial state:</p>
# MAGIC <pre><code>.#.
# MAGIC ..#
# MAGIC ###
# MAGIC </code></pre>
# MAGIC <p>Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)</p>
# MAGIC <p>Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given <code>z</code> coordinate (and the frame of view follows the active cells in each cycle):</p>
# MAGIC <pre><code>Before any cycles:
# MAGIC 
# MAGIC z=0
# MAGIC .#.
# MAGIC ..#
# MAGIC ###
# MAGIC 
# MAGIC 
# MAGIC After 1 cycle:
# MAGIC 
# MAGIC z=-1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=0
# MAGIC #.#
# MAGIC .##
# MAGIC .#.
# MAGIC 
# MAGIC z=1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC 
# MAGIC After 2 cycles:
# MAGIC 
# MAGIC z=-2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-1
# MAGIC ..#..
# MAGIC .#..#
# MAGIC ....#
# MAGIC .#...
# MAGIC .....
# MAGIC 
# MAGIC z=0
# MAGIC ##...
# MAGIC ##...
# MAGIC #....
# MAGIC ....#
# MAGIC .###.
# MAGIC 
# MAGIC z=1
# MAGIC ..#..
# MAGIC .#..#
# MAGIC ....#
# MAGIC .#...
# MAGIC .....
# MAGIC 
# MAGIC z=2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC 
# MAGIC After 3 cycles:
# MAGIC 
# MAGIC z=-2
# MAGIC .......
# MAGIC .......
# MAGIC ..##...
# MAGIC ..###..
# MAGIC .......
# MAGIC .......
# MAGIC .......
# MAGIC 
# MAGIC z=-1
# MAGIC ..#....
# MAGIC ...#...
# MAGIC #......
# MAGIC .....##
# MAGIC .#...#.
# MAGIC ..#.#..
# MAGIC ...#...
# MAGIC 
# MAGIC z=0
# MAGIC ...#...
# MAGIC .......
# MAGIC #......
# MAGIC .......
# MAGIC .....##
# MAGIC .##.#..
# MAGIC ...#...
# MAGIC 
# MAGIC z=1
# MAGIC ..#....
# MAGIC ...#...
# MAGIC #......
# MAGIC .....##
# MAGIC .#...#.
# MAGIC ..#.#..
# MAGIC ...#...
# MAGIC 
# MAGIC z=2
# MAGIC .......
# MAGIC .......
# MAGIC ..##...
# MAGIC ..###..
# MAGIC .......
# MAGIC .......
# MAGIC .......
# MAGIC </code></pre>
# MAGIC <p>After the full six-cycle boot process completes, <em><code>112</code></em> cubes are left in the <em>active</em> state.</p>
# MAGIC <p>Starting with your given initial configuration, simulate six cycles. <em>How many cubes are left in the active state after the sixth cycle?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- ".#.####.
.#...##.
..###.##
#..#.#.#
#..#....
#.####..
##.##..#
#.#.#..#
"

# COMMAND ----------

active <-
  input %>%
  read_lines() %>%
  str_locate_all("#") %>%
  imap_dfr(~tibble(x = .x[,'start'], y = .y, z = 0))
active

# COMMAND ----------

neighbors_offset <-
  expand_grid(
    delta_x = seq(from = -1, to = 1, by = 1),
    delta_y = seq(from = -1, to = 1, by = 1),
    delta_z = seq(from = -1, to = 1, by = 1)
  ) %>%
  filter(!(delta_x == 0 & delta_y == 0 & delta_z == 0))
neighbors_offset

# COMMAND ----------

get_neighbors <- function(active) {
  active %>%
    inner_join(neighbors_offset, by = character()) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z
    )
}

sim <- function(active) {
  neighbors <- get_neighbors(active)
  
  new_active1 <- inner_join(
    active,
    neighbors %>% count(x, y, z) %>% filter(n %in% c(2, 3))
  )
  
  new_active2 <- anti_join(
    neighbors %>% count(x, y, z) %>% filter(n == 3),
    active
  )
  
  bind_rows(new_active1, new_active2) %>% distinct() %>% select(-n) # I don't think I need distinct but won't hurt
}

# COMMAND ----------

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

# COMMAND ----------

answer <- nrow(result)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has <em>four spatial dimensions</em>, not three.</p>
# MAGIC <p>The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (<code>x,y,z,w</code>), there exists a single cube (really, a <em>hypercube</em>) which is still either <em>active</em> or <em>inactive</em>.</p>
# MAGIC <p>Each cube only ever considers its <em>neighbors</em>: any of the 80 other cubes where any of their coordinates differ by at most <code>1</code>. For example, given the cube at <code>x=1,y=2,z=3,w=4</code>, its neighbors include the cube at <code>x=2,y=2,z=3,w=3</code>, the cube at <code>x=0,y=2,z=3,w=4</code>, and so on.</p>
# MAGIC <p>The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the <em>number of active neighbors</em> of each cube.</p>
# MAGIC <p>For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)</p>
# MAGIC <p>Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given <code>z</code> and <code>w</code> coordinate:</p>
# MAGIC <pre><code>Before any cycles:
# MAGIC 
# MAGIC z=0, w=0
# MAGIC .#.
# MAGIC ..#
# MAGIC ###
# MAGIC 
# MAGIC 
# MAGIC After 1 cycle:
# MAGIC 
# MAGIC z=-1, w=-1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=0, w=-1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=1, w=-1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=-1, w=0
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=0, w=0
# MAGIC #.#
# MAGIC .##
# MAGIC .#.
# MAGIC 
# MAGIC z=1, w=0
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=-1, w=1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=0, w=1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC z=1, w=1
# MAGIC #..
# MAGIC ..#
# MAGIC .#.
# MAGIC 
# MAGIC 
# MAGIC After 2 cycles:
# MAGIC 
# MAGIC z=-2, w=-2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-1, w=-2
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=0, w=-2
# MAGIC ###..
# MAGIC ##.##
# MAGIC #...#
# MAGIC .#..#
# MAGIC .###.
# MAGIC 
# MAGIC z=1, w=-2
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=2, w=-2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-2, w=-1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-1, w=-1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=0, w=-1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=1, w=-1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=2, w=-1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-2, w=0
# MAGIC ###..
# MAGIC ##.##
# MAGIC #...#
# MAGIC .#..#
# MAGIC .###.
# MAGIC 
# MAGIC z=-1, w=0
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=0, w=0
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=1, w=0
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=2, w=0
# MAGIC ###..
# MAGIC ##.##
# MAGIC #...#
# MAGIC .#..#
# MAGIC .###.
# MAGIC 
# MAGIC z=-2, w=1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-1, w=1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=0, w=1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=1, w=1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=2, w=1
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-2, w=2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=-1, w=2
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=0, w=2
# MAGIC ###..
# MAGIC ##.##
# MAGIC #...#
# MAGIC .#..#
# MAGIC .###.
# MAGIC 
# MAGIC z=1, w=2
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC z=2, w=2
# MAGIC .....
# MAGIC .....
# MAGIC ..#..
# MAGIC .....
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>After the full six-cycle boot process completes, <em><code>848</code></em> cubes are left in the <em>active</em> state.</p>
# MAGIC <p>Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. <em>How many cubes are left in the active state after the sixth cycle?</em></p>
# MAGIC </article>

# COMMAND ----------

active <- active %>% mutate(w = 0)
active

# COMMAND ----------

neighbors_offset <-
  expand_grid(
    delta_x = seq(from = -1, to = 1, by = 1),
    delta_y = seq(from = -1, to = 1, by = 1),
    delta_z = seq(from = -1, to = 1, by = 1),
    delta_w = seq(from = -1, to = 1, by = 1)
  ) %>%
  filter(!(delta_x == 0 & delta_y == 0 & delta_z == 0 & delta_w == 0))
neighbors_offset

# COMMAND ----------

get_neighbors <- function(active) {
  active %>%
    inner_join(neighbors_offset, by = character()) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z,
      w = w + delta_w
    )
}

sim <- function(active) {
  neighbors <- get_neighbors(active)
  
  new_active1 <- inner_join(
    active,
    neighbors %>% count(x, y, z, w) %>% filter(n %in% c(2, 3))
  )
  
  new_active2 <- anti_join(
    neighbors %>% count(x, y, z, w) %>% filter(n == 3),
    active
  )
  
  bind_rows(new_active1, new_active2) %>% distinct() %>% select(-n) # I don't think I need distinct but won't hurt
}

# COMMAND ----------

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

# COMMAND ----------

answer <- nrow(result)
answer
