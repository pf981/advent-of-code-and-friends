library(tidyverse)





answer <-
  input %>%
  read_lines() %>%
  str_split(" ") %>%
  map_lgl(~all(!duplicated(.))) %>%
  sum()
answer

answer <-
  input %>%
  read_lines() %>%
  str_split(" ") %>%
  map_lgl(function(x) {
    x %>%
      str_split("") %>%
      map_chr(~str_c(str_sort(.), collapse = "")) %>%
      duplicated() %>%
      `!` %>%
      all()
  }) %>%
  sum()
answer
