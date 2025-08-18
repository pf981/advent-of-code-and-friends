library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    from = str_extract(line, "^\\d+") %>% parse_integer(),
    to = str_extract(line, "(?<=> ).*") %>% str_split(", ")
  ) %>%
  unnest()
df

count_pids <- function(pid, visited = c()) {
  if (pid %in% visited) {
    return(0)
  }
  visited <- c(visited, pid)
  connected_pids <-
    df %>%
    filter(from == pid) %>%
    pull(to)
  
  1 + sum(map_dbl(connected_pids, count_pids, visited))
}

count_pids(0)

get_group <- function(pid, visited = c()) {
  if (pid %in% visited) {
    return(NULL)
  }
  visited <- c(visited, pid)
  connected_pids <-
    df %>%
    filter(from == pid) %>%
    pull(to)
  
  c(pid, map(connected_pids, get_group, visited) %>% unlist()) %>% unique()
}

answer <- 0
remaining <- unique(c(df$from, df$to))
while (length(remaining) > 0) {
  remaining <- remaining[!(remaining %in% get_group(remaining[1]))]
  answer <- answer + 1
}
answer
