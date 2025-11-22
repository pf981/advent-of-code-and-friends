library(tidyverse)

text <- "L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"

turns <-
  text |>
  str_split_1(",") |>
  str_sub(1, 1)

steps <-
  text |>
  str_split_1(",") |>
  str_sub(2) |>
  as.integer()

# Double steps to make vis clearer
steps <- steps * 2

deltas <- list(
  c(0, 1), # north
  c(1, 0), # east
  c(0, -1), # south
  c(-1, 0) # west
)
deltas_i <- 1

walls <- tibble(x = 0, y = 0)
x <- 0
y <- 0
x_breaks_major <- c(0)
x_breaks_minor <- c(-1, 1)
y_breaks_major <- c(0)
y_breaks_minor <- c(-1, 1)
for (i in seq_along(turns)) {
  turn <- if (turns[i] == "L") -1 else +1
  deltas_i <- (deltas_i - 1 + turn) %% 4 + 1

  for (d in seq_len(steps[i])) {
    x <- x + deltas[[deltas_i]][1]
    y <- y + deltas[[deltas_i]][2]
    walls <- walls |> add_row(x, y)
  }

  x_breaks_major <- c(x_breaks_major, x)
  y_breaks_major <- c(y_breaks_major, y)
  x_breaks_minor <- c(x_breaks_minor, x - 1, x + 1)
  y_breaks_minor <- c(y_breaks_minor, y - 1, y + 1)
}

x_breaks_major <- sort(unique(x_breaks_major))
x_breaks_minor <- sort(unique(x_breaks_minor))
y_breaks_major <- sort(unique(y_breaks_major))
y_breaks_minor <- sort(unique(y_breaks_minor))

solution <- tribble(
  ~x, ~y,
  0, 0,
  0, 1,
  -5, 1,
  -6, 1,
  -7, 1,
  -11, 1,
  -12, 1,
  -13, 1,
  -13, 0,
  -13, -1,
  -13, -5,
  -13, -6,
  -13, -7,
  -13, -11,
  -13, -12,
  -12, -12
)

p <-
  ggplot(walls, aes(x, y)) +
  geom_tile(width = 0.8, height = 0.8, color = "black") +
  geom_point(
    data = walls[1, ],
    shape = 21, fill = "#1abc9c", color = "black",
    size = 5, stroke = 0.8
  ) +
  geom_text(
    data = walls[1, ],
    label = "S",
    fontface = "bold",
    size = 3
  ) +
  geom_point(
    data = walls[nrow(walls), ],
    shape = 21, fill = "#3498db", color = "black",
    size = 5, stroke = 0.8
  ) +
  geom_text(
    data = walls[nrow(walls), ],
    label = "E",
    fontface = "bold",
    size = 3
  ) +
  geom_point(
    data = solution,
    shape = 22,
    color = "red",
    fill = NA,
    size = 4,
    stroke = 1,
    alpha = 0.7
  ) +
  scale_x_continuous(
    breaks = x_breaks_major,
    minor_breaks = x_breaks_minor,
    limits = c(-25 - 7, 25 - 7)
  ) +
  scale_y_continuous(
    breaks = y_breaks_major,
    minor_breaks = y_breaks_minor,
    limits = c(-25, 25)
  ) +
  coord_fixed() +
  theme_minimal() +
  theme(
    panel.background = element_rect(fill = "white", colour = NA),
    axis.title = element_blank(),
    axis.text = element_blank(),
    panel.grid.major = element_line(colour = scales::col_mix("black", "white", 0.72)),
    panel.grid.minor = element_line(colour = scales::col_mix("black", "white", 0.88), linewidth = rel(0.8))
  )

ggsave(
  "output/2025_15.png",
  p,
  width = 1000,
  height = 1000,
  units = "px",
  dpi = 140
)
