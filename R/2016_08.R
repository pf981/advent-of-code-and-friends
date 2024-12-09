library(tidyverse)



n_rows <- 6
n_cols <- 50

rect <- function(m, row, col, by) {
  m[seq_len(row), seq_len(col)] <- TRUE
  m
}

r <- function(x, by) {
  by <- by %% length(x)
  if (by == 0) return(x)
  c(tail(x, by), head(x, -by))
}

rotate <- function(m, row, col, by) {
  row2 <- row
  col2 <- col
  if (is.na(row)) {
    row <- seq_len(nrow(m))
    row2 <- r(row, by)
  }  
  if (is.na(col)) {
    col <- seq_len(ncol(m))
    col2 <- r(col, by)
  }
  
  m[row, col] <- m[row2, col2]

  m
}

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    operation = str_extract(line, "^\\w+"),
    row = coalesce(str_extract(line, "(?<=x)\\d+"),str_extract(line, "(?<=y=)\\d+")) %>% parse_integer(),
    col = coalesce(str_extract(line, "\\d+(?=x)"), str_extract(line, "(?<=x=)\\d+")) %>% parse_integer(),
    row = ifelse(operation == "rect", row, row + 1),
    col = ifelse(operation == "rect", col, col + 1),
    by = str_extract(line, "\\d+$") %>% parse_integer(),
    f = map(operation, get)
  )
df

m <- matrix(FALSE, nrow = n_rows, ncol = n_cols)
for (i in seq_len(nrow(df))) {
  m <- with(df[i,], f[[1]](m, row, col, by))
}
m

answer <- sum(m)
answer

asplit(m, 1) %>%
  map_chr(~ifelse(., "X", " ") %>% str_c(collapse = ""))

answer <- "CFLELOYFCS"
answer
