library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_21.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "sales") |>
  collect() |>
  mutate(
    year = year(sale_date),
    quarter = quarter(sale_date)
  ) |>
  group_by(year, quarter) |>
  summarise(total_sales  = sum(amount)) |>
  ungroup() |>
  mutate(
    growth_rate = (total_sales - lag(total_sales)) / lag(total_sales)
  ) |>
  slice_max(growth_rate) |>
  select(year, quarter) |>
  unlist() |>
  cat(sep = ",")
# 1997,4
