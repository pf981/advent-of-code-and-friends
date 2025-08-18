library(tidyverse)


sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

create_instructions <- function(instructions) {
  result <- structure(instructions, class = "instructions")
  attr(result, "relative_base") <- 0
  names(result) <- seq(from = 0, length.out = length(instructions))
  result
}

to_character <- function(x) format(x, scientific = FALSE)

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(v, i) {
  index <- i[[1]]
  if (i[[2]] == 0) {
    # Position mode
    index <- v[[to_character(index)]]
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- v[list(index, 1)] + attr(v, "relative_base")
  }
  index
}

`[.instructions` <- function(v, i) {
  index <- to_character(get_index(v, i))
  if (!(index %in% names(v))) v[[index]] <- 0
  result <- v[[index]]
  if (is.null(result) || is.na(result)) v[[index]] <- 0
  v[[index]]
}

`[<-.instructions` <- function(v, i, j, value) {
  v[[to_character(get_index(v, i))]] <- value
  v
}

run_bot <- function(bot, input = NULL) {
  bot$needs_input <- FALSE
  while (bot$instructions[list(bot$i, 1)] != 99) {
    value <- bot$instructions[list(bot$i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000
    
    p1 <- list(bot$i + 1, p1_index_mode)
    p2 <- list(bot$i + 2, p2_index_mode)
    p3 <- list(bot$i + 3, p3_index_mode)
    
    if (op_code == 1) {
      bot$instructions[p3] <- bot$instructions[p1] + bot$instructions[p2]
    } else if (op_code == 2) {
      bot$instructions[p3] <- bot$instructions[p1] * bot$instructions[p2]
    } else if (op_code == 3) {
      if (length(input) == 0) {
        bot$needs_input <- TRUE
        break
      }
      bot$instructions[p1] <- input[1]
      input <- input[-1]
      if (length(input) == 0) bot$needs_input <- TRUE
    } else if (op_code == 4) {
      bot$output <- bot$instructions[p1]
      num_params <- 1
      bot$i <- bot$i + 1 + num_params
      break
    } else if (op_code == 5) {
      if (bot$instructions[p1] != 0) {
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (bot$instructions[p1] == 0) {
        bot$i = get_index(bot$instructions, p2) - 1
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      bot$instructions[p3] <- bot$instructions[p1] < bot$instructions[p2]
    } else if (op_code == 8) {
      bot$instructions[p3] <- bot$instructions[p1] == bot$instructions[p2]
    } else if (op_code == 9) {
      attr(bot$instructions, "relative_base") <- attr(bot$instructions, "relative_base") + bot$instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', bot$i, '\n', paste0(bot$instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    bot$i <- bot$i + 1 + num_params
  }
  
  if (bot$instructions[list(bot$i, TRUE)] == 99) {
    bot$is_halted <- TRUE
  }

  bot
}

create_bot <- function(instructions) {
  list(
    instructions = create_instructions(instructions),
    i = 0,
    x = 0,
    y = 0,
    is_halted = FALSE,
    output = NULL
  )
}

get_output <- function(instructions) {
  result <- c()
  bot <- create_bot(instructions)
  while (!bot$is_halted) {
    bot <- run_bot(bot, 0)
    result <- c(result, bot$output)
  }
  intToUtf8(result)
}

result <- get_output(sequence)
result %>% cat()

m <-
  result %>%
  read_lines() %>%
  discard(~. == "") %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

scaffold_cords <- which(m == "#", arr.ind = TRUE) %>% as_tibble()
scaffold_cords

intersections <- sqldf::sqldf("
SELECT a.row, a.col, (a.row - 1) * (a.col - 1) AS alignment_parameter
FROM
  scaffold_cords a
  JOIN scaffold_cords b ON
    (
         (b.row == a.row + 0 AND b.col == a.col + 1)
      OR (b.row == a.row + 0 AND b.col == a.col - 1)
      OR (b.row == a.row + 1 AND b.col == a.col + 0)
      OR (b.row == a.row - 1 AND b.col == a.col + 0)
    )
GROUP BY 1, 2
HAVING COUNT(*) == 4
")
answer <- sum(intersections$alignment_parameter)
answer

result %>% cat()

# Solution is:
#   A: R,12,L,10,L,10,
#   B: L,6,L,12,R,12,L,4,
#   A: R,12,L,10,L,10,
#   B: L,6,L,12,R,12,L,4,
#   C: L,12,R,12,L,6,
#   B: L,6,L,12,R,12,L,4,
#   C: L,12,R,12,L,6,
#   A: R,12,L,10,L,10,
#   C: L,12,R,12,L,6,
#   C: L,12,R,12,L,6

input_sequence_str <- "A,B,A,B,C,B,C,A,C,C
R,12,L,10,L,10
L,6,L,12,R,12,L,4
L,12,R,12,L,6
n
"
input_sequence <- utf8ToInt(input_sequence_str)

bot <- create_bot(sequence)
bot$instructions[list(0, 1)] <- 2

while(length(input_sequence) > 0) {
  bot <- run_bot(bot, input_sequence[1])
  if (bot$needs_input) input_sequence <- input_sequence[-1]
  cat(intToUtf8(bot$output))
  bot$output <- NULL
}

while(!bot$is_halted) {
  bot <- run_bot(bot, NULL)
  if (bot$output > 256) break
  if (bot$needs_input) {
    message("Why would it need input?")
    break
  }
}

answer <- bot$output
answer
