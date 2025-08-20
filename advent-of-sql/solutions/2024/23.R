library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_23.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

vals <- tbl(con, "sequence_table") |> collect() |> pull(id)

seq(from = 1, to = max(vals)) |>
  enframe() |>
  filter(!(value %in% vals)) |>
  mutate(
    id = cumsum(value != lag(value, default = 0) + 1)
  ) |>
  select(id, value) |>
  group_by(id) |>
  nest() |>
  pull(data) |>
  map(unlist) |>
  map(str_c, collapse = ",") |>
  walk(cat, sep = "\n")
# 997,998,999,1000,1001
# 3761,3762,3763,3764,3765
# 6525,6526,6527
# 6529
# 9289,9290,9291,9292
