library(tidyverse)



sequence <- str_split(input, ",") %>% unlist() %>% parse_double()
sequence

Rcpp::sourceCpp(code = '
// [[Rcpp::plugins(cpp17)]]
#include <Rcpp.h>

class Bot {
  private:
    std::map<int64_t, int64_t> instructions;
    int64_t relative_base;
    int64_t i;
    std::vector<int64_t> partial_output;

    int64_t& get_param(int64_t value, int param) {
      int64_t index_mode = (value % (100 * int64_t(std::pow(10, param)))) / (10 * int64_t(std::pow(10, param)));
      int64_t index = i + param;
      if (index_mode == 0) index = instructions[index];
      if (index_mode == 2) index = instructions[index] + relative_base;
      return instructions[index];
    }

  public:
    std::deque<int64_t> input;
    std::deque<std::tuple<int64_t, int64_t, int64_t>> output;

    Bot(std::vector<int64_t> sequence) : instructions(), relative_base(0), i(0), partial_output(), input(), output() {
      for (int j = 0; j < sequence.size(); ++j) {
        instructions[j] = sequence[j];
      }
    }

    void run(int n_commands) {
      for (; instructions[i] != 99; ++i) {
        if (n_commands-- <= 0) return;

        int64_t value = instructions[i];

        int64_t op_code = value % 100;
        auto& p1 = get_param(value, 1);
        auto& p2 = get_param(value, 2);
        auto& p3 = get_param(value, 3);

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
            if (input.empty()) {
              p1 = -1;
            }
            else {
              p1 = input.front();
              input.pop_front();
            }
            i += 1;
            break;
          case 4:
            partial_output.push_back(p1);
            if (partial_output.size() == 3) {
              output.push_back(std::make_tuple(partial_output[0], partial_output[1], partial_output[2]));
              partial_output.clear();
            }
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
};

// [[Rcpp::export]]
int64_t solve(std::vector<int64_t> sequence) {
  std::vector<Bot> bots(50, sequence);

  for (int j = 0; j < bots.size(); ++j) {
    bots[j].input.push_back(j);
  }

  while (true) {
    for (auto& bot : bots) {
      bot.run(100);
      for (auto [destination, x, y] : bot.output) {
        if (destination == 255) return y;

        bots[destination].input.push_back(x);
        bots[destination].input.push_back(y);
      }
      bot.output.clear();
    }
  }
}
'
)

answer <- solve(sequence)
answer

Rcpp::sourceCpp(code = '
// [[Rcpp::plugins(cpp17)]]
#include <Rcpp.h>

class Bot {
  private:
    std::map<int64_t, int64_t> instructions;
    int64_t relative_base;
    int64_t i;
    std::vector<int64_t> partial_output;

    int64_t& get_param(int64_t value, int param) {
      int64_t index_mode = (value % (100 * int64_t(std::pow(10, param)))) / (10 * int64_t(std::pow(10, param)));
      int64_t index = i + param;
      if (index_mode == 0) index = instructions[index];
      if (index_mode == 2) index = instructions[index] + relative_base;
      return instructions[index];
    }

  public:
    std::deque<int64_t> input;
    std::deque<std::tuple<int64_t, int64_t, int64_t>> output;
    bool is_idle;

    Bot(std::vector<int64_t> sequence) : instructions(), relative_base(0), i(0), partial_output(), input(), output(), is_idle(false) {
      for (int j = 0; j < sequence.size(); ++j) {
        instructions[j] = sequence[j];
      }
    }

    void run(int n_commands) {
      is_idle = false;
      for (; instructions[i] != 99; ++i) {
        if (n_commands-- <= 0) return;

        int64_t value = instructions[i];

        int64_t op_code = value % 100;
        auto& p1 = get_param(value, 1);
        auto& p2 = get_param(value, 2);
        auto& p3 = get_param(value, 3);

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
            if (input.empty()) {
              p1 = -1;
              is_idle = true;
            }
            else {
              p1 = input.front();
              input.pop_front();
            }
            i += 1;
            break;
          case 4:
            partial_output.push_back(p1);
            if (partial_output.size() == 3) {
              output.push_back(std::make_tuple(partial_output[0], partial_output[1], partial_output[2]));
              partial_output.clear();
            }
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
};

// [[Rcpp::export]]
int64_t solve2(std::vector<int64_t> sequence) {
  std::vector<Bot> bots(50, sequence);
  std::pair<int64_t, int64_t> nat;
  std::set<std::pair<int64_t, int64_t>> nat_sent;
  int idle_count = 0;

  for (int j = 0; j < bots.size(); ++j) {
    bots[j].input.push_back(j);
  }

  while (true) {
    for (auto& bot : bots) {
      bot.run(100);
      for (auto [destination, x, y] : bot.output) {
        if (destination == 255) {
          nat = std::make_pair(x, y);
          continue;
        }

        bots[destination].input.push_back(x);
        bots[destination].input.push_back(y);
      }
      bot.output.clear();
      if (!bot.is_idle) idle_count = 0;
    }

    if (idle_count++ >= 3) {
      idle_count = 0;
      if (nat_sent.find(nat) != nat_sent.end()) return nat.second;
      nat_sent.insert(nat);
      bots[0].input.push_back(nat.first);
      bots[0].input.push_back(nat.second);
    }
  }
}
'
)

answer <- solve2(sequence)
answer
