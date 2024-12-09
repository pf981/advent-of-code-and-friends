library(tidyverse)



d_min <- input %>% str_extract("^\\d+") %>% parse_integer()
d_max <- input %>% str_extract("\\d+$") %>% parse_integer()
lst(d_min, d_max)

has_two_adjacent_digits <- function(d) {
  d %>%
    as.character() %>%
    str_split('') %>%
    map(rle) %>%
    map("lengths") %>%
    map_int(max) %>%
    map_lgl(~. > 1)
}

is_non_decreasing <- function(d) {
  d %>%
    as.character() %>%
    str_split('') %>%
    map_lgl(~all(. == sort(.)))
}

answer <-
  tibble(d = seq(from = d_min, to = d_max)) %>%
  filter(has_two_adjacent_digits(d)) %>%
  filter(is_non_decreasing(d)) %>%
  nrow()
answer

has_two_lone_adjacent_digits <- function(d) {
  d %>%
    as.character() %>%
    str_split('') %>%
    map(rle) %>%
    map("lengths") %>%
    map_lgl(~any(. == 2))
}

answer <-
  tibble(d = seq(from = d_min, to = d_max)) %>%
  filter(has_two_lone_adjacent_digits(d)) %>%
  filter(is_non_decreasing(d)) %>%
  nrow()
answer
