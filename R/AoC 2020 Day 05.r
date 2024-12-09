library(tidyverse)




seats <-
  input %>%
  read_lines() %>%
  as_tibble() %>%
  mutate(
    row_id = value %>%
      str_replace_all("B", "1") %>%
      str_replace_all("F", "0") %>%
      str_sub(1, 7) %>%
      strtoi(base = 2),
    col_id = value %>%
      str_replace_all("R", "1") %>%
      str_replace_all("L", "0") %>%
      str_sub(8, 10) %>%
      strtoi(base = 2),
    seat_id = row_id * 8 + col_id
  )

answer <- max(seats$seat_id)
answer

i <- seq(from = min(seats$seat_id), to = max(seats$seat_id), by = 1)
answer <- i[!(i %in% seats$seat_id)]
answer
