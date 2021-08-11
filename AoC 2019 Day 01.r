# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/1

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 1: The Tyranny of the Rocket Equation ---</h2><p>Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him <span title="If only you had time to grab an astrolabe.">measurements</span> from <em class="star">fifty stars</em>.</p>
# MAGIC <p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
# MAGIC <p>The Elves quickly load you into a spacecraft and prepare to launch.</p>
# MAGIC <p>At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.  They haven't determined the amount of fuel required yet.</p>
# MAGIC <p>Fuel required to launch a given <em>module</em> is based on its <em>mass</em>.  Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>For a mass of <code>12</code>, divide by 3 and round down to get <code>4</code>, then subtract 2 to get <code>2</code>.</li>
# MAGIC <li>For a mass of <code>14</code>, dividing by 3 and rounding down still yields <code>4</code>, so the fuel required is also <code>2</code>.</li>
# MAGIC <li>For a mass of <code>1969</code>, the fuel required is <code>654</code>.</li>
# MAGIC <li>For a mass of <code>100756</code>, the fuel required is <code>33583</code>.</li>
# MAGIC </ul>
# MAGIC <p>The Fuel Counter-Upper needs to know the total fuel requirement.  To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.</p>
# MAGIC <p><em>What is the sum of the fuel requirements</em> for all of the modules on your spacecraft?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "57351
149223
142410
129063
91757
52486
125555
124161
104558
110002
140284
131259
142148
69648
73179
89820
125606
70238
131217
99388
71989
126743
55136
128148
52974
131314
82350
126565
54418
105347
71981
146156
113626
117829
55419
91350
137748
113160
102462
100948
101731
131526
139132
51796
100849
122579
132301
51675
86607
140890
77532
81217
149549
113161
119361
109709
64495
103062
72313
140119
77352
91658
141341
91664
64771
88263
102357
149925
123608
88368
57809
65165
63937
78600
134725
58438
62763
131789
119646
65649
143975
142866
97922
64427
149451
84896
75863
53950
55625
146904
50460
99284
125904
85856
60281
79113
111661
145106
105568
147400
"

# COMMAND ----------

modules <- 
  input %>%
  read_table(col_names = FALSE) %>%
  pull()

# COMMAND ----------

answer <- sum(modules %/% 3 - 2)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence.  Apparently, you forgot to include additional fuel for the fuel you just added.</p>
# MAGIC <p>Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2.  However, that fuel <em>also</em> requires fuel, and <em>that</em> fuel requires fuel, and so on.  Any mass that would require <em>negative fuel</em> should instead be treated as if it requires <em>zero fuel</em>; the remaining mass, if any, is instead handled by <em>wishing really hard</em>, which has no mass and is outside the scope of this calculation.</p>
# MAGIC <p>So, for each module mass, calculate its fuel and add it to the total.  Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:</p>
# MAGIC <ul>
# MAGIC <li>A module of mass <code>14</code> requires <code>2</code> fuel.  This fuel requires no further fuel (2 divided by 3 and rounded down is <code>0</code>, which would call for a negative fuel), so the total fuel required is still just <code>2</code>.</li>
# MAGIC <li>At first, a module of mass <code>1969</code> requires <code>654</code> fuel.  Then, this fuel requires <code>216</code> more fuel (<code>654 / 3 - 2</code>).  <code>216</code> then requires <code>70</code> more fuel, which requires <code>21</code> fuel, which requires <code>5</code> fuel, which requires no further fuel.  So, the total fuel required for a module of mass <code>1969</code> is <code>654 + 216 + 70 + 21 + 5 = 966</code>.</li>
# MAGIC <li>The fuel required by a module of mass <code>100756</code> and its fuel is: <code>33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346</code>.</li>
# MAGIC </ul>
# MAGIC <p><em>What is the sum of the fuel requirements</em> for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)</p>
# MAGIC </article>

# COMMAND ----------

calc_fuel <- function(module) {
  module %/% 3 - 2
}

calc_fuel_full <- function(module) {
  total_fuel <- 0
  fuel <- calc_fuel(module)
  while (fuel > 0) {
    total_fuel <- total_fuel + fuel
    fuel <- calc_fuel(fuel)
  }
  as.integer(total_fuel)
}

# COMMAND ----------

answer <-
  modules %>%
  map_int(calc_fuel_full) %>%
  sum()
answer
