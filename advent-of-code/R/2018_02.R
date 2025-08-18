library(tidyverse)



l <- read_lines(input)

answer <-
  l %>%
  str_split("") %>%
  imap_dfr(~tibble(letter = ., word = .y)) %>%
  count(word, letter) %>%
  group_by(word, n) %>%
  slice(1) %>%
  ungroup() %>%
  summarise(sum(n == 2) * sum(n == 3)) %>%
  pull(1)
answer

common_letters <- function(a, b) {
  a_split <- str_split(a, "") %>% first()
  b_split <- str_split(b, "") %>% first()
  
  a_split[a_split == b_split] %>% str_c(collapse = "")
}

df <-
  crossing(a = l, b = l) %>%
  filter(a != b) %>%
  mutate(
    common = map2_chr(a, b, common_letters),
    common_length = str_length(common)
  ) %>%
  arrange(desc(common_length))
df

answer <- df %>% slice(1) %>% pull(common)
answer
