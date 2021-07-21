# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 21: Scrambled Letters and Hash ---</h2><p>The computer system you're breaking into uses a <span title="I do not like them, Security-Account-Manager-I-Am! I do not like scrambled letters and hash!">weird scrambling function</span> to store its passwords. It shouldn't be much trouble to create your own scrambled password so you can add it to the system; you just have to implement the scrambler.</p>
# MAGIC <p>The scrambling function is a series of operations (the exact list is provided in your puzzle input). Starting with the password to be scrambled, apply each operation in succession to the string. The individual operations behave as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>swap position X with position Y</code> means that the letters at indexes <code>X</code> and <code>Y</code> (counting from <code>0</code>) should be <em>swapped</em>.</li>
# MAGIC <li><code>swap letter X with letter Y</code> means that the letters <code>X</code> and <code>Y</code> should be <em>swapped</em> (regardless of where they appear in the string).</li>
# MAGIC <li><code>rotate left/right X steps</code> means that the whole string should be <em>rotated</em>; for example, one right rotation would turn <code>abcd</code> into <code>dabc</code>.</li>
# MAGIC <li><code>rotate based on position of letter X</code> means that the whole string should be <em>rotated to the right</em> based on the <em>index</em> of letter <code>X</code> (counting from <code>0</code>) as determined <em>before</em> this instruction does any rotations.  Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least <code>4</code>.</li>
# MAGIC <li><code>reverse positions X through Y</code> means that the span of letters at indexes <code>X</code> through <code>Y</code> (including the letters at <code>X</code> and <code>Y</code>) should be <em>reversed in order</em>.</li>
# MAGIC <li><code>move position X to position Y</code> means that the letter which is at index <code>X</code> should be <em>removed</em> from the string, then <em>inserted</em> such that it ends up at index <code>Y</code>.</li>
# MAGIC </ul>
# MAGIC <p>For example, suppose you start with <code>abcde</code> and perform the following operations:</p>
# MAGIC <ul>
# MAGIC <li><code>swap position 4 with position 0</code> swaps the first and last letters, producing the input for the next step, <code>ebcda</code>.</li>
# MAGIC <li><code>swap letter d with letter b</code> swaps the positions of <code>d</code> and <code>b</code>: <code>edcba</code>.</li>
# MAGIC <li><code>reverse positions 0 through 4</code> causes the entire string to be reversed, producing <code>abcde</code>.</li>
# MAGIC <li><code>rotate left 1 step</code> shifts all letters left one position, causing the first letter to wrap to the end of the string: <code>bcdea</code>.</li>
# MAGIC <li><code>move position 1 to position 4</code> removes the letter at position <code>1</code> (<code>c</code>), then inserts it at position <code>4</code> (the end of the string): <code>bdeac</code>.</li>
# MAGIC <li><code>move position 3 to position 0</code> removes the letter at position <code>3</code> (<code>a</code>), then inserts it at position <code>0</code> (the front of the string): <code>abdec</code>.</li>
# MAGIC <li><code>rotate based on position of letter b</code> finds the index of letter <code>b</code> (<code>1</code>), then rotates the string right once plus a number of times equal to that index (<code>2</code>): <code>ecabd</code>.</li>
# MAGIC <li><code>rotate based on position of letter d</code> finds the index of letter <code>d</code> (<code>4</code>), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least <code>4</code>, for a total of <code>6</code> right rotations: <code>decab</code>.</li>
# MAGIC </ul>
# MAGIC <p>After these steps, the resulting scrambled password is <code>decab</code>.</p>
# MAGIC <p>Now, you just need to generate a new scrambled password and you can access the system. Given the list of scrambling operations in your puzzle input, <em>what is the result of scrambling <code>abcdefgh</code></em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "rotate right 4 steps
swap letter b with letter e
swap position 1 with position 3
reverse positions 0 through 4
rotate left 5 steps
swap position 6 with position 5
move position 3 to position 2
move position 6 to position 5
reverse positions 1 through 4
rotate based on position of letter e
reverse positions 3 through 7
reverse positions 4 through 7
rotate left 1 step
reverse positions 2 through 6
swap position 7 with position 5
swap letter e with letter c
swap letter f with letter d
swap letter a with letter e
swap position 2 with position 7
swap position 1 with position 7
swap position 6 with position 3
swap letter g with letter h
reverse positions 2 through 5
rotate based on position of letter f
rotate left 1 step
rotate right 2 steps
reverse positions 2 through 7
reverse positions 5 through 6
rotate left 6 steps
move position 2 to position 6
rotate based on position of letter a
rotate based on position of letter a
swap letter f with letter a
rotate right 5 steps
reverse positions 0 through 4
swap letter d with letter c
swap position 4 with position 7
swap letter f with letter h
swap letter h with letter a
rotate left 0 steps
rotate based on position of letter e
swap position 5 with position 4
swap letter e with letter h
swap letter h with letter d
rotate right 2 steps
rotate right 3 steps
swap position 1 with position 7
swap letter b with letter e
swap letter b with letter e
rotate based on position of letter e
rotate based on position of letter h
swap letter a with letter h
move position 7 to position 2
rotate left 2 steps
move position 3 to position 2
swap position 4 with position 6
rotate right 7 steps
reverse positions 1 through 4
move position 7 to position 0
move position 2 to position 0
reverse positions 4 through 6
rotate left 3 steps
rotate left 7 steps
move position 2 to position 3
rotate left 6 steps
swap letter a with letter h
rotate based on position of letter f
swap letter f with letter c
swap position 3 with position 0
reverse positions 1 through 3
swap letter h with letter a
swap letter b with letter a
reverse positions 2 through 3
rotate left 5 steps
swap position 7 with position 5
rotate based on position of letter g
rotate based on position of letter h
rotate right 6 steps
swap letter a with letter e
swap letter b with letter g
move position 4 to position 6
move position 6 to position 5
rotate based on position of letter e
reverse positions 2 through 6
swap letter c with letter f
swap letter h with letter g
move position 7 to position 2
reverse positions 1 through 7
reverse positions 1 through 2
rotate right 0 steps
move position 5 to position 6
swap letter f with letter a
move position 3 to position 1
move position 2 to position 4
reverse positions 1 through 2
swap letter g with letter c
rotate based on position of letter f
rotate left 7 steps
rotate based on position of letter e
swap position 6 with position 1
"

# COMMAND ----------

# input <- "swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d
# "

# COMMAND ----------

swap_position <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  x_value <- str_sub(s, x, x)
  str_sub(s, x, x) <- str_sub(s, y, y)
  str_sub(s, y, y) <- x_value
  s
}

swap_letter <- function(s, x, y) {
  s <- str_replace_all(s, x, "X")
  s <- str_replace_all(s, y, x)
  s <- str_replace_all(s, "X", y)
  s
}

rotate_dir <- function(s, x, y) {
  direction <- x
  x <- y
  
  x <- as.integer(x)
  if (direction == "right") {
    x <- str_length(s) - x
  }
  
  str_c(
    str_sub(s, x + 1),
    str_sub(s, 1, x)
  )
}

rotate_pos <- function(s, x, y) {
  d <- str_locate(s, x) %>% first()
  d <- d - 1
  
  if (d >= 4) {
    d <- d + 1
  }
  d <- d + 1
  if (d > str_length(s)) {
    d <- d - str_length(s)
  }
  rotate_dir(s, "right", d)
}

reverse <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  str_sub(s, x, y) <- stringi::stri_reverse(str_sub(s, x, y))
  s
}

move <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  letter <- str_sub(s, x, x)
  str_sub(s, x, x) <- ""
  str_sub(s, y, y) <- str_c(letter, str_sub(s, y, y))
  s
}

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    instruction = str_extract(line, "^\\w+"),
    instruction = case_when(
        str_detect(line, "swap position") ~ "swap_position",
        str_detect(line, "swap letter") ~ "swap_letter",
        str_detect(line, "rotate based") ~ "rotate_pos",
        instruction == "rotate" ~ "rotate_dir",
        TRUE ~ instruction
    ),
    params = str_extract_all(line, "left|right|(?<=[^\\w])\\w(?=[^\\w]|$)"),
    f = map(instruction, get)
  ) %>%
  unnest_wider(params) %>%
  rename(x = `...1`, y = `...2`)
df

# COMMAND ----------

answer <- "abcdefgh"

for (i in seq_len(nrow(df))) {
  answer <- with(df[i,], f[[1]](answer, x, y))
}
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You scrambled the password correctly, but you discover that you <a href="https://en.wikipedia.org/wiki/File_system_permissions">can't actually modify</a> the <a href="https://en.wikipedia.org/wiki/Passwd">password file</a> on the system. You'll need to un-scramble one of the existing passwords by reversing the scrambling process.</p>
# MAGIC <p>What is the un-scrambled version of the scrambled password <code>fbgdceah</code>?</p>
# MAGIC </article>

# COMMAND ----------

reverse_f <- function(s, f_str, x, y) {
  f <- get(f_str)
  if (f_str %in% c("swap_position", "swap_letter", "reverse")){
    return(f(s, x, y))
  }
  if (f_str == "rotate_dir") {
    rotate_dir(s, ifelse(x == "right", "left", "right"), y)
  }
  
  candidate <- s
  repeat {
    if (f(candidate, x, y) == s) return(candidate)
    candidate <- stringi::stri_rand_shuffle(candidate)
  }
}

# COMMAND ----------

answer <- "fbgdceah"

for (i in rev(seq_len(nrow(df)))) {
  f <- df$instruction[i]
  x <- df$x[i]
  y <- df$y[i]
  
  answer <- reverse_f(answer, f, x, y)
}
answer
