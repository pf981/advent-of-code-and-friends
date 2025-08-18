library(tidyverse)


text <- read_lines("data/2023-09.txt")




extrapolate <- function(sequence) {
  if (all(sequence == 0)) return(0)
  
  deltas <- tail(sequence, -1) - head(sequence, -1)
  tail(sequence, 1) + extrapolate(deltas)
}

sequences <- str_extract_all(text, "-?\\d+") |> map(as.integer)
answer1 = sequences |> map_int(extrapolate) |> sum()
print(answer1)




answer2 = sequences |> map(rev) |> map_int(extrapolate) |> sum()
print(answer2)
