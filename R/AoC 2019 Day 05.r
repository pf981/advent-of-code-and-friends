# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/5

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 5: Sunny with a Chance of Asteroids ---</h2><p>You're starting to sweat as the ship makes its way toward Mercury.  The Elves suggest that you get the air conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.</p>
# MAGIC <p>The Thermal Environment Supervision Terminal (TEST) starts by running a <em>diagnostic program</em> (your puzzle input).  The TEST diagnostic program will run on <a href="2">your existing Intcode computer</a> after a few modifications:</p>
# MAGIC <p><em>First</em>, you'll need to add <em>two new instructions</em>:</p>
# MAGIC <ul>
# MAGIC <li>Opcode <code>3</code> takes a single integer as <em>input</em> and saves it to the position given by its only parameter. For example, the instruction <code>3,50</code> would take an input value and store it at address <code>50</code>.</li>
# MAGIC <li>Opcode <code>4</code> <em>outputs</em> the value of its only parameter. For example, the instruction <code>4,50</code> would output the value at address <code>50</code>.</li>
# MAGIC </ul>
# MAGIC <p>Programs that use these instructions will come with documentation that explains what should be connected to the input and output. The program <code>3,0,4,0,99</code> outputs whatever it gets as input, then halts.</p>
# MAGIC <p><em>Second</em>, you'll need to add support for <em>parameter modes</em>:</p>
# MAGIC <p>Each parameter of an instruction is handled based on its parameter mode.  Right now, your ship computer already understands parameter mode <code>0</code>, <em>position mode</em>, which causes the parameter to be interpreted as a <em>position</em> - if the parameter is <code>50</code>, its value is <em>the value stored at address <code>50</code> in memory</em>. Until now, all parameters have been in position mode.</p>
# MAGIC <p>Now, your ship computer will also need to handle parameters in mode <code>1</code>, <em>immediate mode</em>. In immediate mode, a parameter is interpreted as a <em>value</em> - if the parameter is <code>50</code>, its value is simply <em><code>50</code></em>.</p>
# MAGIC <p>Parameter modes are stored in the same value as the instruction's opcode.  The opcode is a two-digit number based only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are <code>0</code>.</p>
# MAGIC <p>For example, consider the program <code>1002,4,3,4,33</code>.</p>
# MAGIC <p>The first instruction, <code>1002,4,3,4</code>, is a <em>multiply</em> instruction - the rightmost two digits of the first value, <code>02</code>, indicate opcode <code>2</code>, multiplication.  Then, going right to left, the parameter modes are <code>0</code> (hundreds digit), <code>1</code> (thousands digit), and <code>0</code> (ten-thousands digit, not present and therefore zero):</p>
# MAGIC <pre><code>ABCDE
# MAGIC  1002
# MAGIC 
# MAGIC DE - two-digit opcode,      02 == opcode 2
# MAGIC  C - mode of 1st parameter,  0 == position mode
# MAGIC  B - mode of 2nd parameter,  1 == immediate mode
# MAGIC  A - mode of 3rd parameter,  0 == position mode,
# MAGIC                                   omitted due to being a leading zero
# MAGIC </code></pre>
# MAGIC <p>This instruction multiplies its first two parameters.  The first parameter, <code>4</code> in position mode, works like it did before - its value is the value stored at address <code>4</code> (<code>33</code>). The second parameter, <code>3</code> in immediate mode, simply has value <code>3</code>. The result of this operation, <code>33 * 3 = 99</code>, is written according to the third parameter, <code>4</code> in position mode, which also works like it did before - <code>99</code> is written to address <code>4</code>.</p>
# MAGIC <p>Parameters that an instruction writes to will <em>never be in immediate mode</em>.</p>
# MAGIC <p><em>Finally</em>, some notes:</p>
# MAGIC <ul>
# MAGIC <li>It is important to remember that the instruction pointer should increase by <em>the number of values in the instruction</em> after the instruction finishes. Because of the new instructions, this amount is no longer always <code>4</code>.</li>
# MAGIC <li>Integers can be negative: <code>1101,100,-1,4,0</code> is a valid program (find <code>100 + -1</code>, store the result in position <code>4</code>).</li>
# MAGIC </ul>
# MAGIC <p>The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an <em>input</em> instruction - provide it <code>1</code>, the ID for the ship's air conditioner unit.</p>
# MAGIC <p>It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test, it will run an <em>output</em> instruction indicating how far the result of the test was from the expected value, where <code>0</code> means the test was successful.  Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed.</p>
# MAGIC <p>Finally, the program will output a <em>diagnostic code</em> and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished.  If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.</p>
# MAGIC <p>After providing <code>1</code> to the only input instruction and passing all the tests, <em>what diagnostic code does the program produce?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,61,225,101,34,121,224,1001,224,-49,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1101,67,29,225,1,14,65,224,101,-124,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,20,225,1102,27,15,225,1102,18,79,224,101,-1422,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,20,44,225,1001,69,5,224,101,-32,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,15,10,225,1101,6,70,225,102,86,40,224,101,-2494,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,25,15,225,1101,40,67,224,1001,224,-107,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,126,95,224,101,-1400,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1002,151,84,224,101,-2100,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,509,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"

# COMMAND ----------

instructions  <-
  input %>%
  str_split(",") %>%
  unlist() %>%
  parse_integer()
instructions

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

answer <- run_instructions(instructions)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner <span title="Honestly, I'm not sure what you expected.">can't vent its heat anywhere</span> but back into the spacecraft, it's actually making the air inside the ship <em>warmer</em>.</p>
# MAGIC <p>Instead, you'll need to use the TEST to extend the <a href="https://en.wikipedia.org/wiki/Spacecraft_thermal_control">thermal radiators</a>. Fortunately, the diagnostic program (your puzzle input) is already equipped for this.  Unfortunately, your Intcode computer is not.</p>
# MAGIC <p>Your computer is only missing a few opcodes:</p>
# MAGIC <ul>
# MAGIC <li>Opcode <code>5</code> is <em>jump-if-true</em>: if the first parameter is <em>non-zero</em>, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.</li>
# MAGIC <li>Opcode <code>6</code> is <em>jump-if-false</em>: if the first parameter <em>is zero</em>, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.</li>
# MAGIC <li>Opcode <code>7</code> is <em>less than</em>: if the first parameter is <em>less than</em> the second parameter, it stores <code>1</code> in the position given by the third parameter.  Otherwise, it stores <code>0</code>.</li>
# MAGIC <li>Opcode <code>8</code> is <em>equals</em>: if the first parameter is <em>equal to</em> the second parameter, it stores <code>1</code> in the position given by the third parameter.  Otherwise, it stores <code>0</code>.</li>
# MAGIC </ul>
# MAGIC <p>Like all instructions, these instructions need to support <em>parameter modes</em> as described above.</p>
# MAGIC <p>Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. <em>However</em>, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is <em>not automatically increased</em>.</p>
# MAGIC <p>For example, here are several programs that take one input, compare it to the value <code>8</code>, and then produce one output:</p>
# MAGIC <ul>
# MAGIC <li><code>3,9,8,9,10,9,4,9,99,-1,8</code> - Using <em>position mode</em>, consider whether the input is <em>equal to</em> <code>8</code>; output <code>1</code> (if it is) or <code>0</code> (if it is not).</li>
# MAGIC <li><code>3,9,7,9,10,9,4,9,99,-1,8</code> - Using <em>position mode</em>, consider whether the input is <em>less than</em> <code>8</code>; output <code>1</code> (if it is) or <code>0</code> (if it is not).</li>
# MAGIC <li><code>3,3,1108,-1,8,3,4,3,99</code> - Using <em>immediate mode</em>, consider whether the input is <em>equal to</em> <code>8</code>; output <code>1</code> (if it is) or <code>0</code> (if it is not).</li>
# MAGIC <li><code>3,3,1107,-1,8,3,4,3,99</code> - Using <em>immediate mode</em>, consider whether the input is <em>less than </em><code>8</code>; output <code>1</code> (if it is) or <code>0</code> (if it is not).</li>
# MAGIC </ul>
# MAGIC <p>Here are some jump tests that take an input, then output <code>0</code> if the input was zero or <code>1</code> if the input was non-zero:</p>
# MAGIC <ul>
# MAGIC <li><code>3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9</code> (using <em>position mode</em>)</li>
# MAGIC <li><code>3,3,1105,-1,9,1101,0,0,12,4,12,99,1</code> (using <em>immediate mode</em>)</li>
# MAGIC </ul>
# MAGIC <p>Here's a larger example:</p>
# MAGIC <pre><code>3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# MAGIC 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# MAGIC 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
# MAGIC </code></pre>
# MAGIC <p>The above example program uses an input instruction to ask for a single number.  The program will then output <code>999</code> if the input value is below <code>8</code>, output <code>1000</code> if the input value is equal to <code>8</code>, or output <code>1001</code> if the input value is greater than <code>8</code>.</p>
# MAGIC <p>This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, <em>provide it <code>5</code></em>, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the <em>diagnostic code</em>.</p>
# MAGIC <p><em>What is the diagnostic code for system ID <code>5</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

answer <- run_instructions(instructions, 5)
answer
