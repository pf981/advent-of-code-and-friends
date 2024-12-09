library(tidyverse)



final_boss_hp <- str_extract(input, "(?<=Hit Points: )\\d+") %>% parse_integer()
final_boss_damage <- str_extract(input, "(?<=Damage: )\\d+") %>% parse_integer()

lst(final_boss_hp, final_boss_damage)

silent <- FALSE
m <- function(s) {
  if (!silent) {
    message(glue::glue(s, .envir = parent.frame()))
  }
}

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
  ),
  is_hard = FALSE
) {
  m("\n\n-- Player turn --")
  state <- turn(state)
  if (is_hard) {
    state$hp <- state$hp - 1
    if (state$hp <= 0) {
      state$status <- "Lose"
    }
  }
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


simulate_many <- function(actions, state) {
  for (action in actions) {
    state <- simulate(action, state)
  }
  state
}

find_win <- function(
  start_state = list(
    hp = 50, armor = 0, mana = 500,
    boss_hp = final_boss_hp, boss_damage = final_boss_damage,
    shield_timer = 0, poison_timer = 0, recharge_timer = 0,
    status = "Pending", # Win/Lose/Pending
    mana_spent = 0,
    actions = character()
  ),
  is_hard = FALSE
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
    
    
      new_state <- simulate(action, state, is_hard)
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

silent <- TRUE
result <- find_win()# Took 2 mins
str(result) 

answer <- result$mana_spent
answer

silent <- TRUE
result <- find_win(is_hard = TRUE) # Took 13 mins
str(result)

answer <- result$mana_spent
answer
