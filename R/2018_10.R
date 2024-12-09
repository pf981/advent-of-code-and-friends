library(tidyverse)



df <-
  read_lines(input) %>%
  str_extract_all("-?\\d+") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("x", "y", "dx", "dy"))
df

df %>%
  mutate(t = list(seq(from = 0, to = 200, by = 1) + 10400)) %>%
  unnest() %>%
  mutate(
    x = x + t * dx,
    y = y + t * dy
  ) %>%
  ggplot(aes(x, y)) +
  geom_point(size = 0.1, alpha = 0.5) +
  scale_y_reverse() +
  theme_void() +
  facet_wrap(~t, scales = "free")

t <- 10521
df %>%
  mutate(x = x + t * dx, y = y + t * dy) %>%
  ggplot(aes(x, y)) +
    geom_point(size = 4, shape = 15) +
    scale_y_reverse(limits = c(200, 0)) +
    theme_void()

answer <- t
answer
