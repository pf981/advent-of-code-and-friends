library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    x_start = str_extract(line, "(?<=x=)\\d+") %>% parse_integer(),
    x_end = str_extract(line, "(?<=x=\\d{1,10}\\.\\.)\\d+") %>% parse_integer(),
    y_start = str_extract(line, "(?<=y=)\\d+") %>% parse_integer(),
    y_end = str_extract(line, "(?<=y=\\d{1,10}\\.\\.)\\d+") %>% parse_integer(),
    x_end = ifelse(is.na(x_end), x_start, x_end),
    y_end = ifelse(is.na(y_end), y_start, y_end),
    x = map2(x_start, x_end, seq),
    y = map2(y_start, y_end, seq)
  ) %>%
  select(x, y) %>%
  unnest()
df

m <- matrix(".", nrow = max(df$y) + 2, ncol = max(df$x) + 2)

for (i in seq_len(nrow(df))) {
  m[df$y[i], df$x[i]] <- "#"
}
m

simulate <- function(m) {
  xs <- c(500)
  ys <- c(1)
  while (length(xs) > 0) {
    x <- xs[1]
    y <- ys[1]
    xs <- xs[-1]
    ys <- ys[-1]
    
    if (y > nrow(m) - 2) next
    
    if (!(m[y, x] %in% c("|", "."))) next
    m[y, x] <- "|"
    
    # Down
    if (m[y + 1, x] == "|") next
    if (m[y + 1, x] == ".") {
      xs <- c(xs, x)
      ys <- c(ys, y + 1)
      next
    }
    
    # Left
    xl <- x
    repeat {
      xl <- xl - 1
      if (m[y, xl] == "#") break
      m[y, xl] <- "|"
      if (m[y + 1, xl] == ".") {
        xs <- c(xs, xl)
        ys <- c(ys, y + 1)
        break
      }
    }
    
    # Right
    xr <- x
    repeat {
      xr <- xr + 1
      if (m[y, xr] == "#") break
      m[y, xr] <- "|"
      if (m[y + 1, xr] == ".") {
        xs <- c(xs, xr)
        ys <- c(ys, y + 1)
         break
      }
    }
    
    if (m[y, xl] == "#" && m[y, xr] == "#") {
      for (x in seq(from = xl + 1, to = xr - 1, by = 1)) {
        m[y, x] <- "~"
        if (y > 1 && m[y - 1, x] == "|") {
          xs <- c(xs, x)
          ys <- c(ys, y - 1)
        }
      }
    }
  }
  m
}

result <- simulate(m)

answer <- sum(result[min(df$y):max(df$y),] %in% c("|", "~"))
answer

answer <- sum(result[min(df$y):max(df$y),] == "~")
answer
