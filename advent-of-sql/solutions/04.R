library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

# sqlite does not have arrays so process them as strings
read_file("./data/2024/advent_of_sql_day_4.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("ARRAY\\[(.*?)\\]", '"\\1"') |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "toy_production") |>
  collect() |>
  mutate(
    previous_tags =
      previous_tags |>
      str_replace_all("'", "") |>
      str_split(", "),
    new_tags =
      new_tags |>
      str_replace_all("'", "") |>
      str_split(", "),
    added_tags = map2(new_tags, previous_tags, setdiff) |> map_int(length),
    unchanged_tags = map2(previous_tags, new_tags, intersect) |> map_int(length),
    removed_tags = map2(previous_tags, new_tags, setdiff) |> map_int(length)
  ) |>
  slice_max(added_tags) |>
  select(toy_id, added_tags, unchanged_tags, removed_tags) |>
  unlist() |>
  cat(sep = "\n")
