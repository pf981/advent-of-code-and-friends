# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/23

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- 326519478

# COMMAND ----------

# input <- 389125467

# COMMAND ----------

cups <- input %>% str_split("") %>% unlist() %>% as.integer()
cups

# COMMAND ----------

rotate <- function(x, n = 1) {
  if (n == 0) x else c(tail(x, -n), head(x, n))
}

# COMMAND ----------

simulate_moves <- function(cups, n_moves = 1, debug = FALSE) {
  cur_i <- 1
  for (move in seq_len(n_moves)) {
    current_cup <- cups[cur_i]
    picked_up <- cups[((cur_i + seq_len(3) - 1) %% length(cups)) + 1]

    candidates <- cups[!(cups %in% picked_up)]
    destination <- max(candidates[candidates < current_cup])
    if (!is.finite(destination)) {
      destination <- max(candidates)
    }
    destination_i <- which(candidates == destination)

    if (debug) {
      message(glue::glue('-- move {move} --
cups: {paste0(cups, ifelse(seq_along(cups) == cur_i, "*", ""), collapse = " ")}
pick up: {paste0(picked_up, collapse = " ")}
destination: {destination} (i: {destination_i})

'))
    }
    
    cups <- append(candidates, picked_up, after = destination_i)
    
    # Need which(cups == current_cup) == cur_i
    #cups <- rotate(cups, which(cups == current_cup) - cur_i)

    #cur_i <- (cur_i %% length(cups)) + 1
    cur_i <- (which(cups == current_cup) %% length(cups)) + 1
  }
  
  cups
}

# COMMAND ----------

result <- simulate_moves(cups, 100)

rotate(result, which(result == 1) - 1) %>%
  tail(-1) %>%
  paste0(collapse = "")

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

result <- simulate_moves(
  c(cups, seq(from = max(cups), to = 1000000, by = 1)),
  10000000
)

# first_two <-
#   rotate(result, which(result == 1) - 1) %>%
#   tail(-1) %>%
#   head(2)

# first_two[1] * first_two[2]

# COMMAND ----------

result

# COMMAND ----------

first_two <-
  rotate(result, which(result == 1) - 1) %>%
  tail(-1) %>%
  head(2)

first_two[1] * first_two[2]