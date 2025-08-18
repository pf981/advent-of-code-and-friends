library(tidyverse)



df <-
  read_lines(input) %>%
  str_extract_all("(?<=tep ).") %>%
  map_dfr(set_names, c("step", "depends_on"))
df

steps <- df %>% unlist() %>% unique() %>% sort()
steps

solve <- function(steps_remaining = steps) {
  if (length(steps_remaining) == 1) return(steps_remaining)
  
  for (s in steps_remaining) {
    if (nrow(filter(df, depends_on == s, step %in% steps_remaining)) > 0) next
    solution <- str_c(s, solve(steps_remaining[steps_remaining != s]))
    if (!is.na(solution)) return(solution)
  }
  NA
}

answer <- solve()
answer

solve2 <- function(max_workers = 5, step_time_base = 60) {
  t <- 0
  time_remaining <- seq_along(steps) %>% set_names(steps) %>% `+`(step_time_base)
  workers <- rep(NA, max_workers)
  repeat {
    unavailable_steps <- c(
      df %>% filter(step %in% steps[time_remaining > 0]) %>% pull(depends_on),
      steps[time_remaining == 0]
    )
   
    # Assign workers
    workers[workers %in% unavailable_steps] <- NA
    unavailable_steps <- c(unavailable_steps, workers[!is.na(workers)])
    available_steps <- steps[!(steps %in% unavailable_steps)]
    available_workers <- which(is.na(workers))
    for (s in available_steps) {
      if (length(available_workers) == 0) break
      
      workers[available_workers[1]] <- s
      available_workers <- available_workers[-1]
    }
    
    # Update time remaining
    for (w in workers[!is.na(workers)]) {
      # message(glue::glue("Time {t}: Worker on {w}"))
      time_remaining[steps == w] <- time_remaining[steps == w] - 1
    }
    
    t <- t + 1
    if (sum(time_remaining) == 0) return(t)
  }
}

answer <- solve2()
answer
