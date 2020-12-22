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