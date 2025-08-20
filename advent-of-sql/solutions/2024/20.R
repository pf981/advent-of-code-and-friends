library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_20.sql") |>
  str_replace_all("CASCADE", "") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)


tbl(con, "web_requests") |>
  collect() |>
  mutate(
    params =
      url |>
      str_replace_all("^.+\\?", "") |>
      str_split("&"),
    n =
      params |>
      map(str_replace, "=.*", "") |>
      map(unique) |>
      map_int(length)
  ) |>
  filter(
    params |> map_lgl(~"utm_source=advent-of-sql" %in% .x)
  ) |>
  arrange(desc(n), url) |>
  head(1) |>
  pull(url)
# http://abbott.biz?sapiente_incidunt_quisquam_saepe=tempore-vel-labore-vel&eos-fugit-veniam-alias=voluptatum_officia_esse_ut_numquam&ea_voluptas=possimus-iure-doloribus-ab-dolorum&utm_source=advent-of-sql
