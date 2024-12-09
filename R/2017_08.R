library(tidyverse)



df <-
  tibble(line = read_lines(input) %>% str_to_upper()) %>%
  mutate(
    register = str_extract(line, "^\\w+"),
    operation = str_extract(line, "(?<=^\\w{1,100} )\\w+"),
    by = str_extract(line, "-?\\d+"),
    cond = str_extract(line, "(?<=IF ).+"),
    expr = glue::glue("if ({cond}) {register} <- {register} + {ifelse(operation == 'INC', 1, -1)} * {by}")
  )
df

registers <- unique(df$register)
walk(registers, assign, 0, envir = .GlobalEnv)

for (i in seq_len(nrow(df))) {
  eval(rlang::parse_expr(df$expr[i]))
}

answer <- map_dbl(registers, get) %>% max()
answer

answer <- 0
walk(registers, assign, 0, envir = .GlobalEnv)
for (i in seq_len(nrow(df))) {
  eval(rlang::parse_expr(df$expr[i]))
  answer <- map_dbl(registers, get) %>% c(answer) %>% max()
}
answer
