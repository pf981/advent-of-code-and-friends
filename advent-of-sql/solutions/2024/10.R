library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_10.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "Drinks") |>
  collect() |>
  pivot_wider(
    id_cols = date,
    names_from = drink_name,
    values_from = quantity,
    values_fn = sum
  ) |>
  rename_with(str_replace_all, pattern = " ", replacement = "") |>
  filter(
    HotCocoa == 38,
    PeppermintSchnapps == 298,
    Eggnog == 198
  ) |>
  pull(date)
# 2024-03-14
