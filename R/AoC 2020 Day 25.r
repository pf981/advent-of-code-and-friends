library(tidyverse)



encrypt <- function(subject_number, loop_size) {
  value <- 1
  for (i in seq_len(loop_size)) {
    value <- (value * subject_number) %% 20201227
  }
  value
}

compute_loop_size <- function(public_key) {
  value <- 1
  loop_size <- 0
  repeat {
    loop_size <- loop_size + 1
    value <- (value * 7) %% 20201227
    if (value == public_key) {
      break
    }
  }
  loop_size
}

public_keys <- input %>% read_lines() %>% parse_integer()

loop_sizes <- c(
  compute_loop_size(public_keys[1]),
  compute_loop_size(public_keys[2])
)
loop_sizes

subject_number <- 7
encryption_key <- encrypt(
  encrypt(subject_number, loop_sizes[1]),
  loop_sizes[2]
)
answer <- encryption_key
answer

# No puzzle here - just need 49 stars.
