library(tidyverse)



nums <-
  input %>%
  read_lines() %>%
  parse_number()

entries <- nums[(2020 - nums) %in% nums]
entries

answer <- reduce(entries, `*`)
answer

result <-
  expand_grid(x1 = nums, x2 = nums, x3 = nums) %>%
  filter(x1 + x2 + x3 == 2020) %>%
  mutate(prod = x1 * x2 * x3)
result

answer <- result$prod[1]
answer
