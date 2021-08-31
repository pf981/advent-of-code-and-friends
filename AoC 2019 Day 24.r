# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: Planet of Discord ---</h2><p>You land on <a href="https://en.wikipedia.org/wiki/Eris_(dwarf_planet)">Eris</a>, your last stop before reaching Santa.  As soon as you do, your sensors start picking up strange life forms moving around: Eris is infested with <a href="https://www.nationalgeographic.org/thisday/sep9/worlds-first-computer-bug/">bugs</a>! With an <span title="For a sad version of this story, look up Voices of a Distant Star.">over 24-hour roundtrip</span> for messages between you and Earth, you'll have to deal with this problem on your own.</p>
# MAGIC <p>Eris isn't a very large place; a scan of the entire area fits into a 5x5 grid (your puzzle input). The scan shows <em>bugs</em> (<code>#</code>) and <em>empty spaces</em> (<code>.</code>).</p>
# MAGIC <p>Each <em>minute</em>, The bugs live and die based on the number of bugs in the <em>four adjacent tiles</em>:</p>
# MAGIC <ul>
# MAGIC <li>A bug <em>dies</em> (becoming an empty space) unless there is <em>exactly one</em> bug adjacent to it.</li>
# MAGIC <li>An empty space <em>becomes infested</em> with a bug if <em>exactly one or two</em> bugs are adjacent to it.</li>
# MAGIC </ul>
# MAGIC <p>Otherwise, a bug or empty space remains the same.  (Tiles on the edges of the grid have fewer than four adjacent tiles; the missing tiles count as empty space.) This process happens in every location <em>simultaneously</em>; that is, within the same minute, the number of adjacent bugs is counted for every tile first, and then the tiles are updated.</p>
# MAGIC <p>Here are the first few minutes of an example scenario:</p>
# MAGIC <pre><code>Initial state:
# MAGIC ....#
# MAGIC #..#.
# MAGIC #..##
# MAGIC ..#..
# MAGIC #....
# MAGIC 
# MAGIC After 1 minute:
# MAGIC #..#.
# MAGIC ####.
# MAGIC ###.#
# MAGIC ##.##
# MAGIC .##..
# MAGIC 
# MAGIC After 2 minutes:
# MAGIC #####
# MAGIC ....#
# MAGIC ....#
# MAGIC ...#.
# MAGIC #.###
# MAGIC 
# MAGIC After 3 minutes:
# MAGIC #....
# MAGIC ####.
# MAGIC ...##
# MAGIC #.##.
# MAGIC .##.#
# MAGIC 
# MAGIC After 4 minutes:
# MAGIC ####.
# MAGIC ....#
# MAGIC ##..#
# MAGIC .....
# MAGIC ##...
# MAGIC </code></pre>
# MAGIC <p>To understand the nature of the bugs, watch for the first time a layout of bugs and empty spaces <em>matches any previous layout</em>. In the example above, the first layout to appear twice is:</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC .....
# MAGIC #....
# MAGIC .#...
# MAGIC </code></pre>
# MAGIC <p>To calculate the <em>biodiversity rating</em> for this layout, consider each tile left-to-right in the top row, then left-to-right in the second row, and so on. Each of these tiles is worth biodiversity points equal to <em>increasing powers of two</em>: 1, 2, 4, 8, 16, 32, and so on.  Add up the biodiversity points for tiles with bugs; in this example, the 16th tile (<code>32768</code> points) and 22nd tile (<code>2097152</code> points) have bugs, a total biodiversity rating of <code><em>2129920</em></code>.</p>
# MAGIC <p><em>What is the biodiversity rating for the first layout that appears twice?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- ".....
...#.
.#..#
.#.#.
...##
"

# COMMAND ----------

start_m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t() %>%
  `==`("#")
start_m

# COMMAND ----------

shift <- function(m, i, j) {
  i <- seq_len(nrow(m)) + i
  j <- seq_len(ncol(m)) + j
  
  i[i == 0 | i > nrow(m)] <- NA
  j[j == 0 | j > ncol(m)] <- NA
  
  result <- m[i, j]
  result[is.na(result)] <- FALSE
  result
}

count_neighbors <- function(m) {
  shift(m, -1, 0) +
    shift(m, 0, -1) +
    shift(m, 0, 1) +
    shift(m, 1, 0)
}

step <- function(m) {
  neighbors <- count_neighbors(m)
  
  keep_on <- m & neighbors == 1
  turn_on <- !m & neighbors %in% c(1, 2)
  m[] <- FALSE
  m[keep_on | turn_on] <- TRUE
  m
}

step_n <- function(m, n) {
  for (i in seq_len(n)) {
    m <- step(m)
  }
  m
}

# COMMAND ----------

as_character <- function(x) format(x, scientific = FALSE)

solve <- function(m) {
  seen <- list()
  repeat {
    m <- step(m)
    biodiversity <- sum(2^(which(t(m)) - 1))
    if (!is.null(seen[[as_character(biodiversity)]])) {
      return(biodiversity)
    }
    seen[[as_character(biodiversity)]] <- TRUE
  }
}

# COMMAND ----------

answer <- solve(start_m)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After careful analysis, one thing is certain: <em>you have no idea where all these bugs are coming from</em>.</p>
# MAGIC <p>Then, you remember: Eris is an old <a href="20">Plutonian</a> settlement! Clearly, the bugs are coming from recursively-folded space.</p>
# MAGIC <p>This 5x5 grid is <em>only one</em> level in an <em>infinite</em> number of recursion levels. The tile in the middle of the grid is actually another 5x5 grid, the grid in your scan is contained as the middle tile of a larger 5x5 grid, and so on. Two levels of grids look like this:</p>
# MAGIC <pre><code>     |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | |?| | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     | | | | | |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC      |     |         |     |     
# MAGIC </code></pre>
# MAGIC <p>(To save space, some of the tiles are not drawn to scale.)  Remember, this is only a small part of the infinitely recursive grid; there is a 5x5 grid that contains this diagram, and a 5x5 grid that contains that one, and so on.  Also, the <code>?</code> in the diagram contains another 5x5 grid, which itself contains another 5x5 grid, and so on.</p>
# MAGIC <p>The scan you took (your puzzle input) shows where the bugs are <em>on a single level</em> of this structure. The middle tile of your scan is empty to accommodate the recursive grids within it. Initially, no other levels contain bugs.</p>
# MAGIC <p>Tiles still count as <em>adjacent</em> if they are directly <em>up, down, left, or right</em> of a given tile. Some tiles have adjacent tiles at a recursion level above or below its own level. For example:</p>
# MAGIC <pre><code>     |     |         |     |     
# MAGIC   1  |  2  |    3    |  4  |  5  
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC   6  |  7  |    8    |  9  |  10 
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |A|B|C|D|E|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |F|G|H|I|J|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC  11  | 12  |K|L|?|N|O|  14 |  15 
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |P|Q|R|S|T|     |     
# MAGIC      |     |-+-+-+-+-|     |     
# MAGIC      |     |U|V|W|X|Y|     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC  16  | 17  |    18   |  19 |  20 
# MAGIC      |     |         |     |     
# MAGIC -----+-----+---------+-----+-----
# MAGIC      |     |         |     |     
# MAGIC  21  | 22  |    23   |  24 |  25 
# MAGIC      |     |         |     |     
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Tile 19 has four adjacent tiles: 14, 18, 20, and 24.</li>
# MAGIC <li>Tile G has four adjacent tiles: B, F, H, and L.</li>
# MAGIC <li>Tile D has four adjacent tiles: 8, C, E, and I.</li>
# MAGIC <li>Tile E has four adjacent tiles: 8, D, 14, and J.</li>
# MAGIC <li>Tile 14 has <em>eight</em> adjacent tiles: 9, E, J, O, T, Y, 15, and 19.</li>
# MAGIC <li>Tile N has <em>eight</em> adjacent tiles: I, O, S, and five tiles within the sub-grid marked <code>?</code>.</li>
# MAGIC </ul>
# MAGIC <p>The rules about bugs living and dying are the same as before.</p>
# MAGIC <p>For example, consider the same initial state as above:</p>
# MAGIC <pre><code>....#
# MAGIC #..#.
# MAGIC #.?##
# MAGIC ..#..
# MAGIC #....
# MAGIC </code></pre>
# MAGIC <p>The center tile is drawn as <code>?</code> to indicate the next recursive grid. Call this level 0; the grid within this one is level 1, and the grid that contains this one is level -1.  Then, after <em>ten</em> minutes, the grid at each level would look like this:</p>
# MAGIC <pre><code>Depth -5:
# MAGIC ..#..
# MAGIC .#.#.
# MAGIC ..?.#
# MAGIC .#.#.
# MAGIC ..#..
# MAGIC 
# MAGIC Depth -4:
# MAGIC ...#.
# MAGIC ...##
# MAGIC ..?..
# MAGIC ...##
# MAGIC ...#.
# MAGIC 
# MAGIC Depth -3:
# MAGIC #.#..
# MAGIC .#...
# MAGIC ..?..
# MAGIC .#...
# MAGIC #.#..
# MAGIC 
# MAGIC Depth -2:
# MAGIC .#.##
# MAGIC ....#
# MAGIC ..?.#
# MAGIC ...##
# MAGIC .###.
# MAGIC 
# MAGIC Depth -1:
# MAGIC #..##
# MAGIC ...##
# MAGIC ..?..
# MAGIC ...#.
# MAGIC .####
# MAGIC 
# MAGIC Depth 0:
# MAGIC .#...
# MAGIC .#.##
# MAGIC .#?..
# MAGIC .....
# MAGIC .....
# MAGIC 
# MAGIC Depth 1:
# MAGIC .##..
# MAGIC #..##
# MAGIC ..?.#
# MAGIC ##.##
# MAGIC #####
# MAGIC 
# MAGIC Depth 2:
# MAGIC ###..
# MAGIC ##.#.
# MAGIC #.?..
# MAGIC .#.##
# MAGIC #.#..
# MAGIC 
# MAGIC Depth 3:
# MAGIC ..###
# MAGIC .....
# MAGIC #.?..
# MAGIC #....
# MAGIC #...#
# MAGIC 
# MAGIC Depth 4:
# MAGIC .###.
# MAGIC #..#.
# MAGIC #.?..
# MAGIC ##.#.
# MAGIC .....
# MAGIC 
# MAGIC Depth 5:
# MAGIC ####.
# MAGIC #..#.
# MAGIC #.?#.
# MAGIC ####.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>In this example, after 10 minutes, a total of <code><em>99</em></code> bugs are present.</p>
# MAGIC <p>Starting with your scan, <em>how many bugs are present after 200 minutes?</em></p>
# MAGIC </article>

# COMMAND ----------

count_neighbors <- function(ms) {
  counts <- map(ms, function(m) {m[] <- 0; m})
  
  mid_row <- ceiling(nrow(m) / 2)
  mid_col <- ceiling(ncol(m) / 2)
  
  for (depth in seq_along(ms)) {
    m <- ms[[depth]]
    m[mid_row, mid_col] <- FALSE
    counts[[depth]] <-
      counts[[depth]] +
        shift(m, -1, 0) +
        shift(m, 0, -1) +
        shift(m, 0, 1) +
        shift(m, 1, 0)
    
    if (depth != length(ms)) {
      for (direction in c("N", "E", "S", "W")) {
        row <- mid_row + (direction == "S") - (direction == "N")
        col <- mid_col + (direction == "E") - (direction == "W")
        
        if (direction == "N") {
          next_depth_rows <- 1
          next_depth_cols <- seq_len(ncol(m))
        } else if (direction == "E") {
          next_depth_rows <- seq_len(nrow(m))
          next_depth_cols <- ncol(m)
        } else if (direction == "S") {
          next_depth_rows <- nrow(m)
          next_depth_cols <- seq_len(ncol(m))
        } else if (direction == "W") {
          next_depth_rows <- seq_len(nrow(m))
          next_depth_cols <- 1
        }
        
        counts[[depth]][row, col] <- counts[[depth]][row, col] + sum(ms[[depth + 1]][next_depth_rows, next_depth_cols])
        counts[[depth + 1]][next_depth_rows, next_depth_cols] <- counts[[depth + 1]][next_depth_rows, next_depth_cols] + m[row, col]
        
      }
    }
  }
  counts
}

step_single <- function(m, neighbors) {
  keep_on <- m & neighbors == 1
  turn_on <- !m & neighbors %in% c(1, 2)
  m[] <- FALSE
  m[keep_on | turn_on] <- TRUE
  m[ceiling(nrow(m) / 2), ceiling(ncol(m) / 2)] <- FALSE
  m
}

step <- function(ms) {
  neighbors <- count_neighbors(ms)
  
  map2(ms, neighbors, step_single)
}

step_n <- function(ms, n) {
  for (i in seq_len(n)) {
    ms <- step(ms)
  }
  ms
}

# COMMAND ----------

n_minutes <- 200

m <- start_m
m[] <- FALSE

ms <- rep(list(m), n_minutes * 2 + 1)
ms[[ceiling(length(ms) / 2)]] <- start_m
ms

# COMMAND ----------

result <- step_n(ms, n_minutes)
result

# COMMAND ----------

answer <- result %>% unlist() %>% sum()
answer
