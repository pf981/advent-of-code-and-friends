library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_8.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

managers <- tbl(con, "staff") |> collect() |> pull(manager_id)
staff_ids <- seq_along(managers)
result <- 0
while (!is_empty(staff_ids)) {
  staff_ids <- managers[staff_ids] |> discard(is.na)
  result <- result + 1
}
result
# 24
