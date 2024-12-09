library(tidyverse)



ip_register <- read_lines(input, n_max = 1) %>% str_extract("\\d+") %>% parse_integer()
ip_register

instructions <-
  read_lines(input, skip = 1) %>%
  str_split(" ") %>%
  map_dfr(set_names, c("op", "a", "b", "output_register")) %>%
  mutate_at(vars(-op), parse_integer)
instructions

Rcpp::cppFunction('
int solve_cpp(int ip_register, std::vector<std::string> ops, std::vector<int> as, std::vector<int> bs, std::vector<int> output_registers) {
  int ip = 0;
  int registers[6] = {0};
  
  while (true) {
    std::string op = ops[ip];
    int a = as[ip];
    int b = bs[ip];
    int output_register = output_registers[ip];
    
    // Execute instruction
    if (op == "addi" || op == "addr" || op == "mulr" || op == "muli" || op == "banr" || op == "bani" || op == "borr" || op == "bori" || op == "setr" || op == "gtri" || op == "gtrr" || op == "eqri" || op == "eqrr") {
      a = registers[a];
    }
    if (op == "addr" || op == "mulr" || op == "banr" || op == "borr" || op == "gtir" || op == "gtrr" || op == "eqir" || op == "eqrr") {
      b = registers[b];
    }
    
    if (op == "addr" || op == "addi") {
      registers[output_register] = a + b;
    } else if (op == "mulr" || op == "muli") {
      registers[output_register] = a * b;
    } else if (op == "banr" || op == "bani") {
      registers[output_register] = a & b;
    } else if (op == "borr" || op == "bori") {
      registers[output_register] = a | b;
    } else if (op == "setr" || op == "seti") {
      registers[output_register] = a;
    } else if (op == "gtir" || op == "gtri" || op == "gtrr") {
      registers[output_register] = a > b;
    } else if (op == "eqir" || op == "eqri" || op == "eqrr") {
      registers[output_register] = a == b;
    }
    
    
    if (registers[ip_register] + 1 >= ops.size()) break;
  
    registers[ip_register] = registers[ip_register] + 1;
    ip = registers[ip_register];
  }
  
  return registers[0];
}
')

answer <- solve_cpp(
  ip_register = ip_register,
  ops = instructions$op,
  as = instructions$a,
  bs = instructions$b,
  output_registers = instructions$output_register
)
answer

# Sum of factors of 10551403
x <- 10551403
div <- seq_len(x)
factors <- div[x %% div == 0]
answer <- sum(factors)
answer
