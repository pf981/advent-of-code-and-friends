library(tidyverse)



answer <- str_count(input, fixed("(")) - str_count(input, fixed(")"))
answer

answer <- which(cumsum(ifelse(str_split(input, "")[[1]] == "(", 1, -1)) == -1)
answer[[1]]
