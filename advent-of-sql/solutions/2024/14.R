library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_14.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_replace_all("ARRAY\\[(.*?)\\]", '"\\1"') |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  discard(str_starts, "DROP") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "SantaRecords") |>
  collect() |>
  mutate(
    cleaning_receipts = cleaning_receipts |> map(jsonlite::parse_json)
  ) |>
  unnest_longer(cleaning_receipts) |>
  unnest_wider(cleaning_receipts) |>
  filter(
    garment == "suit",
    color == "green"
  ) |>
  pull(drop_off) |>
  max()
# 2024-12-22
