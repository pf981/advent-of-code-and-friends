library(tidyverse)



wire_path <-
  read_lines(input) %>%
  str_split(",")
wire_path

get_points <- function(directions, start_x = 0, start_y = 0) {
  d <- parse_number(directions)
  direction <- str_sub(directions, 1, 1)
  
  add_x <- 0
  add_y <- 0
  
  if (direction == 'R') {
    add_x <- d
  } else if (direction == 'L') {
    add_x <- -d
  } else if (direction == 'U') {
    add_y <- d
  } else if (direction == 'D') {
    add_y <- -d
  } else {
    stop('Unknown direction ', direction)
  }
  
  tibble(
    x = start_x + seq(from = 0, to = add_x),
    y = start_y + seq(from = 0, to = add_y)
  ) %>%
    slice(-1)
}

get_all_points <- function(path) {
  start_x <- 0
  start_y <- 0
  points <- data.frame(x = 0, y = 0)
  for (direction in path) {
    points <- bind_rows(points, get_points(direction, last(points$x), last(points$y)))
  }
  points %>% slice(-1)
}

p1 <- get_all_points(wire_path[[1]])
p2 <- get_all_points(wire_path[[2]])

answer <-
  inner_join(p1, p2) %>%
  filter(!(x == 0 & y == 0)) %>%
  mutate(distance = abs(x) + abs(y)) %>%
  pull(distance) %>%
  min()
answer

answer <-
  inner_join(
    p1 %>% mutate(d1 = row_number()),
    p2 %>% mutate(d2 = row_number())
  ) %>%
  mutate(distance = d1 + d2) %>%
  pull(distance) %>%
  min()
answer
