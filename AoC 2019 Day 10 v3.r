# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/10

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "#.#................#..............#......#......
.......##..#..#....#.#.....##...#.........#.#...
.#...............#....#.##......................
......#..####.........#....#.......#..#.....#...
.....#............#......#................#.#...
....##...#.#.#.#.............#..#.#.......#.....
..#.#.........#....#..#.#.........####..........
....#...#.#...####..#..#..#.....#...............
.............#......#..........#...........#....
......#.#.........#...............#.............
..#......#..#.....##...##.....#....#.#......#...
...#.......##.........#.#..#......#........#.#..
#.............#..........#....#.#.....#.........
#......#.#................#.......#..#.#........
#..#.#.....#.....###..#.................#..#....
...............................#..........#.....
###.#.....#.....#.............#.......#....#....
.#.....#.........#.....#....#...................
........#....................#..#...............
.....#...#.##......#............#......#.....#..
..#..#..............#..#..#.##........#.........
..#.#...#.......#....##...#........#...#.#....#.
.....#.#..####...........#.##....#....#......#..
.....#..#..##...............................#...
.#....#..#......#.#............#........##...#..
.......#.....................#..#....#.....#....
#......#..###...........#.#....#......#.........
..............#..#.#...#.......#..#.#...#......#
.......#...........#.....#...#.............#.#..
..##..##.............#........#........#........
......#.............##..#.........#...#.#.#.....
#........#.........#...#.....#................#.
...#.#...........#.....#.........#......##......
..#..#...........#..........#...................
.........#..#.......................#.#.........
......#.#.#.....#...........#...............#...
......#.##...........#....#............#........
#...........##.#.#........##...........##.......
......#....#..#.......#.....#.#.......#.##......
.#....#......#..............#.......#...........
......##.#..........#..................#........
......##.##...#..#........#............#........
..#.....#.................###...#.....###.#..#..
....##...............#....#..................#..
.....#................#.#.#.......#..........#..
#........................#.##..........#....##..
.#.........#.#.#...#...#....#........#..#.......
...#..#.#......................#...............#
"

# COMMAND ----------

find_max_asteroids <- function(asteroids_str) {
  asteroids_str <- read_lines(asteroids_str)
  asteroids <-
    asteroids_str %>%
    str_c(collapse = "") %>%
    str_split('') %>%
    unlist() %>%
    matrix(ncol = nchar(asteroids_str[[1]]), byrow = TRUE)
  
  coords <-
    which(asteroids == "#", arr.ind = TRUE) %>%
    as_tibble() %>%
    transmute(x = col - 1, y = row - 1)
  
  distances <-
    crossing(a=coords, b=coords) %>%
    as.list() %>%
    bind_cols() %>%
    filter(!(x == x1 & y == y1)) %>% # ?
    mutate(
      angle = (-pi / 2 + Arg(complex(real = x - x1, imaginary = y - y1))) %% (2 * pi),
      d = (x - x1)^2 + (y - y1)^2
    ) %>%
    group_by(x, y, angle) %>%
    arrange(d)
  
  result <- 
    distances %>%
    slice(1) %>%
    ungroup() %>%
    count(x, y) %>%
    arrange(desc(n))
  
  lst(
    answer = result$n[[1]],
    best_x = result$x[[1]],
    best_y = result$y[[1]],
    distances = distances,
    result = result,
    p = ggplot(result, aes(x, y, label = n)) + geom_point() + geom_label() + scale_y_reverse()
  )
}

# COMMAND ----------

result <- find_max_asteroids(input)
result$answer

# COMMAND ----------

# MAGIC %md ### Tests

# COMMAND ----------

library(testthat)

# COMMAND ----------

res <- find_max_asteroids(".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
")

# COMMAND ----------

ggplot(result, aes(x, y, label = n)) + geom_point() + geom_label() + scale_y_reverse()

# COMMAND ----------

res$distances %>%
  filter(x == res$best_x, y == res$best_y) %>%
  ungroup() %>%
  mutate(
    angle = (-pi / 2 + Arg(complex(real = x - x1, imaginary = y - y1))) %% (2 * pi)
  ) %>%
  group_by(angle) %>%
  mutate(rn = row_number()) %>%
  arrange(rn, angle) %>%
  ungroup() %>%
  mutate(id = row_number()) %>%
  head(50)

# COMMAND ----------

res$distances %>%
  filter(x == res$best_x, y == res$best_y) %>%
  ungroup() %>%
  mutate(
    angle = (-pi / 2 + Arg(complex(real = x - x1, imaginary = y - y1))) %% (2 * pi)
  ) %>%
  group_by(angle) %>%
  mutate(rn = row_number()) %>%
  arrange(rn, angle) %>%
  ungroup() %>%
  mutate(id = row_number()) %>%
  slice(200)

# COMMAND ----------

result$distances %>%
  filter(x == result$best_x, y == result$best_y) %>%
  ungroup() %>%
  mutate(
    angle = (-pi / 2 + Arg(complex(real = x - x1, imaginary = y - y1))) %% (2 * pi)
  ) %>%
  group_by(angle) %>%
  mutate(rn = row_number()) %>%
  arrange(rn, angle) %>%
  ungroup() %>%
  mutate(id = row_number()) %>%
  head(50) %>%
  ggplot(aes(x1, y1, label = id)) + geom_label() + annotate("point", x = result$best_x, y = result$best_y, col = "red") + scale_y_reverse()

# COMMAND ----------

res$p

# COMMAND ----------

res$result

# COMMAND ----------

lst(res$best_x, res$best_y)

# COMMAND ----------

test_that("example map 1 works", {
  res <- find_max_asteroids("......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
")
  expect_equal(res$answer, 33)
  expect_equal(c(res$best_x, res$best_y), c(5, 8))
})

# COMMAND ----------


  expect_equal(
    find_max_asteroids("#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
")$answer,
    35
  )
  expect_equal(
    find_max_asteroids(".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
")$answer,
    41
  )
  expect_equal(
    find_max_asteroids(".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
")$answer,
    210
  )
})

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

result <- find_max_asteroids(".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
")

# COMMAND ----------

str(result
    )

# COMMAND ----------

result

# COMMAND ----------

result$distances %>%
  filter(x == result$best_x, y == result$best_y) %>%
  mutate(
    angle = Arg(complex(real = x - x1, imaginary = y - y1)) %% (2 * pi)
  ) %>%
  group_by(angle) %>%
  mutate(
    rn = row_number()
  ) %>%
  arrange(rn, angle) %>%
  display()

# COMMAND ----------

angle = angle + 2pi * row_number

# COMMAND ----------

names(result)

# COMMAND ----------

result %>%
  filter()

# COMMAND ----------

lst(result$best_x, result$best_y)

# COMMAND ----------

x1 = -1
y1 = -1
x2 = -10
y2 = 10

Arg(complex(real = x2 - x1, imaginary = y2 - y1))

# COMMAND ----------

Arg(complex(real = x1 - x2, imaginary = y1 - y2)) / pi * 180

# COMMAND ----------

Arg(complex(real = x1 - x2, imaginary = y1 - y2)) %% (2 * pi) # THIS <---

# COMMAND ----------

(Arg(complex(real = x1 - x2, imaginary = y1 - y2)) / pi * 180) %% 360

# COMMAND ----------

Arg(complex(real = x2 - x1, imaginary = y2 - y1)) / pi * 180

# COMMAND ----------

result$distances %>%
    slice(1) %>%
    ungroup() %>%
    count(x, y) %>%
    arrange(desc(n))

# COMMAND ----------

display(result$result)

# COMMAND ----------

# tribble(
#   ~id, ~x, ~y,
#     1,  1, -10,
#     2, 10,  -1,
#     3, 10,   1,
#     4,1,10,
#     5,-1,10,
#     6,-10,1,
#     7,-10,-1,
#     8,-1,-10
# ) %>%
#   mutate(
#     angle = (pi / 2 + Arg(complex(real = x, imaginary = y))) %% (2 * pi)
#   ) %>%
#   arrange(angle)