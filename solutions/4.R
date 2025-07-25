library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))

View(products)

orders |>
  filter(hour(ordered) |> between(3, 5)) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  distinct(desc) |>
  View()


pastries <- c(
  "Caraway Bagel",
  "Caraway Bialy",
  "Caraway Puff",
  "Caraway Twist",
  "Poppyseed Babka",
  "Poppyseed Hamentash",
  "Poppyseed Linzer Cookie",
  "Poppyseed Mandelbrot",
  "Poppyseed Rugelach",
  "Poppyseed Sufganiah",
  "Raspberry Babka",
  "Raspberry Hamentash",
  "Raspberry Linzer Cookie",
  "Raspberry Mandelbrot",
  "Raspberry Rugelach",
  "Raspberry Sufganiah"
)

candidates <-
  customers |>
  inner_join(orders) |>
  filter(hour(shipped) |> between(3, 4)) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(desc %in% pastries) |>
  pull(customerid) |>
  unique()


customers |>
  filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  # filter(desc %in% pastries) |>
  mutate(hr = hour(shipped)) |>
  ggplot(aes(hr, fill=factor(customerid))) +
    geom_histogram(position = "identity", alpha = 0.5)


plotly::ggplotly()






customers |>
  # filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(desc %in% pastries) |>
  mutate(hr = hour(shipped)) |>
  filter(hr == 4) |>
  count(customerid, hr) |>
  arrange(desc(n))


2749
3903




customers |>
  filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  # filter(desc %in% pastries) |>
  mutate(hr = hour(shipped) <= 5) |>
  count(customerid, hr) |> View()
  ggplot(aes(hr, n)) +
  geom_point()








# filter(hour(ordered) |> between(3, 5)) |>


customers |>
  filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(customerid == 6818) |>
  View()




customers |>
  # filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  filter(desc %in% pastries) |>
  mutate(hr = hour(shipped)) |>
  count(customerid, hr) |>
  ggplot(aes(hr, n)) +
  geom_point(position = position_jitter(width = 0.1), alpha = 0.5)


customers |>
  # filter(customerid %in% candidates) |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  # filter(desc %in% pastries) |>
  mutate(hr = hour(shipped)) |>
  filter(hr == 3) |>
  count(customerid, hr) |>
  arrange(desc(n))


customers |>
  inner_join(orders) |>
  inner_join(orders_items) |>
  inner_join(products) |>
  # filter(customerid == 4233) |> # No
  # filter(customerid == 2752) |> # No
  # filter(customerid == 3431) |> # Maybe, but name is Connor
  filter(customerid == 2749) |>
  View()
