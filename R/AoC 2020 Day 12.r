# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/12

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 12: Rain Risk ---</h2><p>Your ferry made decent progress toward the island, but the storm came in <span title="At least it wasn't a Category Six!">faster than anyone expected</span>. The ferry needs to take <em>evasive actions</em>!</p>
# MAGIC <p>Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the <a href="https://en.wikipedia.org/wiki/Public_address_system" target="_blank">PA system</a> to ask if anyone can help, you quickly volunteer.</p>
# MAGIC <p>The navigation instructions (your puzzle input) consists of a sequence of single-character <em>actions</em> paired with integer input <em>values</em>. After staring at them for a few minutes, you work out what they probably mean:</p>
# MAGIC <ul>
# MAGIC <li>Action <em><code>N</code></em> means to move <em>north</em> by the given value.</li>
# MAGIC <li>Action <em><code>S</code></em> means to move <em>south</em> by the given value.</li>
# MAGIC <li>Action <em><code>E</code></em> means to move <em>east</em> by the given value.</li>
# MAGIC <li>Action <em><code>W</code></em> means to move <em>west</em> by the given value.</li>
# MAGIC <li>Action <em><code>L</code></em> means to turn <em>left</em> the given number of degrees.</li>
# MAGIC <li>Action <em><code>R</code></em> means to turn <em>right</em> the given number of degrees.</li>
# MAGIC <li>Action <em><code>F</code></em> means to move <em>forward</em> by the given value in the direction the ship is currently facing.</li>
# MAGIC </ul>
# MAGIC <p>The ship starts by facing <em>east</em>. Only the <code>L</code> and <code>R</code> actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is <code>N10</code>, the ship would move north 10 units, but would still move east if the following action were <code>F</code>.)</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>F10
# MAGIC N3
# MAGIC F7
# MAGIC R90
# MAGIC F11
# MAGIC </code></pre>
# MAGIC <p>These instructions would be handled as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>F10</code> would move the ship 10 units east (because the ship starts by facing east) to <em>east 10, north 0</em>.</li>
# MAGIC <li><code>N3</code> would move the ship 3 units north to <em>east 10, north 3</em>.</li>
# MAGIC <li><code>F7</code> would move the ship another 7 units east (because the ship is still facing east) to <em>east 17, north 3</em>.</li>
# MAGIC <li><code>R90</code> would cause the ship to turn right by 90 degrees and face <em>south</em>; it remains at <em>east 17, north 3</em>.</li>
# MAGIC <li><code>F11</code> would move the ship 11 units south to <em>east 17, south 8</em>.</li>
# MAGIC </ul>
# MAGIC <p>At the end of these instructions, the ship's <a href="https://en.wikipedia.org/wiki/Manhattan_distance" target="_blank">Manhattan distance</a> (sum of the absolute values of its east/west position and its north/south position) from its starting position is <code>17 + 8</code> = <em><code>25</code></em>.</p>
# MAGIC <p>Figure out where the navigation instructions lead. <em>What is the Manhattan distance between that location and the ship's starting position?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "L90
N5
L180
L180
S4
F21
W4
S1
R270
F18
S4
F44
R90
N5
F18
E5
R270
F1
L90
W5
N4
W5
F37
R90
S1
W2
S1
L90
W5
R90
N1
W2
L180
L90
E3
N1
L90
F30
E4
N2
E2
F76
R90
W4
S3
R90
F2
L90
S3
R180
N5
E4
L90
W4
F1
N2
E1
F8
R90
F88
R180
F60
W2
R90
E3
N3
W5
F56
S1
E5
F5
L90
E4
N3
R90
E2
F34
W4
L90
F100
W4
L90
F40
L90
F51
E5
F52
N1
F45
W2
N2
F56
N2
W3
R180
F14
N3
L90
N2
F18
L180
E1
R90
N2
E3
L180
S5
F87
L90
F32
E1
F92
N1
W3
F89
E2
N1
R90
W1
F9
E1
F74
S1
L270
S1
F99
L90
W1
R90
F78
L90
W4
S2
R180
E3
S4
L90
F78
E5
L90
S5
W2
R90
N1
E5
F33
W1
R180
S1
W4
N1
F69
S5
R90
N5
F89
L90
W1
F91
L90
F19
E5
L90
F53
L90
S5
L90
S4
W1
S2
L180
F3
N5
N5
F78
E3
S1
L180
F79
L90
W4
R180
W3
N4
W5
F84
S4
L180
S1
S3
E2
S4
R90
N1
E5
S4
W4
R90
F44
R90
E5
S5
W1
N4
F37
N2
F41
R90
F58
L90
F5
R90
W4
L90
F45
N4
F48
S1
E2
S1
R90
F30
W2
L90
F53
L90
W5
R90
N2
E1
S3
F29
N5
L270
S2
F87
S4
F86
S4
R90
W5
F59
N2
F35
L90
W5
N3
E3
L90
S2
E2
N2
L90
R90
N5
L270
N5
R90
N4
E2
S3
W2
F55
E4
S1
L90
W3
S4
F95
W5
E2
R90
S3
F54
L90
N5
F69
R90
N1
W3
N4
F49
N4
E5
S2
W5
S5
R90
N1
F76
S5
E4
S5
L90
N2
R90
F68
L90
S1
R90
F67
L90
N3
E1
F51
S1
F94
S3
E5
N3
F76
R180
F53
R90
R90
F96
L270
N1
R90
E3
L90
F57
S5
F39
N2
F95
R270
W1
S4
N5
N4
F5
L90
F83
L180
E4
F82
N5
R90
F52
L90
F13
N5
R90
L90
F10
N5
F80
E4
L180
N1
R90
E1
R180
E5
F25
S3
L180
F29
N1
W1
F20
W1
R180
F56
E5
S2
L90
F67
N4
W3
E2
R180
E1
F16
F59
R180
E5
F21
E2
R90
N4
E5
S5
E3
L90
W1
L90
E2
S3
R90
F59
W4
F44
S2
W1
S1
N5
W1
S3
E1
N3
R90
E2
F39
R90
F2
E1
N5
W5
F24
E3
L90
S3
E2
F57
E2
R90
F12
R90
N2
W3
L180
N4
F78
R180
N4
F92
L90
L180
N2
W4
R90
F7
S4
E3
S4
E1
S4
L180
S2
F81
E5
L90
F3
N4
F39
S2
W4
F28
R90
F75
W1
S3
W5
S1
F67
E3
F62
R90
N3
R180
W2
F67
S2
W1
L90
L90
S2
E3
R90
N5
S4
F14
R180
N2
R90
W3
L180
F37
W1
S4
E1
F45
W4
S5
L180
S2
W1
L90
N4
R90
F44
S1
E3
S4
W5
N4
W4
R270
S1
W3
L90
R90
F95
N1
R90
S1
F48
L90
F53
E2
R180
N5
F46
W5
F98
S3
F81
N5
F98
N4
F67
S1
E1
F10
R90
F66
W3
N1
L180
N1
F27
F54
W2
F3
R90
F68
E2
E4
F30
L90
F62
S2
L90
F99
R90
F48
E4
S4
F96
W4
N5
W5
F44
F90
N1
L90
F68
N4
W1
F83
S5
E1
N3
R90
W4
N5
F59
R90
L180
W2
F14
L90
N1
F58
R90
E2
L90
S5
F30
R90
F17
W1
F29
E3
R90
S3
R90
W1
N2
S3
W2
S2
R90
W2
N2
L90
W1
F55
S3
W4
R180
N3
W1
L90
F59
E5
L90
L180
F70
W1
F41
L180
S5
F22
S5
L270
F11
R90
S3
W2
N4
R90
W5
R180
F17
R90
F99
L180
F26
R90
W5
R180
S5
F28
N5
W1
N5
F100
S4
E2
L270
N4
F100
S1
R180
F81
S5
W5
L180
F1
R90
W5
L90
R90
N4
F69
W5
L180
F68
S5
F21
E4
L180
W3
S3
R90
E3
R90
E2
R90
F19
N3
R90
F81
S1
R90
F1
N1
L90
R90
W1
S4
F93
W5
F31
W1
N1
W1
F59
L180
W5
S4
L90
S1
R270
N1
R90
S3
R90
W2
R90
W2
R180
F83
S3
R90
F99
R90
F25
S2
F81
F33
F55
R90
F40
N5
L90
N5
E5
F56
L180
S2
F52
E4
F99
S2
E1
L180
F47
S3
W4
W3
L90
N1
F26
R90
W5
R90
W5
L90
E2
N1
F35
L90
S3
F20
W5
F29
L90
S2
W4
L180
N5
F27
L90
F80
S1
L90
R180
F37
"

# COMMAND ----------

directions <-
  read_lines(input) %>%
  as_tibble() %>%
  extract(value, c("action", "value"), "(.)(\\d+)") %>%
  mutate(value = as.numeric(value))
directions

# COMMAND ----------

result <- 
  directions %>%
  mutate(
    facing = cumsum(case_when(
      action == "L" ~ value,
      action == "R" ~ -value,
      TRUE ~ 0
    )),
    delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      action == "F" ~ value * sin(facing / 180 * pi),
      TRUE ~ 0
    ),
    delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      action == "F" ~ value * cos(facing / 180 * pi),
      TRUE ~ 0
    )
  )
result

# COMMAND ----------

answer <- abs(sum(result$delta_north)) + abs(sum(result$delta_east))
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.</p>
# MAGIC <p>Almost all of the actions indicate how to move a <em>waypoint</em> which is relative to the ship's position:</p>
# MAGIC <ul>
# MAGIC <li>Action <em><code>N</code></em> means to move the waypoint <em>north</em> by the given value.</li>
# MAGIC <li>Action <em><code>S</code></em> means to move the waypoint <em>south</em> by the given value.</li>
# MAGIC <li>Action <em><code>E</code></em> means to move the waypoint <em>east</em> by the given value.</li>
# MAGIC <li>Action <em><code>W</code></em> means to move the waypoint <em>west</em> by the given value.</li>
# MAGIC <li>Action <em><code>L</code></em> means to rotate the waypoint around the ship <em>left</em> (<em>counter-clockwise</em>) the given number of degrees.</li>
# MAGIC <li>Action <em><code>R</code></em> means to rotate the waypoint around the ship <em>right</em> (<em>clockwise</em>) the given number of degrees.</li>
# MAGIC <li>Action <em><code>F</code></em> means to move <em>forward</em> to the waypoint a number of times equal to the given value.</li>
# MAGIC </ul>
# MAGIC <p>The waypoint starts <em>10 units east and 1 unit north</em> relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.</p>
# MAGIC <p>For example, using the same instructions as above:</p>
# MAGIC <ul>
# MAGIC <li><code>F10</code> moves the ship to the waypoint 10 times (a total of <em>100 units east and 10 units north</em>), leaving the ship at <em>east 100, north 10</em>. The waypoint stays 10 units east and 1 unit north of the ship.</li>
# MAGIC <li><code>N3</code> moves the waypoint 3 units north to <em>10 units east and 4 units north of the ship</em>. The ship remains at <em>east 100, north 10</em>.</li>
# MAGIC <li><code>F7</code> moves the ship to the waypoint 7 times (a total of <em>70 units east and 28 units north</em>), leaving the ship at <em>east 170, north 38</em>. The waypoint stays 10 units east and 4 units north of the ship.</li>
# MAGIC <li><code>R90</code> rotates the waypoint around the ship clockwise 90 degrees, moving it to <em>4 units east and 10 units south of the ship</em>. The ship remains at <em>east 170, north 38</em>.</li>
# MAGIC <li><code>F11</code> moves the ship to the waypoint 11 times (a total of <em>44 units east and 110 units south</em>), leaving the ship at <em>east 214, south 72</em>. The waypoint stays 4 units east and 10 units south of the ship.</li>
# MAGIC </ul>
# MAGIC <p>After these operations, the ship's Manhattan distance from its starting position is <code>214 + 72</code> = <em><code>286</code></em>.</p>
# MAGIC <p>Figure out where the navigation instructions actually lead. <em>What is the Manhattan distance between that location and the ship's starting position?</em></p>
# MAGIC </article>

# COMMAND ----------

wp_changes <-
  directions %>%
  mutate(
    wp_delta_north = case_when(
      action == "N" ~ value,
      action == "S" ~ -value,
      TRUE ~ 0
    ),
    wp_delta_east = case_when(
      action == "E" ~ value,
      action == "W" ~ -value,
      TRUE ~ 0
    )
  ) %>% 
  add_row(wp_delta_north = 1, wp_delta_east = 10, .before = 1)
wp_changes

# COMMAND ----------

for (i in which(wp_changes$action %in% c("L", "R"))) {
  cur_wp <- wp_changes %>% slice(1:i) %>% summarise(wp_north = sum(wp_delta_north), wp_east = sum(wp_delta_east))

  x <- cur_wp$wp_east
  y <- cur_wp$wp_north
  
  v <- paste0(wp_changes$action[i], wp_changes$value[i])
  if (v %in% c("L180", "R180")) {
    new_x <- -x
    new_y <- -y
  } else if (v %in% c("L270", "R90")) {
    new_x <- y
    new_y <- -x
  } else if (v %in% c("R270", "L90")) {
    new_x <- -y
    new_y <- x
  }
  
  wp_changes$wp_delta_north[i] <- new_y - y
  wp_changes$wp_delta_east[i] <- new_x - x
}

# COMMAND ----------

result <-
  wp_changes %>%
  mutate(
    wp_east = cumsum(wp_delta_east),
    wp_north = cumsum(wp_delta_north),
    
    ship_delta_east = case_when(
      action == "F" ~ value * wp_east,
      TRUE ~ 0
    ),
    ship_delta_north = case_when(
      action == "F" ~ value * wp_north,
      TRUE ~ 0
    ),
    
    ship_abs_east = cumsum(ship_delta_east),
    ship_abs_north = cumsum(ship_delta_north)
  )

# COMMAND ----------

answer <- result %>% tail(1) %>% with(abs(ship_abs_east) + abs(ship_abs_north))
answer
