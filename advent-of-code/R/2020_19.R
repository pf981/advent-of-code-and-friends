library(tidyverse)



split_strs <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
split_strs

messages <- split_strs[[2]] %>% enframe(name = "message_id")
messages

rules <-
  split_strs[[1]] %>%
  as_tibble() %>%
  separate(value, c("rule_id", "value"), ": ") %>%
  mutate(
    rule_id = as.integer(rule_id)
  )
rules

char_rules <-
  rules %>%
  filter(str_detect(value, '"')) %>%
  mutate(value = str_replace_all(value, '"', ""))
char_rules

nested_rules <-
  rules %>%
  anti_join(char_rules, by = "rule_id") %>%
  mutate(
    value = str_split(value, fixed(" | ")),
    value = map(value, ~str_split(., fixed(" ")) %>% map(as.integer))
  )
nested_rules

all_rules <- bind_rows(
  char_rules %>% mutate(value = as.list(value)),
  nested_rules
)
all_rules

generate_regex <- function(rule) {
  if (length(rule) > 1) {
    return(rule %>% map_chr(generate_regex) %>% paste0(collapse = ""))
  }
  
  value <- all_rules %>% filter(rule_id == rule) %>% pull(value) %>% first()
  
  if (is.character(value)) {
    return (value)
  }
  glue::glue("(?:{str_c(map_chr(value, generate_regex), collapse = '|')})")
}

result <-
  messages %>%
  mutate(is_match = str_detect(value, paste0("^", generate_regex(0), "$")))
result

answer <- result %>% filter(is_match) %>% nrow()
answer

all_rules$value[all_rules$rule_id == 8] <- list(list(c(42), c(42, 8)))
all_rules$value[all_rules$rule_id == 11] <- list(list(c(42, 31), c(42, 11, 31)))

max_depth <- 20

generate_regex <- function(rule, depth = 1) {
  if (rule == 42) {
    depth <- depth + 1
  }
  if (depth >= max_depth) {
    return("")
  }
  
  if (length(rule) > 1) {
    return(rule %>% map_chr(generate_regex, depth = depth) %>% paste0(collapse = ""))
  }
  
  value <- all_rules %>% filter(rule_id == rule) %>% pull(value) %>% first()
  
  if (is.character(value)) {
    return (value)
  }
  glue::glue("(?:{str_c(map_chr(value, generate_regex, depth = depth), collapse = '|')})")
}

result <-
  messages %>%
  mutate(is_match = str_detect(value, paste0("^", generate_regex(0), "$")))
result

answer <- result %>% filter(is_match) %>% nrow()
answer
