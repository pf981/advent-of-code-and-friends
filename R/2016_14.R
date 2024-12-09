library(tidyverse)



# 

df <-
  tibble(i = seq_len(100000)) %>%
  mutate(
    hash = openssl::md5(str_c(input, i)),
    triple_letter = str_extract(hash, "(.)\\1\\1"), # Only consider first triplet
    pentuple_letter = str_extract_all(hash, "(.)\\1\\1\\1\\1")
  )

df

triples <-
  df %>%
  filter(!is.na(triple_letter)) %>%
  select(i, triple_letter) %>%
  mutate(triple_letter = str_sub(triple_letter, 1, 1)) %>%
  distinct()
triples

pentuples <-
  df %>%
  select(i, pentuple_letter) %>%
  unnest() %>%
  mutate(pentuple_letter = str_sub(pentuple_letter, 1, 1)) %>%
  distinct()
pentuples

keys <- NULL

for (row in seq_along(triples$i)) {
  matched_pentuple <-
    pentuples %>%
    filter(i > triples$i[row], i <= triples$i[row] + 1000, pentuple_letter == triples$triple_letter[row])
  
  if (nrow(matched_pentuple) > 0) {
    keys <- c(keys, triples$i[row])
  }
  
  if (length(keys) >= 64) {
    break
  }
}
keys

answer <- keys[64]
answer

stretch_hash <- function(x, n) {
  result <- openssl::md5(x)
  for (i in seq_len(n)) {
    result <- openssl::md5(result)
  }
  result
}

df <-
  tibble(i = seq_len(23000)) %>%
  mutate(
    hash = stretch_hash(str_c(input, i), 2016),
    triple_letter = str_extract(hash, "(.)\\1\\1"), # Only consider first triplet
    pentuple_letter = str_extract_all(hash, "(.)\\1\\1\\1\\1")
  )

df

triples <-
  df %>%
  filter(!is.na(triple_letter)) %>%
  select(i, triple_letter) %>%
  mutate(triple_letter = str_sub(triple_letter, 1, 1)) %>%
  distinct()
triples

pentuples <-
  df %>%
  select(i, pentuple_letter) %>%
  unnest() %>%
  mutate(pentuple_letter = str_sub(pentuple_letter, 1, 1)) %>%
  distinct()
pentuples

keys <- NULL

for (row in seq_along(triples$i)) {
  matched_pentuple <-
    pentuples %>%
    filter(i > triples$i[row], i <= triples$i[row] + 1000, pentuple_letter == triples$triple_letter[row])
  
  if (nrow(matched_pentuple) > 0) {
    keys <- c(keys, triples$i[row])
  }
  
  if (length(keys) >= 64) {
    break
  }
}
keys

answer <- keys[64]
answer
