library(tidyverse)



sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

Rcpp::cppFunction('
bool run_instructions(std::vector<int> sequence, std::deque<int> input) {
  std::map<int64_t, int64_t> instructions;
  int64_t relative_base = 0;
  int64_t value;
  int64_t i;

  for (int j = 0; j < sequence.size(); ++j) {
    instructions[j] = sequence[j];
  }

  auto get_param = [&](int param) -> decltype(auto) {
    int index_mode = (value % (100 * int64_t(std::pow(10, param)))) / (10 * int64_t(std::pow(10, param)));
    int index = i + param;
    if (index_mode == 0) index = instructions[index];
    if (index_mode == 2) index = instructions[index] + relative_base;
    return instructions[index];
  };

  for (i = 0; instructions[i] != 99; ++i) {
    value = instructions[i];

    int64_t op_code = value % 100;
    auto& p1 = get_param(1);
    auto& p2 = get_param(2);
    auto& p3 = get_param(3);

    switch (op_code) {
      case 1:
        p3 = p1 + p2;
        i += 3;
        break;
      case 2:
        p3 = p1 * p2;
        i += 3;
        break;
      case 3:
        if (input.empty()) Rcpp::stop("Needs input");
        p1 = input.front();
        input.pop_front();
        i += 1;
        break;
      case 4:
        return p1;
      case 5:
        if (p1 != 0) {
          i = p2 - 1;
          continue;
        }
        i += 2;
        break;
      case 6:
        if (p1 == 0) {
          i = p2 - 1;
          continue;
        }
        i += 2;
        break;
      case 7:
        p3 = p1 < p2;
        i += 3;
        break;
      case 8:
        p3 = p1 == p2;
        i += 3;
        break;
      case 9:
        relative_base += p1;
        i += 1;
        break;
      default:
        Rcpp::stop("Unknown opcode: " + std::to_string(op_code));
    }
  }
  Rcpp::stop("Instructions finished");
}
',
  plugins = "cpp17"
)

scan_area <- function(instructions, rows = seq_len(50), cols = seq_len(50)) {
  m <- matrix(FALSE, nrow = length(rows), ncol = length(cols))
  for (row in rows) {
    for (col in cols) {
      m[row, col] <- run_instructions(instructions, c(col - 1, row - 1))
    }
  }
  m
}

m <- scan_area(sequence)
m %>% array_tree() %>% map(as.integer) %>% map_chr(str_c, collapse = "") %>% str_c(collapse = "\n") %>% cat()

answer <- sum(m)
answer

solve <- function(instructions, width = 100, height = 100) {
  check <- function(x, y) run_instructions(sequence, c(x, y))

  height <- height - 1
  width <- width - 1
  
  y <- 4
  x_right <- 5
  
  repeat {
    y_bottom <- y + height
    while (check(x_right + 1, y)) x_right <- x_right + 1
    x <- x_right - width

    if (check(x_right, y) && check(x, y_bottom)) return(c(x, y))

    y <- y + 1
  }
}

result <- solve(sequence)
result

answer <- 10000 * result[1] + result[2]
answer
