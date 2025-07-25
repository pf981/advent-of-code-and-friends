library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))


collector <-
  customers |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(sku |> str_starts("COL")) |>
  group_by(customerid) |>
  mutate(n = sku |> unique() |> length()) |>
  arrange(desc(n)) |>
  head(1)

answer <- collector$phone
print(answer)
#> [1] "212-547-3518"
