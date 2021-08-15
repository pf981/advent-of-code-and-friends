# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 24: Immune System Simulator 20XX ---</h2><p>After <a href="https://www.youtube.com/watch?v=NDVjLt_QHL8&amp;t=7" target="_blank">a weird buzzing noise</a>, you appear back at the man's cottage. He seems relieved to see his friend, but quickly notices that the little reindeer caught some kind of cold while out exploring.</p>
# MAGIC <p>The portly man explains that this reindeer's immune system isn't similar to regular reindeer immune systems:</p>
# MAGIC <p>The <em>immune system</em> and the <em>infection</em> each have <span title="On second thought, it's pretty similar to regular reindeer immune systems.">an army</span> made up of several <em>groups</em>; each <em>group</em> consists of one or more identical <em>units</em>.  The armies repeatedly <em>fight</em> until only one army has units remaining.</p>
# MAGIC <p><em>Units</em> within a group all have the same <em>hit points</em> (amount of damage a unit can take before it is destroyed), <em>attack damage</em> (the amount of damage each unit deals), an <em>attack type</em>, an <em>initiative</em> (higher initiative units attack first and win ties), and sometimes <em>weaknesses</em> or <em>immunities</em>. Here is an example group:</p>
# MAGIC <pre><code>18 units each with 729 hit points (weak to fire; immune to cold, slashing)
# MAGIC  with an attack that does 8 radiation damage at initiative 10
# MAGIC </code></pre>
# MAGIC <p>Each group also has an <em>effective power</em>: the number of units in that group multiplied by their attack damage. The above group has an effective power of <code>18 * 8 = 144</code>. Groups never have zero or negative units; instead, the group is removed from combat.</p>
# MAGIC <p>Each <em>fight</em> consists of two phases: <em>target selection</em> and <em>attacking</em>.</p>
# MAGIC <p>During the <em>target selection</em> phase, each group attempts to choose one target. In decreasing order of effective power, groups choose their targets; in a tie, the group with the higher initiative chooses first. The attacking group chooses to target the group in the enemy army to which it would deal the most damage (after accounting for weaknesses and immunities, but not accounting for whether the defending group has enough units to actually receive all of that damage).</p>
# MAGIC <p>If an attacking group is considering two defending groups to which it would deal equal damage, it chooses to target the defending group with the largest effective power; if there is still a tie, it chooses the defending group with the highest initiative.  If it cannot deal any defending groups damage, it does not choose a target.  Defending groups can only be chosen as a target by one attacking group.</p>
# MAGIC <p>At the end of the target selection phase, each group has selected zero or one groups to attack, and each group is being attacked by zero or one groups.</p>
# MAGIC <p>During the <em>attacking</em> phase, each group deals damage to the target it selected, if any. Groups attack in decreasing order of initiative, regardless of whether they are part of the infection or the immune system. (If a group contains no units, it cannot attack.)</p>
# MAGIC <p>The damage an attacking group deals to a defending group depends on the attacking group's attack type and the defending group's immunities and weaknesses.  By default, an attacking group would deal damage equal to its <em>effective power</em> to the defending group.  However, if the defending group is <em>immune</em> to the attacking group's attack type, the defending group instead takes <em>no damage</em>; if the defending group is <em>weak</em> to the attacking group's attack type, the defending group instead takes <em>double damage</em>.</p>
# MAGIC <p>The defending group only loses <em>whole units</em> from damage; damage is always dealt in such a way that it kills the most units possible, and any remaining damage to a unit that does not immediately kill it is ignored. For example, if a defending group contains <code>10</code> units with <code>10</code> hit points each and receives <code>75</code> damage, it loses exactly <code>7</code> units and is left with <code>3</code> units at full health.</p>
# MAGIC <p>After the fight is over, if both armies still contain units, a new fight begins; combat only ends once one army has lost all of its units.</p>
# MAGIC <p>For example, consider the following armies:</p>
# MAGIC <pre><code>Immune System:
# MAGIC 17 units each with 5390 hit points (weak to radiation, bludgeoning) with
# MAGIC  an attack that does 4507 fire damage at initiative 2
# MAGIC 989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
# MAGIC  slashing) with an attack that does 25 slashing damage at initiative 3
# MAGIC 
# MAGIC Infection:
# MAGIC 801 units each with 4706 hit points (weak to radiation) with an attack
# MAGIC  that does 116 bludgeoning damage at initiative 1
# MAGIC 4485 units each with 2961 hit points (immune to radiation; weak to fire,
# MAGIC  cold) with an attack that does 12 slashing damage at initiative 4
# MAGIC </code></pre>
# MAGIC <p>If these armies were to enter combat, the following fights, including details during the target selection and attacking phases, would take place:</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 1 contains 17 units
# MAGIC Group 2 contains 989 units
# MAGIC Infection:
# MAGIC Group 1 contains 801 units
# MAGIC Group 2 contains 4485 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 1 185832 damage
# MAGIC Infection group 1 would deal defending group 2 185832 damage
# MAGIC Infection group 2 would deal defending group 2 107640 damage
# MAGIC Immune System group 1 would deal defending group 1 76619 damage
# MAGIC Immune System group 1 would deal defending group 2 153238 damage
# MAGIC Immune System group 2 would deal defending group 1 24725 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 84 units
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Immune System group 1 attacks defending group 2, killing 51 units
# MAGIC Infection group 1 attacks defending group 1, killing 17 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 905 units
# MAGIC Infection:
# MAGIC Group 1 contains 797 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 184904 damage
# MAGIC Immune System group 2 would deal defending group 1 22625 damage
# MAGIC Immune System group 2 would deal defending group 2 22625 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Infection group 1 attacks defending group 2, killing 144 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 761 units
# MAGIC Infection:
# MAGIC Group 1 contains 793 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 183976 damage
# MAGIC Immune System group 2 would deal defending group 1 19025 damage
# MAGIC Immune System group 2 would deal defending group 2 19025 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 4 units
# MAGIC Infection group 1 attacks defending group 2, killing 143 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 618 units
# MAGIC Infection:
# MAGIC Group 1 contains 789 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 183048 damage
# MAGIC Immune System group 2 would deal defending group 1 15450 damage
# MAGIC Immune System group 2 would deal defending group 2 15450 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 3 units
# MAGIC Infection group 1 attacks defending group 2, killing 143 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 475 units
# MAGIC Infection:
# MAGIC Group 1 contains 786 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 182352 damage
# MAGIC Immune System group 2 would deal defending group 1 11875 damage
# MAGIC Immune System group 2 would deal defending group 2 11875 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 2 units
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 333 units
# MAGIC Infection:
# MAGIC Group 1 contains 784 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181888 damage
# MAGIC Immune System group 2 would deal defending group 1 8325 damage
# MAGIC Immune System group 2 would deal defending group 2 8325 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 1 unit
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 191 units
# MAGIC Infection:
# MAGIC Group 1 contains 783 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181656 damage
# MAGIC Immune System group 2 would deal defending group 1 4775 damage
# MAGIC Immune System group 2 would deal defending group 2 4775 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 1 unit
# MAGIC Infection group 1 attacks defending group 2, killing 142 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 49 units
# MAGIC Infection:
# MAGIC Group 1 contains 782 units
# MAGIC Group 2 contains 4434 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 181424 damage
# MAGIC Immune System group 2 would deal defending group 1 1225 damage
# MAGIC Immune System group 2 would deal defending group 2 1225 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 0 units
# MAGIC Infection group 1 attacks defending group 2, killing 49 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC No groups remain.
# MAGIC Infection:
# MAGIC Group 1 contains 782 units
# MAGIC Group 2 contains 4434 units
# MAGIC </code></pre>
# MAGIC <p>In the example above, the winning army ends up with <code>782 + 4434 = <em>5216</em></code> units.</p>
# MAGIC <p>You scan the reindeer's condition (your puzzle input); the white-bearded man looks nervous.  As it stands now, <em>how many units would the winning army have</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Immune System:
1432 units each with 7061 hit points (immune to cold; weak to bludgeoning) with an attack that does 41 slashing damage at initiative 17
3387 units each with 9488 hit points (weak to bludgeoning) with an attack that does 27 slashing damage at initiative 20
254 units each with 3249 hit points (immune to fire) with an attack that does 89 cold damage at initiative 1
1950 units each with 8201 hit points with an attack that does 39 fire damage at initiative 15
8137 units each with 3973 hit points (weak to slashing; immune to radiation) with an attack that does 4 radiation damage at initiative 6
4519 units each with 7585 hit points (weak to fire) with an attack that does 15 radiation damage at initiative 8
763 units each with 7834 hit points (immune to radiation, slashing, cold; weak to fire) with an attack that does 91 radiation damage at initiative 18
935 units each with 10231 hit points (immune to slashing, cold) with an attack that does 103 bludgeoning damage at initiative 12
4557 units each with 7860 hit points (immune to slashing) with an attack that does 15 slashing damage at initiative 11
510 units each with 7363 hit points (weak to fire, radiation) with an attack that does 143 fire damage at initiative 5

Infection:
290 units each with 29776 hit points (weak to cold, radiation) with an attack that does 204 bludgeoning damage at initiative 16
7268 units each with 14114 hit points (immune to radiation; weak to bludgeoning) with an attack that does 3 bludgeoning damage at initiative 19
801 units each with 5393 hit points with an attack that does 13 slashing damage at initiative 13
700 units each with 12182 hit points with an attack that does 29 cold damage at initiative 4
531 units each with 16607 hit points (immune to slashing) with an attack that does 53 bludgeoning damage at initiative 10
23 units each with 24482 hit points (weak to cold, fire) with an attack that does 2095 bludgeoning damage at initiative 7
8025 units each with 43789 hit points (weak to cold; immune to radiation) with an attack that does 8 radiation damage at initiative 9
1405 units each with 53896 hit points with an attack that does 70 slashing damage at initiative 14
566 units each with 7820 hit points (immune to cold) with an attack that does 26 cold damage at initiative 2
1641 units each with 7807 hit points (weak to fire; immune to slashing, bludgeoning) with an attack that does 7 radiation damage at initiative 3
"

# COMMAND ----------

# input <- "Immune System:
# 17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
# 989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

# Infection:
# 801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
# 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
# "

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

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

std::pair<std::string, int> get_winner(std::vector<std::string> army, std::vector<int> units, std::vector<int> hit_points, std::vector<int> attack_damage, std::vector<std::string> attack_type, std::vector<int> initiative, std::vector<std::vector<std::string> > weaknesses, std::vector<std::vector<std::string> > immunities, int boost = 0) {
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

# COMMAND ----------

answer <- solve_cpp(df$army, df$units, df$hit_points, df$attack_damage, df$attack_type, df$initiative, df$weaknesses, df$immunities)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Things aren't looking good for the reindeer. The man asks whether more milk and cookies would help you think.</p>
# MAGIC <p>If only you could give the reindeer's immune system a boost, you might be able to change the outcome of the combat.</p>
# MAGIC <p>A <em>boost</em> is an integer increase in immune system units' attack damage. For example, if you were to boost the above example's immune system's units by <code>1570</code>, the armies would instead look like this:</p>
# MAGIC <pre><code>Immune System:
# MAGIC 17 units each with 5390 hit points (weak to radiation, bludgeoning) with
# MAGIC  an attack that does <em>6077</em> fire damage at initiative 2
# MAGIC 989 units each with 1274 hit points (immune to fire; weak to bludgeoning,
# MAGIC  slashing) with an attack that does <em>1595</em> slashing damage at initiative 3
# MAGIC 
# MAGIC Infection:
# MAGIC 801 units each with 4706 hit points (weak to radiation) with an attack
# MAGIC  that does 116 bludgeoning damage at initiative 1
# MAGIC 4485 units each with 2961 hit points (immune to radiation; weak to fire,
# MAGIC  cold) with an attack that does 12 slashing damage at initiative 4
# MAGIC </code></pre>
# MAGIC <p>With this boost, the combat proceeds differently:</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 989 units
# MAGIC Group 1 contains 17 units
# MAGIC Infection:
# MAGIC Group 1 contains 801 units
# MAGIC Group 2 contains 4485 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 185832 damage
# MAGIC Infection group 1 would deal defending group 1 185832 damage
# MAGIC Infection group 2 would deal defending group 1 53820 damage
# MAGIC Immune System group 2 would deal defending group 1 1577455 damage
# MAGIC Immune System group 2 would deal defending group 2 1577455 damage
# MAGIC Immune System group 1 would deal defending group 2 206618 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 1, killing 9 units
# MAGIC Immune System group 2 attacks defending group 1, killing 335 units
# MAGIC Immune System group 1 attacks defending group 2, killing 32 units
# MAGIC Infection group 1 attacks defending group 2, killing 84 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 905 units
# MAGIC Group 1 contains 8 units
# MAGIC Infection:
# MAGIC Group 1 contains 466 units
# MAGIC Group 2 contains 4453 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 108112 damage
# MAGIC Infection group 1 would deal defending group 1 108112 damage
# MAGIC Infection group 2 would deal defending group 1 53436 damage
# MAGIC Immune System group 2 would deal defending group 1 1443475 damage
# MAGIC Immune System group 2 would deal defending group 2 1443475 damage
# MAGIC Immune System group 1 would deal defending group 2 97232 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 1, killing 8 units
# MAGIC Immune System group 2 attacks defending group 1, killing 306 units
# MAGIC Infection group 1 attacks defending group 2, killing 29 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 876 units
# MAGIC Infection:
# MAGIC Group 2 contains 4453 units
# MAGIC Group 1 contains 160 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 106872 damage
# MAGIC Immune System group 2 would deal defending group 2 1397220 damage
# MAGIC Immune System group 2 would deal defending group 1 1397220 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 83 units
# MAGIC Immune System group 2 attacks defending group 2, killing 427 units
# MAGIC </code></pre>
# MAGIC <p>After a few fights...</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 64 units
# MAGIC Infection:
# MAGIC Group 2 contains 214 units
# MAGIC Group 1 contains 19 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 5136 damage
# MAGIC Immune System group 2 would deal defending group 2 102080 damage
# MAGIC Immune System group 2 would deal defending group 1 102080 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 4 units
# MAGIC Immune System group 2 attacks defending group 2, killing 32 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 60 units
# MAGIC Infection:
# MAGIC Group 1 contains 19 units
# MAGIC Group 2 contains 182 units
# MAGIC 
# MAGIC Infection group 1 would deal defending group 2 4408 damage
# MAGIC Immune System group 2 would deal defending group 1 95700 damage
# MAGIC Immune System group 2 would deal defending group 2 95700 damage
# MAGIC 
# MAGIC Immune System group 2 attacks defending group 1, killing 19 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 60 units
# MAGIC Infection:
# MAGIC Group 2 contains 182 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 4368 damage
# MAGIC Immune System group 2 would deal defending group 2 95700 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 3 units
# MAGIC Immune System group 2 attacks defending group 2, killing 30 units
# MAGIC </code></pre>
# MAGIC <p>After a few more fights...</p>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC Group 2 contains 40 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 960 damage
# MAGIC Immune System group 2 would deal defending group 2 81345 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 0 units
# MAGIC Immune System group 2 attacks defending group 2, killing 27 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC Group 2 contains 13 units
# MAGIC 
# MAGIC Infection group 2 would deal defending group 2 312 damage
# MAGIC Immune System group 2 would deal defending group 2 81345 damage
# MAGIC 
# MAGIC Infection group 2 attacks defending group 2, killing 0 units
# MAGIC Immune System group 2 attacks defending group 2, killing 13 units
# MAGIC </code></pre>
# MAGIC <pre><code>Immune System:
# MAGIC Group 2 contains 51 units
# MAGIC Infection:
# MAGIC No groups remain.
# MAGIC </code></pre>
# MAGIC <p>This boost would allow the immune system's armies to win! It would be left with <code><em>51</em></code> units.</p>
# MAGIC <p>You don't even know <em>how</em> you could boost the reindeer's immune system or what effect it might have, so you need to be cautious and find the <em>smallest boost</em> that would allow the immune system to win.</p>
# MAGIC <p><em>How many units does the immune system have left</em> after getting the smallest boost it needs to win?</p>
# MAGIC </article>

# COMMAND ----------

answer <- solve_cpp2(df$army, df$units, df$hit_points, df$attack_damage, df$attack_type, df$initiative, df$weaknesses, df$immunities)
answer
