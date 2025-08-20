library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

read_file("./data/2024/advent_of_sql_day_7.sql") |>
  str_replace_all("CASCADE", "") |>
  str_split_1(";") |>
  str_trim() |>
  discard(\(line) line == "") |>
  walk(DBI::dbExecute, conn = con)

workshop_elves <-
  tbl(con, "workshop_elves") |>
  collect() |>
  group_by(primary_skill)

most_experienced <- workshop_elves |> slice_min(tibble(-years_experience, elf_id))

least_experienced <- workshop_elves |> slice_min(tibble(years_experience, elf_id))

most_experienced |>
  inner_join(least_experienced, by = join_by(primary_skill)) |>
  transmute(
    elf_1_id = elf_id.x,
    elf_2_id = elf_id.y,
    shared_skill = primary_skill
  ) |>
  arrange(shared_skill) |>
  format_csv(col_names = FALSE) |>
  cat()
# 4153,3611,Gift sorting
# 10497,1016,Gift wrapping
# 50,13551,Toy making
