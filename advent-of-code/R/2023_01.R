library(tidyverse)


text <- read_lines("data/2023-01.txt")


get_calibration_value <- function(text, regex, replacement = c("x" = "x")) {
  lookahead_pattern <- str_c("(?=(", regex, "))")
  
  text |>
    str_match_all(lookahead_pattern) |>
    map_chr(\(.) str_c(first(.[,2]), last(.[,2]))) |>
    str_replace_all(replacement) |>
    as.integer()
}




answer1 <- get_calibration_value(text, "\\d") |> sum()
print(answer1)




spelling <- c("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
regex <- str_c("\\d|", str_c(spelling, collapse="|"))
replacement <- seq_along(spelling) |> as.character() |> set_names(spelling)

answer2 <- get_calibration_value(text, regex, replacement) |> sum()
print(answer2)
