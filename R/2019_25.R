library(tidyverse)



sequence <- str_split(input, ",") %>% unlist() %>% parse_double()
sequence

create_instructions <- function(instructions) {
  result <- structure(instructions, class = "instructions")
  attr(result, "relative_base") <- 0
  names(result) <- seq(from = 0, length.out = length(instructions))
  result
}

to_character <- function(x) format(x, scientific = FALSE)

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(v, i) {
  index <- i[[1]]
  if (i[[2]] == 0) {
    # Position mode
    index <- v[[to_character(index)]]
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- v[list(index, 1)] + attr(v, "relative_base")
  }
  index
}

`[.instructions` <- function(v, i) {
  index <- to_character(get_index(v, i))
  if (!(index %in% names(v))) v[[index]] <- 0
  result <- v[[index]]
  if (is.null(result) || is.na(result)) v[[index]] <- 0
  v[[index]]
}

`[<-.instructions` <- function(v, i, j, value) {
  v[[to_character(get_index(v, i))]] <- value
  v
}

run_bot <- function(bot, input = NULL) {
  if (is.character(input)) input <- c(utf8ToInt(input), 10)
  bot$needs_input <- FALSE
  while (bot$instructions[list(bot$i, 1)] != 99) {
    value <- bot$instructions[list(bot$i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000
    
    p1 <- list(bot$i + 1, p1_index_mode)
    p2 <- list(bot$i + 2, p2_index_mode)
    p3 <- list(bot$i + 3, p3_index_mode)
    
    if (op_code == 1) {
      bot$instructions[p3] <- bot$instructions[p1] + bot$instructions[p2]
    } else if (op_code == 2) {
      bot$instructions[p3] <- bot$instructions[p1] * bot$instructions[p2]
    } else if (op_code == 3) {
      if (length(input) == 0) {
        bot$needs_input <- TRUE
        break
      }
      bot$instructions[p1] <- input[1]
      input <- input[-1]
      # if (length(input) == 0) bot$needs_input <- TRUE
    } else if (op_code == 4) {
      cat(intToUtf8(bot$instructions[p1]))
      # bot$output <- bot$instructions[p1]
      # num_params <- 1
      # bot$i <- bot$i + 1 + num_params
      # break
    } else if (op_code == 5) {
      if (bot$instructions[p1] != 0) {
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (bot$instructions[p1] == 0) {
        bot$i = get_index(bot$instructions, p2) - 1
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      bot$instructions[p3] <- bot$instructions[p1] < bot$instructions[p2]
    } else if (op_code == 8) {
      bot$instructions[p3] <- bot$instructions[p1] == bot$instructions[p2]
    } else if (op_code == 9) {
      attr(bot$instructions, "relative_base") <- attr(bot$instructions, "relative_base") + bot$instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', bot$i, '\n', paste0(bot$instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    bot$i <- bot$i + 1 + num_params
  }
  
  if (bot$instructions[list(bot$i, TRUE)] == 99) {
    bot$is_halted <- TRUE
  }

  bot
}

create_bot <- function(instructions) {
  list(
    instructions = create_instructions(instructions),
    i = 0,
    x = 0,
    y = 0,
    is_halted = FALSE,
    needs_input = FALSE,
    output = NULL
  )
}

get_output <- function(instructions) {
  result <- c()
  bot <- create_bot(instructions)
  while (!bot$is_halted) {
    bot <- run_bot(bot, 0)
    result <- c(result, bot$output)
  }
  intToUtf8(result)
}

go <- function(input = NULL) bot <<- run_bot(bot, input)

bot <- create_bot(sequence)
go()          # N  W - Hull Breach

# Hull Breach -> West to Warp Drive Maintenance
go("west")   #  E W - Warp Drive Maintenance | giant electromagnet (don't take)
go("west")   #  E   - Corridor | loom
go("take loom")
go("east")   #  E W - Warp Drive Maintenance
go("east")   # N  W - Hull Breach. Fully explored all west

# Hull Breach -> North to Stables (and Holodeck)
go("north")   # N SW - Stables | infinite loop (don't pick up)
go("north")   #  ES  - Science Lab | mutex (take)
go("take mutex")
go("east")    #  ESW - Passages | tambourine (take). South and east don't go anywhere
go("take tambourine")

# go("east")  #    W - Hallway (dead end)
# go ("west") #  ESW - Passages

# go("south") # N S  - Kitchen | molten lava (don't take)
# go("south") # N    - Observatory | photons (don't take)
# go("north") # N S  - Kitchen 
# go("north") #  ESW - Passages

go("west")   #  ES  - Science Lab
go("south")  # N SW - Stables
go("west")   # NES  - Holodeck | antenna
go("take antenna")

# Holodeck -> South to Sick Bay
go("south")  # N SW - Sick Bay | hologram
go("take hologram")
go("south")  # N    - Navigation | mug
go("take mug")
go("north")  # N SW - Sick Bay
go("west")   #  E   - Gift Wrapping Center | astronaut ice cream
go("take astronaut ice cream")
go("east")   # N SW - Sick Bay
go("north")   # NES  - Holodeck

# Holodeck -> North to Arcade
go("north")  # NES  - Arcade
go("north")  # N S  - Engineering
go("north")  # N S  - Hot Chocolate Fountain | space heater
go("take space heater")
go("north") #  ES   - Crew Quarters
go("east") # E W - Security Checkpoint

# Too heavy: mutex, loom, tambourine, space heater, antenna
# Too heavy:        loom, tambourine, space heater, antenna
# Too heavy:              tambourine, space heater, antenna
# Too light:                          space heater, antenna
# Too heavy:        loom,             space heater, antenna
# Too heavy:        loom,                           antenna
# Too heavy:        loom,                                      
# Too heavy: mutex,       tambourine,               antenna   
# Too heavy:              tambourine,               antenna
# Too light:                                        antenna
# Too light: mutex,                                 antenna
# Too light: mutex,                   space heater, antenna
# Too heavy: mutex,                   space heater, antenna, astronaut ice cream, mug, hologram
# Too heavy: mutex,                   space heater, antenna, astronaut ice cream,
# Too light: mutex,                   space heater, antenna,                      mug,
# Too light: mutex,                   space heater, antenna,                      mug, hologram
# Correct:                            space heater, antenna, astronaut ice cream,      hologram

go("drop mutex")
go("drop loom")
go("drop tambourine")
go("drop mug")
go("east")

# No puzzle here - just need 49 stars.
