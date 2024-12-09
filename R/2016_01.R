library(tidyverse)



x_coef <- c(0, 1, 0, -1)
y_coef <- c(1, 0, -1, 0)

directions <-
  tibble(instruction = str_split(input, ", ") %>% first()) %>%
  transmute(
    turn = str_extract(instruction, "[A-Z]"),
    d = str_extract(instruction, "\\d+") %>% parse_integer(),
    heading = cumsum(ifelse(turn == "R", 1, -1)) %% 4 + 1,
    x = cumsum(x_coef[heading] * d),
    y = cumsum(y_coef[heading] * d),
    blocks = abs(x) + abs(y)
  )

directions

directions %>%
  slice(n()) %>%
  pull(blocks)

directions %>%
  mutate(d = map(d, ~rep(1, .))) %>%
  unnest() %>%
  mutate(
    x = cumsum(x_coef[heading] * d),
    y = cumsum(y_coef[heading] * d),
    blocks = abs(x) + abs(y)
  ) %>%
  group_by(x, y) %>%
  filter(n() > 1) %>%
  ungroup() %>%
  slice(1) %>%
  pull(blocks)
