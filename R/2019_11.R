library(tidyverse)



sequence <- input %>% str_split(",") %>% unlist() %>% parse_double()
sequence

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(df, i) {
  index <- i[[1]] + 1
  if (i[[2]] == 0) {
    # Position mode
    index <- df[[index]] + 1
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- df[[index]] + attr(df, "relative_base") + 1
  }
  index
}

`[.special_index` <- function(df, i) {
  df[[get_index(df, i)]]
}

`[<-.special_index` <- function(df, i, j, value) {
  df[[get_index(df, i)]] <- value
  
  df
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

hashmap <- function(default = NULL) {
  h <- structure(new.env(hash = TRUE), class = "hashmap")
  attr(h, "default") <- default
  h
}

hash_fn <- function(x) paste(x, collapse = ",")

`[.hashmap` <- function(h, i) {
  result <- h[[hash_fn(i)]]
  if (is.null(result)) result <- attr(h, "default")
  result
}

`[<-.hashmap` <- function(h, i, j, value) {
  h[[hash_fn(i)]] <- value
  h
}

as.list.hashmap <- function(h) {
  attr(h, "class") <- NULL
  attr(h, "default") <- NULL
  as.list(h)
}

create_bot <- function(instructions, extra_memory = 1000) {
  bot <- list(
    instructions = structure(c(instructions, numeric(extra_memory)), class = "special_index"),
    i = 0,
    is_halted = FALSE,
    output = NULL
  )
  attr(bot$instructions, "relative_base") <- 0
  bot
}

paint <- function(instructions, panels = hashmap(default = 0)) {
  bot <- create_bot(instructions)
  position <- c(0, 0)
  direction <- "N"

  while (!bot$is_halted) {
    bot <- run_bot(bot, panels[position])
    paint_value <- bot$output
    bot <- run_bot(bot, panels[position])
    direction_value <- bot$output

    panels[position] <- paint_value
    if (direction_value == 0) { # Left
      direction <- case_when(
        direction == "N" ~ "W",
        direction == "E" ~ "N",
        direction == "S" ~ "E",
        direction == "W" ~ "S",
      )
    } else { # Right
      direction <- case_when(
        direction == "N" ~ "E",
        direction == "E" ~ "S",
        direction == "S" ~ "W",
        direction == "W" ~ "N",
      )
    }
    position <- c(
      position[1] + ifelse(direction == "W", -1, 0) + ifelse(direction == "E", 1, 0),
      position[2] + ifelse(direction == "N", -1, 0) + ifelse(direction == "S", 1, 0)
    )
  }
  panels
}

panels <- paint(sequence)
answer <- length(panels)
answer

panels <- hashmap(default = 0)
panels[c(0, 0)] <- 1

panels <- paint(sequence, panels)

coords <-
  panels %>%
  as.list() %>%
  keep(~. == 1) %>%
  names() %>%
  str_split(",") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("row", "col"))

ggplot(coords, aes(row, -col)) +
  geom_tile() +
  ylim(-40, 1) +
  theme_void()
