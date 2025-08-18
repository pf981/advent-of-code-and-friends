library(tidyverse)



v <- input %>% str_split("") %>% first() %>% parse_integer()

answer <- v[v == lead(v, default = v[1])] %>% sum()
answer

d <- length(v) / 2

answer <- v[v == c(tail(v, d), head(v, d))] %>% sum()
answer
