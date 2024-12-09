library(tidyverse)



for (answer in seq_len(10000000)) {
  if (str_starts(digest::digest(str_c(input, answer), serialize = FALSE), "00000")) {
    break
  }
}
answer

for (answer in seq(from = 282749, to = 10000000)) {
  if (str_starts(digest::digest(str_c(input, answer), serialize = FALSE), "000000")) {
    break
  }
}
answer
