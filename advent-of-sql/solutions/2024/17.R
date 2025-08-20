library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_17.sql") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "Workshops") |>
  collect() |>
  mutate(
    start_time = map2(business_start_time, timezone, ~ymd_hm(str_c("2000-01-01 ", .x), tz = .y) |> with_tz("UTC"))
  ) |>
  unnest(start_time) |>
  pull(start_time) |>
  max() |>
  format("%H:%M:%S")
# 14:30:00
