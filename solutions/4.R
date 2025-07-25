library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))


# Pastries' SKUs start with "BKY"
products |> arrange(sku) |> View()


candidates <-
  customers |>
  inner_join(orders) |>
  filter(
    hour(ordered) < 5,
    hour(shipped) < 5
  ) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(sku |> str_starts("BKY")) |>
  count(customerid) |>
  arrange(desc(n))

answer <-
  customers |>
  filter(customerid == candidates$customerid[1]) |>
  pull(phone)
print(answer)
