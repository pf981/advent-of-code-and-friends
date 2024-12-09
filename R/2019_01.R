library(tidyverse)



modules <- 
  input %>%
  read_table(col_names = FALSE) %>%
  pull()

answer <- sum(modules %/% 3 - 2)
answer

calc_fuel <- function(module) {
  module %/% 3 - 2
}

calc_fuel_full <- function(module) {
  total_fuel <- 0
  fuel <- calc_fuel(module)
  while (fuel > 0) {
    total_fuel <- total_fuel + fuel
    fuel <- calc_fuel(fuel)
  }
  as.integer(total_fuel)
}

answer <-
  modules %>%
  map_int(calc_fuel_full) %>%
  sum()
answer
