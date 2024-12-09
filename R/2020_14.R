install.packages("binaryLogic")

library(binaryLogic)
library(tidyverse)



process_segment <- function(segment_lines) {
  mask <- segment_lines[[1]] %>% str_replace("mask = ", "")

  segment_lines[-1] %>%
    as_tibble() %>%
    extract(value, c("address", "value"), "mem\\[(\\d+)\\] = (\\d+)") %>%
    transmute(
      address = as.integer(address),
      value = as.integer(value),
      mask = mask
    )
}

input_lines <- read_lines(input)

mem <- map_dfr(
  split(input_lines, cumsum(str_detect(input_lines, "^mask = "))),
  process_segment
)
mem

# strtoi doesn't work because it can't handle integers this big
binary_str_to_dec <- function(x) {
  x %>%
    str_split("") %>%
    map(as.integer) %>%
    map(function(y) reduce(y, ~.x * 2 + .y))
}

result <-
  mem %>%
  mutate(
    value_bin = as.binary(value, n = 36),
    
    mask_1 = mask %>% chartr("X", "0", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    mask_0 = mask %>% chartr("1X0", "110", .) %>% binary_str_to_dec() %>% as.binary(n = 36),
    
    masked_bin = pmap(lst(value_bin, mask_1, mask_0), ~(..1 | ..2) & ..3),
    masked = map_dbl(masked_bin, as.double) # Can't use integer because it's too big
  )
result

answer <-
  result %>%
  group_by(address) %>%
  slice(n()) %>%
  ungroup() %>%
  summarise(answer = sum(masked)) %>%
  pull(answer)
format(answer, scientific = FALSE)

expand_mask <- function(mask) {
  replacement_grid <- expand.grid(
    rep(list(c("z", "1")), str_count(mask, "X")),
    stringsAsFactors = FALSE
  )
  
  result <- reduce(
    replacement_grid,
    str_replace,
    pattern = "X",
    .init = mask
  )
  
  tibble(
    mask_1 = result %>% chartr("z", "0", .),
    mask_0 = result %>% chartr("10z", "110", .)
  )
}

result <-
  mem %>%
  mutate(
    value_bin = as.binary(value, n = 36),
    mask = map(mask, expand_mask)
  ) %>%
  unnest(mask) %>%
  mutate(
    address_bin = as.binary(address, n = 36),
    mask_1 = mask_1 %>% binary_str_to_dec() %>% as.binary(n = 36),
    mask_0 = mask_0 %>% binary_str_to_dec() %>% as.binary(n = 36),
    address_masked_bin = pmap(lst(address_bin, mask_1, mask_0), ~(..1 | ..2) & ..3),
    address_masked = map_dbl(address_masked_bin, as.double)
  )
result

answer <-
  result %>%
  group_by(address_masked) %>%
  slice(n()) %>%
  ungroup() %>%
  summarise(answer = sum(as.double(value))) %>% # Too big for integer
  pull(answer)
format(answer, scientific = FALSE)
