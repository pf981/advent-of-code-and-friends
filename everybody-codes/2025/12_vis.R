library(tidyverse)


df <-
  read_lines("./input/everybody_codes_e2025_q12_p3.txt") |>
  str_split("") |>
  map(as.integer) |>
  imap(\(row, y) {
    imap(row, \(val, x) tibble(x, y, val)) |>
    list_rbind()
  }) |>
  list_rbind()

p <-
  ggplot(df, aes(x, -y, fill = val)) +
  geom_tile(width = 1) +
  scale_x_continuous(expand = c(0, 0)) +
  scale_y_continuous(expand = c(0, 0)) +
  coord_fixed() +
  theme_void() +
  theme(legend.position = "none")

ggsave(
  "output/2025_12.png",
  p,
  width = max(df$x),
  height = max(df$y),
  units = "px",
  scale = 5
)
