library(tidyverse)



start_m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t() %>%
  `==`("#")
start_m

shift <- function(m, i, j) {
  i <- seq_len(nrow(m)) + i
  j <- seq_len(ncol(m)) + j
  
  i[i == 0 | i > nrow(m)] <- NA
  j[j == 0 | j > ncol(m)] <- NA
  
  result <- m[i, j]
  result[is.na(result)] <- FALSE
  result
}

count_neighbors <- function(m) {
  shift(m, -1, 0) +
    shift(m, 0, -1) +
    shift(m, 0, 1) +
    shift(m, 1, 0)
}

step <- function(m) {
  neighbors <- count_neighbors(m)
  
  keep_on <- m & neighbors == 1
  turn_on <- !m & neighbors %in% c(1, 2)
  m[] <- FALSE
  m[keep_on | turn_on] <- TRUE
  m
}

step_n <- function(m, n) {
  for (i in seq_len(n)) {
    m <- step(m)
  }
  m
}

as_character <- function(x) format(x, scientific = FALSE)

solve <- function(m) {
  seen <- list()
  repeat {
    m <- step(m)
    biodiversity <- sum(2^(which(t(m)) - 1))
    if (!is.null(seen[[as_character(biodiversity)]])) {
      return(biodiversity)
    }
    seen[[as_character(biodiversity)]] <- TRUE
  }
}

answer <- solve(start_m)
answer

count_neighbors <- function(ms) {
  counts <- map(ms, function(m) {m[] <- 0; m})
  
  mid_row <- ceiling(nrow(m) / 2)
  mid_col <- ceiling(ncol(m) / 2)
  
  for (depth in seq_along(ms)) {
    m <- ms[[depth]]
    m[mid_row, mid_col] <- FALSE
    counts[[depth]] <-
      counts[[depth]] +
        shift(m, -1, 0) +
        shift(m, 0, -1) +
        shift(m, 0, 1) +
        shift(m, 1, 0)
    
    if (depth != length(ms)) {
      for (direction in c("N", "E", "S", "W")) {
        row <- mid_row + (direction == "S") - (direction == "N")
        col <- mid_col + (direction == "E") - (direction == "W")
        
        if (direction == "N") {
          next_depth_rows <- 1
          next_depth_cols <- seq_len(ncol(m))
        } else if (direction == "E") {
          next_depth_rows <- seq_len(nrow(m))
          next_depth_cols <- ncol(m)
        } else if (direction == "S") {
          next_depth_rows <- nrow(m)
          next_depth_cols <- seq_len(ncol(m))
        } else if (direction == "W") {
          next_depth_rows <- seq_len(nrow(m))
          next_depth_cols <- 1
        }
        
        counts[[depth]][row, col] <- counts[[depth]][row, col] + sum(ms[[depth + 1]][next_depth_rows, next_depth_cols])
        counts[[depth + 1]][next_depth_rows, next_depth_cols] <- counts[[depth + 1]][next_depth_rows, next_depth_cols] + m[row, col]
        
      }
    }
  }
  counts
}

step_single <- function(m, neighbors) {
  keep_on <- m & neighbors == 1
  turn_on <- !m & neighbors %in% c(1, 2)
  m[] <- FALSE
  m[keep_on | turn_on] <- TRUE
  m[ceiling(nrow(m) / 2), ceiling(ncol(m) / 2)] <- FALSE
  m
}

step <- function(ms) {
  neighbors <- count_neighbors(ms)
  
  map2(ms, neighbors, step_single)
}

step_n <- function(ms, n) {
  for (i in seq_len(n)) {
    ms <- step(ms)
  }
  ms
}

n_minutes <- 200

m <- start_m
m[] <- FALSE

ms <- rep(list(m), n_minutes * 2 + 1)
ms[[ceiling(length(ms) / 2)]] <- start_m
ms

result <- step_n(ms, n_minutes)
result

answer <- result %>% unlist() %>% sum()
answer
