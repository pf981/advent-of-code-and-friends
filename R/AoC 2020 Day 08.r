library(tidyverse)



instructions <-
  input %>%
  read_lines() %>%
  as_tibble() %>%
  separate(value, c("op", "value"), " ") %>%
  mutate(value = parse_number(value))

instructions

accumulator <- 0
visited <- c()
i <- 1

repeat {
  instruction <- instructions %>% slice(i)
  if (i %in% visited) {
    break
  }
  
  visited <- c(visited, i)
  
  if (instruction$op == "acc") {
    accumulator <- accumulator + instruction$value
  }
  
  if (instruction$op == "jmp") {
    i <- i + instruction$value
  } else {
    i <- i + 1
  }
}

answer <- accumulator
answer

try_instructions <- function(instructions) {
  accumulator <- 0
  visited <- c()
  i <- 1

  repeat {
    instruction <- instructions %>% slice(i)
    if (i %in% visited) {
      return(NULL)
    }

    visited <- c(visited, i)

    if (instruction$op == "acc") {
      accumulator <- accumulator + instruction$value
    }

    if (instruction$op == "jmp") {
      i <- i + instruction$value
    } else {
      i <- i + 1
    }
    
    if (i == nrow(instructions) + 1) {
      return(accumulator)
    }
  }
}

for (i in which(instructions$op %in% c("nop", "jmp"))) {
  updated <- instructions
  updated$op[i] <- ifelse(updated$op[i] == "jmp", "nop", "jmp")
  result <- try_instructions(updated)
  if (!is.null(result)) break
}
answer <- result
answer
