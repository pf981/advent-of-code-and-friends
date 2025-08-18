library(tidyverse)



block_counts <- str_split(input, "\t") %>% unlist() %>% parse_integer()
block_counts

redistribute <- function(block_counts, i) {
  remaining <- block_counts[i]
  block_counts[i] <- 0
  x <- i
  while (remaining > 0) {
    x <- x + 1
    if (x > length(block_counts)) {
      x <- x - length(block_counts)
    }
    
    block_counts[x] <- block_counts[x] + 1
    remaining <- remaining - 1
  }
  block_counts
}

hash <- function(x) str_c(x, collapse = ",")

count_cycles <- function(block_counts) {
  done <- c(hash(block_counts))
  cycles <- 0
  
  repeat {
    cycles <- cycles + 1
    block_counts <- redistribute(block_counts, which.max(block_counts)[1])
    new_hash <- hash(block_counts)
    
    if (new_hash %in% done) {
      return(cycles)
    }
    done <- c(done, new_hash)
  }
}

answer <- count_cycles(block_counts)
answer

count_cycles2 <- function(block_counts) {
  first_seen <- list()
  first_seen[[hash(block_counts)]] <- 1
  cycles <- 0
  
  repeat {
    cycles <- cycles + 1
    block_counts <- redistribute(block_counts, which.max(block_counts)[1])
    new_hash <- hash(block_counts)
    
    if (!is.null(first_seen[[new_hash]])) {
      return(cycles - first_seen[[new_hash]])
    }
    first_seen[[new_hash]] <- cycles
  }
}

count_cycles2(block_counts)
