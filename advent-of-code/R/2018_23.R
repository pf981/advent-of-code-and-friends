library(tidyverse)



df <-
  read_lines(input) %>%
  str_extract_all("-?\\d+") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("x", "y", "z", "r"))
df

in_range <- sqldf::sqldf("
SELECT a.x, a.y, a.z, a.r, COUNT(*) AS n_in_range
FROM
  df a
  JOIN df b ON
    ABS(b.x - a.x) + ABS(b.y - a.y) + ABS(b.z - a.z) <= a.r
GROUP BY 1, 2, 3, 4
ORDER BY a.r DESC, n_in_range DESC
")
in_range

answer <- in_range %>% pull(n_in_range) %>% first()
answer

smt2 <- function(commands, bin_path = "z3", args = "-smt2") {
  file_name <- tempfile(fileext = ".smt")
  write_lines(commands, file_name)
  result <- system(glue::glue("{bin_path} {args} {file_name}"), intern = TRUE)
  file.remove(file_name)
  result
}

bot_constraints <-
  df %>%
  # This is essentially ifelse(bot_is_in_range, 1, 0)
  glue::glue_data("(ite
  (<=
    (+
     (abs (- x {x}))
     (abs (- y {y}))
     (abs (- z {z}))
    )
    {r}
  )
  1
  0
)") %>%
  str_c(collapse = "\n")

# Find x, y, z that maximizes the number of bots in range and minimizes the distance to the origin.
smt2_command <- glue::glue("
(declare-const x Int)
(declare-const y Int)
(declare-const z Int)
(maximize (+
  {bot_constraints}
))
(minimize (+ (abs x) (abs y) (abs z)))
(check-sat)
(eval x)
(eval y)
(eval z)
")
smt2_command

result <- smt2(smt2_command)
result

answer <-
  result %>%
  tail(3) %>%
  parse_integer() %>%
  abs() %>%
  sum()
answer
