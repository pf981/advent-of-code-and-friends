library(tidyverse)


input2 <- 40

# 
# input2 <- 10

generate_rows <- function(start_row, n_rows) {
  result <- vector(mode = "list", length = n_rows)
  result[[1]] <- start_row
  for (i in seq_len(n_rows - 1)) {
    left <- lag(result[[i]], default = FALSE)
    center <- result[[i]]
    right <- lead(result[[i]], default = FALSE)

    result[[i + 1]] <-
      (left & center & !right) |
      (center & right & !left) |
      (left & !center & !right) |
      (right & !center & !left)
  }
  result
}

start_row <-
  str_split(input, "") %>%
  unlist() %>%
  map_lgl(~. == "^")
start_row

result <- generate_rows(start_row, input2)
result

answer <- result %>% unlist() %>% `!`() %>% sum()
answer

result <- generate_rows(start_row, 400000)
answer <- result %>% unlist() %>% `!`() %>% sum()
answer
