library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_11.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "TreeHarvests") |>
  collect() |>
  mutate(
    season = fct(season, levels = c("Spring", "Summer", "Fall", "Winter"))
  ) |>
  group_by(field_name) |>
  arrange(harvest_year, season) |>
  mutate(
    three_season_moving_avg = (trees_harvested + lag(trees_harvested, 1, 0) + lag(trees_harvested, 2, 0)) / pmin(row_number(), 3)
  ) |>
  pull(three_season_moving_avg) |>
  max() |>
  round(2) |>
  format(nsmall = 2)
# 327.67
