library(tidyverse)



input2 <- "Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"

boss <-
  tibble(line = read_lines(input)) %>%
  separate(line, into = c("name", "value"), sep = ": ", convert = TRUE) %>%
  mutate(name = name %>% str_to_lower() %>% str_replace_all(" ", "_")) %>%
  pivot_wider()
boss

shop <-
  input2 %>%
  str_split("\n\n", simplify = TRUE) %>%
  map_dfr(
    read_table,
    col_names = c("item", "cost", "damage", "armor"),
    skip = 1,
    .id = "shop_name"
  ) %>%
  mutate(
    shop_name = c("weapons", "armor", "rings")[as.integer(shop_name)]
  )

shop

does_win <- function(damage, armor, boss_hit_points = boss$hit_points, boss_damage = boss$damage, boss_armor = boss$armor) {
  damage <- max(damage - boss_armor, 1)
  boss_damage <- max(boss_damage - armor, 1)
  hit_points <- 100
  
  repeat {
    boss_hit_points <- boss_hit_points - damage
    hit_points <- hit_points - boss_damage
    
    if (boss_hit_points <= 0) {
      return(TRUE)
    }
    if (hit_points <= 0) {
      return(FALSE)
    }
  }
}

i_weapon <- c(1:5)
i_armor <- c(0, 6:10)
i_ring1 <- c(0, 11:16)
i_ring2 <- c(0, 11:16)

loadouts <-
  crossing(i_weapon, i_armor, i_ring1, i_ring2) %>%
  filter(i_ring1 == 0 | i_ring1 != i_ring2) %>%
  asplit(1) %>%
  map_dfr(function(i) {
    slice(shop, i) %>%
      select(cost, damage, armor) %>%
      summarise_all(sum)
  }) %>%
  arrange(cost)

for (i in seq_len(nrow(loadouts))) {
  if (does_win(loadouts$damage[i], loadouts$armor[i])) {
    break
  }
}

answer <- loadouts %>% slice(i) %>% pull(cost)
answer

for (i in rev(seq_len(nrow(loadouts)))) {
  if (!does_win(loadouts$damage[i], loadouts$armor[i])) {
    break
  }
}

answer <- loadouts %>% slice(i) %>% pull(cost)
answer
