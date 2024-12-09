library(tidyverse)


width <- 25
height <- 6

# 
# width <- 3
# height <- 2

even_split <- function(x, n) {
  starts <- seq(from = 1, to = nchar(x), by = n)
  str_sub(x, starts, starts + n - 1)
}

input %>%
  even_split(width * height) %>%
  as_tibble() %>%
  mutate(
    n_0 = str_count(value, "0"),
    n_1 = str_count(value, "1"),
    n_2 = str_count(value, "2")
  ) %>%
  arrange(n_0) %>%
  head(1) %>%
  summarise(result = n_1 * n_2) %>%
  pull(result)

# 
# width <- 2
# height <- 2

result <-
  input %>%
  even_split(width * height) %>%
  str_split("") %>%
  map(function(x) {
    modify_if(x, ~. == "2", ~NA)
  }) %>%
  reduce(coalesce) %>%
  str_c(collapse = "")

result %>% even_split(width) %>% str_c(collapse = "\n") %>% cat()

result %>%
  even_split(width) %>%
  str_c(collapse = "\n") %>%
  str_replace_all("1", "#") %>%
  str_replace_all("0", " ") %>%
  cat()
#> CEKUA