library(tidyverse)



directions <-
  read_lines(input) %>%
  as_tibble() %>%
  extract(value, c("action", "value"), "(.)(\\d+)") %>%
  mutate(value = as.numeric(value))
directions

result <- 
  directions %>%
  mutate(
    facing = cumsum(case_when(
      action == "L" ~ value,
      action == "R" ~ -value,
      TRUE ~ 0
    )),
    delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      action == "F" ~ value * sin(facing / 180 * pi),
      TRUE ~ 0
    ),
    delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      action == "F" ~ value * cos(facing / 180 * pi),
      TRUE ~ 0
    )
  )
result

answer <- abs(sum(result$delta_north)) + abs(sum(result$delta_east))
answer

wp_changes <-
  directions %>%
  mutate(
    wp_delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      TRUE ~ 0
    ),
    wp_delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      TRUE ~ 0
    )
  ) %>% 
  add_row(wp_delta_north = 1, wp_delta_east = 10, .before = 1)
wp_changes

for (i in which(wp_changes$action %in% c("L", "R"))) {
  cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

  x <- cur_wp$wp_east
  y <- cur_wp$wp_north
  
  v <- paste0(wp_changes$action[i], wp_changes$value[i])
  if (v %in% c("L180", "R180")) {
    new_x <- -x
    new_y <- -y
  } else if (v %in% c("L270", "R90")) {
    new_x <- y
    new_y <- -x
  } else if (v %in% c("R270", "L90")) {
    new_x <- -y
    new_y <- x
  }
  
  wp_changes$wp_delta_north[i] <- new_y - y
  wp_changes$wp_delta_east[i] <- new_x - x
}

result <-
  wp_changes %>%
  mutate(
    wp_east = cumsum(wp_delta_east),
    wp_north = cumsum(wp_delta_north),
    
    ship_delta_east = case_when(
      action == "F" ~ value * wp_east,
      TRUE ~ 0
    ),
    ship_delta_north = case_when(
      action == "F" ~ value * wp_north,
      TRUE ~ 0
    ),
    
    ship_abs_east = cumsum(ship_delta_east),
    ship_abs_north = cumsum(ship_delta_north)
  )

answer <- result %>% tail(1) %>% with(abs(ship_abs_east) + abs(ship_abs_north))
answer
