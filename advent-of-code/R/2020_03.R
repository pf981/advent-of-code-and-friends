library(tidyverse)



trees <-
  input %>%
  read_lines()

result <-
  trees %>%
  as_tibble() %>%
  mutate(
    i = 1 + (((seq_along(value) - 1) * 3) %% nchar(first(value))),
    result = str_sub(value, i, i),
    is_tree = result == '#'
  )
result

answer <- result %>% pull(is_tree) %>% sum()
answer

count_trees <- function(trees, n_right, n_down) {
  trees %>%
    as_tibble() %>%
    filter((row_number() - 1) %% n_down == 0) %>%
    mutate(
      i = 1 + (((seq_along(value) - 1) * n_right) %% nchar(first(value))),
      result = str_sub(value, i, i),
      is_tree = result == '#'
    ) %>%
    pull(is_tree) %>%
    sum(na.rm = TRUE)
}

answer <-
  # Note that map2_int won't work because of integer overflow
  map2_dbl(c(1, 3, 5, 7, 1), c(1, 1, 1, 1, 2), count_trees, trees = trees) %>%
  reduce(`*`)
answer
