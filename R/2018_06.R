library(tidyverse)



# 

df <-
  read_lines(input) %>%
  str_split(", ") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("x", "y"))
df

counts <- integer(nrow(df))

for (cur_x in seq(from = -1000, to = 1000, by = 1)) {
  for (cur_y in seq(from = -1000, to = 1000, by = 1)) {
    d <- abs(cur_x - df$x) + abs(cur_y - df$y)
    i <- which.min(d)
    if (sum(d == d[i]) == 1) {
      counts[i] <- counts[i] + 1
    }
  }
}

plot(sort(counts))

answer <- counts %>% discard(~. > 5000) %>% max()
answer

region_size <- 0

for (cur_x in seq(from = -1000, to = 1000, by = 1)) {
  for (cur_y in seq(from = -1000, to = 1000, by = 1)) {
    if (sum(abs(cur_x - df$x) + abs(cur_y - df$y)) < 10000) {
      region_size <- region_size + 1
    }
  }
}
answer <- region_size
answer
