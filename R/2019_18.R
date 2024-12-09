library(patchwork)
library(tidyverse)



m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

coords <-
  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m))
coords

plot_maze <- function(coords) {
  coords %>%
    mutate(
      fill = case_when(
        value %in% letters ~ "#F6AE2D",
        value %in% LETTERS ~ "#A0522D",
        value == "#" ~ "#2F4858",
        value == "@" ~ "#F26419"
      ),
      label = ifelse(str_detect(value, "\\w"), value, NA)
    ) %>%
    ggplot(aes(col, row, fill = I(fill), label = label)) +
      geom_tile() +
      geom_text(size = 2.5) +
      scale_y_reverse() +
      theme_void()
}

plot_maze(coords)

# # This is too slow - took 3 hours

# install.packages("datastructures")

# hashmap <- function(default = NULL) {
#   h <- structure(new.env(hash = TRUE), class = "hashmap")
#   attr(h, "default") <- default
#   h
# }

# hash_fn <- function(x) paste(x, collapse = ",")

# `[.hashmap` <- function(h, i) {
#   result <- h[[hash_fn(i)]]
#   if (is.null(result)) result <- attr(h, "default")
#   result
# }

# `[<-.hashmap` <- function(h, i, j, value) {
#   h[[hash_fn(i)]] <- value
#   h
# }

# as.list.hashmap <- function(h) {
#   attr(h, "class") <- NULL
#   as.list(h)
# }

# to_hashmap <- function(inds, default = "#") {
#   result <- hashmap(default = default)
#   for (i in seq_len(nrow(inds))) {
#     result[c(inds$row[i], inds$col[i])] <- inds$value[i]
#   }
#   result
# }


# solve <- function(coords) {
#   target_length <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% length()
#   visited <- hashmap(default = FALSE)
#   states <- datastructures::fibonacci_heap("numeric")
  
#   datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(keys = "", d = 0))
  
#   coords <- to_hashmap(coords)
  

#   repeat {
#     state <- datastructures::pop(states)[[1]]
    
#     if (visited[c(state$row, state$col, state$keys)]) next
#     visited[c(state$row, state$col, state$keys)] <- TRUE

#     # Key
#     if (state$value %in% letters) {
#       if (!str_detect(state$keys, state$value)) state$keys <- str_c(state$keys, state$value)
#       if (str_length(state$keys) == target_length) return(state$d)
#     }

#     # Lock
#     if (state$value %in% LETTERS) {
#       if (!str_detect(str_to_upper(state$keys), state$value)) next
#     }
    
#     for (direction in c("N", "E", "S", "W")) {
#       new_state <- tibble(
#         row = state$row + (direction == "S") - (direction == "N"),
#         col = state$col + (direction == "E") - (direction == "W"),
#         value = coords[c(row, col)],
#         keys = state$keys,
#         d = state$d + 1
#       )
      
#       if (new_state$value != "#") {
#         datastructures::insert(states, new_state$d, new_state)
#       }
#     }
#   }
# }

Rcpp::cppFunction("
int solve_cpp(std::vector<int> rows, std::vector<int> cols, std::vector<std::string> values) {
  using State = std::tuple<int, int, char, int, std::set<char>>;

  std::map<std::pair<int, int>, char> coords;
  std::set<std::tuple<int, int, std::set<char>>> visited; // row, col, keys
  int target_n_keys = 0;
  std::vector<State> states; // row, col, value, d, keys

  auto comp = [](const State& lhs, const State& rhs){return std::get<3>(rhs) < std::get<3>(lhs); };

  for (int i = 0; i < rows.size(); ++i) {
    coords[std::make_pair(rows[i], cols[i])] = values[i][0];

    if (values[i][0] >= 'a' && values[i][0] <= 'z') {
      ++target_n_keys;
    }

    if (values[i][0] == '@') {
      states.push_back(std::make_tuple(rows[i], cols[i], values[i][0], 0, std::set<char>()));
    }
  }

  while (states.size()) {
    auto [row, col, value, d, keys] = states.front();
    std::pop_heap(states.begin(), states.end(), comp);
    states.pop_back();

    auto state_id = std::make_tuple(row, col, keys);
    if (visited.find(state_id) != visited.end()) continue;
    visited.insert(state_id);

    // Key
    if (value >= 'a' && value <= 'z') {
      keys.insert(value);
      if (keys.size() == target_n_keys) return d;
    }

    // Lock
    if (value >= 'A' && value <= 'Z') {
      if (keys.find(tolower(value)) == keys.end()) continue;
    }

    for (char direction : {'N', 'E', 'S', 'W'}) {
      int new_row = row + (direction == 'S') - (direction == 'N');
      int new_col = col + (direction == 'E') - (direction == 'W');
      char new_value = coords[std::make_pair(new_row, new_col)];
      int new_d = d + 1;

      if (new_value == 0) new_value = '#';

      if (new_value != '#') {
        states.push_back(std::make_tuple(new_row, new_col, new_value, new_d, keys));
        std::push_heap(states.begin(), states.end(), comp);
      }
    }
  }

  Rcpp::stop(\"Unable to find all keys\");
}
",
  plugins = "cpp17" # For structured bindings
)

answer <- solve_cpp(coords$row, coords$col, coords$value)
answer

mid <- c(ceiling(max(coords$row) / 2), ceiling(max(coords$col) / 2))

coords2 <-
  coords %>%
  mutate(
    value = case_when(
      abs(row - mid[1]) == 1 & abs(col - mid[2]) == 1 ~ "@",
      abs(row - mid[1]) <= 1 & abs(col - mid[2]) <= 1 ~ "#",
      TRUE ~ value
    )
  )

quadrants <- list()
quadrants[[1]] <- coords2 %>% filter(row <= mid[1], col >= mid[2])
quadrants[[2]] <- coords2 %>% filter(row <= mid[1], col <= mid[2])
quadrants[[3]] <- coords2 %>% filter(row >= mid[1], col <= mid[2])
quadrants[[4]] <- coords2 %>% filter(row >= mid[1], col >= mid[2])

install.packages("patchwork")
library(patchwork)

(plot_maze(quadrants[[2]]) + plot_maze(quadrants[[1]])) / (plot_maze(quadrants[[3]]) + plot_maze(quadrants[[4]]))

answer <-
  quadrants %>%
  # Remove locks where the key is in a different quadrant
  map(
    ~mutate(., value = ifelse(str_to_lower(value) %in% value, value, "."))
  ) %>%
  map_dbl(~solve_cpp(.$row, .$col, .$value)) %>%
  sum()
answer
