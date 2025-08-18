library(tidyverse)





instructions <- read_lines(input) %>% parse_integer()
instructions

solve <- function(instructions) {
  i <- 1
  jumps <- 0

  repeat {
    if (i > length(instructions)) return(jumps)
    new_i <- i + instructions[i]
    instructions[i] <- instructions[i] + 1
    i <- new_i
    jumps <- jumps + 1
  }
}

answer <- solve(instructions)
answer

solve2 <- function(instructions) {
  i <- 1
  jumps <- 0

  repeat {
    if (i > length(instructions)) return(jumps)
    if (instructions[i] >= 3) {
      extra <- -1
    } else {
      extra <- 1
    }
    
    new_i <- i + instructions[i]
    instructions[i] <- instructions[i] + extra
    i <- new_i
    jumps <- jumps + 1
  }
}

answer <- solve2(instructions)
answer
