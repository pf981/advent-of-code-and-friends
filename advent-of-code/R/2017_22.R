library(tidyverse)



df <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
df

turn_right <- function(direction) {
  case_when(
    direction == "up" ~ "right",
    direction == "right" ~ "down",
    direction == "down" ~ "left",
    direction == "left" ~ "up"
  )
}

turn_left <- function(direction) {
  case_when(
    direction == "up" ~ "left",
    direction == "right" ~ "up",
    direction == "down" ~ "right",
    direction == "left" ~ "down"
  )
}

is_infected <- function(state, pos) {
  matched <-
    state %>%
    filter(row == pos[1], col == pos[2])
  nrow(matched) > 0
}

move_forward <- function(pos, direction) {
  case_when(
    direction == "up" ~ c(pos[1] - 1, pos[2]),
    direction == "right" ~ c(pos[1], pos[2] + 1),
    direction == "down" ~ c(pos[1] + 1, pos[2]),
    direction == "left" ~ c(pos[1], pos[2] - 1)
  )
}

count_infections_caused <- function(df, iterations) {
  infections_caused <- 0
  pos <- c(nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1)
  direction <- "up"
  
  state <- which(df == "#", arr = TRUE) %>% as_tibble()
  
  for (i in seq_len(iterations)) {
    if (is_infected(state, pos)) {
      direction <- turn_right(direction)
      state <- state %>% filter(!(row == pos[1] & col == pos[2]))
    } else {
      direction <- turn_left(direction)
      state <- state %>% add_row(row = pos[1], col = pos[2])
      infections_caused <- infections_caused + 1
    }
    pos <- move_forward(pos, direction)
  } 
  infections_caused
}

answer <- count_infections_caused(df, 10000)
answer

# This was too slow

# turn_around <- function(direction) {
#   case_when(
#     direction == "up" ~ "down",
#     direction == "right" ~ "left",
#     direction == "down" ~ "up",
#     direction == "left" ~ "right"
#   )
# }

# get_status <- function(state, pos) {
#   status <-
#     state %>%
#     filter(row == pos[1], col == pos[2]) %>%
#     pull(status)
  
#   c(status, "clean")[1]
# }

# set_status <- function(state, pos, new_status) {
#   i <- which(state$row == pos[1] & state$col == pos[2])
  
#   if (length(i) == 0) {
#     state <- state %>% add_row(row = pos[1], col = pos[2], status = new_status)
#   } else {
#     state$status[i] <- new_status
#   }
  
#   state
# }

# count_infections_caused <- function(df, iterations) {
#   infections_caused <- 0
#   pos <- c(nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1)
#   direction <- "up"
  
#   state <-
#     which(df == "#", arr = TRUE) %>%
#     as_tibble() %>%
#     add_column(status = "infected")
  
#   for (i in seq_len(iterations)) {
#     node_status <- get_status(state, pos)
    
#     if (node_status == "clean") {
#       direction <- turn_left(direction)
#       state <- set_status(state, pos, "weakened")
#     } else if (node_status == "weakened") {
#       state <- set_status(state, pos, "infected")
#       infections_caused <- infections_caused + 1
#     } else if (node_status == "infected") {
#       direction <- turn_right(direction)
#       state <- set_status(state, pos, "flagged")
#     } else if (node_status == "flagged") {
#       direction <- turn_around(direction)
#       state <- set_status(state, pos, "clean")
#     }
    
#     pos <- move_forward(pos, direction)
#   } 
#   infections_caused
# }

# answer <- count_infections_caused(df, 10000000)
# answer

Rcpp::cppFunction('
int count_infections_caused_cpp(std::vector<int> infected_rows, std::vector<int> infected_cols, int start_row, int start_col, int iterations) {
  const int CLEAN = 0, WEAKENED = 1, INFECTED = 2, FLAGGED = 3;

  std::map<std::pair<int, int>, int> state;
  for (int i = 0; i < infected_rows.size(); ++i) {
    state[std::make_pair(infected_rows[i], infected_cols[i])] = INFECTED;
  }

  int infections_caused = 0;
  auto pos = std::make_pair(start_row, start_col);
  int row_change = -1 ;
  int col_change = 0;
  for (int i = 0; i < iterations; ++i) {
    switch (state[pos]) {
      case CLEAN:
        // Turn left
        if      (row_change == -1) {row_change =  0; col_change = -1;} // up -> left
        else if (col_change ==  1) {row_change = -1; col_change =  0;} // right -> up
        else if (row_change ==  1) {row_change =  0; col_change =  1;} // down -> right
        else if (col_change == -1) {row_change =  1; col_change =  0;} // left -> down
        break;
      case WEAKENED:
        // No turn
        ++infections_caused;
        break;
      case INFECTED:
        // Turn right
        if      (row_change == -1) {row_change =  0; col_change =  1;} // up -> right
        else if (col_change ==  1) {row_change =  1; col_change =  0;} // right -> down
        else if (row_change ==  1) {row_change =  0; col_change = -1;} // down -> left
        else if (col_change == -1) {row_change = -1; col_change =  0;} // left -> up
        break;
      case FLAGGED:
        // Reverse
        if      (row_change == -1) {row_change =  1; col_change =  0;} // up -> down
        else if (col_change ==  1) {row_change =  0; col_change = -1;} // right -> left
        else if (row_change ==  1) {row_change = -1; col_change =  0;} // down -> up
        else if (col_change == -1) {row_change =  0; col_change =  1;} // left -> right
        break;
    }
    state[pos] = (state[pos] + 1) % 4;
    pos.first += row_change;
    pos.second += col_change;
  }

  return infections_caused;
}
')

infections <- which(df == "#", arr = TRUE) %>% as_tibble()

answer <- count_infections_caused_cpp(infections$row, infections$col, nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1, 10000000)
answer
