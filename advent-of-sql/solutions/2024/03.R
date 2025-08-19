library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_3.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

tbl(con, "christmas_menus") |>
  collect() |>
  mutate(
    xml = map(menu_data, xml2::read_xml),
    guests =
      xml |>
      map(xml2::xml_find_first, "//total_present|//total_guests|//total_count") |>
      map_int(xml2::xml_integer),
    food_ids =
      xml |>
      map(xml2::xml_find_all, "//food_item_id") |>
      map(xml2::xml_integer)
  ) |>
  filter(guests > 78) |>
  pull(food_ids) |>
  unlist() |>
  enframe() |>
  count(value) |>
  slice_max(n) |>
  pull(value)
# 493
