# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/18

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 18: Many-Worlds Interpretation ---</h2><p>As you approach Neptune, a planetary security system detects you and activates a giant <a href="https://en.wikipedia.org/wiki/Tractor_beam">tractor beam</a> on <a href="https://en.wikipedia.org/wiki/Triton_(moon)">Triton</a>!  You have no choice but to land.</p>
# MAGIC <p>A scan of the local area reveals only one interesting feature: a massive underground vault.  You generate a map of the tunnels (your puzzle input).  The tunnels are too narrow to move diagonally.</p>
# MAGIC <p>Only one <em>entrance</em> (marked <code>@</code>) is present among the <em>open passages</em> (marked <code>.</code>) and <em>stone walls</em> (<code>#</code>), but you also detect an assortment of <em>keys</em> (shown as lowercase letters) and <em>doors</em> (shown as uppercase letters). Keys of a given letter open the door of the same letter: <code>a</code> opens <code>A</code>, <code>b</code> opens <code>B</code>, and so on.  You aren't sure which key you need to disable the tractor beam, so you'll need to <em>collect all of them</em>.</p>
# MAGIC <p>For example, suppose you have the following map:</p>
# MAGIC <pre><code>#########
# MAGIC #b.A.@.a#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Starting from the entrance (<code>@</code>), you can only access a large door (<code>A</code>) and a key (<code>a</code>). Moving toward the door doesn't help you, but you can move <code>2</code> steps to collect the key, unlocking <code>A</code> in the process:</p>
# MAGIC <pre><code>#########
# MAGIC #b.....@#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Then, you can move <code>6</code> steps to collect the only other key, <code>b</code>:</p>
# MAGIC <pre><code>#########
# MAGIC #@......#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>So, collecting every key took a total of <code><em>8</em></code> steps.</p>
# MAGIC <p>Here is a larger example:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.b.A.@.a.B.c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>The only reasonable move is to take key <code>a</code> and unlock door <code>A</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.b.....@.B.c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Then, do the same with key <code>b</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.@.........c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>...and the same with key <code>c</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.............@.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Now, you have a choice between keys <code>d</code> and <code>e</code>.  While key <code>e</code> is closer, collecting it now would be slower in the long run than collecting key <code>d</code> first, so that's the best choice:</p>
# MAGIC <pre><code>########################
# MAGIC #f...E.e...............#
# MAGIC ######################.#
# MAGIC #@.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Finally, collect key <code>e</code> to unlock door <code>E</code>, then collect key <code>f</code>, taking a grand total of <code><em>86</em></code> steps.</p>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <ul>
# MAGIC <li><pre><code>########################
# MAGIC #...............b.C.D.f#
# MAGIC #.######################
# MAGIC #.....@.a.B.c.d.A.e.F.g#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Shortest path is <code>132</code> steps: <code>b</code>, <code>a</code>, <code>c</code>, <code>d</code>, <code>f</code>, <code>e</code>, <code>g</code></p></li>
# MAGIC <li><pre><code>#################
# MAGIC #i.G..c...e..H.p#
# MAGIC ########.########
# MAGIC #j.A..b...f..D.o#
# MAGIC ########@########
# MAGIC #k.E..a...g..B.n#
# MAGIC ########.########
# MAGIC #l.F..d...h..C.m#
# MAGIC #################
# MAGIC </code></pre>
# MAGIC <p>Shortest paths are <code>136</code> steps;<br>one is: <code>a</code>, <code>f</code>, <code>b</code>, <code>j</code>, <code>g</code>, <code>n</code>, <code>h</code>, <code>d</code>, <code>l</code>, <code>o</code>, <code>e</code>, <code>p</code>, <code>c</code>, <code>i</code>, <code>k</code>, <code>m</code></p></li>
# MAGIC <li><pre><code>########################
# MAGIC #@..............ac.GI.b#
# MAGIC ###d#e#f################
# MAGIC ###A#B#C################
# MAGIC ###g#h#i################
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Shortest paths are <code>81</code> steps; one is: <code>a</code>, <code>c</code>, <code>f</code>, <code>i</code>, <code>d</code>, <code>g</code>, <code>b</code>, <code>e</code>, <code>h</code></p></li>
# MAGIC </ul>
# MAGIC <p><em>How many steps is the shortest path that collects all of the keys?</em></p>
# MAGIC </article>

# COMMAND ----------

install.packages("patchwork")

# COMMAND ----------

install.packages("datastructures")

# COMMAND ----------

library(patchwork)
library(tidyverse)

# COMMAND ----------

input <- "#################################################################################
#.................C...#...#.......#.....#.#.........#.R.....#.....B............t#
#.###################.#.#.###.#.###.#.#V#.#.#####.#.#.#####.#.#####.###########.#
#...Z...#.......#.....#.#...#.#...#.#.#.#.#.#.#...#.#.#...#...#...#.#.....#.#...#
#.#####.#.#####.#.#####.###.#.###.#.#.###.#.#.#.#####.#.#.#####.#.#.#.###.#.#.###
#.#.....#k..#...#...#...#.#.#...#...#...#...#.#.......#.#.....#.#n#.....#.#...#.#
#.#.#.#####.#.#####.#.#.#.#.#.#########.#.###.#########.#.#####.#.#######.#.###.#
#.#.#.#.....#.#...F.#.#.#...#.#...#...#.#.#............m#.#.....#.......#.#.#...#
#.#.###.#####.#.#######.#.#####.#.#.#.#.#.#####.#####.#####.###########.#.#.#.#.#
#.#...#.#.....#...#.....#.......#.#.#.#.#.....#.#...#.#.....#.....#.......#.#.#.#
#.###.#.#.#######.#.#############.#.#.#.#####.#.#.#.###.#####.###.#########.#.#.#
#.#...#.#.......#.#...#...#.....#.#.#.#.#...#...#.#.#...#..q..#.#.#.....#.....#.#
#.#.###.#######.#.#.#.###.#.#.###.#.#.#.#.#.#.###.#.#.###.#####.#.#.###.#######.#
#.#...........#.#.#.#...#...#...#.#.#...#.#.#.#...#...#...#.....#...#.#w..#...#i#
#.###########.#.#.#####.#.#####.#.#.###U###.#.#.#######.###.#########.###.#.#.###
#...#.#.....#.#.#.......#.#...#.#.#...#.#...#.#.....#...#.........#.....#...#...#
###.#.#.###.#.#.#########.###.#.#.#.#.#.#.###.#####.#.#.#####.#.###.#.#########.#
#.#.#.#.#.#.#.#.#.......#.....#.#.#.#.#.#...#.#...#.#.#.#...#.#.#...#s......#...#
#.#.#.#.#.#.###.#####.#.#####.#.#.###.#.#.#.#.#.###.#.###.#.#.#.#.#######.###.###
#.....#.#.......#...#.#...#...#...#...#.#.#...#...#.#.....#.#.#...#..x..#....d#.#
#######.#########.#.#####.#.#######.###.#.#######.#.#######J###.###.###.#######.#
#.....#...#...#.S.#.#j..#...........#.#.#.#.......#.#.....#...#...#.#.#.#.#.....#
#.###.###.#.#.#.###.###.#############.#.#.#.#####.#.#.#.#########.#.#.#.#.#.#.#.#
#.#.....#.#.#.....#...#.......#.........#...#.....#...#.........#...#...#.#.#.#.#
#.#####.#.#.#######.#.#######.###.###########.###########.#.#########.###.#.#.###
#.#.E.#.#.#.#...#...#...#...#...#.....#.#.....#...........#.#.....#...#..e..#...#
#.#.#.#.#H#X#.#.#.#.#####W#.###Q#####.#.#.#####.###.#########.###.#.###########.#
#...#.#...#.#.#.#.#.#...#.#...#.#...#.#.#...#.#...#.#...#...#.#.#.#.............#
#####.#####.#.#.#.###.#.#.###.#.#.###.#.###.#.###.#.#.#.#.#.#.#.#.#############.#
#...#.#.....#.#.#...D.#...#.#.#.#.....#.#...#...#.#.#.#...#...#.#.#...........#.#
###.#.#.#####.#############.#.#.#.#####.#.#####.#.###.#########.#.#.###.#.#####.#
#...#...#..........o........#...#......g#.....#.#.....#...#.#...#.#.#.K.#.#....h#
#.#.#####.###########.#################.#####.#.#######.#.#.#.#.#.#.#.#####.#####
#.#.....#.#.....#...#.........#.......#.#.#...#.....#...#.#...#.#...#...#...#...#
#.#######.###.#.#.#.#######.#.#######.#.#.#.###.###.#.###.#####.#######.#.#####.#
#.#.....#...#.#...#...#...#.#.........#.#.#...#...#.#.#...........#.....#.....#.#
#.#.###.###.#.#######.#.###.#####.#####.#.###.#.#.#.#.###########.#.#########.#.#
#.#.#.#...#...#.#.....#...#.....#.#.....#.#...#.#.#.#...#.........#.#.........#.#
#.#.#.###.#####.#.#######.#####.###.#####.#.#####.#.###.#.#########.#.#########.#
#.......#.....................#...................#.....#.........#.............#
#######################################.@.#######################################
#.......#...........#.....#.....................#.....#.......#...........#.....#
#.#######.#.#######.#.###.#.#####.#####.#.#.#####.#.#.#######.#.#########.#####.#
#.#.......#.....#...#...#.#.#...#.....#.#.#.......#.#.........#.#.......#...#...#
#.#.###########.#.#####.###.#.#.#####.#.#.#####.###.###########.#.###.#.###.#.###
#b..#...........#.....#...#.#.#.#.#...#.#.#...#...#...#.........#.#...#.#...#...#
#.###.###############.###.#.#.#.#.#.###.###.#.#######.#.#########.#.#.###.#####.#
#...#...........#...#.#...#.#.#...#.#...#...#.......#.#.#.......#.#.#.#...#.....#
###.###########.###.#.#.#.#.#.###.#.###.#.#########.#.#.#.#####.###.#.#.###.###.#
#.............#...#.....#.#...#...#...#.#.#.#.....#.#.#.#.#...#.....#.#....l#...#
#.#########.#####.#####.#######.#####G#.#.#.#.#O###.#.#.#.#.#.#.#####.#######.###
#.#...#...#.#...#...#...#.....#...#...#.#.#.#.#...#...#.#.#.#.#.#.Y.#.......#.#.#
#.#.#.#.#.###.#.#.#.###.#.###.###.#.###.#.#.#.###.#.###.#.#.#.###.#.#######.#.#.#
#.#.#a..#.....#.#.#...#.#.#.#.....#.#.#.#.#.#...#...#...#.#.#.....#.....#...#.#.#
###.###########.#####.###.#.#####.#.#.#.#.#.###.#####.###.#.###########.#.###.#.#
#...#..y#.....#.#...#.......#...#.#.#...#.#.........#.#.......#.#.......#.#...#.#
#.###.#.#.#.#.#.#.#.#.#######.#.#.#.###.#.#.#########.#######.#.#.#######.#.###.#
#.....#.#.#.#.#...#.#.#.......#.#.#...#.#.#.#.......#.....#z#.#.#.#.....#.#p..#.#
#######.###.#######.#.#.#######.#####.###.###.#####.#####.#.#.#.#A#.###.#.###.#.#
#.....#.....#.....#.#.#.....#.......#...#...#...#.....#...#.....#.#...#.....#.#.#
#.###.#####.#.###.#.#######.#######.###.#.#.#.###.###.#.#######.#.#.#########.#.#
#...#.......#.#.#...#.....#...#...#...#.#.#...#...#...#.......#.#.#.#.........#.#
###.#########.#.#.#######.#.#.###.###.#.#.#####.###.###########.#.###.#########.#
#...#...#...P.#...#.......#.#...#.#...#.#.#.....#...#.......#.#.#.....#...#.....#
#.###.###.###.#####.#########.#.#.#.###.#.#.#######.#.#####.#.#.#######.#.#####.#
#.....#...#...#.....#.......#.#.#...#...#.#.......#...#...#...#.#.......#.......#
#####.#.###.###.#####.#####.###.###.#.#.#.#######.#####.#.###.#.###.###.#########
#...#c#...#.#...#.....#...#...#...#.#.#u#.#.....#.....#.#.....#...#...#.#.......#
###.#.###.###.###.#####.#####.###.#.#.#.#.#.###.#####.#.#########.###.#.#.#####.#
#...#...#.L.#.#.#...#.......#.#...#...#.#.#.#.#.#...#.#.....#...#.#...#.......#.#
#.#####.###.#.#.#.#.#.#####.#.#.#######.#.#.#.#.###.#.#####.#.#.#.#.#####.#####.#
#...#...#.#...#...#.#.....#.#.#.#.....#.#.#.#.#.....#...#...#.#...#.#...#.#...#.#
###.#.###.#########.###.###.#.#.#####.#.#.#.#.#####.###.#.###.#######.#.###.#.#.#
#...#...#.........#...#.#...#...#.....#.#...#.#...#.#.#.#.#...#.....#.#...N.#.#.#
#.#####.#.#####.#.###.#.#.#######.#####.#####.#.#.#.#.#.###.###.###.#.#######.#T#
#.I.#...#.#.....#.....#.#...#...#.......#.#.....#.#.#.#...#.#.....#...#...#...#.#
#.#.#.###.#.###############.#.#.#.#######.#.#####.#.#.###.#.#####.#####.#.#.###.#
#.#...#...#.#.....#.........#.#.#...#...#...#...#.#.#...#.#f......#.#...#.#.....#
#.#########.#.#####.###.#####.#.###.#.#.#.###.#.#.#.###.#.#########.#.#.#######.#
#...........#..r....M.#.......#v......#.#.....#.#.......#.............#.........#
#################################################################################
"

# COMMAND ----------

# input <- "#########
# #b.A.@.a#
# #########
# "

# COMMAND ----------

# input <- "###############
# #d.ABC.#.....a#
# ######@#@######
# ###############
# ######@#@######
# #b.....#.....c#
# ###############
# "

# COMMAND ----------

m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

# COMMAND ----------

hashmap <- function(default = NULL) {
  h <- structure(new.env(hash = TRUE), class = "hashmap")
  attr(h, "default") <- default
  h
}

hash_fn <- function(x) paste(x, collapse = ",")

`[.hashmap` <- function(h, i) {
  result <- h[[hash_fn(i)]]
  if (is.null(result)) result <- attr(h, "default")
  result
}

`[<-.hashmap` <- function(h, i, j, value) {
  h[[hash_fn(i)]] <- value
  h
}

as.list.hashmap <- function(h) {
  attr(h, "class") <- NULL
  as.list(h)
}

to_hashmap <- function(inds, default = "#") {
  result <- hashmap(default = default)
  for (i in seq_len(nrow(inds))) {
    # cur_row <- inds %>% slice(i)
    # result[c(cur_row$row, cur_row$col)] <- cur_row
    result[c(inds$row[i], inds$col[i])] <- inds$value[i]
  }
  result
}

# COMMAND ----------

coords <-
  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m))
coords

# COMMAND ----------

sort_string <- function(s) {
  s %>%
    str_split("") %>%
    unlist() %>%
    str_sort() %>%
    str_c(collapse = "")
}

solve <- function(coords) {
  target <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% unlist() %>% str_sort() %>% str_c(collapse = "")
  visited <- hashmap(default = FALSE)
  states <- datastructures::fibonacci_heap("numeric")
  
  datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(keys = "", d = 0))
  
  coords <- to_hashmap(coords)
  

  repeat {
    state <- datastructures::pop(states)[[1]]
    
    if (visited[c(state$row, state$col, state$keys)]) next
    visited[c(state$row, state$col, state$keys)] <- TRUE

    # Key
    if (state$value %in% letters) {
      if (!str_detect(state$keys, state$value)) state$keys <- sort_string(str_c(state$keys, state$value))
      if (state$keys == target) return(state$d)
    }

    # Lock
    if (state$value %in% LETTERS) {
      if (!str_detect(str_to_upper(state$keys), state$value)) next
    }
    
    for (direction in c("N", "E", "S", "W")) {
      new_state <- tibble(
        row = state$row + (direction == "S") - (direction == "N"),
        col = state$col + (direction == "E") - (direction == "W"),
        value = coords[c(row, col)],
        keys = state$keys,
        d = state$d + 1
      )
      
      if (new_state$value != "#") {
        datastructures::insert(states, new_state$d, new_state)
      }
    }
  }
}

# COMMAND ----------

answer <- solve(coords)
answer # 3hrs

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You arrive at the vault only to <span title="To see the inspiration for this puzzle, look up 'Link to the Past Randomizer Multiworld'.">discover</span> that there is not one vault, but <em>four</em> - each with its own entrance.</p>
# MAGIC <p>On your map, find the area in the middle that looks like this:</p>
# MAGIC <pre><code>...
# MAGIC .@.
# MAGIC ...
# MAGIC </code></pre>
# MAGIC <p>Update your map to instead use the correct data:</p>
# MAGIC <pre><code>@#@
# MAGIC ###
# MAGIC @#@
# MAGIC </code></pre>
# MAGIC <p>This change will split your map into four separate sections, each with its own entrance:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #a.#Cd#       #a.#Cd#
# MAGIC ##...##       ##<em>@#@</em>##
# MAGIC ##.@.##  --&gt;  ##<em>###</em>##
# MAGIC ##...##       ##<em>@#@</em>##
# MAGIC #cB#Ab#       #cB#Ab#
# MAGIC #######       #######
# MAGIC </code></pre>
# MAGIC <p>Because some of the keys are for doors in other vaults, it would take much too long to collect all of the keys by yourself.  Instead, you deploy four remote-controlled robots. Each starts at one of the entrances (<code>@</code>).</p>
# MAGIC <p>Your goal is still to <em>collect all of the keys in the fewest steps</em>, but now, each robot has its own position and can move independently.  You can only remotely control a single robot at a time. Collecting a key instantly unlocks any corresponding doors, regardless of the vault in which the key or door is found.</p>
# MAGIC <p>For example, in the map above, the top-left robot first collects key <code>a</code>, unlocking door <code>A</code> in the bottom-right vault:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#Cd#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##@#@##
# MAGIC #cB#.b#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Then, the bottom-right robot collects key <code>b</code>, unlocking door <code>B</code> in the bottom-left vault:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#Cd#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##@#.##
# MAGIC #c.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Then, the bottom-left robot collects key <code>c</code>:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#.d#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##.#.##
# MAGIC #@.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Finally, the top-right robot collects key <code>d</code>:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#.@#
# MAGIC ##.#.##
# MAGIC #######
# MAGIC ##.#.##
# MAGIC #@.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>In this example, it only took <code><em>8</em></code> steps to collect all of the keys.</p>
# MAGIC <p>Sometimes, multiple robots might have keys available, or a robot might have to wait for multiple keys to be collected:</p>
# MAGIC <pre><code>###############
# MAGIC #d.ABC.#.....a#
# MAGIC ######@#@######
# MAGIC ###############
# MAGIC ######@#@######
# MAGIC #b.....#.....c#
# MAGIC ###############
# MAGIC </code></pre>
# MAGIC <p>First, the top-right, bottom-left, and bottom-right robots take turns collecting keys <code>a</code>, <code>b</code>, and <code>c</code>, a total of <code>6 + 6 + 6 = 18</code> steps. Then, the top-left robot can access key <code>d</code>, spending another <code>6</code> steps; collecting all of the keys here takes a minimum of <code><em>24</em></code> steps.</p>
# MAGIC <p>Here's a more complex example:</p>
# MAGIC <pre><code>#############
# MAGIC #DcBa.#.GhKl#
# MAGIC #.###@#@#I###
# MAGIC #e#d#####j#k#
# MAGIC ###C#@#@###J#
# MAGIC #fEbA.#.FgHi#
# MAGIC #############
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Top-left robot collects key <code>a</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>b</code>.</li>
# MAGIC <li>Top-left robot collects key <code>c</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>d</code>.</li>
# MAGIC <li>Top-left robot collects key <code>e</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>f</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>g</code>.</li>
# MAGIC <li>Top-right robot collects key <code>h</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>i</code>.</li>
# MAGIC <li>Top-right robot collects key <code>j</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>k</code>.</li>
# MAGIC <li>Top-right robot collects key <code>l</code>.</li>
# MAGIC </ul>
# MAGIC <p>In the above example, the fewest steps to collect all of the keys is <code><em>32</em></code>.</p>
# MAGIC <p>Here's an example with more choices:</p>
# MAGIC <pre><code>#############
# MAGIC #g#f.D#..h#l#
# MAGIC #F###e#E###.#
# MAGIC #dCba@#@BcIJ#
# MAGIC #############
# MAGIC #nK.L@#@G...#
# MAGIC #M###N#H###.#
# MAGIC #o#m..#i#jk.#
# MAGIC #############
# MAGIC </code></pre>
# MAGIC <p>One solution with the fewest steps is:</p>
# MAGIC <ul>
# MAGIC <li>Top-left robot collects key <code>e</code>.</li>
# MAGIC <li>Top-right robot collects key <code>h</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>i</code>.</li>
# MAGIC <li>Top-left robot collects key <code>a</code>.</li>
# MAGIC <li>Top-left robot collects key <code>b</code>.</li>
# MAGIC <li>Top-right robot collects key <code>c</code>.</li>
# MAGIC <li>Top-left robot collects key <code>d</code>.</li>
# MAGIC <li>Top-left robot collects key <code>f</code>.</li>
# MAGIC <li>Top-left robot collects key <code>g</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>k</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>j</code>.</li>
# MAGIC <li>Top-right robot collects key <code>l</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>n</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>m</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>o</code>.</li>
# MAGIC </ul>
# MAGIC <p>This example requires at least <code><em>72</em></code> steps to collect all keys.</p>
# MAGIC <p>After updating your map and using the remote-controlled robots, <em>what is the fewest steps necessary to collect all of the keys?</em></p>
# MAGIC </article>

# COMMAND ----------

mid <- c(ceiling(max(coords$row) / 2), ceiling(max(coords$col) / 2))

coords2 <-
  coords %>%
  mutate(
    value = case_when(
      abs(row - mid[1]) == 1 & abs(col - mid[2]) == 1 ~ "@",
      abs(row - mid[1]) <= 1 & abs(col - mid[2]) <= 1 ~ "#",
      TRUE ~ value
    )
  )

quadrants <- list()
quadrants[[1]] <- coords2 %>% filter(row <= mid[1], col >= mid[2])
quadrants[[2]] <- coords2 %>% filter(row <= mid[1], col <= mid[2])
quadrants[[3]] <- coords2 %>% filter(row >= mid[1], col <= mid[2])
quadrants[[4]] <- coords2 %>% filter(row >= mid[1], col >= mid[2])

# COMMAND ----------

plot_maze <- function(coords) {
  coords %>%
    mutate(
      # https://coolors.co/55dde0-33658a-2f4858-f6ae2d-f26419
      fill = case_when(
        value %in% letters ~ "#F6AE2D",
        value %in% LETTERS ~ "#33658A",
        value == "#" ~ "#2F4858",
        value == "@" ~ "#F26419"
      ),
      label = ifelse(str_detect(value, "\\w"), value, NA)
    ) %>%
    ggplot(aes(col, row, fill = I(fill), label = label)) +
      geom_tile() +
      geom_text(size = 2.5) +
      scale_y_reverse() +
      theme_void()
}

(plot_maze(quadrants[[2]]) + plot_maze(quadrants[[1]])) / (plot_maze(quadrants[[3]]) + plot_maze(quadrants[[4]]))

# COMMAND ----------

# Observe that for any given letter, no quadrant contains both the key and lock. This means that, for each quadrant, we just need to collect all the keys ignoring the locks.

# COMMAND ----------

collect_keys <- function(coords) {
  target_n_keys <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% length()
  visited <- hashmap(default = FALSE)
  states <- datastructures::fibonacci_heap("numeric")
  
  datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(keys = "", d = 0))
  
  coords <- to_hashmap(coords)
  
  message(target_n_keys)
  
  while (datastructures::size(states) > 0) {
    state <- datastructures::pop(states)[[1]]
    
    if (visited[c(state$row, state$col, state$keys)]) next
    visited[c(state$row, state$col, state$keys)] <- TRUE

    # Key
    if (state$value %in% letters) {
      if (!str_detect(state$keys, state$value)) state$keys <- str_c(state$keys, state$value)
      if (str_length(state$keys) == target_n_keys) return(state$d)
      message(state$keys)
    }

    # Lock - ignore all locks
    # if (state$value %in% LETTERS) {
    #   if (!str_detect(str_to_upper(state$keys), state$value)) next
    # }
    
    for (direction in c("N", "E", "S", "W")) {
      new_state <- tibble(
        row = state$row + (direction == "S") - (direction == "N"),
        col = state$col + (direction == "E") - (direction == "W"),
        value = coords[c(row, col)],
        keys = state$keys,
        d = state$d + 1
      )
      
      if (new_state$value != "#") {
        datastructures::insert(states, new_state$d, new_state)
      }
    }
  }
  stop("Could not find all keys")
}

# COMMAND ----------

collect_keys(quadrants[[1]])

# COMMAND ----------

quadrants[[1]]$value %>% keep(str_detect, "[a-z]")# %>% length()

# COMMAND ----------

collect_keys(quadrants[[2]])

# COMMAND ----------

collect_keys(quadrants[[3]])

# COMMAND ----------

collect_keys(quadrants[[4]])

# COMMAND ----------

answer <- quadrants %>% map_dbl(collect_keys) %>% sum()
answer

# COMMAND ----------

paths_to_keys <- quadrants %>% map(get_paths_to_keys)

str(paths_to_keys)

# COMMAND ----------

# The keys can be collected in this order:
#     q1:   m    tin        hexsdwq
#     q2: og               k       j
#     q3:    buvr   cya
#     q4:              fzpl
key_order <- "ogmbuvrtincyafzplkhexsdwqj" %>% str_split("") %>% unlist()
key_order

# COMMAND ----------

get_key <- function(coords, target_key, keys = c(), start_state = NULL) {
  visited <- hashmap(default = FALSE)
  states <- datastructures::fibonacci_heap("numeric")
  
  if (is.null(start_state)) {
    start_state <- coords %>% filter(value == "@") %>% mutate(d = 0)
  }
  datastructures::insert(states, 0, start_state)
  
  coords <- to_hashmap(coords)
  
  while (datastructures::size(states) > 0) {
    state <- datastructures::pop(states)[[1]]
    
    if (visited[c(state$row, state$col)]) next
    visited[c(state$row, state$col)] <- TRUE

    # Key
    if (state$value %in% letters && !(state$value %in% keys)) {
      if (state$value != target_key) next
      return(state)
    }

    # Lock
    if (state$value %in% LETTERS) {
      if (!(str_to_lower(state$value) %in% keys)) next
    }
    
    for (direction in c("N", "E", "S", "W")) {
      new_state <- tibble(
        row = state$row + (direction == "S") - (direction == "N"),
        col = state$col + (direction == "E") - (direction == "W"),
        value = coords[c(row, col)],
        d = state$d + 1
      )
      
      if (new_state$value != "#") {
        datastructures::insert(states, new_state$d, new_state)
      }
    }
  }
  stop("Could not find key")
}

# COMMAND ----------

state <- list(NULL, NULL, NULL, NULL)
keys <- c()
for (key in key_order) {
  quadrant <- which(map_lgl(quadrants, ~key %in% .$value))
  
  state[[quadrant]] <- get_key(coords = quadrants[[quadrant]], target_key = key, keys = keys, start_state = state[[quadrant]])
  keys <- c(keys, key)
}
answer <- state %>% map_dbl("d") %>% sum()
answer

# COMMAND ----------

# 2038 too high

# I Think just find the shortest path that collects all the keys. What about back tracking? Maybe there isn't any! No key from the same maze is required to unlock a lock from the same maze!

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

# collect_keys <- function(coords) {
#   target_n_keys <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% length()
#   visited <- hashmap(default = FALSE)
#   states <- datastructures::fibonacci_heap("numeric")
  
#   datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(keys = "", d = 0))
  
#   coords <- to_hashmap(coords)
  
#   message(target_n_keys)
  
#   while (datastructures::size(states) > 0) {
#     state <- datastructures::pop(states)[[1]]
    
#     if (visited[c(state$row, state$col)]) next
#     visited[c(state$row, state$col)] <- TRUE

#     # Key
#     if (state$value %in% letters) {
#       state$keys <- str_c(state$keys, state$value)
#       if (str_length(state$keys) == target_n_keys) return(state$d)
#       message(state$keys)
#     }

#     # Lock - ignore all locks
#     # if (state$value %in% LETTERS) {
#     #   if (!str_detect(str_to_upper(state$keys), state$value)) next
#     # }
    
#     for (direction in c("N", "E", "S", "W")) {
#       new_state <- tibble(
#         row = state$row + (direction == "S") - (direction == "N"),
#         col = state$col + (direction == "E") - (direction == "W"),
#         value = coords[c(row, col)],
#         keys = state$keys,
#         d = state$d + 1
#       )
      
#       if (new_state$value != "#") {
#         datastructures::insert(states, new_state$d, new_state)
#       }
#     }
#   }
#   stop("Could not find all keys")
# }

# COMMAND ----------

get_paths_to_keys <- function(coords) {
  paths_to_keys <- list()
  
  visited <- hashmap(default = FALSE)
  states <- datastructures::fibonacci_heap("numeric")
  
  start_coords <- coords %>% filter(value == "@") %>% mutate(passed = "", d = 0)
  for (i in seq_len(nrow(start_coords))) {
    datastructures::insert(states, 0, start_coords[i,])
  }
  
  coords <- to_hashmap(coords)
  
  while (datastructures::size(states) > 0) {
    state <- datastructures::pop(states)[[1]]
    
    if (visited[c(state$row, state$col, state$keys)]) next
    visited[c(state$row, state$col, state$keys)] <- TRUE

    # Key
    if (state$value %in% letters) {
      paths_to_keys[[state$value]] <- state$passed
      state$passed  <- str_c(state$passed, state$value)
    }

    # Lock
    if (state$value %in% LETTERS) {
      state$passed  <- str_c(state$passed, state$value)
    }
    
    for (direction in c("N", "E", "S", "W")) {
      new_state <- tibble(
        row = state$row + (direction == "S") - (direction == "N"),
        col = state$col + (direction == "E") - (direction == "W"),
        value = coords[c(row, col)],
        passed = state$passed,
        d = state$d + 1
      )
      
      if (new_state$value != "#") {
        datastructures::insert(states, new_state$d, new_state)
      }
    }
  }
  
  paths_to_keys
}

# COMMAND ----------

key_order <- "abcd" %>% str_split("") %>% unlist()
key_order

# COMMAND ----------

# The keys can be collected in this order:
#     q1:   m    tin        hexsdwq
#     q2: go               k       j
#     q3:    buvr   cya
#     q4:              fzpl
key_order <- tribble(
  ~quadrant, ~key,
          2,  "g",
          2,  "o",
          1,  "m",
          3,  "b",
          3,  "u",
          3,  "v",
          3,  "r",
          1,  "t",
          1,  "i",
          1,  "n",
          3,  "c",
          3,  "y",
          3,  "a",
          4,  "f",
          4,  "z",
          4,  "p",
          4,  "l",
          2,  "k",
          3,  "h",
          3,  "e",
          3,  "x",
          3,  "s",
          3,  "d",
          3,  "w",
          3,  "a",
          2,  "j"
)

# COMMAND ----------

state <- list(NULL, NULL, NULL, NULL)
keys <- c()
for (i in seq_len(nrow(key_order))) {
  quadrant <- key_order$quadrant[i]
  key <- key_order$key[i]
  
  state[[quadrant]] <- get_key(coords = coords, target_key = key, keys = keys, start_state = state[[quadrant]])
  keys <- c(keys, key)
}
answer <- state %>% map_dbl(d) %>% sum()
answer

# COMMAND ----------

state %>% map_dbl(d)

# COMMAND ----------

key_order

# COMMAND ----------

names(paths_to_keys)

# COMMAND ----------

# I think just get shortest path from @ to all keys. The path will contain a bunch of locks. You should be able to figure out the order of keys from that

# COMMAND ----------

# needs to be solved as a graph
# get distance between all pairs
# a node includes the keys possessed. Actually, a node is JUST the keys possessed in order

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------

coords_quad1 %>%
  mutate(
    # https://coolors.co/55dde0-33658a-2f4858-f6ae2d-f26419
    fill = case_when(
      value %in% letters ~ "#F6AE2D",
      value %in% LETTERS ~ "#33658A",
      value == "#" ~ "#2F4858",
      value == "@" ~ "#F26419"
    ),
    label = ifelse(str_detect(value, "\\w"), value, NA)
  ) %>%
  ggplot(aes(col, row, fill = I(fill), label = label)) +
    geom_tile() +
    geom_text(size = 2.5) +
    scale_y_reverse() +
    theme_void()

# COMMAND ----------

coords2 %>%
  mutate(
    # https://coolors.co/55dde0-33658a-2f4858-f6ae2d-f26419
    fill = case_when(
      value %in% letters ~ "#F6AE2D",
      value %in% LETTERS ~ "#33658A",
      value == "#" ~ "#2F4858",
      value == "@" ~ "#F26419"
    ),
    label = ifelse(str_detect(value, "\\w"), value, NA)
  ) %>%
  ggplot(aes(col, row, fill = I(fill), label = label)) +
    geom_tile() +
    geom_text(size = 2.5) +
    scale_y_reverse() +
    theme_void()

# COMMAND ----------

# get_key <- function(coords, key) {
#   visited <- hashmap(default = FALSE)
#   states <- datastructures::fibonacci_heap("numeric")
  
#   start_coords <- coords %>% filter(value == "@") %>% mutate(keys = "", d = 0)
#   for (i in seq_len(nrow(start_coords))) {
#     datastructures::insert(states, 0, start_coords[i,])
#   }
  
#   coords <- to_hashmap(coords)
  
#   while (TRUE) {
#     state <- datastructures::pop(states)[[1]]
    
#     if (visited[c(state$row, state$col, state$keys)]) next
#     visited[c(state$row, state$col, state$keys)] <- TRUE

#     # Key
#     if (state$value %in% letters) {
#       if (state$value != key) next
#       state$keys  <- str_c(state$keys, state$value)
#       return(state)
#       # visited <- hashmap(default = FALSE)
#       # key_order <- key_order[-1]
#       # if (length(key_order) == 0) return(state$d)
#     }

#     # Lock
#     if (state$value %in% LETTERS) {
#       if (str_detect(state$value, state$keys)) next
#     }
    
#     for (direction in c("N", "E", "S", "W")) {
#       new_state <- tibble(
#         row = state$row + (direction == "S") - (direction == "N"),
#         col = state$col + (direction == "E") - (direction == "W"),
#         value = coords[c(row, col)],
#         locks_passed = state$locks_passed,
#         d = state$d + 1
#       )
      
#       if (new_state$value != "#") {
#         datastructures::insert(states, new_state$d, new_state)
#       }
#     }
#   }
# }

# COMMAND ----------

h <- hashmap()
h[c(1,1)] <- "@"
h[c(1,1)]

# COMMAND ----------

# sort_string <- function(s) {
#   s %>%
#     str_split("") %>%
#     unlist() %>%
#     str_sort() %>%
#     str_c(collapse = "")
# }

# solve <- function(coords) {
#   target <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% unlist() %>% str_sort() %>% str_c(collapse = "")
#   visited <- hashmap(default = FALSE)
#   states <- datastructures::fibonacci_heap("numeric")
  
#   datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(keys = "", d = 0))
  
#   coords <- to_hashmap(coords)
  

#   repeat {
#     state <- datastructures::pop(states)[[1]]
#     message(glue::glue("nrow: {nrow(state)}\n\n"))
#     message(glue::glue("cls: {class(state$value)}\n\n"))
#     message(glue::glue("{state$row},{state$col}: {state$value} ({state$d})\n\n"))
    
#     if (visited[c(state$row, state$col, state$keys)]) next
#     visited[c(state$row, state$col, state$keys)] <- TRUE

#     # Key
#     if (state$value %in% letters) {
#       if (!str_detect(state$keys, state$value)) state$keys <- sort_string(str_c(state$keys, state$value))
#       if (state$keys == target) return(state$d)
#     }

#     # Lock
#     if (state$value %in% LETTERS) {
#       if (!str_detect(str_to_upper(state$keys), state$value)) next
#     }
    
#     for (direction in c("N", "E", "S", "W")) {
#       new_state <- tibble(
#         row = state$row + (direction == "S") - (direction == "N"),
#         col = state$col + (direction == "E") - (direction == "W"),
#         value = coords[c(row, col)],
#         keys = state$keys,
#         d = state$d + 1
#       )
      
#       if (new_state$value != "#") {
#         datastructures::insert(states, new_state$d, new_state)
#       }
#     }
#   }
# }

# COMMAND ----------

h <- to_hashmap(coords)
h[c(1,2)]

# COMMAND ----------

start_pos <- coords %>% filter(value == "@")
start_pos

# COMMAND ----------

coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% unlist() %>% str_sort() %>% str_c(collapse = "")

# COMMAND ----------

states <- datastructures::fibonacci_heap("numeric")

# COMMAND ----------

datastructures::insert(states, 0, list(row = start_pos$row, col = start_pos$col, value = 1, keys = ""))

# COMMAND ----------

datastructures::insert(states, 0, list(row = start_pos$row, col = start_pos$col, value = 1, keys = ""))
a <- datastructures::pop(states)
a

# COMMAND ----------

?datastructures::pop

# COMMAND ----------

a[[1]]

# COMMAND ----------

states <- datastructures::fibonacci_heap("numeric")
  
datastructures::insert(states, 0, list(row = start_pos$row, col = start_pos$col, value = coords[c(start_pos$row, start_pos$col)], keys = ""))

# COMMAND ----------

answer <- solve(start_pos, coords)
answer

# COMMAND ----------

sort_string <- function(s) {
  s %>%
    str_split("") %>%
    unlist() %>%
    str_sort() %>%
    str_c(collapse = "")
}

target <- m[m %in% letters] %>% str_c(collapse = "") %>% sort_string()
target

# COMMAND ----------



# COMMAND ----------

answer <- solve(start_pos, coords)
answer

# COMMAND ----------

# MAGIC %md ## Scratch

# COMMAND ----------



# as.hashmap <- function(x, ...) UseMethod("as.hashmap", x)

# COMMAND ----------

Rcpp::sourceCpp(code = '
#include <Rcpp.h>

struct state {
  int64_t d;
  int row;
  int col;
  std::string keys;
};

struct pair_hash {
  template <class T1, class T2>
  std::size_t operator () (const std::pair<T1,T2> &p) const {
    auto h1 = std::hash<T1>{}(p.first);
    auto h2 = std::hash<T2>{}(p.second);

    return h1 ^ h2;  
  }
};

// [[Rcpp::export]]
int64_t solve_cpp(int start_row, int start_col, std::vector<int> rows, std::vector<int> cols, std::string values) {
  std::unordered_map<std::pair<int, int>, char, pair_hash> coords;

  islower(\'a\');
  // int target_key_length = count_if(s.begin(), s.end(), [](unsigned char ch) { return islower(ch); });
  int target_key_length = count_if(values.begin(), values.end(), &std::islower);

  std::string target = values;
  target.erase(std::remove(target.begin(), target.end(), \'a\'), target.end());
  sort(target.begin(), target.end());
  std::cout << target << std::endl;

  return 0;
}
')

# COMMAND ----------

solve_cpp(
  start_row = 0,
  start_col = 0,
  rows = 1,
  cols = 1,
  values = "helloa"
)

# COMMAND ----------

Rcpp::sourceCpp(code = '
#include <Rcpp.h>

// struct state {
//   int64_t d;
//   int row;
//   int col;
//   std::string keys;
// };

// [[Rcpp::export]]
//int64_t solve_cpp(int start_row, int start_col, std::vector<int> rows, std::vector<int> cols, std::vector<char> values) {
int solve_cpp() {
  // std::unordered_map<std::pair<int, int>, char> coords;

  return 0;
}
')

# COMMAND ----------

# MAGIC %md ## asd

# COMMAND ----------

c(m)

# COMMAND ----------

arrayInd(which(m != ""), dim(m), dimnames(m), useNames = TRUE)

# COMMAND ----------

keys <-
  which(m %in% letters) %>%
  arrayInd(dim(m), dimnames(m), useNames = TRUE) %>%
  as_tibble() %>%
  mutate(value = m[m %in% letters]) %>%
  create_coord(default = FALSE)
str(keys)

# COMMAND ----------

locks <-
  which(m %in% LETTERS) %>%
  arrayInd(dim(m), dimnames(m), useNames = TRUE) %>%
  as_tibble() %>%
  mutate(value = m[m %in% LETTERS]) %>%
  create_coord(default = FALSE)
str(locks)

# COMMAND ----------

available_coords <-
  which(m != "#", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = TRUE) %>%
  create_coord(default = FALSE)
str(available_coords)

# COMMAND ----------

x <- m
wh = c(1,1)
arrayInd(wh, dim(x), dimnames(x), useNames = TRUE)

# COMMAND ----------

which

# COMMAND ----------


  result <- list()
 # if (!is.null(inds)) {
    result <- as.list(inds$value)
    names(inds) <- hash(inds$row, inds$col)
 # }
result

# COMMAND ----------

inds

# COMMAND ----------

inds <-
  which(m != "#", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = TRUE)
inds

# COMMAND ----------

create_coord(a, default = FALSE)

# COMMAND ----------

start_pos <- which(m == "@", arr.ind = TRUE)
start_pos

# COMMAND ----------

which(str_is_upper(m), arr.ind = TRUE)

# COMMAND ----------

which(m %in% c("#"), arr.ind = TRUE)

# COMMAND ----------

m[m %in% c("#")]

# COMMAND ----------

str_to_upper(m)

# COMMAND ----------

items <-
  which(m != "#", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = TRUE) %>%
  create_coord(default = FALSE)

# COMMAND ----------

available_coords <-
  which(m != "#", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = TRUE) %>%
  create_coord(default = FALSE)
available_coords

# COMMAND ----------

items <-

# COMMAND ----------

available_coords <- which(m != "#", arr.ind = TRUE)
available_coords

# COMMAND ----------

#djkstra but visited includes items held

# COMMAND ----------

Rcpp::sourceCpp(code = '
#include <Rcpp.h>

struct State {
  int64_t d;
  int row;
  int col;
  std::string keys;
};

struct PairHash {
  template <class T1, class T2>
  std::size_t operator () (const std::pair<T1,T2> &p) const {
    auto h1 = std::hash<T1>{}(p.first);
    auto h2 = std::hash<T2>{}(p.second);

    return h1 ^ h2;  
  }
};

// [[Rcpp::export]]
int64_t solve_cpp(std::vector<int> rows, std::vector<int> cols, std::string values) {
  int target_key_length = std::count_if(values.begin(), values.end(), [](unsigned char c){ return std::islower(c); });
  std::unordered_map<std::pair<int, int>, char, PairHash> coords;

  //auto comp = [](const State& lhs, const State& rhs) { return lhs.row < rhs.row ? true : (lhs.col < rhs.col ? true : lhs.keys < rhs.keys); };
  //auto visited  = std::unordered_set<State, decltype(comp)>(comp);

  
  auto hash = [](const Point& p) { return p.X + 10 * p.Y; };
  auto equal = [](const Point& p1, const Point& p2) { return p1.X == p2.X && p1.Y == p2.Y; };
  auto visited  = std::unordered_set<State, decltype(hash)>(hash), decltype(equal)>(equal);

  int start_row;
  int start_col;


  for (int i = 0; i < rows.size(); ++i) {
    if (values[i] == \'@\') {
      // State s = {1, 1, 1, ""};
      // visited.insert(s);
      //visited.insert({0, rows[i], cols[i], ""});
    }
    coords[std::make_pair(rows[i], cols[i])] = values[i];
  }
  


  return 0;
}
')

# COMMAND ----------

solve_cpp(
  rows = coords$row,
  cols = coords$col,
  values = str_c(coords$value, collapse = "")
)

# COMMAND ----------

# Rcpp::sourceCpp(code = '
# #include <Rcpp.h>

# struct State {
#   int64_t d;
#   int row;
#   int col;
#   std::string keys;
# };

# struct pair_hash {
#   template <class T1, class T2>
#   std::size_t operator () (const std::pair<T1,T2> &p) const {
#     auto h1 = std::hash<T1>{}(p.first);
#     auto h2 = std::hash<T2>{}(p.second);

#     return h1 ^ h2;  
#   }
# };

# // [[Rcpp::export]]
# int64_t solve_cpp(std::vector<int> rows, std::vector<int> cols, std::string values) {
#   int target_key_length = std::count_if(values.begin(), values.end(), [](unsigned char c){ return std::islower(c); });
#   std::unordered_map<std::pair<int, int>, char, pair_hash> coords;

#   auto comp = [](const State& lhs, const State& rhs) { return lhs.row < rhs.row ? true : (lhs.col < rhs.col ? true : lhs.keys < rhs.keys); };
#   auto visited  = std::set<State, decltype(comp)>(comp);

#   int start_row;
#   int start_col;


#   for (int i = 0; i < rows.size(); ++i) {
#     if (values[i] == \'@\') {
#       // State s = {1, 1, 1, ""};
#       // visited.insert(s);
#       visited.insert({0, rows[i], cols[i], ""});
#     }
#     coords[std::make_pair(rows[i], cols[i])] = values[i];
#   }
  


#   return 0;
# }
# ')

# COMMAND ----------

# Rcpp::sourceCpp(code = '
# #include <Rcpp.h>

# struct State {
#   int64_t d;
#   int row;
#   int col;
#   std::string keys;
# };

# struct pair_hash {
#   template <class T1, class T2>
#   std::size_t operator () (const std::pair<T1,T2> &p) const {
#     auto h1 = std::hash<T1>{}(p.first);
#     auto h2 = std::hash<T2>{}(p.second);

#     return h1 ^ h2;  
#   }
# };

# // [[Rcpp::export]]
# int64_t solve_cpp(std::vector<int> rows, std::vector<int> cols, std::string values) {
#   int target_key_length = std::count_if(values.begin(), values.end(), [](unsigned char c){ return std::islower(c); });
#   std::unordered_map<std::pair<int, int>, char, pair_hash> coords;
#   // std::set<State, > visited;
#   // auto visited = std::make_set<State>([](const State& lhs, const State& rhs) { lhs.row == rhs.row && lhs.col == rhs.col && lhs.keys == rhs.keys; });


#    auto comp = [](const State& lhs, const State& rhs) { lhs.row == rhs.row && lhs.col == rhs.col && lhs.keys == rhs.keys; };
#    auto set  = std::set<State, decltype(comp)>(comp);

#   int start_row;
#   int start_col;


#   for (int i = 0; i < rows.size(); ++i) {
#     if (values[i] == \'@\') {
#       start_row = rows[i];
#       start_col = cols[i];
#     }
#     coords[std::make_pair(rows[i], cols[i])] = values[i];
#   }
  


#   return 0;
# }
# ')

# COMMAND ----------

# Rcpp::sourceCpp(code = '
# #include <Rcpp.h>

# struct State {
#   int row;
#   int col;
#   std::string keys;
# };

# struct pair_hash {
#   template <class T1, class T2>
#   std::size_t operator () (const std::pair<T1,T2> &p) const {
#     auto h1 = std::hash<T1>{}(p.first);
#     auto h2 = std::hash<T2>{}(p.second);

#     return h1 ^ h2;  
#   }
# };

# // [[Rcpp::export]]
# int64_t solve_cpp(std::vector<int> rows, std::vector<int> cols, std::string values) {
#   int target_key_length = std::count_if(values.begin(), values.end(), [](unsigned char c){ return std::islower(c); });
#   std::unordered_map<std::pair<int, int>, char, pair_hash> coords;
#   std::set<State> visited;

#   int start_row;
#   int start_col;


#   for (int i = 0; i < rows.size(); ++i) {
#     if (values[i] == \'@\') {
#       visited.insert({rows[i], cols[i], ""});
#     }
#     coords[std::make_pair(rows[i], cols[i])] = values[i];
#   }
  


#   return 0;
# }
# ')

# COMMAND ----------

  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m))
