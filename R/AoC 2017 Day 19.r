library(tidyverse)



# 

m <-
  read_lines(input) %>%
  str_split("") %>%
  {matrix(unlist(.), ncol = length(.[[1]]), byrow = TRUE)}
m

is_available <- function(m, pos) {
  row <- pos[1]
  col <- pos[2]
  if (row < 1 || col < 1 || row > nrow(m) || col > ncol(m)) return(FALSE)
  m[row, col] != " "
}

get_new_pos <- function(m, pos, direction) {
  pos <- case_when(
    direction == "up" ~ c(pos[1] - 1, pos[2]),
    direction == "down" ~ c(pos[1] + 1, pos[2]),
    direction == "left" ~ c(pos[1], pos[2] - 1),
    direction == "right" ~ c(pos[1], pos[2] + 1)
  )
  if (is_available(m, pos)) {
    pos
  } else {
    NA
  }
}

get_possible_directions <- function(direction) {
  case_when(
    direction == "up" ~ c("up", "left", "right", "end"),
    direction == "down" ~ c("down", "left", "right", "end"),
    direction == "left" ~ c("left", "up", "down", "end"),
    direction == "right" ~ c("right", "up", "down", "end")
  )
}

solve <- function(m) {
  pos <- c(1, which(m[1,] != " "))
  direction = "down"

  path <- ""

  repeat {
    path <- str_c(path, m[pos[1], pos[2]])

    for (new_direction in get_possible_directions(direction)) {
      if (new_direction == "end") return(path)
      
      new_pos <- get_new_pos(m, pos, new_direction)
      
      if (!is.na(new_pos)) {
        pos <- new_pos
        direction <- new_direction
        break
      }
    }
  }
}

result <- solve(m)
answer <- result %>% str_replace_all("[^A-Z]", "")
answer

answer <- result %>% str_length()
answer
