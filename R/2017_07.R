library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    program = str_extract(line, "^\\w+"),
    weight = str_extract(line, "\\d+") %>% parse_integer(),
    holding = str_extract(line, "(?<=-> ).+") %>% str_split(", ")
  ) %>%
  unnest()

df

root <- df %>% filter(!(program %in% holding)) %>% pull(program) %>% first()
answer <- root
answer

get_total_weight <- function(program_name, df) {
  if (is.na(program_name)) {
    return(0)
  }
  
  sub_program_weight <-
    df %>%
    filter(program == program_name) %>%
    pull(holding) %>%
    map_dbl(get_total_weight, df) %>%
    sum()
  
  program_weight <-
    df %>%
    filter(program == program_name) %>%
    pull(weight) %>%
    first()
  
  program_weight + sub_program_weight
}

is_balanced <- function(df) {
  unbalanced <-
    df %>%
    mutate(
      total_weight = map_dbl(holding, get_total_weight, df)
    ) %>%
    group_by(program) %>%
    mutate(new_total_weight = ifelse(total_weight == first(total_weight), last(total_weight), first(total_weight))) %>%
    filter(new_total_weight != total_weight)
  
  nrow(unbalanced) == 0
}

solve <- function(df) {
  candidates <-
    df %>%
    mutate(
      total_weight = map_dbl(holding, get_total_weight, df)
    ) %>%
    group_by(program) %>%
    mutate(new_total_weight = ifelse(total_weight == first(total_weight), last(total_weight), first(total_weight))) %>%
    filter(new_total_weight != total_weight)

  for (i in seq_len(nrow(candidates))) {
    new_df <- df
    new_weight <- new_df$weight[new_df$program == candidates$holding[i]] - (candidates$total_weight[i] - candidates$new_total_weight[i])
    new_df$weight[new_df$program == candidates$holding[i]] <- new_weight
    if (is_balanced(new_df)) {
      return(new_weight[1])
    }
  }
}

answer <- solve(df)
answer
