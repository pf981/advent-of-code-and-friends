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

input <- "#########
#b.A.@.a#
#########
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

start_pos <- coords %>% filter(value == "@")
start_pos

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

sort_string <- function(s) {
  s %>%
    str_split("") %>%
    unlist() %>%
    str_sort() %>%
    str_c(collapse = "")
}

solve <- function(start_pos, coords) {
  target <- coords %>% unique() %>% keep(str_detect, "[a-z]") %>% unlist() %>% str_sort() %>% str_c(collapse = "")
  
  ds <- c(0)
  rows <- c(start_pos$row)
  cols <- c(start_pos$col)
  keyss <- c("")

  visited <- c()

  repeat {
    i <- which.min(ds)

    d <- ds[1]
    row <- rows[1]
    col <- cols[1]
    keys <- keyss[1]

    ds <- ds[-1]
    rows <- rows[-1]
    cols <- cols[-1]
    keyss <- keyss[-1]

    if (hash(row, col, keys) %in% visited) next
    visited <- c(visited, hash(row, col, keys))

    value <- coords[row, col]

    # Key
    if (value %in% letters) {
      if (!str_detect(keys, value)) keys <- sort_string(str_c(keys, value))
      if (keys == target) return(d)
    }

    # Lock
    if (value %in% LETTERS) {
      if (!str_detect(str_to_upper(keys), value)) next
    }
    
    for (direction in c("N", "E", "S", "W")) {
      new_row <- row + (direction == "S") - (direction == "N")
      new_col <- col + (direction == "E") - (direction == "W")
      new_d <- d + 1
      
      if (coords[new_row, new_col] != "#") {
        ds <- c(ds, new_d)
        rows <- c(rows, new_row)
        cols <- c(cols, new_col)
        keyss <- c(keyss, keys)
      }
    }
  }
}

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
