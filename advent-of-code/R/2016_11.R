library(tidyverse)



# 

elements <- str_extract_all(input, "[\\w+]+(?=-compatible microchip| generator)") %>% unlist() %>% unique()
elements

lookup <- seq_len(2 * length(elements))

names(lookup) <- c(
  str_c(elements, "-compatible microchip"),
  str_c(elements, " generator")
)

floor_to_int <- function(floor) {
  lookup[floor]
}

floors_to_int <- function(floors) map(floors, floor_to_int)

floors <-
  read_lines(input) %>% 
  str_extract_all("[\\w+-]+( microchip| generator)") %>%
  floors_to_int() %>%
  map(sort)

floors

elevator_col <- 2 * length(elements) + 1
microchip_col <- seq(from = 1, to = length(elements), by = 1)
generator_col <- seq(from = length(elements) + 1, to = 2 * length(elements), by = 1)

lst(elevator_col, microchip_col, generator_col)

m_start <-
  floors %>%
  map(function(x) {
    v <- rep(FALSE, 2 * length(elements))
    v[x] <- TRUE
    v
  }) %>%
  simplify2array() %>%
  t() %>%
  cbind(c(TRUE, rep(FALSE, nrow(.) - 1)))

colnames(m_start) <- c(str_c(elements, "-M"), str_c(elements, "-G"), "E")
rownames(m_start) <- str_c("F", seq_len(nrow(m_start)))
m_start

is_valid <- function(m) {
  microchips <- m[,microchip_col]
  generators <- m[,generator_col]

  # Microchips without a corresponding generator
  exposed_microchips <- microchips & !generators

  # Filtered to floors that contain a generator
  !any(exposed_microchips[as.logical(apply(generators, 1, FUN=max)),])
}

hash_m <- function(m) str_c(m, collapse = "")

solve <- function(m = m_start) {
  ms <- list(m)
  n_moves <- c(0)
  
  done_states <- map_chr(ms, hash_m)
  
  repeat {
    # Choose the state with the least moves
    i <- which.min(n_moves)
    m <- ms[[i]]
    n_move <- n_moves[[i]]
    
    ms[[i]] <- NULL
    n_moves <- n_moves[-i]


    # All possible moves
    elevator <- which(m[, elevator_col])
    possble_items <- which(m[elevator, -elevator_col])
    for (new_elevator in c(elevator + 1, elevator - 1)) {
      if (new_elevator < 1 || new_elevator > nrow(m)) {
        next
      }
      
      for (item1 in possble_items) {
        for (item2 in c(0, possble_items[possble_items > item1])) {
          items <- c(item1, item2, elevator_col)
          
          new_m <- m
          new_m[elevator, items] <- FALSE
          new_m[new_elevator, items] <- TRUE
          
          if (!is_valid(m)) {
            next
          }
          
          
          # Check if the problem is solved
          if (all(new_m[nrow(new_m),])) {
            return(n_move + 1)
          }
          
          state_hash <- hash_m(new_m)
          if (!(state_hash %in% done_states)) { # If the state hasn't been reached before
            ms <- c(ms, list(new_m))
            n_moves <- c(n_moves, n_move + 1)
            done_states <- c(done_states, state_hash)
          }
        }
      }
    }
  }
}

answer <- solve()
answer # This took 8.4 hrs



start_state <-
  read_lines(input) %>% 
  str_extract_all("[\\w+-]+( microchip| generator)") %>%
  enframe(name = "floor") %>%
  unnest() %>%
  separate(value, into = c("element", "item_type"), sep = " |-[a-z]+ ", extra = "merge") %>%
  pivot_wider(names_from = item_type, values_from = floor) %>%
  select(-element)

start_state

is_valid <- function(state) {
  floors_with_exposed_chip <-
    state %>%
    filter(microchip != generator) %>%
    pull(microchip) %>%
    unique()
  
  floors_with_generator <-
    state %>%
    pull(generator) %>%
    unique()
  
  !any(floors_with_exposed_chip %in% floors_with_generator)
}

hash <- function(state, elevator) {
  list(
    state = state %>% arrange(microchip, generator), # Sorting the state means that element names are interchangable - dramatically reducing the state space
    elevator = elevator
  ) %>%
    digest::digest()
}

solve <- function(state = start_state) {
  states <- list(state)
  n_moves <- c(0)
  elevators <- c(1)
  
  done_states <- c(hash(state, 1))
  
  repeat {
    # Choose the state with the least moves
    i <- which.min(n_moves)
    state <- states[[i]]
    n_move <- n_moves[[i]]
    elevator <- elevators[[i]]
    
    states[[i]] <- NULL
    n_moves <- n_moves[-i]
    elevators <- elevators[-i]

    # All possible moves
    possible_items <- which(state == elevator, arr.ind = TRUE) %>% asplit(1)
    for (new_elevator in c(elevator + 1, elevator - 1)) {
      if (new_elevator < 1 || new_elevator > 4) {
        next
      }
      
      i_possible <- seq_along(possible_items)
      for (item1 in c(0, i_possible)) {
        for (item2 in i_possible[i_possible > item1]) {
          new_state <- state
          for (item in c(item1, item2)) {
            if (item > 0) {
              new_state[possible_items[[item]][["row"]], possible_items[[item]][["col"]]] <- new_elevator
            }
          }
          
          state_hash <- hash(new_state, new_elevator)
          if (state_hash %in% done_states) {
            next
          }
          
          if (!is_valid(new_state)) {
            next
          }
          
          # Check if the problem is solved
          if (all(new_state == 4)) {
            return(n_move + 1)
          }
          
          states <- c(states, list(new_state))
          n_moves <- c(n_moves, n_move + 1)
          elevators <- c(elevators, new_elevator)
          done_states <- c(done_states, state_hash)
        }
      }
    }
  }
}

answer <- solve()
answer # 1.6 hrs
