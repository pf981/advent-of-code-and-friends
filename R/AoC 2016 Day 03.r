library(tidyverse)



df <- read_table(input, col_names = c("s1", "s2", "s3"))
df

answer <-
  df %>%
  filter(
    s1 < s2 + s3,
    s2 < s1 + s3,
    s3 < s1 + s2
  ) %>%
  nrow()
answer

answer <-
  matrix(c(df$s1, df$s2, df$s3), ncol = 3, byrow = TRUE) %>%
  as_tibble() %>%
  set_names(c("s1", "s2", "s3")) %>%
  filter(
    s1 < s2 + s3,
    s2 < s1 + s3,
    s3 < s1 + s2
  ) %>%
  nrow()
answer
