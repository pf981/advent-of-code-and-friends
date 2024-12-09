library(tidyverse)


text <- read_lines("data/2023-08.txt")




get_steps <- function(pos) {
  i <- 1
  steps <- 0
  while (!str_ends(pos, "Z")) {
    pos <- tree[[pos]][1 + (instructions[i] == "R")]
    steps <- steps + 1
    i <- i + 1
    if (i > length(instructions)) {
      i <- 1
    }
  }
  steps
}

instructions <- text[1] |> str_split_1("")
tree <-
  text |>
  tail(-2) |>
  str_extract_all("\\w{3}") |>
  (\(.) set_names(., map_chr(., head, 1)))() |>
  map(tail, -1)

answer1 <- get_steps("AAA")
print(answer1)




gcd <- function(x, y) ifelse(y, Recall(y, x %% y), x)
lcm <- function(x, y) x * y / gcd(x, y)

steps <-
  names(tree) |>
  keep(str_ends, "A") |>
  map_int(get_steps)

answer2 <- reduce(steps, lcm)
print(format(answer2, scientific = FALSE))
