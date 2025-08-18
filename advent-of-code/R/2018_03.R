library(tidyverse)



df <-
  input %>%
  read_lines() %>%
  str_match("(\\d+).+?(\\d+).+?(\\d+).+?(\\d+).+?(\\d+)") %>%
  as_tibble() %>%
  transmute(
    id = V2,
    left = V3,
    top = V4,
    width = V5,
    height = V6
  ) %>%
  mutate_all(as.integer)
df

m <- matrix(0, ncol = 1500, nrow = 1500)

for (i in seq_len(nrow(df))) {
  rows <- seq(
    from = df$top[i] + 1,
    to = df$top[i] + df$height[i],
    by = 1,
  )
  cols <- seq(
    from = df$left[i] + 1,
    to = df$left[i] + df$width[i],
    by = 1,
  )
  m[rows, cols] <- m[rows, cols] + 1
}

answer <- sum(m > 1)
answer

for (i in seq_len(nrow(df))) {
  rows <- seq(
    from = df$top[i] + 1,
    to = df$top[i] + df$height[i],
    by = 1,
  )
  cols <- seq(
    from = df$left[i] + 1,
    to = df$left[i] + df$width[i],
    by = 1,
  )
  if(all(m[rows, cols] == 1)) break
}
answer <- df$id[i]
answer
