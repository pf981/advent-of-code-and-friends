# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/17
# MAGIC 
# MAGIC <main>
# MAGIC <style>article *[title]{border-bottom:1px dotted #ffff66;}</style><script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 17: Conway Cubes ---</h2><p>As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.</p>
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
# MAGIC <p>Your puzzle answer was <code>276</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has <em>four spatial dimensions</em>, not three.</p>
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
# MAGIC <p>Your puzzle answer was <code>2136</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
# MAGIC <p>At this point, all that is left is for you to <a href="/2020">admire your Advent calendar</a>.</p>
# MAGIC <p>If you still want to see it, you can <a href="17/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Conway+Cubes%22+%2D+Day+17+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F17&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Conway+Cubes%22+%2D+Day+17+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F17'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

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

# input <- ".#.
# ..#
# ###
# "

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

cross_join <- function(a, b) {
  full_join(
    a %>% add_column(.dummy = TRUE),
    b %>% add_column(.dummy = TRUE),
    by = ".dummy"
  ) %>%
   select(-.dummy)
}

# COMMAND ----------

get_neighbors <- function(active) {
  active %>%
    cross_join(neighbors_offset) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z
    )
}

# COMMAND ----------

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

print_slice <- function(active) {
  cat(paste0("\n\nz=", active$z[[1]], "\n"))
  active <-
    active %>%
    mutate(
      x = x - min(x) + 1,
      y = y - min(y) + 1
    )
  m <- matrix(".", nrow = max(active$x), ncol = max(active$y))
  m[cbind(active$x, active$y)] <- "#"
  cat(apply(m, 2, paste0, collapse = "") %>% paste0(collapse = "\n"))
}

# COMMAND ----------

print_state <- function(active) {
  for (cur_z in sort(unique(active$z))) {
    active %>%
      filter(z == cur_z) %>%
      print_slice()
  }
  invisible()
}

# COMMAND ----------

print_state(active)

# COMMAND ----------

print_state(sim(active))

# COMMAND ----------

print_state(sim(sim(active)))

# COMMAND ----------

print_state(sim(sim(sim(active))))

# COMMAND ----------

# v <- sim(active)
# get_neighbors(v) %>%
#   count(x, y, z) %>%
#   ggplot(aes(x, y, label = n)) +
#     geom_label() +
#     geom_point(data = v, color = "red", alpha = 0.5, size = 8) +
#     facet_grid(~z) +
#     scale_y_reverse()
# # This looks correct

# COMMAND ----------

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

# COMMAND ----------

nrow(result)

# COMMAND ----------

# MAGIC %md ## Part 2

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
    cross_join(neighbors_offset) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z,
      w = w + delta_w
    )
}

# COMMAND ----------

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

print_state(sim(active) %>% mutate(z = paste(z, w)))

# COMMAND ----------

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

# COMMAND ----------

nrow(result)