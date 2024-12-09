library(tidyverse)



target <- c(17, 61)

lines = read_lines(input)

start_state <-
  lines %>%
  keep(str_starts, "value") %>%
  str_match("(\\d+).+?(\\d+)") %>%
  as_tibble() %>%
  transmute(
    bot = V3 %>% parse_integer(),
    value = V2 %>% parse_integer()
  )

gives <-
  lines %>%
  discard(str_starts, "value") %>%
  str_replace_all("output ", "10000") %>% # Prefix output with 10000
  str_match("(\\d+).+?(\\d+).+?(\\d+)") %>%
  as_tibble() %>%
  transmute(
    bot = V2 %>% parse_integer(),
    low_bot = V3 %>% parse_integer(),
    high_bot = V4 %>% parse_integer()
  )

lst(start_state, gives)

simulate <- function(state, gives, target = c(17, 61)) {
  two_chip_bots <-
    state %>%
    group_by(bot) %>%
    filter(n() == 2) %>%
    arrange(value)

  active <-
    two_chip_bots %>%
    summarise(
      low_value = min(value),
      high_value = max(value),
      .groups = "drop"
    ) %>%
    inner_join(gives, by = "bot") %>%
    head(1)

  if (nrow(active) == 1) {
    message(glue::glue("bot {active$bot} gives {active$low_value} to bot {active$low_bot}, and {active$high_value} to bot {active$high_bot}"))
    answer <- two_chip_bots %>% filter(all(value == target)) %>% pull(bot) %>% first()
    
    status <- "Pending"
    state <-
      state %>%
      add_row(bot = active$low_bot, value = active$low_value) %>%
      add_row(bot = active$high_bot, value = active$high_value) %>%
      filter(bot != active$bot)
  } else {
    status <- "Done"
    answer <- NA
  }

  lst(state, status, answer)
}

state <- start_state
status <- "Pending"
while (status == "Pending") {
  result <- simulate(state, gives, target)
  state <- result$state
  status <- result$status
  if(!is.na(result$answer)) {
    answer <- result$answer
  }
}

answer

answer <-
  state %>%
  filter(bot %in% c(100000, 100001, 100002)) %>%
  pull(value) %>%
  prod()
answer
