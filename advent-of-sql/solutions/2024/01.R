library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_1.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  map(DBI::dbExecute, conn = con)

result <-
  tbl(con, "wish_lists") |>
  collect() |>
  mutate(wishes = map(wishes, jsonlite::parse_json)) |>
  unnest_wider(wishes) |>
  inner_join(tbl(con, "children") |> collect()) |>
  inner_join(
    tbl(con, "toy_catalogue") |> collect(),
    by = join_by(first_choice == toy_name)
  ) |>
  transmute(
    name,
    primary_wish = first_choice,
    backup_wish = second_choice,
    favorite_color = map_chr(colors, first),
    color_count = map_int(colors, length),
    gift_complexity = case_when(
      difficulty_to_make == 1 ~ "Simple Gift",
      difficulty_to_make == 2 ~ "Moderate Gift",
      .default = "Complex Gift"
    ),
    workshop_assignment = case_when(
      category == "outdoor" ~ "Outside Workshop",
      category == "educational" ~ "Learning Workshop",
      .default = "General Workshop"
    )
  ) |>
  arrange(name) |>
  head(5)

result |>
  format_csv(col_names = FALSE) |>
  cat()
# Abagail,Building sets,LEGO blocks,Blue,1,Complex Gift,Learning Workshop
# Abbey,Barbie dolls,Play-Doh,Purple,1,Moderate Gift,General Workshop
# Abbey,Toy trains,Toy trains,Pink,2,Complex Gift,General Workshop
# Abbey,Stuffed animals,Teddy bears,White,4,Complex Gift,General Workshop
# Abbey,Yo-yos,Building blocks,Blue,5,Simple Gift,General Workshop
