library(tidyverse)



items <- read_lines(input) %>% parse_number()
items

ways_to_fill <- function(items, capacity) {
  if (capacity == 0) {
    return(1)
  }
  if (capacity < 0) {
    return(0)
  }
  
  result <- 0
  for (item in items) {
    items <- items[items != item | duplicated(items)]
    result <- result + ways_to_fill(
      items,
      capacity - item
    )
  }
  result
}

ways_to_fill(items, 150)

ways_to_fill_min <- function(items, capacity, n_containers = 0) {
  if (capacity == 0) {
    return(lst(n_containers, n_ways = 1))
  }
  if (capacity < 0) {
    return(lst(n_containers, n_ways = 0))
  }
  
  cur_n_ways <- 0
  cur_n_containers <- Inf
  for (item in items) {
    items <- items[items != item | duplicated(items)]
    output <- ways_to_fill_min(
      items,
      capacity - item,
      n_containers + 1
    )
    
    if (output$n_containers == cur_n_containers) {
      cur_n_ways <- cur_n_ways + output$n_ways
    } else if (output$n_containers < cur_n_containers && output$n_ways > 0) {
      cur_n_ways <- output$n_ways
      cur_n_containers <- output$n_containers
    }
  }
  lst(
    n_containers = cur_n_containers,
    n_ways = cur_n_ways,
  )
}

result <- ways_to_fill_min(items, 150)
result

answer <- result$n_ways
answer
