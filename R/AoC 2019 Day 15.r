library(tidyverse)



sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

create_instructions <- function(instructions) {
  result <- structure(instructions, class = "instructions")
  attr(result, "relative_base") <- 0
  names(result) <- seq(from = 0, length.out = length(instructions))
  result
}

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(v, i) {
  index <- i[[1]]
  if (i[[2]] == 0) {
    # Position mode
    index <- v[[as.character(index)]]
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- v[list(index, 1)] + attr(v, "relative_base")
  }
  index
}

`[.instructions` <- function(v, i) {
  index <- as.character(get_index(v, i))
  result <- v[[index]]
  if (is.null(result) || is.na(result)) v[[index]] <- 0
  v[[index]]
}

`[<-.instructions` <- function(v, i, j, value) {
  v[[as.character(get_index(v, i))]] <- value
  v
}

run_bot <- function(bot, input) {
  while (bot$instructions[list(bot$i, 1)] != 99) {
    value <- bot$instructions[list(bot$i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000
    
    p1 <- list(bot$i + 1, p1_index_mode)
    p2 <- list(bot$i + 2, p2_index_mode)
    p3 <- list(bot$i + 3, p3_index_mode)
    
    if (op_code == 1) {
      bot$instructions[p3] <- bot$instructions[p1] + bot$instructions[p2]
    } else if (op_code == 2) {
      bot$instructions[p3] <- bot$instructions[p1] * bot$instructions[p2]
    } else if (op_code == 3) {
      bot$instructions[p1] <- input
    } else if (op_code == 4) {
      bot$output <- bot$instructions[p1]
      num_params <- 1
      bot$i <- bot$i + 1 + num_params
      break
    } else if (op_code == 5) {
      if (bot$instructions[p1] != 0) {
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (bot$instructions[p1] == 0) {
        bot$i = get_index(bot$instructions, p2) - 1
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      bot$instructions[p3] <- bot$instructions[p1] < bot$instructions[p2]
    } else if (op_code == 8) {
      bot$instructions[p3] <- bot$instructions[p1] == bot$instructions[p2]
    } else if (op_code == 9) {
      attr(bot$instructions, "relative_base") <- attr(bot$instructions, "relative_base") + bot$instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(bot$instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    bot$i <- bot$i + 1 + num_params
  }
  
  if (bot$instructions[list(bot$i, TRUE)] == 99) {
    bot$is_halted <- TRUE
  }

  bot
}

create_bot <- function(instructions) {
  list(
    instructions = create_instructions(instructions),
    i = 0,
    x = 0,
    y = 0,
    is_halted = FALSE,
    output = NULL
  )
}

hash <- paste

solve <- function(instructions) {
  bots <- list(create_bot(instructions))
  ds <- c(0)
  visited <- c()

  repeat {
    i <- which.min(ds)

    bot <- bots[[i]]
    d <- ds[i]

    bots[[i]] <- NULL
    ds <- ds[-i]

    if (hash(bot$x, bot$y) %in% visited) next
    visited <- c(visited, hash(bot$x, bot$y))
    
    for (input_value in seq_len(4)) {
      new_x <- bot$x + (input_value == 4) - (input_value == 3)
      new_y <- bot$y + (input_value == 2) - (input_value == 1)

      if (hash(new_x, new_y) %in% visited) next
      
      new_bot <- run_bot(bot, input_value)
      new_bot$x <- new_x
      new_bot$y <- new_y
      
      if (new_bot$output == 0) {
        visited <- c(visited, hash(new_x, new_y))
        next # Wall
      }

      if (new_bot$output == 1) { # Move
        bots <- c(bots, list(new_bot))
        ds <- c(ds, d + 1)
      }

      if (new_bot$output == 2) return(d + 1) # Found oxygen system
    }
  }
}

answer <- solve(sequence)
answer

create_area_map <- function(instructions) {
  area_map <- list() # x, y, value
  
  bots <- list(create_bot(instructions))
  visited <- c()

  while (length(bots) > 0) {
    bot <- bots[[1]]
    bots[[1]] <- NULL

    if (hash(bot$x, bot$y) %in% visited) next
    visited <- c(visited, hash(bot$x, bot$y))
    
    for (input_value in seq_len(4)) {
      new_x <- bot$x + (input_value == 4) - (input_value == 3)
      new_y <- bot$y + (input_value == 2) - (input_value == 1)

      if (hash(new_x, new_y) %in% visited) next
      
      new_bot <- run_bot(bot, input_value)
      new_bot$x <- new_x
      new_bot$y <- new_y
      
      if (new_bot$output == 0) {
        visited <- c(visited, hash(new_x, new_y))
      } else if (new_bot$output == 1) { # Move
        bots <- c(bots, list(new_bot))
      } else if (new_bot$output == 2) {} # Found oxygen system
      
      area_map <- c(area_map, list(c(new_bot$x, new_bot$y, new_bot$output)))
    }
  }
  
  area_map %>% map_dfr(set_names, c("x", "y", "value"))
}

area_map <- create_area_map(sequence)
area_map

ggplot(area_map, aes(x, y, fill = as.factor(value))) +
  geom_tile() +
  annotate("label", x = 0, y = 0, color = "red", label = "S") +
  scale_fill_manual(values = c("black", "grey", "green")) +
  theme_void() +
  theme(legend.position = "none")

compute_oxygen_fill_time <- function(area_map) {
  ds <- c(0)
  xs <- c(area_map$x[area_map$value == 2])
  ys <- c(area_map$y[area_map$value == 2])
  
  visited <- c()
  valid_coords <-
    area_map %>%
    filter(value == 1) %>%
    transmute(id = hash(x, y)) %>%
    pull() %>%
    c(hash(0, 0))
  
  max_d <- 0
  
  while(length(ds) > 0) {
    i <- which.min(ds)

    d <- ds[i]
    x <- xs[i]
    y <- ys[i]

    ds <- ds[-i]
    xs <- xs[-i]
    ys <- ys[-i]

    if (hash(x, y) %in% visited) next
    visited <- c(visited, hash(x, y))
    
    max_d <- max(max_d, d)
    
    for (direction in seq_len(4)) {
      new_x <- x + (direction == 4) - (direction == 3)
      new_y <- y + (direction == 2) - (direction == 1)
      new_d <- d + 1

      if (hash(new_x, new_y) %in% visited) next
      
      if (hash(new_x, new_y) %in% valid_coords) { # Move
        ds <- c(ds, new_d)
        xs <- c(xs, new_x)
        ys <- c(ys, new_y)
      }
    }
  }
  max_d
}

answer <- compute_oxygen_fill_time(area_map)
answer
