library(tidyverse)



lines <- input %>% read_lines()
earliest_departure <- lines[[1]] %>% parse_integer()
bus_ids <-
  lines[[2]] %>%
  str_split(",") %>%
  unlist() %>%
  parse_integer(na = "x")

lst(earliest_departure, bus_ids)

answer <-
  tibble(
    id = bus_ids,
    soonest = id - (earliest_departure %% id)
  ) %>%
  filter(soonest == min(soonest, na.rm = TRUE)) %>%
  with(id * soonest)
answer

mod_values <-
  bus_ids %>%
  enframe(name = "position", value = "id") %>%
  mutate(
    position = position - 1,
    a = (id - position) %% id,
    m = id
  ) %>%
  filter(!is.na(id))
mod_values

mul_inv <- function(a, b) {
  b0 <- b
  x0 <- 0L
  x1 <- 1L

  if (b == 1) {
    return(1L)
  }
  while(a > 1) {
    q <- bit64::as.integer64(a / b)

    t <- b
    b <- a %% b
    a <- t

    t <- x0
    x0 <- x1 - q * x0
    x1 <- t
  }

  if (x1 < 0) {
    x1 <- x1 + b0
  }
  x1
}

# numbers::chinese(mod_values$a, mod_values$m) didn't give the right answer.
# I modified https://rosettacode.org/wiki/Chinese_remainder_theorem#R to be able to handle 64 bit integers.
chinese_remainder <- function(a, m) {
  a <- bit64::as.integer64(a)
  m <- bit64::as.integer64(m)

  prod <- 1L
  sum <- 0L

  for (i in seq_along(m)) {
    prod <- prod * m[i]
  }

  for (i in seq_along(m)) {
    p <- prod / m[i]
    sum <- sum + a[i] * mul_inv(p, m[i]) * p
  }

  sum %% prod
}

answer <- chinese_remainder(mod_values$a, mod_values$m) %>% format(scientific = FALSE)
answer
