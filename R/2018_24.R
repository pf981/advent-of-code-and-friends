library(tidyverse)



# 

df <-
  tibble(line = read_lines(input)) %>%
  mutate(army = str_extract(line, ".+(?=:)")) %>%
  fill(army) %>%
  filter(str_detect(line, ".+[^:]$")) %>%
  mutate(
    units = line %>% str_extract("^\\d+") %>% parse_integer(),
    hit_points = line %>% str_extract("\\d+(?= hit points)") %>% parse_integer(),
    attack_damage = line %>% str_extract("(?<=does )\\d+") %>% parse_integer(),
    attack_type = line %>% str_extract("\\w+(?= damage)"),
    initiative = line %>% str_extract("\\d+$") %>% parse_integer(),
    weaknesses = line %>% str_extract("(?<=weak to ).*?(?=[;)])") %>% str_split(", ") %>% map(discard, is.na),
    immunities = line %>% str_extract("(?<=immune to ).*?(?=[;)])") %>% str_split(", ") %>% map(discard, is.na)
  ) %>%
  select(-line) %>%
  group_by(army) %>%
  mutate(group_id = row_number()) %>%
  ungroup()
df

# # This was too slow

# target_selection <- function(df) {
#   result <- NULL
  
#   df <-
#     df %>%
#     mutate(effective_power = units * attack_damage) %>%
#     arrange(desc(effective_power), desc(initiative))
  
#   remaining_targets <- df
  
#   for (i in seq_len(nrow(df))) {
#     attacker <- df %>% slice(i)
    
#     if (nrow(filter(remaining_targets, army != attacker$army)) == 0) next
    
#     target <-
#       remaining_targets %>%
#       filter(army != attacker$army) %>%
#       rowwise() %>%
#       mutate(
#         damage_multiplier = ifelse(any(immunities == attacker$attack_type), 0, 1) * ifelse(any(weaknesses == attacker$attack_type), 2, 1),
#         damage = attacker$effective_power * damage_multiplier
#       ) %>%
#       arrange(desc(damage), desc(effective_power), desc(initiative)) %>%
#       filter(damage > 0) %>% # If you can't deal damage, don't target
#       select(damage_multiplier, army, group_id) %>%
#       head(1)
    
#     result <- bind_rows(
#       result,
#       tibble(
#         attacker$initiative,
#         damage_multiplier = target$damage_multiplier,
#         attacker$army,
#         attacker$group_id,
#         target$army,
#         target$group_id
#       ) %>%
#         rename_all(str_replace, fixed("$"), "_")
#     )
#     remaining_targets <- remaining_targets %>% anti_join(target)
#   }
#   result %>% arrange(desc(attacker_initiative))
# }

# attack <- function(df, targets) {
#   targets %>% arrange(desc(attacker_initiative))
  
#   for (i in seq_len(nrow(targets))) {
#     target_info <- targets %>% slice(i)
    
#     defender_i <- which(df$army == target_info$target_army & df$group_id == target_info$target_group_id)
    
#     attacker <- df %>% filter(army == target_info$attacker_army, group_id == target_info$attacker_group_id)
#     defender <- df %>% slice(defender_i)
    
#     if (nrow(attacker) == 0 || nrow(defender) == 0) next
    
#     damage <- attacker$units * attacker$attack_damage * target_info$damage_multiplier
#     units_lost <- damage %/% defender$hit_points
    
#     df$units[defender_i] <- defender$units - units_lost
#     if (df$units[defender_i] <= 0) {
#       df <- df %>% slice(-defender_i)
#     }
#   }
  
#   df
# }

# remaining <- df
# while (n_distinct(remaining$army) >= 2) {
#   targets <- target_selection(remaining)
#   remaining <- attack(remaining, targets)
# }

# answer <- remaining %>% pull(units) %>% sum()
# answer

Rcpp::sourceCpp(code = '
#include "Rcpp.h"
#include <string>

struct Army {
  int units;
  int hit_points;
  int attack_damage;
  std::string attack_type;
  int initiative;
  std::vector<std::string> weaknesses;
  std::vector<std::string> immunities;
};

// attacking_side, (attacker_initiative, defender_initiative)
typedef std::pair<std::string, std::pair<int, int> > Target;

template <class T>
bool contains(const T& element, const std::vector<T>& v) {
  return std::find(v.begin(), v.end(), element) != v.end();
}

int calculate_damage(const Army& attacker, const Army& defender) {
  return attacker.units * attacker.attack_damage * (contains(attacker.attack_type, defender.weaknesses) ? 2 : 1) * (!contains(attacker.attack_type, defender.immunities));
}

// attacker_army reference gets sorted. defender_army is a copy
std::vector<Target> target_selection_side(std::vector<Army>& attacker_army, std::vector<Army> defender_army, const std::string& attacking_side) {
  std::vector<Target> result;

  // Sort attacker_army by effective_power DESC, initiative DESC
  std::sort(
    attacker_army.begin(),
    attacker_army.end(),
    [](const Army& a, const Army& b) {
      return (a.units * a.attack_damage > b.units * b.attack_damage) || (a.units * a.attack_damage == b.units * b.attack_damage && a.initiative > b.initiative);
    }
  );

  for (auto attacker : attacker_army) {
    if (defender_army.size() == 0) break;

    auto defender = std::max_element(
      defender_army.begin(),
      defender_army.end(),
      [&](const Army& a, const Army& b) {
        int a_damage = calculate_damage(attacker, a);
        int b_damage = calculate_damage(attacker, b);
        if (a_damage != b_damage) return a_damage < b_damage;

        int a_effective_power = a.units * a.attack_damage;
        int b_effective_power = b.units * b.attack_damage;
        if (a_effective_power != b_effective_power) return a_effective_power < b_effective_power;

        return a.initiative < b.initiative;
      }
    );
    if (calculate_damage(attacker, *defender) == 0) continue; // If you cant deal damage, dont target

    result.push_back(
      std::make_pair(attacking_side, std::make_pair(attacker.initiative, defender->initiative))
    );

    defender_army.erase(defender);
  }

  return result;
}

std::vector<Target> target_selection(std::vector<Army>& immune, std::vector<Army>& infection) {
  auto result = target_selection_side(immune, infection, "Immune System");
  auto result2 = target_selection_side(infection, immune, "Infection");

  std::copy(std::begin(result2), std::end(result2), std::back_inserter(result));
  std::sort(
    result.begin(),
    result.end(),
    [](const Target& a, const Target& b) { return a.second.first > b.second.first; }
  );

  return result;
}

void attack(std::vector<Army>& immune, std::vector<Army>& infection, const std::vector<Target>& targets) {
  for (auto target : targets) {
    auto& attacker_army = target.first == "Immune System" ? immune : infection;
    auto& defender_army = target.first != "Immune System" ? immune : infection;
  
    // targets are already sorted by attacker_initiative

    auto attacker = std::find_if(attacker_army.begin(), attacker_army.end(), [&](const Army& a) { return a.initiative == target.second.first; });
    auto defender = std::find_if(defender_army.begin(), defender_army.end(), [&](const Army& a) { return a.initiative == target.second.second; });

    int damage = calculate_damage(*attacker, *defender);
    int lost_units = damage / defender->hit_points;

    defender->units -= lost_units;
    if (defender->units <= 0) {
      defender_army.erase(defender);
    }
  }
}

std::pair<std::string, int> get_winner(const std::vector<std::string>& army, const std::vector<int>& units, const std::vector<int>& hit_points, const std::vector<int>& attack_damage, const std::vector<std::string>& attack_type, const std::vector<int>& initiative, const std::vector<std::vector<std::string> >& weaknesses, const std::vector<std::vector<std::string> >& immunities, int boost = 0) {
  std::vector<Army> immune;
  std::vector<Army> infection;

  for (int i = 0; i < army.size(); ++i) {
    auto& side = army[i] == "Immune System" ? immune : infection;
    side.push_back({
      units[i],
      hit_points[i],
      attack_damage[i] + (army[i] == "Immune System" ? boost : 0),
      attack_type[i],
      initiative[i],
      weaknesses[i],
      immunities[i]
    });
  }

  int total_army = accumulate(immune.begin(), immune.end(), 0, [](int sum, const Army& x) { return sum + x.units; }) + accumulate(infection.begin(), infection.end(), 0, [](int sum, const Army& x) { return sum + x.units; });
  while (immune.size() > 0 && infection.size() > 0) {
    auto targets = target_selection(immune, infection);
    attack(immune, infection, targets);

    // If no units were lost in the attack, it is a draw. Just take Infection to be the winner.
    int new_total_army = accumulate(immune.begin(), immune.end(), 0, [](int sum, const Army& x) { return sum + x.units; }) + accumulate(infection.begin(), infection.end(), 0, [](int sum, const Army& x) { return sum + x.units; });
    if (new_total_army == total_army) break;
    total_army = new_total_army;
  }

  auto& winning_army = infection.size() > 0 ? infection : immune;
  return std::make_pair(
    infection.size() > 0 ? "Infection" : "Immune System",
    accumulate(winning_army.begin(), winning_army.end(), 0, [](int sum, const Army& x) { return sum + x.units; })
  );
}

// [[Rcpp::export]]
int solve_cpp(std::vector<std::string> army, std::vector<int> units, std::vector<int> hit_points, std::vector<int> attack_damage, std::vector<std::string> attack_type, std::vector<int> initiative, std::vector<std::vector<std::string> > weaknesses, std::vector<std::vector<std::string> > immunities) {
  auto result = get_winner(army, units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities);
  return result.second;
}

// [[Rcpp::export]]
int solve_cpp2(std::vector<std::string> army, std::vector<int> units, std::vector<int> hit_points, std::vector<int> attack_damage, std::vector<std::string> attack_type, std::vector<int> initiative, std::vector<std::vector<std::string> > weaknesses, std::vector<std::vector<std::string> > immunities) {
  for (int boost = 0;; ++boost) {
    auto result = get_winner(army, units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities, boost);
    if (result.first == "Immune System") {
      return result.second;
    }
  }
}
')

answer <- solve_cpp(df$army, df$units, df$hit_points, df$attack_damage, df$attack_type, df$initiative, df$weaknesses, df$immunities)
answer

answer <- solve_cpp2(df$army, df$units, df$hit_points, df$attack_damage, df$attack_type, df$initiative, df$weaknesses, df$immunities)
answer
