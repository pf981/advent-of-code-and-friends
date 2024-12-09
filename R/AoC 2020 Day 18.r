devtools::install_github("tobcap/walkast")

library(tidyverse)
library(rlang)



eval_left_to_right <- function (math_string) {
  new_expr <- walkast::walk_ast(
    parse_expr(str_replace_all(math_string, fixed("*"), "-")), # Replace with a left-to-right operator
    walkast::make_visitor(
      hd = function(f) {
        if (f == "-") {
          `*`
        } else {
          f
        }
      }
    )
  )
  
  eval_tidy(new_expr)
}

math_strings <- read_lines(input)
results <- map_dbl(math_strings, eval_left_to_right)

answer <- sum(results)
format(answer, scientific = FALSE)

eval_new_precedence <- function (math_string) {
  new_expr <- walkast::walk_ast(
    parse_expr(chartr("*+", "+*", math_string)),
    walkast::make_visitor(
      hd = function(f) {
        if (f == "+") {
          `*`
        } else if (f == "*") {
          `+`
        } else {
          f
        }
      }
    )
  )
  
  eval_tidy(new_expr)
}

results <- map_dbl(math_strings, eval_new_precedence)
answer <- sum(results)
format(answer, scientific = FALSE)
