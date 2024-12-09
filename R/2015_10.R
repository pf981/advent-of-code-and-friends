library(tidyverse)



x <- str_split(input, "")[[1]]

for (i in seq_len(40)) {
  run_lengths <- rle(x)
  x <- str_c(run_lengths$lengths, run_lengths$values, collapse = "") %>% str_split("") %>% first()
}

answer <- length(x)
answer

x <- str_split(input, "")[[1]]

for (i in seq_len(50)) {
  run_lengths <- rle(x)
  x <- str_c(run_lengths$lengths, run_lengths$values, collapse = "") %>% str_split("") %>% first()
}

answer <- length(x)
answer
