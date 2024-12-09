library(tidyverse)



# 

parse_line <- function(line, i = 1) {
  line %>%
    str_extract_all("(?<=<).+?(?=>)") %>%
    first() %>%
    str_split(",") %>%
    map(parse_number) %>%
    simplify2array() %>%
    as_tibble() %>%
    set_names("p", "v", "a") %>%
    add_column(id = i - 1)
}

df <-
  read_lines(input) %>%
  imap_dfr(parse_line)
df

update_state <- function(state) {
  state %>%
    mutate(
      v = v + a,
      p = p + v
    )
}

simulate <- function(state, n) {
  for (i in seq_len(n)) {
    state <- update_state(state)
  }
  state
}

result <- simulate(df, 1000)
answer <-
  result %>%
  group_by(id) %>%
  summarise(d = sum(abs(p))) %>%
  arrange(d) %>%
  pull(id) %>%
  first()
answer

update_state2 <- function(state) {
  state <-
    state %>%
    mutate(
      v = v + a,
      p = p + v
    )
  
  valid_ids <-
    state %>%
    group_by(id) %>%
    summarise(hash = str_c(p, collapse = ",")) %>%
    group_by(hash) %>%
    filter(n() == 1) %>%
    pull(id)
  state %>% filter(id %in% valid_ids)
}

simulate2 <- function(state, n) {
  for (i in seq_len(n)) {
    state <- update_state2(state)
  }
  state
}

result <- simulate2(df, 1000)

answer <-
  result %>%
  pull(id) %>%
  unique() %>%
  length()
answer
