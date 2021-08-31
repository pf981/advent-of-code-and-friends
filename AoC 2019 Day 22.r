# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Slam Shuffle ---</h2><p>There isn't much to do while you wait for the droids to repair your ship.  At least you're drifting in the right direction.  You decide to practice a new <a href="https://en.wikipedia.org/wiki/Shuffling">card shuffle</a> you've been working on.</p>
# MAGIC <p>Digging through the ship's storage, you find a deck of <em>space cards</em>! Just like <span title="What do you mean, you've never heard of space cards? They're all the rage in Zozo.">any deck of space cards</span>, there are 10007 cards in the deck numbered <code>0</code> through <code>10006</code>. The deck must be new - they're still in <em>factory order</em>, with <code>0</code> on the top, then <code>1</code>, then <code>2</code>, and so on, all the way through to <code>10006</code> on the bottom.</p>
# MAGIC <p>You've been practicing three different <em>techniques</em> that you use while shuffling. Suppose you have a deck of only 10 cards (numbered <code>0</code> through <code>9</code>):</p>
# MAGIC <p><em>To <code>deal into new stack</code></em>, create a new stack of cards by dealing the top card of the deck onto the top of the new stack repeatedly until you run out of cards:</p>
# MAGIC <pre><code>Top          Bottom
# MAGIC 0 1 2 3 4 5 6 7 8 9   Your deck
# MAGIC                       New stack
# MAGIC 
# MAGIC   1 2 3 4 5 6 7 8 9   Your deck
# MAGIC                   0   New stack
# MAGIC 
# MAGIC     2 3 4 5 6 7 8 9   Your deck
# MAGIC                 1 0   New stack
# MAGIC 
# MAGIC       3 4 5 6 7 8 9   Your deck
# MAGIC               2 1 0   New stack
# MAGIC 
# MAGIC Several steps later...
# MAGIC 
# MAGIC                   9   Your deck
# MAGIC   8 7 6 5 4 3 2 1 0   New stack
# MAGIC 
# MAGIC                       Your deck
# MAGIC 9 8 7 6 5 4 3 2 1 0   New stack
# MAGIC </code></pre>
# MAGIC <p>Finally, pick up the new stack you've just created and use it as the deck for the next technique.</p>
# MAGIC <p><em>To <code>cut N</code> cards</em>, take the top <code>N</code> cards off the top of the deck and move them as a single unit to the bottom of the deck, retaining their order. For example, to <code>cut 3</code>:</p>
# MAGIC <pre><code>Top          Bottom
# MAGIC 0 1 2 3 4 5 6 7 8 9   Your deck
# MAGIC 
# MAGIC       3 4 5 6 7 8 9   Your deck
# MAGIC 0 1 2                 Cut cards
# MAGIC 
# MAGIC 3 4 5 6 7 8 9         Your deck
# MAGIC               0 1 2   Cut cards
# MAGIC 
# MAGIC 3 4 5 6 7 8 9 0 1 2   Your deck
# MAGIC </code></pre>
# MAGIC <p>You've also been getting pretty good at a version of this technique where <code>N</code> is negative! In that case, cut (the absolute value of) <code>N</code> cards from the bottom of the deck onto the top.  For example, to <code>cut -4</code>:</p>
# MAGIC <pre><code>Top          Bottom
# MAGIC 0 1 2 3 4 5 6 7 8 9   Your deck
# MAGIC 
# MAGIC 0 1 2 3 4 5           Your deck
# MAGIC             6 7 8 9   Cut cards
# MAGIC 
# MAGIC         0 1 2 3 4 5   Your deck
# MAGIC 6 7 8 9               Cut cards
# MAGIC 
# MAGIC 6 7 8 9 0 1 2 3 4 5   Your deck
# MAGIC </code></pre>
# MAGIC <p><em>To <code>deal with increment N</code></em>, start by clearing enough space on your table to lay out all of the cards individually in a long line.  Deal the top card into the leftmost position. Then, move <code>N</code> positions to the right and deal the next card there. If you would move into a position past the end of the space on your table, wrap around and keep counting from the leftmost card again.  Continue this process until you run out of cards.</p>
# MAGIC <p>For example, to <code>deal with increment 3</code>:</p>
# MAGIC <pre><code>
# MAGIC 0 1 2 3 4 5 6 7 8 9   Your deck
# MAGIC . . . . . . . . . .   Space on table
# MAGIC ^                     Current position
# MAGIC 
# MAGIC Deal the top card to the current position:
# MAGIC 
# MAGIC   1 2 3 4 5 6 7 8 9   Your deck
# MAGIC 0 . . . . . . . . .   Space on table
# MAGIC ^                     Current position
# MAGIC 
# MAGIC Move the current position right 3:
# MAGIC 
# MAGIC   1 2 3 4 5 6 7 8 9   Your deck
# MAGIC 0 . . . . . . . . .   Space on table
# MAGIC       ^               Current position
# MAGIC 
# MAGIC Deal the top card:
# MAGIC 
# MAGIC     2 3 4 5 6 7 8 9   Your deck
# MAGIC 0 . . 1 . . . . . .   Space on table
# MAGIC       ^               Current position
# MAGIC 
# MAGIC Move right 3 and deal:
# MAGIC 
# MAGIC       3 4 5 6 7 8 9   Your deck
# MAGIC 0 . . 1 . . 2 . . .   Space on table
# MAGIC             ^         Current position
# MAGIC 
# MAGIC Move right 3 and deal:
# MAGIC 
# MAGIC         4 5 6 7 8 9   Your deck
# MAGIC 0 . . 1 . . 2 . . 3   Space on table
# MAGIC                   ^   Current position
# MAGIC 
# MAGIC Move right 3, wrapping around, and deal:
# MAGIC 
# MAGIC           5 6 7 8 9   Your deck
# MAGIC 0 . 4 1 . . 2 . . 3   Space on table
# MAGIC     ^                 Current position
# MAGIC 
# MAGIC And so on:
# MAGIC 
# MAGIC 0 7 4 1 8 5 2 9 6 3   Space on table
# MAGIC </code></pre>
# MAGIC <p>Positions on the table which already contain cards are still counted; they're not skipped.  Of course, this technique is carefully designed so it will never put two cards in the same position or leave a position empty.</p>
# MAGIC <p>Finally, collect the cards on the table so that the leftmost card ends up at the top of your deck, the card to its right ends up just below the top card, and so on, until the rightmost card ends up at the bottom of the deck.</p>
# MAGIC <p>The complete shuffle process (your puzzle input) consists of applying many of these techniques.  Here are some examples that combine techniques; they all start with a <em>factory order</em> deck of 10 cards:</p>
# MAGIC <pre><code>deal with increment 7
# MAGIC deal into new stack
# MAGIC deal into new stack
# MAGIC Result: 0 3 6 9 2 5 8 1 4 7
# MAGIC </code></pre>
# MAGIC <pre><code>cut 6
# MAGIC deal with increment 7
# MAGIC deal into new stack
# MAGIC Result: 3 0 7 4 1 8 5 2 9 6
# MAGIC </code></pre>
# MAGIC <pre><code>deal with increment 7
# MAGIC deal with increment 9
# MAGIC cut -2
# MAGIC Result: 6 3 0 7 4 1 8 5 2 9
# MAGIC </code></pre>
# MAGIC <pre><code>deal into new stack
# MAGIC cut -2
# MAGIC deal with increment 7
# MAGIC cut 8
# MAGIC cut -4
# MAGIC deal with increment 7
# MAGIC cut 3
# MAGIC deal with increment 9
# MAGIC deal with increment 3
# MAGIC cut -1
# MAGIC Result: 9 2 5 8 1 4 7 0 3 6
# MAGIC </code></pre>
# MAGIC <p>Positions within the deck count from <code>0</code> at the top, then <code>1</code> for the card immediately below the top card, and so on to the bottom.  (That is, cards start in the position matching their number.)</p>
# MAGIC <p>After shuffling your <em>factory order</em> deck of 10007 cards, <em>what is the position of card <code>2019</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "cut -7812
deal with increment 55
cut -3909
deal with increment 51
deal into new stack
deal with increment 4
cut -77
deal with increment 26
deal into new stack
deal with increment 36
cut 5266
deal with increment 20
cut 8726
deal with increment 22
cut 4380
deal into new stack
cut 3342
deal with increment 16
cut -2237
deal into new stack
deal with increment 20
cut 7066
deal with increment 18
cut 5979
deal with increment 9
cut 2219
deal with increment 44
cut 7341
deal with increment 10
cut -6719
deal with increment 42
deal into new stack
cut -2135
deal with increment 75
cut 5967
deal into new stack
cut 6401
deal with increment 39
deal into new stack
deal with increment 56
cut 7735
deal with increment 49
cut -6350
deal with increment 50
deal into new stack
deal with increment 72
deal into new stack
cut 776
deal into new stack
deal with increment 18
cut 9619
deal with increment 9
deal into new stack
cut 5343
deal into new stack
cut 9562
deal with increment 65
cut 4499
deal with increment 58
cut -4850
deal into new stack
cut -9417
deal into new stack
deal with increment 33
cut 2763
deal with increment 61
cut 7377
deal with increment 27
cut 895
deal into new stack
deal with increment 41
cut -1207
deal with increment 22
cut -7401
deal with increment 48
cut 5776
deal with increment 3
cut 2097
deal with increment 49
cut -8098
deal with increment 68
cut 2296
deal with increment 35
cut -4471
deal with increment 56
cut -2778
deal with increment 5
cut -6386
deal with increment 54
cut -7411
deal with increment 20
cut -4222
deal into new stack
cut -5236
deal with increment 64
cut -3581
deal with increment 11
cut 3255
deal with increment 20
cut -5914
"

# COMMAND ----------

n_cards <- 10007

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    action = str_extract(line, "^\\w+"),
    value = str_extract(line, "-?\\d+") %>% parse_integer()
  )
df

# COMMAND ----------

deal <- function(cards, increment) {
  if (is.na(increment)) return(rev(cards))
  
  inds <- (increment * seq(from = 0, length.out = length(cards))) %% length(cards)
  cards[inds + 1] <- cards
  cards
}

cut <- function(cards, n) {
  c(tail(cards, -n), head(cards, n))
}

# COMMAND ----------

shuffle <- function(df, cards = seq(from = 0, length.out = n_cards)) {
  for (i in seq_len(nrow(df))) {
    f <- get(df$action[i])
    cards <- f(cards, df$value[i])
  }
  cards
}

cards <- shuffle(df)

# COMMAND ----------

answer <- which(cards == 2019) - 1
answer

# COMMAND ----------

# MAGIC %md ## Start test

# COMMAND ----------

n_cards <- 10007
shuffle_coefs <- get_shuffle_coefficients(df, n_cards)

A <- modular_exponentiation(shuffle_coefs$a, 1, n_cards)
B <- (shuffle_coefs$b * (A - 1) * inverse(shuffle_coefs$a - 1)) %% n_cards

# COMMAND ----------

(shuffle_coefs$a * 2019 + shuffle_coefs$b) %% n_cards # Expect 4775

# COMMAND ----------

(A * 2019 + B) %% n_cards # Expect 4775

# COMMAND ----------

(inverse(A) * (4775 - B)) %% n_cards # Expect 2019

# COMMAND ----------

# MAGIC %md ## End test

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After a while, you realize your shuffling skill won't improve much more with merely a single deck of cards.  You ask every 3D printer on the ship to make you some more cards while you check on the ship repairs.  While reviewing the work the droids have finished so far, you think you see <a href="https://en.wikipedia.org/wiki/Halley%27s_Comet">Halley's Comet</a> fly past!</p>
# MAGIC <p>When you get back, you discover that the 3D printers have combined their power to create for you a single, giant, brand new, <em>factory order</em> deck of <em><code>119315717514047</code> space cards</em>.</p>
# MAGIC <p>Finally, a deck of cards worthy of shuffling!</p>
# MAGIC <p>You decide to apply your complete shuffle process (your puzzle input) to the deck <em><code>101741582076661</code> times in a row</em>.</p>
# MAGIC <p>You'll need to be careful, though - one wrong move with this many cards and you might <em>overflow</em> your entire ship!</p>
# MAGIC <p>After shuffling your new, giant, <em>factory order</em> deck that many times, <em>what number is on the card that ends up in position <code>2020</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(VeryLargeIntegers)

# COMMAND ----------

# Both 119315717514047 and 101741582076661 are prime.
n_cards <- as.vli("119315717514047")
n_shuffles <- as.vli("101741582076661")
target_position <- as.vli("2020")

# COMMAND ----------

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
#   position_after_shuffle = a * position_before_shuffle + b MOD n
get_shuffle_coefficients <- function(df, n_cards) {
  # Start with identity
  coefs <- list(a = as.vli("1"), b = as.vli("0"))
  
  for (i in seq_len(nrow(df))) {
    f <- get(str_c("get_coefs_", df$action[i]))
    coefs <- f(n_cards, df$value[i], coefs)
  }
  coefs
}

# COMMAND ----------

shuffle_coefs <- get_shuffle_coefficients(df, n_cards)
A <- powmod(shuffle_coefs$a, n_shuffles, n_cards)

B <- mulmod(shuffle_coefs$b * (A - 1), invmod(shuffle_coefs$a - 1, n_cards), n_cards)
# answer <- mulmod(invmod(A, n_cards), (2020 - B), n_cards)
# answer

# COMMAND ----------

shuffle_coefs <- get_shuffle_coefficients(df, n_cards)

# A and B are the coefficients after 101741582076661 applications of a*x + b

# We have
#   a*x + b
# Which after one iteration, goes to
#   a*(a*x + b) + b = a^2*x + b + b*a
# After two iterations
#  a^2*(a*x + b) + b + ab = a^3*x + b + b*a + b*a^2
# After n iterations
#  a^n*x + b + b*a + b*a^2 + ... + b*a^(n-1) = A*x + B where A = a^n and B = sum of i from 0 to n-1 of b*a^i
#
# B is a geometric series which can be evaluated as
#  b * (a^n - 1) * (a - 1)' = b*(A-1)*(a-1)'
#
# n is prime so we can invert any number, k, from Fermat's Little Theorem
#       k^(n-1) = 1       MOD n
#  => k*k^(n-2) = 1       MOD n 
#  =>        k' = k^(n-2) MOD n
A <- powmod(shuffle_coefs$a, n_shuffles, n_cards)
B <- mulmod(shuffle_coefs$b * (A - 1), invmod(shuffle_coefs$a - 1, n_cards), n_cards)

# We need to find x such that
#      A*x + B = 2020          MOD n
#   =>       x = A'*(2020 - B) MOD n
answer <- mulmod(invmod(A, n_cards), (2020 - B), n_cards)
answer

# COMMAND ----------

VeryLargeIntegers::

# COMMAND ----------

lst(
  invmod(shuffle_coefs$a %>% format(scientific = FALSE) %>% as.vli(), n_cards),
  powmod(shuffle_coefs$a %>% format(scientific = FALSE) %>% as.vli(), n_cards - 2, n_cards)
)

# COMMAND ----------

# MAGIC %md ## Old

# COMMAND ----------

get_coefs_deal <- function(n_cards, increment, coefs) {
  if (is.na(increment)) {
    coefs$a <- (-coefs$a) %% n_cards
    coefs$b <- (n_cards - 1 - coefs$b) %% n_cards
  } else {
    coefs$a <- (coefs$a * increment) %% n_cards
    coefs$b <- (coefs$b * increment) %% n_cards
  }
  coefs
}

get_coefs_cut <- function(n_cards, n, coefs) {
  coefs$b <- (coefs$b - n) %% n_cards
  coefs
}

# Find a and b such that
#   position_after_shuffle = a * position_before_shuffle + b MOD n
get_shuffle_coefficients <- function(df, n_cards) {
  # Start with identity
  coefs <- list(a = 1, b = 0)
  
  for (i in seq_len(nrow(df))) {
    f <- get(str_c("get_coefs_", df$action[i]))
    coefs <- f(n_cards, df$value[i], coefs)
  }
  coefs
}

# COMMAND ----------

# modular_exponentiation <- function(n, k, m) {
#   if (k == 0) return(1)
#   if (n == 0) return(0)
#   b <- n %% m
#   r <- 1
#   while (k != 0) {
#     if (k %% 2 == 1) {
#       r <- (b * r) %% m
#       k <- k - 1
#     }
#     k <- k / 2
#     b <- (b * b) %% m
#   }
#   return(r)
# }
modular_exponentiation <- function(n, k, m) {
  VeryLargeIntegers::powmod(
    VeryLargeIntegers::as.vli(format(n, scientific = FALSE)),
    VeryLargeIntegers::as.vli(format(k, scientific = FALSE)), 
    VeryLargeIntegers::as.vli(format(m, scientific = FALSE))
  ) %>%
    as.character() %>%
    as.numeric()
}

# COMMAND ----------

shuffle_coefs <- get_shuffle_coefficients(df, n_cards)

# A and B are the coefficients after 101741582076661 applications of a*x + b

# We have
#   a*x + b
# Which after one iteration, goes to
#   a*(a*x + b) + b = a^2*x + b + b*a
# After two iterations
#  a^2*(a*x + b) + b + ab = a^3*x + b + b*a + b*a^2
# After n iterations
#  a^n*x + b + b*a + b*a^2 + ... + b*a^(n-1) = A*x + B where A = a^n and B = sum of i from 0 to n-1 of b*a^i
#
# B is a geometric series which can be evaluated as
#  b * (a^n - 1) * (a - 1)' = b*(A-1)*(a-1)'
#
# n is prime so we can invert any number, k, from Fermat's Little Theorem
#       k^(n-1) = 1       MOD n
#  => k*k^(n-2) = 1       MOD n 
#  =>        k' = k^(n-2) MOD n
inverse <- function(k) modular_exponentiation(k, n_cards - 2, n_cards)
A <- modular_exponentiation(shuffle_coefs$a, n_shuffles, n_cards)
B <- (shuffle_coefs$b * (A - 1) * inverse(shuffle_coefs$a - 1)) %% n_cards # FIXME: Is this mod here correct? I think so

# We need to find x such that
#      A*x + B = 2020          MOD n
#   =>       x = A'*(2020 - B) MOD n
answer <- (inverse(A) * (2020 - B)) %% n_cards
format(answer, scientific = FALSE)

# COMMAND ----------

install.packages("VeryLargeIntegers")

# COMMAND ----------

modular_exponentiation(A, n_cards - 2, n_cards) %>% format(scientific = FALSE)

# COMMAND ----------

x=VeryLargeIntegers::as.vli("111")

# COMMAND ----------

as.character(x) %>% as.numeric()

# COMMAND ----------

x=VeryLargeIntegers::powmod(
  VeryLargeIntegers::as.vli(format(A, scientific = FALSE)),
  VeryLargeIntegers::as.vli(format(n_cards - 2, scientific = FALSE)), 
  VeryLargeIntegers::as.vli(format(n_cards, scientific = FALSE))
)

# COMMAND ----------

shuffle_coefs

# COMMAND ----------

# 73372000059392 too high
# 30179661447168 too low

# COMMAND ----------

install.packages("VeryLargeIntegers")
