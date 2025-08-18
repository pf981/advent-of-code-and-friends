install.packages("matrixcalc")

library(tidyverse)



seat_str <- read_lines(input)

seats <-
  seat_str %>%
  str_c(collapse = "") %>%
  str_split('') %>%
  unlist() %>%
  matrix(ncol = nchar(seat_str[[1]]), byrow = TRUE)
seats

left <- function(m) matrixcalc::shift.left(m, fill = NA_integer_)
right <- function(m) matrixcalc::shift.right(m, fill = NA_integer_)
up <- function(m) matrixcalc::shift.up(m, fill = NA_integer_)
down <- function(m) matrixcalc::shift.down(m, fill = NA_integer_)

inds <- matrix(seq_along(unlist(seats)), ncol = ncol(seats))

N <- down(inds)
NE <- compose(left, down)(inds)
E <- left(inds)
SE <- compose(left, up)(inds)
S <- up(inds)
SW <- compose(right, up)(inds)
W <- right(inds)
NW <- compose(right, down)(inds)

update <- function(seats) {
  repeat {
    occupied_neighbors <-
      (!is.na(seats[N ]) & seats[N ] == "#") + 
      (!is.na(seats[NE]) & seats[NE] == "#") + 
      (!is.na(seats[E ]) & seats[E ] == "#") + 
      (!is.na(seats[SE]) & seats[SE] == "#") + 
      (!is.na(seats[S ]) & seats[S ] == "#") + 
      (!is.na(seats[SW]) & seats[SW] == "#") + 
      (!is.na(seats[W ]) & seats[W ] == "#") + 
      (!is.na(seats[NW]) & seats[NW] == "#")

    new_occupied <- seats == "L" & occupied_neighbors == 0
    new_empty <- seats == "#" & occupied_neighbors >= 4
    
    if (all(!new_occupied & !new_empty)) {
      break
    }
    
    seats[new_occupied] <- "#"
    seats[new_empty] <- "L"
  }
  seats
}

answer <- sum(update(seats) == "#")
answer

offsets <- function(m, f) {
  result <- matrix(NA_integer_, nrow = nrow(m), ncol = ncol(m))
  repeat {
    m <- f(m)
    if (all(is.na(m))) {
      break
    }
    result[is.na(result)] <- m[is.na(result)]
  }
  result
}

inds <- matrix(seq_along(unlist(seats)), ncol = ncol(seats))
inds[seats == "."] <- NA

N <- offsets(inds, down)
NE <- offsets(inds, compose(left, down))
E <- offsets(inds, left)
SE <- offsets(inds, compose(left, up))
S <- offsets(inds, up)
SW <- offsets(inds, compose(right, up))
W <- offsets(inds, right)
NW <- offsets(inds, compose(right, down))

update <- function(seats) {
  repeat {
    occupied_neighbors <-
      (!is.na(seats[N ]) & seats[N ] == "#") + 
      (!is.na(seats[NE]) & seats[NE] == "#") + 
      (!is.na(seats[E ]) & seats[E ] == "#") + 
      (!is.na(seats[SE]) & seats[SE] == "#") + 
      (!is.na(seats[S ]) & seats[S ] == "#") + 
      (!is.na(seats[SW]) & seats[SW] == "#") + 
      (!is.na(seats[W ]) & seats[W ] == "#") + 
      (!is.na(seats[NW]) & seats[NW] == "#")

    new_occupied <- seats == "L" & occupied_neighbors == 0
    new_empty <- seats == "#" & occupied_neighbors >= 5
    
    if (all(!new_occupied & !new_empty)) {
      break
    }
    
    seats[new_occupied] <- "#"
    seats[new_empty] <- "L"
  }
  seats
}

result <- update(seats)
result

answer <- sum(result == "#")
answer
