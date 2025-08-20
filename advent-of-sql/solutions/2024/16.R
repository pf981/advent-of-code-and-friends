library(sf)
library(tidyverse)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")

# Use json_array to just get it parsing
read_file("./data/2024/advent_of_sql_day_16.sql") |>
  str_replace_all("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") |>
  str_replace_all(fixed("GEOGRAPHY(POINT)"), "TEXT") |>
  str_replace_all("(GEOMETRY|GEOGRAPHY)\\((POLYGON|Point)(, \\d+)?\\)", "TEXT") |>
  str_replace_all("ST_Point|ST_SetSRID|ST_GeomFromText", "json_array") |>
  str_split_1(";") |>
  str_trim() |>
  discard(str_equal, "") |>
  walk(DBI::dbExecute, conn = con)

sleigh_locations <- tbl(con, "sleigh_locations") |>
  collect() |>
  mutate(
    coordinate = coordinate |>
      str_extract_all("-?\\d+(\\.\\d+)?") |>
      map(as.double) |>
      map(set_names, c("lon", "lat", "crs"))
  ) |>
  unnest_wider(coordinate) |>
  st_as_sf(coords = c("lon", "lat"), crs = 4326)

areas <- tbl(con, "areas") |>
  collect() |>
  mutate(
    polygon = polygon |> str_extract("POLYGON\\(.*\\)")
  ) |>
  st_as_sf(wkt = "polygon", crs = 4326)

st_join(sleigh_locations, areas, join = st_within) |>
  mutate(
    timestamp = ymd_hms(timestamp),
    next_timestamp = lead(timestamp)
  ) |>
  group_by(place_name) |>
  summarise(
    arrive = min(timestamp),
    depart = max(next_timestamp, na.rm = TRUE),
    total_hours_spent = (depart - arrive) / dhours(1)
  ) |>
  slice_max(total_hours_spent) |>
  pull(place_name)
# Paris
