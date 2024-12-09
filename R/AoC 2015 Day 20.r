library(tidyverse)

input <- 34000000

presents <- integer(input / 10)

for (elf in seq_along(presents)) {
  houses <- seq_len(length(presents) / elf) * elf
  presents[houses] <- presents[houses] + elf * 10
}

answer <- which(presents >= input) %>% min()
answer

presents <- integer(input / 10)

for (elf in seq_along(presents)) {
  houses <- seq_len(50) * elf
  houses <- houses[houses <= length(presents)]
  presents[houses] <- presents[houses] + elf * 11
}

answer <- which(presents >= input) %>% min()
answer
