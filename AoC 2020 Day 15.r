# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/15

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "20,9,11,0,1,2"

# COMMAND ----------

# input <- "0,3,6"

# COMMAND ----------

nums <- input %>% str_split(",") %>% unlist() %>% parse_integer()
nums

# COMMAND ----------

simulate <- function(n, init) {
  turns <- tibble(turn = seq_len(n), value = NA)
  turns$value[seq_along(init)] <- init
  
  for (i in turns$turn) {
    if(i %in% seq_along(init)) {
      turns$value[i] <- init[i]
    } else {
      turns$value[i] <- i - 1 - max(which(turns$value[seq_len(i - 2)] == last_turn))
      if (!is.finite(turns$value[i])) {
        turns$value[i] <- 0
      }
    }
    
    last_turn <- turns$value[i]
  }
  turns
}

# COMMAND ----------

result <- simulate(2020, nums)
result$value %>% last()