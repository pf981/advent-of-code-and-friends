# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 9: Marble Mania ---</h2><p>You talk to the Elves while you wait for your navigation system to <span title="Do you have any idea how long it takes to load navigation data for all of time and space?!">initialize</span>. To pass the time, they introduce you to their favorite <a href="https://en.wikipedia.org/wiki/Marble_(toy)">marble</a> game.</p>
# MAGIC <p>The Elves play this game by taking turns arranging the marbles in a <em>circle</em> according to very particular rules. The marbles are numbered starting with <code>0</code> and increasing by <code>1</code> until every marble has a number.</p>
# MAGIC <p>First, the marble numbered <code>0</code> is placed in the circle. At this point, while it contains only a single marble, it is still a circle: the marble is both clockwise from itself and counter-clockwise from itself. This marble is designated the <em>current marble</em>.</p>
# MAGIC <p>Then, each Elf takes a turn placing the <em>lowest-numbered remaining marble</em> into the circle between the marbles that are <code>1</code> and <code>2</code> marbles <em>clockwise</em> of the current marble. (When the circle is large enough, this means that there is one marble between the marble that was just placed and the current marble.) The marble that was just placed then becomes the <em>current marble</em>.</p>
# MAGIC <p>However, if the marble that is about to be placed has a number which is a multiple of <code>23</code>, <em>something entirely different happens</em>. First, the current player keeps the marble they would have placed, adding it to their <em>score</em>. In addition, the marble <code>7</code> marbles <em>counter-clockwise</em> from the current marble is <em>removed</em> from the circle and <em>also</em> added to the current player's score. The marble located immediately <em>clockwise</em> of the marble that was removed becomes the new <em>current marble</em>.</p>
# MAGIC <p>For example, suppose there are 9 players. After the marble with value <code>0</code> is placed in the middle, each player (shown in square brackets) takes a turn. The result of each of those turns would produce circles of marbles like this, where clockwise is to the right and the resulting current marble is in parentheses:</p>
# MAGIC <pre><code>[-] <em>(0)</em>
# MAGIC [1]  0<em> (1)</em>
# MAGIC [2]  0<em> (2)</em> 1 
# MAGIC [3]  0  2  1<em> (3)</em>
# MAGIC [4]  0<em> (4)</em> 2  1  3 
# MAGIC [5]  0  4  2<em> (5)</em> 1  3 
# MAGIC [6]  0  4  2  5  1<em> (6)</em> 3 
# MAGIC [7]  0  4  2  5  1  6  3<em> (7)</em>
# MAGIC [8]  0<em> (8)</em> 4  2  5  1  6  3  7 
# MAGIC [9]  0  8  4<em> (9)</em> 2  5  1  6  3  7 
# MAGIC [1]  0  8  4  9  2<em>(10)</em> 5  1  6  3  7 
# MAGIC [2]  0  8  4  9  2 10  5<em>(11)</em> 1  6  3  7 
# MAGIC [3]  0  8  4  9  2 10  5 11  1<em>(12)</em> 6  3  7 
# MAGIC [4]  0  8  4  9  2 10  5 11  1 12  6<em>(13)</em> 3  7 
# MAGIC [5]  0  8  4  9  2 10  5 11  1 12  6 13  3<em>(14)</em> 7 
# MAGIC [6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7<em>(15)</em>
# MAGIC [7]  0<em>(16)</em> 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15 
# MAGIC [8]  0 16  8<em>(17)</em> 4  9  2 10  5 11  1 12  6 13  3 14  7 15 
# MAGIC [9]  0 16  8 17  4<em>(18)</em> 9  2 10  5 11  1 12  6 13  3 14  7 15 
# MAGIC [1]  0 16  8 17  4 18  9<em>(19)</em> 2 10  5 11  1 12  6 13  3 14  7 15 
# MAGIC [2]  0 16  8 17  4 18  9 19  2<em>(20)</em>10  5 11  1 12  6 13  3 14  7 15 
# MAGIC [3]  0 16  8 17  4 18  9 19  2 20 10<em>(21)</em> 5 11  1 12  6 13  3 14  7 15 
# MAGIC [4]  0 16  8 17  4 18  9 19  2 20 10 21  5<em>(22)</em>11  1 12  6 13  3 14  7 15 
# MAGIC [5]  0 16  8 17  4 18<em>(19)</em> 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 
# MAGIC [6]  0 16  8 17  4 18 19  2<em>(24)</em>20 10 21  5 22 11  1 12  6 13  3 14  7 15 
# MAGIC [7]  0 16  8 17  4 18 19  2 24 20<em>(25)</em>10 21  5 22 11  1 12  6 13  3 14  7 15
# MAGIC </code></pre>
# MAGIC <p>The goal is to be the <em>player with the highest score</em> after the last marble is used up. Assuming the example above ends after the marble numbered <code>25</code>, the winning score is <code>23+9=<em>32</em></code> (because player 5 kept marble <code>23</code> and removed marble <code>9</code>, while no other player got any points in this very short example game).</p>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <ul>
# MAGIC <li><code>10</code> players; last marble is worth <code>1618</code> points: high score is <em><code>8317</code></em></li>
# MAGIC <li><code>13</code> players; last marble is worth <code>7999</code> points: high score is <em><code>146373</code></em></li>
# MAGIC <li><code>17</code> players; last marble is worth <code>1104</code> points: high score is <em><code>2764</code></em></li>
# MAGIC <li><code>21</code> players; last marble is worth <code>6111</code> points: high score is <em><code>54718</code></em></li>
# MAGIC <li><code>30</code> players; last marble is worth <code>5807</code> points: high score is <em><code>37305</code></em></li>
# MAGIC </ul>
# MAGIC <p><em>What is the winning Elf's score?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "476 players; last marble is worth 71657 points"

# COMMAND ----------

players <- input %>% str_extract("\\d+(?= players)") %>% parse_integer()
points <- input %>% str_extract("\\d+(?= points)") %>% parse_integer()
lst(players, points)

# COMMAND ----------

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

# COMMAND ----------

answer <- calculate_high_score(players, points)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Amused by the speed of your answer, the Elves are curious:</p>
# MAGIC <p><em>What would the new winning Elf's score be if the number of the last marble were 100 times larger?</em></p>
# MAGIC </article>

# COMMAND ----------

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

# COMMAND ----------

calculate_high_score_cpp(players, points * 100)
