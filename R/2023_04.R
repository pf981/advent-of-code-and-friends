library(tidyverse)




n_wins <-
  read_delim("data/2023-04.txt", delim = "|", col_names = c("have", "want")) |>
  mutate(
    have = str_extract_all(have, "\\d+"),
    want = str_extract_all(want, "\\d+"),
    n_wins = map2_int(have, want, \(.x, .y) length(intersect(.x[-1], .y)))
  ) |>
  pull(n_wins)

answer1 <-
  n_wins |>
  discard(\(.) . == 0) |>
  (\(.) 2 ^ (. - 1))() |>
  sum()
print(answer1)




count_scratchcards <- memoise::memoise(function(i) {
  if (i > length(n_wins)) return(0)
  1 + sum(map_int(i + seq_len(n_wins[[i]]), count_scratchcards))
})

answer2 <- sum(map_int(seq_along(n_wins), count_scratchcards))
print(answer2)
