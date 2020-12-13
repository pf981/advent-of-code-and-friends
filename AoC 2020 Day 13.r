# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/13

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "1000303
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19
"

# COMMAND ----------

# input <- "939
# 7,13,x,x,59,x,31,19
# "

# COMMAND ----------

lines <- input %>% read_lines()
earliest_departure <- lines[[1]] %>% parse_integer()
bus_ids <-
  lines[[2]] %>%
  str_split(",") %>%
  unlist() %>%
  parse_integer(na = "x") %>%
  discard(is.na)

lst(earliest_departure, bus_ids)

# COMMAND ----------

tibble(
  id = bus_ids,
  soonest = id - (earliest_departure %% id)
) %>%
  filter(soonest == min(soonest)) %>%
  with(id * soonest)