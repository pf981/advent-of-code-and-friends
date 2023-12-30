library(tidyverse)


text <- read_lines("data/2023-06.txt")




count_ways <- function(T, D) {
    upper <- (-T - sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    lower <- (-T + sqrt(T ** 2 - 4 * (-1) * (-D))) / 2 * (-1)
    ceiling(upper) - floor(lower) - 1
}

nums <- text |> str_extract_all("\\d+") |> map(as.integer)
answer1 <- prod(count_ways(nums[[1]], nums[[2]]))
print(answer1)




nums <- nums |> map(str_c, collapse = "") |> as.numeric()
answer2 <- count_ways(nums[[1]], nums[[2]])
print(answer2)
