install.packages("gtools")

library(testthat)
library(tidyverse)



sequence <- input %>% str_split(",") %>% unlist() %>% parse_integer()
sequence

get_index <- function(df, i) {
  index <- i[[1]] + 1
  if (!i[[2]]) {
    index <- df[[index]] + 1
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

run_instructions <- function(instructions, phase, input) {
  instructions <- structure(instructions, class = "special_index")
  
  i <- 0
  first_input <- TRUE
  
  while (instructions[list(i, TRUE)] != 99) {
    value <- instructions[list(i, TRUE)]
    
    op_code <- value %% 100
    p1_is_immediate <- value %% 1000 %/% 100
    p2_is_immediate <- value %% 10000 %/% 1000
    p3_is_immediate <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_is_immediate)
    p2 <- list(i + 2, p2_is_immediate)
    p3 <- list(i + 3, p3_is_immediate)
    
    if (op_code == 1) {
      instructions[p3] <- instructions[p1] + instructions[p2]
    } else if (op_code == 2) {
      instructions[p3] <- instructions[p1] * instructions[p2]
    } else if (op_code == 3) {
      # The first input instruction (opcode 3) is the phase setting
      if (first_input) {
        instructions[p1] <- phase
        first_input <- FALSE
      } else {
        instructions[p1] <- input
      }
    } else if (op_code == 4) {
      input <- instructions[p1]
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
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    i <- i + 1 + num_params
  }
  
  input
}

get_thruster_output <- function(instructions, phases, a_input = 0) {
  a_output <- run_instructions(instructions, phase = phases[[1]], input = a_input)
  b_output <- run_instructions(instructions, phase = phases[[2]], input = a_output)
  c_output <- run_instructions(instructions, phase = phases[[3]], input = b_output)
  d_output <- run_instructions(instructions, phase = phases[[4]], input = c_output)
  e_output <- run_instructions(instructions, phase = phases[[5]], input = d_output)

  thruster_output <- e_output
  thruster_output
}

get_max_thruster_output <- function(instructions) {
  gtools::permutations(n = 5, r = 5, v = seq(from = 0, to = 4, by = 1)) %>%
    array_tree() %>%
    map(unlist) %>%
    map_dbl(~get_thruster_output(instructions, .)) %>%
    max()
}

test_that("thruster output works", {
  expect_equal(
    get_thruster_output(
      instructions = c(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0),
      c(4, 3, 2, 1, 0)
    ),
    43210
  )
  expect_equal(
    get_thruster_output(
      instructions = c(3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0),
      c(0,1,2,3,4)
    ),
    54321
  )
  expect_equal(
    get_thruster_output(
      instructions = c(3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0),
      c(1,0,4,3,2)
    ),
    65210
  )
})

test_that("max thruster output works", {
  expect_equal(
    get_max_thruster_output(c(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0)),
    43210
  )
})

answer <- get_max_thruster_output(sequence)
answer

run_amp <- function(amp, input) {
  while (amp$instructions[list(amp$i, TRUE)] != 99) {
    value <- amp$instructions[list(amp$i, TRUE)]
    
    op_code <- value %% 100
    p1_is_immediate <- value %% 1000 %/% 100
    p2_is_immediate <- value %% 10000 %/% 1000
    p3_is_immediate <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(amp$i + 1, p1_is_immediate)
    p2 <- list(amp$i + 2, p2_is_immediate)
    p3 <- list(amp$i + 3, p3_is_immediate)
    
    if (op_code == 1) {
      amp$instructions[p3] <- amp$instructions[p1] + amp$instructions[p2]
    } else if (op_code == 2) {
      amp$instructions[p3] <- amp$instructions[p1] * amp$instructions[p2]
    } else if (op_code == 3) {
      # The first input instruction (opcode 3) is the phase setting
      if (amp$first_input) {
        amp$instructions[p1] <- amp$phase
        amp$first_input <- FALSE
      } else if (!is.na(input)) {
        amp$instructions[p1] <- input
        input <- NA # Only use the input once
      } else {
        break # No input, so go to next amplifier
      }
    } else if (op_code == 4) {
      amp$output <- amp$instructions[p1]
    } else if (op_code == 5) {
      if (amp$instructions[p1] != 0) {
        amp$i <- amp$instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (amp$instructions[p1] == 0) {
        amp$i = get_index(amp$instructions, p2) - 1
        amp$i <- amp$instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      amp$instructions[p3] <- amp$instructions[p1] < amp$instructions[p2]
    } else if (op_code == 8) {
      amp$instructions[p3] <- amp$instructions[p1] == amp$instructions[p2]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(amp$instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    amp$i <- amp$i + 1 + num_params
  }
  
  if (amp$instructions[list(amp$i, TRUE)] == 99) {
    amp$is_halted <- TRUE
  }
  
  amp
}

create_amp <- function(instructions, phase) {
  list(
    instructions = structure(instructions, class = "special_index"),
    phase = phase,
    i = 0,
    first_input = TRUE,
    is_halted = FALSE,
    output = NULL
  )
}

get_thruster_output2 <- function(instructions, phases, a_input = 0) {
  amp_a <- create_amp(instructions, phases[[1]])
  amp_b <- create_amp(instructions, phases[[2]])
  amp_c <- create_amp(instructions, phases[[3]])
  amp_d <- create_amp(instructions, phases[[4]])
  amp_e <- create_amp(instructions, phases[[5]])
  
  while (!amp_e$is_halted) {
    amp_a <- run_amp(amp_a, a_input)
    amp_b <- run_amp(amp_b, amp_a$output)
    amp_c <- run_amp(amp_c, amp_b$output)
    amp_d <- run_amp(amp_d, amp_c$output)
    amp_e <- run_amp(amp_e, amp_d$output)

    a_input <- amp_e$output
  }

  thruster_output <- amp_e$output
  thruster_output
}

get_max_thruster_output2 <- function(instructions) {
  gtools::permutations(n = 5, r = 5, v = seq(from = 5, to = 9, by = 1)) %>%
    array_tree() %>%
    map(unlist) %>%
    map_dbl(~get_thruster_output2(instructions, .)) %>%
    max()
}

test_that("part2 thruster output works", {
  expect_equal(
    get_thruster_output2(
      instructions = c(3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5),
      c(9, 8, 7, 6, 5)
    ),
    139629729
  )
  expect_equal(
    get_thruster_output2(
      instructions = c(3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10),
      c(9,7,8,5,6)
    ),
    18216
  )
})

test_that("part2 max thruster output works", {
  expect_equal(
    get_max_thruster_output2(
      instructions = c(3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5)
    ),
    139629729
  )
  expect_equal(
    get_max_thruster_output2(
      instructions = c(3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10)
    ),
    18216
  )
})

answer <- get_max_thruster_output2(sequence)
answer
