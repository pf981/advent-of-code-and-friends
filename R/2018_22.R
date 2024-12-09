library(tidyverse)



nums <- str_extract_all(input, "\\d+") %>% first() %>% parse_integer()
depth <- nums[1]
target <- nums[-1]
lst(depth, target)

extra <- 20
geologic_index <- matrix(0, nrow = target[2] + 1 + extra, ncol = target[1] + 1 + extra)
geologic_index[1, ] <- (seq_len(ncol(geologic_index)) - 1) * 16807
geologic_index[, 1] <- (seq_len(nrow(geologic_index)) - 1) * 48271
geologic_index[1, 1] <- 0

erosion_level <- (geologic_index + depth) %% 20183

for (x in seq_len(ncol(geologic_index) - 1)) {
  for (y in seq_len(nrow(geologic_index) - 1)) {
    geologic_index[y + 1, x + 1] <- erosion_level[y + 1, x] * erosion_level[y, x + 1]
    erosion_level[y + 1, x + 1] <- (geologic_index[y + 1, x + 1] + depth) %% 20183
  }
}

geologic_index[target[2] + 1, target[1] + 1] <- 0
erosion_level[target[2] + 1, target[1] + 1] <- (geologic_index[target[2] + 1, target[1] + 1] + depth) %% 20183

risk_level <- erosion_level %% 3
answer <- sum(risk_level[seq_len(target[2] + 1), seq_len(target[1] + 1)])
answer

terrain <- risk_level
terrain[risk_level == 0] <- "rocky"
terrain[risk_level == 1] <- "wet"
terrain[risk_level == 2] <- "narrow"

nodes_df <-
  tibble(region_type = c("rocky", "wet", "narrow")) %>%
  rowwise() %>%
  mutate(
    coords = list(which(terrain == region_type, arr.ind = TRUE) %>% as_tibble())
  ) %>%
  unnest() %>%
  mutate(
    equip = list(c("torch", "climbing gear", "neither")),
    disallowed_equip = case_when(
      region_type == "rocky" ~ "neither",
      region_type == "wet" ~ "torch",
      region_type == "narrow" ~ "climbing gear"
    )
  ) %>%
  unnest() %>%
  filter(equip != disallowed_equip) %>%
  mutate(node_name = str_c(row, col, equip, sep = ","))
nodes_df

edges <- 
  bind_rows(
    nodes_df %>% inner_join(nodes_df, by = c("row", "col")) %>% filter(equip.y != equip.x) %>% mutate(d = 7),     # Swap equipment
    nodes_df %>% mutate(row = row - 1) %>% inner_join(nodes_df, by = c("row", "col", "equip")) %>% mutate(d = 1), # N
    nodes_df %>% mutate(col = col + 1) %>% inner_join(nodes_df, by = c("row", "col", "equip")) %>% mutate(d = 1), # E
    nodes_df %>% mutate(row = row + 1) %>% inner_join(nodes_df, by = c("row", "col", "equip")) %>% mutate(d = 1), # S
    nodes_df %>% mutate(col = col - 1) %>% inner_join(nodes_df, by = c("row", "col", "equip")) %>% mutate(d = 1)  # W
  ) %>%
  transmute(
    from_node = node_name.y,
    to_node = node_name.x,
    d
  )
edges

start_node <- "1,1,torch"
end_nodes <- nodes_df %>% filter(row == target[2] + 1, col == target[1] + 1, equip == "torch") %>% pull(node_name)

lst(start_node, end_nodes)

ds <- c(0)
nodes <- c(start_node)
visited_nodes <- NULL

repeat {
  i <- which.min(ds)
  
  d <- ds[i]
  node <- nodes[i]
  
  ds <- ds[-i]
  nodes <- nodes[-i]
  
  if (node %in% end_nodes) break
  if (node %in% visited_nodes) next
  visited_nodes <- c(visited_nodes, node)
  
  new_nodes <- edges %>% filter(from_node == node)
  for (j in seq_len(nrow(new_nodes))) {
    nodes <- c(nodes, new_nodes$to_node[j])
    ds <- c(ds, d + new_nodes$d[j])
  }
  
}
answer <- d
answer # 5 mins
