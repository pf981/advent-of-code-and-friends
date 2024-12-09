library(tidyverse)


m <- read_lines("data/2023-10.txt") |> str_split("")

pipes <-
  list(
    "|" = c(
      " # ",
      " # ",
      " # "
    ),
    "-" = c(
      "   ",
      "###",
      "   "
    ),
    "L" = c(
      " # ",
      " ##",
      "   "
    ),
    "J" = c(
      " # ",
      "## ",
      "   "
    ),
    "7" = c(
      "   ",
      "## ",
      " # "
    ),
    "F" = c(
      "   ",
      " ##",
      " # "
    )
  ) |>
  map(str_split, "") |>
  map(simplify2array) |>
  map(t)

start <- map(m, \(.) . == "S")
start_row <- which(map_lgl(start, sum))
start_col <- which(start[[start_row]])

start_sides <-
  c(
    ifelse(start_row - 1 == 0,             0, m[[start_row - 1]][[start_col]] %in% c("|", "7", "F")),
    ifelse(start_col + 1 > length(m[[1]]), 0, m[[start_row]][[start_col + 1]] %in% c("-", "J", "7")),
    ifelse(start_row + 1 > length(m),      0, m[[start_row + 1]][[start_col]] %in% c("|", "L", "J")),
    ifelse(start_col - 1 == 0,             0, m[[start_row]][[start_col - 1]] %in% c("-", "L", "F"))
  ) |>
  as.integer() |>
  str_c(collapse = "")

m[[start_row]][[start_col]] <-
  c(
    `1010` = "|",
    `0101` = "-",
    `1100` = "L",
    `1001` = "J",
    `0011` = "7",
    `0110` = "F"
  )[start_sides]


grid <- matrix(" ", nrow = length(m) * 3, ncol = length(m[[1]]) * 3)

stamp <- function(row, col, ch) {
  rows <- seq(from = (row - 1) * 3 + 1, to = row * 3, by = 1)
  cols <- seq(from = (col - 1) * 3 + 1, to = col * 3, by = 1)
  grid[rows, cols] <<- pipes[[ch]]
}

pipe_len <- 0
prev_row <- 0
prev_col <- 0
row <- start_row
col <- start_col
repeat {
  pipe_len <- pipe_len + 1
  
  ch <- m[[row]][[col]]
  stamp(row, col, ch)
  
  new_row <- row
  new_col <- col
  
  if (ch %in% c("|", "L", "J") && any(c(row - 1, col) != c(prev_row, prev_col))) {
    new_row <- row - 1
  } else if (ch %in% c("-", "L", "F") && any(c(row, col + 1) != c(prev_row, prev_col))) {
    new_col <- col + 1
  } else if (ch %in% c("|", "7", "F") && any(c(row + 1, col) != c(prev_row, prev_col))) {
    new_row <- row + 1
  } else if (ch %in% c("-", "J", "7") && any(c(row, col - 1) != c(prev_row, prev_col))) {
    new_col <- col - 1
  }
  
  prev_row <- row
  prev_col <- col
  row <- new_row
  col <- new_col
  
  if (all(c(row, col) == c(start_row, start_col))) {
    break
  }
}
answer1 <- pipe_len %/% 2
print(answer1)




# #: Wall
# .: Grass
#  : Water
stack = fastmap::faststack()
stack$push(c(1, 1))
while (stack$size() != 0) {
  pos <- stack$pop()
  if (pos[1] == 0 || pos[2] == 0 || pos[1] > nrow(grid) || pos[2] > ncol(grid) || grid[pos[1],pos[2]] != " ") {
    next
  }
  
  grid[pos[1],pos[2]] <- "."
  for (d in c("N", "E", "S", "W")) {
    stack$push(c(pos[1] + (d == "S") - (d == "N"), pos[2] + (d == "E") - (d == "W")))
  }
}

water_centers <-
  which(grid == " ", arr.ind = TRUE) |>
  as_tibble() |>
  filter((row - 1) %% 3 == 1, (col - 1) %% 3 == 1)

answer2 <- nrow(water_centers)
print(answer2)




c("#", ".", " ") |>
  map(\(.) which(grid == ., arr.ind = TRUE) |> as_tibble()) |>
  list_rbind(names_to = "tile_type") |>
  ggplot(aes(col, row, fill = factor(tile_type))) +
  geom_tile(col = NA, width = 1.05, height = 1.05) +
  scale_x_continuous(
    breaks = seq(0.5, ncol(grid) + 1, 3),
    minor_breaks = seq(0.5, ncol(grid) + 1, 1),
    limits = c(0.5, ncol(grid) + 0.5),
    expand = c(0, 0)
  ) +
  scale_y_reverse(
    breaks = seq(0.5, nrow(grid) + 1, 3),
    minor_breaks = seq(0.5, nrow(grid) + 1, 1),
    limits = c(nrow(grid) + 0.5, 0.5),
    expand = c(0, 0)
  ) +
  scale_fill_manual(values = c("black", "yellowgreen", "steelblue1")) +
  theme_void() +
  theme(
    legend.position = "none",
    aspect.ratio = nrow(grid) / ncol(grid)
  )
