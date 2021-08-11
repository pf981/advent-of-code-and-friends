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

input <- "Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
"

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
    weaknesses = line %>% str_extract("(?<=weak to).*?(?=[;)])") %>% str_split(", ") %>% map(discard, is.na),
    immunities = line %>% str_extract("(?<=immune to).*?(?=[;)])") %>% str_split(", ") %>% map(discard, is.na)
  ) %>%
  select(-line) %>%
  group_by(army) %>%
  mutate(group_id = row_number()) %>%
  ungroup()
df

# COMMAND ----------

do_print <- TRUE
m <- function(s) {
  if (do_print) {
    print(glue::glue(s, .envir = parent.frame()))
  }
}

# COMMAND ----------

print_armies <- function(df) {
  df <- df %>% arrange(army, group_id)
  army <- ""
  for (i in seq_len(nrow(df))) {
    group_info <- df %>% slice(i)
    if (group_info$army != army) {
      army <- group_info$army
      print(glue::glue("{army}:"))
    }
    m("Group {group_info$group_id} contains {group_info$units} units")
  }
}
print_armies(df)

# COMMAND ----------

target_selection <- function(df) {
  df <- df %>% arrange(army, group_id) %>% mutate(target = NA)
  for (i in seq_len(nrow(df))) {
    group_info <- df %>% slice(i)
    
    for (j in seq_len(nrow(filter(df, army != group_info$army)))) {
      other_group <- df %>% slice(j)
      damage <- group_info$units * group_info$attack_damage
      if (any(other_group$immunities == other_group$attack_type)) {
        other_damage <- 0
      } else if (any(other_group$weaknesses == other_group$attack_type)) {
        other_damage <- other_damage * 2
      }

      m("{group_info$army} group {group_info$group_id} would deal defending group {other_group$group_id} {damage} damage")
    }
  }
  df
}
target_selection(df)

# COMMAND ----------

target_selection <- function(df) {
  df <- df %>% mutate(dummy = TRUE)
  
  df %>%
    inner_join(by = "dummy") %>%
    filter(army.x != army.y) %>%
    rowwise() %>%
    mutate(
      effective_power = units.x * attack_damage.x
      damage = effective_power * ifelse(any(immunities.y == attack_damage.x), 0, 1) * ifelse(any(weaknesses.y == attack_damage.x), 2, 1)
    ) %>%
    ungroup() %>%
    arrange(desc(damage), group_id) %>% #
    group_by(army, group_id) %>%
    slice(1) %>%
    arrange(army, group_id)
}
target_selection(df)

# COMMAND ----------

df %>% arrange(army, group_id) %>% mutate(target = NA) %>% inner_join(., ., by = "target")

# COMMAND ----------

# I don't understand the targeting example. Why was infection group 1 damage calculated for both 1 and 2, but group 2 was only calculated for group 2!!????

# COMMAND ----------

df %>%
  mutate(effective_power = units * attack_damage) %>%
  arrange(desc(effective_power), desc(initiative)) %>%
  rowwise() %>%
  mutate(
    weaknesses = str_c(weaknesses, collapse = ", "),
    immunities = str_c(immunities, collapse = ", ")
  ) %>%
  display()

# COMMAND ----------

army, units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities

# COMMAND ----------

str_split(input, "\n\n") %>% first() %>% map(read_lines, skip = 1)

# COMMAND ----------

# hit_points, attack_damage, attack_type, initiative, weaknesses, immunities

# COMMAND ----------

effective_power <- unites * attack_damage

# COMMAND ----------

target selection:
 - decreasing effective power, initiative
 - target enemy group which it would deal most damage (weaknesses immunities, ignoring if enough units)
                                                       In tie, highest effective power then highest initiative
                                               If damage is zero, does not proceed
                                                       Can only be target of one attacking group

# COMMAND ----------

immune means no damage. weak double damage

# COMMAND ----------

# df <-
#   tibble(line = read_lines(input)) %>%
#   mutate(army = str_extract(line, ".+(?=:)")) %>%
#   fill(army) %>%
#   filter(str_detect(line, ".+[^:]$")) %>%
#   mutate(
#     units = line %>% str_extract("^\\d+") %>% parse_integer(),
#     hit_points = line %>% str_extract("\\d+(?= hit points)") %>% parse_integer(),
#     attack_damage = line %>% str_extract("(?<=does )\\d+") %>% parse_integer(),
#     attack_type = line %>% str_extract("\\w+(?= damage)"),
#     initiative = line %>% str_extract("\\d+$") %>% parse_integer(),
#     weaknesses = line %>% str_extract("(?<=weak to).*?(?=[;)])") %>% coalesce(""), # TODO list
#     immunities = line %>% str_extract("(?<=immune to).*?(?=[;)])") %>% coalesce("") # TODO list
#   ) %>%
#   select(-line) %>%
#   group_by(army) %>%
#   mutate(group_id = row_number()) %>%
#   ungroup()
# df
