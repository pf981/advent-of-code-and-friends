library(tidyverse)



checksum <- function(x) {
  x %>%
    str_split("") %>%
    map_dfr(enframe, .id = "id") %>%
    filter(value != "-") %>%
    count(id, value) %>%
    group_by(id) %>%
    arrange(desc(n), value) %>%
    slice_head(n = 5) %>%
    summarise(check_str = str_c(value, collapse = "")) %>%
    arrange(as.integer(id)) %>%
    pull(check_str)
}

df <-
  tibble(line = read_lines(input)) %>%
  transmute(
    encrypted_name = str_extract(line, "[a-z-]+(?=-\\d)"),
    sector = str_extract(line, "\\d+") %>% parse_integer(),
    expected_checksum = str_extract(line, "\\w+(?=])"),
    actual_checksum = checksum(encrypted_name)
  )
df

answer <-
  df %>%
  filter(actual_checksum == expected_checksum) %>%
  pull(sector) %>%
  sum()
answer

decrypt <- function(encrypted_name, sector) {
  v <- str_split(encrypted_name, "") %>% first()
  sector <- sector %% 26
  
  key <- c(tail(letters, -sector), head(letters, sector), " ")
  names(key) <- c(letters, "-")
  
  key[v] %>% str_c(collapse = "")
}
decrypt("qzmt-zixmtkozy-ivhz", 343)

result <- 
  df %>%
  filter(actual_checksum == expected_checksum) %>%
  mutate(
    name = map2_chr(encrypted_name, sector, decrypt)
  )
result

answer <-
  result %>%
  filter(name == "northpole object storage") %>%
  pull(sector)
answer
