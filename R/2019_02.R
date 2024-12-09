library(tidyverse)



instructions_original <-
  input %>%
  str_split(",") %>%
  first() %>%
  parse_integer()
instructions_original

instructions <- instructions_original
instructions[[1 + 1]] <- 12
instructions[[2 + 1]] <- 2

i <- 1
while (instructions[[i]] != 99) {
  op_code <- instructions[[i]]
  fn <- if (op_code == 1) {
    `+`
  } else if (op_code == 2) {
    `*`
  } else {
    stop(paste0('Invalid op code: ', op_code, ' at position ', i))
  }
  instructions[[instructions[[i + 3]] + 1]] <- fn(instructions[[instructions[[i + 1]] + 1]], instructions[[instructions[[i + 2]] + 1]])
  
  i <- i + 4
}
answer <- instructions[[1]]
answer

run_instructions <- function(instructions) {
  i <- 1
  while (instructions[[i]] != 99) {
    op_code <- instructions[[i]]
    fn <- list(`+`, `*`)[[op_code]]
    
    instructions[[instructions[[i + 3]] + 1]] <- fn(
      instructions[[instructions[[i + 1]] + 1]],
      instructions[[instructions[[i + 2]] + 1]]
    )

    i <- i + 4
  }
  instructions
}

find_solution <- function(instructions_original) {
  for (pos_1 in seq(from = 0, to = 99)) {
    for (pos_2 in seq(from = 0, to = 99)) {
      instructions <- instructions_original
      instructions[[1 + 1]] <- pos_1
      instructions[[2 + 1]] <- pos_2
      
      result <- run_instructions(instructions)
      if (result[[1]] == 19690720) {
        return(list(pos_1, pos_2))
      }
    }
  }
}

solution <- find_solution(instructions_original)
answer <- 100 * solution[[1]] + solution[[2]]
answer
