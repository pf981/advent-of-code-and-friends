library(tidyverse)



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
    crossing(a = coords, b = coords) %>%
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

result <- find_max_asteroids(input)
result$answer

library(testthat)

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

test_that("example map 2 works", {
  res <- find_max_asteroids("#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
")
  expect_equal(res$answer, 35)
  expect_equal(c(res$best_x, res$best_y), c(1, 2))
})

test_that("example map 3 works", {
  res <- find_max_asteroids(".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
")
  expect_equal(res$answer, 41)
  expect_equal(c(res$best_x, res$best_y), c(6, 3))
})

test_that("example map 4 works", {
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
  expect_equal(res$answer, 210)
  expect_equal(c(res$best_x, res$best_y), c(11, 13))
})

result$distances %>%
  filter(x == result$best_x, y == result$best_y) %>%
  ungroup() %>%
  group_by(angle) %>%
  mutate(rn = row_number()) %>%
  arrange(rn, angle) %>%
  ungroup() %>%
  slice(200) %>%
  with(100 * x1 + y1)