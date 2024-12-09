input <- 3014603

# This is just the Josephus permutation. I have answered a question like this on SO https://stackoverflow.com/a/48703963/1751961
josephus <- function(n) 2 * (n - 2 ^ (floor(log2(n)))) + 1

josephus(input)

# This recursive solution is nice, but it goes too deep and fails

# steal <- function(elves = seq_len(input)) {
#   if (length(elves) == 1) return(elves)
  
#   elves <- elves[-((length(elves) %/% 2) + 1)]

#   steal(c(tail(elves, -1), elves[1]))
# }

# Even non-recursive R solution was too slow

# steal <- function(n_elves) {
#   elves <- seq_len(n_elves)
  
#   while (length(elves) > 1) {
#     elves <- elves[-((length(elves) %/% 2) + 1)]
#     elves <- c(tail(elves, -1), elves[1])
#   }
#   elves
# }
# answer <- steal(input)
# answer

# This solution worked but took 34 minutes due to the erase in the middle

# Rcpp::cppFunction('
# int steal(int n_elves) {
#     std::deque<int> left(n_elves);

#     // 1:n_elves
#     std::iota(elves.begin(), elves.end(), 1);
    
#     while (elves.size() > 1) {
#       elves.erase(elves.begin() + int(elves.size() / 2));
#       std::rotate(elves.begin(), elves.begin() + 1, elves.end());
#     }

#     return elves.front();
# } 
# ')
# answer <- steal(input)
# answer # This took 34 minutes

# This solution was way faster. Keep track of left and right - this gets rid of the erase so all operations are what dequeues are optimised for.

Rcpp::cppFunction('
int steal(int n_elves) {
    std::deque<int> left(n_elves / 2 + 1); // Assumes odd n_elves
    std::deque<int> right(n_elves / 2);

    std::iota(left.begin(), left.end(), 1);
    std::iota(right.rbegin(), right.rend(), n_elves / 2 + 1);
    
    while (!left.empty() && !right.empty()) {
        (left.size() > right.size() ? left : right).pop_back();

        right.push_front(left.front());
        left.pop_front();

        left.push_back(right.back());
        right.pop_back();
    }

    return (left.empty() ? right : left).front();
} 
')
answer <- steal(input) # 5 seconds
answer
