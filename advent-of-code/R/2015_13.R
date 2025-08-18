install.packages("combinat")

library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    a = str_extract(line, "^\\w+"),
    b = str_extract(line, "\\w+(?=\\.$)"),
    happiness = parse_number(line) * ifelse(str_detect(line, "would lose"), -1, 1),
    index = str_c(a, b)
  )
df

people <- df %>% pull(a) %>% unique()
people

standardize_start <- function(x) {
  start_i <- order(x)[1] - 1
  
  if (start_i == 0) {
    x
  } else {
    c(tail(x, -start_i), head(x, start_i))
  }
}

permutations <-
  combinat::permn(people) %>%
  map(standardize_start) %>%
  discard(duplicated(map_chr(., str_c, collapse = "")))

compute_happiness <- function(seating) {
  indices <- c(
    str_c(seating, lead(seating, default = first(seating))),
    str_c(seating, lag(seating, default = last(seating)))
  )
  df %>%
    filter(index %in% indices) %>%
    pull(happiness) %>%
    sum()
}

answer <- permutations %>% map_dbl(compute_happiness) %>% max()
answer

new_rows <-
  bind_rows(
    tibble(
      a = people,
      b = "paul"
    ),
    tibble(
      a = "paul",
      b = people
    )
  ) %>%
  mutate(index = str_c(a, b), happiness = 0)

df <- bind_rows(df, new_rows)

people <- c(people, "paul")

permutations <-
  combinat::permn(people) %>%
  map(standardize_start) %>%
  discard(duplicated(map_chr(., str_c, collapse = "")))

answer <- permutations %>% map_dbl(compute_happiness) %>% max()
answer
