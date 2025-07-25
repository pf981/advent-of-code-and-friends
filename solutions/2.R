library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))

glimpse(customers)
glimpse(orders_items)
glimpse(orders)
glimpse(products)


contractor <-
  customers |>
  mutate(
    initials =
      name |>
      str_extract_all("[A-Z]([^ ]*) ?") |>
      map(str_sub, 1, 1) |>
      map_chr(str_c, collapse = "")
  ) |>
  filter(initials == "JP") |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(desc |> str_to_lower() |> str_detect("coffee|bagel")) |>
  filter(year(ordered) == 2017)

answer <- contractor |> pull(phone) |> unique()
print(answer)
#> [1] "332-274-4185"
