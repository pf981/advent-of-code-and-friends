library(tidyverse)



# 

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    depth = str_extract(line, "^\\d+") %>% parse_integer(),
    range = str_extract(line, "\\d+$") %>% parse_integer(),
    severity = depth * range,
    period = (range - 2) * 2 + 2,
    is_caught = (depth %% period) == 0
  )
df

answer <-
  df %>%
  filter(is_caught) %>%
  pull(severity) %>%
  sum()
answer

# This is too slow
# t <- 0
# repeat {
#   caught <-
#     df %>%
#     mutate(
#       depth = depth + t,
#       period = (range - 2) * 2 + 2,
#       is_caught = (depth %% period) == 0
#     ) %>%
#     pull(is_caught) %>%
#     any()
#   if (!caught) break
#   t <- t + 1
# }

# answer <- t
# answer

Rcpp::cppFunction('
int solve_cpp(std::vector<int> depth, std::vector<int> period) {
  bool done = false;
  int t = 0;
  while (!done) {
    done = true;
    for (int i = 0; i < depth.size(); ++i) {
      if ((depth[i] + t) % period[i] == 0) {
        done = false;
        break;
      }
    }
    ++t;
  }
  return t - 1;
}
')

answer <- solve_cpp(df$depth, df$period)
answer
