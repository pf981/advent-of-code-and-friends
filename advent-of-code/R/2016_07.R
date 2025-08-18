library(tidyverse)



is_abba1 <- function(x) {
  inside <- str_extract_all(x, "\\[[a-z]+\\]")
  outside <- str_extract_all(x, "[a-z]+($|\\[)")

  inside_match <- inside %>% str_detect("([a-z])(?!\\1)([a-z])\\2\\1") %>% any()
  outside_match <- outside %>% str_detect("([a-z])(?!\\1)([a-z])\\2\\1") %>% any()
  
  outside_match && !inside_match
}

is_abba <- function(x) map_lgl(x, is_abba1)

answer <-
  input %>%
  read_lines() %>%
  is_abba() %>%
  sum()
answer

extract_bab1 <- function(x) {
  x %>%
    str_locate_all("(?=([a-z])(?!\\1).\\1)") %>%
    first() %>%
    as_tibble() %>%
    pull(start) %>%
    str_sub(x, ., . + 2) %>%
    unlist()
}

extract_bab <- function(x) x %>% map(extract_bab1) %>% unlist() %>% unique()

is_bab1 <- function(x) {
  inside <- str_extract_all(x, "\\[[a-z]+\\]") %>% unlist()
  outside <- str_extract_all(x, "[a-z]+($|\\[)") %>% unlist()

  inside_bab <- inside %>% extract_bab() %>% str_sub(1, 2)
  outside_bab <- outside %>% extract_bab() %>% str_sub(2, 3)
  
  length(intersect(inside_bab, outside_bab)) > 0
}

is_bab <- function(x) map_lgl(x, is_bab1)

answer <-
  input %>%
  read_lines() %>%
  is_bab() %>%
  sum()
answer
