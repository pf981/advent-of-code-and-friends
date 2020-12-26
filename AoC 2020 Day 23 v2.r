# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/23

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- 326519478

# COMMAND ----------

# input <- 389125467

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

simulate_moves(cups, length(cups), 100) %>% str_c(collapse = "")

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# result <- simulate_moves(cups, 100, 100)

# COMMAND ----------

result <- simulate_moves(cups, 1000000, 10000000)
result[1] * result[2]

# COMMAND ----------

# Rcpp::cppFunction("
# struct Node {
#   int64_t value;
#   Node* next;
# };

# // [[Rcpp::export]]
# std::vector<int64_t> simulate_moves(std::vector<int64_t> cups, int64_t n_cups,int64_t n_moves) {
#   // Create the circular linked list
#   std::vector<Node> nodes(n_cups); // 1:n_cups
#   for (int64_t i = 1; i <= n_cups; ++i) {
#     nodes[i - 1] = {i, nullptr};
#   }

#   Node *head = &nodes[cups[0] - 1];
#   for (auto cup_it = cups.begin() + 1; cup_it != cups.end(); ++cup_it) {
#     head->next = &nodes[*cup_it - 1];
#     head = head->next;
#   }
#   for (int64_t i = cups.size() + 1; i <= n_cups; ++i) {
#     head->next = &nodes[i - 1];
#     head = head->next;
#   }
#   head->next = &nodes[cups[0] - 1];
#   head = head->next;


#   // Do the moves
#   Node* pick_up;
#   Node* dest;

#   for (int64_t move = 0; move < n_moves; ++move, head = head->next) {
#     pick_up = head->next;
#     head->next = pick_up->next->next->next;

#     int64_t dest_value = head->value;
#     do {
#       dest_value = dest_value - 1;
#       if (dest_value == 0) {
#         dest_value = n_cups;
#       }
#     } while (dest_value == pick_up->value || dest_value == pick_up->next->value || dest_value == pick_up->next->next->value);

#     dest = &nodes[dest_value - 1];

#     pick_up->next->next->next = dest->next;
#     dest->next = pick_up;
#   }


#   // Return the result in the correct order
#   while (head->value != 1) {
#     head = head->next;
#   }

#   //return head->next->value * head->next->next->value;


#   // DEBUG
#   std::vector<int64_t> result;
#   Node *node = head;
#   do {
#     result.push_back(node->value);
#     node = node->next;
#   } while(node != head);
#   return result;
# }
# ")