# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/9
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 9: Sensor Boost ---</h2><p>You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress signal coming from the asteroid belt.  It must be the Ceres monitoring station!</p>
# MAGIC <p>In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest <em>BOOST</em> program - Basic Operation Of System Test.</p>
# MAGIC <p>While BOOST (your puzzle input) is capable of boosting your sensors, for <span title="Oh sure, NOW safety is a priority.">tenuous safety reasons</span>, it refuses to do so until the computer it runs on passes some checks to demonstrate it is a <em>complete Intcode computer</em>.</p>
# MAGIC <p><a href="5">Your existing Intcode computer</a> is missing one key feature: it needs support for parameters in <em>relative mode</em>.</p>
# MAGIC <p>Parameters in mode <code>2</code>, <em>relative mode</em>, behave very similarly to parameters in <em>position mode</em>: the parameter is interpreted as a position.  Like position mode, parameters in relative mode can be read from or written to.</p>
# MAGIC <p>The important difference is that relative mode parameters don't count from address <code>0</code>.  Instead, they count from a value called the <em>relative base</em>. The <em>relative base</em> starts at <code>0</code>.</p>
# MAGIC <p>The address a relative mode parameter refers to is itself <em>plus</em> the current <em>relative base</em>. When the relative base is <code>0</code>, relative mode parameters and position mode parameters with the same value refer to the same address.</p>
# MAGIC <p>For example, given a relative base of <code>50</code>, a relative mode parameter of <code>-7</code> refers to memory address <code>50 + -7 = <em>43</em></code>.</p>
# MAGIC <p>The relative base is modified with the <em>relative base offset</em> instruction:</p>
# MAGIC <ul>
# MAGIC <li>Opcode <code>9</code> <em>adjusts the relative base</em> by the value of its only parameter. The relative base increases (or decreases, if the value is negative) by the value of the parameter.</li>
# MAGIC </ul>
# MAGIC <p>For example, if the relative base is <code>2000</code>, then after the instruction <code>109,19</code>, the relative base would be <code>2019</code>. If the next instruction were <code>204,-34</code>, then the value at address <code>1985</code> would be output.</p>
# MAGIC <p>Your Intcode computer will also need a few other capabilities:</p>
# MAGIC <ul>
# MAGIC <li>The computer's available memory should be much larger than the initial program. Memory beyond the initial program starts with the value <code>0</code> and can be read or written like any other memory. (It is invalid to try to access memory at a negative address, though.)</li>
# MAGIC <li>The computer should have support for large numbers. Some instructions near the beginning of the BOOST program will verify this capability.</li>
# MAGIC </ul>
# MAGIC <p>Here are some example programs that use these features:</p>
# MAGIC <ul>
# MAGIC <li><code>109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99</code> takes no input and produces a <a href="https://en.wikipedia.org/wiki/Quine_(computing)">copy of itself</a> as output.</li>
# MAGIC <li><code>1102,34915192,34915192,7,4,7,99,0</code> should output a 16-digit number.</li>
# MAGIC <li><code>104,1125899906842624,99</code> should output the large number in the middle.</li>
# MAGIC </ul>
# MAGIC <p>The BOOST program will ask for a single input; run it in test mode by providing it the value <code>1</code>. It will perform a series of checks on each opcode, output any opcodes (and the associated parameter modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.</p>
# MAGIC <p>Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning opcodes when run in test mode; it should only output a single value, the BOOST keycode. <em>What BOOST keycode does it produce?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>2436480432</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
# MAGIC <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>You now have a complete Intcode computer.</em></p>
# MAGIC <p>Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the BOOST program.</p>
# MAGIC <p>The program runs in sensor boost mode by providing the input instruction the value <code>2</code>.  Once run, it will boost the sensors automatically, but it might take a few seconds to complete the operation on slower hardware.  In sensor boost mode, the program will output a single value: <em>the coordinates of the distress signal</em>.</p>
# MAGIC <p>Run the BOOST program in sensor boost mode.  <em>What are the coordinates of the distress signal?</em></p>
# MAGIC </article>
# MAGIC <form method="post" action="9/answer"><input type="hidden" name="level" value="2"><p>Answer: <input type="text" name="answer" autocomplete="off"> <input type="submit" value="[Submit]"></p></form>
# MAGIC <p>Although it hasn't changed, you can still <a href="9/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Sensor+Boost%22+%2D+Day+9+%2D+Advent+of+Code+2019&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2019%2Fday%2F9&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+Part+One+of+%22Sensor+Boost%22+%2D+Day+9+%2D+Advent+of+Code+2019+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2019%2Fday%2F9'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,1,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,0,1020,1102,1,800,1023,1101,0,388,1025,1101,0,31,1012,1102,1,1,1021,1101,22,0,1014,1101,0,30,1002,1101,0,716,1027,1102,32,1,1009,1101,0,38,1017,1102,20,1,1015,1101,33,0,1016,1101,0,35,1007,1101,0,25,1005,1102,28,1,1011,1102,1,36,1008,1101,0,39,1001,1102,1,21,1006,1101,397,0,1024,1102,1,807,1022,1101,0,348,1029,1101,0,23,1003,1101,29,0,1004,1102,1,26,1013,1102,34,1,1018,1102,1,37,1010,1101,0,27,1019,1102,24,1,1000,1101,353,0,1028,1101,0,723,1026,109,14,2101,0,-9,63,1008,63,27,63,1005,63,205,1001,64,1,64,1106,0,207,4,187,1002,64,2,64,109,-17,2108,24,6,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,7,2101,0,2,63,1008,63,21,63,1005,63,255,4,235,1001,64,1,64,1106,0,255,1002,64,2,64,109,-7,2108,29,7,63,1005,63,273,4,261,1106,0,277,1001,64,1,64,1002,64,2,64,109,10,1208,-5,31,63,1005,63,293,1105,1,299,4,283,1001,64,1,64,1002,64,2,64,109,2,1207,-1,35,63,1005,63,315,1106,0,321,4,305,1001,64,1,64,1002,64,2,64,109,8,1205,3,333,1106,0,339,4,327,1001,64,1,64,1002,64,2,64,109,11,2106,0,0,4,345,1106,0,357,1001,64,1,64,1002,64,2,64,109,-15,21108,40,40,6,1005,1019,379,4,363,1001,64,1,64,1106,0,379,1002,64,2,64,109,16,2105,1,-5,4,385,1001,64,1,64,1105,1,397,1002,64,2,64,109,-25,2102,1,-1,63,1008,63,26,63,1005,63,421,1001,64,1,64,1106,0,423,4,403,1002,64,2,64,109,-8,1202,9,1,63,1008,63,25,63,1005,63,445,4,429,1105,1,449,1001,64,1,64,1002,64,2,64,109,5,1207,0,40,63,1005,63,467,4,455,1106,0,471,1001,64,1,64,1002,64,2,64,109,-6,2107,24,8,63,1005,63,487,1105,1,493,4,477,1001,64,1,64,1002,64,2,64,109,15,21107,41,40,1,1005,1011,509,1106,0,515,4,499,1001,64,1,64,1002,64,2,64,109,12,1205,-1,529,4,521,1105,1,533,1001,64,1,64,1002,64,2,64,109,-20,2102,1,2,63,1008,63,29,63,1005,63,555,4,539,1105,1,559,1001,64,1,64,1002,64,2,64,109,15,1201,-9,0,63,1008,63,38,63,1005,63,579,1105,1,585,4,565,1001,64,1,64,1002,64,2,64,109,-2,21102,42,1,-3,1008,1012,44,63,1005,63,609,1001,64,1,64,1106,0,611,4,591,1002,64,2,64,109,-21,2107,29,8,63,1005,63,629,4,617,1106,0,633,1001,64,1,64,1002,64,2,64,109,15,1202,0,1,63,1008,63,30,63,1005,63,657,1001,64,1,64,1106,0,659,4,639,1002,64,2,64,109,15,21102,43,1,-8,1008,1016,43,63,1005,63,681,4,665,1105,1,685,1001,64,1,64,1002,64,2,64,109,-10,21107,44,45,-4,1005,1010,707,4,691,1001,64,1,64,1106,0,707,1002,64,2,64,109,11,2106,0,2,1001,64,1,64,1106,0,725,4,713,1002,64,2,64,109,-16,21101,45,0,8,1008,1017,43,63,1005,63,749,1001,64,1,64,1105,1,751,4,731,1002,64,2,64,109,-3,1208,2,36,63,1005,63,773,4,757,1001,64,1,64,1106,0,773,1002,64,2,64,109,18,1206,-4,787,4,779,1105,1,791,1001,64,1,64,1002,64,2,64,109,-8,2105,1,7,1001,64,1,64,1106,0,809,4,797,1002,64,2,64,109,-2,21108,46,44,2,1005,1016,825,1105,1,831,4,815,1001,64,1,64,1002,64,2,64,109,7,21101,47,0,-8,1008,1013,47,63,1005,63,857,4,837,1001,64,1,64,1105,1,857,1002,64,2,64,109,-17,1201,-4,0,63,1008,63,24,63,1005,63,883,4,863,1001,64,1,64,1105,1,883,1002,64,2,64,109,10,1206,7,895,1106,0,901,4,889,1001,64,1,64,4,64,99,21102,1,27,1,21102,1,915,0,1105,1,922,21201,1,24405,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,22102,1,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0"

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

input %>% str_split(",") %>% unlist() %>% parse_integer() %>% run_instructions(1)
#> 2436480432

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

input %>% str_split(",") %>% unlist() %>% parse_integer() %>% run_instructions(2)
#> 45710