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
  std::vector<Node> nodes;
  for (int64_t cup : cups) {
    nodes.push_back({cup, nullptr});
  }
  for (int64_t i = nodes.size() + 1; i < n_cups; ++i) {
    nodes.push_back({i, nullptr});
  }

  Node *head = &nodes[0];
  Node *tail = head;
  for (int64_t i = 1; i < nodes.size(); ++i) {
    tail->next = &nodes[i];
    tail = tail->next;
  }
  tail->next = head;



  // Do the moves
  Node* pick_up;
  Node* dest;

  for (int64_t move = 0; move < n_moves; ++move, head = head->next) {
    pick_up = head->next;
    head->next = pick_up->next->next->next;

    dest = head->next;
    for (Node* node = head->next->next; node != head; node = node->next) {
      if (
          (node->value > head->value && dest->value > head->value && node->value > dest->value)
          || (node->value < head->value && dest->value < head->value && node->value > dest->value)
          || (node->value < head->value && dest->value > head->value)
        ) {
        dest = node;
      }
    }
    pick_up->next->next->next = dest->next;
    dest->next = pick_up;
  }


  // Return the result
  // while (head->value != 1) {
  //   head = head->next;
  // }
  // return head->next->value * head->next->next->value;

  // debug
  std::vector<int64_t> result;
  Node* n = head;
  do {
    result.push_back(n->value);
    n = n->next;
  } while(n != head);
  return result;
}
")

# COMMAND ----------

simulate_moves(
  "389125467" %>% str_split("") %>% unlist() %>% as.numeric(),
  nchar("389125467"),
  10
)

# COMMAND ----------



# COMMAND ----------

rotate <- function(x, n = 1) {
  if (n == 0) x else c(tail(x, -n), head(x, n))
}

# COMMAND ----------

simulate_moves <- function(cups, n_moves = 1, debug = FALSE) {
  cur_i <- 1
  for (move in seq_len(n_moves)) {
    current_cup <- cups[cur_i]
    picked_up <- cups[((cur_i + seq_len(3) - 1) %% length(cups)) + 1]

    candidates <- cups[!(cups %in% picked_up)]
    destination <- max(candidates[candidates < current_cup])
    if (!is.finite(destination)) {
      destination <- max(candidates)
    }
    destination_i <- which(candidates == destination)

    if (debug) {
      message(glue::glue('-- move {move} --
cups: {paste0(cups, ifelse(seq_along(cups) == cur_i, "*", ""), collapse = " ")}
pick up: {paste0(picked_up, collapse = " ")}
destination: {destination} (i: {destination_i})

'))
    }
    
    cups <- append(candidates, picked_up, after = destination_i)
    
    # Need which(cups == current_cup) == cur_i
    #cups <- rotate(cups, which(cups == current_cup) - cur_i)

    #cur_i <- (cur_i %% length(cups)) + 1
    cur_i <- (which(cups == current_cup) %% length(cups)) + 1
  }
  
  cups
}

# COMMAND ----------

# Rcpp::cppFunction("
# struct Node {
#     int64_t value;
#     Node* next; // Node* next {nullptr};
# };

# // [[Rcpp::export]]
# std::vector<int64_t> simulate_moves(std::vector<int64_t> cups, int64_t n_cups,int64_t n_moves) {
#   // Create the circular linked list
#   std::vector<Node> nodes;
#   for (int64_t cup : cups) {
#     nodes.push_back({cup, nullptr});
#   }
#   for (int64_t i = nodes.size() + 1; i < n_cups; ++i) {
#     nodes.push_back({i, nullptr});
#   }

#   Node *head = &nodes[0];
#   Node *tail = head;
#   for (int64_t i = 1; i < nodes.size(); ++i) {
#     tail->next = &nodes[i];
#     tail = tail->next;
#   }
#   tail->next = head;
 
#   // debug
#   std::vector<int64_t> result;
#   Node* n = head;
#   do {
#     result.push_back(n->value);
#     n = n->next;
#   } while(n != head);
#   return result;

#   Node* pick_up;
#   Node* dest;

#   // Do the moves
#   for (int64_t move = 0; move < n_moves; ++move) {
#     pick_up = head->next;
#     head->next = pick_up->next->next->next;

#     dest = head->next;
#     for (Node* node = head->next->next; node != head; node = node->next) {
#       if (
#           (node->value > head->value && node->value > dest->value)
#           || (node->value < head->value && dest->value < head->value && node->value > dest->value)
#         ) {
#         dest = node;
#       }
#     }
#     pick_up->next->next->next = dest->next;
#     dest->next = pick_up;
#   }

#   while (head->value != 1) {
#     head = head->next;
#   }

#   //std::vector<int64_t> result;
#   while (head->next->value != 1) {
#     result.push_back(head->value);
#     head = head->next;
#   }

#   // return head->next->value * head->next->next->value;
#   return result;
# }
# ")

# COMMAND ----------

# Rcpp::cppFunction("
# struct Node {
#     int64_t value;
#     Node* next; // Node* next {nullptr};
# };

# // [[Rcpp::export]]
# int64_t simulate_moves(std::vector<int64_t> cups, int64_t n_cups,int64_t n_moves) {
#   // Create the circular linked list
#   std::vector<Node> nodes;
#   for (int64_t cup : cups) {
#     nodes.push_back({cup, nullptr});
#   }
#   for (int64_t i = nodes.size() + 1; i < n_cups; ++i) {
#     nodes.push_back({i, nullptr});
#   }

#   Node *head = &nodes[0];
#   Node *tail = head;
#   for (int64_t i = 1; i < nodes.size(); ++i) {
#     tail->next = &nodes[i];
#     tail = tail->next;
#   }
#   tail->next = head;

#   Node* pick_up;
#   Node* dest;

#   // Do the moves
#   for (int64_t move = 0; move < n_moves; ++move) {
#     pick_up = head->next;
#     head->next = pick_up->next->next->next;

#     dest = head->next;
#     for (Node* node = head->next->next; node != head; node = node->next) {
#       if (
#           (node->value > head->value && node->value > dest->value)
#           || (node->value < head->value && dest->value < head->value && node->value > dest->value)
#         ) {
#         dest = node;
#       }
#     }
#     pick_up->next->next->next = dest->next;
#     dest->next = pick_up;
#   }

#   while (head->value != 1) {
#     head = head->next;
#   }

#   return head->next->value * head->next->next->value;
# }
# ")

# COMMAND ----------

# Rcpp::cppFunction("
# struct Node {
#     int64_t value;
#     Node* next; // Node* next {nullptr};
# };

# // [[Rcpp::export]]
# int64_t simulate_moves(std::vector<int64_t> cups, int64_t n_cups,int64_t n_moves) {
#   int64_t cur_i = 0;
#   std::vector<Node> nodes;
#   Node head = {int64_t(), nullptr};
#   Node tail;

#   //for (int64_t i = 0; i < cups.size(); ++i) {
# //  for (int64_t cup : cups) {
# //    // Node node = {cup, nullptr};
# //Node node(cup);
# //    nodes.push_back(node);
# //  }
#   //for (int64_t i = l.size() + 1; i < n_cups; ++i) {
#   //  l.push_back(i);
#   //}
# //
#   //for (int64_t move = 0; move < n_moves; ++move) {
#   //  
#   //}

#   return cups[0];
# }
# ")
# # simulate_moves <- function(cups, n_moves = 1, debug = FALSE) {
# #   cur_i <- 1
# #   for (move in seq_len(n_moves)) {
# #     current_cup <- cups[cur_i]
# #     picked_up <- cups[((cur_i + seq_len(3) - 1) %% length(cups)) + 1]

# #     candidates <- cups[!(cups %in% picked_up)]
# #     destination <- max(candidates[candidates < current_cup])
# #     if (!is.finite(destination)) {
# #       destination <- max(candidates)
# #     }
# #     destination_i <- which(candidates == destination)

# #     if (debug) {
# #       message(glue::glue('-- move {move} --
# # cups: {paste0(cups, ifelse(seq_along(cups) == cur_i, "*", ""), collapse = " ")}
# # pick up: {paste0(picked_up, collapse = " ")}
# # destination: {destination} (i: {destination_i})

# # '))
# #     }
    
# #     cups <- append(candidates, picked_up, after = destination_i)
    
# #     # Need which(cups == current_cup) == cur_i
# #     #cups <- rotate(cups, which(cups == current_cup) - cur_i)

# #     #cur_i <- (cur_i %% length(cups)) + 1
# #     cur_i <- (which(cups == current_cup) %% length(cups)) + 1
# #   }
  
# #   cups
# # }

# COMMAND ----------

simulate_moves(1:10, 5)

# COMMAND ----------

result <- simulate_moves(cups, 100)

rotate(result, which(result == 1) - 1) %>%
  tail(-1) %>%
  paste0(collapse = "")

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

result <- simulate_moves(
  c(cups, seq(from = max(cups), to = 1000000, by = 1)),
  10000000
)

# first_two <-
#   rotate(result, which(result == 1) - 1) %>%
#   tail(-1) %>%
#   head(2)

# first_two[1] * first_two[2]

# COMMAND ----------

result

# COMMAND ----------

first_two <-
  rotate(result, which(result == 1) - 1) %>%
  tail(-1) %>%
  head(2)

first_two[1] * first_two[2]