library(tidyverse)



n_cards <- 10007

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    action = str_extract(line, "^\\w+"),
    value = str_extract(line, "-?\\d+") %>% parse_integer()
  )
df

deal <- function(cards, increment) {
  if (is.na(increment)) return(rev(cards))
  
  inds <- (increment * seq(from = 0, length.out = length(cards))) %% length(cards)
  cards[inds + 1] <- cards
  cards
}

cut <- function(cards, n) {
  c(tail(cards, -n), head(cards, n))
}

shuffle <- function(df, cards = seq(from = 0, length.out = n_cards)) {
  for (i in seq_len(nrow(df))) {
    f <- get(df$action[i])
    cards <- f(cards, df$value[i])
  }
  cards
}

cards <- shuffle(df)

answer <- which(cards == 2019) - 1
answer

install.packages("VeryLargeIntegers")

library(VeryLargeIntegers)

# Both 119315717514047 and 101741582076661 are prime.
n_cards <- as.vli("119315717514047")
n_shuffles <- as.vli("101741582076661")
target_position <- as.vli("2020")

get_coefs_deal <- function(n_cards, increment, coefs) {
  if (is.na(increment)) {
    coefs$a <- mulmod(coefs$a, -1, n_cards)
    coefs$b <- submod(n_cards - 1, coefs$b, n_cards)
  } else {
    coefs$a <- mulmod(coefs$a, increment, n_cards)
    coefs$b <- mulmod(coefs$b, increment, n_cards)
  }
  coefs
}

get_coefs_cut <- function(n_cards, n, coefs) {
  coefs$b <- submod(coefs$b, n, n_cards)
  coefs
}

# Find a and b such that
#     position_after_shuffle = a * position_before_shuffle + b MOD n
get_shuffle_coefficients <- function(df, n_cards) {
  # Start with identity
  coefs <- list(a = as.vli("1"), b = as.vli("0"))
  
  for (i in seq_len(nrow(df))) {
    f <- get(str_c("get_coefs_", df$action[i]))
    coefs <- f(n_cards, df$value[i], coefs)
  }
  coefs
}

# Find a and b such that
#     position_after_shuffle = a * position_before_shuffle + b MOD n
shuffle_coefs <- get_shuffle_coefficients(df, n_cards)

# Let A and B be the coefficients after 101741582076661 applications of a*x + b

# We have
#     a*x + b
# Which after one iteration, goes to
#     a*(a*x + b) + b = a^2*x + b + b*a
# After two iterations
#    a^2*(a*x + b) + b + ab = a^3*x + b + b*a + b*a^2
# After n iterations
#    a^n*x + b + b*a + b*a^2 + ... + b*a^(n-1) = A*x + B where
#    A = a^n, and
#    B = sum of i from 0 to n-1 of b*a^i
#
# B is a geometric series which can be evaluated as
#    B = b * (a^n - 1) * (a - 1)' = b*(A-1)*(a-1)'
A <- powmod(shuffle_coefs$a, n_shuffles, n_cards)
B <- mulmod(shuffle_coefs$b * (A - 1), invmod(shuffle_coefs$a - 1, n_cards), n_cards)

# We need to find x such that
#      A*x + B = 2020          MOD n
#   =>       x = A'*(2020 - B) MOD n
answer <- mulmod(invmod(A, n_cards), (2020 - B), n_cards)
answer
