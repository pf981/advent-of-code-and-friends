library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_5.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

DBI::dbListTables(con)

tbl(con, "toy_production") |>
  collect() |>
  arrange(production_date) |>
  mutate(
    previous_day_production = lag(toys_produced),
    production_change = toys_produced - previous_day_production,
    production_change_percentage = production_change / previous_day_production * 100
  ) |>
  slice_max(production_change_percentage) |>
  pull(production_date)
# 2017-03-20