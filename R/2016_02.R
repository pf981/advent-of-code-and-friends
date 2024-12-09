library(tidyverse)



dial_number <- function(delta_x, delta_y) {
  x <- 2
  y <- 2
  result_x <- integer(length(delta_x))
  result_y <- integer(length(delta_y))
  
  for (i in seq_along(delta_x)){
    new_pos <- c(x + delta_x[i], y + delta_y[i])
    if (all(new_pos <= 3) && all(new_pos > 0)) {
      x <- new_pos[1]
      y <- new_pos[2]
    }
    
    result_x[i] <- x
    result_y[i] <- y
  }
  (result_y - 1) * 3 + result_x
}

x_coef <- c(U = 0, R = 1, D = 0, L = -1)
y_coef <- c(U = -1, R = 0, D = 1, L = 0)

instructions <-
  read_lines(input) %>%
  str_split("") %>%
  map_dfr(~tibble(direction = .), .id = "id") %>%
  mutate(
    number = dial_number(x_coef[direction], y_coef[direction])
  )

answer <-
  instructions %>%
  group_by(id) %>%
  slice(n()) %>%
  pull(number) %>%
  str_c(collapse = "")
answer

diamond_number <- function(delta_x, delta_y) {
  x <- -2
  y <- 0
  result_x <- integer(length(delta_x))
  result_y <- integer(length(delta_y))
  
  for (i in seq_along(delta_x)){
    new_pos <- c(x + delta_x[i], y + delta_y[i])
    if (
      all(abs(new_pos) <= 2) &&
      sum(abs(new_pos)) <= 2
    ) {
      x <- new_pos[1]
      y <- new_pos[2]
    }
    
    result_x[i] <- x
    result_y[i] <- y
  }
  matrix(
    c(
      NA,  NA,   1,  NA, NA,
      NA,   2,   3,   4, NA,
       5,   6,   7,   8,  9,
      NA, "A", "B", "C", NA,
      NA,  NA, "D",  NA, NA
    ),
    ncol = 5,
    byrow = TRUE
  )[cbind(result_y + 3, result_x + 3)] %>% as.vector()
}

answer <-
  instructions %>%
  mutate(
    number = diamond_number(x_coef[direction], y_coef[direction])
  ) %>%
  group_by(id) %>%
  slice(n()) %>%
  pull(number) %>%
  str_c(collapse = "")
answer
