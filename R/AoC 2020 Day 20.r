library(tidyverse)



str_rev <- stringi::stri_reverse

parse_tile <- function(x) {
  l <- read_lines(x)
  
  tile_id <- parse_number(l[[1]])
  
  lst(
    tile_id = parse_number(l[[1]]),
    m = str_split(l[-1], "") %>% unlist() %>% matrix(ncol = nchar(l[[2]]), byrow = TRUE)
  )
}

get_edges <- function(tile_info) {
  tile_id <- tile_info$tile_id
  m <- tile_info$m
  tibble(
    tile_id = tile_id,
    north = str_c(m[1,], collapse = ""),
    east = str_c(m[,ncol(m)], collapse = ""),
    south = str_c(rev(m[nrow(m),]), collapse = ""),
    west = str_c(rev(m[,1]), collapse = "")
  )
}

explode <- function(tiles) {
  result <- bind_rows(
    tiles %>% add_column(is_inverted = FALSE),
    tibble(
      tile_id = tiles$tile_id,
      north = str_rev(tiles$north),
      east = str_rev(tiles$west),
      south = str_rev(tiles$south),
      west = str_rev(tiles$east),
      is_inverted = TRUE
    )
  )
  
  result %>%
    mutate(orientation = list(1:4)) %>%
    unnest_longer(orientation) %>%
    mutate(
      n = case_when(
        orientation == 1 ~ north,
        orientation == 2 ~ east,
        orientation == 3 ~ south,
        orientation == 4 ~ west
      ),
      w = case_when(
        orientation == 1 ~ west,
        orientation == 2 ~ north,
        orientation == 3 ~ east,
        orientation == 4 ~ south
      ),
      s = case_when(
        orientation == 1 ~ south,
        orientation == 2 ~ west,
        orientation == 3 ~ north,
        orientation == 4 ~ east
      ),
      e = case_when(
        orientation == 1 ~ east,
        orientation == 2 ~ south,
        orientation == 3 ~ west,
        orientation == 4 ~ north
      )
    ) %>%
    transmute(
      tile_id_original = tile_id,
      tile_id = str_c(tile_id, "_", orientation, ifelse(is_inverted, "i", "")),
      n,
      e,
      s,
      w
    )
}

tiles_m <-
  input %>%
  str_split("\n\n") %>%
  unlist() %>%
  map(parse_tile)
tiles_m

tiles <-
  tiles_m %>%
  map_dfr(get_edges)
tiles

tiles_exploded <- explode(tiles)
tiles_exploded

place_tile <- function(placed_tile_mat, tiles, to_place_tile_id, i, j, width, debug = FALSE) {
  verbose <- if (debug) message else function(...) invisible()
  
  verbose(paste0("Trying ", to_place_tile_id, " in ", i, ", ", j, "."))
  this_tile <- tiles %>% filter(tile_id == to_place_tile_id)
  
  required_north <- ifelse(
    j > 1,
    str_rev(tiles$s[tiles$tile_id == placed_tile_mat[i, j - 1]]),
    this_tile$n
  )
  required_west <- ifelse(
    i > 1,
    str_rev(tiles$e[tiles$tile_id == placed_tile_mat[i - 1, j]]),
    this_tile$w
  )
  
  verbose(glue::glue("Required n:{required_north}; w:{required_west}"))
  verbose(glue::glue("Actual n:{this_tile$n}; w:{this_tile$w}"))

  if (this_tile$n != required_north || this_tile$w != required_west) {
    return(NA)
  }
  
  verbose(paste0("Placing ", to_place_tile_id, " in ", i, ", ", j, "."))
  
  placed_tile_mat[i, j] <- to_place_tile_id
  if (i == width && j == width) {
    return(placed_tile_mat)
  }
  
  # Remove tile
  # tiles <- tiles %>% filter(tile_id_original != this_tile$tile_id_original)
  remaining_tiles <- tiles %>% filter(!(tile_id_original %in% parse_number(placed_tile_mat)))
  i <- i + 1
  if (i > width) {
    i <- 1
    j <- j + 1
  }
  
  # Iterate through remaining tiles and place_tile
  for (new_tile_id in remaining_tiles$tile_id) {
    result <- place_tile(placed_tile_mat, tiles, new_tile_id, i, j, width, debug)
    if (!is.na(result)) {
      return(result)
    }
  }
  return(NA)
}

solve <- function(tiles_exploded, debug = FALSE) {
  width <- tiles_exploded %>% pull(tile_id_original) %>% unique() %>% length() %>% sqrt()

  for (to_place_tile_id in tiles_exploded$tile_id) {
    result <- place_tile(
      matrix(NA, nrow = width, ncol = width),
      tiles_exploded,
      to_place_tile_id,
      i = 1,
      j = 1,
      width = width,
      debug = debug
    )
    if (!is.na(result)) {
      return(result)
    }
  }
  NA
}

result <- solve(tiles_exploded)
result # 18 minutes

corners <- c(
  result[1, 1],
  result[1, ncol(result)],
  result[nrow(result), ncol(result)],
  result[nrow(result), 1]
) %>%
  parse_number()
corners

answer <- reduce(corners, `*`)
format(answer, scientific = FALSE)

rotate <- function(x) apply(t(x), 2, rev)

get_trimmed_tile <- function(original_tile_id, orientation, is_inverted) {
  m <-
    tiles_m %>%
    keep(~.$tile_id == original_tile_id) %>%
    `[[`(1) %>%
    `[[`("m")
  
  if (is_inverted) {
    m <- t(apply(m, 1, rev))
  }

  if (orientation > 1) {
    for (i in seq(from = 2, to = orientation, by = 1)) {
      m <- rotate(m)
    }
  }
  
  m[c(-1, -nrow(m)), c(-1, -ncol(m))]
}

coords <-
  cbind(as.character(result), which(result == result, arr.ind = TRUE)) %>%
  as_tibble() %>%
  transmute(
    tile_id = V1,
    x = as.integer(row),
    y = as.integer(col)
  )
coords

map_tiles <-
  coords %>%
  mutate(
    s = asplit(str_match(tile_id, "(\\d+)_(\\d)(i?)"), 1),
    original_tile_id = map_chr(s, 2),
    orientation = map_int(s, ~as.integer(.[3])),
    is_inverted = map_lgl(s, ~.[4] == "i")
  ) %>%
  select(-s) %>%
  mutate(m = pmap(lst(original_tile_id, orientation, is_inverted), get_trimmed_tile))
map_tiles

img_m <-
  map_tiles %>%
  group_by(y) %>%
  arrange(x) %>%
  summarise(m = list(reduce(m, cbind))) %>%
  ungroup() %>%
  arrange(y) %>%
  summarise(m = list(reduce(m, rbind))) %>%
  pull(m) %>%
  first()

monster <- "                  # 
#    ##    ##    ###
 #  #  #  #  #  #   " %>%
  read_lines() %>%
  str_split("") %>%
  simplify2array() %>%
  t()
monster

show_monster <- function(mat, monster) {
  if (sum(monster == mat) == sum(monster == "#")) {
    mat[monster == "#"] <- "O"
  }
  
  mat
}

monster_mats <- list(
  monster,
  rotate(monster),
  rotate(rotate(monster)),
  rotate(rotate(rotate(monster))),
  
  t(apply(monster, 1, rev)),
  rotate(t(apply(monster, 1, rev))),
  rotate(rotate(t(apply(monster, 1, rev)))),
  rotate(rotate(rotate(t(apply(monster, 1, rev)))))
)

result <- img_m
for (monster_mat in monster_mats) {
  for (x in seq_len(ncol(result) - ncol(monster_mat) + 1)) {
    for (y in seq_len(nrow(result) - nrow(monster_mat) + 1)) {
      result[y:(y + nrow(monster_mat) - 1), x:(x + ncol(monster_mat) - 1)] <- show_monster(result[y:(y + nrow(monster_mat) - 1), x:(x + ncol(monster_mat) - 1)], monster_mat)
    }
  }
  result
}
result

answer <- sum(result == "#")
answer
