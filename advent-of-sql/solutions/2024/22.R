library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_22.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "elves") |>
  collect() |>
  mutate(
    skills = skills |> str_split(","),
    has_sql = skills |> map_lgl(~"SQL" %in% .)
  ) |>
  pull(has_sql) |>
  sum()
# 2488
