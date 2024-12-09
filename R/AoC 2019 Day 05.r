library(tidyverse)



instructions  <-
  input %>%
  str_split(",") %>%
  unlist() %>%
  parse_integer()
instructions

`[.special_index` <- function(df, i) {
  index <- i[[1]] + 1
  if (!i[[2]]) {
    index <- df[[index]] + 1
  }
  df[[index]]
}

`[<-.special_index` <- function(df, i, j, value) {
  index <- i[[1]] + 1
  if (!i[[2]]) {
    index <- df[[index]] + 1
  }
  df[[index]] <- value
  
  df
}

run_instructions <- function(instructions, input = 1) {
  instructions <- structure(instructions, class = "special_index")
  
  i <- 0
  
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
      instructions[p1] <- input
    } else if (op_code == 4) {
      input <- instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i))
    }
    
    i <- i + 2
    if (op_code %in% c(1, 2)) {
      i <- i + 2
    }
  }
  
  input
}

answer <- run_instructions(instructions)
answer

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

print_state <- function(instructions, input, i, p1, p2, p3, op_code) {
  num_params <- case_when(
    op_code %in% c(99) ~ 0,
    op_code %in% c(3, 4) ~ 1,
    op_code %in% c(5, 6) ~ 2,
    op_code %in% c(1, 2, 7, 8) ~ 3
  )
  params <- list(p1, p2, p3) %>% head(num_params)
  
  x <- rep_along(instructions, NA) %>% set_names(instructions)
  x[get_index(instructions, list(i, TRUE))] <- "i"
  iwalk(params, function(a, b) x[get_index(instructions, a)] <<- b)
        
  print(x)
  print(glue::glue("\nOp {op_code}: "))
  case_when(
    op_code == 1 ~ "p3 <- {instructions[p1]} + {instructions[p2]} ({instructions[p1] + instructions[p2]})",
    op_code == 2 ~ "p3 <- {instructions[p1]} * {instructions[p2]} ({instructions[p1] * instructions[p2]})",
    op_code == 3 ~ "p1 <- {input}",
    op_code == 4 ~ "input <- {instructions[p1]}",
    op_code == 5 ~ "IF {instructions[p1]} != 0 ({instructions[p1] != 0}) GOTO p2",
    op_code == 6 ~ "IF {instructions[p1]} == 0 ({instructions[p1] == 0}) GOTO p2",
    op_code == 7 ~ "ifp2 <- {instructions[p1]} == 0 ({instructions[p1] == 0})",
    op_code == 99 ~ "exit"
  ) %>%
    glue::glue() %>%
    print()
  print(glue::glue("\nValue: {input}\n\n"))
}

run_instructions <- function(instructions, input = 1) {
  instructions <- structure(instructions, class = "special_index")
  
  i <- 0
  
  while (instructions[list(i, TRUE)] != 99) {
    value <- instructions[list(i, TRUE)]
    
    op_code <- value %% 100
    p1_is_immediate <- value %% 1000 %/% 100
    p2_is_immediate <- value %% 10000 %/% 1000
    p3_is_immediate <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_is_immediate)
    p2 <- list(i + 2, p2_is_immediate)
    p3 <- list(i + 3, p3_is_immediate)
    
    # print_state(instructions, input, i, p1, p2, p3, op_code)
    
    if (op_code == 1) {
      instructions[p3] <- instructions[p1] + instructions[p2]
    } else if (op_code == 2) {
      instructions[p3] <- instructions[p1] * instructions[p2]
    } else if (op_code == 3) {
      instructions[p1] <- input
    } else if (op_code == 4) {
      input <- instructions[p1]
    } else if (op_code == 5) {
      if (instructions[p1] != 0) {
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (instructions[p1] == 0) {
        # i = get_index(instructions, p2) - 1
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

# Tests

library("testthat")

test_that("position mode equal to works", {
  expect_equal(run_instructions(c(3,9,8,9,10,9,4,9,99,-1,8), 8), 1)
  expect_equal(run_instructions(c(3,9,8,9,10,9,4,9,99,-1,8), 5), 0)
})

test_that("position mode less than to works", {
  expect_equal(run_instructions(c(3,9,7,9,10,9,4,9,99,-1,8), 7), 1)
  expect_equal(run_instructions(c(3,9,7,9,10,9,4,9,99,-1,8), 8), 0)
  expect_equal(run_instructions(c(3,9,7,9,10,9,4,9,99,-1,8), 9), 0)
})

test_that("immediate mode equal to works", {
  expect_equal(run_instructions(c(3,3,1108,-1,8,3,4,3,99), 8), 1)
  expect_equal(run_instructions(c(3,3,1108,-1,8,3,4,3,99), 5), 0)
})

test_that("immediate mode less than to works", {
  expect_equal(run_instructions(c(3,3,1107,-1,8,3,4,3,99), 7), 1)
  expect_equal(run_instructions(c(3,3,1107,-1,8,3,4,3,99), 8), 0)
  expect_equal(run_instructions(c(3,3,1107,-1,8,3,4,3,99), 9), 0)
})

# BUG HERE
test_that("position mode jump works", {
  expect_equal(run_instructions(c(3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9), 0), 0)
  expect_equal(run_instructions(c(3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9), 1), 1)
  expect_equal(run_instructions(c(3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9), 99), 1)
})

test_that("immediate mode jump works", {
  expect_equal(run_instructions(c(3,3,1105,-1,9,1101,0,0,12,4,12,99,1), 0), 0)
  expect_equal(run_instructions(c(3,3,1105,-1,9,1101,0,0,12,4,12,99,1), 1), 1)
  expect_equal(run_instructions(c(3,3,1105,-1,9,1101,0,0,12,4,12,99,1), 99), 1)
})

test_that("larger example works", {
  expect_equal(run_instructions(c(3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99), 5), 999)
  expect_equal(run_instructions(c(3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99), 8), 1000)
  expect_equal(run_instructions(c(3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99), 9), 1001)
})

answer <- run_instructions(instructions, 5)
answer
