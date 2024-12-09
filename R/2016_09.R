library(tidyverse)



decompress <- function(x) {
  parts <- str_match(x, "(.*?)\\((\\d+)x(\\d+)\\)(.*)")
  
  if (any(is.na(parts))) {
    return(x)
  }
  
  before <- parts[[2]]
  n_chars <- parts[[3]] %>% parse_integer()
  n_times <- parts[[4]] %>% parse_integer()
  after <- parts[[5]]
  
  new_string <-
    after %>%
    str_sub(1, n_chars) %>%
    rep(n_times) %>%
    str_c(collapse = "")
  
  after <- after %>% str_sub(n_chars + 1)

  str_c(before, new_string, decompress(after))
}

answer <- input %>%
  decompress() %>%
  nchar()
answer

decompress_length <- function(x) {
  parts <- str_match(x, "(.*?)\\((\\d+)x(\\d+)\\)(.*)")
  
  if (any(is.na(parts))) {
    return(nchar(x))
  }
  
  before <- parts[[2]]
  n_chars <- parts[[3]] %>% parse_number()
  n_times <- parts[[4]] %>% parse_number()
  after <- parts[[5]]
  
  repeated_string <- after %>% str_sub(1, n_chars)  
  after <- after %>% str_sub(n_chars + 1)
  
  nchar(before) +
    n_times * decompress_length(repeated_string) +
    decompress_length(after)
}

answer <- decompress_length(input)
answer
