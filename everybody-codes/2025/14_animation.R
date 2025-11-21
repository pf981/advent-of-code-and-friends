library(tidyverse)


n <- 34

sim <- function(mat) {
  neigh <- matrix(FALSE, n, n)
  neigh[-1, -1] <- neigh[-1, -1] + mat[-n, -n] # NW
  neigh[-1, -n] <- neigh[-1, -n] + mat[-n, -1] # NE
  neigh[-n, -1] <- neigh[-n, -1] + mat[-1, -n] # SW
  neigh[-n, -n] <- neigh[-n, -n] + mat[-1, -1] # SE
  return ((mat + neigh) %% 2 == 0)
}

mat <- matrix(FALSE, n, n)
df <- NULL
for (rnd in seq_len(331 + 4095)) {
  mat <- sim(mat)
  df <-
    mat |>
    which(arr.ind = TRUE) |>
    as_tibble() |>
    add_column(rnd = rnd) |>
    bind_rows(df)
}

p <-
  df |>
  ggplot(aes(col, row)) +
  geom_tile() +
  scale_x_continuous(limits = c(0.5, n + 0.5), expand = c(0, 0)) +
  scale_y_continuous(limits = c(0.5, n + 0.5), expand = c(0, 0)) +
  coord_fixed() +
  theme_void() +
  gganimate::transition_manual(rnd)

anim <- gganimate::animate(p, nframes = max(df$rnd), renderer = gganimate::ffmpeg_renderer())
gganimate::anim_save("./output/2025_14.mp4", anim)
