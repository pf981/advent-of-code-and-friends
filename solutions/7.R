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


color_orders <-
  customers |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(sku |> str_starts("COL")) |>
  mutate(
    order_hour = ordered |> floor_date("hours"),
    df =
      desc |>
      str_match("(.*) \\((.*)\\)") |>
      as_tibble() |>
      select(item_name = V2, item_color = V3)
  ) |>
  unnest(df)


meet_cute <- color_orders |>
  filter(customerid == cheapskate$customerid) |>
  select(order_hour, item_name, item_color) |>
  inner_join(color_orders, by = c("order_hour", "item_name")) |>
  filter(customerid != cheapskate$customerid)


answer <- meet_cute$phone
print(answer)
#> [1] "838-335-7157"
