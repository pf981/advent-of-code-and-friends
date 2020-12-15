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

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# Use environments as a hashmap
# FIXME: use next
# 
# Using `<-` with environment will give shallow copy
`[[.hashmap` <- function(x, i) {
  class(x) <- class(x)[class(x) != "hashmap"]
  result <- x[[as.character(i)]]
  class(x) <- c("hashmap", class(x))
  result
}

`[[<-.hashmap` <- function(x, i, value) {
  class(x) <- class(x)[class(x) != "hashmap"]
  x[[as.character(i)]] <- value
  class(x) <- c("hashmap", class(x))
  invisible(x)
}
  
hashmap <- function(init) {
  h <- new.env(hash = TRUE)
  class(h) <- c("hashmap", class(h))
  
  for (i in seq_along(init)) {
    h[[init[i]]] <- i
  }
  
  h
}

# COMMAND ----------

simulate <- function(n, init) {
  last_seen <- hashmap(init)
  last_seen2 <- hashmap(head(init, -1))

  last_value <- last(init)
  #result <- init#
  
  for (i in seq(from = length(init) + 1, n)) {
    new_value <- c(i - 1 - last_seen2[[last_value]], 0L)[1]
    last_seen2[[last_value]] <- i - 1
    last_seen[[new_value]] <- i
    
    last_value <- new_value
    #result <- c(result, last_value)#
  }
  #last_turn
  #result#
  last_value
}

# COMMAND ----------

simulate(10, c(0,3,6))

# COMMAND ----------

simulate(30000000, c(0,3,6))

# COMMAND ----------

result <- simulate(30000000, c(20,9,11,0,1,2))
result
#> 48568

# COMMAND ----------

simulate(2020, nums)

# COMMAND ----------

result <- simulate(30000000, nums)
result

# COMMAND ----------

simulate <- function(n, init) {
  last_seen <- hashmap(init)
  last_seen2 <- hashmap(head(init, -1))

  last_value <- last(init)
  
  for (i in seq(from = length(init) + 1, n)) {
    new_value <- c(i - 1 - last_seen2[[as.character(last_value)]], 0L)[1]
    last_seen2[[as.character(last_value)]] <- i - 1
    last_seen[[as.character(new_value)]] <- i
    
    last_value <- new_value
  }
  last_value
}

# COMMAND ----------

simulate <- function(n, init) {
  last_seen <- new.env(init)
  for (i in seq_along(init)) {
    last_seen[[as.character(init[i]])] <- i
  }
  
  for (i in seq(from = length(init) + 1, n)) {
    v <- i - last_seen[[as.character(v)]]
    last_seen[[as.character(v)]] <- i
  }
  v
}

# COMMAND ----------

map_int(1:10, simulate, c(0,3,6))