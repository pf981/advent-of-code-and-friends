# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 22: Wizard Simulator 20XX ---</h2><p>Little Henry Case decides that defeating bosses with <a href="21">swords and stuff</a> is boring.  Now he's playing the game with a <span title="Being a !@#$% Sorcerer.">wizard</span>.  Of course, he gets stuck on another boss and needs your help again.</p>
# MAGIC <p>In this version, combat still proceeds with the player and the boss taking alternating turns.  The player still goes first.  Now, however, you don't get any equipment; instead, you must choose one of your spells to cast.  The first character at or below <code>0</code> hit points loses.</p>
# MAGIC <p>Since you're a wizard, you don't get to wear armor, and you can't attack normally.  However, since you do <em>magic damage</em>, your opponent's armor is ignored, and so the boss effectively has zero armor as well.  As before, if armor (from a spell, in this case) would reduce damage below <code>1</code>, it becomes <code>1</code> instead - that is, the boss' attacks always deal at least <code>1</code> damage.</p>
# MAGIC <p>On each of your turns, you must select one of your spells to cast.  If you cannot afford to cast any spell, you lose.  Spells cost <em>mana</em>; you start with <em>500</em> mana, but have no maximum limit.  You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it.  Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.</p>
# MAGIC <ul>
# MAGIC <li><em>Magic Missile</em> costs <code>53</code> mana.  It instantly does <code>4</code> damage.</li>
# MAGIC <li><em>Drain</em> costs <code>73</code> mana.  It instantly does <code>2</code> damage and heals you for <code>2</code> hit points.</li>
# MAGIC <li><em>Shield</em> costs <code>113</code> mana.  It starts an <em>effect</em> that lasts for <code>6</code> turns.  While it is active, your armor is increased by <code>7</code>.</li>
# MAGIC <li><em>Poison</em> costs <code>173</code> mana.  It starts an <em>effect</em> that lasts for <code>6</code> turns.  At the start of each turn while it is active, it deals the boss <code>3</code> damage.</li>
# MAGIC <li><em>Recharge</em> costs <code>229</code> mana.  It starts an <em>effect</em> that lasts for <code>5</code> turns.  At the start of each turn while it is active, it gives you <code>101</code> new mana.</li>
# MAGIC </ul>
# MAGIC <p><em>Effects</em> all work the same way.  Effects apply at the start of both the player's turns and the boss' turns.  Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one.  If this decreases the timer to zero, the effect ends.  You cannot cast a spell that would start an effect which is already active.  However, effects can be started on the same turn they end.</p>
# MAGIC <p>For example, suppose the player has <code>10</code> hit points and <code>250</code> mana, and that the boss has <code>13</code> hit points and <code>8</code> damage:</p>
# MAGIC <pre><code>-- Player turn --
# MAGIC - Player has 10 hit points, 0 armor, 250 mana
# MAGIC - Boss has 13 hit points
# MAGIC Player casts Poison.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 10 hit points, 0 armor, 77 mana
# MAGIC - Boss has 13 hit points
# MAGIC Poison deals 3 damage; its timer is now 5.
# MAGIC Boss attacks for 8 damage.
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 0 armor, 77 mana
# MAGIC - Boss has 10 hit points
# MAGIC Poison deals 3 damage; its timer is now 4.
# MAGIC Player casts Magic Missile, dealing 4 damage.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 0 armor, 24 mana
# MAGIC - Boss has 3 hit points
# MAGIC Poison deals 3 damage. This kills the boss, and the player wins.
# MAGIC </code></pre>
# MAGIC <p>Now, suppose the same initial conditions, except that the boss has <code>14</code> hit points instead:</p>
# MAGIC <pre><code>-- Player turn --
# MAGIC - Player has 10 hit points, 0 armor, 250 mana
# MAGIC - Boss has 14 hit points
# MAGIC Player casts Recharge.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 10 hit points, 0 armor, 21 mana
# MAGIC - Boss has 14 hit points
# MAGIC Recharge provides 101 mana; its timer is now 4.
# MAGIC Boss attacks for 8 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 0 armor, 122 mana
# MAGIC - Boss has 14 hit points
# MAGIC Recharge provides 101 mana; its timer is now 3.
# MAGIC Player casts Shield, increasing armor by 7.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 7 armor, 110 mana
# MAGIC - Boss has 14 hit points
# MAGIC Shield's timer is now 5.
# MAGIC Recharge provides 101 mana; its timer is now 2.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 1 hit point, 7 armor, 211 mana
# MAGIC - Boss has 14 hit points
# MAGIC Shield's timer is now 4.
# MAGIC Recharge provides 101 mana; its timer is now 1.
# MAGIC Player casts Drain, dealing 2 damage, and healing 2 hit points.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 3 hit points, 7 armor, 239 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 3.
# MAGIC Recharge provides 101 mana; its timer is now 0.
# MAGIC Recharge wears off.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 2 hit points, 7 armor, 340 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 2.
# MAGIC Player casts Poison.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 2 hit points, 7 armor, 167 mana
# MAGIC - Boss has 12 hit points
# MAGIC Shield's timer is now 1.
# MAGIC Poison deals 3 damage; its timer is now 5.
# MAGIC Boss attacks for 8 - 7 = 1 damage!
# MAGIC 
# MAGIC -- Player turn --
# MAGIC - Player has 1 hit point, 7 armor, 167 mana
# MAGIC - Boss has 9 hit points
# MAGIC Shield's timer is now 0.
# MAGIC Shield wears off, decreasing armor by 7.
# MAGIC Poison deals 3 damage; its timer is now 4.
# MAGIC Player casts Magic Missile, dealing 4 damage.
# MAGIC 
# MAGIC -- Boss turn --
# MAGIC - Player has 1 hit point, 0 armor, 114 mana
# MAGIC - Boss has 2 hit points
# MAGIC Poison deals 3 damage. This kills the boss, and the player wins.
# MAGIC </code></pre>
# MAGIC <p>You start with <em>50 hit points</em> and <em>500 mana points</em>. The boss's actual stats are in your puzzle input. What is the <em>least amount of mana</em> you can spend and still win the fight?  (Do not include mana recharge effects as "spending" negative mana.)</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Hit Points: 51
Damage: 9
"

# COMMAND ----------

final_boss_hp <- str_extract(input, "(?<=Hit Points: )\\d+") %>% parse_integer()
final_boss_damage <- str_extract(input, "(?<=Damage: )\\d+") %>% parse_integer()

lst(final_boss_hp, final_boss_damage)

# COMMAND ----------

silent <- FALSE
m <- function(s) {
  if (!silent) {
    message(glue::glue(s, .envir = parent.frame()))
  }
}

# COMMAND ----------

turn <- function(state) {
  m("- Player has {state$hp} hit points, {state$armor} armor, {state$mana} mana")
  m("- Boss has {state$boss_hp} hit points")
  
  if (state$shield_timer > 0) {
    state$shield_timer <- state$shield_timer - 1
    m("Shield's timer is now {state$shield_timer}.")

    if (state$shield_timer == 0) {
      state$armor <- state$armor - 7
      m("Shield wears off, decreasing armor by 7.")
    }
  }
  if (state$poison_timer > 0) {
    state$boss_hp <- state$boss_hp - 3
    state$poison_timer <- state$poison_timer - 1
    
    if (state$boss_hp <= 0) {
      m("Poison deals 3 damage. This kills the boss, and the player wins.")
      state$status <- "Win"
      return(state)
    }
    m("Poison deals 3 damage; its timer is now {state$poison_timer}.")
    if (state$poison_timer == 0) {
      m("Poison wears off.")
    }
  }
  if (state$recharge_timer > 0) {
    state$mana <- state$mana + 101
    state$recharge_timer <- state$recharge_timer - 1
    m("Recharge provides 101 mana; its timer is now {state$recharge_timer}.")

    if (state$recharge_timer == 0) {
      m("Recharge wears off.")
    }
  }
  state
}

simulate <- function(
  action,
  state = list(
    hp = 50, armor = 0, mana = 500,
    boss_hp = final_boss_hp, boss_damage = final_boss_damage,
    shield_timer = 0, poison_timer = 0, recharge_timer = 0,
    status = "Pending", # Win/Lose/Pending
    mana_spent = 0,
    actions = character()
  )
) {
  m("\n\n-- Player turn --")
  state <- turn(state)
  if (state$status != "Pending" && state$mana >= 53) return(state)
  
  if (action == "Magic Missile") {
    state$mana_spent <- state$mana_spent + 53
    state$mana <- state$mana - 53
    state$boss_hp <- state$boss_hp - 4
    m("Player casts Magic Missile, dealing 4 damage.")
  } else if (action == "Drain") {
    state$mana_spent <- state$mana_spent + 73
    state$mana <- state$mana - 73
    state$boss_hp <- state$boss_hp - 2
    state$hp <- state$hp + 2
    m("Player casts Drain, dealing 2 damage, and healing 2 hit points.")
  } else if (action == "Shield") {
    if (state$shield_timer > 0) {
      m("Cannot cast Shield while Shield is active. Player loses.")
      state$status <- "Lose"
      return(state)
    }
    
    state$mana_spent <- state$mana_spent + 113
    state$mana <- state$mana - 113
    state$shield_timer <- 6
    state$armor <- state$armor + 7
    m("Player casts Shield, increasing armor by 7.")
  } else if (action == "Poison") {
    if (state$poison_timer > 0) {
      m("Cannot cast Poison while Poison is active. Player loses.")
      state$status <- "Lose"
      return(state)
    }
    
    state$mana_spent <- state$mana_spent + 173
    state$mana <- state$mana - 173
    state$poison_timer <- 6
    m("Player casts Poison.")
  } else if (action == "Recharge") {
    if (state$recharge_timer > 0) {
      m("Cannot cast Recharge while Recharge is active. Player loses.")
      state$status <- "Lose"
      return(state)
    }
    
    state$mana_spent <- state$mana_spent + 229
    state$mana <- state$mana - 229
    state$recharge_timer <- 5
    m("Player casts Recharge.")
  }
  
  if(state$mana < 0) {
    m("Actually, that action wasn't possible because the player is out of mana. Player loses.")
    state$status <- "Lose"
    return(state)
  }
  if (state$boss_hp <= 0) {
    m("Boss is dead and the player wins.")
    state$status <- "Win"
    return(state)
  }
  
  
  m("\n\n-- Boss turn --")
  state <- turn(state)
  if (state$status != "Pending") return(state)
  
  state$hp <- state$hp - (state$boss_damage - state$armor)
  m("Boss attacks for {state$boss_damage} - {state$armor} = {state$boss_damage - state$armor} damage!")
  
  if(state$hp < 0) {
    m("Player dies. Player loses.")
      state$status <- "Lose"
      return(state)
  }
  state
}


# COMMAND ----------

simulate_many <- function(actions, state) {
  for (action in actions) {
    state <- simulate(action, state)
  }
  state
}

# COMMAND ----------

find_win <- function(
  start_state = list(
    hp = 50, armor = 0, mana = 500,
    boss_hp = final_boss_hp, boss_damage = final_boss_damage,
    shield_timer = 0, poison_timer = 0, recharge_timer = 0,
    status = "Pending", # Win/Lose/Pending
    mana_spent = 0,
    actions = character()
  )
) {
  states <- replicate(5, start_state, simplify = FALSE)
  next_action <- c("Magic Missile", "Drain", "Shield", "Poison", "Recharge")
  mana_to_be_spent <- start_state$mana_spent + c(53, 73, 113, 173, 229)
  
  while (length(states) > 0) {
    
    i <- which.min(mana_to_be_spent)
    state <- states[[i]]
    action <- next_action[[i]]
    
    states[[i]] <- NULL
    next_action <- next_action[-i]
    mana_to_be_spent <- mana_to_be_spent[-i]
    
    
      new_state <- simulate(action, state)
      new_state$actions <- c(new_state$actions, action)
      if (new_state$status == "Win") {
        return(new_state)
      }
      if (new_state$status == "Pending") {
        states <- c(states, replicate(5, new_state, simplify = FALSE))
        mana_to_be_spent <- c(mana_to_be_spent, new_state$mana_spent + c(53, 73, 113, 173, 229))
        next_action <- c(next_action, c("Magic Missile", "Drain", "Shield", "Poison", "Recharge"))
      }
  }
  NULL
}

# COMMAND ----------

silent <- TRUE
result <- find_win()
str(result) # Took 7 mins

# COMMAND ----------

answer <- result$mana_spent
answer
