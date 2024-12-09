install.packages("combinat")

library(tidyverse)



df <-
  tibble(text = read_lines(input)) %>%
  separate(text, into = c("from", "to"), sep = " to ") %>%
  separate(to, into = c("to", "d"), sep = " = ", convert = TRUE) %>%
  mutate(
    lookup = ifelse(from < to, str_c(from, to), str_c(to, from))
  )

df

nodes <- c(df$from, df$to) %>% unique()
nodes

permutations <- combinat::permn(nodes)

# Remove reverse
# permutations <- permutations[order(map_chr(permutations, first))] %>% head(., length(.) / 2)

compute_distance <- function(route) {
  route_from <- head(route, -1)
  route_to <- head(lead(route), -1)
  route_lookup <- ifelse(route_from < route_to, str_c(route_from, route_to), str_c(route_to, route_from))

  df %>% filter(lookup %in% route_lookup) %>% pull(d) %>% sum()
}

distances <- map_int(permutations, compute_distance)

answer <- min(distances)
answer

# permutations %>%
#   map_int(compute_distance) %>%
#   max()

answer <- max(distances)
answer
