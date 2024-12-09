# install.packages("DescTools")

library(tidyverse)



# 

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    disc = str_extract(line, "\\d+") %>% parse_integer(),
    positions = str_extract(line, "\\d+(?= positions)") %>% parse_integer(),
    start_position = str_extract(line, "\\d+(?=\\.)") %>% parse_integer()
  )

total_positions <- DescTools::LCM(df$positions)

df <-
  df %>%
  mutate(
    step_size = total_positions / positions,
    true_start = step_size * (start_position + disc)
  )

lst(total_positions, df)

create_f <- function(true_start, step_size, total_positions) {
  function(t) {
    (true_start + step_size * t) %% total_positions == 0
  }
}

fs <-
  df %>%
  mutate(
    f = pmap(lst(true_start, step_size, total_positions), create_f)
  ) %>%
  pull(f)

fs

t <- 1
repeat {
  if (all(map_lgl(fs, ~.(t)))) {
    break
  }
  t <- t + 1
}
t

df <-
  tibble(
    line = c(
      read_lines(input),
      "Disc #7 has 11 positions; at time=0, it is at position 0."
    )
  ) %>%
  mutate(
    disc = str_extract(line, "\\d+") %>% parse_integer(),
    positions = str_extract(line, "\\d+(?= positions)") %>% parse_integer(),
    start_position = str_extract(line, "\\d+(?=\\.)") %>% parse_integer()
  )

total_positions <- DescTools::LCM(df$positions)

df <-
  df %>%
  mutate(
    step_size = total_positions / positions,
    true_start = step_size * (start_position + disc)
  )

lst(total_positions, df)

fs <-
  df %>%
  mutate(
    f = pmap(lst(true_start, step_size, total_positions), create_f)
  ) %>%
  pull(f)

fs

t <- 1
repeat {
  if (all(map_lgl(fs, ~.(t)))) {
    break
  }
  t <- t + 1
}
t
