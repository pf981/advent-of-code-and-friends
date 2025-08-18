install.packages("igraph")

library(tidyverse)



orbits <- read_delim(input, delim = ")", col_names = c("center", "satellite"))
orbits

g <- 
  orbits %>%
  transmute(src = satellite, dst = center) %>%
  as.matrix() %>%
  igraph::graph_from_edgelist()

count_orbits <- function(v, graph = g) {
  igraph::subcomponent(g, v, mode = "out") %>% length() %>% `-`(1)
}

objects <- orbits %>% unlist() %>% unique()
answer <- objects %>% map_dbl(count_orbits) %>% sum()
answer

# Subtract 3 because we don't count the first and last. Subtract 2 for the ends, then subtract another because we are counting edges, not nodes.
answer <- igraph::shortest_paths(g, "YOU", "SAN", mode = "all")$vpath[[1]] %>% length() %>% `-`(3)
answer
