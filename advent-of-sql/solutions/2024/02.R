library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_2.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "letters_a") |>
  union_all(tbl(con, "letters_b")) |>
  arrange(id) |>
  pull(value) |>
  intToUtf8() |>
  str_remove_all("[^a-zA-Z !\"'(),-.:;?]") |>
  cat()
# Dear Santa, I hope this letter finds you well in the North Pole! I want a SQL course for Christmas!
