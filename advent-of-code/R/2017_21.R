library(tidyverse)



# 

df <-
  read_lines(input) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("from", "to"))
df

flip_x <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    stringi::stri_reverse() %>%
    str_c(collapse = "/")
}

flip_y <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    rev() %>%
    str_c(collapse = "/")
}

# Counter-clockwise
rotate <- function(s) {
  s %>%
    str_split("/") %>%
    first() %>%
    str_split("") %>%
    map(rev) %>%
    simplify2array() %>%
    asplit(1) %>%
    map_chr(str_c, collapse = "") %>%
    str_c(collapse = "/")
}

rotate_n <- function(s, n) {
  for (i in seq_len(n)) {
    s <- rotate(s)
  }
  s
}

df <- df %>% rowwise()
df <-
  bind_rows(
    df,
    df %>% mutate(from = from %>% flip_x()),
    df %>% mutate(from = from %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(1)),
    df %>% mutate(from = from %>% rotate_n(2)),
    df %>% mutate(from = from %>% rotate_n(3)),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x()),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(1) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(2) %>% flip_x() %>% flip_y()),
    df %>% mutate(from = from %>% rotate_n(3) %>% flip_x() %>% flip_y())
  ) %>%
  ungroup()
df

enhance <- function(s) {
  df$to[which(df$from == s)[1]]
}

break_rows <- function(s, break_size) {
  s %>%
    str_split("/") %>%
    first() %>%
    enframe() %>%
    mutate(name = (name - 1) %/% break_size) %>%
    group_by(name) %>%
    summarise(value = str_c(value, collapse = "/")) %>%
    pull(value)
}

break_cols <- function(s, break_size) {
  s %>%
    str_split("/") %>%
    first() %>%
    map(str_extract_all, str_c(".{", break_size, "}")) %>%
    pmap(str_c, sep = "/") %>%
    unlist()
}

break_pixels <- function(s) {
  rows <- str_count(s, "/") + 1
  
  if (rows %% 2 == 0) {
    break_size <- 2
  } else if (rows %% 3 == 0) {
    break_size <- 3
  } else {
    stop(str_c("Unable to break rows: ", rows))
  }
  
  s %>%
    break_rows(break_size) %>%
    map(break_cols, break_size)
}

combine_rows <- function(s_vec) {
  str_c(s_vec, collapse = "/")
}

combine_cols <- function(s_vec) {
  s_vec %>%
    str_split("/") %>%
    pmap_chr(str_c, collapse = "") %>%
    str_c(collapse = "/")
}

combine_pixels <- function(s_grid) {
  s_grid %>% map_chr(combine_cols) %>% combine_rows()
}

simulate <- function(n, s = ".#./..#/###") {
  for (i in seq_len(n)) {
    s <-
      s %>%
      break_pixels() %>%
      map(map_chr, enhance) %>%
      combine_pixels()
  }
  s
}

result <- simulate(5)
answer <- str_count(result, "#")
answer

result <- simulate(18)
answer <- str_count(result, "#")
answer
