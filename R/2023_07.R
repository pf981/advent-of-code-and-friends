library(tidyverse)


text <- read_lines("data/2023-07.txt")




get_strength <- function(hand, card_order = "23456789TJQKA", original_hand = hand) {
  counts <-
    hand |>
    str_split_1("") |>
    enframe() |>
    count(value) |>
    arrange(desc(n))
  
  hand_strength <-
    c(
      counts$n[1] == 5,
      counts$n[1] == 4,
      counts$n[1] == 3 & counts$n[2] == 2,
      counts$n[1] == 3,
      counts$n[1] == 2 & counts$n[2] == 2,
      counts$n[1] == 2
    ) |>
    as.integer() |>
    str_c(collapse = "")
  
  card_strength <-
    str_locate(card_order, str_split_1(original_hand, ""))[,1] |>
    str_pad(2, pad = "0") |>
    str_c(collapse = "")
  
  str_c(hand_strength, card_strength) |> as.numeric()
}

hands_bids <-
  text |>
  str_split(" ") |>
  enframe() |>
  unnest_wider(value, names_sep = "") |>
  mutate(
    hand = value1,
    bid = as.integer(value2),
    .keep = "none"
  )

answer1 <-
  hands_bids |>
  mutate(
    strength = map_dbl(hand, get_strength)
  ) |>
  arrange(strength) |>
  mutate(
    rank = row_number(),
    score = rank * bid
  ) |>
  pull(score) |>
  sum()
print(answer1)




answer2 <-
  hands_bids |>
  mutate(
    id = row_number(),
    new_hand = map(hand, str_replace_all, "J", str_split_1("23456789TJQKA", "")) |> map(unique)
  ) |>
  unnest(new_hand) |>
  mutate(
    strength = map2_dbl(new_hand, hand, \(.x, .y) get_strength(.x, card_order = "J23456789TQKA", original_hand = .y))
  ) |>
  group_by(id) |>
  slice_max(strength, with_ties = FALSE) |>
  ungroup() |>
  arrange(strength) |>
  mutate(
    rank = row_number(),
    score = rank * bid
  ) |>
  pull(score) |>
  sum()
print(answer2)

