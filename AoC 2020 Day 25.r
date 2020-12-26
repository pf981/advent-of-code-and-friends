# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/25

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "12578151
5051300"

# COMMAND ----------

# input <- "5764801
# 17807724"

# COMMAND ----------

public_keys <- read_lines(input)
public_keys

# COMMAND ----------

encrypt <- function(subject_number, loop_size) {
  value <- 1
  for (i in seq_len(loop_size)) {
    value <- (value * subject_number) %% 20201227
  }
  value
}

# COMMAND ----------

compute_loop_size <- function(public_key) {
  value <- 1
  loop_size <- 0
  repeat {
    loop_size <- loop_size + 1
    value <- (value * 7) %% 20201227
    if (value == public_key) {
      break
    }
  }
  loop_size
}

# COMMAND ----------

loop_sizes <- c(
  compute_loop_size(public_keys[1]),
  compute_loop_size(public_keys[2])
)
loop_sizes

# COMMAND ----------

encryption_key <- encrypt(
  encrypt(subject_numbers[1], loop_sizes[1]),
  loop_sizes[2]
)
encryption_key

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

subject_numbers <- c(7, 7)
loop_sizes <- c(8, 11)

# COMMAND ----------

compute_loop_size(5764801)
compute_loop_size(17807724)

# COMMAND ----------

lst(
  encrypt(subject_numbers[1], loop_sizes[1]),
  encrypt(subject_numbers[2], loop_sizes[2])
)

# COMMAND ----------

# MAGIC %md `encrypt(subject_number, loop_size) = subject_number^loop_size %% 20201227`

# COMMAND ----------

# MAGIC %md Fermat's Little Theorem, maybe? 20201227 is prime
# MAGIC 
# MAGIC `a^p = a %% p`

# COMMAND ----------

(subject_numbers[1] ^ loop_sizes[1]) %% 20201227

# COMMAND ----------

# Subject number is always 7?

# COMMAND ----------

key <- (s1 ^ (l1 * l2)) %% 20201227

# COMMAND ----------

unknown s1, s2, l1, l2

5764801 = s1^l1 %% 20201227
17807724 = s2^l2 %% 20201227

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

1
for loop size
  v = v * subject_number
  v = v %% 20201227

# COMMAND ----------

subject_number <- 17807724 # Public key
loop_size 8 => encryption key = 14897079

# COMMAND ----------

5764801 =8> 14897079 

# COMMAND ----------

subject_number (public_key). No public key is the RESULT
loop_size
encryption_key (public_key)

# COMMAND ----------

loop_size_card
loop_size_door

subject_number
public_key_card
public_key_door

x encryption_key_card - no, there is only one as they are the say
x encryption_key_door

encryption_key

# COMMAND ----------

vlaye 

# COMMAND ----------

subject_number <- 7