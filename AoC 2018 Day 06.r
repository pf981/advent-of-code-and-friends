# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 6: Chronal Coordinates ---</h2><p>The device on your wrist beeps several times, and once again you feel like you're falling.</p>
# MAGIC <p>"<span title="Why is the situation always critical? Why can't the situation just be boring for once?">Situation critical</span>," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."</p>
# MAGIC <p>The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.</p>
# MAGIC <p><em>If they're dangerous,</em> maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.</p>
# MAGIC <p>Using only the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a>, determine the <em>area</em> around each coordinate by counting the number of <a href="https://en.wikipedia.org/wiki/Integer">integer</a> X,Y locations that are <em>closest</em> to that coordinate (and aren't <em>tied in distance</em> to any other coordinate).</p>
# MAGIC <p>Your goal is to find the size of the <em>largest area</em> that isn't infinite. For example, consider the following list of coordinates:</p>
# MAGIC <pre><code>1, 1
# MAGIC 1, 6
# MAGIC 8, 3
# MAGIC 3, 4
# MAGIC 5, 5
# MAGIC 8, 9
# MAGIC </code></pre>
# MAGIC <p>If we name these coordinates <code>A</code> through <code>F</code>, we can draw them on a grid, putting <code>0,0</code> at the top left:</p>
# MAGIC <pre><code>..........
# MAGIC .A........
# MAGIC ..........
# MAGIC ........C.
# MAGIC ...D......
# MAGIC .....E....
# MAGIC .B........
# MAGIC ..........
# MAGIC ..........
# MAGIC ........F.
# MAGIC </code></pre>
# MAGIC <p>This view is partial - the actual grid extends infinitely in all directions.  Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:</p>
# MAGIC <pre><code>aaaaa.cccc
# MAGIC a<em>A</em>aaa.cccc
# MAGIC aaaddecccc
# MAGIC aadddecc<em>C</em>c
# MAGIC ..d<em>D</em>deeccc
# MAGIC bb.de<em>E</em>eecc
# MAGIC b<em>B</em>b.eeee..
# MAGIC bbb.eeefff
# MAGIC bbb.eeffff
# MAGIC bbb.ffff<em>F</em>f
# MAGIC </code></pre>
# MAGIC <p>Locations shown as <code>.</code> are equally far from two or more coordinates, and so they don't count as being closest to any.</p>
# MAGIC <p>In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself).  Therefore, in this example, the size of the largest area is <em>17</em>.</p>
# MAGIC <p><em>What is the size of the largest area</em> that isn't infinite?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "262, 196
110, 109
58, 188
226, 339
304, 83
136, 356
257, 50
315, 148
47, 315
73, 130
136, 91
341, 169
334, 346
285, 248
76, 233
334, 64
106, 326
48, 207
64, 65
189, 183
300, 247
352, 279
338, 287
77, 277
220, 152
77, 295
49, 81
236, 294
321, 192
43, 234
180, 69
130, 122
166, 225
301, 290
49, 176
62, 156
346, 55
150, 138
214, 245
272, 241
50, 283
104, 70
215, 184
339, 318
175, 123
250, 100
134, 227
96, 197
312, 174
133, 237
"

# COMMAND ----------

# input <- "1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# "

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_split(", ") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("x", "y"))
df

# COMMAND ----------

counts <- integer(nrow(df))

for (cur_x in seq(from = -1000, to = 1000, by = 1)) {
  for (cur_y in seq(from = -1000, to = 1000, by = 1)) {
    d <- abs(cur_x - df$x) + abs(cur_y - df$y)
    i <- which.min(d)
    if (sum(d == d[i]) == 1) {
      counts[i] <- counts[i] + 1
    }
  }
}

# COMMAND ----------

plot(sort(counts))

# COMMAND ----------

answer <- counts %>% discard(~. > 5000) %>% max()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>On the other hand, <em>if the coordinates are safe</em>, maybe the best you can do is try to find a <em>region</em> near as many coordinates as possible.</p>
# MAGIC <p>For example, suppose you want the sum of the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a> to all of the coordinates to be <em>less than 32</em>.  For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:</p>
# MAGIC <pre><code>..........
# MAGIC .A........
# MAGIC ..........
# MAGIC ...#<em>#</em>#..C.
# MAGIC ..#D###...
# MAGIC ..###E#...
# MAGIC .B.###....
# MAGIC ..........
# MAGIC ..........
# MAGIC ........F.
# MAGIC </code></pre>
# MAGIC <p>In particular, consider the highlighted location <code>4,3</code> located at the top middle of the region. Its calculation is as follows, where <code>abs()</code> is the <a href="https://en.wikipedia.org/wiki/Absolute_value">absolute value</a> function:</p>
# MAGIC <ul>
# MAGIC <li>Distance to coordinate A: <code>abs(4-1) + abs(3-1) = &nbsp;5</code></li>
# MAGIC <li>Distance to coordinate B: <code>abs(4-1) + abs(3-6) = &nbsp;6</code></li>
# MAGIC <li>Distance to coordinate C: <code>abs(4-8) + abs(3-3) = &nbsp;4</code></li>
# MAGIC <li>Distance to coordinate D: <code>abs(4-3) + abs(3-4) = &nbsp;2</code></li>
# MAGIC <li>Distance to coordinate E: <code>abs(4-5) + abs(3-5) = &nbsp;3</code></li>
# MAGIC <li>Distance to coordinate F: <code>abs(4-8) + abs(3-9) = 10</code></li>
# MAGIC <li>Total distance: <code>5 + 6 + 4 + 2 + 3 + 10 = 30</code></li>
# MAGIC </ul>
# MAGIC <p>Because the total distance to all coordinates (<code>30</code>) is less than 32, the location is <em>within</em> the region.</p>
# MAGIC <p>This region, which also includes coordinates D and E, has a total size of <em>16</em>.</p>
# MAGIC <p>Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than <em>10000</em>.</p>
# MAGIC <p><em>What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?</em></p>
# MAGIC </article>

# COMMAND ----------

region_size <- 0

for (cur_x in seq(from = -1000, to = 1000, by = 1)) {
  for (cur_y in seq(from = -1000, to = 1000, by = 1)) {
    if (sum(abs(cur_x - df$x) + abs(cur_y - df$y)) < 10000) {
      region_size <- region_size + 1
    }
  }
}
answer <- region_size
answer
