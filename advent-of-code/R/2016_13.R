library(tidyverse)

input <- 1364
target_x <- 31
target_y <- 39

# input <- 10
# target_x <- 7
# target_y <- 4

hash <- function(x, y) str_c(x, y, sep = ",")

is_wall <- function(x, y) {
  if (x < 0 || y < 0) return(TRUE)
  value <- x*x + 3*x + 2*x*y + y + y*y + input
  sum_of_bits <- value %>% intToBits() %>% as.integer() %>% sum()
  sum_of_bits %% 2
}

solve <- function() {
  ds <- 0
  xs <- 1
  ys <- 1

  visited_hashes <- NULL

  repeat {
    i <- which.min(ds)
    d <- ds[i]
    x <- xs[i]
    y <- ys[i]

    ds <- ds[-i]
    xs <- xs[-i]
    ys <- ys[-i]

    visited_hashes <- c(visited_hashes, hash(x, y))
    
    new_xs <- c(x, x + 1, x, x - 1)
    new_ys <- c(y - 1, y, y + 1, y)
    
    for (new_pos_i in seq_along(new_xs)[!(hash(new_xs, new_ys) %in% visited_hashes)]) {  
      new_x <- new_xs[new_pos_i]
      new_y <- new_ys[new_pos_i]
      
      if (!is_wall(new_x, new_y)) {
        if (new_x == target_x && new_y == target_y) { # If solved
          return(d + 1)
        }

        xs <- c(xs, new_x)
        ys <- c(ys, new_y)
        ds <- c(ds, d + 1)
      }
    }
  }
}

answer <- solve()
answer

solve <- function() {
  ds <- 0
  xs <- 1
  ys <- 1

  visited_hashes <- NULL

  repeat {
    i <- which.min(ds)
    d <- ds[i]
    x <- xs[i]
    y <- ys[i]
    
    if (d > 50) {
      return(visited_hashes %>% unique() %>% length())
    }

    ds <- ds[-i]
    xs <- xs[-i]
    ys <- ys[-i]

    visited_hashes <- c(visited_hashes, hash(x, y))
    
    new_xs <- c(x, x + 1, x, x - 1)
    new_ys <- c(y - 1, y, y + 1, y)
    
    for (new_pos_i in seq_along(new_xs)[!(hash(new_xs, new_ys) %in% visited_hashes)]) {  
      new_x <- new_xs[new_pos_i]
      new_y <- new_ys[new_pos_i]
      
      if (!is_wall(new_x, new_y)) {
        xs <- c(xs, new_x)
        ys <- c(ys, new_y)
        ds <- c(ds, d + 1)
      }
    }
  }
}

answer <- solve()
answer
