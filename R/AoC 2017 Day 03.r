library(tidyverse)

input <- 289326

ring <- ceiling(sqrt(input)) %/% 2
end <- (2 * (ring + 1) - 1)^2
start <- pmin((2 * (ring) - 1)^2 + 1, end)
edge_size <- sqrt(end)
edge_position <- (input - start + 1) %% (edge_size - 1)
middle <- floor(edge_size / 2)
distance_from_middle_edge <- abs(edge_position - middle)

answer <- distance_from_middle_edge + ring
answer

results <- list()
results[[str_c(0, ",", 0)]] <- 1

x <- 1
y <- 0

repeat {
  myseq <- c(myseq, str_c(x, ",", y))
  
  result <- sum(c(
    results[[str_c(x + 1, ",", y)]],
    results[[str_c(x + 1, ",", y + 1)]],
    results[[str_c(x, ",", y + 1)]],
    results[[str_c(x - 1, ",", y + 1)]],
    results[[str_c(x - 1, ",", y)]],
    results[[str_c(x - 1, ",", y - 1)]],
    results[[str_c(x, ",", y - 1)]],
    results[[str_c(x + 1, ",", y - 1)]]
  ))
  if (result > input) {
    break
  }
  results[[str_c(x, ",", y)]] <- result
  
  if (!is.null(results[[str_c(x - 1, ",", y)]]) && is.null(results[[str_c(x, ",", y + 1)]])) {# If the left is done, go up
    y <- y  + 1
  } else if (!is.null(results[[str_c(x, ",", y - 1)]])) { # If below is done, go left
    x <- x - 1
  } else if (!is.null(results[[str_c(x + 1, ",", y)]])) { # If right is done, go down
    y <- y - 1
  } else if (!is.null(results[[str_c(x, ",", y + 1)]])) { # If up is done, go right
    x <- x + 1
  }
}
  
answer <- result
result
