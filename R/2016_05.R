library(tidyverse)



answer <-
  str_c(input, seq(from = 0, to = 12000000)) %>%
  openssl::md5() %>%
  keep(str_starts, "00000") %>%
  str_sub(6, 6) %>%
  head(8) %>%
  str_c(collapse = "")  # 13 minutes

answer

hashes <-
  str_c(input, seq(from = 0, to = 30000000)) %>%
  openssl::md5() %>%
  keep(str_starts, "00000") # 20 mins

hashes

answer <-
  hashes %>%
  enframe() %>%
  mutate(
    pos = str_sub(value, 6, 6)
  ) %>%
  group_by(pos) %>%
  summarise(
    letter = first(str_sub(value, 7, 7))
  ) %>%
  arrange(pos) %>%
  pull(letter) %>%
  head(8) %>%
  str_c(collapse = "")

answer
