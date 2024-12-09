library(tidyverse)



m <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

carts <-
  map_dfr(
    str_split("^v<>", "")[[1]],
    function(dir) {
      which(m == dir, arr.ind = TRUE) %>%
        as_tibble() %>%
        mutate(direction = dir, intersections = 0)
    }
  ) %>%
  arrange(row, col)
carts

step <- function(carts) {
  for (i in seq_len(nrow(carts))) {
    dir <- carts$direction[i]
    row <- carts$row[i]
    col <- carts$col[i]
    intersections <- carts$intersections[i]
    track <- m[row, col]
    dir <- case_when(
      dir == "^" && track == "\\" ~ "<",
      dir == "^" && track ==  "/" ~ ">",
      dir == "v" && track == "\\" ~ ">",
      dir == "v" && track ==  "/" ~ "<",
      dir == "<" && track == "\\" ~ "^",
      dir == "<" && track ==  "/" ~ "v",
      dir == ">" && track == "\\" ~ "v",
      dir == ">" && track ==  "/" ~ "^",
      TRUE ~ dir
    )
    if (track == "+") {
      dir <- case_when(
        # Left
        dir == "^" && intersections == 0 ~ "<",
        dir == "v" && intersections == 0 ~ ">",
        dir == "<" && intersections == 0 ~ "v",
        dir == ">" && intersections == 0 ~ "^",
        # Straight (no change)
        # Right
        dir == "^" && intersections == 2 ~ ">",
        dir == "v" && intersections == 2 ~ "<",
        dir == "<" && intersections == 2 ~ "^",
        dir == ">" && intersections == 2 ~ "v",
        TRUE ~ dir
      )
      intersections <- (intersections + 1) %% 3
    }

    if (dir == "^") {
      row <- row - 1
    } else if (dir == "v") {
      row <- row + 1
    } else if (dir == "<") {
      col <- col - 1
    } else if (dir == ">") {
      col <- col + 1
    }
    
    if (any(carts$row == row & carts$col == col)) {
      # Just return the answer rather than carts
      return(str_c(col - 1, row - 1, sep = ","))
    }
    
    carts$direction[i] <- dir
    carts$row[i] <- row
    carts$col[i] <- col
    carts$intersections[i] <- intersections
  }
  
  carts %>% arrange(row, col)
}

print_cart <- function(carts) {
  m2 <- mt
  m2[str_detect(m2, "[v^<>]")] <- "?"
  for (i in seq_len(nrow(carts))) {
    m2[carts$row[i], carts$col[i]] <- carts$direction[i]
  }
  cat(str_c(apply(m2, 1, str_c, collapse = ""), collapse = "\n"))
  cat("\n\n")
}

first_crash <- function(carts) {
  repeat {
    carts <- step(carts)
    if (is.character(carts)) {
      return(carts)
    }
  }
}

answer <- first_crash(carts)
answer

step <- function(carts) {
  carts$delete <- FALSE
  for (i in seq_len(nrow(carts))) {
    if (carts$delete[i]) next
    dir <- carts$direction[i]
    row <- carts$row[i]
    col <- carts$col[i]
    intersections <- carts$intersections[i]
    track <- m[row, col]
    dir <- case_when(
      dir == "^" && track == "\\" ~ "<",
      dir == "^" && track ==  "/" ~ ">",
      dir == "v" && track == "\\" ~ ">",
      dir == "v" && track ==  "/" ~ "<",
      dir == "<" && track == "\\" ~ "^",
      dir == "<" && track ==  "/" ~ "v",
      dir == ">" && track == "\\" ~ "v",
      dir == ">" && track ==  "/" ~ "^",
      TRUE ~ dir
    )
    if (track == "+") {
      dir <- case_when(
        # Left
        dir == "^" && intersections == 0 ~ "<",
        dir == "v" && intersections == 0 ~ ">",
        dir == "<" && intersections == 0 ~ "v",
        dir == ">" && intersections == 0 ~ "^",
        # Straight (no change)
        # Right
        dir == "^" && intersections == 2 ~ ">",
        dir == "v" && intersections == 2 ~ "<",
        dir == "<" && intersections == 2 ~ "^",
        dir == ">" && intersections == 2 ~ "v",
        TRUE ~ dir
      )
      intersections <- (intersections + 1) %% 3
    }

    if (dir == "^") {
      row <- row - 1
    } else if (dir == "v") {
      row <- row + 1
    } else if (dir == "<") {
      col <- col - 1
    } else if (dir == ">") {
      col <- col + 1
    }
    
    if (any(carts$row == row & carts$col == col & !carts$delete)) {
      carts$delete[i] <- TRUE
      carts$delete[carts$row == row & carts$col == col] <- TRUE
      next
    }
    
    carts$direction[i] <- dir
    carts$row[i] <- row
    carts$col[i] <- col
    carts$intersections[i] <- intersections
  }
  
  carts %>%
    filter(!delete) %>%
    select(-delete) %>%
    arrange(row, col)
}

last_cart <- function(carts) {
  repeat {
    carts <- step(carts)
    if (nrow(carts) <= 1) {
      return(carts)
    }
  }
}

result <- last_cart(carts)
answer <- str_c(result$col - 1, result$row - 1, sep = ",")
answer
