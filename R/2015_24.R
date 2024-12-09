library(tidyverse)



packages <- read_lines(input) %>% parse_number()

create_groups <- function(nums, target = sum(nums / 3), previous_nums = NULL) {
  if (target == 0) {
    return(list(previous_nums))
  }
  
  if (target < 0 || length(nums) == 0) {
    return(list())
  }
  
  all_groups <- list()
  for (i in seq_along(nums)) {
    cur_groups <- create_groups(
      nums = nums[seq_along(nums) > i],
      target = target - nums[[i]],
      previous_nums = c(previous_nums, nums[[i]])
    )
    all_groups <- c(all_groups, cur_groups)
  }
  all_groups
}

possible_groups <-
  create_groups(packages) %>% # 3 minutes
  {.[order(map_dbl(., length), map_dbl(., prod))]}
length(possible_groups)

find_group_combination <- function(possible_groups) {
  for (group1 in possible_groups) {
    for (group2 in discard(possible_groups, ~any(. %in% group1))) {
      if (any(!map_lgl(possible_groups, ~any(. %in% c(group1, group2))))) {
        return(lst(
          group1,
          group2
        ))
      }
    }
  }
}

result <- find_group_combination(possible_groups)
result

answer <- prod(result$group1)
answer

possible_groups <-
  create_groups(packages, sum(packages) / 4) %>% # 3 minutes
  {.[order(map_dbl(., length), map_dbl(., prod))]}
length(possible_groups)

find_group_combination <- function(possible_groups) {
  for (group1 in possible_groups) {
    for (group2 in discard(possible_groups, ~any(. %in% group1))) {
      for (group3 in discard(possible_groups, ~any(. %in% c(group1, group2)))) {
        if (any(!map_lgl(possible_groups, ~any(. %in% c(group1, group2, group3))))) {
          return(lst(
            group1,
            group2,
            group3
          ))
        }
      }
    }
  }
}

result <- find_group_combination(possible_groups)
result

answer <- prod(result$group1)
answer
