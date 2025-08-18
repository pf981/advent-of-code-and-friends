library(tidyverse)



nums <- input %>% read_lines() %>% parse_integer()
sequence <- sort(c(0, nums, max(nums) + 3))
answer <- sum(diff(sequence) == 1) * sum(diff(sequence) == 3)
answer

ways <- integer(max(sequence) + 1)
ways[length(ways)] <- 1

for (num in rev(sequence)[-1]) {
  next_nums <- sequence[sequence %in% (num + 1:3)]
  ways[num + 1] <- sum(ways[next_nums + 1])
}

answer <- format(ways[[1]], scientific = FALSE)
answer
