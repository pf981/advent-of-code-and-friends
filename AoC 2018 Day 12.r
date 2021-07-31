# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 12: Subterranean Sustainability ---</h2><p>The year 518 is significantly more underground than your history books implied.  Either that, or you've arrived in a <span title="It's probably this one. Can never be too sure, though.">vast cavern network</span> under the North Pole.</p>
# MAGIC <p>After exploring a little, you discover a long tunnel that contains a row of small pots as far as you can see to your left and right.  A few of them contain plants - someone is trying to grow things in these geothermally-heated caves.</p>
# MAGIC <p>The pots are numbered, with <code>0</code> in front of you.  To the left, the pots are numbered <code>-1</code>, <code>-2</code>, <code>-3</code>, and so on; to the right, <code>1</code>, <code>2</code>, <code>3</code>.... Your puzzle input contains a list of pots from <code>0</code> to the right and whether they do (<code>#</code>) or do not (<code>.</code>) currently contain a plant, the <em>initial state</em>. (No other pots currently contain plants.) For example, an initial state of <code>#..##....</code> indicates that pots <code>0</code>, <code>3</code>, and <code>4</code> currently contain plants.</p>
# MAGIC <p>Your puzzle input also contains some notes you find on a nearby table: someone has been trying to figure out how these plants <em>spread</em> to nearby pots.  Based on the notes, for each generation of plants, a given pot has or does not have a plant based on whether that pot (and the two pots on either side of it) had a plant in the last generation. These are written as <code>LLCRR =&gt; N</code>, where <code>L</code> are pots to the left, <code>C</code> is the current pot being considered, <code>R</code> are the pots to the right, and <code>N</code> is whether the current pot will have a plant in the next generation. For example:</p>
# MAGIC <ul>
# MAGIC <li>A note like <code>..#.. =&gt; .</code> means that a pot that contains a plant but with no plants within two pots of it will not have a plant in it during the next generation.</li>
# MAGIC <li>A note like <code>##.## =&gt; .</code> means that an empty pot with two plants on each side of it will remain empty in the next generation.</li>
# MAGIC <li>A note like <code>.##.# =&gt; #</code> means that a pot has a plant in a given generation if, in the previous generation, there were plants in that pot, the one immediately to the left, and the one two pots to the right, but not in the ones immediately to the right and two to the left.</li>
# MAGIC </ul>
# MAGIC <p>It's not clear what these plants are for, but you're sure it's important, so you'd like to make sure the current configuration of plants is sustainable by determining what will happen after <em><code>20</code> generations</em>.</p>
# MAGIC <p>For example, given the following input:</p>
# MAGIC <pre><code>initial state: #..#.#..##......###...###
# MAGIC 
# MAGIC ...## =&gt; #
# MAGIC ..#.. =&gt; #
# MAGIC .#... =&gt; #
# MAGIC .#.#. =&gt; #
# MAGIC .#.## =&gt; #
# MAGIC .##.. =&gt; #
# MAGIC .#### =&gt; #
# MAGIC #.#.# =&gt; #
# MAGIC #.### =&gt; #
# MAGIC ##.#. =&gt; #
# MAGIC ##.## =&gt; #
# MAGIC ###.. =&gt; #
# MAGIC ###.# =&gt; #
# MAGIC ####. =&gt; #
# MAGIC </code></pre>
# MAGIC <p>For brevity, in this example, only the combinations which do produce a plant are listed. (Your input includes all possible combinations.) Then, the next 20 generations will look like this:</p>
# MAGIC <pre><code>                 1         2         3     
# MAGIC        0         0         0         0     
# MAGIC  0: ...#..#.#..##......###...###...........
# MAGIC  1: ...#...#....#.....#..#..#..#...........
# MAGIC  2: ...##..##...##....#..#..#..##..........
# MAGIC  3: ..#.#...#..#.#....#..#..#...#..........
# MAGIC  4: ...#.#..#...#.#...#..#..##..##.........
# MAGIC  5: ....#...##...#.#..#..#...#...#.........
# MAGIC  6: ....##.#.#....#...#..##..##..##........
# MAGIC  7: ...#..###.#...##..#...#...#...#........
# MAGIC  8: ...#....##.#.#.#..##..##..##..##.......
# MAGIC  9: ...##..#..#####....#...#...#...#.......
# MAGIC 10: ..#.#..#...#.##....##..##..##..##......
# MAGIC 11: ...#...##...#.#...#.#...#...#...#......
# MAGIC 12: ...##.#.#....#.#...#.#..##..##..##.....
# MAGIC 13: ..#..###.#....#.#...#....#...#...#.....
# MAGIC 14: ..#....##.#....#.#..##...##..##..##....
# MAGIC 15: ..##..#..#.#....#....#..#.#...#...#....
# MAGIC 16: .#.#..#...#.#...##...#...#.#..##..##...
# MAGIC 17: ..#...##...#.#.#.#...##...#....#...#...
# MAGIC 18: ..##.#.#....#####.#.#.#...##...##..##..
# MAGIC 19: .#..###.#..#.#.#######.#.#.#..#.#...#..
# MAGIC 20: .#....##....#####...#######....#.#..##.
# MAGIC </code></pre>
# MAGIC <p>The generation is shown along the left, where <code>0</code> is the initial state.  The pot numbers are shown along the top, where <code>0</code> labels the center pot, negative-numbered pots extend to the left, and positive pots extend toward the right. Remember, the initial state begins at pot <code>0</code>, which is not the leftmost pot used in this example.</p>
# MAGIC <p>After one generation, only seven plants remain.  The one in pot <code>0</code> matched the rule looking for <code>..#..</code>, the one in pot <code>4</code> matched the rule looking for <code>.#.#.</code>, pot <code>9</code> matched <code>.##..</code>, and so on.</p>
# MAGIC <p>In this example, after 20 generations, the pots shown as <code>#</code> contain plants, the furthest left of which is pot <code>-2</code>, and the furthest right of which is pot <code>34</code>. Adding up all the numbers of plant-containing pots after the 20th generation produces <code><em>325</em></code>.</p>
# MAGIC <p><em>After <code>20</code> generations, what is the sum of the numbers of all pots which contain a plant?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "initial state: ##.###.......#..#.##..#####...#...#######....##.##.##.##..#.#.##########...##.##..##.##...####..####

#.#.# => #
.##.. => .
#.#.. => .
..### => #
.#..# => #
..#.. => .
####. => #
###.. => #
#.... => .
.#.#. => #
....# => .
#...# => #
..#.# => #
#..#. => #
.#... => #
##..# => .
##... => .
#..## => .
.#.## => #
.##.# => .
#.##. => #
.#### => .
.###. => .
..##. => .
##.#. => .
...## => #
...#. => .
..... => .
##.## => .
###.# => #
##### => #
#.### => .
"

# COMMAND ----------

start_state <- str_extract(input, "[#.]+")
start_state

# COMMAND ----------

df <-
  read_lines(input) %>%
  tail(-2) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("from", "to"))
df

# COMMAND ----------

plant_regex <-
  df %>%
  filter(to == "#") %>%
  mutate(
    from_regex = str_c(
      "(?<=",
      str_sub(from, 1, 2),
      ")",
      str_sub(from, 3, 3),
      "(?=",
      str_sub(from, 4),
      ")"
    ) %>%
      str_replace_all(fixed("."), "\\.")
  ) %>%
  pull(from_regex) %>%
  str_c(collapse = "|")
plant_regex

# COMMAND ----------

simulate1 <- function(s) {
  x <- str_locate_all(s, plant_regex)[[1]][,1]
  s <- rep(".", str_length(s))
  s[x] <- "#"
  str_c(s, collapse = "")
}

simulate <- function(s, n) {
  for (i in seq_len(n)) {
    s <- simulate1(str_c(".....", s, "....."))
  }
  s
}

score <- function(s, n) {
  simulate(start_state, n) %>%
    str_split("") %>%
    first() %>%
    {which(. == "#") - n * 5 - 1} %>%
    sum()
}

# COMMAND ----------

answer <- score(start_state, 20)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You realize that 20 generations aren't enough.  After all, these plants will need to last another 1500 years to even reach your timeline, not to mention your future.</p>
# MAGIC <p><em>After fifty billion (<code>50000000000</code>) generations, what is the sum of the numbers of all pots which contain a plant?</em></p>
# MAGIC </article>

# COMMAND ----------

plot_df <-
  tibble(x = seq_len(500)) %>%
  rowwise() %>%
  mutate(sc = score(start_state, x))

# COMMAND ----------

ggplot(plot_df, aes(x, sc)) +
  geom_line() +
  theme_minimal()

# COMMAND ----------

plot_df %>%
  ungroup() %>%
  mutate(dsc = sc - lag(sc)) %>%
  tail(n = 20)

# COMMAND ----------

answer <- format(11957 + 23 * (50000000000 - 500), scientific = FALSE)
answer
