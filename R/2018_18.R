library(tidyverse)



m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

get_adjacent_squares <- function(m, row, col) {
  c(
    tryCatch(m[row - 1, col - 1], error = function(e) NULL),
    tryCatch(m[row - 1, col + 0], error = function(e) NULL),
    tryCatch(m[row - 1, col + 1], error = function(e) NULL),
    tryCatch(m[row + 0, col - 1], error = function(e) NULL),
#   tryCatch(m[row + 0, col + 0], error = function(e) NULL),
    tryCatch(m[row + 0, col + 1], error = function(e) NULL),
    tryCatch(m[row + 1, col - 1], error = function(e) NULL),
    tryCatch(m[row + 1, col + 0], error = function(e) NULL),
    tryCatch(m[row + 1, col + 1], error = function(e) NULL)
  )
}

step <- function(m) {
  trees <- m
  lumberyards <- m
  trees[] <- 0
  lumberyards[] <- 0
  
  for (row in seq_len(nrow(m))) {
    for (col in seq_len(ncol(m))) {
      adjacent_squares <- get_adjacent_squares(m, row, col)
      trees[row, col] <- sum(adjacent_squares == "|")
      lumberyards[row, col] <- sum(adjacent_squares == "#")
    }
  }
  
  new_m <- m
  new_m[m == "." & trees >= 3] <- "|"
  new_m[m == "|" & lumberyards >= 3] <- "#"
  new_m[m == "#" & !(trees >= 1 & lumberyards >= 1)] <- "."
  
  new_m
}

simulate <- function(m, minutes) {
  for (i in seq_len(minutes)) {
    m <- step(m)
  }
  m
}

result <- simulate(m, 10)

answer <- sum(result == "|") * sum(result == "#")
answer

minutes <- 1300
result <- m
ntrees <- integer(minutes)
nlumberyards <- integer(minutes)
for (i in seq_len(minutes)) {
  result <- step(result)
  ntrees[i] <- sum(result == "|")
  nlumberyards[i] <- sum(result == "#")
}

df <-
 tibble(ntrees, nlumberyards) %>%
 mutate(
   x = row_number(),
   resource_value = ntrees * nlumberyards
 )

df %>%
 select(-resource_value) %>%
 pivot_longer(-x) %>%
 ggplot(aes(x, value, col = name)) +
   geom_line() +
   theme_minimal()

df %>% filter(x >= 1000) %>% print(n = 100)

answer <- df %>% filter(x == 1000 + ((1000000000 - 1000) %% 28)) %>% pull(resource_value)
answer
