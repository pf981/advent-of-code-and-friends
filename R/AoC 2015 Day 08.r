library(tidyverse)

# I escaped all the backslashes


df <-
  tibble(text = read_lines(input)) %>%
  mutate(
    string_code_characters = str_length(text),
    string_memory_characters =
      text %>%
      str_sub(2, -2) %>%
      str_count('\\\\\\\\|\\\\"|\\\\x..|.')
  )
df

answer <- sum(df$string_code_characters) - sum(df$string_memory_characters)
answer

answer <-
  df %>%
  mutate(
    encoded_characters = str_length(text) + str_count(text, fixed('"')) + str_count(text, fixed('\\')) + 2
  ) %>%
  summarise(answer = sum(encoded_characters) - sum(string_code_characters)) %>%
  pull(answer)
answer
