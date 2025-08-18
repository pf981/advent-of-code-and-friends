library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))

glimpse(customers)


keypad <-
  c(2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9) |>
  set_names(str_split_1("abcdefghijklmnopqrstuvwxyz", ""))

names_to_phone <- function(last_names) {
  last_names |>
    str_split("") |>
    map(map_int, \(ch) {keypad[ch]}) |>
    map_chr(str_c, collapse = "")
}

investigators_phone <-
  customers |>
  mutate(
    last_name =
      name |>
      str_split(" ") |>
      map_chr(\(first_last) first_last[[2]]) |>
      str_to_lower() |>
      str_replace_all("[^a-z]", ""),
    phone_stripped = phone |> str_replace_all("[^0-9]", ""),
    expected_phone = last_name |> names_to_phone()
  ) |>
  filter(phone_stripped == expected_phone) |>
  pull(phone)

answer <- investigators_phone
print(answer)
#> [1] "826-636-2286"