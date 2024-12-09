library(tidyverse)



sequence <- input %>% str_split(",") %>% unlist() %>% parse_integer()
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

run_instructions <- function(instructions, input = 1) {
  instructions <- c(instructions, numeric(100000)) # Extra memory. Note i'm using numeric rather than integer so it can handle big integers
  instructions <- structure(instructions, class = "special_index")
  attr(instructions, "relative_base") <- 0
  
  output <- list()
  
  i <- 0
  current_tile = c()
  
  while (instructions[list(i, 1)] != 99) {
    value <- instructions[list(i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_index_mode)
    p2 <- list(i + 2, p2_index_mode)
    p3 <- list(i + 3, p3_index_mode)
    
    # print_state(instructions, input, i, p1, p2, p3, op_code)
    
    if (op_code == 1) {
      instructions[p3] <- instructions[p1] + instructions[p2]
    } else if (op_code == 2) {
      instructions[p3] <- instructions[p1] * instructions[p2]
    } else if (op_code == 3) {
      instructions[p1] <- input
    } else if (op_code == 4) {
      input <- instructions[p1] # What is this!?
      current_tile <- c(current_tile, instructions[p1])
      if (length(current_tile) == 3) {
        output <- c(output, list(current_tile))
        current_tile <- c()
      }
    } else if (op_code == 5) {
      if (instructions[p1] != 0) {
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (instructions[p1] == 0) {
        i = get_index(instructions, p2) - 1
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      instructions[p3] <- instructions[p1] < instructions[p2]
    } else if (op_code == 8) {
      instructions[p3] <- instructions[p1] == instructions[p2]
    } else if (op_code == 9) {
      # New instruction: Relative base offset
      attr(instructions, "relative_base") <- attr(instructions, "relative_base") + instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    i <- i + 1 + num_params
  }

  map_dfr(output, set_names, c("x", "y", "tile_id"))
}

df <- run_instructions(sequence)
df

answer <- sum(df$tile_id == 2)
answer

ggplot(df, aes(x, -y, fill = as.factor(tile_id))) +
  geom_tile() +
  scale_fill_manual(
    values = c("white", "black", "grey", "brown", "green")
  ) +
  theme_void() +
  theme(legend.position = "none")

df %>% filter(tile_id %in% c(3, 4))

run_instructions2 <- function(instructions) {
  instructions <- c(instructions, numeric(1000)) # Extra memory. Note i'm using numeric rather than integer so it can handle big integers
  instructions <- structure(instructions, class = "special_index")
  attr(instructions, "relative_base") <- 0
  
  i <- 0
  current_tile = c()
  
  ball_x <- 18
  paddle_x <- 20
  
  n_blocks <- 0
  score <- 0
  
  while (instructions[list(i, 1)] != 99) {
    input <- case_when(
      ball_x < paddle_x ~ -1, # Left
      ball_x > paddle_x ~ 1, # Right
      TRUE ~ 0
    )
    value <- instructions[list(i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000 # Unused
    
    p1 <- list(i + 1, p1_index_mode)
    p2 <- list(i + 2, p2_index_mode)
    p3 <- list(i + 3, p3_index_mode)
    
    # print_state(instructions, input, i, p1, p2, p3, op_code)
    
    if (op_code == 1) {
      instructions[p3] <- instructions[p1] + instructions[p2]
    } else if (op_code == 2) {
      instructions[p3] <- instructions[p1] * instructions[p2]
    } else if (op_code == 3) {
      #if (n_blocks == 0) break
      instructions[p1] <- input
      n_blocks <- 0
    } else if (op_code == 4) {
      current_tile <- c(current_tile, instructions[p1])
      if (length(current_tile) == 3) {
        if (current_tile[1] == -1 && current_tile[2] == 0) {
          score <- current_tile[3]
        } else if (current_tile[3] == 2) {
          n_blocks <- n_blocks + 1
        } else if (current_tile[3] == 3) {
          paddle_x <- current_tile[1]
        } else if (current_tile[3] == 4) {
          ball_x <- current_tile[1]
        }
        
        current_tile <- c()
      }
    } else if (op_code == 5) {
      if (instructions[p1] != 0) {
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (instructions[p1] == 0) {
        i = get_index(instructions, p2) - 1
        i <- instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      instructions[p3] <- instructions[p1] < instructions[p2]
    } else if (op_code == 8) {
      instructions[p3] <- instructions[p1] == instructions[p2]
    } else if (op_code == 9) {
      # New instruction: Relative base offset
      attr(instructions, "relative_base") <- attr(instructions, "relative_base") + instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', i, '\n', paste0(instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    i <- i + 1 + num_params
  }

  score
}

instructions <- sequence
instructions[1] <- 2
answer <- run_instructions2(instructions)
answer # 5 minutes
