library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_8.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

managers <- tbl(con, "staff") |> collect() |> pull(manager_id)

dp <- rep_along(managers, NA_integer_)
dp[1] <- 1

get_path_length <- function(staff_id) {
  if (is.na(dp[staff_id])) {
    dp[staff_id] <- 1 + get_path_length(managers[staff_id])
  }
  return(dp[staff_id])
}

seq_along(managers) |>
  map_int(get_path_length) |>
  max()
# 24
