# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 13: A Maze of Twisty Little Cubicles ---</h2><p>You arrive at the first floor of this new building to discover a much less welcoming environment than the shiny atrium of the last one.  Instead, you are in a maze of <span title="You are in a twisty alike of little cubicles, all maze.">twisty little cubicles</span>, all alike.</p>
# MAGIC <p>Every location in this area is addressed by a pair of non-negative integers (<code>x,y</code>). Each such coordinate is either a wall or an open space. You can't move diagonally. The cube maze starts at <code>0,0</code> and seems to extend infinitely toward <em>positive</em> <code>x</code> and <code>y</code>; negative values are <em>invalid</em>, as they represent a location outside the building. You are in a small waiting area at <code>1,1</code>.</p>
# MAGIC <p>While it seems chaotic, a nearby morale-boosting poster explains, the layout is actually quite logical. You can determine whether a given <code>x,y</code> coordinate will be a wall or an open space using a simple system:</p>
# MAGIC <ul>
# MAGIC <li>Find <code>x*x + 3*x + 2*x*y + y + y*y</code>.</li>
# MAGIC <li>Add the office designer's favorite number (your puzzle input).</li>
# MAGIC <li>Find the <a href="https://en.wikipedia.org/wiki/Binary_number">binary representation</a> of that sum; count the <em>number</em> of <a href="https://en.wikipedia.org/wiki/Bit">bits</a> that are <code>1</code>.
# MAGIC <ul>
# MAGIC <li>If the number of bits that are <code>1</code> is <em>even</em>, it's an <em>open space</em>.</li>
# MAGIC <li>If the number of bits that are <code>1</code> is <em>odd</em>, it's a <em>wall</em>.</li>
# MAGIC </ul>
# MAGIC </li>
# MAGIC </ul>
# MAGIC <p>For example, if the office designer's favorite number were <code>10</code>, drawing walls as <code>#</code> and open spaces as <code>.</code>, the corner of the building containing <code>0,0</code> would look like this:</p>
# MAGIC <pre><code>  0123456789
# MAGIC 0 .#.####.##
# MAGIC 1 ..#..#...#
# MAGIC 2 #....##...
# MAGIC 3 ###.#.###.
# MAGIC 4 .##..#..#.
# MAGIC 5 ..##....#.
# MAGIC 6 #...##.###
# MAGIC </code></pre>
# MAGIC <p>Now, suppose you wanted to reach <code>7,4</code>. The shortest route you could take is marked as <code>O</code>:</p>
# MAGIC <pre><code>  0123456789
# MAGIC 0 .#.####.##
# MAGIC 1 .O#..#...#
# MAGIC 2 #OOO.##...
# MAGIC 3 ###O#.###.
# MAGIC 4 .##OO#OO#.
# MAGIC 5 ..##OOO.#.
# MAGIC 6 #...##.###
# MAGIC </code></pre>
# MAGIC <p>Thus, reaching <code>7,4</code> would take a minimum of <code>11</code> steps (starting from your current location, <code>1,1</code>).</p>
# MAGIC <p>What is the <em>fewest number of steps required</em> for you to reach <code>31,39</code>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- 1364
target_x <- 31
target_y <- 39

# COMMAND ----------

# input <- 10
# target_x <- 7
# target_y <- 4

# COMMAND ----------

hash <- function(x, y) str_c(x, y, sep = ",")

is_wall <- function(x, y) {
  if (x < 0 || y < 0) return(TRUE)
  value <- x*x + 3*x + 2*x*y + y + y*y + input
  sum_of_bits <- value %>% intToBits() %>% as.integer() %>% sum()
  sum_of_bits %% 2
}

# COMMAND ----------

solve <- function() {
  ds <- 0
  xs <- 1
  ys <- 1

  visited_hashes <- NULL

  repeat {
    i <- which.min(ds)
    d <- ds[i]
    x <- xs[i]
    y <- ys[i]

    ds <- ds[-i]
    xs <- xs[-i]
    ys <- ys[-i]

    visited_hashes <- c(visited_hashes, hash(x, y))
    
    new_xs <- c(x, x + 1, x, x - 1)
    new_ys <- c(y - 1, y, y + 1, y)
    
    for (new_pos_i in seq_along(new_xs)[!(hash(new_xs, new_ys) %in% visited_hashes)]) {  
      new_x <- new_xs[new_pos_i]
      new_y <- new_ys[new_pos_i]
      
      if (!is_wall(new_x, new_y)) {
        if (new_x == target_x && new_y == target_y) { # If solved
          return(d + 1)
        }

        xs <- c(xs, new_x)
        ys <- c(ys, new_y)
        ds <- c(ds, d + 1)
      }
    }
  }
}

# COMMAND ----------

answer <- solve()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many locations</em> (distinct <code>x,y</code> coordinates, including your starting location) can you reach in at most <code>50</code> steps?</p>
# MAGIC </article>

# COMMAND ----------

solve <- function() {
  ds <- 0
  xs <- 1
  ys <- 1

  visited_hashes <- NULL

  repeat {
    i <- which.min(ds)
    d <- ds[i]
    x <- xs[i]
    y <- ys[i]
    
    if (d > 50) {
      return(visited_hashes %>% unique() %>% length())
    }

    ds <- ds[-i]
    xs <- xs[-i]
    ys <- ys[-i]

    visited_hashes <- c(visited_hashes, hash(x, y))
    
    new_xs <- c(x, x + 1, x, x - 1)
    new_ys <- c(y - 1, y, y + 1, y)
    
    for (new_pos_i in seq_along(new_xs)[!(hash(new_xs, new_ys) %in% visited_hashes)]) {  
      new_x <- new_xs[new_pos_i]
      new_y <- new_ys[new_pos_i]
      
      if (!is_wall(new_x, new_y)) {
        xs <- c(xs, new_x)
        ys <- c(ys, new_y)
        ds <- c(ds, d + 1)
      }
    }
  }
}

# COMMAND ----------

answer <- solve()
answer
