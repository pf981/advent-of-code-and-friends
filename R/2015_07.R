library(tidyverse)



# 

df <-
  tibble(instruction = read_lines(input)) %>%
  mutate(
    operation = case_when(
      str_detect(instruction, "^\\w+ ->") ~ "SET",
      str_detect(instruction, " AND ") ~ "AND",
      str_detect(instruction, " OR ") ~ "OR",
      str_detect(instruction, " LSHIFT ") ~ "LSHIFT",
      str_detect(instruction, " RSHIFT ") ~ "RSHIFT",
      str_detect(instruction, "^NOT ") ~ "NOT",
    ),
    a = str_extract(instruction, "^\\w+"),
    b = str_extract(instruction, "\\w+(?= ->)"),
    output_wire = str_extract(instruction, "\\w+$")
  )

df

cache <- list()

v <- function(wire) {
  if (!is.null(cache[[wire]])) {
    return(cache[[wire]])
  }
  value <- parse_number(wire) %>% suppressWarnings()
  if (!is.na(value)) {
    # message(glue::glue("Static: {value}"))
    return(value)
  }
  
  details <- df %>% filter(output_wire == wire)
  
  operation <- details$operation
  a <- details$a
  b <- details$b
  # output_wire <- details$output_wire
  # message(glue::glue("{a} {operation} {b} -> {wire}"))
  
  if (operation == "SET") {
    cache[[wire]] <<- v(b)
  } else if (operation == "AND") {
    cache[[wire]] <<- bitwAnd(v(a), v(b))
  } else if (operation == "OR") {
    cache[[wire]] <<- bitwOr(v(a), v(b))
  } else if (operation == "LSHIFT") {
    cache[[wire]] <<- bitwShiftL(v(a), v(b))
  } else if (operation == "RSHIFT") {
    cache[[wire]] <<- bitwShiftR(v(a), v(b))
  } else if (operation == "NOT") {
    cache[[wire]] <<- 65535 + bitwNot(v(b)) + 1
  }
  cache[[wire]]
}

answer <- v("a")
answer

# cache[order(names(cache))]

cache <- list(b = 16076)

answer <- v("a")
answer
