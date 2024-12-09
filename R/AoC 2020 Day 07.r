library(tidyverse)



bags <-
  input %>%
  read_lines() %>%
  as_tibble() %>%
  separate(value, c("outer", "inner"), " bags contain ") %>%
  mutate(inner = str_split(inner, ", ")) %>%
  unnest(inner) %>%
  separate(inner, c("num", "inner"), extra = "merge", remove = FALSE) %>%
  mutate(
    num = as.integer(num),
    inner = str_remove(inner, " bags?\\.?$"),
    outer = str_remove(outer, " bags?\\.?$")
  ) %>%
  filter(inner != "other")
bags

outer_bags <- bags %>% filter(inner == "shiny gold") %>% pull(outer) %>% unique()
repeat {
  new_outer_bags <- bags %>% filter(inner %in% outer_bags) %>% pull(outer) %>% unique()
  
  if (all(new_outer_bags %in% outer_bags)) {
    break
  }
  
  outer_bags = union(outer_bags, new_outer_bags)
}
outer_bags

answer <- outer_bags %>% length()
answer

count_inner_bags <- function(bag) {
  bags %>%
    filter(outer == bag) %>%
    mutate(
      inner_bags = map_int(inner, count_inner_bags),
      total = num + num * inner_bags
    ) %>%
    pull(total) %>%
    sum()
}

answer <- count_inner_bags("shiny gold")
answer
