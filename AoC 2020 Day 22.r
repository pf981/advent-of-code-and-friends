# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/22

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Player 1:
43
36
13
11
20
25
37
38
4
18
1
8
27
23
7
22
10
5
50
40
45
26
15
32
33

Player 2:
21
29
12
28
46
9
44
6
16
39
19
24
17
14
47
48
42
34
31
3
41
35
2
30
49
"

# COMMAND ----------

# input <- "Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10
# "

# COMMAND ----------

# input <- "Player 1:
# 43
# 19

# Player 2:
# 2
# 29
# 14
# "

# COMMAND ----------

players <-
  input %>%
  str_split("\n\n") %>%
  unlist() %>%
  map(~read_lines(.) %>% tail(-1) %>% parse_integer())
players

# COMMAND ----------

print_round <- function(player1, player2, round) {
  message(glue::glue("-- Round {round} --
Player 1's deck: {str_c(player1, collapse = ', ')}
Player 2's deck: {str_c(player2, collapse = ', ')}
Player 1 plays: {player1[1]}
Player 2 plays: {player2[1]}
Player {which.max(c(player1[1], player2[1]))} wins the round!

"))
}

# COMMAND ----------

player1 <- players[[1]]
player2 <- players[[2]]

round <- 0

while (length(player1) > 0 && length(player2) > 0) {
  round <- round + 1
  print_round(player1, player2, round)
  
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

# COMMAND ----------

enframe(rev(c(player1, player2))) %>%
  summarise(result = sum(name * value)) %>%
  pull(result)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

recursive_combat <- function(player1, player2, game = 1) {
  round <- 0
  seen1 <- NULL
  seen2 <- NULL
  while (length(player1) > 0 && length(player2) > 0) {
    round <- round + 1
    
    message(glue::glue("-- Round {round} (Game {game}) --
Player 1's deck: {str_c(player1, collapse = ', ')}
Player 2's deck: {str_c(player2, collapse = ', ')}
Player 1 plays: {player1[1]}
Player 2 plays: {player2[1]}
"))
    
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
            
    message(glue::glue("Player {winner} wins the round!\n\n"))
  }
  
  lst(
    cards = c(player1, player2),
    winner = ifelse(length(player1) == 0, 2, 1)
  )
}

# COMMAND ----------

result <- recursive_combat(players[[1]], players[[2]])
result

# COMMAND ----------

enframe(rev(result$cards)) %>%
  summarise(answer = sum(name * value)) %>%
  pull(answer)

# COMMAND ----------

# player1 <- c(9, 2, 6, 3, 1)
# player2 <- c(5, 8, 4, 7, 10)

# recursive_combat(player1, player2)

# COMMAND ----------

# player1 <- c(43, 19)
# player2 <- c(2, 29, 14)

# recursive_combat(player1, player2)