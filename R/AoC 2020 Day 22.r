library(tidyverse)



players <-
  input %>%
  str_split("\n\n") %>%
  unlist() %>%
  map(~read_lines(.) %>% tail(-1) %>% parse_integer())
players

player1 <- players[[1]]
player2 <- players[[2]]

round <- 0

while (length(player1) > 0 && length(player2) > 0) {
  round <- round + 1
  
  plays <- c(player1[1], player2[1])
  player1 <- tail(player1, -1)
  player2 <- tail(player2, -1)
  if (plays[1] > plays[2]) {
    player1 <- c(player1, sort.int(plays, decreasing = TRUE))
  } else {
    player2 <- c(player2, sort.int(plays, decreasing = TRUE))
  }
}
lst(player1, player2)

answer <-
  enframe(rev(c(player1, player2))) %>%
  summarise(result = sum(name * value)) %>%
  pull(result)
answer

recursive_combat <- function(player1, player2, game = 1) {
  round <- 0
  seen1 <- NULL
  seen2 <- NULL
  while (length(player1) > 0 && length(player2) > 0) {
    round <- round + 1
    
    # Check if state has been seen before
    new_seen1 <- str_c(player1, collapse = ",")
    new_seen2 <- str_c(player2, collapse = ",")
    if (new_seen1 %in% seen1 || new_seen2 %in% seen2) {
      return(lst(cards = player1, winner = 1))
    }
    seen1 <- c(seen1, new_seen1)
    seen2 <- c(seen2, new_seen2)

    # Draw the first card
    draw1 <- player1[1]
    draw2 <- player2[1]  
    player1 <- tail(player1, -1)
    player2 <- tail(player2, -1)
    
    sub1 <- head(player1, draw1)
    sub2 <- head(player2, draw2)

    if (length(sub1) == draw1 && length(sub2) == draw2) {
      winner <- recursive_combat(sub1, sub2)$winner
    } else {
      winner <- which.max(c(draw1, draw2))
    }
    
    if (winner == 1) {
      player1 <- c(player1, draw1, draw2)
    } else {
      player2 <- c(player2, draw2, draw1)
    }
  }
  
  lst(
    cards = c(player1, player2),
    winner = ifelse(length(player1) == 0, 2, 1)
  )
}

result <- recursive_combat(players[[1]], players[[2]])
result

answer <-
  enframe(rev(result$cards)) %>%
  summarise(answer = sum(name * value)) %>%
  pull(answer)
answer
