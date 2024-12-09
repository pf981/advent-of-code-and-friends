library(tidyverse)



nums <-
  input %>%
  read_lines() %>%
  str_extract_all("\\d+") %>%
  map(parse_integer)
  
answer <- nums %>% map_dbl(~max(.) - min(.)) %>% sum()
answer

div <- function(x) {
  for (a in x) {
    for (b in x[x < a]) {
      if (a / b == as.integer(a / b)) return(a / b)
    }
  }
}

answer <- nums %>% map_dbl(div) %>% sum()
answer
