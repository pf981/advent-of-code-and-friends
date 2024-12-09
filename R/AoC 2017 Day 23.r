library(tidyverse)



df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    x = str_split(line, " ")
  ) %>%
  unnest_wider(x) %>%
  rename(
    instruction = ...1,
    x = ...2,
    y = ...3
  )
df

get_value <- function(x, state) {
  if (!is.na(as.integer(x))) {
    return(as.integer(x))
  }
  c(state[[x]], 0)[1]
}

count_mul <- function(df) {
  sound <- 0
  state <- list()
  i <- 1
  mul_count <- 0
  repeat {
    if (i > nrow(df)) break;
    instruction <- df$instruction[i]
    x <- df$x[i]
    y <- df$y[i]

    if (instruction == "set") {
      state[[x]] <- get_value(y, state)
    } else if (instruction == "sub") {
      state[[x]] <- get_value(x, state) - get_value(y, state)
    } else if (instruction == "mul") {
      state[[x]] <- get_value(x, state) * get_value(y, state)
      mul_count <- mul_count + 1
    } else if (instruction == "jnz") {
      if (get_value(x, state) != 0) {
        i <- i + get_value(y, state) - 1
      }
    }
    i <- i + 1
  }
  mul_count
}

answer <- count_mul(df)
answer

"
a = 1
b = 84                   # set b 84
c = b                    # set c b
if (a != 0) {            # jnz a 2
                         # jnz 1 5
  b = b * 100 + 100000   # mul b 100
                         # sub b -100000
  c = b + 17000          # set c b
                         # sub c -17000
}
repeat {
  f = 1                  # set f 1
  d = 2                  # set d 2
  do {
    e = 2                # set e 2
    do {
      g = d              # set g d
      g *= e             # mul g e
      g -= b             # sub g b
      if (g == 0) {      # jnz g 2
        f = 0            # set f 0
      }
      --e                # sub e -1
      g = e              # set g e
      g -= b             # sub g b
    } while (g != 0)     # jnz g -8
    --d                  # sub d -1
    g = d                # set g d
    g -= b               # sub g b
  } while (g != 0)       # jnz g -13
  if (f != 0) {          # jnz f 2
    ++h                  # sub h -1
  }
  g = b                  # set g b
  g -= c                 # sub g c
  if (g != 0) {          # jnz g 2
    return               # jnz 1 3
  }           
  b += 17                # sub b -17
}                        # jnz 1 -23
"

b <- 84 * 100 + 100000
h <- 0
.c <- b + 17000
repeat {
  if (!RcppAlgos::isPrimeRcpp(b)) {
    h <- h + 1
  }
  if (b == .c) break
  b <- b + 17
}
answer <- h
answer
