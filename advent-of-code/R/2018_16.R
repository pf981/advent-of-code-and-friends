library(tidyverse)



txt <-
  str_split(input, "\n\n\n\n") %>%
  first()

samples <-
  txt[[1]] %>%
  str_split("\n\n") %>%
  first() %>%
  str_split("\n") %>%
  str_extract_all("\\d+") %>%
  map(parse_integer) %>%
  map_dfr(function(nums) {
    tibble(
      opcode = nums[5],
      a = nums[6],
      b = nums[7],
      output_register = nums[8],
      before = list(head(nums, 4)),
      after = list(tail(nums, 4))
    )
  })
samples

instructions <-
  txt[[2]] %>%
  read_lines() %>%
  str_split(" ") %>%
  map(as.integer) %>%
  map_dfr(set_names, c("opcode", "a", "b", "output_register"))
instructions

execute <- function(op, a, b, output_register, registers) {
  if (op %in% c("addi", "addr", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "gtri", "gtrr", "eqri", "eqrr")) {
    a <- registers[[a + 1]]
  }
  if (op %in% c("addr", "mulr", "banr", "borr", "gtir", "gtrr", "eqir", "eqrr")) {
    b <- registers[[b + 1]]
  }
  
  output_register <- output_register + 1
  
  if (str_starts(op, "add")) {
    registers[[output_register]] <- a + b
  } else if (str_starts(op, "mul")) {
    registers[[output_register]] <- a * b
  } else if (str_starts(op, "ban")) {
    registers[[output_register]] <- bitwAnd(a, b)
  } else if (str_starts(op, "bor")) {
    registers[[output_register]] <- bitwOr(a, b)
  } else if (str_starts(op, "set")) {
    registers[[output_register]] <- a
  } else if (str_starts(op, "gt")) {
    registers[[output_register]] <- as.integer(a > b)
  } else if (str_starts(op, "eq")) {
    registers[[output_register]] <- as.integer(a == b)
  }
  
  registers
}

ops <- c("addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr")

get_possible_ops <- function(a, b, output_register, before, after) {
  result <- NULL
  for (op in ops) {
    if (all(execute(op, a, b, output_register, before) == after)) {
      result <- c(result, op)
    }
  }
  result
}

result <-
  samples %>%
  rowwise() %>%
  mutate(
    possible_ops = list(get_possible_ops(a, b, output_register, before, after)),
    num_ops = length(possible_ops)
  )
result

answer <- result %>% filter(num_ops >= 3) %>% nrow()
answer

find_mapping <- function(possible_mapping, op_mapping) {
  if (all(!is.na(op_mapping))) return(op_mapping)
  if (nrow(possible_mapping) == 0) return(NA)
  
  op_code <- possible_mapping$opcode[1]
  
  for (op in (possible_mapping %>% filter(opcode == op_code) %>% pull(possible_ops))) {
    new_op_mapping <- op_mapping
    new_op_mapping[op_code + 1] <- op
    
    new_possible_mapping <- possible_mapping %>% filter(opcode != op_code, possible_ops != op)
    
    result <- find_mapping(new_possible_mapping, new_op_mapping)
    if (!is.na(result[1])) return(result)
  }
  NA
}

possible_mapping <-
  result %>%
  ungroup() %>%
  distinct(opcode, possible_ops) %>%
  arrange(opcode) %>%
  mutate(row = row_number()) %>%
  group_by(opcode) %>%
  mutate(rows = n()) %>%
  unnest() %>%
  group_by(opcode, possible_ops) %>%
  filter(n_distinct(row) == rows) %>%
  distinct(opcode, possible_ops) %>%
  group_by(opcode) %>%
  mutate(n = n()) %>%
  arrange(n) %>%
  ungroup()
possible_mapping

op_mapping <- find_mapping(
  possible_mapping,
  rep(NA, result %>% pull(opcode) %>% unique() %>% length())
)
op_mapping

inst <- instructions %>% mutate(op = op_mapping[opcode + 1])
inst

registers <- rep(0, 4)
for (i in seq_len(nrow(inst))) {
  registers <- execute(inst$op[i], inst$a[i], inst$b[i], inst$output_register[i], registers)
}
registers

answer <- registers[1]
answer
