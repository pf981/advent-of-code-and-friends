# install.packages("binaryLogic")

library(tidyverse)



hash_step <- function(nums, lengths) {
  skip_size <- 0
  w_total <- 0
  for (l in lengths) {
    nums[seq_len(l)] <- nums[rev(seq_len(l))]

    w <- l + skip_size
    while (w > length(nums)) w <- w - length(nums)

    nums <- c(
      tail(nums, -w),
      head(nums, w)
    )
    skip_size <- skip_size + 1
    w_total <- w_total + w
  }
  while (w_total > length(nums)) w_total <- w_total - length(nums)
  lst(nums, w_total)
  c(
    tail(nums, w_total),
    head(nums, -w_total)
  )
}

hash <- function(x, nums = seq(from = 0, to = 255, by = 1)) {
  lengths <- rep(
    c(utf8ToInt(x), 17, 31, 73, 47, 23),
    64
  )
  
  result <- hash_step(nums, lengths)
  
  result %>%
    enframe() %>%
    mutate(name = (name - 1) %/% 16) %>%
    group_by(name) %>%
    summarise(
      output = reduce(value, bitwXor),
      hex = format(as.hexmode(output), width = 2)
    ) %>%
    pull(hex) %>%
    str_c(collapse = "")
}

get_row <- function(i, key) {
  str_c(key, "-", i) %>%
    hash() %>%
    str_split("") %>%
    first() %>%
    as.hexmode() %>%
    binaryLogic::as.binary(n = 4) %>%
    unlist()
}

get_grid <- function(key) {
  map(seq(from = 0, to = 127, by = 1), get_row, key)
}

grid <- get_grid(input)

answer <- grid %>% unlist() %>% sum()
answer

set_group <- function(row, col) {
  if (visited[row, col] || !m[row, col]) return(NULL)
  
  visited[row, col] <<- TRUE
  
  result <- c(
      if (row > 1) group[row - 1, col],
      if (row < nrow(group)) group[row + 1, col],
      if (col > 1) group[row, col - 1],
      if (col < ncol(group)) group[row, col + 1]
    ) %>% max(na.rm = TRUE)
  if (!is.finite(result)) {
    result <- max(group, na.rm = TRUE) + 1
    if (!is.finite(result)) result <- 1
  }
  group[row, col] <<- result
  if (row > 1) set_group(row - 1, col)
  if (row < nrow(group)) set_group(row + 1, col)
  if (col > 1) set_group(row, col - 1)
  if (col < ncol(group)) set_group(row, col + 1)
  
  NULL
}

m <- simplify2array(grid) %>% t()

visited <- m
visited[] <- FALSE

group <- m
group[] <- NA

for (row in seq_len(nrow(m))) {
  for (col in seq_len(ncol(m))) {
    set_group(row, col)
  }
}

answer <- max(group, na.rm = TRUE)
answer
