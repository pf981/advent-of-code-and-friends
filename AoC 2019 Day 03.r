# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/3

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 3: Crossed Wires ---</h2><p>The gravity assist was successful, and you're well on your way to the Venus refuelling station.  During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.</p>
# MAGIC <p>Opening the front panel reveals a jumble of wires. Specifically, <em>two wires</em> are connected to a central port and extend outward on a grid.  You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).</p>
# MAGIC <p>The wires <span title="A jumble of twisty little wires, all alike.">twist and turn</span>, but the two wires occasionally cross paths. To fix the circuit, you need to <em>find the intersection point closest to the central port</em>. Because the wires are on a grid, use the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a> for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.</p>
# MAGIC <p>For example, if the first wire's path is <code>R8,U5,L5,D3</code>, then starting from the central port (<code>o</code>), it goes right <code>8</code>, up <code>5</code>, left <code>5</code>, and finally down <code>3</code>:</p>
# MAGIC <pre><code>...........
# MAGIC ...........
# MAGIC ...........
# MAGIC ....+----+.
# MAGIC ....|....|.
# MAGIC ....|....|.
# MAGIC ....|....|.
# MAGIC .........|.
# MAGIC .o-------+.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>Then, if the second wire's path is <code>U7,R6,D4,L4</code>, it goes up <code>7</code>, right <code>6</code>, down <code>4</code>, and left <code>4</code>:</p>
# MAGIC <pre><code>...........
# MAGIC .+-----+...
# MAGIC .|.....|...
# MAGIC .|..+--X-+.
# MAGIC .|..|..|.|.
# MAGIC .|.-<em>X</em>--+.|.
# MAGIC .|..|....|.
# MAGIC .|.......|.
# MAGIC .o-------+.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>These wires cross at two locations (marked <code>X</code>), but the lower-left one is closer to the central port: its distance is <code>3 + 3 = 6</code>.</p>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <ul>
# MAGIC <li><code>R75,D30,R83,U83,L12,D49,R71,U7,L72<br>U62,R66,U55,R34,D71,R55,D58,R83</code> = distance <code>159</code></li>
# MAGIC <li><code>R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51<br>U98,R91,D20,R16,D67,R40,U7,R15,U6,R7</code> = distance <code>135</code></li>
# MAGIC </ul>
# MAGIC <p><em>What is the Manhattan distance</em> from the central port to the closest intersection?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "R998,U367,R735,U926,R23,U457,R262,D473,L353,U242,L930,U895,R321,U683,L333,U623,R105,D527,R437,D473,L100,D251,L958,U384,R655,U543,L704,D759,R529,D176,R835,U797,R453,D650,L801,U437,L468,D841,R928,D747,L803,U677,R942,D851,R265,D684,L206,U763,L566,U774,L517,U337,L86,D585,R212,U656,L799,D953,L24,U388,L465,U656,L467,U649,R658,U519,L966,D290,L979,D819,R208,D907,R941,D458,L882,U408,R539,D939,R557,D771,L448,U460,L586,U148,R678,U360,R715,U312,L12,D746,L958,U216,R275,D278,L368,U663,L60,D543,L605,D991,L369,D599,R464,D387,L835,D876,L810,U377,L521,U113,L803,U680,L732,D449,R891,D558,L25,U249,L264,U643,L544,U504,R876,U403,R950,U19,L224,D287,R28,U914,R906,U970,R335,U295,R841,D810,R891,D596,R451,D79,R924,U823,L724,U968,R342,D349,R656,U373,R864,U374,L401,D102,L730,D886,R268,D188,R621,U258,L788,U408,L199,D422,R101,U368,L636,U543,R7,U722,L533,U242,L340,D195,R158,D291,L84,U936,L570,D937,L321,U947,L707,U32,L56,U650,L427,U490,L472,U258,R694,U87,L887,U575,R826,D398,R602,U794,R855,U225,R435,U591,L58,U281,L834,D400,R89,D201,L328,U278,L494,D70,L770,D182,L251,D44,R753,U431,R573,D71,R809,U983,L159,U26,R540,U516,R5,D23,L603,U65,L260,D187,R973,U877,R110,U49,L502,D68,R32,U153,R495,D315,R720,D439,R264,D603,R717,U586,R732,D111,R997,U578,L243,U256,R147,D425,L141,U758,R451,U779,R964,D219,L151,D789,L496,D484,R627,D431,R433,D761,R355,U975,L983,U364,L200,U578,L488,U668,L48,D774,R438,D456,L819,D927,R831,D598,L437,U979,R686,U930,L454,D553,L77,D955,L98,U201,L724,U211,R501,U492,L495,U732,L511
L998,U949,R912,D186,R359,D694,L878,U542,L446,D118,L927,U175,R434,U473,R147,D54,R896,U890,R300,D537,R254,D322,R758,D690,R231,U269,R288,U968,R638,U192,L732,D355,R879,U451,R336,D872,L141,D842,L126,U584,L973,D940,R890,D75,L104,U340,L821,D590,R577,U859,L948,D199,L872,D751,L368,U506,L308,U827,R181,U94,R670,U901,R739,D48,L985,D801,R722,D597,R654,D606,R183,U646,R939,U677,R32,U936,L541,D934,R316,U354,L415,D930,R572,U571,R147,D609,L534,D406,R872,D527,L816,D960,R652,D429,L402,D858,R374,D930,L81,U106,R977,U251,R917,U966,R353,U732,L613,U280,L713,D937,R481,U52,R746,U203,L500,D557,L209,U249,R89,D58,L149,U872,R331,D460,R343,D423,R392,D160,L876,U981,L399,D642,R525,U515,L537,U113,R886,D516,L301,D680,L236,U399,R460,D869,L942,D280,R669,U476,R683,D97,R199,D444,R137,D489,L704,D120,R753,D100,L737,U375,L495,D325,R48,D269,R575,U895,L184,D10,L502,D610,R618,D744,R585,U861,R695,D775,L942,U64,L819,U161,L332,U513,L461,D366,R273,D493,L197,D97,L6,U63,L564,U59,L699,U30,L68,U861,R35,U564,R540,U371,L115,D595,L412,D781,L185,D41,R207,D264,R999,D799,R421,D117,R377,D571,R268,D947,R77,D2,R712,D600,L516,U389,L868,D762,L996,U205,L178,D339,L844,D629,R67,D732,R109,D858,R630,U470,L121,D542,L751,U353,L61,U770,R952,U703,R264,D537,L569,U55,L795,U389,R836,U166,R585,U275,L734,U966,L130,D357,L260,U719,L647,D606,R547,U575,R791,U686,L597,D486,L774,U386,L163,U912,L234,D238,L948,U279,R789,U300,R117,D28,L833,U835,L340,U693,R343,D573,R882,D241,L731,U812,R600,D663,R902,U402,R831,D802,L577,U920,L947,D538,L192
"

# COMMAND ----------

wire_path <-
  read_lines(input) %>%
  str_split(",")
wire_path

# COMMAND ----------

get_points <- function(directions, start_x = 0, start_y = 0) {
  d <- parse_number(directions)
  direction <- str_sub(directions, 1, 1)
  
  add_x <- 0
  add_y <- 0
  
  if (direction == 'R') {
    add_x <- d
  } else if (direction == 'L') {
    add_x <- -d
  } else if (direction == 'U') {
    add_y <- d
  } else if (direction == 'D') {
    add_y <- -d
  } else {
    stop('Unknown direction ', direction)
  }
  
  tibble(
    x = start_x + seq(from = 0, to = add_x),
    y = start_y + seq(from = 0, to = add_y)
  ) %>%
    slice(-1)
}

get_all_points <- function(path) {
  start_x <- 0
  start_y <- 0
  points <- data.frame(x = 0, y = 0)
  for (direction in path) {
    points <- bind_rows(points, get_points(direction, last(points$x), last(points$y)))
  }
  points %>% slice(-1)
}

# COMMAND ----------

p1 <- get_all_points(wire_path[[1]])
p2 <- get_all_points(wire_path[[2]])

# COMMAND ----------

answer <-
  inner_join(p1, p2) %>%
  filter(!(x == 0 & y == 0)) %>%
  mutate(distance = abs(x) + abs(y)) %>%
  pull(distance) %>%
  min()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It turns out that this circuit is very timing-sensitive; you actually need to <em>minimize the signal delay</em>.</p>
# MAGIC <p>To do this, calculate the <em>number of steps</em> each wire takes to reach each intersection; choose the intersection where the <em>sum of both wires' steps</em> is lowest. If a wire visits a position on the grid multiple times, use the steps value from the <em>first</em> time it visits that position when calculating the total value of a specific intersection.</p>
# MAGIC <p>The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:</p>
# MAGIC <pre><code>...........
# MAGIC .+-----+...
# MAGIC .|.....|...
# MAGIC .|..+--X-+.
# MAGIC .|..|..|.|.
# MAGIC .|.-X--+.|.
# MAGIC .|..|....|.
# MAGIC .|.......|.
# MAGIC .o-------+.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>In the above example, the intersection closest to the central port is reached after <code>8+5+5+2 = <em>20</em></code> steps by the first wire and <code>7+6+4+3 = <em>20</em></code> steps by the second wire for a total of <code>20+20 = <em>40</em></code> steps.</p>
# MAGIC <p>However, the top-right intersection is better: the first wire takes only <code>8+5+2 = <em>15</em></code> and the second wire takes only <code>7+6+2 = <em>15</em></code>, a total of <code>15+15 = <em>30</em></code> steps.</p>
# MAGIC <p>Here are the best steps for the extra examples from above:</p>
# MAGIC <ul>
# MAGIC <li><code>R75,D30,R83,U83,L12,D49,R71,U7,L72<br>U62,R66,U55,R34,D71,R55,D58,R83</code> = <code>610</code> steps</li>
# MAGIC <li><code>R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51<br>U98,R91,D20,R16,D67,R40,U7,R15,U6,R7</code> = <code>410</code> steps</li>
# MAGIC </ul>
# MAGIC <p><em>What is the fewest combined steps the wires must take to reach an intersection?</em></p>
# MAGIC </article>

# COMMAND ----------

answer <-
  inner_join(
    p1 %>% mutate(d1 = row_number()),
    p2 %>% mutate(d2 = row_number())
  ) %>%
  mutate(distance = d1 + d2) %>%
  pull(distance) %>%
  min()
answer
