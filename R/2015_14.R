library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    reindeer = str_extract(line, "^\\w+"),
    speed = str_extract(line, "\\d+") %>% parse_number(),
    flight_time = str_extract(line, "(?<=for )\\d+") %>% parse_number(),
    rest_time = str_extract(line, "(?<=rest for )\\d+") %>% parse_number()
  )
df

t <- 2503

answer <-
  df %>%
  mutate(
    d_round = t %/% (flight_time + rest_time) * (flight_time * speed),
    d_extra = pmin(t %% (flight_time + rest_time), flight_time) * speed,
    d = d_round + d_extra
  ) %>%
  pull(d) %>%
  max()
answer

answer <-
  df %>%
  crossing(t = seq_len(2503))  %>%
  mutate(
    d_round = t %/% (flight_time + rest_time) * (flight_time * speed),
    d_extra = pmin(t %% (flight_time + rest_time), flight_time) * speed,
    d = d_round + d_extra
  ) %>%
  group_by(t) %>%
  filter(d == max(d)) %>%
  ungroup() %>%
  count(reindeer) %>%
  pull(n) %>%
  max()
answer
