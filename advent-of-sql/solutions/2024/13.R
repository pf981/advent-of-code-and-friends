library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

# sqlite does not have arrays so process them as strings
read_file("./data/2024/advent_of_sql_day_13.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_replace_all("ARRAY\\[(.*?)\\]", '"\\1"') |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  discard(str_starts, "DROP") |>
  walk(DBI::dbExecute, conn = con)


tbl(con, "contact_list") |>
  collect() |>
  mutate(
    email_addresses =
      email_addresses |>
      str_replace_all("'", "") |>
      str_split(", "),
  ) |>
  unnest_longer(email_addresses) |>
  mutate(
    domain = email_addresses |> str_replace(".*@", "")
  ) |>
  count(domain) |>
  slice_max(n) |>
  pull(domain)
# bells.org
