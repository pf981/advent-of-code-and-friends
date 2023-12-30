library(tidyverse)


text <- read_lines("data/2023-09.txt")




extrapolate <- function(sequence) {
  if (all(sequence == 0)) return(0)
  
  deltas <- tail(sequence, -1) - head(sequence, -1)
  tail(sequence, 1) + extrapolate(deltas)
}

sequences <- str_extract_all(text, "-?\\d+") |> map(as.integer)
answer1 = sum(map_int(sequences, extrapolate))
print(answer1)




answer2 = sum(map_int(sequences, \(.) extrapolate(rev(.))))
print(answer2)
