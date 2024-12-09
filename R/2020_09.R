library(tidyverse)



window_size <- 25

nums <-
  input %>% 
  read_lines() %>%
  parse_number()
nums

get_prev <- function(x, window_size) {
  map_dfc(seq_len(window_size), lag, x = x) %>%
    asplit(1)
}

is_sum <- function(value, prev) {
  if (any(is.na(prev))) {
    return(TRUE)
  }
  sums <-
    expand.grid(prev, prev) %>%
    # filter(Var1 != Var2) %>%
    mutate(x = Var1 + Var2) %>%
    pull(x) %>%
    unique()
  
  value %in% sums
}

result <-
  nums %>%
  enframe() %>%
  mutate(
    prev = get_prev(value, window_size),
    is_answer = !map2_lgl(value, prev, is_sum)
  ) %>%
  filter(is_answer) %>%
  head(1) %>%
  pull(value)
answer <- result
answer

find_weakness <- function(nums, result) {
  for (i in seq_along(nums)) {
    cur_sum <- 0
    for (j in seq(from = i, to = length(nums), by = 1)) {
      cur_sum <- cur_sum + nums[[j]]
      if (cur_sum == result) {
        return(lst(i, j))
      }
      if (cur_sum > result) {
        break
      }
    }
  }
}

weakness <- find_weakness(nums, result)
w <- nums[weakness$i:weakness$j]
answer <- min(w) + max(w)
answer
