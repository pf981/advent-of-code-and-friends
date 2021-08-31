# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/7

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 7: Amplification Circuit ---</h2><p>Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time. To do this, you'll need to configure a series of <a href="https://en.wikipedia.org/wiki/Amplifier">amplifiers</a> already installed on the ship.</p>
# MAGIC <p>There are five <span title="As you can see, I know exactly how rockets work.">amplifiers connected in series</span>; each one receives an input signal and produces an output signal.  They are connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on.  The first amplifier's input value is <code>0</code>, and the last amplifier's output leads to your ship's thrusters.</p>
# MAGIC <pre><code>    O-------O  O-------O  O-------O  O-------O  O-------O
# MAGIC 0 -&gt;| Amp A |-&gt;| Amp B |-&gt;| Amp C |-&gt;| Amp D |-&gt;| Amp E |-&gt; (to thrusters)
# MAGIC     O-------O  O-------O  O-------O  O-------O  O-------O
# MAGIC </code></pre>
# MAGIC <p>The Elves have sent you some <em>Amplifier Controller Software</em> (your puzzle input), a program that should run on your <a href="5">existing Intcode computer</a>. Each amplifier will need to run a copy of the program.</p>
# MAGIC <p>When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier for its current <em>phase setting</em> (an integer from <code>0</code> to <code>4</code>). Each phase setting is used <em>exactly once</em>, but the Elves can't remember which amplifier needs which phase setting.</p>
# MAGIC <p>The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal, and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input signal, it waits until one arrives.)</p>
# MAGIC <p>Your job is to <em>find the largest output signal that can be sent to the thrusters</em> by trying every possible combination of phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.</p>
# MAGIC <p>For example, suppose you want to try the phase setting sequence <code>3,1,2,4,0</code>, which would mean setting amplifier <code>A</code> to phase setting <code>3</code>, amplifier <code>B</code> to setting <code>1</code>, <code>C</code> to <code>2</code>, <code>D</code> to <code>4</code>, and <code>E</code> to <code>0</code>. Then, you could determine the output signal that gets sent from amplifier <code>E</code> to the thrusters with the following steps:</p>
# MAGIC <ul>
# MAGIC <li>Start the copy of the amplifier controller software that will run on amplifier <code>A</code>. At its first input instruction, provide it the amplifier's phase setting, <code>3</code>.  At its second input instruction, provide it the input signal, <code>0</code>.  After some calculations, it will use an output instruction to indicate the amplifier's output signal.</li>
# MAGIC <li>Start the software for amplifier <code>B</code>. Provide it the phase setting (<code>1</code>) and then whatever output signal was produced from amplifier <code>A</code>. It will then produce a new output signal destined for amplifier <code>C</code>.</li>
# MAGIC <li>Start the software for amplifier <code>C</code>, provide the phase setting (<code>2</code>) and the value from amplifier <code>B</code>, then collect its output signal.</li>
# MAGIC <li>Run amplifier <code>D</code>'s software, provide the phase setting (<code>4</code>) and input value, and collect its output signal.</li>
# MAGIC <li>Run amplifier <code>E</code>'s software, provide the phase setting (<code>0</code>) and input value, and collect its output signal.</li>
# MAGIC </ul>
# MAGIC <p>The final output signal from amplifier <code>E</code> would be sent to the thrusters. However, this phase setting sequence may not have been the best one; another sequence might have sent a higher signal to the thrusters.</p>
# MAGIC <p>Here are some example programs:</p>
# MAGIC <ul>
# MAGIC <li><p>Max thruster signal <em><code>43210</code></em> (from phase setting sequence <code>4,3,2,1,0</code>):</p><pre><code>3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0</code></pre></li>
# MAGIC <li><p>Max thruster signal <em><code>54321</code></em> (from phase setting sequence <code>0,1,2,3,4</code>):</p><pre><code>3,23,3,24,1002,24,10,24,1002,23,-1,23,<br>101,5,23,23,1,24,23,23,4,23,99,0,0</code></pre></li>
# MAGIC <li><p>Max thruster signal <em><code>65210</code></em> (from phase setting sequence <code>1,0,4,3,2</code>):</p><pre><code>3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,<br>1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0</code></pre></li>
# MAGIC </ul>
# MAGIC <p>Try every combination of phase settings on the amplifiers.  <em>What is the highest signal that can be sent to the thrusters?</em></p>
# MAGIC </article>

# COMMAND ----------

install.packages("gtools")

# COMMAND ----------

library(testthat)
library(tidyverse)

# COMMAND ----------

input <- "3,8,1001,8,10,8,105,1,0,0,21,34,59,68,85,102,183,264,345,426,99999,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,1002,9,2,9,101,5,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,102,3,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99"

# COMMAND ----------

sequence <- input %>% str_split(",") %>% unlist() %>% parse_integer()
sequence

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

# COMMAND ----------

get_thruster_output <- function(instructions, phases, a_input = 0) {
  a_output <- run_instructions(instructions, phase = phases[[1]], input = a_input)
  b_output <- run_instructions(instructions, phase = phases[[2]], input = a_output)
  c_output <- run_instructions(instructions, phase = phases[[3]], input = b_output)
  d_output <- run_instructions(instructions, phase = phases[[4]], input = c_output)
  e_output <- run_instructions(instructions, phase = phases[[5]], input = d_output)

  thruster_output <- e_output
  thruster_output
}

# COMMAND ----------

get_max_thruster_output <- function(instructions) {
  gtools::permutations(n = 5, r = 5, v = seq(from = 0, to = 4, by = 1)) %>%
    array_tree() %>%
    map(unlist) %>%
    map_dbl(~get_thruster_output(instructions, .)) %>%
    max()
}

# COMMAND ----------

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

# COMMAND ----------

test_that("max thruster output works", {
  expect_equal(
    get_max_thruster_output(c(3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0)),
    43210
  )
})

# COMMAND ----------

answer <- get_max_thruster_output(sequence)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It's no good - in this configuration, the amplifiers can't generate a large enough output signal to produce the thrust you'll need.  The Elves quickly talk you through rewiring the amplifiers into a <em>feedback loop</em>:</p>
# MAGIC <pre><code>      O-------O  O-------O  O-------O  O-------O  O-------O
# MAGIC 0 -+-&gt;| Amp A |-&gt;| Amp B |-&gt;| Amp C |-&gt;| Amp D |-&gt;| Amp E |-.
# MAGIC    |  O-------O  O-------O  O-------O  O-------O  O-------O |
# MAGIC    |                                                        |
# MAGIC    '--------------------------------------------------------+
# MAGIC                                                             |
# MAGIC                                                             v
# MAGIC                                                      (to thrusters)
# MAGIC </code></pre>
# MAGIC <p>Most of the amplifiers are connected as they were before; amplifier <code>A</code>'s output is connected to amplifier <code>B</code>'s input, and so on. <em>However,</em> the output from amplifier <code>E</code> is now connected into amplifier <code>A</code>'s input. This creates the feedback loop: the signal will be sent through the amplifiers <em>many times</em>.</p>
# MAGIC <p>In feedback loop mode, the amplifiers need <em>totally different phase settings</em>: integers from <code>5</code> to <code>9</code>, again each used exactly once. These settings will cause the Amplifier Controller Software to repeatedly take input and produce output many times before halting. Provide each amplifier its phase setting at its first input instruction; all further input/output instructions are for signals.</p>
# MAGIC <p>Don't restart the Amplifier Controller Software on any amplifier during this process. Each one should continue receiving and sending signals until it halts.</p>
# MAGIC <p>All signals sent or received in this process will be between pairs of amplifiers except the very first signal and the very last signal. To start the process, a <code>0</code> signal is sent to amplifier <code>A</code>'s input <em>exactly once</em>.</p>
# MAGIC <p>Eventually, the software on the amplifiers will halt after they have processed the final loop. When this happens, the last output signal from amplifier <code>E</code> is sent to the thrusters. Your job is to <em>find the largest output signal that can be sent to the thrusters</em> using the new phase settings and feedback loop arrangement.</p>
# MAGIC <p>Here are some example programs:</p>
# MAGIC <ul>
# MAGIC <li><p>Max thruster signal <em><code>139629729</code></em> (from phase setting sequence <code>9,8,7,6,5</code>):</p><pre><code>3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,<br>27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5</code></pre></li>
# MAGIC <li><p>Max thruster signal <em><code>18216</code></em> (from phase setting sequence <code>9,7,8,5,6</code>):</p><pre><code>3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,<br>-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,<br>53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10</code></pre></li>
# MAGIC </ul>
# MAGIC <p>Try every combination of the new phase settings on the amplifier feedback loop.  <em>What is the highest signal that can be sent to the thrusters?</em></p>
# MAGIC </article>

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

get_max_thruster_output2 <- function(instructions) {
  gtools::permutations(n = 5, r = 5, v = seq(from = 5, to = 9, by = 1)) %>%
    array_tree() %>%
    map(unlist) %>%
    map_dbl(~get_thruster_output2(instructions, .)) %>%
    max()
}

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

answer <- get_max_thruster_output2(sequence)
answer
