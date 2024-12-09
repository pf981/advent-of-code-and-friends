library(tidyverse)



# 

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    instruction = str_extract(line, "^\\w+"),
    x = str_extract(line, "(?<= )-?\\w+"),
    y = str_extract(line, "-?\\w+$")
  )
df

get_value <- function(state, x) {
  value <- suppressWarnings(parse_integer(x))
  if (is.na(value)) {
    value <- state[[x]]
  }
  if (is.null(value)) {
    value <- 0
  }
  value
}

cpy <- function(state, x, y) {
  value <- get_value(state, x)
  
  state[[y]] <- value
  state[["line"]] <- state[["line"]] + 1
  state
}

inc <- function(state, x, y) {
  state[[x]] <- get_value(state, x) + 1
  state[["line"]] <- state[["line"]] + 1
  state
}

dec <- function(state, x, y) {
  state[[x]] <- get_value(state, x) - 1
  state[["line"]] <- state[["line"]] + 1
  state
}

jnz <- function(state, x, y) {
  jump <- 1
  if (get_value(state, x) != 0) {
    jump <- get_value(state, y)
  }
  
  state[["line"]] <- state[["line"]] + jump
  state
}

state <- list(line = 1, a = 0, b = 0)

while (state$line <= nrow(df)) {
  inst <- df %>% slice(state$line)
  
  f <- get(inst$instruction)
  state <- f(state, inst$x, inst$y)
}
state # Took 1.3 hrs

answer <- state$a
answer

# This R solution was way too slow, so I did it in c++

# get_value <- function(state, x) {
#   value <- as.integer(x)
#   if (is.na(value)) {
#     value <- state[[x]]
#   }
#   if (is.null(value)) {
#     value <- 0
#   }
#   value
# }

# line <- 1
# state <- list(c = 1)
# while (line <= nrow(df)) {
#   instruction <- df$instruction[line]
#   x <- df$x[line]
#   y <- df$y[line]
  
#   if (instruction == "cpy") {
    
#   } else if (instruction == "cpy") {
#     state[[y]] <- get_value(state, x)
#   } else if (instruction == "inc") {
#     state[[x]] <- get_value(state, x) + 1
#   } else if (instruction == "dec") {
#     state[[x]] <- get_value(state, x) - 1
#   } else if (instruction == "jnz") {
#     if (get_value(state, x) != 0) {
#       line <- line + get_value(state, y) - 1
#     }
#   }
  
#   line <- line + 1
# }

# answer <- state$a
# answer

Rcpp::cppFunction('
int solve_cpp(std::vector<std::string> instructions, std::vector<std::string> xs, std::vector<std::string> ys) { 
    std::unordered_map<std::string, int> registers;
    registers["c"] = 1;

    auto getValue = [&registers] (const std::string& s) {
      try {
        return std::stoi(s);
      }
      catch (...) {
        return registers[s];
      }
    };

    for(int line = 0; line < instructions.size(); ++line) {
        const std::string& instruction = instructions[line];
        const std::string& x = xs[line];
        const std::string& y = ys[line];

        if (instruction == "cpy") {
          registers[y] = getValue(x);
        }
        else if (instruction == "inc") {
          ++registers[x];
        }
        else if (instruction == "dec") {
          --registers[x];
        }
        else if (instruction == "jnz")  {
          if (getValue(x) != 0) {
            line = line + getValue(y) - 1;
          }
        }
    }

    return registers["a"];
} 
')

answer <- solve_cpp(df$instruction, df$x, df$y)
answer
