library(tidyverse)





answer <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  bind_cols() %>%
  t() %>%
  apply(MARGIN = 2, FUN = function(x) {
    table(x) %>%
      sort(decreasing = TRUE) %>%
      names() %>%
      first()
  }) %>%
  str_c(collapse = "")
answer

answer <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  bind_cols() %>%
  t() %>%
  apply(MARGIN = 2, FUN = function(x) {
    table(x) %>%
      sort(decreasing = TRUE) %>%
      names() %>%
      last()
  }) %>%
  str_c(collapse = "")
answer
