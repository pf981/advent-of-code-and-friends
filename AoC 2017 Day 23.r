# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 23: Coprocessor Conflagration ---</h2><p>You decide to head directly to the CPU and fix the printer from there. As you get close, you find an <em>experimental coprocessor</em> doing so much work that the local programs are afraid it will <a href="https://en.wikipedia.org/wiki/Halt_and_Catch_Fire">halt and catch fire</a>. This would cause serious issues for the rest of the computer, so you head in and see what you can do.</p>
# MAGIC <p>The code it's running seems to be a variant of the kind you saw recently on that <a href="18">tablet</a>. The general functionality seems <em>very similar</em>, but some of the instructions are different:</p>
# MAGIC <ul>
# MAGIC <li><code>set X Y</code> <em>sets</em> register <code>X</code> to the value of <code>Y</code>.</li>
# MAGIC <li><code>sub X Y</code> <em>decreases</em> register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>mul X Y</code> sets register <code>X</code> to the result of <em>multiplying</em> the value contained in register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>jnz X Y</code> <em>jumps</em> with an offset of the value of <code>Y</code>, but only if the value of <code>X</code> is <em>not zero</em>. (An offset of <code>2</code> skips the next instruction, an offset of <code>-1</code> jumps to the previous instruction, and so on.)</li>
# MAGIC <p>Only the instructions listed above are used. The eight registers here, named <code>a</code> through <code>h</code>, all start at <code>0</code>.</p>
# MAGIC </ul>
# MAGIC <p>The coprocessor is currently set to some kind of <em>debug mode</em>, which allows for testing, but prevents it from doing any meaningful work.</p>
# MAGIC <p>If you run the program (your puzzle input), <em>how many times is the <code>mul</code> instruction invoked?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "set b 84
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
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

count_mul <- function(df) {
  sound <- 0
  state <- list()
  i <- 1
  mul_count <- 0
  repeat {
    if (i > nrow(df)) break;
    instruction <- df$instruction[i]
    x <- df$x[i]
    y <- df$y[i]

    if (instruction == "set") {
      state[[x]] <- get_value(y, state)
    } else if (instruction == "sub") {
      state[[x]] <- get_value(x, state) - get_value(y, state)
    } else if (instruction == "mul") {
      state[[x]] <- get_value(x, state) * get_value(y, state)
      mul_count <- mul_count + 1
    } else if (instruction == "jnz") {
      if (get_value(x, state) != 0) {
        i <- i + get_value(y, state) - 1
      }
    }
    i <- i + 1
  }
  mul_count
}

# COMMAND ----------

answer <- count_mul(df)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, it's time to fix the problem.</p>
# MAGIC <p>The <em>debug mode switch</em> is wired directly to register <code>a</code>.  You <span title="From 'magic' to 'more magic'.">flip the switch</span>, which makes <em>register <code>a</code> now start at <code>1</code></em> when the program is executed.</p>
# MAGIC <p>Immediately, the coprocessor begins to overheat.  Whoever wrote this program obviously didn't choose a very efficient implementation.  You'll need to <em>optimize the program</em> if it has any hope of completing before Santa needs that printer working.</p>
# MAGIC <p>The coprocessor's ultimate goal is to determine the final value left in register <code>h</code> once the program completes. Technically, if it had that... it wouldn't even need to run the program.</p>
# MAGIC <p>After setting register <code>a</code> to <code>1</code>, if the program were to run to completion, <em>what value would be left in register <code>h</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

"
a = 1
b = 84                   # set b 84
c = b                    # set c b
if (a != 0) {            # jnz a 2
                         # jnz 1 5
  b = b * 100 + 100000   # mul b 100
                         # sub b -100000
  c = b + 17000          # set c b
                         # sub c -17000
}
repeat {
  f = 1                  # set f 1
  d = 2                  # set d 2
  do {
    e = 2                # set e 2
    do {
      g = d              # set g d
      g *= e             # mul g e
      g -= b             # sub g b
      if (g == 0) {      # jnz g 2
        f = 0            # set f 0
      }
      --e                # sub e -1
      g = e              # set g e
      g -= b             # sub g b
    } while (g != 0)     # jnz g -8
    --d                  # sub d -1
    g = d                # set g d
    g -= b               # sub g b
  } while (g != 0)       # jnz g -13
  if (f != 0) {          # jnz f 2
    ++h                  # sub h -1
  }
  g = b                  # set g b
  g -= c                 # sub g c
  if (g != 0) {          # jnz g 2
    return               # jnz 1 3
  }           
  b += 17                # sub b -17
}                        # jnz 1 -23
"

# COMMAND ----------

b <- 84 * 100 + 100000
h <- 0
.c <- b + 17000
repeat {
  if (!RcppAlgos::isPrimeRcpp(b)) {
    h <- h + 1
  }
  if (b == .c) break
  b <- b + 17
}
answer <- h
answer
