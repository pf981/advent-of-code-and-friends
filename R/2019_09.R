library(tidyverse)



# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(df, i) {
  index <- i[[1]] + 1
  if (i[[2]] == 0) {
    # Position mode
    index <- df[[index]] + 1
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- df[[index]] + attr(df, "relative_base") + 1 # Do I need to +1?
    #index <- df[[index + attr(df, "relative_base")]] + 1 # Do I need to +1?
  }
  index
}

`[.special_index` <- function(df, i) {
  df[[get_index(df, i)]]
}

`[<-.special_index` <- function(df, i, j, value) {
  df[[get_index(df, i)]] <- value
  
  df
}

run_instructions <- function(instructions, input = 1) {
  instructions <- c(instructions, numeric(100000)) # Extra memory. Note i'm using numeric rather than integer so it can handle big integers
  instructions <- structure(instructions, class = "special_index")
  attr(instructions, "relative_base") <- 0
  
  output <- NULL
  
  i <- 0
  
  while (instructions[list(i, 1)] != 99) {
    value <- instructions[list(i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_index_mode)
    p2 <- list(i + 2, p2_index_mode)
    p3 <- list(i + 3, p3_index_mode)
    
    # print_state(instructions, input, i, p1, p2, p3, op_code)
    
    if (op_code == 1) {
      instructions[p3] <- instructions[p1] + instructions[p2]
    } else if (op_code == 2) {
      instructions[p3] <- instructions[p1] * instructions[p2]
    } else if (op_code == 3) {
      instructions[p1] <- input
    } else if (op_code == 4) {
      input <- instructions[p1]
      output <- c(output, input)
    } else if (op_code == 5) {
      if (instructions[p1] != 0) {
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (instructions[p1] == 0) {
        i = get_index(instructions, p2) - 1
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      instructions[p3] <- instructions[p1] < instructions[p2]
    } else if (op_code == 8) {
      instructions[p3] <- instructions[p1] == instructions[p2]
    } else if (op_code == 9) {
      # New instruction: Relative base offset
      attr(instructions, "relative_base") <- attr(instructions, "relative_base") + instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    i <- i + 1 + num_params
  }

  output
}

library(testthat)

test_that("relative mode works", {
  expect_equal(
    run_instructions(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), 0),
    c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99)
  )
})

test_that("can handle large numbers", {
  expect_equal(nchar(run_instructions(c(1102,34915192,34915192,7,4,7,99,0), 0)), 16)
  expect_equal(run_instructions(c(104,1125899906842624,99), 0), 1125899906842624)
})

input %>% str_split(",") %>% unlist() %>% parse_integer() %>% run_instructions(1)
#> 2436480432

input %>% str_split(",") %>% unlist() %>% parse_integer() %>% run_instructions(2)
#> 45710