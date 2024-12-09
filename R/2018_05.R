library(tidyverse)



pairs_regex <- str_c(c(letters, LETTERS), c(LETTERS, letters)) %>% str_c(collapse = "|")

react <- function(s) {
  repeat {
    new_s <- str_replace_all(s, pairs_regex, "")
    if (new_s == s) break
    s <- new_s
  }
  s
}

result <- react(input)
answer <- str_length(result)
answer

answer <-
  str_c(letters, "|", LETTERS) %>%
  map_chr(~(str_replace_all(input, ., ""))) %>%
  map_chr(react) %>%
  map_int(str_length) %>%
  min ()
answer
