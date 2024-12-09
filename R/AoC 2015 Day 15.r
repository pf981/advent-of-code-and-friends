library(tidyverse)



Rcpp::cppFunction("
int solve() {
  int best_score = 0;
  for (int a = 0; a < 100; ++a) {
    for (int b = 0; b < 100; ++b) {
      for (int c = 0; c < 100; ++c) {
        for (int d = 0; d < 100; ++d) {
          if (a + b + c + d == 100) {
            best_score = std::max(
              std::max(a*2 + b*0 +c*0 + d*0, 0) * std::max(a*0 + b*5 + c*0 + d*-1, 0) * std::max(a*-2 + b*-3 + c*5 + d*0, 0) * std::max(a*0 + b*0 + c*-1 + d*5, 0),
              best_score
            );
          }
        }
      }
    }
  }

  return best_score;
} 
")

answer <- solve()
answer

Rcpp::cppFunction("
int solve() {
  int best_score = 0;
  for (int a = 0; a < 100; ++a) {
    for (int b = 0; b < 100; ++b) {
      for (int c = 0; c < 100; ++c) {
        for (int d = 0; d < 100; ++d) {
          if (a + b + c + d == 100 && a*3 + b*3 + c*8 + d*8 == 500) {
            best_score = std::max(
              std::max(a*2 + b*0 +c*0 + d*0, 0) * std::max(a*0 + b*5 + c*0 + d*-1, 0) * std::max(a*-2 + b*-3 + c*5 + d*0, 0) * std::max(a*0 + b*0 + c*-1 + d*5, 0),
              best_score
            );
          }
        }
      }
    }
  }

  return best_score;
} 
")

answer <- solve()
answer
