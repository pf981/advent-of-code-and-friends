library(tidyverse)


text <- read_lines("data/2023-02.txt")



cubes <-
  text |>
  str_match_all("(\\d+) (red|green|blue)") |>
  map(as_tibble) |>
  list_rbind(names_to = "id") |>
  mutate(id, color = V3, num = as.integer(V2), .keep = "none") |>
  group_by(id, color) |>
  summarise(across(num, max))

answer1 <-
  cubes |>
  group_by(id) |>
  filter(all(num <= c(red = 12, green = 13, blue = 14)[color])) |>
  distinct(id) |>
  pull(id) |>
  sum()
print(answer1)




answer2 <-
  cubes |>
  group_by(id) |>
  summarise(power = prod(num)) |>
  pull(power) |>
  sum()
print(answer2)
