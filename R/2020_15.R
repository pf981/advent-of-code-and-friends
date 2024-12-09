library(tidyverse)



nums <- input %>% str_split(",") %>% unlist() %>% parse_integer()
nums

simulate <- function(n, init) {
  last_seen <- new.env(hash = TRUE) # Use environments as hash map
  for (i in seq_along(init)) {
    last_seen[[as.character(init[i])]] <- i
  }
  
  v_prev <- last(init)
  for (i in seq(from = length(init) + 1, n)) {
    v <- c(i - 1 - last_seen[[as.character(v_prev)]], 0)[1]
    last_seen[[as.character(v_prev)]] <- i - 1    
    v_prev <- v
  }
  v
}

answer <- simulate(2020, nums)
answer

# R implementation works, but takes 10 minutes
# simulate(30000000, nums)

Rcpp::cppFunction('
int64_t simulate_cpp(int64_t n, std::vector<int64_t> init) 
{ 
    std::unordered_map<int64_t, int64_t> hashtable;
    int64_t v_prev = init.back();
    int64_t v;
    
    for (int i = 1; i <= init.size(); ++i) {
      hashtable[init[i - 1]] = i;
    }
    
    for (int i = init.size() + 1; i <= n; ++i) {
      v = hashtable[v_prev] ? i - 1 - hashtable[v_prev] : 0;
      hashtable[v_prev] = i - 1;
      v_prev = v;
    }
    
    return v;
} 
')

answer <- simulate_cpp(30000000, nums)
answer
