library(tidyverse)



str_lines <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
str_lines

constraints <-
  str_lines[[1]] %>%
  as_tibble() %>%
  separate(value, c("type", "value"), ": ") %>%
  mutate(
    type_id1 = row_number(),
    value = str_split(value, " or ") %>% map(~str_split(., "-") %>% map(parse_integer) %>% map(~seq(.[[1]], .[[2]])) %>% unlist())
  ) %>%
  unnest(value)
constraints

your_ticket <-
  str_lines[[2]][[2]] %>%
  str_split(",") %>%
  unlist() %>%
  parse_integer() %>%
  enframe(name = "type_id2") %>%
  add_column(ticket_id = 0)
your_ticket

nearby_tickets <-
  str_lines[[3]][-1] %>%
  str_split(",") %>%
  imap_dfr(~parse_integer(.x) %>% enframe(name = "type_id2") %>% add_column(ticket_id = .y))
nearby_tickets

error_values <- nearby_tickets$value %>% discard(~. %in% constraints$value)
error_values

answer <- sum(error_values)
answer

invalid_tickets <- nearby_tickets %>% filter(value %in% error_values) %>% pull(ticket_id)
valid_tickets <- nearby_tickets %>% filter(!(ticket_id %in% invalid_tickets))
valid_tickets

type_matches <-
  valid_tickets %>%
  inner_join(constraints) %>%
  group_by(type_id2, type_id1, type) %>%
  summarise(tickets = n_distinct(ticket_id)) %>%
  ungroup() %>%
  filter(tickets == max(tickets))
type_matches

final_matches <- NULL

repeat {
  new_matches <-
    type_matches %>%
    filter(
      !(type_id2 %in% final_matches$type_id2),
      !(type_id1 %in% final_matches$type_id1)
    ) %>%
    group_by(type_id2) %>%
    filter(n() == 1)
  
  if (nrow(new_matches) == 0) {
    break
  }
  
  final_matches <- bind_rows(final_matches, new_matches)
}
final_matches

answer <-
  your_ticket %>%
  inner_join(final_matches %>% select(type_id2, type)) %>%
  filter(str_starts(type, "departure")) %>%
  pull(value) %>%
  as.double() %>% # Too big for integer
  reduce(`*`)
format(answer, scientific = FALSE)
