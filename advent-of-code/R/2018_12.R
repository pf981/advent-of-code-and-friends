library(tidyverse)



start_state <- str_extract(input, "[#.]+")
start_state

df <-
  read_lines(input) %>%
  tail(-2) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("from", "to"))
df

plant_regex <-
  df %>%
  filter(to == "#") %>%
  mutate(
    from_regex = str_c(
      "(?<=",
      str_sub(from, 1, 2),
      ")",
      str_sub(from, 3, 3),
      "(?=",
      str_sub(from, 4),
      ")"
    ) %>%
      str_replace_all(fixed("."), "\\.")
  ) %>%
  pull(from_regex) %>%
  str_c(collapse = "|")
plant_regex

simulate1 <- function(s) {
  x <- str_locate_all(s, plant_regex)[[1]][,1]
  s <- rep(".", str_length(s))
  s[x] <- "#"
  str_c(s, collapse = "")
}

simulate <- function(s, n) {
  for (i in seq_len(n)) {
    s <- simulate1(str_c(".....", s, "....."))
  }
  s
}

score <- function(s, n) {
  simulate(start_state, n) %>%
    str_split("") %>%
    first() %>%
    {which(. == "#") - n * 5 - 1} %>%
    sum()
}

answer <- score(start_state, 20)
answer

plot_df <-
  tibble(x = seq_len(500)) %>%
  rowwise() %>%
  mutate(sc = score(start_state, x))

ggplot(plot_df, aes(x, sc)) +
  geom_line() +
  theme_minimal()

plot_df %>%
  ungroup() %>%
  mutate(dsc = sc - lag(sc)) %>%
  tail(n = 20)

answer <- format(11957 + 23 * (50000000000 - 500), scientific = FALSE)
answer
