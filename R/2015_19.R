library(tidyverse)



input2 <- "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

# 

# input2 <- "HOH"

replacements <-
  tibble(line = read_lines(input)) %>%
  separate(line, into = c("from", "to"), sep = " => ")
replacements

str_replace_position <- function(s, start, end, replacement) {
  str_sub(s, start, end) <- replacement
  s
}

output <-
  replacements %>%
  mutate(
    locations = str_locate_all(input2, from)
  ) %>%
  unnest_longer(locations) %>%
  mutate(
    start = locations[,1],
    end = locations[,2],
    result = str_replace_position(input2, start, end, to)
  ) %>%
  select(-locations)

output

answer <- output %>% distinct(result) %>% filter(!is.na(result)) %>% nrow()
answer

# Just randomly try steps. This isn't guaranteed to always get the right answer.
calculate_steps <- function(molecule = input2) {
  mol <- molecule
  n_steps <- 0

  repeat {
    if (mol == "e") {
      return(n_steps)
    }
    
    cur_replacements <-
      replacements %>%
      filter(str_detect(mol, to)) %>%
      slice_sample(n = 1)
    
    if (nrow(cur_replacements) == 0) {
      mol <- molecule
      n_steps <- 0
      next
    }
    
    cur_replacements <-
      cur_replacements %>%
      mutate(locations = str_locate_all(mol, to)) %>%
      unnest_longer(locations) %>%
      mutate(
        start = locations[,1],
        end = locations[,2],
        result = str_replace_position(mol, start, end, from)
      )
    
    mol <- cur_replacements %>% slice_sample(n = 1) %>% pull(result)

    n_steps <- n_steps + 1
  }
}

answer <- calculate_steps()
answer
