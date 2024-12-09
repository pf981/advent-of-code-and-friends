library(tidyverse)



# 

df <-
  tibble(line = read_lines(input))  %>%
  transmute(
    start = str_extract(line, "^\\d+") %>% parse_number(),
    end = str_extract(line, "\\d+$") %>% parse_number()
  )
df

find_min <- function() {
  i <- 0
  repeat {
    new_end <-
      df %>%
      filter(start <= i, end >= i) %>%
      pull(end) %>%
      max()
    
    if (!is.finite(new_end)) {
      return(i)
    }
    i <- new_end + 1
  }
}

find_min()

count_allowed <- function(max_allowed = 4294967295) {
  allowed <- 0
  i <- 0
  while(i <= max_allowed) {
    new_end <-
      df %>%
      filter(start <= i, end >= i) %>%
      pull(end) %>%
      max()
    
    if (!is.finite(new_end)) {
      new_end <-
        df %>%
        filter(start > i) %>%
        pull(start) %>%
        min()
      
      if (!is.finite(new_end)) {
        return (allowed + max_allowed - i + 1)
      }
      
      allowed <- allowed + (new_end - i)
      i <- new_end
    } else {
      i <- new_end + 1
    }
  }
  allowed
}

count_allowed()
