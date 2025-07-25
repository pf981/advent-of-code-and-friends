library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))


# "senior" "cat"
products |> arrange(sku) |> View()

"Staten Island came to pick it up. She was wearing a ‘Noah’s Market’ sweatshirt, and it was just covered in cat hair"

cat_lady <-
  customers |>
  filter(citystatezip |> str_detect("Staten Island")) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(
    desc |> str_to_lower() |> str_detect("cat"),
    desc |> str_to_lower() |> str_detect("senior")
  ) |>
  group_by(customerid) |> 
  mutate(n = n()) |>
  arrange(desc(n)) |>
  head(1)

answer <- cat_lady$phone
print(answer)
#> "631-507-6048"
