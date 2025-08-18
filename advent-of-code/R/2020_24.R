library(tidyverse)



tiles <- input %>% read_lines() %>% str_extract_all("(e|se|sw|w|nw|ne)")
tiles

paths <-
  tiles %>%
  enframe(name = "path_id", value = "direction") %>%
  unnest(direction) %>%
  mutate(
    x = case_when(
      direction == "e"  ~ 2,
      direction == "se" ~ 1,
      direction == "sw" ~ -1,
      direction == "w"  ~ -2,
      direction == "nw" ~ -1,
      direction == "ne" ~ 1,
    ),
    y = case_when(
      direction == "e"  ~ 0,
      direction == "se" ~ -1,
      direction == "sw" ~ -1,
      direction == "w"  ~ 0,
      direction == "nw" ~ 1,
      direction == "ne" ~ 1,
    )
  )
paths

black_tiles <-
  paths %>%
  group_by(path_id) %>%
  summarise(x = sum(x), y = sum(y)) %>%
  count(x, y) %>%
  filter((n %% 2) == 1) %>%
  select(-n)

answer <- black_tiles %>% nrow()
answer

adjacent_delta <- tribble(
  ~dx, ~dy,
    2,   0,
   -2,   0,
    1,   1,
   -1,   1,
   -1,   -1,
    1,  -1
)
adjacent_delta

simulate_impl <- function(black_tiles) {
  neighbor_black_count <-
    black_tiles %>%
    mutate(delta = list(adjacent_delta)) %>%
    unnest(delta) %>%
    transmute(
      x = x + dx,
      y = y + dy
    ) %>%
    count(x, y) %>%
    ungroup() # Unneeded?
  
  new_black <- neighbor_black_count %>% filter(n == 2) %>% select(-n)
  
  new_white <- bind_rows(
    neighbor_black_count %>% filter(n > 2),
    anti_join(black_tiles, neighbor_black_count) # n == 0
  ) %>%
    select(-n)
  
  bind_rows(
    anti_join(black_tiles, new_white),
    anti_join(new_black, black_tiles)
  ) %>%
    distinct()
}

simulate <- function(black_tiles, n_times = 1) {
  for (i in seq_len(n_times)) {
    black_tiles <- simulate_impl(black_tiles)
  }
  black_tiles
}

plot_tiles <- function(black_tiles) {
  neighbor_black_count <-
    black_tiles %>%
    mutate(delta = list(adjacent_delta)) %>%
    unnest(delta) %>%
    transmute(
      x = x + dx,
      y = y + dy
    ) %>%
    count(x, y) %>%
    ungroup()

  ggplot(mapping = aes(x, y)) +
    geom_label(data = neighbor_black_count, mapping = aes(label = n), size = 2) +
    geom_point(data = black_tiles, size = 5, alpha = 0.3, color = "red") +
    theme_void()
}
plot_tiles(black_tiles)

answer <- simulate(black_tiles, 100) %>% nrow()
answer
