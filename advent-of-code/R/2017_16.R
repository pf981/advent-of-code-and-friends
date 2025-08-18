library(tidyverse)



df <-
  str_split(input, ",") %>%
  first() %>%
  enframe() %>%
  mutate(
    instruction = str_extract(value, "^."),
    a = str_extract(value, "(?<=^.).+(?=/)|(?<=^s).+"),
    b = str_extract(value, "(?<=/).+")
  )
df

start_letters <- head(letters, 16)

dance <- function(v = start_letters) {
  for (i in seq_len(nrow(df))) {
    instruction = df$instruction[i]
    a = df$a[i]
    b = df$b[i]

    if (instruction == "s") {
      x <- as.integer(a)
      v <- c(tail(v, x), head(v, -x))
    } else if (instruction == "x") {
      a <- as.integer(a) + 1
      b <- as.integer(b) + 1
      va <- v[a]
      v[a] <- v[b]
      v[b] <- va
    } else if (instruction == "p") {
      a <- which(v == a)
      b <- which(v == b)
      va <- v[a]
      v[a] <- v[b]
      v[b] <- va
    }
  }
  v
}

answer <- dance() %>% str_c(collapse = "")
answer

v_strs <- c()
v <- start_letters
v_str <- str_c(v, collapse = "")
while (!(v_str %in% v_strs)) {
  v_strs <- c(v_strs, v_str)
  v <- dance(v)
  v_str <- str_c(v, collapse = "")
}
length(v_strs)

answer <- v_strs[(1000000 %% length(v_strs)) + 1]
answer
