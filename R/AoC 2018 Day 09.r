library(tidyverse)



players <- input %>% str_extract("\\d+(?= players)") %>% parse_integer()
points <- input %>% str_extract("\\d+(?= points)") %>% parse_integer()
lst(players, points)

calculate_high_score <- function(players, points) {
  player <- 1
  scores <- integer(players)
  marbles <- c(0)
  remaining <- seq_len(points)
  
  while(length(remaining) > 0) {
    if (remaining[1] %% 23 == 0) {
      scores[player] <- scores[player] + remaining[1]
      remaining <- tail(remaining, -1)
      
      # Remove 7 counter-clockwise
      i_7cc <- length(marbles) - 6
      while (i_7cc < 1) i_7cc <- i_7cc + length(marbles)
      scores[player] <- scores[player] + marbles[i_7cc]
      marbles <- c(tail(marbles, -i_7cc), head(marbles, i_7cc - 1))
      
    } else {
      marbles <- c(remaining[1], tail(marbles, -2), head(marbles, 2))
      remaining <- tail(remaining, -1)
    }
    player <- (player %% players) + 1
  }
  max(scores)
}

answer <- calculate_high_score(players, points)
answer

Rcpp::cppFunction('
int64_t calculate_high_score_cpp(int players, int points) {
  std::deque<int> marbles = {0};
  std::vector<int64_t> scores(players, 0);

  // For some reason this is way, way faster than std::rotate
  auto rot_left = [&marbles](int n) {
    for (int i = 0; i < n; ++i) {
      marbles.push_back(marbles.front());
      marbles.pop_front();
    }
  };
  auto rot_right = [&marbles](int n) {
    for (int i = 0; i < n; ++i) {
      marbles.push_front(marbles.back());
      marbles.pop_back();
    }
  };

  for (int new_marble = 1; new_marble <= points; ++new_marble) {
    if (new_marble % 23 == 0) {
      rot_right(7);
      scores[new_marble % players] += new_marble + marbles.front();
      marbles.pop_front();
    }
    else {
      rot_left(2);
      marbles.push_front(new_marble);
    }
  }

  return *std::max_element(scores.begin(), scores.end());
}
')

calculate_high_score_cpp(players, points * 100)
