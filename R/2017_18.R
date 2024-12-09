library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    x = str_split(line, " ")
  ) %>%
  unnest_wider(x) %>%
  rename(
    instruction = ...1,
    x = ...2,
    y = ...3
  )
df

get_value <- function(x, state) {
  if (!is.na(as.integer(x))) {
    return(as.integer(x))
  }
  c(state[[x]], 0)[1]
}

solve <- function(df) {
  sound <- 0
  state <- list()
  i <- 1
  repeat {
    instruction <- df$instruction[i]
    x <- df$x[i]
    y <- df$y[i]

    if (instruction == "snd") {
      sound <- get_value(x, state)
    } else if (instruction == "set") {
      state[[x]] <- get_value(y, state)
    } else if (instruction == "add") {
      state[[x]] <- get_value(x, state) + get_value(y, state)
    } else if (instruction == "mul") {
      state[[x]] <- get_value(x, state) * get_value(y, state)
    } else if (instruction == "mod") {
      state[[x]] <- get_value(x, state) %% get_value(y, state)
    } else if (instruction == "rcv") {
      if (get_value(x, state) != 0) {
        return(sound)
      }
    } else if (instruction == "jgz") {
      if (get_value(x, state) > 0) {
        i <- i + get_value(y, state) - 1
      }
    }
    i <- i + 1
  }
}

solve(df)

run <- function(df, state) {
  instruction <- df$instruction[state$line]
  x <- df$x[state$line]
  y <- df$y[state$line]

  state$waiting_for_signal <- FALSE
  if (instruction == "snd") {
    state$signal_out <- c(state$signal_out, get_value(x, state))
  } else if (instruction == "set") {
    state[[x]] <- get_value(y, state)
  } else if (instruction == "add") {
    state[[x]] <- get_value(x, state) + get_value(y, state)
  } else if (instruction == "mul") {
    state[[x]] <- get_value(x, state) * get_value(y, state)
  } else if (instruction == "mod") {
    state[[x]] <- get_value(x, state) %% get_value(y, state)
  } else if (instruction == "rcv") {
    if (length(state$signal_in) == 0) {
      state$waiting_for_signal <- TRUE
      return(state)
    }
    state[[x]] <- state$signal_in[1]
    state$signal_in <- state$signal_in[-1]
  } else if (instruction == "jgz") {
    if (get_value(x, state) > 0) {
      state$line <- state$line + get_value(y, state) - 1
    }
  }
  state$line <- state$line + 1
  state
}

solve2 <- function(df) {
  state1 <- list(
    p = 0,
    line = 1,
    signal_in = NULL,
    signal_out = NULL,
    waiting_for_signal = FALSE
  )
  state2 <- list(
    p = 1,
    line = 1,
    signal_in = NULL,
    signal_out = NULL,
    waiting_for_signal = FALSE
  )
  state2_sent <- 0
  repeat {
    state1 <- run(df, state1)
    state2$signal_in <- c(state2$signal_in, state1$signal_out)
    state1$signal_out <- NULL
    
    state2 <- run(df, state2)
    state1$signal_in <- c(state1$signal_in, state2$signal_out)
    state2_sent <- state2_sent + length(state2$signal_out)
    state2$signal_out <- NULL
    
    if (state1$waiting_for_signal && length(state1$signal_in) == 0 && state2$waiting_for_signal && length(state2$signal_in) == 0) {
      break
    }
  }
  state2_sent - length(state1$signal_in)
}

answer <- solve2(df)
answer
