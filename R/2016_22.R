library(tidyverse)



# 

df <-
  read_table(input, skip = 1) %>%
  mutate_all(~str_remove(., "T|%") %>% parse_guess()) %>%
  rename_all(~str_remove(str_to_lower(.), '[^a-z]')) %>%
  mutate(
    x = str_extract(filesystem, "(?<=x)\\d+") %>% parse_integer(),
    y = str_extract(filesystem, "(?<=y)\\d+") %>% parse_integer()
  )
df

answer <- sqldf::sqldf("
SELECT COUNT(DISTINCT a.filesystem || b.filesystem)
FROM
  df a
  LEFT JOIN df b ON
    b.avail >= a.used
    AND b.filesystem != a.filesystem
WHERE
  a.used > 0
") %>%
  pull(1)
answer

df %>%
  mutate(value = str_c(used, " | ", avail)) %>%
  select(x, y, value) %>%
  pivot_wider(names_from = x) %>%
  display()

df %>%
  mutate(
    col = case_when(
      x == min(x) & y == min(y) ~ "blue",
      x == max(x) & y == min(y) ~ "orange",
      avail == 90 ~ "green",
      used > 90 ~ "red",
      TRUE ~ "grey"
    )
  ) %>%
  ggplot(aes(x, y, fill = I(col))) +
  geom_tile(col = "black") +
  scale_x_continuous(
    breaks = seq(from = min(df$x), to = max(df$x), by = 1),
    expand = c(0, 0)
  ) +
  scale_y_reverse(
    breaks = seq(from = min(df$y), to = max(df$y), by = 1),
    expand = c(0, 0)
  ) +
  theme_void() +
  theme(axis.text = element_text(size = rel(0.7)))

# Clearly this is just a sliding puzzle with a wall.
answer <- 16 + 12 + 22 + 31 * 5
answer
