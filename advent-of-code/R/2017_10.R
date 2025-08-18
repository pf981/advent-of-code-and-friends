library(tidyverse)



nums <- seq(from = 0, to = 255, by = 1)
lengths <- str_split(input, ",") %>% first() %>% parse_integer()
lengths

hash <- function(nums, lengths) {
  skip_size <- 0
  w_total <- 0
  for (l in lengths) {
    nums[seq_len(l)] <- nums[rev(seq_len(l))]

    w <- l + skip_size
    while (w > length(nums)) w <- w - length(nums)

    nums <- c(
      tail(nums, -w),
      head(nums, w)
    )
    skip_size <- skip_size + 1
    w_total <- w_total + w
  }
  while (w_total > length(nums)) w_total <- w_total - length(nums)
  lst(nums, w_total)
  c(
    tail(nums, w_total),
    head(nums, -w_total)
  )
}

result <- hash(nums, lengths)
answer <- result[1] * result[2]
answer

to_hex <- function(x, nums = seq(from = 0, to = 255, by = 1)) {
  lengths <- rep(
    c(utf8ToInt(x), 17, 31, 73, 47, 23),
    64
  )
  
  result <- hash(nums, lengths)
  
  result %>%
    enframe() %>%
    mutate(name = (name - 1) %/% 16) %>%
    group_by(name) %>%
    summarise(
      output = reduce(value, bitwXor),
      hex = format(as.hexmode(output), width = 2)
    ) %>%
    pull(hex) %>%
    str_c(collapse = "")
}

answer <- to_hex(input)
answer
