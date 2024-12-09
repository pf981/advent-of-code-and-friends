library(tidyverse)



active <-
  input %>%
  read_lines() %>%
  str_locate_all("#") %>%
  imap_dfr(~tibble(x = .x[,'start'], y = .y, z = 0))
active

neighbors_offset <-
  expand_grid(
    delta_x = seq(from = -1, to = 1, by = 1),
    delta_y = seq(from = -1, to = 1, by = 1),
    delta_z = seq(from = -1, to = 1, by = 1)
  ) %>%
  filter(!(delta_x == 0 & delta_y == 0 & delta_z == 0))
neighbors_offset

get_neighbors <- function(active) {
  active %>%
    inner_join(neighbors_offset, by = character()) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z
    )
}

sim <- function(active) {
  neighbors <- get_neighbors(active)
  
  new_active1 <- inner_join(
    active,
    neighbors %>% count(x, y, z) %>% filter(n %in% c(2, 3))
  )
  
  new_active2 <- anti_join(
    neighbors %>% count(x, y, z) %>% filter(n == 3),
    active
  )
  
  bind_rows(new_active1, new_active2) %>% distinct() %>% select(-n) # I don't think I need distinct but won't hurt
}

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

answer <- nrow(result)
answer

active <- active %>% mutate(w = 0)
active

neighbors_offset <-
  expand_grid(
    delta_x = seq(from = -1, to = 1, by = 1),
    delta_y = seq(from = -1, to = 1, by = 1),
    delta_z = seq(from = -1, to = 1, by = 1),
    delta_w = seq(from = -1, to = 1, by = 1)
  ) %>%
  filter(!(delta_x == 0 & delta_y == 0 & delta_z == 0 & delta_w == 0))
neighbors_offset

get_neighbors <- function(active) {
  active %>%
    inner_join(neighbors_offset, by = character()) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z,
      w = w + delta_w
    )
}

sim <- function(active) {
  neighbors <- get_neighbors(active)
  
  new_active1 <- inner_join(
    active,
    neighbors %>% count(x, y, z, w) %>% filter(n %in% c(2, 3))
  )
  
  new_active2 <- anti_join(
    neighbors %>% count(x, y, z, w) %>% filter(n == 3),
    active
  )
  
  bind_rows(new_active1, new_active2) %>% distinct() %>% select(-n) # I don't think I need distinct but won't hurt
}

result <- active
for (i in seq_len(6)) {
  result <- sim(result)
}
result

answer <- nrow(result)
answer
