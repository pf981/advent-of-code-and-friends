library(tidyverse)



df <-
  read_table(input, col_names = "dimensions") %>%
  separate(dimensions, into = c("l", "w", "h"), sep = "x", convert = TRUE) %>%
  mutate(surface_area = 2*l*w + 2*w*h + 2*h*l + pmin(l*w, w*h, h*l))

answer <- df %>% pull(surface_area) %>% sum()
answer

answer <-
  df %>%
  mutate(ribbon_length = 2 * pmin(l+w, w+h, h+l) + l*w*h) %>%
  pull(ribbon_length) %>%
  sum()
answer
