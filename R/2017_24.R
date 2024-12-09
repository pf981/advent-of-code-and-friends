library(tidyverse)



# 

df <-
  read_lines(input) %>%
  str_split("/") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("a", "b"))
df

get_strongest_bridge <- function(df, previous_port = 0) {
  strongest <- 0
  for (i in seq_len(nrow(df))) {
    if (df$a[i] == previous_port || df$b[i] == previous_port) {
      strength <- df$a[i] + df$b[i] + get_strongest_bridge(filter(df, !(a == df$a[i] & b == df$b[i])), ifelse(df$a[i] == previous_port, df$b[i], df$a[i]))
      strongest <- max(strongest, strength)
    }
  }
  strongest
}

answer <- get_strongest_bridge(df)
answer # 26 minutes

get_longest_bridge <- function(df, previous_port = 0) {
  longest_length <- 0
  longest_strength <- 0
  for (i in seq_len(nrow(df))) {
    if (df$a[i] == previous_port || df$b[i] == previous_port) {
      result <- get_longest_bridge(
        filter(df, !(a == df$a[i] & b == df$b[i])),
        ifelse(df$a[i] == previous_port, df$b[i], df$a[i])
      )
      this_strength <- df$a[i] + df$b[i] + result$longest_strength
      this_length <- result$longest_length + 1
      if (this_length > longest_length || (this_length == longest_length && this_strength > longest_strength)) {
        longest_strength <- this_strength
        longest_length<- this_length
      }
    }
  }
  lst(longest_length, longest_strength)
}

result <- get_longest_bridge(df)
answer <- result$longest_strength
answer # 29 minutes
