library(tidyverse)



str_to_named_lgl <- function(x) {
  x <- str_split(x, ",? ")
  map(x, function(y) {
    rep(TRUE, length(y)) %>%
    set_names(y) %>%
    as.list() %>%
    as_tibble()
  })
}

foods <-
  input %>%
  read_lines() %>%
  as_tibble() %>%
  extract(
    value,
    c("ingredients", "allergens"),
    "(.*) \\(contains (.*)\\)"
  ) %>%
  mutate(
    ingredients = str_to_named_lgl(ingredients),
    allergens = str_to_named_lgl(allergens)
  )

all_ingredients <- foods %>% select(ingredients) %>% unnest_wider(ingredients) %>% names()
all_allergens <- foods %>% select(allergens) %>% unnest_wider(allergens) %>% names()

foods <-
  foods %>%
  unnest_wider(ingredients) %>%
  unnest_wider(allergens) %>%
  mutate_all(replace_na, FALSE)

foods

possible_allergen_ingredients <- NULL

for (ingredient in all_ingredients) {
  for (allergen in all_allergens) {
    if (all((foods[[allergen]] & foods[[ingredient]]) | !foods[[allergen]])) {
      possible_allergen_ingredients <- bind_rows(possible_allergen_ingredients, tibble(ingredient = ingredient, allergen = allergen))
    }
  }
}
possible_allergen_ingredients

definitely_non_allergen <- all_ingredients[!(all_ingredients %in% possible_allergen_ingredients$ingredient)]
definitely_non_allergen

answer <- foods %>% select(all_of(definitely_non_allergen)) %>% as.matrix() %>% sum()
answer

unconfirmed_allergen_ingredients <- possible_allergen_ingredients
confirmed_allergen_ingredients <- NULL

repeat {
  new_confirmed1 <-
    unconfirmed_allergen_ingredients %>%
    group_by(ingredient) %>%
    filter(n() == 1)
  
  new_confirmed2 <-
    unconfirmed_allergen_ingredients %>%
    group_by(allergen) %>%
    filter(n() == 1)
  
  new_confirmed <-
    bind_rows(new_confirmed1, new_confirmed2) %>% 
    ungroup() %>%
    distinct()
  
  if (nrow(new_confirmed) == 0) {
    break
  }
  
  confirmed_allergen_ingredients <- bind_rows(confirmed_allergen_ingredients, new_confirmed)
  
  unconfirmed_allergen_ingredients <-
    unconfirmed_allergen_ingredients %>%
    filter(
      !(ingredient %in% confirmed_allergen_ingredients$ingredient),
      !(allergen %in% confirmed_allergen_ingredients$allergen)
    )
}
lst(unconfirmed_allergen_ingredients, confirmed_allergen_ingredients)

answer <-
  confirmed_allergen_ingredients %>%
  arrange(allergen) %>%
  pull(ingredient) %>%
  str_c(collapse = ",")
answer
