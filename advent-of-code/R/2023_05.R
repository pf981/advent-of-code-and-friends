library(tidyverse)


text <- read_file("data/2023-05.txt")




lines <- str_split_1(text, "\n\n")
seeds <-
  lines[[1]] |>
  str_extract_all("\\d+", simplify = TRUE) |>
  as.numeric()

m <-
  lines[-1] |>
  map(read_lines) |>
  map(\(.) {
    .[-1] |>
      str_extract_all("\\d+", simplify = TRUE) |>
      as_tibble() |>
      set_names(c("dest_start", "source_start", "range_len")) |>
      mutate(across(everything(), as.numeric))
  })

get_location <- function(value, step) {
  if (step > length(m)) return(value)
  
  dest <-
    m[[step]] |>
    mutate(
      is_valid = value >= source_start & value < source_start + range_len,
      dest = dest_start + value - source_start
    ) |>
    filter(value >= source_start & value < source_start + range_len) |>
    pull(dest)
  
  get_location(c(dest, value)[[1]], step + 1)
}

answer1 <-
  seeds |>
  map_dbl(get_location, step = 1) |>
  min()
print(answer1)




get_seed <- function(value, step) {
  if (step == 0) return(value)
  
  dest <-
    m[[step]] |>
    rename(source_start = dest_start, dest_start = source_start) |>
    mutate(
      is_valid = value >= source_start & value < source_start + range_len,
      dest = dest_start + value - source_start
    ) |>
    filter(value >= source_start & value < source_start + range_len) |>
    pull(dest)
  
  get_seed(c(dest, value)[[1]], step - 1)
}

candidates <- numeric()
for (i in seq_along(m)) {
  new_candidates <- 
    c(
      m[[i]]$dest_start,
      m[[i]]$dest_start + m[[i]]$range_len - 1
    ) |>
    map_dbl(\(.) get_seed(., i))
  candidates <- c(candidates, new_candidates)
}

candidates <-
  seeds |>
  split(cumsum(seq_along(seeds) %% 2)) |>
  simplify2array() |>
  t() |>
  as_tibble() |>
  mutate(candidate = list(candidates)) |>
  unnest(candidate) |>
  filter(candidate >= V1 & candidate < V1 + V2) |>
  distinct(candidate) |>
  pull()

answer2 <-
  candidates |>
  map_dbl(get_location, step = 1) |>
  min()
print(answer2)
