library(tidyverse)



passport_fields <-
  input %>%
  str_split("\n\n") %>%
  unlist() %>%
  str_replace_all("\n", " ") %>%
  str_split(" ") %>%
  imap_dfr(~tibble(i = .y, value = .x) %>% separate(value, c("key", "value"), ":"))
passport_fields

answer <-
  passport_fields %>%
  filter(key != "cid") %>%
  count(i) %>%
  filter(n == 7) %>%
  nrow()
answer

answer <-
  passport_fields %>%
  filter(key != "cid") %>%
  mutate(num = suppressWarnings(parse_number(value))) %>%
  filter(
    coalesce(!(key == "byr" & !(value >= 1920 & value <= 2002)), TRUE),
    coalesce(!(key == "iyr" & !(value >= 2010 & value <= 2020)), TRUE),
    coalesce(!(key == "eyr" & !(value >= 2020 & value <= 2030)), TRUE),
    coalesce(!(key == "hgt" & !( (str_detect(value, "^\\d+cm$") & num >= 150 & num <= 193) | (str_detect(value, "^\\d+in$") & num >= 59 & num <= 76) )), TRUE),
    coalesce(!(key == "hcl" & !( str_detect(value, "^#[0-9a-f]{6}$") )), TRUE),
    coalesce(!(key == "ecl" & !(value %in% c("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))), TRUE),
    coalesce(!(key == "pid" & !(str_detect(value, "^\\d{9}$"))), TRUE)
  ) %>%
  count(i) %>%
  filter(n == 7) %>%
  nrow()
answer
