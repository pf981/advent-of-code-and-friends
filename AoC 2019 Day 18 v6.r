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

solve <- function(coords) {
  target_length <- coords$value %>% unique() %>% keep(str_detect, "[a-z]") %>% length()
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
      if (!str_detect(state$keys, state$value)) state$keys <- str_c(state$keys, state$value)
      if (str_length(state$keys) == target_length) return(state$d)
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
      fill = case_when(
        value %in% letters ~ "#F6AE2D",
        value %in% LETTERS ~ "#A0522D",
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

get_paths_to_keys <- function(coords) {
  paths_to_keys <- list()
  
  visited <- hashmap(default = FALSE)
  states <- datastructures::fibonacci_heap("numeric")
  
  datastructures::insert(states, 0, coords %>% filter(value == "@") %>% mutate(passed = "", d = 0))
  
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
  
  state[[quadrant]] <- get_key(
    coords = quadrants[[quadrant]],
    target_key = key,
    keys = keys,
    start_state = state[[quadrant]]
  )
  keys <- c(keys, key)
}
answer <- state %>% map_dbl("d") %>% sum()
answer
