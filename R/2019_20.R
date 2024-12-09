library(tidyverse)



m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

portals <- arrayInd(which(m %in% LETTERS), dim(m), useNames = TRUE) %>% as_tibble()

for (i in seq_len(nrow(portals))) {
  prefix_row <- portals$row[i]
  prefix_col <- portals$col[i]
  
  for (direction in c("N", "E", "S", "W")) {
    suffix_row <- prefix_row + (direction == "S") - (direction == "N")
    suffix_col <- prefix_col + (direction == "E") - (direction == "W")
    target_row <- suffix_row + (direction == "S") - (direction == "N")
    target_col <- suffix_col + (direction == "E") - (direction == "W")
    
    if (suffix_row == 0 || suffix_col == 0 || suffix_row > nrow(m) || suffix_col > ncol(m)) next
    if (target_row == 0 || target_col == 0 || target_row > nrow(m) || target_col > ncol(m)) next
    
    if (m[suffix_row, suffix_col] %in% LETTERS && m[target_row, target_col] == ".") {
      if (direction %in% c("N", "W")) {
        temp_row <- prefix_row
        temp_col <- prefix_col
        prefix_row <- suffix_row
        prefix_col <- suffix_col
        suffix_row <- temp_row
        suffix_col <- temp_col
      }
      m[target_row, target_col] <- str_c(m[prefix_row, prefix_col], m[suffix_row, suffix_col])
    }
  }
}
m[m %in% LETTERS] <- " "

coords <-
  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m)) %>%
  filter(value != " ")

coords <-
  left_join(
    coords,
    coords %>% filter(!(value %in% c("#", "."))),
    by = "value",
    suffix = c("", "_to")
  ) %>%
  filter(value %in% c("AA", "ZZ") | is.na(row_to) | !(row == row_to & col == col_to)) %>%
  mutate(
    row_to = coalesce(row_to, row),
    col_to = coalesce(col_to, col)
  )

coords

coords %>%
  mutate(
    label = ifelse(str_detect(value, "\\w"), value, NA),
    fill = case_when(
      !is.na(label) ~ "#DEDEDE",
      value == "#" ~ "#2F4858",
      value == "@" ~ "#F26419",
      value == "." ~ "#DEDEDE"
    )
  ) %>%
  ggplot(aes(col, row, fill = I(fill), label = label)) +
    geom_tile() +
    geom_label(size = 3, mapping = aes(col = label), fill = "white", label.padding = unit(0.05, "lines")) +
    scale_y_reverse() +
    theme_void() +
    theme(legend.position = "none")

Rcpp::cppFunction('
int solve_cpp(std::vector<int> rows, std::vector<int> cols, std::vector<std::string> values, std::vector<int> to_rows, std::vector<int> to_cols) {
  using State = std::tuple<int, int, std::string, int>; // row, col, value, d

  std::map<std::pair<int, int>, std::string> coords; // row, col -> value
  std::set<std::pair<int, int>> visited; // row, col
  std::vector<State> states;
  std::map<std::pair<int, int>, std::pair<int, int>> portals; // row, col -> row, col

  auto comp = [](const State& lhs, const State& rhs){ return std::get<3>(rhs) < std::get<3>(lhs); };

  for (int i = 0; i < rows.size(); ++i) {
    coords[std::make_pair(rows[i], cols[i])] = values[i];

    if (values[i] == "AA") {
      states.push_back(std::make_tuple(rows[i], cols[i], values[i], 0));
    }

    portals[std::make_pair(rows[i], cols[i])] = std::pair(to_rows[i], to_cols[i]);
  }

  while (states.size()) {
    auto [row, col, value, d] = states.front();
    std::pop_heap(states.begin(), states.end(), comp);
    states.pop_back();

    auto state_id = std::pair(row, col);
    if (visited.find(state_id) != visited.end()) continue;
    visited.insert(state_id);

    for (char direction : {\'N\', \'E\', \'S\', \'W\'}) {
      auto [new_row, new_col] = portals[std::make_pair(
        row + (direction == \'S\') - (direction == \'N\'),
        col + (direction == \'E\') - (direction == \'W\')
      )];
      std::string new_value = coords[std::make_pair(new_row, new_col)];
      int new_d = d + 1 + (value != "." && value != "#");

      if (new_value == "ZZ") return new_d - 1;
      if (new_value == "" || new_value == "#") continue;

      states.push_back(std::make_tuple(new_row, new_col, new_value, new_d));
      std::push_heap(states.begin(), states.end(), comp);
    }
  }

  Rcpp::stop("Unable to find solution");
}
',
  plugins = "cpp17" # For structured bindings
)

answer <- solve_cpp(
  rows = coords$row,
  cols = coords$col, 
  values = coords$value,
  to_rows = coords$row_to,
  to_cols = coords$col_to
)
answer

Rcpp::cppFunction('
int solve_cpp2(std::vector<int> rows, std::vector<int> cols, std::vector<std::string> values, std::vector<int> to_rows, std::vector<int> to_cols, std::vector<int> depth_changes) {
  using State = std::tuple<int, int, std::string, int, int>; // row, col, value, d, depth

  std::map<std::pair<int, int>, std::string> coords; // row, col -> value
  std::set<std::tuple<int, int, int>> visited; // row, col, depth
  std::vector<State> states;
  std::map<std::pair<int, int>, std::tuple<int, int, int>> portals; // row, col -> row, col, depth_change

  auto comp = [](const State& lhs, const State& rhs){ return std::get<3>(rhs) < std::get<3>(lhs); };

  for (int i = 0; i < rows.size(); ++i) {
    coords[std::make_pair(rows[i], cols[i])] = values[i];

    if (values[i] == "AA") {
      states.push_back(std::make_tuple(rows[i], cols[i], values[i], 0, 0));
    }

    portals[std::make_pair(rows[i], cols[i])] = std::make_tuple(to_rows[i], to_cols[i], depth_changes[i]);
  }

  while (states.size()) {
    auto [row, col, value, d, depth] = states.front();
    std::pop_heap(states.begin(), states.end(), comp);
    states.pop_back();

    auto state_id = std::make_tuple(row, col, depth);
    if (visited.find(state_id) != visited.end()) continue;
    visited.insert(state_id);

    for (char direction : {\'N\', \'E\', \'S\', \'W\'}) {
      auto [new_row, new_col, depth_change] = portals[std::make_pair(
        row + (direction == \'S\') - (direction == \'N\'),
        col + (direction == \'E\') - (direction == \'W\')
      )];
      std::string new_value = coords[std::make_pair(new_row, new_col)];
      int new_d = d + 1 + (value != "." && value != "#");
      int new_depth = depth + depth_change;

      if (new_value == "ZZ" && depth == 0) return new_d - 1;

      if (new_value == "ZZ" || new_value == "AA") continue;
      if (new_value == "" || new_value == "#") continue;
      if (new_depth < 0) continue;

      states.push_back(std::make_tuple(new_row, new_col, new_value, new_d, new_depth));
      std::push_heap(states.begin(), states.end(), comp);
    }
  }

  Rcpp::stop("Unable to find solution");
}
',
  plugins = "cpp17" # For structured bindings
)

coords <-
  coords %>%
  mutate(
    depth_change = case_when(
      str_length(value) == 1 ~ 0,
      pmin(row, col, max(row) - row, max(col) - col) <= 3 ~ -1,
      TRUE ~ 1
    )
  )
coords

answer <- solve_cpp2(
  rows = coords$row,
  cols = coords$col, 
  values = coords$value,
  to_rows = coords$row_to,
  to_cols = coords$col_to,
  depth_changes = coords$depth_change
)
answer
