library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_0.sql") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "Children") |>
  inner_join(tbl(con, "ChristmasList")) |>
  filter(was_delivered == 1) |>
  distinct(child_id, country, city) |>
  group_by(city) |>
  filter(n() >= 5) |>
  distinct(country, city) |>
  inner_join(tbl(con, "Children")) |>
  group_by(country, city) |>
  summarise(
    mean_naughty_nice_score = mean(naughty_nice_score)
  ) |>
  ungroup() |>
  slice_max(mean_naughty_nice_score, n = 5) |>
  pull(city) |>
  cat(sep = "\n")
# Lyon
# Manchester
# Paris
# London
# Birmingham
