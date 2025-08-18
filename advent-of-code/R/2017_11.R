library(tidyverse)



df <-
  str_split(input, ",") %>%
  first() %>%
  enframe() %>%
  mutate(
    x = (value %in% c("se", "ne")) - (value %in% c("nw", "sw")),
    y = (value %in% c("n", "nw")) - (value %in% c("s", "se")),
    z = (value %in% c("s", "sw")) - (value %in% c("n", "ne")),
    d = (abs(cumsum(x)) + abs(cumsum(y)) + abs(cumsum(z))) / 2
  )
df

answer <- df %>% slice_tail(n = 1) %>% pull(d)
answer

answer <- df %>% pull(d) %>% max()
answer
