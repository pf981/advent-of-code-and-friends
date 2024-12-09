library(tidyverse)



sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

Rcpp::cppFunction('
int64_t run_instructions(std::vector<int> sequence, std::deque<int> input) {
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
        if (p1 > 256) return p1;
        std::cout << char(p1);
        i += 1;
        break;
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

# When you jump, you land on D

# NOT A J                    Jump if there is no next square .???
# NOT C T; AND D T; OR T J   Jump if ??.#    (NOT C AND D)

input_str <- "NOT A J
NOT C T
AND D T
OR T J
WALK
"

answer <- run_instructions(sequence, utf8ToInt(input_str))
answer

# If B or C is a hole, jump
#   NOT B J
#   NOT C T
#   OR T J

# If A is a hole, jump
#   NOT A T
#   OR T J

# If D is a hole, don't jump
#   AND D J

# If E is a hole and H is a hole, don't jump
#   NOT E T
#   AND H T
#   OR E T
#   AND T J

input_str <- "NOT B J
NOT C T
OR T J
NOT A T
OR T J
AND D J
NOT E T
AND H T
OR E T
AND T J
RUN
"

answer <- run_instructions(sequence, utf8ToInt(input_str))
answer
