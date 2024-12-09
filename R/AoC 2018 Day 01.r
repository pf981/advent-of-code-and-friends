library(tidyverse)



nums <- str_extract_all(input, "-?\\d+") %>% first() %>% parse_integer()
answer <- nums %>% sum()
answer

freqs <- rep_len(nums, 1000000) %>% cumsum()
answer <- freqs[duplicated(freqs)][1]
answer
