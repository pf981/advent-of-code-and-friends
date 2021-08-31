# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 18: Duet ---</h2><p>You discover a tablet containing some strange assembly code labeled simply "<a href="https://en.wikipedia.org/wiki/Duet">Duet</a>". Rather than bother the sound card with it, you decide to run the code yourself. Unfortunately, you don't see any documentation, so you're left to figure out what the instructions mean on your own.</p>
# MAGIC <p>It seems like the assembly is meant to operate on a set of <em>registers</em> that are each named with a single letter and that can each hold a single <a href="https://en.wikipedia.org/wiki/Integer">integer</a>. You suppose each register should start with a value of <code>0</code>.</p>
# MAGIC <p>There aren't that many instructions, so it shouldn't be hard to figure out what they do.  Here's what you determine:</p>
# MAGIC <ul>
# MAGIC <li><code>snd X</code> <em><span title="I don't recommend actually trying this.">plays a sound</span></em> with a frequency equal to the value of <code>X</code>.</li>
# MAGIC <li><code>set X Y</code> <em>sets</em> register <code>X</code> to the value of <code>Y</code>.</li>
# MAGIC <li><code>add X Y</code> <em>increases</em> register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>mul X Y</code> sets register <code>X</code> to the result of <em>multiplying</em> the value contained in register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>mod X Y</code> sets register <code>X</code> to the <em>remainder</em> of dividing the value contained in register <code>X</code> by the value of <code>Y</code> (that is, it sets <code>X</code> to the result of <code>X</code> <a href="https://en.wikipedia.org/wiki/Modulo_operation">modulo</a> <code>Y</code>).</li>
# MAGIC <li><code>rcv X</code> <em>recovers</em> the frequency of the last sound played, but only when the value of <code>X</code> is not zero. (If it is zero, the command does nothing.)</li>
# MAGIC <li><code>jgz X Y</code> <em>jumps</em> with an offset of the value of <code>Y</code>, but only if the value of <code>X</code> is <em>greater than zero</em>. (An offset of <code>2</code> skips the next instruction, an offset of <code>-1</code> jumps to the previous instruction, and so on.)</li>
# MAGIC </ul>
# MAGIC <p>Many of the instructions can take either a register (a single letter) or a number. The value of a register is the integer it contains; the value of a number is that number.</p>
# MAGIC <p>After each <em>jump</em> instruction, the program continues with the instruction to which the <em>jump</em> jumped. After any other instruction, the program continues with the next instruction. Continuing (or jumping) off either end of the program terminates it.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>set a 1
# MAGIC add a 2
# MAGIC mul a a
# MAGIC mod a 5
# MAGIC snd a
# MAGIC set a 0
# MAGIC rcv a
# MAGIC jgz a -1
# MAGIC set a 1
# MAGIC jgz a -2
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>The first four instructions set <code>a</code> to <code>1</code>, add <code>2</code> to it, square it, and then set it to itself modulo <code>5</code>, resulting in a value of <code>4</code>.</li>
# MAGIC <li>Then, a sound with frequency <code>4</code> (the value of <code>a</code>) is played.</li>
# MAGIC <li>After that, <code>a</code> is set to <code>0</code>, causing the subsequent <code>rcv</code> and <code>jgz</code> instructions to both be skipped (<code>rcv</code> because <code>a</code> is <code>0</code>, and <code>jgz</code> because <code>a</code> is not greater than <code>0</code>).</li>
# MAGIC <li>Finally, <code>a</code> is set to <code>1</code>, causing the next <code>jgz</code> instruction to activate, jumping back two instructions to another jump, which jumps again to the <code>rcv</code>, which ultimately triggers the <em>recover</em> operation.</li>
# MAGIC </ul>
# MAGIC <p>At the time the <em>recover</em> operation is executed, the frequency of the last sound played is <code>4</code>.</p>
# MAGIC <p><em>What is the value of the recovered frequency</em> (the value of the most recently played sound) the <em>first</em> time a <code>rcv</code> instruction is executed with a non-zero value?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 952
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    x = str_split(line, " ")
  ) %>%
  unnest_wider(x) %>%
  rename(
    instruction = ...1,
    x = ...2,
    y = ...3
  )
df

# COMMAND ----------

get_value <- function(x, state) {
  if (!is.na(as.integer(x))) {
    return(as.integer(x))
  }
  c(state[[x]], 0)[1]
}

solve <- function(df) {
  sound <- 0
  state <- list()
  i <- 1
  repeat {
    instruction <- df$instruction[i]
    x <- df$x[i]
    y <- df$y[i]

    if (instruction == "snd") {
      sound <- get_value(x, state)
    } else if (instruction == "set") {
      state[[x]] <- get_value(y, state)
    } else if (instruction == "add") {
      state[[x]] <- get_value(x, state) + get_value(y, state)
    } else if (instruction == "mul") {
      state[[x]] <- get_value(x, state) * get_value(y, state)
    } else if (instruction == "mod") {
      state[[x]] <- get_value(x, state) %% get_value(y, state)
    } else if (instruction == "rcv") {
      if (get_value(x, state) != 0) {
        return(sound)
      }
    } else if (instruction == "jgz") {
      if (get_value(x, state) > 0) {
        i <- i + get_value(y, state) - 1
      }
    }
    i <- i + 1
  }
}

# COMMAND ----------

solve(df)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you congratulate yourself for a job well done, you notice that the documentation has been on the back of the tablet this entire time. While you actually got most of the instructions correct, there are a few key differences. This assembly code isn't about sound at all - it's meant to be run <em>twice at the same time</em>.</p>
# MAGIC <p>Each running copy of the program has its own set of registers and follows the code independently - in fact, the programs don't even necessarily run at the same speed. To coordinate, they use the <em>send</em> (<code>snd</code>) and <em>receive</em> (<code>rcv</code>) instructions:</p>
# MAGIC <ul>
# MAGIC <li><code>snd X</code> <em>sends</em> the value of <code>X</code> to the other program. These values wait in a queue until that program is ready to receive them. Each program has its own message queue, so a program can never receive a message it sent.</li>
# MAGIC <li><code>rcv X</code> <em>receives</em> the next value and stores it in register <code>X</code>. If no values are in the queue, the program <em>waits for a value to be sent to it</em>. Programs do not continue to the next instruction until they have received a value. Values are received in the order they are sent.</li>
# MAGIC </ul>
# MAGIC <p>Each program also has its own <em>program ID</em> (one <code>0</code> and the other <code>1</code>); the register <code>p</code> should begin with this value.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>snd 1
# MAGIC snd 2
# MAGIC snd p
# MAGIC rcv a
# MAGIC rcv b
# MAGIC rcv c
# MAGIC rcv d
# MAGIC </code></pre>
# MAGIC <p>Both programs begin by sending three values to the other.  Program <code>0</code> sends <code>1, 2, 0</code>; program <code>1</code> sends <code>1, 2, 1</code>. Then, each program receives a value (both <code>1</code>) and stores it in <code>a</code>, receives another value (both <code>2</code>) and stores it in <code>b</code>, and then each receives the program ID of the other program (program <code>0</code> receives <code>1</code>; program <code>1</code> receives <code>0</code>) and stores it in <code>c</code>. Each program now sees a different value in its own copy of register <code>c</code>.</p>
# MAGIC <p>Finally, both programs try to <code>rcv</code> a <em>fourth</em> time, but no data is waiting for either of them, and they reach a <em>deadlock</em>.  When this happens, both programs terminate.</p>
# MAGIC <p>It should be noted that it would be equally valid for the programs to run at different speeds; for example, program <code>0</code> might have sent all three values and then stopped at the first <code>rcv</code> before program <code>1</code> executed even its first instruction.</p>
# MAGIC <p>Once both of your programs have terminated (regardless of what caused them to do so), <em>how many times did program <code>1</code> send a value</em>?</p>
# MAGIC </article>

# COMMAND ----------

run <- function(df, state) {
  instruction <- df$instruction[state$line]
  x <- df$x[state$line]
  y <- df$y[state$line]

  state$waiting_for_signal <- FALSE
  if (instruction == "snd") {
    state$signal_out <- c(state$signal_out, get_value(x, state))
  } else if (instruction == "set") {
    state[[x]] <- get_value(y, state)
  } else if (instruction == "add") {
    state[[x]] <- get_value(x, state) + get_value(y, state)
  } else if (instruction == "mul") {
    state[[x]] <- get_value(x, state) * get_value(y, state)
  } else if (instruction == "mod") {
    state[[x]] <- get_value(x, state) %% get_value(y, state)
  } else if (instruction == "rcv") {
    if (length(state$signal_in) == 0) {
      state$waiting_for_signal <- TRUE
      return(state)
    }
    state[[x]] <- state$signal_in[1]
    state$signal_in <- state$signal_in[-1]
  } else if (instruction == "jgz") {
    if (get_value(x, state) > 0) {
      state$line <- state$line + get_value(y, state) - 1
    }
  }
  state$line <- state$line + 1
  state
}

solve2 <- function(df) {
  state1 <- list(
    p = 0,
    line = 1,
    signal_in = NULL,
    signal_out = NULL,
    waiting_for_signal = FALSE
  )
  state2 <- list(
    p = 1,
    line = 1,
    signal_in = NULL,
    signal_out = NULL,
    waiting_for_signal = FALSE
  )
  state2_sent <- 0
  repeat {
    state1 <- run(df, state1)
    state2$signal_in <- c(state2$signal_in, state1$signal_out)
    state1$signal_out <- NULL
    
    state2 <- run(df, state2)
    state1$signal_in <- c(state1$signal_in, state2$signal_out)
    state2_sent <- state2_sent + length(state2$signal_out)
    state2$signal_out <- NULL
    
    if (state1$waiting_for_signal && length(state1$signal_in) == 0 && state2$waiting_for_signal && length(state2$signal_in) == 0) {
      break
    }
  }
  state2_sent - length(state1$signal_in)
}

# COMMAND ----------

answer <- solve2(df)
answer
