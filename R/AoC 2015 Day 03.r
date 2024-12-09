library(tidyverse)



df <-
  tibble(instruction = c("x", str_split(input, "")[[1]])) %>%
  mutate(
    x = cumsum(str_count(instruction, fixed(">")) - str_count(instruction, fixed("<"))),
    y = cumsum(str_count(instruction, fixed("^")) - str_count(instruction, fixed("v")))
  )
df

answer <- df %>% distinct(x, y) %>% nrow()
answer

santa <-
  df %>%
  filter(row_number() == 1 | row_number() %% 2 == 0) %>%
  mutate(
    x = cumsum(str_count(instruction, fixed(">")) - str_count(instruction, fixed("<"))),
    y = cumsum(str_count(instruction, fixed("^")) - str_count(instruction, fixed("v")))
  )

santa_robot <-
  df %>%
  filter(row_number() %% 2 == 1) %>%
  mutate(
    x = cumsum(str_count(instruction, fixed(">")) - str_count(instruction, fixed("<"))),
    y = cumsum(str_count(instruction, fixed("^")) - str_count(instruction, fixed("v")))
  )

answer <- bind_rows(santa, santa_robot) %>% distinct(x, y) %>% nrow()
answer
