library(tidyverse)



target_row <- str_extract(input, "(?<=row )\\d+") %>% parse_integer()
target_column <- str_extract(input, "(?<=column )\\d+") %>% parse_integer()

lst(target_row, target_column)

code <- 20151125
row <- 1
column <- 1
lowest_row <- 1

while (!(row == target_row && column == target_column)) {
  code <- (code * 252533) %% 33554393
  if (row == 1) {
    lowest_row <- lowest_row + 1
    row <- lowest_row
    column = 1
  } else {
    row <- row - 1
    column <- column + 1
  }
}

answer <- code
answer

# No puzzle here - just need all the stars
