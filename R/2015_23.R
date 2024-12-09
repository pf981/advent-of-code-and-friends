library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  transmute(
    line_number = row_number(),
    instruction = str_extract(line, "^[a-z]+"),
    r = str_extract(line, "(?<= )[a-z]+"),
    offset = str_extract(line, "[+-]\\d+") %>% parse_integer()
  )

df

hlf <- function(state, r, offset) {
  state[[r]] <- as.integer(state[[r]] / 2)
  state$line <- state$line + 1
  state
}

tpl <- function(state, r, offset) {
  state[[r]] <- state[[r]] * 3
  state$line <- state$line + 1
  state
}

inc <- function(state, r, offset) {
  state[[r]] <- state[[r]] + 1
  state$line <- state$line + 1
  state
}

jmp <- function(state, r, offset) {
  state$line <- state$line + offset
  state
}

jie <- function(state, r, offset) {
  if (state[[r]] %% 2 == 0) {
    state$line <- state$line + offset
  } else {
    state$line <- state$line + 1
  }
  state
}

jio <- function(state, r, offset) {
  if (state[[r]] == 1) {
    state$line <- state$line + offset
  } else {
    state$line <- state$line + 1
  }
  state
}

state <- list(line = 1, a = 0, b = 0)

while (state$line <= nrow(df)) {
  inst <- df %>% slice(state$line)
  
  f <- get(inst$instruction)
  state <- f(state, inst$r, inst$offset)
}

answer <- state$b
answer

state <- list(line = 1, a = 1, b = 0)

while (state$line <= nrow(df)) {
  inst <- df %>% slice(state$line)
  
  f <- get(inst$instruction)
  state <- f(state, inst$r, inst$offset)
}

answer <- state$b
answer
