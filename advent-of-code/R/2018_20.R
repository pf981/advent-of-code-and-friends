library(tidyverse)



get_paths <- function(s) {
  xs <- NULL
  ys <- NULL
  
  from_xs <- NULL
  from_ys <- NULL
  to_xs <- NULL
  to_ys <- NULL
  
  x <- 0
  y <- 0
  
  prev_x <- x
  prev_y <- y
  
  vs <- s %>% str_remove_all("\\^|\\$") %>% str_split("") %>% first()
  for (v in vs) {
    if (v == "(") {
      xs <- c(xs, x)
      ys <- c(ys, y)
    } else if (v == ")") {
      x <- xs[length(xs)]
      y <- ys[length(ys)]
      xs <- head(xs, -1)
      ys <- head(ys, -1)
    } else if (v == "|") {
      x <- xs[length(xs)]
      y <- ys[length(ys)]
    } else {
      x <- x + (v == "E") - (v == "W")
      y <- y + (v == "S") - (v == "N")
      
      from_xs <- c(from_xs, prev_x)
      from_ys <- c(from_ys, prev_y)
      to_xs <- c(to_xs, x)
      to_ys <- c(to_ys, y)
    }
    prev_x <- x
    prev_y <- y
  }
  
  tibble(from_x = from_xs, from_y = from_ys, to_x = to_xs, to_y = to_ys)
}

paths <- get_paths(input)
from <- str_c(paths$from_x, paths$from_y, sep = ",")
to <- str_c(paths$to_x, paths$to_y, sep = ",")
lst(from, to)

visited <- NULL
visited_d <- NULL
nodes <- c("0,0")
ds <- c(0)

while (length(ds) > 0) {
  node <- nodes[1]
  d <- ds[1]
    
  nodes <- nodes[-1]
  ds <- ds[-1]

  if (node %in% visited) next
  
  visited <- c(visited, node)
  visited_d <- c(visited_d, d)
  
  new_nodes <- to[from == node]
  nodes <- c(nodes, new_nodes)
  ds <- c(ds, rep(d + 1, length(new_nodes)))
}

answer <- max(visited_d)
answer

answer <- sum(visited_d >= 1000)
answer
