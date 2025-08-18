library(tidyverse)



df <-
  read_table(input, col_names = "string") %>%
  mutate(
    is_nice = str_count(string, "[aeiou]") >= 3 & str_detect(string, "(.)\\1") & !str_detect(string, "ab|cd|pq|xy")
  )
df

answer <- sum(df$is_nice)
answer

answer <-
  df %>%
  mutate(
    is_nice = str_detect(string, "(..).*\\1") & str_detect(string, "(.).\\1")
  ) %>%
  pull(is_nice) %>%
  sum()
answer
