library(tidyverse)



get_directions <- function(hash_input) {
  first_four <-
    hash_input %>%
    openssl::md5() %>%
    str_split("") %>%
    unlist() %>%
    head(4)
  
  c("U", "D", "L", "R")[first_four %in% c("b", "c", "d", "e", "f")]
}

shortest_path <- function(start_hash) {
  xs <- c(1)
  ys <- c(1)
  hash_inputs <- c(start_hash)
  path_lengths <- c(0)
  
  repeat {
    # Choose the shortest path so far
    i <- which.min(path_lengths)
    
    x <- xs[i]
    y <- ys[i]
    hash_input <- hash_inputs[i]
    path_length <- path_lengths[i]
    
    xs <- xs[-i]
    ys <- ys[-i]
    hash_inputs <- hash_inputs[-i]
    path_lengths <- path_lengths[-i]
    
    
    # For each possible move
    for (direction in get_directions(hash_input)) {
      new_x <- x + case_when(direction == "R" ~ 1, direction == "L" ~ -1, TRUE ~ 0)
      new_y <- y + case_when(direction == "U" ~ -1, direction == "D" ~ 1, TRUE ~ 0)
      new_hash_input <- str_c(hash_input, direction)
      
      if (new_x < 1 || new_x > 4 || new_y < 1 || new_y > 4) {
        next
      }
      
      if (new_x == 4 && new_y == 4) {
        return(new_hash_input)
      }
      
      xs <- c(xs, new_x)
      ys <- c(ys, new_y)
      hash_inputs <- c(hash_inputs, new_hash_input)
      path_lengths <- c(path_lengths, path_length + 1)
    }
  }
}

result <- shortest_path(input)
result

answer <- result %>% str_remove("^[a-z]+")
answer

longest_path <- function(hash_input, x = 1, y = 1) {
  if (x == 4 && y == 4) {
    return(0)
  }
  if (x < 1 || x > 4 || y < 1 || y > 4) {
    return(NA)
  }
  
  longest_path <- NA

  for (direction in get_directions(hash_input)) {
    new_x <- x + case_when(direction == "R" ~ 1, direction == "L" ~ -1, TRUE ~ 0)
    new_y <- y + case_when(direction == "U" ~ -1, direction == "D" ~ 1, TRUE ~ 0)
    new_hash_input <- str_c(hash_input, direction)

    new_path_length <- 1 + longest_path(new_hash_input, new_x, new_y)
    if ((!is.na(new_path_length) && new_path_length > longest_path) || is.na(longest_path)) {
      longest_path <- new_path_length
    }
  }
  longest_path
}

answer <- longest_path(input)
answer
