library(tidyverse)



input2 <- "children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"

columns <- c("children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes")

lines <- read_lines(input)

sues <-
  columns %>%
  map_dfc(~str_extract(lines, glue::glue("(?<={.x}: )\\d+")) %>% parse_number()) %>%
  set_names(columns) %>%
  rownames_to_column("id")

sues

target <-
  tibble(line = read_lines(input2)) %>%
  separate(line, into = c("name", "value"), sep = ": ", convert = TRUE) %>%
  pivot_wider()
target

sues %>%
  replace_na(target) %>%
  inner_join(target) %>%
  pull(id)

sues %>%
  replace_na(target %>% select(-cats, -trees, -pomeranians, -goldfish)) %>%
  mutate(
    cats = cats > target$cats,
    trees = trees > target$trees,
    pomeranians = pomeranians < target$pomeranians,
    goldfish = goldfish < target$goldfish
  ) %>%
  replace_na(list(
    cats = TRUE,
    trees = TRUE,
    pomeranians = TRUE,
    goldfish = TRUE
  )) %>%
  inner_join(
    target %>% mutate(cats = TRUE, trees = TRUE, pomeranians = TRUE, goldfish = TRUE)
  ) %>%
  pull(id)
