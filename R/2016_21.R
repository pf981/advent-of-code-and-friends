library(tidyverse)



# 

swap_position <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  x_value <- str_sub(s, x, x)
  str_sub(s, x, x) <- str_sub(s, y, y)
  str_sub(s, y, y) <- x_value
  s
}

swap_letter <- function(s, x, y) {
  s <- str_replace_all(s, x, "X")
  s <- str_replace_all(s, y, x)
  s <- str_replace_all(s, "X", y)
  s
}

rotate_dir <- function(s, x, y) {
  direction <- x
  x <- y
  
  x <- as.integer(x)
  if (direction == "right") {
    x <- str_length(s) - x
  }
  
  str_c(
    str_sub(s, x + 1),
    str_sub(s, 1, x)
  )
}

rotate_pos <- function(s, x, y) {
  d <- str_locate(s, x) %>% first()
  d <- d - 1
  
  if (d >= 4) {
    d <- d + 1
  }
  d <- d + 1
  if (d > str_length(s)) {
    d <- d - str_length(s)
  }
  rotate_dir(s, "right", d)
}

reverse <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  str_sub(s, x, y) <- stringi::stri_reverse(str_sub(s, x, y))
  s
}

move <- function(s, x, y) {
  x <- as.integer(x) + 1
  y <- as.integer(y) + 1
  
  letter <- str_sub(s, x, x)
  str_sub(s, x, x) <- ""
  str_sub(s, y, y) <- str_c(letter, str_sub(s, y, y))
  s
}

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    instruction = str_extract(line, "^\\w+"),
    instruction = case_when(
        str_detect(line, "swap position") ~ "swap_position",
        str_detect(line, "swap letter") ~ "swap_letter",
        str_detect(line, "rotate based") ~ "rotate_pos",
        instruction == "rotate" ~ "rotate_dir",
        TRUE ~ instruction
    ),
    params = str_extract_all(line, "left|right|(?<=[^\\w])\\w(?=[^\\w]|$)"),
    f = map(instruction, get)
  ) %>%
  unnest_wider(params) %>%
  rename(x = `...1`, y = `...2`)
df

answer <- "abcdefgh"

for (i in seq_len(nrow(df))) {
  answer <- with(df[i,], f[[1]](answer, x, y))
}
answer

reverse_f <- function(s, f_str, x, y) {
  f <- get(f_str)
  if (f_str %in% c("swap_position", "swap_letter", "reverse")){
    return(f(s, x, y))
  }
  if (f_str == "rotate_dir") {
    rotate_dir(s, ifelse(x == "right", "left", "right"), y)
  }
  
  candidate <- s
  repeat {
    if (f(candidate, x, y) == s) return(candidate)
    candidate <- stringi::stri_rand_shuffle(candidate)
  }
}

answer <- "fbgdceah"

for (i in rev(seq_len(nrow(df)))) {
  f <- df$instruction[i]
  x <- df$x[i]
  y <- df$y[i]
  
  answer <- reverse_f(answer, f, x, y)
}
answer
