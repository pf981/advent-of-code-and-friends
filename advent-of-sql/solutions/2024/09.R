library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_9.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "Training_Sessions") |>
  inner_join(tbl(con, "Reindeers")) |>
  filter(reindeer_name != "Rudolph") |>
  group_by(reindeer_name, exercise_name) |>
  summarise(top_speed = mean(speed_record, na.rm = TRUE)) |>
  group_by(reindeer_name) |>
  summarise(top_speed = max(top_speed)) |>
  arrange(desc(top_speed)) |>
  head(3) |>
  collect() |>
  mutate(top_speed = format(round(top_speed, 2), nsmall = 2)) |>
  format_csv(col_names = FALSE) |>
  cat()
# Cupid,88.64
# Blitzen,88.38
# Vixen,88.01
