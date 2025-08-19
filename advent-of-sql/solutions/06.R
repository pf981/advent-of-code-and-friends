library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_6.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

gifts <- tbl(con, "gifts") |> collect()
mean_gift_price <- gifts |> pull(price) |> mean()

tbl(con, "children") |>
  collect() |>
  inner_join(gifts |> select(child_id, price)) |>
  filter(price > mean_gift_price) |>
  arrange(price)
# Hobart
  