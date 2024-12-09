library(tidyverse)



df <-
  read_csv(input, col_names = FALSE) %>%
  rename_all(str_to_lower) %>%
  mutate(id = row_number()) %>%
  mutate_all(as.integer)
df

point_groups <- sqldf::sqldf("
SELECT
  a.x1 || ',' || a.x2 || ',' || a.x3 || ',' || a.x4 AS group_id,
  b.x1 || ',' || b.x2 || ',' || b.x3 || ',' || b.x4 AS member
FROM
  df a
  LEFT JOIN df b ON
    abs(b.x1 - a.x1) + abs(b.x2 - a.x2) + abs(b.x3 - a.x3) + abs(b.x4 - a.x4) <= 3
")

for (i in seq_len(nrow(point_groups))) {
  members <- point_groups$member[point_groups$group_id == point_groups$group_id[i]]
  group_ids_to_merge <- point_groups$group_id[point_groups$member %in% members]
  
  point_groups$group_id[point_groups$group_id %in% group_ids_to_merge] <- point_groups$group_id[i]
}

point_groups <- point_groups %>% distinct()
point_groups

answer <- point_groups %>% pull(group_id) %>% unique() %>% length()
answer

# No puzzle here - just need 49 stars.
