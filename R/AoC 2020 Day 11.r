# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/11

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 11: Seating System ---</h2><p>Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!</p>
# MAGIC <p>By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).</p>
# MAGIC <p>The seat layout fits neatly on a grid. Each position is either floor (<code>.</code>), an empty seat (<code>L</code>), or an occupied seat (<code>#</code>). For example, the initial seat layout might look like this:</p>
# MAGIC <pre><code>L.LL.LL.LL
# MAGIC LLLLLLL.LL
# MAGIC L.L.L..L..
# MAGIC LLLL.LL.LL
# MAGIC L.LL.LL.LL
# MAGIC L.LLLLL.LL
# MAGIC ..L.L.....
# MAGIC LLLLLLLLLL
# MAGIC L.LLLLLL.L
# MAGIC L.LLLLL.LL
# MAGIC </code></pre>
# MAGIC <p>Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the <em>number of occupied seats</em> adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:</p>
# MAGIC <ul>
# MAGIC <li>If a seat is <em>empty</em> (<code>L</code>) and there are <em>no</em> occupied seats adjacent to it, the seat becomes <em>occupied</em>.</li>
# MAGIC <li>If a seat is <em>occupied</em> (<code>#</code>) and <em>four or more</em> seats adjacent to it are also occupied, the seat becomes <em>empty</em>.</li>
# MAGIC <li>Otherwise, the seat's state does not change.</li>
# MAGIC </ul>
# MAGIC <p><span title="Floor... floor never changes.">Floor (<code>.</code>) never changes</span>; seats don't move, and nobody sits on the floor.</p>
# MAGIC <p>After one round of these rules, every seat in the example layout becomes occupied:</p>
# MAGIC <pre><code>#.##.##.##
# MAGIC #######.##
# MAGIC #.#.#..#..
# MAGIC ####.##.##
# MAGIC #.##.##.##
# MAGIC #.#####.##
# MAGIC ..#.#.....
# MAGIC ##########
# MAGIC #.######.#
# MAGIC #.#####.##
# MAGIC </code></pre>
# MAGIC <p>After a second round, the seats with four or more occupied adjacent seats become empty again:</p>
# MAGIC <pre><code>#.LL.L#.##
# MAGIC #LLLLLL.L#
# MAGIC L.L.L..L..
# MAGIC #LLL.LL.L#
# MAGIC #.LL.LL.LL
# MAGIC #.LLLL#.##
# MAGIC ..L.L.....
# MAGIC #LLLLLLLL#
# MAGIC #.LLLLLL.L
# MAGIC #.#LLLL.##
# MAGIC </code></pre>
# MAGIC <p>This process continues for three more rounds:</p>
# MAGIC <pre><code>#.##.L#.##
# MAGIC #L###LL.L#
# MAGIC L.#.#..#..
# MAGIC #L##.##.L#
# MAGIC #.##.LL.LL
# MAGIC #.###L#.##
# MAGIC ..#.#.....
# MAGIC #L######L#
# MAGIC #.LL###L.L
# MAGIC #.#L###.##
# MAGIC </code></pre>
# MAGIC <pre><code>#.#L.L#.##
# MAGIC #LLL#LL.L#
# MAGIC L.L.L..#..
# MAGIC #LLL.##.L#
# MAGIC #.LL.LL.LL
# MAGIC #.LL#L#.##
# MAGIC ..L.L.....
# MAGIC #L#LLLL#L#
# MAGIC #.LLLLLL.L
# MAGIC #.#L#L#.##
# MAGIC </code></pre>
# MAGIC <pre><code>#.#L.L#.##
# MAGIC #LLL#LL.L#
# MAGIC L.#.L..#..
# MAGIC #L##.##.L#
# MAGIC #.#L.LL.LL
# MAGIC #.#L#L#.##
# MAGIC ..L.L.....
# MAGIC #L#L##L#L#
# MAGIC #.LLLLLL.L
# MAGIC #.#L#L#.##
# MAGIC </code></pre>
# MAGIC <p>At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count <em><code>37</code></em> occupied seats.</p>
# MAGIC <p>Simulate your seating area by applying the seating rules repeatedly until no seats change state. <em>How many seats end up occupied?</em></p>
# MAGIC </article>

# COMMAND ----------

install.packages("matrixcalc")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "LLLLLLLLLLLLLLL.LL.L.LLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLLLLL..L.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLL.LLLLL.L.LLLLLL.
LLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LL.LL.LLLLLLLLLLLLLLL
LLLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLL.LLLLLLLL.L.LLLLLLLLLLLLLL.
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.L
LLLL..LLLLL.LLLLLLLL..LLLLLLLLLLLLLL..LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL..LLLL.LLL.LLLLLLLLLLL
LLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLL.LLLLLLL.L
.LLLLL..LLL.LLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLL.LLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLL.LLLLLLLLL
LLLLLLLLLLL.LLL.LLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLL.L.LLLLLLLLLLLLLLLLLL.LLLLLLLLL
LLLLL.L.LLL.LLLLLLLL.LLLLLLLLL..LL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLL..LLLLL.LLLLL.LLL.LLLLL
L..L.L...LL.LL...L....LL......L.L.L...L....LL........LL.L..L...L.......L.L...L...LL......LL...L
LLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLL.LLL.LLLLLLL.LLLLLLLLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLL.LLL.LLLLLLLL.
LL.LL.LL.LL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.L.LLLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLL
LLLL..LLLLLLLLLLLLLL.LLLLLLLLLLLL.LL.LLLLLLLLL.LLLLLL.LLLLLLL.LL.L.LLLLLL...LLLLLLLLL.LLLLLLLLL
LLLLL..LLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLLLL
L.LLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LL........LL....L.L.....LLL......LLL..L.L.LLLLL...LL....L.....LL..LL.L.......L.L.L.LL.L.L.L....
.LLLLLLLLLLLL.LL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLL.LLLL..LLLLLLLLLLLL..LLLLLLLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL..LLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.L.L.LLLLLLLLLLLLL.LLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL..LLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLL
LLLLL..LLLL.LLLLLLLL.L.LLLLLLL.LLL.L..LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLL.LLL
LLLL..LLL.L...LLLLLL.LL.LLLLLL.LLLL.LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LL.LL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLLLLLLLLLLLL..LLLLLLL.LLLLLL.LLLL.LLLL.LLLLLLLLL.LLLLLL.LLL...LLLLLL.LLLLLLLL
....LLL.......L...LL.L..........L....LLL.L.LL..L..L........LLL..LL...L......L..LLL..L....L.....
LLLLL.LLLLLLLL.LLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLL.LL.LL.LL.LLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLL.LLL.LLL.LLLLL.LLLLL.LLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLLLLLLLLLLLLLL.L
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL...LLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LL.LLLLLLLLLLLLLLLLLLL..LLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLLLL
LLLLLLLLLLLLLLLLL.LL.LLLLLLLLL.LLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LL.LL.LLLLLLLLL
LLLLL.LLLLL.LL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLL.L.LLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLL.LLLL..LL.LL.LLLLL.LLLLL.LLLLLLLLL
.LL.L...LLLL..L..L..LL...LL....LL..L...LL.L..L...L...L.................LLL....L..L...L.LLL..L..
LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLL.LLLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLLL.LLLLLL.LL.LLL.LLLLLLLLLLLL..L.LLLLLLLLLLLLLLLLLL
LLL.L.LLL.LLLLLL.LLL.LL.LL.LLLLL.LLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLLL
LLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLL..LLLLLLL.L.LLLLLLLLL.LLLLLL.LLLLL.LLLL..LLLLLLLLL
LLLLL.L.LLLLLLLL.LL..LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLL.L.LLLL.LLLLL.LLLLLLLLLLLLLLL
LLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLLLLLLLLLLLLL.LLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LL.L.LLL..LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLL.LLLLLLLLL
LL.L....L.L..........L...L.L.......LL......L.LL...LL.....L.L.L...L....LL.L..L......L..LL..L....
LLLLL.LLLLL.LLLLLLLL..LLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.L.LLL.LLLLLLLLL
L.LLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLL.LLLLL.LLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLL.LLLLLLLLL
LLLL.LLLLLLLLLLLLLLL.LLLLL.LLL.LL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLL.LLLLL..LL
LLLLL.LLLLL.LL.LLLLL..LLLLL.LL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLL.LLLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.L.LL.LLLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLL.LLLLL.LLLLLLLLL
........L....LLL.L....L...L...L.LL.......L..L..L.LL.L.L.L..L...L..L..L.........LLL.....LL.L..L.
LLLLL.LL.LL.LLLLLLLLLLLLLLLLLL.L.LLL..LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLL..L.LLL.LL
LLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL..LLLLLLLL.LL.LLLLL.LLLLLLLLL
LLLLL.LLLLLLLLLLLLLL.LLLLL..LL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLL.L.LLLLLLL
LLLLL.LLLLL.LLLLLL.L.LLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.L.L.LL.LLLL.LLLLLLLLL
LLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.L.LLLL.LLLLLLLLLLL.LLLLLLLLL
LLLLLLLLLLL.LLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLLLLLLL.LLLLLLLLL
LLLLL.L.LLL.LLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLL
LLLLL.LLLLL.LLLLLLLL.L.LLLLLLL.LLLLLLLLLL.LLLL.LLLL.LLLL.LLLLLLLLL.LLLLLL..LLLL.LLLLL.LLLLLLLLL
...L.....LL.L...L......LL..L.....LL.L...L..L...L....L......L....L......L.LL..L........L.......L
LLLLLLLL..L.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLL..LLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLL.L.LLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLL.LL..LLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLL.L
LLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL..LLLLLLLLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLL.LLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL
....L..L....L....L..L..LL.L......LL..LLL..L.L.L.LL......L.LLLL.L...LLL...L.....L.L.L.L.LLLL....
L.LLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLL..LLLL.LLL..LLLLLLLLL.LLLLLLLLLLL..LLLLLLLLLLLL.LL
L.L.L.LLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL..LLLLLLLLL.LLLLLL.L..LL.LLLLL.LLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLL.LLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLL..LLLLLLLLLLLL.LLLLL.LLL
LLLLL.LLLLLLLLLLLL...LLL.LLLLLLLLLLL.LLLLLLLLL.LLLLL.LLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLL
LLLLL.LLLLL.LL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL..LLLLLLLL
.L.LLLL..L.........LLL...L..L.L..LLL....LL...L..L......LL...L...L...L...L.....LLL.L...L.L..LLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLL.LLLLLLLLLLLL.L.LLLLLLLLLL.L.LL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLL.LLLLLLLLL.L.LLLLLLLLL
LLLLLLL.LLL.L.LLLLLL.LLLLLLLLL.L.LLL.LLLLLLLLL..LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL
LLLLL.LLLLL.LLLLL.LL.LLLLLLLLL.L.LLL.L.LLLLLLLLLL.LLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL
LLLLL.L.L.LLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LL.L.LLL.LLLLLLLLLLLL.LL.LL.LL.LLLLLLLLLLLL
LLLLL.LLLLL.LLLLLLL..LLLLLLL.L.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLL.LLLLLLLLL
LLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLL..LLLLLLLLL.LLLLLLLL..LLLL.LLLL.LLLLLLLLL.LL.LLLLL.LLLLLLLLL
LLLLL.LLLLL.LLLLLLLL.LL.LLL.LL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLL.LLLLLLLL.LLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL
.L.....L..LL.L.L.L.LL.L.L..L...L...L....LL.L..L.L..L...L..L.L.L..L........L.L.L.L..L.LL.L.L....
LLLLL.LLLLL.LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLL..LLLLLLLL.LL.LLLLLLLLL.LLLLLLLLLLLLLLL
LLLLL.LLLLL.LLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLL.LLLLLLLLLL.L.LLLLL.LL.LL.LLLLLLLLL
LLLL.LLLLLL.LLLLLLL..LL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLL.LLLLL..LLLL.LLLLLLLLL
.LLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL
LLLLLLLLLLLLLL.LLLLL.L.LLLLLLL.LLLLL..LLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLL.LL..LLLLL
LLLLL.LLLLLLL.L.LLLL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLL..LLLLL.LLLL.LLL.
LLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLL.LLLLL.LLL
..L..LLLL....L...L.L.L....L.....LL..L.....L..L............L.L....L.L..L.LL...L.L........L...L..
LLLLL..LLLLLLLL.LLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLL..LLL.LLLL
LLLLL.LLLLL.LLLLLLLL.LLLLLL.LL.LLLLLLL.LLLLLLL.LLLLLLLLL.LL.LLL.LL.LLLLLL..LLLL.LLLLLLLLLLLLLLL
LLLLL.LLLLLLLL.LLLLL.LL.LLLLL..LLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLL
LLLLL.LLL.LLLLLLLLL..LLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.LLLLL.LLLLLLLLL
LLLLL.LLLLL.L.LLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LL.LL.LLLL.LLLL
"

# COMMAND ----------

seat_str <- read_lines(input)

seats <-
  seat_str %>%
  str_c(collapse = "") %>%
  str_split('') %>%
  unlist() %>%
  matrix(ncol = nchar(seat_str[[1]]), byrow = TRUE)
seats

# COMMAND ----------

left <- function(m) matrixcalc::shift.left(m, fill = NA_integer_)
right <- function(m) matrixcalc::shift.right(m, fill = NA_integer_)
up <- function(m) matrixcalc::shift.up(m, fill = NA_integer_)
down <- function(m) matrixcalc::shift.down(m, fill = NA_integer_)

# COMMAND ----------

inds <- matrix(seq_along(unlist(seats)), ncol = ncol(seats))

N <- down(inds)
NE <- compose(left, down)(inds)
E <- left(inds)
SE <- compose(left, up)(inds)
S <- up(inds)
SW <- compose(right, up)(inds)
W <- right(inds)
NW <- compose(right, down)(inds)

# COMMAND ----------

update <- function(seats) {
  repeat {
    occupied_neighbors <-
      (!is.na(seats[N ]) & seats[N ] == "#") + 
      (!is.na(seats[NE]) & seats[NE] == "#") + 
      (!is.na(seats[E ]) & seats[E ] == "#") + 
      (!is.na(seats[SE]) & seats[SE] == "#") + 
      (!is.na(seats[S ]) & seats[S ] == "#") + 
      (!is.na(seats[SW]) & seats[SW] == "#") + 
      (!is.na(seats[W ]) & seats[W ] == "#") + 
      (!is.na(seats[NW]) & seats[NW] == "#")

    new_occupied <- seats == "L" & occupied_neighbors == 0
    new_empty <- seats == "#" & occupied_neighbors >= 4
    
    if (all(!new_occupied & !new_empty)) {
      break
    }
    
    seats[new_occupied] <- "#"
    seats[new_empty] <- "L"
  }
  seats
}

answer <- sum(update(seats) == "#")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about <em>the first seat they can see</em> in each of those eight directions!</p>
# MAGIC <p>Now, instead of considering just the eight immediately adjacent seats, consider the <em>first seat</em> in each of those eight directions. For example, the empty seat below would see <em>eight</em> occupied seats:</p>
# MAGIC <pre><code>.......#.
# MAGIC ...#.....
# MAGIC .#.......
# MAGIC .........
# MAGIC ..#L....#
# MAGIC ....#....
# MAGIC .........
# MAGIC #........
# MAGIC ...#.....
# MAGIC </code></pre>
# MAGIC <p>The leftmost empty seat below would only see <em>one</em> empty seat, but cannot see any of the occupied ones:</p>
# MAGIC <pre><code>.............
# MAGIC .L.L.#.#.#.#.
# MAGIC .............
# MAGIC </code></pre>
# MAGIC <p>The empty seat below would see <em>no</em> occupied seats:</p>
# MAGIC <pre><code>.##.##.
# MAGIC #.#.#.#
# MAGIC ##...##
# MAGIC ...L...
# MAGIC ##...##
# MAGIC #.#.#.#
# MAGIC .##.##.
# MAGIC </code></pre>
# MAGIC <p>Also, people seem to be more tolerant than you expected: it now takes <em>five or more</em> visible occupied seats for an occupied seat to become empty (rather than <em>four or more</em> from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.</p>
# MAGIC <p>Given the same starting layout as above, these new rules cause the seating area to shift around as follows:</p>
# MAGIC <pre><code>L.LL.LL.LL
# MAGIC LLLLLLL.LL
# MAGIC L.L.L..L..
# MAGIC LLLL.LL.LL
# MAGIC L.LL.LL.LL
# MAGIC L.LLLLL.LL
# MAGIC ..L.L.....
# MAGIC LLLLLLLLLL
# MAGIC L.LLLLLL.L
# MAGIC L.LLLLL.LL
# MAGIC </code></pre>
# MAGIC <pre><code>#.##.##.##
# MAGIC #######.##
# MAGIC #.#.#..#..
# MAGIC ####.##.##
# MAGIC #.##.##.##
# MAGIC #.#####.##
# MAGIC ..#.#.....
# MAGIC ##########
# MAGIC #.######.#
# MAGIC #.#####.##
# MAGIC </code></pre>
# MAGIC <pre><code>#.LL.LL.L#
# MAGIC #LLLLLL.LL
# MAGIC L.L.L..L..
# MAGIC LLLL.LL.LL
# MAGIC L.LL.LL.LL
# MAGIC L.LLLLL.LL
# MAGIC ..L.L.....
# MAGIC LLLLLLLLL#
# MAGIC #.LLLLLL.L
# MAGIC #.LLLLL.L#
# MAGIC </code></pre>
# MAGIC <pre><code>#.L#.##.L#
# MAGIC #L#####.LL
# MAGIC L.#.#..#..
# MAGIC ##L#.##.##
# MAGIC #.##.#L.##
# MAGIC #.#####.#L
# MAGIC ..#.#.....
# MAGIC LLL####LL#
# MAGIC #.L#####.L
# MAGIC #.L####.L#
# MAGIC </code></pre>
# MAGIC <pre><code>#.L#.L#.L#
# MAGIC #LLLLLL.LL
# MAGIC L.L.L..#..
# MAGIC ##LL.LL.L#
# MAGIC L.LL.LL.L#
# MAGIC #.LLLLL.LL
# MAGIC ..L.L.....
# MAGIC LLLLLLLLL#
# MAGIC #.LLLLL#.L
# MAGIC #.L#LL#.L#
# MAGIC </code></pre>
# MAGIC <pre><code>#.L#.L#.L#
# MAGIC #LLLLLL.LL
# MAGIC L.L.L..#..
# MAGIC ##L#.#L.L#
# MAGIC L.L#.#L.L#
# MAGIC #.L####.LL
# MAGIC ..#.#.....
# MAGIC LLL###LLL#
# MAGIC #.LLLLL#.L
# MAGIC #.L#LL#.L#
# MAGIC </code></pre>
# MAGIC <pre><code>#.L#.L#.L#
# MAGIC #LLLLLL.LL
# MAGIC L.L.L..#..
# MAGIC ##L#.#L.L#
# MAGIC L.L#.LL.L#
# MAGIC #.LLLL#.LL
# MAGIC ..#.L.....
# MAGIC LLL###LLL#
# MAGIC #.LLLLL#.L
# MAGIC #.L#LL#.L#
# MAGIC </code></pre>
# MAGIC <p>Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count <em><code>26</code></em> occupied seats.</p>
# MAGIC <p>Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, <em>how many seats end up occupied?</em></p>
# MAGIC </article>

# COMMAND ----------

offsets <- function(m, f) {
  result <- matrix(NA_integer_, nrow = nrow(m), ncol = ncol(m))
  repeat {
    m <- f(m)
    if (all(is.na(m))) {
      break
    }
    result[is.na(result)] <- m[is.na(result)]
  }
  result
}

# COMMAND ----------

inds <- matrix(seq_along(unlist(seats)), ncol = ncol(seats))
inds[seats == "."] <- NA

N <- offsets(inds, down)
NE <- offsets(inds, compose(left, down))
E <- offsets(inds, left)
SE <- offsets(inds, compose(left, up))
S <- offsets(inds, up)
SW <- offsets(inds, compose(right, up))
W <- offsets(inds, right)
NW <- offsets(inds, compose(right, down))

# COMMAND ----------

update <- function(seats) {
  repeat {
    occupied_neighbors <-
      (!is.na(seats[N ]) & seats[N ] == "#") + 
      (!is.na(seats[NE]) & seats[NE] == "#") + 
      (!is.na(seats[E ]) & seats[E ] == "#") + 
      (!is.na(seats[SE]) & seats[SE] == "#") + 
      (!is.na(seats[S ]) & seats[S ] == "#") + 
      (!is.na(seats[SW]) & seats[SW] == "#") + 
      (!is.na(seats[W ]) & seats[W ] == "#") + 
      (!is.na(seats[NW]) & seats[NW] == "#")

    new_occupied <- seats == "L" & occupied_neighbors == 0
    new_empty <- seats == "#" & occupied_neighbors >= 5
    
    if (all(!new_occupied & !new_empty)) {
      break
    }
    
    seats[new_occupied] <- "#"
    seats[new_empty] <- "L"
  }
  seats
}

# COMMAND ----------

result <- update(seats)
result

# COMMAND ----------

answer <- sum(result == "#")
answer
