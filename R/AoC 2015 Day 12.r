library(tidyverse)



answer <- str_extract_all(input, "-?\\d+")[[1]] %>% parse_number() %>% sum()
answer

l <- jsonlite::fromJSON(input, simplifyVector = FALSE)
str(l)

add_numbers <- function(l) {
  if (is.integer(l)) {
    as.integer(sum(l))
  } else if (is.character(l) || (!is.null(names(l)) && any(l == "red"))) {
    0L
  } else {
    l %>% map_int(add_numbers) %>% sum()
  }
}

add_numbers(l)
