# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/19

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- '0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'

# COMMAND ----------

input %>% str_split("\n\n") %>% unlist() %>% keep(2)

# COMMAND ----------

split_strs <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
split_strs

# COMMAND ----------

rules <-
  split_strs[[1]] %>%
  as_tibble() %>%
  separate(value, c("rule_id", "value"), ": ") %>%
  mutate(
    rule_id = as.integer(rule_id)
  )
rules

# COMMAND ----------

char_rules <-
  rules %>%
  filter(str_detect(value, '"')) %>%
  mutate(value = str_replace_all(value, '"', ""))
char_rules

# COMMAND ----------

nested_rules <-
  rules %>%
  anti_join(char_rules, by = "rule_id") %>%
  mutate(
    value = str_split(value, fixed(" | "))
  ) %>%
  unnest(value) %>%
  mutate(value = str_split(value, " "))
nested_rules

# COMMAND ----------

messages <- split_strs[[2]] %>% enframe(name = "message_id")
messages

# COMMAND ----------

check_match <- function(message_str, check_rule_id) {
  if (check_rule_id %in% char_rules$rule_id) {
    match_char <- char_rules %>% filter(rule_id == check_rule_id) %>% pull(value)
    return(list(
      is_match = str_detect(message_str, match_char),
      message_str = str_replace(message_str, match_char, "")
    ))
  }
  
  nested_rules_df <- nested_rules %>% filter(rule_id %in% check_rule_id)
  
  if (nrow(nested_rules_df) == 0) {
    stop(paste0("Unknown rule id: ", check_rule_id))
  }
  
  for (rule_group in seq_len(nrow(nested_rules_df))) {
    cur_message_str <- message_str
    is_done <- TRUE
    
    for (individual_rule in unlist((slice(nested_rules_df, rule_group)$value))) {
      result <- check_match(cur_message_str, individual_rule)
      
      if (result$is_match) {
        cur_message_str <- result$message_str
      } else {
        is_done <- FALSE
        break
      }
    }
    if (nchar(cur_message_str) == 0 && is_done) {
      return(list(
        is_match = TRUE,
        message_str = cur_message_str
      ))
    }
  }
  
  list(
    is_match = FALSE,
    message_str = NA
  )
}

# COMMAND ----------

check_match(messages[[1]], 0)