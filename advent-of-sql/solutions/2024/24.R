library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_24.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "user_plays") |>
  inner_join(tbl(con, "songs")) |>
  collect() |># View()
  group_by(song_title) |>
  summarise(
    total_plays = sum(duration == song_duration, na.rm = TRUE),
    total_skips = sum(is.na(duration) | duration != song_duration),
  ) |>
  arrange(desc(total_plays), total_skips) |>
  head(1) |>
  pull(song_title)
# All I Want For Christmas Is You
