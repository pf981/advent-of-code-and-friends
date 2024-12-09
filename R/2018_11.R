library(tidyverse)

input <- 4172

create_power_matrix <- function(grid_serial_number = input) {
  x_coord <- matrix(seq_len(300), nrow = 300, ncol = 300, byrow = TRUE)
  y_coord <- matrix(seq_len(300), nrow = 300, ncol = 300, byrow = FALSE)
  rack_id <- x_coord + 10
  power_level <- (rack_id * y_coord + grid_serial_number) * rack_id
  power_level <- (power_level %/% 100) %% 10
  power_level <- power_level - 5
  power_level
}

shift <- function(m, rows, cols) {
  i_rows <- seq(from = rows + 1, to = nrow(m), by = 1)
  i_cols <- seq(from = cols + 1, to = ncol(m), by = 1)
  m <- m[i_rows, i_cols]
  while (rows > 0) {
    m <- rbind(m, 0)
    rows <- rows - 1
  }
  while (cols > 0) {
    m <- cbind(m, 0)
    cols <- cols - 1
  }
  m
}

create_grid_power_matrix <- function(m) {
  shift(m, 0, 0) + shift(m, 0, 1) + shift(m, 0, 2) +
  shift(m, 1, 0) + shift(m, 1, 1) + shift(m, 1, 2) +
  shift(m, 2, 0) + shift(m, 2, 1) + shift(m, 2, 2)
}

m <- create_power_matrix()

grid_power <- create_grid_power_matrix(m)
grid_power

max_grid <- arrayInd(which.max(grid_power), dim(grid_power))
answer <- str_c(max_grid[2], ",", max_grid[1])
answer

Rcpp::cppFunction('
std::string solve_cpp(NumericMatrix m_start) {
  int64_t max_grid_total = INT_MIN;
  int max_grid_size, max_grid_col, max_grid_row;
  NumericMatrix m = Rcpp::clone(m_start);

  for (int size = 1; size <= m.nrow(); ++size) {
    for (int row = 0; row < m.nrow() - size + 1; ++row) {
      for (int col = 0; col < m.ncol() - size + 1; ++col) {
        if (m(row, col) > max_grid_total) {
          max_grid_total = m(row, col);
          max_grid_size = size;
          max_grid_col = col;
          max_grid_row = row;
        }

        if (size != m.nrow() && !(row == m.nrow() - size || col == m.ncol() - size)) {
          for (int i = row; i <= row + size; ++i) {
            m(row, col) += m_start(i, col + size);
          }
          // Subtract 1 so you dont double-count the bottom right corner
          for (int j = col; j <= col + size - 1; ++j) {
            m(row, col) += m_start(row + size, j);
          }
        }
      }
    }
  }

  return
    std::to_string(max_grid_col + 1) + "," +
    std::to_string(max_grid_row + 1) + "," +
    std::to_string(max_grid_size);
}
')

answer <- solve_cpp(m)
answer
