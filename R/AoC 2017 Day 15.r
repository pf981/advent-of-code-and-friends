library(tidyverse)



s <- str_extract_all(input, "\\d+") %>% first() %>% parse_number()
a_start <- s[1]
b_start <- s[2]
lst(a_start, b_start)

a_factor <- 16807
b_factor <- 48271
denominator <- 2147483647
mod <- 2^16

a <- a_start
b <- b_start
match_count <- 0
for (i in seq_len(40000000)) {
  a <- (a_factor * a) %% denominator
  b <- (b_factor * b) %% denominator
  match_count <- match_count + ((a %% mod) == (b %% mod))
}

answer <- match_count
answer

a <- a_start
b <- b_start
match_count <- 0
for (i in seq_len(5000000)) {
  repeat {
    a <- (a_factor * a) %% denominator
    if (a %% 4 == 0) break
  }
  repeat {
    b <- (b_factor * b) %% denominator
    if (b %% 8 == 0) break
  }
  
  match_count <- match_count + ((a %% mod) == (b %% mod))
}

answer <- match_count
answer
