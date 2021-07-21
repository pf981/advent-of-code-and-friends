# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 11: Radioisotope Thermoelectric Generators ---</h2><p>You come upon a column of four floors that have been entirely sealed off from the rest of the building except for a small dedicated lobby.  There are some radiation warnings and a big sign which reads "Radioisotope Testing Facility".</p>
# MAGIC <p>According to the project status board, this facility is currently being used to experiment with <a href="https://en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator">Radioisotope Thermoelectric Generators</a> (RTGs, or simply "generators") that are designed to be paired with specially-constructed microchips. Basically, an RTG is a highly radioactive rock that generates electricity through heat.</p>
# MAGIC <p>The <span title="The previous version, model number PB-NUK, used Blutonium.">experimental RTGs</span> have poor radiation containment, so they're dangerously radioactive. The chips are prototypes and don't have normal radiation shielding, but they do have the ability to <em>generate an electromagnetic radiation shield when powered</em>.  Unfortunately, they can <em>only</em> be powered by their corresponding RTG. An RTG powering a microchip is still dangerous to other microchips.</p>
# MAGIC <p>In other words, if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be <em>fried</em>. Therefore, it is assumed that you will follow procedure and keep chips connected to their corresponding RTG when they're in the same room, and away from other RTGs otherwise.</p>
# MAGIC <p>These microchips sound very interesting and useful to your current activities, and you'd like to try to retrieve them.  The fourth floor of the facility has an assembling machine which can make a self-contained, shielded computer for you to take with you - that is, if you can bring it all of the RTGs and microchips.</p>
# MAGIC <p>Within the radiation-shielded part of the facility (in which it's safe to have these pre-assembly RTGs), there is an elevator that can move between the four floors. Its capacity rating means it can carry at most yourself and two RTGs or microchips in any combination. (They're rigged to some heavy diagnostic equipment - the assembling machine will detach it for you.) As a security measure, the elevator will only function if it contains at least one RTG or microchip. The elevator always stops on each floor to recharge, and this takes long enough that the items within it and the items on that floor can irradiate each other. (You can prevent this if a Microchip and its Generator end up on the same floor in this way, as they can be connected while the elevator is recharging.)</p>
# MAGIC <p>You make some notes of the locations of each component of interest (your puzzle input). Before you don a hazmat suit and start moving things around, you'd like to have an idea of what you need to do.</p>
# MAGIC <p>When you enter the containment area, you and the elevator will start on the first floor.</p>
# MAGIC <p>For example, suppose the isolated area has the following arrangement:</p>
# MAGIC <pre class="wrap"><code>The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# MAGIC The second floor contains a hydrogen generator.
# MAGIC The third floor contains a lithium generator.
# MAGIC The fourth floor contains nothing relevant.
# MAGIC </code></pre>
# MAGIC <p>As a diagram (<code>F#</code> for a Floor number, <code>E</code> for Elevator, <code>H</code> for Hydrogen, <code>L</code> for Lithium, <code>M</code> for Microchip, and <code>G</code> for Generator), the initial state looks like this:</p>
# MAGIC <pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  .  .  LG .  
# MAGIC F2 .  HG .  .  .  
# MAGIC F1 E  .  HM .  LM 
# MAGIC </code></pre>
# MAGIC <p>Then, to get everything up to the assembling machine on the fourth floor, the following steps could be taken:</p>
# MAGIC <ul>
# MAGIC <li><p>Bring the Hydrogen-compatible Microchip to the second floor, which is safe because it can get power from the Hydrogen Generator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  .  .  LG .  
# MAGIC F2 E  HG HM .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Hydrogen-related items to the third floor, which is safe because the Hydrogen-compatible microchip is getting power from its generator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 E  HG HM LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Leave the Hydrogen Generator on floor three, but bring the Hydrogen-compatible Microchip back down with you so you can still use the elevator:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 E  .  HM .  .  
# MAGIC F1 .  .  .  .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>At the first floor, grab the Lithium-compatible Microchip, which is safe because Microchips don't affect each other:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 E  .  HM .  LM 
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips up one floor, where there is nothing to fry them:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 E  .  HM .  LM 
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips up again to floor three, where they can be temporarily connected to their corresponding generators while the elevator recharges, preventing either of them from being fried:</p><pre><code>F4 .  .  .  .  .  
# MAGIC F3 E  HG HM LG LM 
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips to the fourth floor:</p><pre><code>F4 E  .  HM .  LM 
# MAGIC F3 .  HG .  LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Leave the Lithium-compatible microchip on the fourth floor, but bring the Hydrogen-compatible one so you can still use the elevator; this is safe because although the Lithium Generator is on the destination floor, you can connect Hydrogen-compatible microchip to the Hydrogen Generator there:</p><pre><code>F4 .  .  .  .  LM 
# MAGIC F3 E  HG HM LG .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Generators up to the fourth floor, which is safe because you can connect the Lithium-compatible Microchip to the Lithium Generator upon arrival:</p><pre><code>F4 E  HG .  LG LM 
# MAGIC F3 .  .  HM .  .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring the Lithium Microchip with you to the third floor so you can use the elevator:</p><pre><code>F4 .  HG .  LG .  
# MAGIC F3 E  .  HM .  LM 
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC <li><p>Bring both Microchips to the fourth floor:</p><pre><code>F4 E  HG HM LG LM 
# MAGIC F3 .  .  .  .  .  
# MAGIC F2 .  .  .  .  .  
# MAGIC F1 .  .  .  .  .  
# MAGIC </code></pre></li>
# MAGIC </ul>
# MAGIC <p>In this arrangement, it takes <code>11</code> steps to collect all of the objects at the fourth floor for assembly. (Each elevator stop counts as one step, even if nothing is added to or removed from it.)</p>
# MAGIC <p>In your situation, what is the <em>minimum number of steps</em> required to bring all of the objects to the fourth floor?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.
"

# COMMAND ----------

# input <- "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.
# "

# COMMAND ----------

elements <- str_extract_all(input, "[\\w+]+(?=-compatible microchip| generator)") %>% unlist() %>% unique()
elements

# COMMAND ----------

lookup <- seq_len(2 * length(elements))

names(lookup) <- c(
  str_c(elements, "-compatible microchip"),
  str_c(elements, " generator")
)

floor_to_int <- function(floor) {
  lookup[floor]
}

floors_to_int <- function(floors) map(floors, floor_to_int)

# COMMAND ----------

floors <-
  read_lines(input) %>% 
  str_extract_all("[\\w+-]+( microchip| generator)") %>%
  floors_to_int() %>%
  map(sort)

floors

# COMMAND ----------

elevator_col <- 2 * length(elements) + 1
microchip_col <- seq(from = 1, to = length(elements), by = 1)
generator_col <- seq(from = length(elements) + 1, to = 2 * length(elements), by = 1)

lst(elevator_col, microchip_col, generator_col)

# COMMAND ----------

m_start <-
  floors %>%
  map(function(x) {
    v <- rep(FALSE, 2 * length(elements))
    v[x] <- TRUE
    v
  }) %>%
  simplify2array() %>%
  t() %>%
  cbind(c(TRUE, rep(FALSE, nrow(.) - 1)))

colnames(m_start) <- c(str_c(elements, "-M"), str_c(elements, "-G"), "E")
rownames(m_start) <- str_c("F", seq_len(nrow(m_start)))
m_start

# COMMAND ----------

is_valid <- function(m) {
  microchips <- m[,microchip_col]
  generators <- m[,generator_col]

  # Microchips without a corresponding generator
  exposed_microchips <- microchips & !generators

  # Filtered to floors that contain a generator
  !any(exposed_microchips[as.logical(apply(generators, 1, FUN=max)),])
}

hash_m <- function(m) str_c(m, collapse = "")

solve <- function(m = m_start) {
  ms <- list(m)
  n_moves <- c(0)
  
  done_states <- map_chr(ms, hash_m)
  
  repeat {
    # Choose the state with the least moves
    i <- which.min(n_moves)
    m <- ms[[i]]
    n_move <- n_moves[[i]]
    
    ms[[i]] <- NULL
    n_moves <- n_moves[-i]


    # All possible moves
    elevator <- which(m[, elevator_col])
    possble_items <- which(m[elevator, -elevator_col])
    for (new_elevator in c(elevator + 1, elevator - 1)) {
      if (new_elevator < 1 || new_elevator > nrow(m)) {
        next
      }
      
      for (item1 in possble_items) {
        for (item2 in c(0, possble_items[possble_items > item1])) {
          items <- c(item1, item2, elevator_col)
          
          new_m <- m
          new_m[elevator, items] <- FALSE
          new_m[new_elevator, items] <- TRUE
          
          if (!is_valid(m)) {
            next
          }
          
          
          # Check if the problem is solved
          if (all(new_m[nrow(new_m),])) {
            return(n_move + 1)
          }
          
          state_hash <- hash_m(new_m)
          if (!(state_hash %in% done_states)) { # If the state hasn't been reached before
            ms <- c(ms, list(new_m))
            n_moves <- c(n_moves, n_move + 1)
            done_states <- c(done_states, state_hash)
          }
        }
      }
    }
  }
}

# COMMAND ----------

answer <- solve()
answer # This took 8.4 hrs

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You step into the cleanroom separating the lobby from the isolated area and put on the hazmat suit.</p>
# MAGIC <p>Upon entering the isolated containment area, however, you notice some extra parts on the first floor that weren't listed on the record outside:</p>
# MAGIC <ul>
# MAGIC <li>An elerium generator.</li>
# MAGIC <li>An elerium-compatible microchip.</li>
# MAGIC <li>A dilithium generator.</li>
# MAGIC <li>A dilithium-compatible microchip.</li>
# MAGIC </ul>
# MAGIC <p>These work just like the other generators and microchips. You'll have to get them up to assembly as well.</p>
# MAGIC <p>What is the <em>minimum number of steps</em> required to bring all of the objects, including these four new ones, to the fourth floor?</p>
# MAGIC </article>

# COMMAND ----------

input <- "The first floor contains an elerium generator, an elerium-compatible microchip, a dilithium generator, dilithium-compatible microchip, a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.
"

# COMMAND ----------

elements <- str_extract_all(input, "[\\w+]+(?=-compatible microchip| generator)") %>% unlist() %>% unique()
elements

# COMMAND ----------

lookup <- seq_len(2 * length(elements))

names(lookup) <- c(
  str_c(elements, "-compatible microchip"),
  str_c(elements, " generator")
)

floor_to_int <- function(floor) {
  lookup[floor]
}

floors_to_int <- function(floors) map(floors, floor_to_int)

# COMMAND ----------

floors <-
  read_lines(input) %>% 
  str_extract_all("[\\w+-]+( microchip| generator)") %>%
  floors_to_int() %>%
  map(sort)

floors

# COMMAND ----------

elevator_col <- 2 * length(elements) + 1
microchip_col <- seq(from = 1, to = length(elements), by = 1)
generator_col <- seq(from = length(elements) + 1, to = 2 * length(elements), by = 1)

lst(elevator_col, microchip_col, generator_col)

# COMMAND ----------

m_start <-
  floors %>%
  map(function(x) {
    v <- rep(FALSE, 2 * length(elements))
    v[x] <- TRUE
    v
  }) %>%
  simplify2array() %>%
  t() %>%
  cbind(c(TRUE, rep(FALSE, nrow(.) - 1)))

colnames(m_start) <- c(str_c(elements, "-M"), str_c(elements, "-G"), "E")
rownames(m_start) <- str_c("F", seq_len(nrow(m_start)))
m_start

# COMMAND ----------

apply(m_start, 1, function(x) str_c(as.integer(x), collapse = "")) %>% str_c(collapse = "\n") %>% cat()

# COMMAND ----------

str_length("111100011110001")

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <algorithm>
#include <bitset>
#include <set>
#include <string>
#include <vector>

struct State {
    std::bitset<7> microchips[4];
    std::bitset<7> generators[4];
    int elevator;
    int moves;
};

bool is_valid(const State& state) {
    for (int i = 0; i < 4; ++i) {
      if ((state.microchips[i] & ~state.generators[i]).any() && state.generators[i].any()) {
          return false;
      }
    }
    return true;
}

bool is_solved(const State& state) {
    return state.microchips[3].all() && state.generators[3].all();
}

ulong hash(const State& state) {
    // Dont include moves in hash
    ulong result = state.elevator;
    ulong multiplier = 1;
    for (int i = 0; i < 4; ++i) {
        multiplier *= 256;
        result += multiplier * state.microchips[i].to_ulong();
        multiplier *= 256;
        result += multiplier * state.generators[i].to_ulong();
    }
    return result;
}

bool itemExists(const State& s, int elevator, int item) {
    if (item < 7) {
        return s.microchips[elevator][item];
    }
    if (item < 14) {
        return s.generators[elevator][item - 7];
    }
    if (item == 14) {
        return true; // 14 means no item
    }
}

void setItem(State& s, int elevator, int item, bool item_value) {
    if (item < 7) {
        s.microchips[elevator].set(item, item_value);
    }
    else if (item < 14) {
        s.generators[elevator].set(item - 7, item_value);
    }
    else if (item == 14) {
        // Do nothing. 14 means there is no item
    }
}

// [[Rcpp::export]]
int solve_cpp() 
{
    State start_state = {
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      0,
      0
    };

    
    auto cmp = [](const State& left, const State& right) { return left.moves < right.moves; };

    std::vector<State> states;
    states.push_back(start_state);
    std::push_heap(states.begin(), states.end(), cmp);
    std::set<ulong > done_states;
    
    while (true) {
        State s = states.front();
        std::pop_heap(states.begin(), states.end(), cmp);
        states.pop_back(); // Actually remove the element

        for (int new_elevator : {s.elevator - 1, s.elevator + 1}) {
            if (new_elevator < 0 || new_elevator >= 4) continue;
            for (int item1 = 0; item1 < 14; ++item1) {
                if (!itemExists(s, new_elevator, item1)) continue;
                for (int item2 = item1 + 1; item2 <= 14; ++item2) {
                    if (!itemExists(s, new_elevator, item2)) continue;
                
                    State new_state(s);
                    new_state.elevator = new_elevator;
                    new_state.moves = new_state.moves + 1;
                    setItem(new_state, s.elevator, item1, false);
                    setItem(new_state, s.elevator, item2, false);
                    setItem(new_state, new_state.elevator, item1, true);
                    setItem(new_state, new_state.elevator, item2, true);

                    ulong new_hash = hash(new_state);
                    if (!done_states.count(new_hash)) continue;
                    done_states.insert(new_hash);

                    if (!is_valid(new_state)) continue;

                    if (is_solved(new_state)) return new_state.moves;
      
                    states.push_back(new_state);
                    std::push_heap(states.begin(), states.end(), cmp);
                }
            }
        }
    }

    return -1;
} 
')

# COMMAND ----------

solve_cpp()

# COMMAND ----------

# Ideas for R - check the hash first.
# Maybe if you store it as
# element1 = c(chip_floor, generator_floor)
# 
# The you can sort 1, 2 to get hash - so order of elements doesn't matter

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <algorithm>
#include <bitset>
#include <set>
#include <string>
#include <vector>

struct State {
    std::bitset<7> microchips[4];
    std::bitset<7> generators[4];
    int elevator;
    int moves;
};

bool is_valid(const State& state) {
    for (int i = 0; i < 4; ++i) {
      if ((state.microchips[i] & ~state.generators[i]).any() && state.generators[i].any()) {
          return false;
      }
    }
    return true;
}

ulong hash(const State& state) {
    // Dont include moves in hash
    ulong result = state.elevator;
    ulong multiplier = 1;
    for (int i = 0; i < 4; ++i) {
        multiplier *= 256;
        result += multiplier * state.microchips[i].to_ulong();
        multiplier *= 256;
        result += multiplier * state.generators[i].to_ulong();
    }
    return result;
}

// std::bitset::reference getItem(State& s, int elevator, int item) {
//     if (item < 7) {
//         return s.microchips[elevator][item];
//     }
//     if (item < 14) {
//         return s.generators[elevator][item - 7];
//     }
//     return ??? I think I need optional?
// }

// bool itemExists(const State& s, int elevator, int item) {
//     if (item < 7) {
//         return s.microchips[elevator][item];
//     }
//     if (item < 14) {
//         return s.generators[elevator][item - 7];
//     }
//     if (item == 14) {
//         return true; // 14 means no item
//     }
// }

// [[Rcpp::export]]
int solve_cpp() 
{
    State start_state = {
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      0,
      0
    };

    std::vector<State> states;
    states.push_back(start_state);
    std::push_heap(states.begin(), states.end(), [](const State& left, const State& right) { return left.moves < right.moves; });
    std::set<ulong > done_states;
    
    while (true) {
        State s = states.front();
        std::pop_heap(states.begin(), states.end());

        // for (int new_elevator : {s.elevator - 1, s.elevator + 1}) {
        //     if (new_elevator < 0 || new_elevator >= 4) continue;
        //     for (int item1 = 0; item1 < 14; ++item1) {
        //         if (!itemExists(s, new_elevator, item1)) continue; // Check if item1 exists
        //         for (int item2 = item1 + 1; item2 <= 14; ++item2) {
        //             if (!itemExists(s, new_elevator, item2)) continue; // Check if item2 exists
        //         
        //         }
        //     }
        // }

        break;
    }

    return 0;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <set>
#include <vector>

struct State {
    std::bitset<7> microchips[4];
    std::bitset<7> generators[4];
    int elevator;
};

bool is_valid(const State& state) {
    for (int i = 0; i < 4; ++i) {
      //if ((state.microchips[i] & state.generators[i].flip()).any() && state.generators[i].any()) {
      std::bitset<7> not_generators(state.generators);
      not_generators.flip();
      if ((state.microchips[i] & not_generators).any() && state.generators[i].any()) {
          return false;
      }
    }
    return true;
}

ulong hash(const State& state) {
    ulong result = state.elevator;
    ulong multiplier = 1;
    for (int i = 0; i < 4; ++i) {
        multiplier *= 256;
        result += multiplier * state.microchips[i].to_ulong();
        multiplier *= 256;
        result += multiplier * state.generators[i].to_ulong();
    }
    return result;
}

// [[Rcpp::export]]
int solve_cpp() 
{
    std::bitset<7> microchips[] = {
        std::bitset<7>("11110001"),
        std::bitset<7>("00001110"),
        std::bitset<7>("00000000"),
        std::bitset<7>("00000000")
    };
    std::bitset<7> generators[] = {
        std::bitset<7>("11110001"),
        std::bitset<7>("00001110"),
        std::bitset<7>("00000000"),
        std::bitset<7>("00000000")
    };

    std::set<ulong > done_states;
    // done_states.insert()

    State state = {
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      {
          std::bitset<7>("11110001"),
          std::bitset<7>("00001110"),
          std::bitset<7>("00000000"),
          std::bitset<7>("00000000")
      },
      0
    };


    int elevator = 0;
    // return is_valid(microchips, generators);
    // return hash(state);
    return is_valid(state);
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <set>
#include <vector>

bool is_valid(std::bitset<7> microchips[4], std::bitset<7> generators[4]) {
    for (int i = 0; i < 4; ++i) {
      if ((microchips[i] & generators[i].flip()).any() && generators[i].any()) {
          return false;
      }
    }
    return true;
}

ulong hash(std::bitset<7> microchips[4], std::bitset<7> generators[4], int elevator) {
    ulong result = elevator;
    ulong multiplier = 1;
    for (int i = 0; i < 4; ++i) {
        multiplier *= 256;
        result += multiplier * microchips[i].to_ulong();
        multiplier *= 256;
        result += multiplier * generators[i].to_ulong();
    }
    return result;
}

// [[Rcpp::export]]
int solve_cpp() 
{
    std::bitset<7> microchips[] = {
        std::bitset<7>("11110001"),
        std::bitset<7>("00001110"),
        std::bitset<7>("00000000"),
        std::bitset<7>("00000000")
    };
    std::bitset<7> generators[] = {
        std::bitset<7>("11110001"),
        std::bitset<7>("00001110"),
        std::bitset<7>("00000000"),
        std::bitset<7>("00000000")
    };

    std::set<ulong > done_states;
    // done_states.insert()


    int elevator = 0;
    // return is_valid(microchips, generators);
    return hash(microchips, generators, elevator);
} 
')

# COMMAND ----------

solve_cpp()

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state[1] = {std::bitset<15>("111100011110001")};
    return 1;
} 
')

# COMMAND ----------



# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state("111100011110001");
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state(std::string("111100011110001"));
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <string>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state = std::string("111100011110001");
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state[4] = {};
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state[] = {
        std::string("111100011110001")
    };
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state[] = {
        "111100011110001",
        "000001100001110",
        "000010000000000",
        "000000000000000"
    };
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <vector>

int solve_cpp() 
{
    std::bitset<15> state[] = {
        {"111100011110001"},
        {"000001100001110"},
        {"000010000000000"},
        {"000000000000000"}
    };
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp(
  code = '
#include <bitset>
#include <vector>

// [[Rcpp::export]]
int solve_cpp() 
{
    std::vector<std::bitset<15> > state{{"111100011110001"}, {"000001100001110"}, {"000010000000000"}, {"000000000000000"}};
    return 1;
} 
')

# COMMAND ----------

Rcpp::sourceCpp

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp() 
{
    std::bitset<15> a;
    return 1;
} 
')

# COMMAND ----------

Rcpp::cppFunction(
  include = "bitset",
'
int solve_cpp() 
{
    std::vector<std::bitset<15> > state{"111100011110001", "000001100001110", "000010000000000", "000000000000000"};
    return 1;
} 
')

# COMMAND ----------

?cppFunction

# COMMAND ----------

std::bitset<4> b3{"0011"}

# COMMAND ----------

# answer <- solve()
# answer # This took ?? hrs

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ## Try c++

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp(int64_t n, std::vector<int64_t> init) 
{ 
    std::unordered_map<int64_t, int64_t> hashtable;
    int64_t v_prev = init.back();
    int64_t v;
    
    for (int i = 1; i <= init.size(); ++i) {
      hashtable[init[i - 1]] = i;
    }
    
    for (int i = init.size() + 1; i <= n; ++i) {
      v = hashtable[v_prev] ? i - 1 - hashtable[v_prev] : 0;
      hashtable[v_prev] = i - 1;
      v_prev = v;
    }
    
    return v;
} 
')

# COMMAND ----------

is_valid <- function(m) {
  microchips <- m[,microchip_col]
  generators <- m[,generator_col]

  # Microchips without a corresponding generator
  exposed_microchips <- microchips & !generators

  # Filtered to floors that contain a generator
  !any(exposed_microchips[as.logical(apply(generators, 1, FUN=max)),])
}

hash_m <- function(m) str_c(m, collapse = "")

solve <- function(m = m_start) {
  ms <- list(m)
  n_moves <- c(0)
  
  done_states <- map_chr(ms, hash_m)
  
  repeat {
    # Choose the state with the least moves
    i <- which.min(n_moves)
    m <- ms[[i]]
    n_move <- n_moves[[i]]
    
    ms[[i]] <- NULL
    n_moves <- n_moves[-i]


    # All possible moves
    elevator <- which(m[, elevator_col])
    possble_items <- which(m[elevator, -elevator_col])
    for (new_elevator in c(elevator + 1, elevator - 1)) {
      if (new_elevator < 1 || new_elevator > nrow(m)) {
        next
      }
      
      for (item1 in possble_items) {
        for (item2 in c(0, possble_items[possble_items > item1])) {
          items <- c(item1, item2, elevator_col)
          
          new_m <- m
          new_m[elevator, items] <- FALSE
          new_m[new_elevator, items] <- TRUE
          
          if (!is_valid(m)) {
            next
          }
          
          
          # Check if the problem is solved
          if (all(new_m[nrow(new_m),])) {
            return(n_move + 1)
          }
          
          state_hash <- hash_m(new_m)
          if (!(state_hash %in% done_states)) { # If the state hasn't been reached before
            ms <- c(ms, list(new_m))
            n_moves <- c(n_moves, n_move + 1)
            done_states <- c(done_states, state_hash)
          }
        }
      }
    }
  }
}
