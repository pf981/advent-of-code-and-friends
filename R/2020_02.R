library(tidyverse)



passwords <- 
  input %>%
  read_lines() %>%
  as_tibble() %>%
  separate(value, into = c("spec", "password"), sep = ": ") %>%
  separate(spec, into = c("times", "letter"), sep = " ") %>%
  separate(times, into = c("min_times", "max_times"), sep = "-", convert = TRUE) %>%
  mutate(times = str_count(password, letter))

passwords

answer <-
  passwords %>%
  filter(times >= min_times, times <= max_times) %>%
  nrow()
answer

answer <-
  passwords %>%
  mutate(
    str2 = pmap_chr(list(password, min_times, max_times), str_sub),
    match_count = (str_sub(str2, -1, -1) == letter) + (str_sub(str2, 1, 1) == letter)
  ) %>%
  filter(match_count == 1) %>%
  nrow()
answer
