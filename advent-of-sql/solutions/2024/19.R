library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_19.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_replace_all("ARRAY\\[(.*?)\\]", '"\\1"') |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "employees") |>
  collect() |>
  mutate(
    last_score =
      year_end_performance_scores |>
      str_split(",") |>
      map_chr(last) |>
      as.integer(),
    bonus = ifelse(last_score > mean(last_score), 0.15 * salary, 0)
  ) |>
  summarise(
    total_salary_with_bonuses = sum(salary + bonus)
  ) |>
  pull() |>
  format(1.1, nsmall = 2) |>
  cat()
# 5491552488.10
