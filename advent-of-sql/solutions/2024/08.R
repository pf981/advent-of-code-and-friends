library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_8.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

managers <- tbl(con, "staff") |> collect() |> pull(manager_id)
managers[1] <- 1

staff_ids <- seq_along(managers)

dp <- rep_along(managers, NA_integer_)
dp[1] <- 1

while (!is_empty(staff_ids)) {
  dp[staff_ids] <- 1 + dp[managers[staff_ids]]
  staff_ids <- staff_ids |> keep(\(staff_id) is.na(dp[staff_id]))
}

max(dp)
# 24
