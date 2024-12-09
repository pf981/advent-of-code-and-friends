library(tidyverse)

input <- 348

solve <- function(skip = input, iterations = 2017) {
  buffer <- c(0)
  for (i in seq_len(iterations)) {
    w <- (skip %% length(buffer)) + 1
    buffer <- c(
      i,
      tail(buffer, -w),
      head(buffer, w),
      if (w == 0) buffer else NULL
    )
  }
  buffer
}

result <- solve()
answer <- result[2]
answer

# This is too slow. The list grows too big.

# Rcpp::sourceCpp(code = '
# #include <list>
#
# std::list<int>::iterator cycle(std::list<int>::iterator& it, int n, const std::list<int>::iterator& begin, const std::list<int>::iterator& end) {
#   for (int i = 0; i < n; ++i) {
#     ++it;
#     if (it == end) it = begin;
#   }
# }
#
# // [[Rcpp::export]]
# std::list<int> solve_cpp(int skip, int iterations) {
#   std::list<int> buffer = {0};
#   auto it = buffer.begin();
#   for (int iteration = 0; iteration < iterations; ++iteration) {
#     cycle(
#       it,
#       skip,
#       buffer.begin(),
#       buffer.end()
#     );
#     ++it;
#     it = buffer.insert(it, iteration + 1);
#   }
#   return buffer;
# }
# ')
#
# result <- solve_cpp(input, 50000000)
# answer <- result[which(result == 0) + 1]
# answer

# 0 is always the first element. So we just need to keep track of whatever is in position 1
Rcpp::cppFunction('
int solve_cpp(int skip, int iterations) {
  int buffer_size = 1;
  int i = 0;
  int result;
  for (int iteration = 0; iteration < iterations; ++iteration) {
    i = ((i + skip) % buffer_size) + 1;
    ++buffer_size;
    if (i == 1) result = iteration + 1;
  }
  return result;
}
')

answer <- solve_cpp(input, 50000000)
answer
