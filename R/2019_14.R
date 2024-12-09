library(tidyverse)



df <-
  read_lines(input) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("lhs", "rhs")) %>%
  mutate(
    chemical_out = str_extract(rhs, "[A-Z]+$"),
    n_out = str_extract(rhs, "\\d+"),
    chemical_in = str_extract_all(lhs, "[A-Z]+"),
    n_in = str_extract_all(lhs, "\\d+")
  ) %>%
  unnest(chemical_in, n_in) %>%
  mutate(
    n_in = as.integer(n_in),
    n_out = as.integer(n_out)
  ) %>%
  select(-lhs, -rhs)
df

zero_if_invalid <- function(x) {
  if (is.null(x) || is.na(x)) return(0)
  x
}

solve <- function(df, targets = c(FUEL = 1)) {
  leftovers <- c()
  total_ore <- 0
  
  while (length(targets) > 0) {
    target_chemical <- names(targets)[1]
    target_n <- targets[1]
    targets <- targets[-1]
    recipes <- df[df$chemical_out == target_chemical,]
   
    # Take output from leftovers
    if (zero_if_invalid(leftovers[target_chemical]) > 0) {
      n_out_taken_from_leftovers <- min(leftovers[target_chemical], target_n)
      target_n <- target_n - n_out_taken_from_leftovers
      leftovers[target_chemical] <- leftovers[target_chemical] - n_out_taken_from_leftovers
    }
    if (target_n <= 0) next
    
    n_batches <- ceiling(target_n / recipes$n_out[1])
    n_out_created <- n_batches * recipes$n_out[1]
    n_out_leftover <- n_out_created - target_n
    
    # Store the leftovers from the output
    if (n_out_leftover > 0) {
      leftovers[target_chemical] <- zero_if_invalid(leftovers[target_chemical]) + n_out_leftover
    }
    
    for (i in seq_len(nrow(recipes))) {
      n_in_needed <- n_batches * recipes$n_in[i]

      # Take input from leftovers
      if (zero_if_invalid(leftovers[recipes$chemical_in[i]]) > 0) {
        n_in_taken_from_leftovers <- min(leftovers[recipes$chemical_in[i]], n_in_needed)
        n_in_needed <- n_in_needed - n_in_taken_from_leftovers
        leftovers[recipes$chemical_in[i]] <- leftovers[recipes$chemical_in[i]] - n_in_taken_from_leftovers
      }
      
      if (n_in_needed <= 0) next
      
      if (recipes$chemical_in[i] == "ORE") {
        total_ore <- total_ore + n_in_needed
        next
      }
      
      targets[recipes$chemical_in[i]] <- zero_if_invalid(targets[recipes$chemical_in[i]]) + n_in_needed
    }
  }
  unname(total_ore)
}

answer <- solve(df)
answer

target <- 1000000000000
low <- 1
high <- Inf
while (low < high - 1) {
  if (is.infinite(high)) {
    mid <- low * 10
  } else {
    mid <- floor((low + high) / 2)
  }
  
  result <- solve(df, targets = c(FUEL = mid))
  
  if (result < target) {
    low <- mid
  } else if (result > target) {
    high <- mid
  } else {
    low <- mid
    break
  }
}
answer <- low
answer
