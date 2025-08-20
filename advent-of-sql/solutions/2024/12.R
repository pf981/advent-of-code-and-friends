library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_12.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  discard(str_starts, "DROP") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "gift_requests") |>
  inner_join(tbl(con, "gifts")) |>
  count(gift_name) |>
  collect() |>
  transmute(
    gift_name,
    overall_rank =
      percent_rank(n) |>
      round(2) |>
      format(nsmall = 2)
  ) |>
  arrange(desc(overall_rank), gift_name) |>
  filter(overall_rank != max(overall_rank)) |>
  head(1) |>
  unlist() |>
  cat(sep = "\n")
# chemistry set
# 0.86
