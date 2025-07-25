library(tidyverse)

data_path <- "data/5784"

customers <- read_csv(file.path(data_path, "noahs-customers.csv"))
orders_items <- read_csv(file.path(data_path, "noahs-orders_items.csv"))
orders <- read_csv(file.path(data_path, "noahs-orders.csv"))
products <- read_csv(file.path(data_path, "noahs-products.csv"))

# "lived in my neighborhood"
contractor_city <-
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
  filter(year(ordered) == 2017) |>
  pull(citystatezip) |>
  unique()


# "Cancer born in the year of the Rabbit"

# https://en.wikipedia.org/wiki/Rabbit_(zodiac)
year_of_rabbit <- tribble(
  ~start_date, ~end_date,
  "29 January 1903",	"15 February 1904",
  "14 February 1915",	"3 February 1916",
  "2 February 1927",	"22 January 1928",
  "19 February 1939",	"7 February 1940",
  "6 February 1951",	"26 January 1952",
  "25 January 1963",	"12 February 1964",
  "11 February 1975",	"30 January 1976",
  "29 January 1987",	"16 February 1988",
  "16 February 1999",	"4 February 2000",
  "3 February 2011",	"22 January 2012",
  "22 January 2023",	"9 February 2024",
  "8 February 2035",	"27 January 2036",
  "26 January 2047",	"13 February 2048",
  "11 February 2059",	"1 February 2060",
  "31 January 2071",	"18 February 2072",
  "17 February 2083",	"5 February 2084",
  "5 February 2095",	"24 January 2096"
) |>
  mutate(across(everything(), dmy))

cancer_ints <- c(621, 722)

new_contractor <-
  customers |>
  cross_join(year_of_rabbit) |>
  filter(
    birthdate |> between(start_date, end_date),
    (100 * month(birthdate) + day(birthdate)) |> between(!!!cancer_ints),
    citystatezip == contractor_city
  )

answer <- new_contractor$phone
print(answer)
#> [1] "917-288-9635"
