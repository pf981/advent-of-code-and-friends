library(tidyverse)


disk_length <- 272

# 
# disk_length <- 20

x <- str_split(input, "") %>% first() %>% parse_logical()
x

grow_string <- function(x, disk_length) {
  while (length(x) < disk_length) {
    x <- c(x, 0, !rev(x))
  }
  head(x, disk_length)
}

checksum <- function(x) {
  repeat {
    x <- split(as.integer(x), (seq_along(x) - 1) %/% 2) %>% map_int(~sum(.) != 1)
    if (length(x) %% 2 == 1) {
      break
    }
  }
  str_c(x, collapse = "")
}


s <- grow_string(x, disk_length)
s %>% as.integer() %>% str_c(collapse = "")

answer <- checksum(s)
answer

s <- grow_string(x, 35651584)

answer <- checksum(s)
answer # 5 minutes
