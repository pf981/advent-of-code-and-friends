library(tidyverse)



m <-
  read_lines(input) %>%
  str_split("") %>%
  map(~. == "#") %>%
  {matrix(unlist(.), byrow = TRUE, ncol = length(.[[1]]))}

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
  shift(m, -1, -1) +
    shift(m, -1, 0) +
    shift(m, -1, 1) +
    shift(m, 0, -1) +
    # Note: No 0, 0
    shift(m, 0, 1) +
    shift(m, 1, -1) +
    shift(m, 1, 0) +
    shift(m, 1, 1)
}

step <- function(m) {
  neighbors <- count_neighbors(m)
  
  keep_on <- m & neighbors %in% c(2, 3)
  turn_on <- !m & neighbors == 3
  m[] <- FALSE
  m[keep_on | turn_on] <- TRUE
  m
}

step_n <- function(m, n) {
  for (. in seq_len(n)) {
    m <- step(m)
  }
  m
}

answer <- step_n(m, 100) %>% sum()
answer

step_n2 <- function(m, n) {
  for (. in seq_len(n)) {
    m[c(1, 1, nrow(m), nrow(m)), c(1, ncol(m), ncol(m), 1)] <- TRUE
    m <- step(m)
  }
  m[c(1, 1, nrow(m), nrow(m)), c(1, ncol(m), ncol(m), 1)] <- TRUE
  m
}

answer <- step_n2(m, 100) %>% sum()
answer
