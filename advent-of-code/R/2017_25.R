library(tidyverse)





# move_left <- function(tape) {
#   if (tape$pos == 1) {
#     tape$v <- c(0, tape$v)
#   } else {
#     tape$pos <- tape$pos - 1
#   }
#   tape
# }

# move_right <- function(tape) {
#   if (tape$pos == length(tape$v)) {
#     tape$v <- c(tape$v, 0)
#   }
#   tape$pos <- tape$pos + 1
#   tape
# }

# steps <- 6
# tape <- list(
#   v = c(0),
#   pos = 1,
#   state= "A"
# )

# for (i in seq_len(steps)) {
#   if (tape$state == "A") {
#     if (tape$v[tape$pos] == 0) {
#       tape$v[tape$pos] <- 1
#       tape <- move_right(tape)
#       tape$state <- "B"
#     } else {
#       tape$v[tape$pos] <- 0
#       tape <- move_left(tape)
#       tape$state <- "B"
#     }
#   } else if (tape$state == "B") {
#     if (tape$v[tape$pos] == 0) {
#       tape$v[tape$pos] <- 1
#       tape <- move_left(tape)
#       tape$state <- "A"
#     } else {
#       tape$v[tape$pos] <- 1
#       tape <- move_right(tape)
#       tape$state <- "A"
#     }
#   }
# }

# answer <- sum(tape$v)
# answer

move_left <- function(tape) {
  if (tape$pos == 1) {
    tape$v <- c(0, tape$v)
  } else {
    tape$pos <- tape$pos - 1
  }
  tape
}

move_right <- function(tape) {
  if (tape$pos == length(tape$v)) {
    tape$v <- c(tape$v, 0)
  }
  tape$pos <- tape$pos + 1
  tape
}

steps <- 12523873
tape <- list(
  v = c(0),
  pos = 1,
  state= "A"
)

for (i in seq_len(steps)) {
  if (tape$state == "A") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "B"
    } else {
      tape$v[tape$pos] <- 1
      tape <- move_left(tape)
      tape$state <- "E"
    }
  } else if (tape$state == "B") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "C"
    } else {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "F"
    }
  } else if (tape$state == "C") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_left(tape)
      tape$state <- "D"
    } else {
      tape$v[tape$pos] <- 0
      tape <- move_right(tape)
      tape$state <- "B"
    }
  } else if (tape$state == "D") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "E"
    } else {
      tape$v[tape$pos] <- 0
      tape <- move_left(tape)
      tape$state <- "C"
    }
  } else if (tape$state == "E") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_left(tape)
      tape$state <- "A"
    } else {
      tape$v[tape$pos] <- 0
      tape <- move_right(tape)
      tape$state <- "D"
    }
  } else if (tape$state == "F") {
    if (tape$v[tape$pos] == 0) {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "A"
    } else {
      tape$v[tape$pos] <- 1
      tape <- move_right(tape)
      tape$state <- "C"
    }
  }
}

answer <- sum(tape$v)
answer # 4 minutes

# No puzzle here - just need 49 stars.
