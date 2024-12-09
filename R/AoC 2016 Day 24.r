install.packages("combinat")

library(tidyverse)



# 

m <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  simplify2array() %>%
  identity() %>%
  t()
m

visited <- m == "#"
visited

pois <- m
pois[] <- m %in% seq(from = 0, to = max(m), by = 1)
class(pois) <- "logical"
pois

pois_df <-
  which(pois, arr.ind = TRUE) %>%
  as_tibble() %>%
  add_column(name = m[which(pois, arr.ind = TRUE)])
pois_df

# Get shortest path from any POI to any other POI

combinations <-
  crossing(
    pois_df %>% rename_all(~str_c("from_", .)),
    pois_df %>% rename_all(~str_c("to_", .))
  ) %>%
  filter(to_name > from_name)
combinations

shortest_distance <- function(from_row, from_col, to_row, to_col) {
  rows <- c(from_row)
  cols <- c(from_col)
  ds <- c(0)
  v <- visited
  
  repeat {
    i <- which.min(ds)
    row <- rows[i]
    col <- cols[i]
    d <- ds[i]
    
    rows <- rows[-i]
    cols <- cols[-i]
    ds <- ds[-i]
    
    for (new_pos in list(c(row - 1, col), c(row + 1, col), c(row, col - 1), c(row, col + 1))) {
      if (v[new_pos[1], new_pos[2]]) next
      v[new_pos[1], new_pos[2]] <- TRUE
      
      if (new_pos[1] == to_row && new_pos[2] == to_col) return(d + 1)
      
      rows <- c(rows, new_pos[1])
      cols <- c(cols, new_pos[2])
      ds <- c(ds, d + 1)
    }
  }
}

distances <-
  combinations %>%
  mutate(
    d = pmap_dbl(lst(from_row, from_col, to_row, to_col), shortest_distance)
  ) %>%
  {bind_rows(
    mutate(., lookup = str_c(from_name, "-", to_name)),
    mutate(., lookup = str_c(to_name, "-", from_name))
  )}
distances

get_total_distance <- function(poi_seq) {
  inner_join(
    tibble(lookup = str_c(poi_seq, "-", lead(poi_seq)) %>% head(-1)),
    distances
  ) %>%
    pull(d) %>%
    sum()
}

answer <-
  distances$to_name %>%
  unique() %>%
  combinat::permn() %>%
  map(~c("0", .)) %>%
  map_dbl(get_total_distance) %>%
  min()
answer

answer <-
  distances$to_name %>%
  unique() %>%
  combinat::permn() %>%
  map(~c("0", ., "0")) %>%
  map_dbl(get_total_distance) %>%
  min()
answer
