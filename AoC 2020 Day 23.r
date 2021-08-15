# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Crab Cups ---</h2><p>The small crab challenges <em>you</em> to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.</p>
# MAGIC <p>The cups will be arranged in a circle and labeled <em>clockwise</em> (your puzzle input). For example, if your labeling were <code>32415</code>, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled <code>3</code>, <code>2</code>, <code>4</code>, <code>1</code>, <code>5</code>, and then back to <code>3</code> again.</p>
# MAGIC <p>Before the crab starts, it will designate the first cup in your list as the <em>current cup</em>. The crab is then going to do <em>100 moves</em>.</p>
# MAGIC <p>Each <em>move</em>, the crab does the following actions:</p>
# MAGIC <ul>
# MAGIC <li>The crab picks up the <em>three cups</em> that are immediately <em>clockwise</em> of the <em>current cup</em>. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.</li>
# MAGIC <li>The crab selects a <em>destination cup</em>: the cup with a <em>label</em> equal to the <em>current cup's</em> label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it <em>wraps around</em> to the highest value on any cup's label instead.</li>
# MAGIC <li>The crab places the cups it just picked up so that they are <em>immediately clockwise</em> of the destination cup. They keep the same order as when they were picked up.</li>
# MAGIC <li>The crab selects a new <em>current cup</em>: the cup which is immediately clockwise of the current cup.</li>
# MAGIC </ul>
# MAGIC <p>For example, suppose your cup labeling were <code>389125467</code>. If the crab were to do merely 10 moves, the following changes would occur:</p>
# MAGIC <pre><code>-- move 1 --
# MAGIC cups: (3) 8  9  1  2  5  4  6  7 
# MAGIC pick up: 8, 9, 1
# MAGIC destination: 2
# MAGIC 
# MAGIC -- move 2 --
# MAGIC cups:  3 (2) 8  9  1  5  4  6  7 
# MAGIC pick up: 8, 9, 1
# MAGIC destination: 7
# MAGIC 
# MAGIC -- move 3 --
# MAGIC cups:  3  2 (5) 4  6  7  8  9  1 
# MAGIC pick up: 4, 6, 7
# MAGIC destination: 3
# MAGIC 
# MAGIC -- move 4 --
# MAGIC cups:  7  2  5 (8) 9  1  3  4  6 
# MAGIC pick up: 9, 1, 3
# MAGIC destination: 7
# MAGIC 
# MAGIC -- move 5 --
# MAGIC cups:  3  2  5  8 (4) 6  7  9  1 
# MAGIC pick up: 6, 7, 9
# MAGIC destination: 3
# MAGIC 
# MAGIC -- move 6 --
# MAGIC cups:  9  2  5  8  4 (1) 3  6  7 
# MAGIC pick up: 3, 6, 7
# MAGIC destination: 9
# MAGIC 
# MAGIC -- move 7 --
# MAGIC cups:  7  2  5  8  4  1 (9) 3  6 
# MAGIC pick up: 3, 6, 7
# MAGIC destination: 8
# MAGIC 
# MAGIC -- move 8 --
# MAGIC cups:  8  3  6  7  4  1  9 (2) 5 
# MAGIC pick up: 5, 8, 3
# MAGIC destination: 1
# MAGIC 
# MAGIC -- move 9 --
# MAGIC cups:  7  4  1  5  8  3  9  2 (6)
# MAGIC pick up: 7, 4, 1
# MAGIC destination: 5
# MAGIC 
# MAGIC -- move 10 --
# MAGIC cups: (5) 7  4  1  8  3  9  2  6 
# MAGIC pick up: 7, 4, 1
# MAGIC destination: 3
# MAGIC 
# MAGIC -- final --
# MAGIC cups:  5 (8) 3  7  4  1  9  2  6 
# MAGIC </code></pre>
# MAGIC <p>In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the <em>current cup</em> is marked with <code>( )</code>.</p>
# MAGIC <p>After the crab is done, what order will the cups be in? Starting <em>after the cup labeled <code>1</code></em>, collect the other cups' labels clockwise into a single string with no extra characters; each number except <code>1</code> should appear exactly once. In the above example, after 10 moves, the cups clockwise from <code>1</code> are labeled <code>9</code>, <code>2</code>, <code>6</code>, <code>5</code>, and so on, producing <em><code>92658374</code></em>. If the crab were to complete all 100 moves, the order after cup <code>1</code> would be <em><code>67384529</code></em>.</p>
# MAGIC <p>Using your labeling, simulate 100 moves. <em>What are the labels on the cups after cup <code>1</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- 326519478

# COMMAND ----------

cups <- input %>% str_split("") %>% unlist() %>% as.integer()
cups

# COMMAND ----------

Rcpp::cppFunction("
struct Node {
  int64_t value;
  Node* next;
};

// [[Rcpp::export]]
std::vector<int64_t> simulate_moves(std::vector<int64_t> cups, int64_t n_cups,int64_t n_moves) {
  // Create the circular linked list
  std::vector<Node> nodes(n_cups); // 1:n_cups
  for (int64_t i = 1; i <= n_cups; ++i) {
    nodes[i - 1] = {i, nullptr};
  }

  Node *head = &nodes[cups[0] - 1];
  for (auto cup_it = cups.begin() + 1; cup_it != cups.end(); ++cup_it) {
    head->next = &nodes[*cup_it - 1];
    head = head->next;
  }
  for (int64_t i = cups.size() + 1; i <= n_cups; ++i) {
    head->next = &nodes[i - 1];
    head = head->next;
  }
  head->next = &nodes[cups[0] - 1];
  head = head->next;


  // Do the moves
  Node* pick_up;
  Node* dest;

  for (int64_t move = 0; move < n_moves; ++move, head = head->next) {
    pick_up = head->next;
    head->next = pick_up->next->next->next;

    int64_t dest_value = head->value;
    do {
      dest_value = dest_value - 1;
      if (dest_value == 0) {
        dest_value = n_cups;
      }
    } while (dest_value == pick_up->value || dest_value == pick_up->next->value || dest_value == pick_up->next->next->value);

    dest = &nodes[dest_value - 1];

    pick_up->next->next->next = dest->next;
    dest->next = pick_up;
  }


  // Return the result in the correct order
  std::vector<int64_t> result;
  while (head->value != 1) {
    head = head->next;
  }
  do {
    result.push_back(head->next->value);
    head = head->next;
  } while(head->next->value != 1);
  return result;
}
")

# COMMAND ----------

answer <- simulate_moves(cups, length(cups), 100) %>% str_c(collapse = "")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Due to what you can only assume is a mistranslation (you're <span title="If I were going for a programming language pun here, I'd say you were a little... RUSTy.">not exactly fluent in Crab</span>), you are quite surprised when the crab starts arranging <em>many</em> cups in a circle on your raft - <em>one million</em> (<code>1000000</code>) in total.</p>
# MAGIC <p>Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were <code>54321</code>, the cups would be numbered <code>5</code>, <code>4</code>, <code>3</code>, <code>2</code>, <code>1</code>, and then start counting up from <code>6</code> until one million is reached.) In this way, every number from one through one million is used exactly once.</p>
# MAGIC <p>After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do <em>ten million</em> (<code>10000000</code>) moves!</p>
# MAGIC <p>The crab is going to hide your <em class="star">stars</em> - one each - under the <em>two cups that will end up immediately clockwise of cup <code>1</code></em>. You can have them if you predict what the labels on those cups will be when the crab is finished.</p>
# MAGIC <p>In the above example (<code>389125467</code>), this would be <code>934001</code> and then <code>159792</code>; multiplying these together produces <em><code>149245887792</code></em>.</p>
# MAGIC <p>Determine which two cups will end up immediately clockwise of cup <code>1</code>. <em>What do you get if you multiply their labels together?</em></p>
# MAGIC </article>

# COMMAND ----------

result <- simulate_moves(cups, 1000000, 10000000)
answer <- result[1] * result[2]
answer
