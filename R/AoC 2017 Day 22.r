# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 22: Sporifica Virus ---</h2><p>Diagnostics indicate that the local <em>grid computing cluster</em> has been contaminated with the <em>Sporifica Virus</em>. The grid computing cluster is a seemingly-<span title="The infinite is possible at AdventOfCodeCom.">infinite</span> two-dimensional grid of compute nodes.  Each node is either <em>clean</em> or <em>infected</em> by the virus.</p><p>
# MAGIC </p><p>To <a href="https://en.wikipedia.org/wiki/Morris_worm#The_mistake">prevent overloading</a> the nodes (which would render them useless to the virus) or detection by system administrators, exactly one <em>virus carrier</em> moves through the network, infecting or cleaning nodes as it moves. The virus carrier is always located on a single node in the network (the <em>current node</em>) and keeps track of the <em>direction</em> it is facing.</p>
# MAGIC <p>To avoid detection, the virus carrier works in bursts; in each burst, it <em>wakes up</em>, does some <em>work</em>, and goes back to <em>sleep</em>. The following steps are all executed <em>in order</em> one time each burst:</p>
# MAGIC <ul>
# MAGIC <li>If the <em>current node</em> is <em>infected</em>, it turns to its <em>right</em>.  Otherwise, it turns to its <em>left</em>. (Turning is done in-place; the <em>current node</em> does not change.)</li>
# MAGIC <li>If the <em>current node</em> is <em>clean</em>, it becomes <em>infected</em>.  Otherwise, it becomes <em>cleaned</em>. (This is done <em>after</em> the node is considered for the purposes of changing direction.)</li>
# MAGIC <li>The virus carrier <a href="https://www.youtube.com/watch?v=2vj37yeQQHg">moves</a> <em>forward</em> one node in the direction it is facing.</li>
# MAGIC </ul>
# MAGIC <p>Diagnostics have also provided a <em>map of the node infection status</em> (your puzzle input).  <em>Clean</em> nodes are shown as <code>.</code>; <em>infected</em> nodes are shown as <code>#</code>.  This map only shows the center of the grid; there are many more nodes beyond those shown, but none of them are currently infected.</p>
# MAGIC <p>The virus carrier begins in the middle of the map facing <em>up</em>.</p>
# MAGIC <p>For example, suppose you are given a map like this:</p>
# MAGIC <pre><code>..#
# MAGIC #..
# MAGIC ...
# MAGIC </code></pre>
# MAGIC <p>Then, the middle of the infinite grid looks like this, with the virus carrier's position marked with <code>[ ]</code>:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . . #[.]. . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on a <em>clean</em> node, so it turns <em>left</em>, <em>infects</em> the node, and moves left:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . .[#]# . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on an <em>infected</em> node, so it turns <em>right</em>, <em>cleans</em> the node, and moves up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . .[.]. # . . .
# MAGIC . . . . # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Four times in a row, the virus carrier finds a <em>clean</em>, <em>infects</em> it, turns <em>left</em>, and moves forward, ending in the same place and still facing up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . #[#]. # . . .
# MAGIC . . # # # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Now on the same node as before, it sees an infection, which causes it to turn <em>right</em>, <em>clean</em> the node, and move forward:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . # .[.]# . . .
# MAGIC . . # # # . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>After the above actions, a total of <code>7</code> bursts of activity had taken place. Of them, <code>5</code> bursts of activity caused an infection.</p>
# MAGIC <p>After a total of <code>70</code>, the grid looks like this, with the virus carrier facing up:</p>
# MAGIC <pre><code>. . . . . # # . .
# MAGIC . . . . # . . # .
# MAGIC . . . # . . . . #
# MAGIC . . # . #[.]. . #
# MAGIC . . # . # . . # .
# MAGIC . . . . . # # . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>By this time, <code>41</code> bursts of activity caused an infection (though most of those nodes have since been cleaned).</p>
# MAGIC <p>After a total of <code>10000</code> bursts of activity, <code>5587</code> bursts will have caused an infection.</p>
# MAGIC <p>Given your actual map, after <code>10000</code> bursts of activity, <em>how many bursts cause a node to become infected</em>? (Do not count nodes that begin infected.)</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- ".....###..#....#.#..##...
......##.##...........##.
.#..#..#.#.##.##.........
...#..###..##.#.###.#.#.#
##....#.##.#..####.####..
#..##...#.##.##.....##..#
.#.#......#...####...#.##
###....#######...#####.#.
##..#.####...#.#.##......
##.....###....#.#..#.##.#
.#..##.....#########.##..
##...##.###..#.#..#.#...#
...####..#...#.##.#..####
.#..##......#####..#.###.
...#.#.#..##...#####.....
#..###.###.#.....#.#.###.
##.##.#.#.##.#..#..######
####.##..#.###.#...#..###
.........#####.##.###..##
..#.##.#..#..#...##..#...
###.###.#.#..##...###....
##..#.#.#.#.#.#.#...###..
#..#.#.....#..#..#..##...
........#######.#...#.#..
..##.###.#.##.#.#.###..##
"

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
df

# COMMAND ----------

turn_right <- function(direction) {
  case_when(
    direction == "up" ~ "right",
    direction == "right" ~ "down",
    direction == "down" ~ "left",
    direction == "left" ~ "up"
  )
}

turn_left <- function(direction) {
  case_when(
    direction == "up" ~ "left",
    direction == "right" ~ "up",
    direction == "down" ~ "right",
    direction == "left" ~ "down"
  )
}

is_infected <- function(state, pos) {
  matched <-
    state %>%
    filter(row == pos[1], col == pos[2])
  nrow(matched) > 0
}

move_forward <- function(pos, direction) {
  case_when(
    direction == "up" ~ c(pos[1] - 1, pos[2]),
    direction == "right" ~ c(pos[1], pos[2] + 1),
    direction == "down" ~ c(pos[1] + 1, pos[2]),
    direction == "left" ~ c(pos[1], pos[2] - 1)
  )
}

count_infections_caused <- function(df, iterations) {
  infections_caused <- 0
  pos <- c(nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1)
  direction <- "up"
  
  state <- which(df == "#", arr = TRUE) %>% as_tibble()
  
  for (i in seq_len(iterations)) {
    if (is_infected(state, pos)) {
      direction <- turn_right(direction)
      state <- state %>% filter(!(row == pos[1] & col == pos[2]))
    } else {
      direction <- turn_left(direction)
      state <- state %>% add_row(row = pos[1], col = pos[2])
      infections_caused <- infections_caused + 1
    }
    pos <- move_forward(pos, direction)
  } 
  infections_caused
}

# COMMAND ----------

answer <- count_infections_caused(df, 10000)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you go to remove the virus from the infected nodes, it <em>evolves</em> to resist your attempt.</p>
# MAGIC <p>Now, before it infects a clean node, it will <em>weaken</em> it to disable your defenses. If it encounters an infected node, it will instead <em>flag</em> the node to be cleaned in the future.  So:</p>
# MAGIC <ul>
# MAGIC <li><em>Clean</em> nodes become <em>weakened</em>.</li>
# MAGIC <li><em>Weakened</em> nodes become <em>infected</em>.</li>
# MAGIC <li><em>Infected</em> nodes become <em>flagged</em>.</li>
# MAGIC <li><em>Flagged</em> nodes become <em>clean</em>.</li>
# MAGIC </ul>
# MAGIC <p>Every node is always in exactly one of the above states.</p>
# MAGIC <p>The virus carrier still functions in a similar way, but now uses the following logic during its bursts of action:</p>
# MAGIC <ul>
# MAGIC <li>Decide which way to turn based on the <em>current node</em>:
# MAGIC   <ul>
# MAGIC   <li>If it is <em>clean</em>, it turns <em>left</em>.</li>
# MAGIC   <li>If it is <em>weakened</em>, it does <em>not</em> turn, and will continue moving in the same direction.</li>
# MAGIC   <li>If it is <em>infected</em>, it turns <em>right</em>.</li>
# MAGIC   <li>If it is <em>flagged</em>, it <em>reverses</em> direction, and will go back the way it came.</li>
# MAGIC   </ul>
# MAGIC </li>
# MAGIC <li>Modify the state of the <em>current node</em>, as described above.</li>
# MAGIC <li>The virus carrier moves <em>forward</em> one node in the direction it is facing.</li>
# MAGIC </ul>
# MAGIC <p>Start with the same map (still using <code>.</code> for <em>clean</em> and <code>#</code> for infected) and still with the virus carrier starting in the middle and facing <em>up</em>.</p>
# MAGIC <p>Using the same initial state as the previous example, and drawing <em>weakened</em> as <code>W</code> and <em>flagged</em> as <code>F</code>, the middle of the infinite grid looks like this, with the virus carrier's position again marked with <code>[ ]</code>:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . . #[.]. . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>This is the same as before, since no initial nodes are <em>weakened</em> or <em>flagged</em>.  The virus carrier is on a clean node, so it still turns left, instead <em>weakens</em> the node, and moves left:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . # . . .
# MAGIC . . .[#]W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The virus carrier is on an infected node, so it still turns right, instead <em>flags</em> the node, and moves up:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . .[.]. # . . .
# MAGIC . . . F W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>This process repeats three more times, ending on the previously-flagged node and facing right:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC . . W[F]W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Finding a flagged node, it reverses direction and <em>cleans</em> the node:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC . .[W]. W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>The <em>weakened</em> node becomes infected, and it continues in the same direction:</p>
# MAGIC <pre><code>. . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . W W . # . . .
# MAGIC .[.]# . W . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC . . . . . . . . .
# MAGIC </code></pre>
# MAGIC <p>Of the first <code>100</code> bursts, <code>26</code> will result in <em>infection</em>. Unfortunately, another feature of this evolved virus is <em>speed</em>; of the first <code>10000000</code> bursts, <code>2511944</code> will result in <em>infection</em>.</p>
# MAGIC <p>Given your actual map, after <code>10000000</code> bursts of activity, <em>how many bursts cause a node to become infected</em>? (Do not count nodes that begin infected.)</p>
# MAGIC </article>

# COMMAND ----------

# This was too slow

# turn_around <- function(direction) {
#   case_when(
#     direction == "up" ~ "down",
#     direction == "right" ~ "left",
#     direction == "down" ~ "up",
#     direction == "left" ~ "right"
#   )
# }

# get_status <- function(state, pos) {
#   status <-
#     state %>%
#     filter(row == pos[1], col == pos[2]) %>%
#     pull(status)
  
#   c(status, "clean")[1]
# }

# set_status <- function(state, pos, new_status) {
#   i <- which(state$row == pos[1] & state$col == pos[2])
  
#   if (length(i) == 0) {
#     state <- state %>% add_row(row = pos[1], col = pos[2], status = new_status)
#   } else {
#     state$status[i] <- new_status
#   }
  
#   state
# }

# count_infections_caused <- function(df, iterations) {
#   infections_caused <- 0
#   pos <- c(nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1)
#   direction <- "up"
  
#   state <-
#     which(df == "#", arr = TRUE) %>%
#     as_tibble() %>%
#     add_column(status = "infected")
  
#   for (i in seq_len(iterations)) {
#     node_status <- get_status(state, pos)
    
#     if (node_status == "clean") {
#       direction <- turn_left(direction)
#       state <- set_status(state, pos, "weakened")
#     } else if (node_status == "weakened") {
#       state <- set_status(state, pos, "infected")
#       infections_caused <- infections_caused + 1
#     } else if (node_status == "infected") {
#       direction <- turn_right(direction)
#       state <- set_status(state, pos, "flagged")
#     } else if (node_status == "flagged") {
#       direction <- turn_around(direction)
#       state <- set_status(state, pos, "clean")
#     }
    
#     pos <- move_forward(pos, direction)
#   } 
#   infections_caused
# }

# answer <- count_infections_caused(df, 10000000)
# answer

# COMMAND ----------

Rcpp::cppFunction('
int count_infections_caused_cpp(std::vector<int> infected_rows, std::vector<int> infected_cols, int start_row, int start_col, int iterations) {
  const int CLEAN = 0, WEAKENED = 1, INFECTED = 2, FLAGGED = 3;

  std::map<std::pair<int, int>, int> state;
  for (int i = 0; i < infected_rows.size(); ++i) {
    state[std::make_pair(infected_rows[i], infected_cols[i])] = INFECTED;
  }

  int infections_caused = 0;
  auto pos = std::make_pair(start_row, start_col);
  int row_change = -1 ;
  int col_change = 0;
  for (int i = 0; i < iterations; ++i) {
    switch (state[pos]) {
      case CLEAN:
        // Turn left
        if      (row_change == -1) {row_change =  0; col_change = -1;} // up -> left
        else if (col_change ==  1) {row_change = -1; col_change =  0;} // right -> up
        else if (row_change ==  1) {row_change =  0; col_change =  1;} // down -> right
        else if (col_change == -1) {row_change =  1; col_change =  0;} // left -> down
        break;
      case WEAKENED:
        // No turn
        ++infections_caused;
        break;
      case INFECTED:
        // Turn right
        if      (row_change == -1) {row_change =  0; col_change =  1;} // up -> right
        else if (col_change ==  1) {row_change =  1; col_change =  0;} // right -> down
        else if (row_change ==  1) {row_change =  0; col_change = -1;} // down -> left
        else if (col_change == -1) {row_change = -1; col_change =  0;} // left -> up
        break;
      case FLAGGED:
        // Reverse
        if      (row_change == -1) {row_change =  1; col_change =  0;} // up -> down
        else if (col_change ==  1) {row_change =  0; col_change = -1;} // right -> left
        else if (row_change ==  1) {row_change = -1; col_change =  0;} // down -> up
        else if (col_change == -1) {row_change =  0; col_change =  1;} // left -> right
        break;
    }
    state[pos] = (state[pos] + 1) % 4;
    pos.first += row_change;
    pos.second += col_change;
  }

  return infections_caused;
}
')

# COMMAND ----------

infections <- which(df == "#", arr = TRUE) %>% as_tibble()

answer <- count_infections_caused_cpp(infections$row, infections$col, nrow(df) %/% 2 + 1, ncol(df) %/% 2 + 1, 10000000)
answer
