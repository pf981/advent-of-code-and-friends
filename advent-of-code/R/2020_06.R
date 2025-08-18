library(tidyverse)



answers <-
  input %>%
  str_split("\n\n") %>%
  map(str_split, "\n") %>%
  first() %>%
  enframe(name = "group", value = "answer") %>%
  unnest(answer)

answer <-
  answers %>%
  group_by(group) %>%
  summarise(
    yes_questions = answer %>%
      str_split("") %>%
      unlist() %>%
      unique() %>%
      length()
  ) %>%
  pull(yes_questions) %>%
  sum()
answer

answer <-
  answers %>%
  group_by(group) %>%
  summarise(
    yes_questions = list(
      answer %>%
        str_split("") %>%
        reduce(intersect)
    )
  ) %>%
  unnest(yes_questions) %>%
  count(group) %>%
  pull(n) %>%
  sum()
answer
