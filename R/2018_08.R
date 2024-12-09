library(tidyverse)



nums <- str_split(input, " ") %>% first() %>% parse_integer()
nums

parse_tree <- function(nums) {
  n_child <- nums[1]
  n_meta <- nums[2]
  n_chars <- 2
  nums <- tail(nums, -2)
  
  children = vector(mode = "list", length = n_child)
  for (i in seq_along(children)) {
    children[[i]] <- parse_tree(nums)
    nums <- tail(nums, -children[[i]]$n_chars)
    n_chars <- n_chars + children[[i]]$n_chars
  }
  
  metadata <- head(nums, n_meta)
  n_chars <- n_chars + n_meta
  
  lst(
    n_child,
    n_meta,
    n_chars,
    metadata,
    children
  )
}

tree <- parse_tree(nums)
tree %>% str()

sum_meta <- function(tree) {
  sum(tree$metadata, na.rm = TRUE) + sum(map_dbl(tree$children, sum_meta), na.rm = TRUE)
}

answer <- sum_meta(tree)
answer

node_value <- function(tree) {
  if (tree$n_child == 0) {
    return(sum(tree$metadata, na.rm = TRUE))
  }
  
  result <- 0
  for (i in tree$metadata) {
    if (is.na(i) || i > tree$n_child || i < 1) next
    result <- result + node_value(tree$children[[i]])
  }
  
  result
}

answer <- node_value(tree)
answer
