library(tidyverse)



starting_positions <-
  read_lines(input) %>%
  str_extract_all("-?\\d+") %>%
  map(parse_double) %>%
  map_dfr(set_names, c("x", "y", "z")) %>%
  mutate(id = row_number())
starting_positions

simulate <- function(state) {
  state %>%
    inner_join(state, by = "dimension", suffix = c("", "_other")) %>%
    mutate(
      delta_velocity = case_when(
        position < position_other ~ 1,
        position > position_other ~ -1,
        TRUE ~ 0
      )
    ) %>%
    group_by(id, dimension) %>%
    summarise(
      position = first(position),
      velocity = first(velocity),
      delta_velocity = sum(delta_velocity)
    ) %>%
    transmute(
      id,
      dimension,
      velocity = velocity + delta_velocity,
      position = position + velocity
    )
}

state <-
  starting_positions %>%
  pivot_longer(-id, names_to = "dimension", values_to = "position") %>%
  mutate(velocity = 0)

for (i in seq_len(1000)) {
  state <- simulate(state)
}

answer <-
  state %>%
  group_by(id) %>%
  summarise(
    potential_energy = sum(abs(position)),
    kinetic_energy = sum(abs(velocity)),
    total_energy = potential_energy * kinetic_energy
  ) %>%
  pull(total_energy) %>%
  sum()

answer

Rcpp::cppFunction('
int64_t find_period(std::vector<int64_t> positions) {
  std::vector<int64_t> velocities(positions.size());

  auto start_positions = positions;
  auto start_velocities = velocities;

  for (int64_t t = 1;; ++t) {
    for (int i = 0; i < positions.size(); ++i) {
      for (auto other_position : positions) {
        velocities[i] += positions[i] < other_position ? 1 : (positions[i] > other_position ? -1 : 0);
      }
    }

    std::transform(positions.begin(), positions.end(), velocities.begin(), positions.begin(), std::plus<int64_t>());

    if (positions == start_positions && velocities == start_velocities) {
      return t;
    }
  }
}
')

periods <-
  starting_positions %>%
  select(x, y, z) %>%
  summarise_all(find_period)
periods

gcd <- function(u, v) {
  ifelse(
    u %% v != 0,
    gcd(v, (u %% v)),
    v
  )
}
 
lcm <- function(u, v) {
  abs(u * v) / gcd(u, v)
}

answer <- reduce(periods, lcm)
answer %>% format(scientific = FALSE)
