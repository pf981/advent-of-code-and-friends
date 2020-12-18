# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/17

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- ".#.####.
.#...##.
..###.##
#..#.#.#
#..#....
#.####..
##.##..#
#.#.#..#
"

# COMMAND ----------

input <- ".#.
..#
###
"

# COMMAND ----------

active <-
  input %>%
  read_lines() %>%
  str_locate_all("#") %>%
  imap_dfr(~tibble(x = .x[,'start'], y = .y, z = 0))
active

# COMMAND ----------

neighbors_offset <-
  expand_grid(
    delta_x = seq(from = -1, to = 1, by = 1),
    delta_y = seq(from = -1, to = 1, by = 1),
    delta_z = seq(from = -1, to = 1, by = 1)
  ) %>%
  filter(!(delta_x == 0 & delta_y == 0 & delta_z == 0))
neighbors_offset

# COMMAND ----------

cross_join <- function(a, b) {
  full_join(
    a %>% add_column(.dummy = TRUE),
    b %>% add_column(.dummy = TRUE),
    by = ".dummy"
  ) %>%
   select(-.dummy)
}

# COMMAND ----------

get_neighbors <- function(active) {
  active %>%
    cross_join(neighbors_offset) %>%
    transmute(
      x = x + delta_x,
      y = y + delta_y,
      z = z + delta_z
    )
}

# COMMAND ----------

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
  
  bind_rows(new_active1, new_active2)
}

# COMMAND ----------

print_slice <- function(active) {
  cat(paste0("\n\nz=", active$z[[1]], "\n"))
  active <-
    active %>%
    mutate(
      x = x - min(x) + 1,
      y = y - min(y) + 1
    )
  m <- matrix(".", nrow = max(active$x), ncol = max(active$y))
  m[cbind(active$x, active$y)] <- "#"
  cat(apply(m, 2, paste0, collapse = "") %>% paste0(collapse = "\n"))
}

# COMMAND ----------

print_state <- function(active) {
  for (cur_z in sort(unique(active$z))) {
    active %>%
      filter(z == cur_z) %>%
      print_slice()
  }
  invisible()
}

# COMMAND ----------

print_state(active)

# COMMAND ----------

print_state(sim(active))

# COMMAND ----------

get_neighbors(active) %>%
  count(x, y, z) %>%
  ggplot(aes(x, y, label = n)) +
    geom_label() +
    facet_grid(~z) +
    scale_y_reverse()
# This looks correct

# COMMAND ----------

  neighbors <- get_neighbors(active)
  
  new_active1 <- inner_join(
    active,
    neighbors %>% count(x, y, z) %>% filter(n %in% c(2, 3))
  )
  
  new_active2 <- anti_join(
    neighbors %>% count(x, y, z) %>% filter(n == 3),
    active
  )
  
  bind_rows(new_active1, new_active2)

# COMMAND ----------

new_active1 #%>% print_state()

# COMMAND ----------

new_active2 %>% arrange(z, y, x)

# COMMAND ----------

  bind_rows(new_active1, new_active2) %>% print_state()

# COMMAND ----------

 bind_rows(new_active1, new_active2) %>% arrange(z, y, x)

# COMMAND ----------

 bind_rows(new_active1, new_active2) %>% arrange(z, y, x) %>% filter(z == 0) 

# COMMAND ----------

 bind_rows(new_active1, new_active2) %>% arrange(z, y, x) %>% filter(z == 0) %>% print_slice()

# COMMAND ----------

# MAGIC %md The issue is with print_slice.

# COMMAND ----------

# active2 <- active

# COMMAND ----------

# active <-  bind_rows(new_active1, new_active2) %>% arrange(z, y, x) %>% filter(z == 0)

# COMMAND ----------

print_slice <- function(active) {
  cat(paste0("\n\nz=", active$z[[1]], "\n"))
  active <-
    active %>%
    mutate(
      x = x - min(x) + 1,
      y = y - min(y) + 1
    )
  m <- matrix(".", nrow = max(active$x), ncol = max(active$y))
  m[cbind(active$x, active$y)] <- "#"
  cat(apply(m, 2, paste0, collapse = "") %>% paste0(collapse = "\n"))
}

# COMMAND ----------

print_slice <- function(active) {
  cat(paste0("\n\nz=", active$z[[1]], "\n"))
  active <-
    active %>%
    mutate(
      x = x - min(x) + 1,
      y = y - min(y) + 1
    )
  m <- matrix(".", nrow = max(active$x), ncol = max(active$y))
  m[cbind(active$x, active$y)] <- "#"
  cat(apply(m, 1, paste0, collapse = "") %>% paste0(collapse = "\n"))
}