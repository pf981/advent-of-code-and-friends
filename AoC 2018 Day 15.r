# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 15: Beverage Bandits ---</h2><p>Having perfected their hot chocolate, the Elves have a new problem: the <a href="https://en.wikipedia.org/wiki/Goblin">Goblins</a> that live in these caves will do anything to steal it. Looks like they're here for a fight.</p>
# MAGIC <p>You scan the area, generating a map of the walls (<code>#</code>), open cavern (<code>.</code>), and starting position of every Goblin (<code>G</code>) and Elf (<code>E</code>) (your puzzle input).</p>
# MAGIC <p>Combat proceeds in <em>rounds</em>; in each round, each unit that is still alive takes a <em>turn</em>, resolving all of its actions before the next unit's turn begins. On each unit's turn, it tries to <em>move</em> into range of an enemy (if it isn't already) and then <em>attack</em> (if it is in range).</p>
# MAGIC <p>All units are very disciplined and always follow very strict combat rules. Units never move or attack diagonally, as doing so would be dishonorable. When multiple choices are equally valid, ties are broken in <em>reading order</em>: top-to-bottom, then left-to-right.  For instance, the order in which units take their turns within a round is the <em>reading order of their starting positions</em> in that round, regardless of the type of unit or whether other units have moved after the round started.  For example:</p>
# MAGIC <pre><code>                 would take their
# MAGIC These units:   turns in this order:
# MAGIC   #######           #######
# MAGIC   #.G.E.#           #.1.2.#
# MAGIC   #E.G.E#           #3.4.5#
# MAGIC   #.G.E.#           #.6.7.#
# MAGIC   #######           #######
# MAGIC </code></pre>
# MAGIC <p>Each unit begins its turn by identifying all possible <em>targets</em> (enemy units). If no targets remain, combat ends.</p>
# MAGIC <p>Then, the unit identifies all of the open squares (<code>.</code>) that are <em>in range</em> of each target; these are the squares which are <em>adjacent</em> (immediately up, down, left, or right) to any target and which aren't already occupied by a wall or another unit. Alternatively, the unit might <em>already</em> be in range of a target. If the unit is not already in range of a target, and there are no open squares which are in range of a target, the unit ends its turn.</p>
# MAGIC <p>If the unit is already in range of a target, it does not <em>move</em>, but continues its turn with an <em>attack</em>. Otherwise, since it is not in range of a target, it <em>moves</em>.</p>
# MAGIC <p>To <em>move</em>, the unit first considers the squares that are <em>in range</em> and determines <em>which of those squares it could reach in the fewest steps</em>. A <em>step</em> is a single movement to any <em>adjacent</em> (immediately up, down, left, or right) open (<code>.</code>) square. Units cannot move into walls or other units. The unit does this while considering the <em>current positions of units</em> and does <em>not</em> do any prediction about where units will be later. If the unit cannot reach (find an open path to) any of the squares that are in range, it ends its turn. If multiple squares are in range and <em>tied</em> for being reachable in the fewest steps, the square which is first in <em>reading order</em> is chosen. For example:</p>
# MAGIC <pre><code>Targets:      In range:     Reachable:    Nearest:      Chosen:
# MAGIC #######       #######       #######       #######       #######
# MAGIC #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
# MAGIC #...#.#  --&gt;  #.?.#?#  --&gt;  #.@.#.#  --&gt;  #.!.#.#  --&gt;  #...#.#
# MAGIC #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
# MAGIC #######       #######       #######       #######       #######
# MAGIC </code></pre>
# MAGIC <p>In the above scenario, the Elf has three targets (the three Goblins):</p>
# MAGIC <ul>
# MAGIC <li>Each of the Goblins has open, adjacent squares which are <em>in range</em> (marked with a <code>?</code> on the map).</li>
# MAGIC <li>Of those squares, four are <em>reachable</em> (marked <code>@</code>); the other two (on the right) would require moving through a wall or unit to reach.</li>
# MAGIC <li>Three of these reachable squares are <em>nearest</em>, requiring the fewest steps (only <code>2</code>) to reach (marked <code>!</code>).</li>
# MAGIC <li>Of those, the square which is first in reading order is <em>chosen</em> (<code>+</code>).</li>
# MAGIC </ul>
# MAGIC <p>The unit then takes a single <em>step</em> toward the chosen square along the <em>shortest path</em> to that square. If multiple steps would put the unit equally closer to its destination, the unit chooses the step which is first in reading order. (This requires knowing when there is <em>more than one shortest path</em> so that you can consider the first step of each such path.) For example:</p>
# MAGIC <pre><code>In range:     Nearest:      Chosen:       Distance:     Step:
# MAGIC #######       #######       #######       #######       #######
# MAGIC #.E...#       #.E...#       #.E...#       #4E<em>2</em>12#       #..E..#
# MAGIC #...?.#  --&gt;  #...!.#  --&gt;  #...+.#  --&gt;  #3<em>2</em>101#  --&gt;  #.....#
# MAGIC #..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
# MAGIC #######       #######       #######       #######       #######
# MAGIC </code></pre>
# MAGIC <p>The Elf sees three squares in range of a target (<code>?</code>), two of which are nearest (<code>!</code>), and so the first in reading order is chosen (<code>+</code>). Under "Distance", each open square is marked with its distance from the destination square; the two squares to which the Elf could move on this turn (down and to the right) are both equally good moves and would leave the Elf <code>2</code> steps from being in range of the Goblin. Because the step which is first in reading order is chosen, the Elf moves <em>right</em> one square.</p>
# MAGIC <p>Here's a larger example of movement:</p>
# MAGIC <pre><code>Initially:
# MAGIC #########
# MAGIC #G..G..G#
# MAGIC #.......#
# MAGIC #.......#
# MAGIC #G..E..G#
# MAGIC #.......#
# MAGIC #.......#
# MAGIC #G..G..G#
# MAGIC #########
# MAGIC 
# MAGIC After 1 round:
# MAGIC #########
# MAGIC #.G...G.#
# MAGIC #...G...#
# MAGIC #...E..G#
# MAGIC #.G.....#
# MAGIC #.......#
# MAGIC #G..G..G#
# MAGIC #.......#
# MAGIC #########
# MAGIC 
# MAGIC After 2 rounds:
# MAGIC #########
# MAGIC #..G.G..#
# MAGIC #...G...#
# MAGIC #.G.E.G.#
# MAGIC #.......#
# MAGIC #G..G..G#
# MAGIC #.......#
# MAGIC #.......#
# MAGIC #########
# MAGIC 
# MAGIC After 3 rounds:
# MAGIC #########
# MAGIC #.......#
# MAGIC #..GGG..#
# MAGIC #..GEG..#
# MAGIC #G..G...#
# MAGIC #......G#
# MAGIC #.......#
# MAGIC #.......#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Once the Goblins and Elf reach the positions above, they all are either in range of a target or cannot find any square in range of a target, and so none of the units can move until a unit dies.</p>
# MAGIC <p>After moving (or if the unit began its turn in range of a target), the unit <em>attacks</em>.</p>
# MAGIC <p>To <em>attack</em>, the unit first determines <em>all</em> of the targets that are <em>in range</em> of it by being immediately <em>adjacent</em> to it. If there are no such targets, the unit ends its turn. Otherwise, the adjacent target with the <em>fewest hit points</em> is selected; in a tie, the adjacent target with the fewest hit points which is first in reading order is selected.</p>
# MAGIC <p>The unit deals damage equal to its <em>attack power</em> to the selected target, reducing its hit points by that amount. If this reduces its hit points to <code>0</code> or fewer, the selected target <em>dies</em>: its square becomes <code>.</code> and it takes no further turns.</p>
# MAGIC <p>Each <em>unit</em>, either Goblin or Elf, has <code>3</code> <em>attack power</em> and starts with <code>200</code> <em>hit points</em>.</p>
# MAGIC <p>For example, suppose the only Elf is about to attack:</p>
# MAGIC <pre><code>       HP:            HP:
# MAGIC G....  9       G....  9  
# MAGIC ..G..  4       ..G..  4  
# MAGIC ..E<em>G</em>.  2  --&gt;  ..E..     
# MAGIC ..G..  2       ..G..  2  
# MAGIC ...G.  1       ...G.  1  
# MAGIC </code></pre>
# MAGIC <p>The "HP" column shows the hit points of the Goblin to the left in the corresponding row. The Elf is in range of three targets: the Goblin above it (with <code>4</code> hit points), the Goblin to its right (with <code>2</code> hit points), and the Goblin below it (also with <code>2</code> hit points). Because three targets are in range, the ones with the lowest hit points are selected: the two Goblins with <code>2</code> hit points each (one to the right of the Elf and one below the Elf). Of those, the Goblin first in reading order (the one to the right of the Elf) is selected. The selected Goblin's hit points (<code>2</code>) are reduced by the Elf's attack power (<code>3</code>), reducing its hit points to <code>-1</code>, killing it.</p>
# MAGIC <p>After attacking, the unit's turn ends.  Regardless of how the unit's turn ends, the next unit in the round takes its turn.  If all units have taken turns in this round, the round ends, and a new round begins.</p>
# MAGIC <p>The Elves look quite outnumbered.  You need to determine the <em>outcome</em> of the battle: the <em>number of full rounds that were completed</em> (not counting the round in which combat ends) multiplied by <em>the sum of the hit points of all remaining units</em> at the moment combat ends. (Combat only ends when a unit finds no targets during its turn.)</p>
# MAGIC <p>Below is an entire sample combat. Next to each map, each row's units' hit points are listed from left to right.</p>
# MAGIC <pre><code>Initially:
# MAGIC #######   
# MAGIC #.G...#   G(200)
# MAGIC #...EG#   E(200), G(200)
# MAGIC #.#.#G#   G(200)
# MAGIC #..G#E#   G(200), E(200)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC After 1 round:
# MAGIC #######   
# MAGIC #..G..#   G(200)
# MAGIC #...EG#   E(197), G(197)
# MAGIC #.#G#G#   G(200), G(197)
# MAGIC #...#E#   E(197)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC After 2 rounds:
# MAGIC #######   
# MAGIC #...G.#   G(200)
# MAGIC #..GEG#   G(200), E(188), G(194)
# MAGIC #.#.#G#   G(194)
# MAGIC #...#E#   E(194)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC Combat ensues; eventually, the top Elf dies:
# MAGIC 
# MAGIC After 23 rounds:
# MAGIC #######   
# MAGIC #...G.#   G(200)
# MAGIC #..G.G#   G(200), G(131)
# MAGIC #.#.#G#   G(131)
# MAGIC #...#E#   E(131)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC After 24 rounds:
# MAGIC #######   
# MAGIC #..G..#   G(200)
# MAGIC #...G.#   G(131)
# MAGIC #.#G#G#   G(200), G(128)
# MAGIC #...#E#   E(128)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC After 25 rounds:
# MAGIC #######   
# MAGIC #.G...#   G(200)
# MAGIC #..G..#   G(131)
# MAGIC #.#.#G#   G(125)
# MAGIC #..G#E#   G(200), E(125)
# MAGIC #.....#   
# MAGIC #######   
# MAGIC 
# MAGIC After 26 rounds:
# MAGIC #######   
# MAGIC #G....#   G(200)
# MAGIC #.G...#   G(131)
# MAGIC #.#.#G#   G(122)
# MAGIC #...#E#   E(122)
# MAGIC #..G..#   G(200)
# MAGIC #######   
# MAGIC 
# MAGIC After 27 rounds:
# MAGIC #######   
# MAGIC #G....#   G(200)
# MAGIC #.G...#   G(131)
# MAGIC #.#.#G#   G(119)
# MAGIC #...#E#   E(119)
# MAGIC #...G.#   G(200)
# MAGIC #######   
# MAGIC 
# MAGIC After 28 rounds:
# MAGIC #######   
# MAGIC #G....#   G(200)
# MAGIC #.G...#   G(131)
# MAGIC #.#.#G#   G(116)
# MAGIC #...#E#   E(113)
# MAGIC #....G#   G(200)
# MAGIC #######   
# MAGIC 
# MAGIC More combat ensues; eventually, the bottom Elf dies:
# MAGIC 
# MAGIC After 47 rounds:
# MAGIC #######   
# MAGIC #G....#   G(200)
# MAGIC #.G...#   G(131)
# MAGIC #.#.#G#   G(59)
# MAGIC #...#.#   
# MAGIC #....G#   G(200)
# MAGIC #######   
# MAGIC </code></pre>
# MAGIC <p>Before the 48th round can finish, the top-left Goblin finds that there are no targets remaining, and so combat ends. So, the number of <em>full rounds</em> that were completed is <code><em>47</em></code>, and the sum of the hit points of all remaining units is <code>200+131+59+200 = <em>590</em></code>. From these, the <em>outcome</em> of the battle is <code>47 * 590 = <em>27730</em></code>.</p>
# MAGIC <p>Here are a few example summarized combats:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #G..#E#       #...#E#   E(200)
# MAGIC #E#E.E#       #E#...#   E(197)
# MAGIC #G.##.#  --&gt;  #.E##.#   E(185)
# MAGIC #...#E#       #E..#E#   E(200), E(200)
# MAGIC #...E.#       #.....#
# MAGIC #######       #######
# MAGIC 
# MAGIC Combat ends after 37 full rounds
# MAGIC Elves win with 982 total hit points left
# MAGIC Outcome: 37 * 982 = <em>36334</em>
# MAGIC </code></pre>
# MAGIC <pre><code>#######       #######   
# MAGIC #E..EG#       #.E.E.#   E(164), E(197)
# MAGIC #.#G.E#       #.#E..#   E(200)
# MAGIC #E.##E#  --&gt;  #E.##.#   E(98)
# MAGIC #G..#.#       #.E.#.#   E(200)
# MAGIC #..E#.#       #...#.#   
# MAGIC #######       #######   
# MAGIC 
# MAGIC Combat ends after 46 full rounds
# MAGIC Elves win with 859 total hit points left
# MAGIC Outcome: 46 * 859 = <em>39514</em>
# MAGIC </code></pre>
# MAGIC <pre><code>#######       #######   
# MAGIC #E.G#.#       #G.G#.#   G(200), G(98)
# MAGIC #.#G..#       #.#G..#   G(200)
# MAGIC #G.#.G#  --&gt;  #..#..#   
# MAGIC #G..#.#       #...#G#   G(95)
# MAGIC #...E.#       #...G.#   G(200)
# MAGIC #######       #######   
# MAGIC 
# MAGIC Combat ends after 35 full rounds
# MAGIC Goblins win with 793 total hit points left
# MAGIC Outcome: 35 * 793 = <em>27755</em>
# MAGIC </code></pre>
# MAGIC <pre><code>#######       #######   
# MAGIC #.E...#       #.....#   
# MAGIC #.#..G#       #.#G..#   G(200)
# MAGIC #.###.#  --&gt;  #.###.#   
# MAGIC #E#G#G#       #.#.#.#   
# MAGIC #...#G#       #G.G#G#   G(98), G(38), G(200)
# MAGIC #######       #######   
# MAGIC 
# MAGIC Combat ends after 54 full rounds
# MAGIC Goblins win with 536 total hit points left
# MAGIC Outcome: 54 * 536 = <em>28944</em>
# MAGIC </code></pre>
# MAGIC <pre><code>#########       #########   
# MAGIC #G......#       #.G.....#   G(137)
# MAGIC #.E.#...#       #G.G#...#   G(200), G(200)
# MAGIC #..##..G#       #.G##...#   G(200)
# MAGIC #...##..#  --&gt;  #...##..#   
# MAGIC #...#...#       #.G.#...#   G(200)
# MAGIC #.G...G.#       #.......#   
# MAGIC #.....G.#       #.......#   
# MAGIC #########       #########   
# MAGIC 
# MAGIC Combat ends after 20 full rounds
# MAGIC Goblins win with 937 total hit points left
# MAGIC Outcome: 20 * 937 = <em>18740</em>
# MAGIC </code></pre>
# MAGIC <p><em>What is the outcome</em> of the combat described in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "################################
#####################...########
##########.##########..#########
##########.##########...########
#######....########..G.G########
######.....######..........#####
#######....######G.........#####
#######...G#####...........#####
#######..#.####............#####
########....###..G.......E######
######....####.............#####
######.G###............G......##
######..##G...#####............#
#######......#######.E........##
#######..G..#########.........##
######..#.G.#########G........##
#####.......#########G...E.E...#
#####.G.....#########....E.....#
###...###...#########..E.......#
####.###.....#######E....E...E##
####.##.......#####....#.....###
##..G.#..G............####....##
##..............##########..E###
#....#.G........#.##########.###
#.........G.......##########.###
##......GG##G.....##############
#........#####....##############
#..###.########...##############
#..#############..##############
##.#############################
##.#############################
################################
"

# COMMAND ----------

# input <- "#######
# #.G...#
# #...EG#
# #.#.#G#
# #..G#E#
# #.....#
# #######
# "

# COMMAND ----------

# input <- "#########
# #G..G..G#
# #.......#
# #.......#
# #G..E..G#
# #.......#
# #.......#
# #G..G..G#
# #########
# "

# COMMAND ----------

# input <- "#######
# #G..#E#
# #E#E.E#
# #G.##.#
# #...#E#
# #...E.#
# #######
# "

# COMMAND ----------

# input <- "#######
# #E..EG#
# #.#G.E#
# #E.##E#
# #G..#.#
# #..E#.#
# #######
# "

# COMMAND ----------

# input <- "#######
# #E.G#.#
# #.#G..#
# #G.#.G#
# #G..#.#
# #...E.#
# #######
# "

# COMMAND ----------

# input <- "#######
# #.E...#
# #.#..G#
# #.###.#
# #E#G#G#
# #...#G#
# #######
# "

# COMMAND ----------

# input <- "#########
# #G......#
# #.E.#...#
# #..##..G#
# #...##..#
# #...#...#
# #.G...G.#
# #.....G.#
# #########
# "

# COMMAND ----------

# input <- "################################
# #####################...########
# ##########.##########..#########
# ##########.##########...########
# #######....########.....########
# ######.....######..........#####
# #######....######..........#####
# #######....#####...........#####
# #######..#.####........G...#####
# ########....###.......G.GE######
# ######....####.....G...GE..#####
# ######..###...G........G......##
# ######..##....#####............#
# #######..G...#######.G........##
# #######..G..#########EGEE.....##
# ######..#...#########GE.......##
# #####.......#########E.E.......#
# #####....G..#########GE........#
# ###...###...#########G.........#
# ####.###..G..#######..........##
# ####.##.......#####....#.....###
# ##....#....GG.G.......####....##
# ##..............##########...###
# #....#..........#.##########.###
# #.................##########.###
# ##........##......##############
# #........#####....##############
# #..###.########...##############
# #..#############..##############
# ##.#############################
# ##.#############################
# ################################
# "

# COMMAND ----------

start_m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()

start_m

# COMMAND ----------

hp <- matrix(0, nrow = nrow(start_m), ncol = ncol(start_m))
hp[start_m %in% c("G", "E")] <- 200

hp

# COMMAND ----------

# The most efficient way is to get number of steps from all enemies to everywhere else. Then just choose the mn adjacent square. But that would need to be resolved in reverse order

# Easiest way is solve up, left, right, down separately and pick the smallest

# Memoise move will dramaticall speed up

# COMMAND ----------

get_adjacent_squares <- function(targets, m, square_type) {
  bind_rows(
    tibble(row = targets$row - 1, col = targets$col),
    tibble(row = targets$row + 1, col = targets$col),
    tibble(row = targets$row, col = targets$col - 1),
    tibble(row = targets$row, col = targets$col + 1)
  ) %>%
    filter(row >= 1, row <= nrow(m), col >= 1, col <= ncol(m)) %>%
    filter(map2_lgl(row, col, ~m[.x, .y] %in% square_type)) %>%
    arrange(row, col)
}

which_df <- function(w, m) {
  w <- matrix(w, nrow = nrow(m))
  which(w, arr.ind = TRUE) %>% as_tibble() %>% arrange(row, col)
}

move <- function(state, cur_pos, target_squares) {
  for (i in seq_len(nrow(target_squares))) {
    state$m[target_squares$row[i], target_squares$col[i]] <- "T"
  }
    
  ds <- c(0)
  rows <- c(cur_pos$row)
  cols <- c(cur_pos$col)
  first_rows <- c(NA)
  first_cols <- c(NA)
  
  while (length(ds) > 0) {
    # print(ds)
    i <- which.min(ds)
    
    d <- ds[i]
    cur_row <- rows[i]
    cur_col <- cols[i]
    cur_first_row <- first_rows[i]
    cur_first_col <- first_cols[i]
    
    ds <- ds[-i]
    rows <- rows[-i]
    cols <- cols[-i]
    first_rows <- first_rows[-i]
    first_cols <- first_cols[-i]
    
    if (state$m[cur_row, cur_col] == "#") next
    
    if (is.na(cur_first_row) && !(cur_row == cur_pos$row && cur_col == cur_pos$col)) {
      cur_first_row <- cur_row
      cur_first_col <- cur_col
    }
    
    # message(glue::glue("Trying ({cur_row}, {cur_col}): {s$m[cur_row, cur_col]}"))
    
    # If found target
    # mym <<- s$m # FIXME: TEST
    # stop(s$m) # FIXME: TEST
    if (state$m[cur_row, cur_col] == "T") {
      return(tibble(row = cur_first_row, col = cur_first_col))
    }
    
    # Don't revisit this position
    state$m[cur_row, cur_col] <- "#"
    
    new_squares <- get_adjacent_squares(tibble(row = cur_row, col = cur_col), state$m, c(".", "T"))
    
    for (new_square_i in seq_len(nrow(new_squares))) {
      ds <- c(ds, d + 1)
      rows <- c(rows, new_squares$row[new_square_i])
      cols <- c(cols, new_squares$col[new_square_i])
      first_rows <- c(first_rows, cur_first_row)
      first_cols <- c(first_cols, cur_first_col)
    }
  }
  cur_pos
}

step <- function(state) {
  units <- which_df(state$m %in% c("G", "E"), state$m)
  #print("units:") # FIXME: Remove
  #print(units) # FIXME: Remove

  for (i in seq_len(nrow(units))) {
    cur_pos <- slice(units, i)
    if (state$hp[cur_pos$row, cur_pos$col] <= 0) next
    
    enemy_type <- ifelse(state$m[cur_pos$row, cur_pos$col] == "G", "E", "G")
    
    # Identify targets
    targets <- which_df(state$m == enemy_type, state$m)
    
    # If there are no more targets, the game is over
    if (nrow(targets) < 1) return(state)
    
    # Identify adjacent squares to targets not occupied
    target_squares <- get_adjacent_squares(targets, state$m, ".")
    
    # If not in range, then move
    if (nrow(get_adjacent_squares(cur_pos, state$m, enemy_type)) == 0) {
      #message(glue::glue("Unit ({cur_pos[1]}, {cur_pos[2]}) moving.")) # FIXME: REMOVE
      new_pos <- move(state, cur_pos, target_squares)
  
      if (!(new_pos$row == cur_pos$row && new_pos$col == cur_pos$col)) {
        state$m[new_pos$row, new_pos$col] <- state$m[cur_pos$row, cur_pos$col]
        state$m[cur_pos$row, cur_pos$col] <- "."

        state$hp[new_pos$row, new_pos$col] <- state$hp[cur_pos$row, cur_pos$col]
        state$hp[cur_pos$row, cur_pos$col] <- 0

        cur_pos <- new_pos
      }
      
    }
    
    # If in range, attack
    in_range_targets <- get_adjacent_squares(cur_pos, state$m, enemy_type)
    if (nrow(in_range_targets) >= 1) {
      target <-
        in_range_targets %>%
        mutate(
          target_hp = map2_dbl(row, col, ~state$hp[.x, .y])
        ) %>%
        arrange(target_hp, row, col)
      
      attack_row <- target$row[1]
      attack_col <- target$col[1]
      state$hp[attack_row, attack_col] <- state$hp[attack_row, attack_col] - 3
      if (state$hp[attack_row, attack_col] <= 0) {
        state$m[attack_row, attack_col] <- "."
      }
    }
  }
  state$rounds_completed <- state$rounds_completed + 1
  state
}

# COMMAND ----------

state <- list(
  m = start_m,
  hp = hp,
  rounds_completed = 0
)

rounds_completed <- 0
repeat {
  state <- step(state)
  if (state$rounds_completed == rounds_completed) break
  rounds_completed <- state$rounds_completed
}

answer <- rounds_completed * sum(state$hp %>% keep(~ . > 0))
answer # 37.05 minutes

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>According to your calculations, the Elves are going to lose badly. Surely, you won't mess up the timeline too much if you give them <span title="See also: the plot of every Civilization game.">just a little advanced technology</span>, right?</p>
# MAGIC <p>You need to make sure the Elves not only <em>win</em>, but also suffer <em>no losses</em>: even the death of a single Elf is unacceptable.</p>
# MAGIC <p>However, you can't go too far: larger changes will be more likely to permanently alter spacetime.</p>
# MAGIC <p>So, you need to <em>find the outcome</em> of the battle in which the Elves have the <em>lowest integer attack power</em> (at least <code>4</code>) that allows them to <em>win without a single death</em>. The Goblins always have an attack power of <code>3</code>.</p>
# MAGIC <p>In the first summarized example above, the lowest attack power the Elves need to win without losses is <code>15</code>:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #.G...#       #..E..#   E(158)
# MAGIC #...EG#       #...E.#   E(14)
# MAGIC #.#.#G#  --&gt;  #.#.#.#
# MAGIC #..G#E#       #...#.#
# MAGIC #.....#       #.....#
# MAGIC #######       #######
# MAGIC 
# MAGIC Combat ends after 29 full rounds
# MAGIC Elves win with 172 total hit points left
# MAGIC Outcome: 29 * 172 = <em>4988</em>
# MAGIC </code></pre>
# MAGIC <p>In the second example above, the Elves need only <code>4</code> attack power:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #E..EG#       #.E.E.#   E(200), E(23)
# MAGIC #.#G.E#       #.#E..#   E(200)
# MAGIC #E.##E#  --&gt;  #E.##E#   E(125), E(200)
# MAGIC #G..#.#       #.E.#.#   E(200)
# MAGIC #..E#.#       #...#.#
# MAGIC #######       #######
# MAGIC 
# MAGIC Combat ends after 33 full rounds
# MAGIC Elves win with 948 total hit points left
# MAGIC Outcome: 33 * 948 = <em>31284</em>
# MAGIC </code></pre>
# MAGIC <p>In the third example above, the Elves need <code>15</code> attack power:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #E.G#.#       #.E.#.#   E(8)
# MAGIC #.#G..#       #.#E..#   E(86)
# MAGIC #G.#.G#  --&gt;  #..#..#
# MAGIC #G..#.#       #...#.#
# MAGIC #...E.#       #.....#
# MAGIC #######       #######
# MAGIC 
# MAGIC Combat ends after 37 full rounds
# MAGIC Elves win with 94 total hit points left
# MAGIC Outcome: 37 * 94 = <em>3478</em>
# MAGIC </code></pre>
# MAGIC <p>In the fourth example above, the Elves need <code>12</code> attack power:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #.E...#       #...E.#   E(14)
# MAGIC #.#..G#       #.#..E#   E(152)
# MAGIC #.###.#  --&gt;  #.###.#
# MAGIC #E#G#G#       #.#.#.#
# MAGIC #...#G#       #...#.#
# MAGIC #######       #######
# MAGIC 
# MAGIC Combat ends after 39 full rounds
# MAGIC Elves win with 166 total hit points left
# MAGIC Outcome: 39 * 166 = <em>6474</em>
# MAGIC </code></pre>
# MAGIC <p>In the last example above, the lone Elf needs <code>34</code> attack power:</p>
# MAGIC <pre><code>#########       #########   
# MAGIC #G......#       #.......#   
# MAGIC #.E.#...#       #.E.#...#   E(38)
# MAGIC #..##..G#       #..##...#   
# MAGIC #...##..#  --&gt;  #...##..#   
# MAGIC #...#...#       #...#...#   
# MAGIC #.G...G.#       #.......#   
# MAGIC #.....G.#       #.......#   
# MAGIC #########       #########   
# MAGIC 
# MAGIC Combat ends after 30 full rounds
# MAGIC Elves win with 38 total hit points left
# MAGIC Outcome: 30 * 38 = <em>1140</em>
# MAGIC </code></pre>
# MAGIC <p>After increasing the Elves' attack power until it is just barely enough for them to win without any Elves dying, <em>what is the outcome</em> of the combat described in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

step <- function(state) {
  units <- which_df(state$m %in% c("G", "E"), state$m)
  #print("units:") # FIXME: Remove
  #print(units) # FIXME: Remove

  for (i in seq_len(nrow(units))) {
    cur_pos <- slice(units, i)
    if (state$hp[cur_pos$row, cur_pos$col] <= 0) next
    
    enemy_type <- ifelse(state$m[cur_pos$row, cur_pos$col] == "G", "E", "G")
    
    # Identify targets
    targets <- which_df(state$m == enemy_type, state$m)
    
    # If there are no more targets, the game is over
    if (nrow(targets) < 1) return(state)
    
    # Identify adjacent squares to targets not occupied
    target_squares <- get_adjacent_squares(targets, state$m, ".")
    
    # If not in range, then move
    if (nrow(get_adjacent_squares(cur_pos, state$m, enemy_type)) == 0) {
      #message(glue::glue("Unit ({cur_pos[1]}, {cur_pos[2]}) moving.")) # FIXME: REMOVE
      new_pos <- move(state, cur_pos, target_squares)
  
      if (!(new_pos$row == cur_pos$row && new_pos$col == cur_pos$col)) {
        state$m[new_pos$row, new_pos$col] <- state$m[cur_pos$row, cur_pos$col]
        state$m[cur_pos$row, cur_pos$col] <- "."

        state$hp[new_pos$row, new_pos$col] <- state$hp[cur_pos$row, cur_pos$col]
        state$hp[cur_pos$row, cur_pos$col] <- 0

        cur_pos <- new_pos
      }
      
    }
    
    # If in range, attack
    in_range_targets <- get_adjacent_squares(cur_pos, state$m, enemy_type)
    if (nrow(in_range_targets) >= 1) {
      target <-
        in_range_targets %>%
        mutate(
          target_hp = map2_dbl(row, col, ~state$hp[.x, .y])
        ) %>%
        arrange(target_hp, row, col)
      
      attack_row <- target$row[1]
      attack_col <- target$col[1]
      state$hp[attack_row, attack_col] <- state$hp[attack_row, attack_col] - ifelse(state$m[cur_pos$row, cur_pos$col] == "E", state$e_dmg, 3)
      if (state$hp[attack_row, attack_col] <= 0) {
        if (state$m[attack_row, attack_col] == "E") {
          state$elf_dead <- TRUE
          return(state)
        }
        state$m[attack_row, attack_col] <- "."
      }
    }
  }
  state$rounds_completed <- state$rounds_completed + 1
  state
}

# COMMAND ----------

calculate_outcome <- function(state) {
  rounds_completed <- 0
  repeat {
    state <- step(state)
    if (state$elf_dead) return(NA)
    if (state$rounds_completed == rounds_completed) break
    rounds_completed <- state$rounds_completed
  }

  rounds_completed * sum(state$hp %>% keep(~ . > 0))
}

# COMMAND ----------

start_state <- list(
  m = start_m,
  hp = hp,
  rounds_completed = 0,
  elf_dead = FALSE,
  e_dmg = 4
)

highest_dmg_lost <- 2
lowest_dmg_won <- Inf
lowest_dmg_won_outcome <- NA

repeat {
  state <- start_state
  state$e_dmg <- min(
    (highest_dmg_lost + lowest_dmg_won) %/% 2,
    highest_dmg_lost * 2
  )
  
  if (state$e_dmg == highest_dmg_lost || state$e_dmg == lowest_dmg_won) break
  
  outcome <- calculate_outcome(state)
  
  if (!is.na(outcome)) {
    lowest_dmg_won_outcome <- outcome
    lowest_dmg_won <- state$e_dmg
  } else {
    highest_dmg_lost <- state$e_dmg
  }
}

answer <- lowest_dmg_won_outcome
answer # 2.23 hrs

# COMMAND ----------

# 83435 too low. I think it's not guaranteed to find lowest damage

# COMMAND ----------

lst(highest_dmg_lost, lowest_dmg_won, lowest_dmg_won_outcome)

# COMMAND ----------

start_state <- list(
  m = start_m,
  hp = hp,
  rounds_completed = 0,
  elf_dead = FALSE,
  e_dmg = 4
)

highest_dmg_lost <- 4
lowest_dmg_won_outcome <- NA

repeat {
  state <- start_state
  state$e_dmg <- highest_dmg_lost
  
  outcome <- calculate_outcome(state)
  
  if (!is.na(outcome)) {
    lowest_dmg_won_outcome <- outcome
    break
  }
  highest_dmg_lost <- highest_dmg_lost + 1
}

answer <- lowest_dmg_won_outcome
answer
