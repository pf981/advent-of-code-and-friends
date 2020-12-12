# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/9

# COMMAND ----------

library(tidyverse)
library(glue)

# COMMAND ----------

input <- "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,0,1020,1102,1,800,1023,1101,0,388,1025,1101,0,31,1012,1102,1,1,1021,1101,22,0,1014,1101,0,30,1002,1101,0,716,1027,1102,32,1,1009,1101,0,38,1017,1102,20,1,1015,1101,33,0,1016,1101,0,35,1007,1101,0,25,1005,1102,28,1,1011,1102,1,36,1008,1101,0,39,1001,1102,1,21,1006,1101,397,0,1024,1102,1,807,1022,1101,0,348,1029,1101,0,23,1003,1101,29,0,1004,1102,1,26,1013,1102,34,1,1018,1102,1,37,1010,1101,0,27,1019,1102,24,1,1000,1101,353,0,1028,1101,0,723,1026,109,14,2101,0,-9,63,1008,63,27,63,1005,63,205,1001,64,1,64,1106,0,207,4,187,1002,64,2,64,109,-17,2108,24,6,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,7,2101,0,2,63,1008,63,21,63,1005,63,255,4,235,1001,64,1,64,1106,0,255,1002,64,2,64,109,-7,2108,29,7,63,1005,63,273,4,261,1106,0,277,1001,64,1,64,1002,64,2,64,109,10,1208,-5,31,63,1005,63,293,1105,1,299,4,283,1001,64,1,64,1002,64,2,64,109,2,1207,-1,35,63,1005,63,315,1106,0,321,4,305,1001,64,1,64,1002,64,2,64,109,8,1205,3,333,1106,0,339,4,327,1001,64,1,64,1002,64,2,64,109,11,2106,0,0,4,345,1106,0,357,1001,64,1,64,1002,64,2,64,109,-15,21108,40,40,6,1005,1019,379,4,363,1001,64,1,64,1106,0,379,1002,64,2,64,109,16,2105,1,-5,4,385,1001,64,1,64,1105,1,397,1002,64,2,64,109,-25,2102,1,-1,63,1008,63,26,63,1005,63,421,1001,64,1,64,1106,0,423,4,403,1002,64,2,64,109,-8,1202,9,1,63,1008,63,25,63,1005,63,445,4,429,1105,1,449,1001,64,1,64,1002,64,2,64,109,5,1207,0,40,63,1005,63,467,4,455,1106,0,471,1001,64,1,64,1002,64,2,64,109,-6,2107,24,8,63,1005,63,487,1105,1,493,4,477,1001,64,1,64,1002,64,2,64,109,15,21107,41,40,1,1005,1011,509,1106,0,515,4,499,1001,64,1,64,1002,64,2,64,109,12,1205,-1,529,4,521,1105,1,533,1001,64,1,64,1002,64,2,64,109,-20,2102,1,2,63,1008,63,29,63,1005,63,555,4,539,1105,1,559,1001,64,1,64,1002,64,2,64,109,15,1201,-9,0,63,1008,63,38,63,1005,63,579,1105,1,585,4,565,1001,64,1,64,1002,64,2,64,109,-2,21102,42,1,-3,1008,1012,44,63,1005,63,609,1001,64,1,64,1106,0,611,4,591,1002,64,2,64,109,-21,2107,29,8,63,1005,63,629,4,617,1106,0,633,1001,64,1,64,1002,64,2,64,109,15,1202,0,1,63,1008,63,30,63,1005,63,657,1001,64,1,64,1106,0,659,4,639,1002,64,2,64,109,15,21102,43,1,-8,1008,1016,43,63,1005,63,681,4,665,1105,1,685,1001,64,1,64,1002,64,2,64,109,-10,21107,44,45,-4,1005,1010,707,4,691,1001,64,1,64,1106,0,707,1002,64,2,64,109,11,2106,0,2,1001,64,1,64,1106,0,725,4,713,1002,64,2,64,109,-16,21101,45,0,8,1008,1017,43,63,1005,63,749,1001,64,1,64,1105,1,751,4,731,1002,64,2,64,109,-3,1208,2,36,63,1005,63,773,4,757,1001,64,1,64,1106,0,773,1002,64,2,64,109,18,1206,-4,787,4,779,1105,1,791,1001,64,1,64,1002,64,2,64,109,-8,2105,1,7,1001,64,1,64,1106,0,809,4,797,1002,64,2,64,109,-2,21108,46,44,2,1005,1016,825,1105,1,831,4,815,1001,64,1,64,1002,64,2,64,109,7,21101,47,0,-8,1008,1013,47,63,1005,63,857,4,837,1001,64,1,64,1105,1,857,1002,64,2,64,109,-17,1201,-4,0,63,1008,63,24,63,1005,63,883,4,863,1001,64,1,64,1105,1,883,1002,64,2,64,109,10,1206,7,895,1106,0,901,4,889,1001,64,1,64,4,64,99,21102,1,27,1,21102,1,915,0,1105,1,922,21201,1,24405,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22102,1,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0"

# COMMAND ----------

input <- "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"

# COMMAND ----------

# i is a two-element list. The first is the 0-indexed index. The second is
#  - TRUE if the index is in immediate mode. This means i is just i
#  - FALSE if the index is relative. This means i really means df[i]
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

# COMMAND ----------

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
  print(glue("\nOp {op_code}: "))
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
    glue() %>%
    print()
  print(glue("\nValue: {input}\n\n"))
}

# COMMAND ----------

run_instructions <- function(instructions, input = 1) {
  instructions <- structure(instructions, class = "special_index")
  
  i <- 0
  relative_base <- 0
  
  while (instructions[list(i, 1)] != 99) {
    value <- instructions[list(i, 1)]
    
    op_code <- value %% 100
    p1_is_immediate <- value %% 1000 %/% 100
    p2_is_immediate <- value %% 10000 %/% 1000
    p3_is_immediate <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_is_immediate)
    p2 <- list(i + 2, p2_is_immediate)
    p3 <- list(i + 3, p3_is_immediate)
    
    print_state(instructions, input, i, p1, p2, p3, op_code)
    
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
      relative_base <- instructions[p1]
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

# COMMAND ----------

run_instructions(c(3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9), 0)

# COMMAND ----------

# MAGIC %md ## WIP

# COMMAND ----------

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(df, i) {
  index <- i[[1]] + 1
  if (i[[2]] == 0) {
    # Relative mode
    index <- df[[index]] + 1
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- df[[index + attr(instructions, "relative_base")]] + 1
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

# COMMAND ----------

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
  print(glue("\nOp {op_code}: "))
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
    glue() %>%
    print()
  print(glue("\nValue: {input}\n\n"))
}

# COMMAND ----------

run_instructions <- function(instructions, input = 1) {
  instructions <- structure(instructions, class = "special_index")
  attr(instructions, "relative_base") <- 0
  
  i <- 0
  
  while (instructions[list(i, 1)] != 99) {
    value <- instructions[list(i, 1)]
    
    op_code <- value %% 100
    p1_is_immediate <- value %% 1000 %/% 100
    p2_is_immediate <- value %% 10000 %/% 1000
    p3_is_immediate <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_is_immediate)
    p2 <- list(i + 2, p2_is_immediate)
    p3 <- list(i + 3, p3_is_immediate)
    
    print_state(instructions, input, i, p1, p2, p3, op_code)
    
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
      attr(instructions, "relative_base") <- instructions[p1]
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

# COMMAND ----------

# MAGIC %md ### Tests

# COMMAND ----------

library("testthat")

# COMMAND ----------

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

# COMMAND ----------

test_that("relative mode works", {
  # expect_equal(run_instructions(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), 0), c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99)) # Maybe?, maybe concat?
  expect_equal(nchar(run_instructions(c(1102,34915192,34915192,7,4,7,99,0), 0)), 16)
  expect_equal(run_instructions(c(104,1125899906842624,99), 0), 1125899906842624)
})

# COMMAND ----------

run_instructions(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), 0)

# COMMAND ----------

# MAGIC %md IMPORTANT NOTE: You need to expand memory with instructions <- c(instructions, numeric(100000))

# COMMAND ----------

# WIP:
library(tidyverse)
library(glue)

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


print_state <- function(instructions, input, i, p1, p2, p3, op_code) {
  num_params <- case_when(
    op_code %in% c(99) ~ 0,
    op_code %in% c(3, 4, 9) ~ 1,
    op_code %in% c(5, 6) ~ 2,
    op_code %in% c(1, 2, 7, 8) ~ 3
  )
  params <- list(p1, p2, p3) %>% head(num_params)
  
  x <- rep_along(instructions, NA) %>% set_names(instructions)
  x[get_index(instructions, list(i, TRUE))] <- "i"
  iwalk(params, function(a, b) x[get_index(instructions, a)] <<- b)
  
  message(x)
  message(glue("\nOp {op_code}: "))
  case_when(
    op_code == 1 ~ "p3 <- {instructions[p1]} + {instructions[p2]} ({instructions[p1] + instructions[p2]})",
    op_code == 2 ~ "p3 <- {instructions[p1]} * {instructions[p2]} ({instructions[p1] * instructions[p2]})",
    op_code == 3 ~ "p1 <- {input}",
    op_code == 4 ~ "input <- {instructions[p1]}",
    op_code == 5 ~ "IF {instructions[p1]} != 0 ({instructions[p1] != 0}) GOTO p2",
    op_code == 6 ~ "IF {instructions[p1]} == 0 ({instructions[p1] == 0}) GOTO p2",
    op_code == 7 ~ "ifp2 <- {instructions[p1]} == 0 ({instructions[p1] == 0})",
    op_code == 9 ~ "relative_base <- {instructions[p1]}",
    op_code == 99 ~ "exit"
  ) %>%
    glue() %>%
    message()
  message(glue("\nValue: {input}\n\n"))
}


run_instructions <- function(instructions, input = 1) {
  # instructions <- c(instructions, integer(100000))
  instructions <- c(instructions, numeric(100000))
  instructions <- structure(instructions, class = "special_index")
  attr(instructions, "relative_base") <- 0
  
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
      attr(instructions, "relative_base") <- instructions[p1]
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
  
  input
}


# run_instructions(c(1102,34915192,34915192,7,4,7,99,0), 0)
run_instructions(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), 0)
# 
# input <- 0
# instructions <- structure(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), class = "special_index")


# 109,1, - Base set to 1
# 204,-1, - Set input to instruction[0] (which is 109)
# 1001,100,1,100,1008,100,16,101,1006,101,0,99


input <- "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,0,1020,1102,1,800,1023,1101,0,388,1025,1101,0,31,1012,1102,1,1,1021,1101,22,0,1014,1101,0,30,1002,1101,0,716,1027,1102,32,1,1009,1101,0,38,1017,1102,20,1,1015,1101,33,0,1016,1101,0,35,1007,1101,0,25,1005,1102,28,1,1011,1102,1,36,1008,1101,0,39,1001,1102,1,21,1006,1101,397,0,1024,1102,1,807,1022,1101,0,348,1029,1101,0,23,1003,1101,29,0,1004,1102,1,26,1013,1102,34,1,1018,1102,1,37,1010,1101,0,27,1019,1102,24,1,1000,1101,353,0,1028,1101,0,723,1026,109,14,2101,0,-9,63,1008,63,27,63,1005,63,205,1001,64,1,64,1106,0,207,4,187,1002,64,2,64,109,-17,2108,24,6,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,7,2101,0,2,63,1008,63,21,63,1005,63,255,4,235,1001,64,1,64,1106,0,255,1002,64,2,64,109,-7,2108,29,7,63,1005,63,273,4,261,1106,0,277,1001,64,1,64,1002,64,2,64,109,10,1208,-5,31,63,1005,63,293,1105,1,299,4,283,1001,64,1,64,1002,64,2,64,109,2,1207,-1,35,63,1005,63,315,1106,0,321,4,305,1001,64,1,64,1002,64,2,64,109,8,1205,3,333,1106,0,339,4,327,1001,64,1,64,1002,64,2,64,109,11,2106,0,0,4,345,1106,0,357,1001,64,1,64,1002,64,2,64,109,-15,21108,40,40,6,1005,1019,379,4,363,1001,64,1,64,1106,0,379,1002,64,2,64,109,16,2105,1,-5,4,385,1001,64,1,64,1105,1,397,1002,64,2,64,109,-25,2102,1,-1,63,1008,63,26,63,1005,63,421,1001,64,1,64,1106,0,423,4,403,1002,64,2,64,109,-8,1202,9,1,63,1008,63,25,63,1005,63,445,4,429,1105,1,449,1001,64,1,64,1002,64,2,64,109,5,1207,0,40,63,1005,63,467,4,455,1106,0,471,1001,64,1,64,1002,64,2,64,109,-6,2107,24,8,63,1005,63,487,1105,1,493,4,477,1001,64,1,64,1002,64,2,64,109,15,21107,41,40,1,1005,1011,509,1106,0,515,4,499,1001,64,1,64,1002,64,2,64,109,12,1205,-1,529,4,521,1105,1,533,1001,64,1,64,1002,64,2,64,109,-20,2102,1,2,63,1008,63,29,63,1005,63,555,4,539,1105,1,559,1001,64,1,64,1002,64,2,64,109,15,1201,-9,0,63,1008,63,38,63,1005,63,579,1105,1,585,4,565,1001,64,1,64,1002,64,2,64,109,-2,21102,42,1,-3,1008,1012,44,63,1005,63,609,1001,64,1,64,1106,0,611,4,591,1002,64,2,64,109,-21,2107,29,8,63,1005,63,629,4,617,1106,0,633,1001,64,1,64,1002,64,2,64,109,15,1202,0,1,63,1008,63,30,63,1005,63,657,1001,64,1,64,1106,0,659,4,639,1002,64,2,64,109,15,21102,43,1,-8,1008,1016,43,63,1005,63,681,4,665,1105,1,685,1001,64,1,64,1002,64,2,64,109,-10,21107,44,45,-4,1005,1010,707,4,691,1001,64,1,64,1106,0,707,1002,64,2,64,109,11,2106,0,2,1001,64,1,64,1106,0,725,4,713,1002,64,2,64,109,-16,21101,45,0,8,1008,1017,43,63,1005,63,749,1001,64,1,64,1105,1,751,4,731,1002,64,2,64,109,-3,1208,2,36,63,1005,63,773,4,757,1001,64,1,64,1106,0,773,1002,64,2,64,109,18,1206,-4,787,4,779,1105,1,791,1001,64,1,64,1002,64,2,64,109,-8,2105,1,7,1001,64,1,64,1106,0,809,4,797,1002,64,2,64,109,-2,21108,46,44,2,1005,1016,825,1105,1,831,4,815,1001,64,1,64,1002,64,2,64,109,7,21101,47,0,-8,1008,1013,47,63,1005,63,857,4,837,1001,64,1,64,1105,1,857,1002,64,2,64,109,-17,1201,-4,0,63,1008,63,24,63,1005,63,883,4,863,1001,64,1,64,1105,1,883,1002,64,2,64,109,10,1206,7,895,1106,0,901,4,889,1001,64,1,64,4,64,99,21102,1,27,1,21102,1,915,0,1105,1,922,21201,1,24405,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22102,1,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0"

input %>% str_split(",") %>% unlist() %>% parse_integer() %>% run_instructions(100)


# COMMAND ----------

# More experimentation
library(tidyverse)
library(glue)

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
  df[[as.integer(get_index(df, i))]]
}

`[<-.special_index` <- function(df, i, j, value) {
  df[[as.integer(get_index(df, i))]] <- value
  
  df
}

as.integer64.special_index <- function(x) {
  if (!inherits(x, "integer64")) stop("x must inherit integer64")
  class(x) <- "integer64"
  x
}


print_state <- function(instructions, input, i, p1, p2, p3, op_code) {
  num_params <- case_when(
    op_code %in% c(99) ~ 0,
    op_code %in% c(3, 4, 9) ~ 1,
    op_code %in% c(5, 6) ~ 2,
    op_code %in% c(1, 2, 7, 8) ~ 3
  )
  params <- list(p1, p2, p3) %>% head(num_params)
  
  x <- rep_along(instructions, NA) %>% set_names(instructions)
  x[get_index(instructions, list(i, TRUE))] <- "i"
  iwalk(params, function(a, b) x[get_index(instructions, a)] <<- b)
  
  message(x)
  message(glue("\nOp {op_code}: "))
  case_when(
    op_code == 1 ~ "p3 <- {instructions[p1]} + {instructions[p2]} ({instructions[p1] + instructions[p2]})",
    op_code == 2 ~ "p3 <- {instructions[p1]} * {instructions[p2]} ({instructions[p1] * instructions[p2]})",
    op_code == 3 ~ "p1 <- {input}",
    op_code == 4 ~ "input <- {instructions[p1]}",
    op_code == 5 ~ "IF {instructions[p1]} != 0 ({instructions[p1] != 0}) GOTO p2",
    op_code == 6 ~ "IF {instructions[p1]} == 0 ({instructions[p1] == 0}) GOTO p2",
    op_code == 7 ~ "ifp2 <- {instructions[p1]} == 0 ({instructions[p1] == 0})",
    op_code == 9 ~ "relative_base <- {instructions[p1]}",
    op_code == 99 ~ "exit"
  ) %>%
    glue() %>%
    message()
  message(glue("\nValue: {input}\n\n"))
}


run_instructions <- function(instructions, input = 1) {
  message("TEST!")
  instructions <- bit64::as.integer64(c(instructions, integer(100000)))
  class(instructions) <- c("special_index", class(instructions))
  
  attr(instructions, "relative_base") <- 0
  
  i <- 0
  
  while (instructions[list(i, 1)] != 99) {
    value <- instructions[list(i, 1)]
    
    op_code <- as.integer(value %% 100)
    p1_index_mode <- as.integer(value %% 1000 %/% 100)
    p2_index_mode <- as.integer(value %% 10000 %/% 1000)
    p3_index_mode <- as.integer(value %% 100000 %/% 10000) # Unused
    
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
    } else if (op_code == 5) {
      if (instructions[p1] != 0) {
        i <- as.integer(instructions[p2])
        next
      }
    } else if (op_code == 6) {
      if (instructions[p1] == 0) {
        i = get_index(instructions, p2) - 1
        i <- as.integer(instructions[p2])
        next
      }
    } else if (op_code == 7) {
      instructions[p3] <- as.integer(instructions[p1] < instructions[p2])
    } else if (op_code == 8) {
      instructions[p3] <- as.integer(instructions[p1] == instructions[p2])
    } else if (op_code == 9) {
      # New instruction: Relative base offset
      attr(instructions, "relative_base") <- instructions[p1]
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
  
  input
}


# run_instructions(c(1102,34915192,34915192,7,4,7,99,0), 0)
run_instructions(c(109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99), 0)