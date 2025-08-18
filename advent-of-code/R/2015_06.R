library(tidyverse)



generate_f <- function(operation, x_start, x_end, y_start, y_end) {
  if (operation == "turn on") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- TRUE
      m
    }
  }
  else if (operation == "turn off") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- FALSE
      m
    }
  }
  else if (operation == "toggle") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- !m[x_start:x_end, y_start:y_end]
      m
    }
  } else {
    stop(str_c("Don't understand operation ", operation))
  }
}

df <-
  read_table(input, col_names = "instruction") %>%
  mutate(
    operation = str_extract(instruction, "^[:alpha:]+ ?[:alpha:]+"),
    x_start = str_extract(instruction, "\\d+(?=,)"),
    x_end = str_extract(instruction, "(?<=through )\\d+"),
    y_start = str_extract(instruction, "(?<=,)\\d+"),
    y_end = str_extract(instruction, "\\d+$"),
    f = pmap(list(operation, x_start, x_end, y_start, y_end), generate_f)
  )
df

result <- compose(!!!df$f, .dir = "forward")(matrix(FALSE, nrow = 1000, ncol = 1000))

answer <- sum(result)
answer

generate_f2 <- function(operation, x_start, x_end, y_start, y_end) {
  if (operation == "turn on") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- m[x_start:x_end, y_start:y_end] + 1
      m
    }
  }
  else if (operation == "turn off") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- pmax(m[x_start:x_end, y_start:y_end] - 1, 0)
      m
    }
  }
  else if (operation == "toggle") {
    function(m) {
      m[x_start:x_end, y_start:y_end] <- m[x_start:x_end, y_start:y_end] + 2
      m
    }
  } else {
    stop(str_c("Don't understand operation ", operation))
  }
}

df2 <-
  df %>%
  mutate(
     f = pmap(list(operation, x_start, x_end, y_start, y_end), generate_f2)
  )

result <- compose(!!!df2$f, .dir = "forward")(matrix(0, nrow = 1000, ncol = 1000))

answer <- sum(result)
answer
