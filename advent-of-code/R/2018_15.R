library(tidyverse)



start_m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()

start_m

hp <- matrix(0, nrow = nrow(start_m), ncol = ncol(start_m))
hp[start_m %in% c("G", "E")] <- 200

hp

get_adjacent_squares <- function(targets, m, square_type) {
  bind_rows(
    tibble(row = targets$row - 1, col = targets$col),
    tibble(row = targets$row + 1, col = targets$col),
    tibble(row = targets$row, col = targets$col - 1),
    tibble(row = targets$row, col = targets$col + 1)
  ) %>%
    filter(row >= 1, row <= nrow(m), col >= 1, col <= ncol(m)) %>%
    filter(map2_lgl(row, col, ~m[.x, .y] %in% square_type)) %>%
    arrange(row, col)
}

which_df <- function(w, m) {
  w <- matrix(w, nrow = nrow(m))
  which(w, arr.ind = TRUE) %>% as_tibble() %>% arrange(row, col)
}

move <- function(state, cur_pos, target_squares) {
  for (i in seq_len(nrow(target_squares))) {
    state$m[target_squares$row[i], target_squares$col[i]] <- "T"
  }
    
  ds <- c(0)
  rows <- c(cur_pos$row)
  cols <- c(cur_pos$col)
  first_rows <- c(NA)
  first_cols <- c(NA)
  
  while (length(ds) > 0) {
    i <- which.min(ds)
    
    d <- ds[i]
    cur_row <- rows[i]
    cur_col <- cols[i]
    cur_first_row <- first_rows[i]
    cur_first_col <- first_cols[i]
    
    ds <- ds[-i]
    rows <- rows[-i]
    cols <- cols[-i]
    first_rows <- first_rows[-i]
    first_cols <- first_cols[-i]
    
    if (state$m[cur_row, cur_col] == "#") next
    
    if (is.na(cur_first_row) && !(cur_row == cur_pos$row && cur_col == cur_pos$col)) {
      cur_first_row <- cur_row
      cur_first_col <- cur_col
    }
    
    # If found target
    if (state$m[cur_row, cur_col] == "T") {
      return(tibble(row = cur_first_row, col = cur_first_col))
    }
    
    # Don't revisit this position
    state$m[cur_row, cur_col] <- "#"
    
    new_squares <- get_adjacent_squares(tibble(row = cur_row, col = cur_col), state$m, c(".", "T"))
    
    for (new_square_i in seq_len(nrow(new_squares))) {
      ds <- c(ds, d + 1)
      rows <- c(rows, new_squares$row[new_square_i])
      cols <- c(cols, new_squares$col[new_square_i])
      first_rows <- c(first_rows, cur_first_row)
      first_cols <- c(first_cols, cur_first_col)
    }
  }
  cur_pos
}

step <- function(state) {
  units <- which_df(state$m %in% c("G", "E"), state$m)

  for (i in seq_len(nrow(units))) {
    cur_pos <- slice(units, i)
    if (state$hp[cur_pos$row, cur_pos$col] <= 0) next
    
    enemy_type <- ifelse(state$m[cur_pos$row, cur_pos$col] == "G", "E", "G")
    
    # Identify targets
    targets <- which_df(state$m == enemy_type, state$m)
    
    # If there are no more targets, the game is over
    if (nrow(targets) < 1) return(state)
    
    # Identify adjacent squares to targets not occupied
    target_squares <- get_adjacent_squares(targets, state$m, ".")
    
    # If not in range, then move
    if (nrow(get_adjacent_squares(cur_pos, state$m, enemy_type)) == 0) {
      new_pos <- move(state, cur_pos, target_squares)
  
      if (!(new_pos$row == cur_pos$row && new_pos$col == cur_pos$col)) {
        state$m[new_pos$row, new_pos$col] <- state$m[cur_pos$row, cur_pos$col]
        state$m[cur_pos$row, cur_pos$col] <- "."

        state$hp[new_pos$row, new_pos$col] <- state$hp[cur_pos$row, cur_pos$col]
        state$hp[cur_pos$row, cur_pos$col] <- 0

        cur_pos <- new_pos
      }
      
    }
    
    # If in range, attack
    in_range_targets <- get_adjacent_squares(cur_pos, state$m, enemy_type)
    if (nrow(in_range_targets) >= 1) {
      target <-
        in_range_targets %>%
        mutate(
          target_hp = map2_dbl(row, col, ~state$hp[.x, .y])
        ) %>%
        arrange(target_hp, row, col)
      
      attack_row <- target$row[1]
      attack_col <- target$col[1]
      state$hp[attack_row, attack_col] <- state$hp[attack_row, attack_col] - 3
      if (state$hp[attack_row, attack_col] <= 0) {
        state$m[attack_row, attack_col] <- "."
      }
    }
  }
  state$rounds_completed <- state$rounds_completed + 1
  state
}

state <- list(
  m = start_m,
  hp = hp,
  rounds_completed = 0
)

rounds_completed <- 0
repeat {
  state <- step(state)
  if (state$rounds_completed == rounds_completed) break
  rounds_completed <- state$rounds_completed
}

answer <- rounds_completed * sum(state$hp %>% keep(~ . > 0))
answer # 37.05 minutes

step <- function(state) {
  units <- which_df(state$m %in% c("G", "E"), state$m)

  for (i in seq_len(nrow(units))) {
    cur_pos <- slice(units, i)
    if (state$hp[cur_pos$row, cur_pos$col] <= 0) next
    
    enemy_type <- ifelse(state$m[cur_pos$row, cur_pos$col] == "G", "E", "G")
    
    # Identify targets
    targets <- which_df(state$m == enemy_type, state$m)
    
    # If there are no more targets, the game is over
    if (nrow(targets) < 1) return(state)
    
    # Identify adjacent squares to targets not occupied
    target_squares <- get_adjacent_squares(targets, state$m, ".")
    
    # If not in range, then move
    if (nrow(get_adjacent_squares(cur_pos, state$m, enemy_type)) == 0) {
      new_pos <- move(state, cur_pos, target_squares)
  
      if (!(new_pos$row == cur_pos$row && new_pos$col == cur_pos$col)) {
        state$m[new_pos$row, new_pos$col] <- state$m[cur_pos$row, cur_pos$col]
        state$m[cur_pos$row, cur_pos$col] <- "."

        state$hp[new_pos$row, new_pos$col] <- state$hp[cur_pos$row, cur_pos$col]
        state$hp[cur_pos$row, cur_pos$col] <- 0

        cur_pos <- new_pos
      }
      
    }
    
    # If in range, attack
    in_range_targets <- get_adjacent_squares(cur_pos, state$m, enemy_type)
    if (nrow(in_range_targets) >= 1) {
      target <-
        in_range_targets %>%
        mutate(
          target_hp = map2_dbl(row, col, ~state$hp[.x, .y])
        ) %>%
        arrange(target_hp, row, col)
      
      attack_row <- target$row[1]
      attack_col <- target$col[1]
      state$hp[attack_row, attack_col] <- state$hp[attack_row, attack_col] - ifelse(state$m[cur_pos$row, cur_pos$col] == "E", state$e_dmg, 3)
      if (state$hp[attack_row, attack_col] <= 0) {
        if (state$m[attack_row, attack_col] == "E") {
          state$elf_dead <- TRUE
          return(state)
        }
        state$m[attack_row, attack_col] <- "."
      }
    }
  }
  state$rounds_completed <- state$rounds_completed + 1
  state
}

calculate_outcome <- function(state) {
  rounds_completed <- 0
  repeat {
    state <- step(state)
    if (state$elf_dead) return(NA)
    if (state$rounds_completed == rounds_completed) break
    rounds_completed <- state$rounds_completed
  }

  rounds_completed * sum(state$hp %>% keep(~ . > 0))
}

# This method did not find the right number. This is because if an elf damage results in a loss, that doesn't mean that all lower elf damages will also lose.

# start_state <- list(
#   m = start_m,
#   hp = hp,
#   rounds_completed = 0,
#   elf_dead = FALSE,
#   e_dmg = 4
# )

# highest_dmg_lost <- 2
# lowest_dmg_won <- Inf
# lowest_dmg_won_outcome <- NA

# repeat {
#   state <- start_state
#   state$e_dmg <- min(
#     (highest_dmg_lost + lowest_dmg_won) %/% 2,
#     highest_dmg_lost * 2
#   )
  
#   if (state$e_dmg == highest_dmg_lost || state$e_dmg == lowest_dmg_won) break
  
#   outcome <- calculate_outcome(state)
  
#   if (!is.na(outcome)) {
#     lowest_dmg_won_outcome <- outcome
#     lowest_dmg_won <- state$e_dmg
#   } else {
#     highest_dmg_lost <- state$e_dmg
#   }
# }

# answer <- lowest_dmg_won_outcome
# answer # 2.23 hrs

start_state <- list(
  m = start_m,
  hp = hp,
  rounds_completed = 0,
  elf_dead = FALSE,
  e_dmg = 4
)

highest_dmg_lost <- 4
lowest_dmg_won_outcome <- NA

repeat {
  state <- start_state
  state$e_dmg <- highest_dmg_lost
  
  outcome <- calculate_outcome(state)
  
  if (!is.na(outcome)) {
    lowest_dmg_won_outcome <- outcome
    break
  }
  highest_dmg_lost <- highest_dmg_lost + 1
}

answer <- lowest_dmg_won_outcome
answer # 2.68 hrs
