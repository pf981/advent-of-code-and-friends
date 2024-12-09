library(tidyverse)



nums <- input %>% str_split("") %>% unlist() %>% parse_integer()
nums

create_pattern <- function(step, length_out, base_pattern = c(0, 1, 0, -1)) {
  base_pattern %>%
    rep(each = step) %>%
    rep(length.out = length_out + 1) %>%
    tail(-1)
}

process_phase <- function(nums) {
  result <- integer(length(nums))
  for (step in seq_along(nums)) {
    pattern <- create_pattern(step, length(nums))
    result[step] <- abs(sum(nums * pattern)) %% 10
  }
  result
}

solve <- function(nums, n_phases = 100) {
  for (phase in seq(from = 0, to = n_phases - 1, by = 1)) {
    nums <- process_phase(nums)
  }
  nums
}

result <- solve(nums)
result

answer <- result %>% head(8) %>% str_c(collapse = "")
answer

m <- map(seq_len(50), create_pattern, 50) %>% simplify2array() %>% t()
m

plot_df <-
  m %>%
  as_tibble() %>%
  mutate(y = row_number()) %>%
  pivot_longer(-y, names_to = "x") %>%
  mutate(
    x = str_extract(x, "\\d+") %>% parse_integer()
  )

ggplot(plot_df, aes(x, y, fill = as.factor(value), label = value)) +
  geom_tile(height = 0.8) +
  geom_text(size = 2) +
  scale_fill_manual(values = c("red", "grey", "green")) +
  scale_x_continuous(breaks = seq_len(50), expand = c(0, 0)) +
  scale_y_reverse(breaks = seq_len(50), expand = c(0, 0)) +
  labs(
    x = "Coefficient",
    y = "Step"
  ) +
  theme_void() +
  theme(
    axis.text = element_text(size = rel(0.5)),
    axis.title.x = element_text(size = rel(0.9)),
    axis.title.y = element_text(angle = 90, size = rel(0.9)),
    legend.position = "none"
  )

step <- function(x) x %>% rev() %>% cumsum() %>% `%%`(10) %>% rev()

offset <- head(nums, 7) %>% str_c(collapse = "") %>% parse_integer()

new_nums <- tail(rep(nums, 10000), -offset)
for (i in seq_len(100)) {
  new_nums <- step(new_nums)
}

answer <- head(new_nums, 8)
answer %>% str_c(collapse = "")
