library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))

cheapskate <-
  customers |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  mutate(wholesale_ratio = unit_price / wholesale_cost) |>
  filter(wholesale_ratio < 1) |> # Losing money
  group_by(customerid) |>
  mutate(n = n()) |>
  arrange(desc(n)) |>
  head(1)

answer <- cheapskate$phone
print(answer)
#> [1] "585-838-9161"
