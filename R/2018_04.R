library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    time = str_extract(line, "(?<=\\[).+(?=\\])")  %>% lubridate::ymd_hm(),
    event = str_replace(line, ".+] ", ""),
    guard = str_extract(event, "\\d+") %>% parse_integer()
  ) %>%
  arrange(time) %>%
  fill(guard) %>%
  mutate(
    shift =  coalesce(guard != lag(guard), TRUE) %>% cumsum(),
    sleep_id = cumsum(event == "falls asleep")
  ) %>%
  filter(event %in% c("falls asleep", "wakes up")) %>%
  group_by(guard, shift, sleep_id) %>%
  summarise(
    start_sleep = min(time),
    end_sleep = max(time)
  ) %>%
  ungroup()
df

all_time <-
  df %>%
  rowwise() %>%
  mutate(
    minute = list(seq(from = start_sleep, to = end_sleep - lubridate::minutes(1), by = "min"))
  ) %>%
  unnest() %>%
  mutate(minute = 60 * lubridate::hour(minute) + lubridate::minute(minute))
all_time

most_asleep_guard <-
  all_time %>%
  count(guard) %>%
  arrange(desc(n)) %>%
  head(1) %>%
  pull(guard)
most_asleep_guard

most_asleep_minute <-
  all_time %>%
  filter(guard == most_asleep_guard) %>%
  count(minute) %>%
  arrange(desc(n)) %>%
  head(1) %>%
  pull(minute)
most_asleep_minute

answer <- most_asleep_guard * most_asleep_minute
answer

answer <-
  all_time %>%
  count(guard, minute) %>%
  arrange(desc(n)) %>%
  head(1) %>%
  transmute(guard * minute) %>%
  pull(1)
answer
