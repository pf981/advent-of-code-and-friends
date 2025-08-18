library(tidyverse)


g <- read_lines("data/2023-03.txt")




n_rows <- length(g)
n_cols <- str_length(g[[1]])
values <- integer()

construct_row <- function(locations, nums) {
  result <- rep_len(0, n_cols)
  for (i in seq_along(nums)) {
    result[seq(from = locations[i, 1], to = locations[i, 2], by = 1)] <- length(values) + i
  }
  values <<- c(values, as.integer(nums))
  result
}

values_matrix <-
  map2(str_locate_all(g, "\\d+"), str_extract_all(g, "\\d+"), construct_row) |>
  simplify2array() |>
  t()

touching_symbol <-
  str_locate_all(g, "[^0-9\\.]") |>
  map(as_tibble) |>
  list_rbind(names_to = "row") |>
  mutate(
    d = list(expand_grid(dr = seq(from = -1, to = 1, by = 1), dc = seq(from = -1, to = 1, by = 1)))
  ) |>
  unnest(d) |>
  mutate(
    row = row + dr,
    col = start + dc,
    .keep = "none"
  )

answer1 <-
  values_matrix[as.matrix(touching_symbol)] |>
  c() |>
  unique() |>
  (\(.) values[.])() |>
  sum()
print(answer1)




answer2 <-
  str_locate_all(g, fixed("*")) |>
  map(as_tibble) |>
  list_rbind(names_to = "row") |>
  mutate(
    d = list(expand_grid(dr = seq(from = -1, to = 1, by = 1), dc = seq(from = -1, to = 1, by = 1))),
  ) |>
  unnest(d) |>
  mutate(
    row,
    col = start,
    neighbor_row = row + dr,
    neighbor_col = col + dc,
    value_idx = values_matrix[cbind(neighbor_row, neighbor_col)],
    .keep = "none"
  ) |> 
  filter(value_idx != 0) |>
  group_by(row, col) |>
  distinct(value_idx) |>
  filter(n() == 2) |>
  summarise(gear_ratio = prod(values[value_idx])) |>
  pull(gear_ratio) |>
  sum()
print(answer2)
