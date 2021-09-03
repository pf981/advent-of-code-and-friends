# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/2

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 2: Bathroom Security ---</h2><p>You arrive at <em>Easter Bunny Headquarters</em> under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.</p>
# MAGIC <p>"In order to improve security," the document you find says, "bathroom codes will no longer be written down.  Instead, please memorize and follow the procedure below to access the bathrooms."</p>
# MAGIC <p>The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: <code>U</code> moves up, <code>D</code> moves down, <code>L</code> moves left, and <code>R</code> moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, <em>the "5" button</em>); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.</p>
# MAGIC <p>You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:</p>
# MAGIC <pre><code>1 2 3
# MAGIC 4 5 6
# MAGIC 7 8 9
# MAGIC </code></pre>
# MAGIC <p>Suppose your instructions are:</p>
# MAGIC <pre><code>ULL
# MAGIC RRDDD
# MAGIC LURDL
# MAGIC UUUUD
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is <code>1</code>.</li>
# MAGIC <li>Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with <code>9</code>.</li>
# MAGIC <li>Continuing from "9", you move left, up, right, down, and left, ending with <code>8</code>.</li>
# MAGIC <li>Finally, you move up four times (stopping at "2"), then down once, ending with <code>5</code>.</li>
# MAGIC </ul>
# MAGIC <p>So, in this example, the bathroom code is <code>1985</code>.</p>
# MAGIC <p>Your puzzle input is the instructions from the document you found at the front desk. What is the <em>bathroom code</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "UUURRRRULRDLRDRRDURDDDLLDLLLULDUDDLDLULUURULRLDLRRLLLRRDRRLDDLLULUDUDDLRDRDUURDLURUURLRULLDDURULRRURDUURLULUUUURDDDDUUDLULRULLLRLLRRRURDLLRLLRRRUURULRDRUUDDDDDLLLRURRURRUURDUURDDRDLULRRLLLDRRRLURRLLURLDRRDDLDLRRLLRDRLLLLDLULDLRRDRRLDDURLULLUDLUDRRDRRLRLULURDRLRLUUUDLRLDLLLURDUDULULDDRUUURLLLDLLDDUDDRURURUDDLUULRDRRRRLDRDDURLUDURDULLDLUDLULDRLRLLRLLLLRURDURLLDRRDRLRUUUUULLLRUDURUDLLLUDLLLLRDLDRDUDRURLUDDUDDURLUUUUDDLLUDLULLLLLDUDLLRLRRDDDULULRLDRLLULDLUDLLURULRDDUURULRDLDLDLRL
URUUURDULUDLUUUUDDRRRDRRRLDUDLRDRRDRDDLRUULDLLDUDULLLRLDRDRRLDLDLUUDRUULDUDULDUDURURDDURULDLURULRLULDUDDUULDLLLDDURDDRDDURUULUUDRLDDULDRRRRDURRUDLLLURDDDLRULLRDDRDDDDLUUDRDUULRRRRURULDDDLDDRDRRUDRRURUDRDDLDRRRLLURURUULUUDRDULLDRLRDRRDDURDUDLDRLUDRURDURURULDUUURDUULRRRRRUDLLULDDDRLULDDULUDRRRDDRUDRRDLDLRUULLLLRRDRRLUDRUULRDUDRDRRRDDRLLRUUDRLLLUDUDLULUUDULDRRRRDDRURULDULLURDLLLDUUDLLUDRLDURRRLDDDURUDUDURRULDD
LRUDDULLLULRLUDUDUDRLLUUUULLUDLUUUUDULLUURDLLRDUDLRUDRUDDURURRURUDLLLRLDLUDRRRRRRDLUURLRDDDULRRUDRULRDRDDUULRDDLDULDRRRDDLURRURLLLRURDULLRUUUDDUDUURLRLDDUURLRDRRLURLDRLLUUURDRUUDUUUDRLURUUUDLDRRLRLLRRUURULLLRLLDLLLDULDDLDULDLDDRUDURDDURDUDURDLLLRRDDLULLLUDURLUDDLDLUUDRDRUDUUDLLDDLLLLDRDULRDLDULLRUDDUULDUDLDDDRUURLDRRLURRDDRUUDRUDLLDLULLULUDUDURDDRLRDLRLDRLDDRULLLRUDULDRLRLRULLRLLRRRLLRRRDDRULRUURRLLLRULDLUDRRDDLLLUDDUDDDLURLUDRDLURUUDLLDLULURRLLDURUDDDDRLULRDDLRLDDLRLLDDRRLRDUDUUULRRLRULUDURDUDRLRLRUDUDLLRRRRLRRUDUL
RULLLLUUUDLLDLLRULLRURRULDDRDLUULDRLLRUDLLRRLRDURLLDUUUUURUUURDLUURRLDDDLRRRRLRULDUDDLURDRRUUDLRRRDLDDUDUDDRUDURURLDULLDLULDLLUDLULRDRLLURRLLDURLDLRDLULUDDULDLDDDDDUURRDRURLDLDULLURDLLDDLLUDLDLDRLRLDLRDRLDLRRUUDRURLUUUDLURUULDUDRDULLDURUDLUUURRRLLDUDUDDUUULLLRUULDLURUDDRLUDRDDLDLLUDUDRRRDDUUULUULLLRLLUURDUUDRUUULULLDLDRUUDURLLUULRLDLUURLLUUDRURDDRLURULDUDUUDRRUUURDULRLDUUDDRURURDRRULDDDRLUDLLUUDURRRLDLRLRDRURLURLLLRLDDLRRLDLDDURDUUDRDRRLDRLULDRLURUUUDDRLLLDDLDURLLLLDRDLDRRUDULURRLULRDRLLUULLRLRDRLLULUURRUDRUDDDLLDURURLURRRDLLDRDLUDRULULULRLDLRRRUUDLULDURLRDRLULRUUURRDDLRUURUDRURUDURURDD
DURRDLLLDDLLDLLRLULULLRDLDRRDDRDLRULURRDUUDDRLLDDLDRRLRDUDRULDLRURDUUDRDDLLDRRDRUDUDULLDDDDLDRRRLRLRDRDLURRDDLDDDUUDRDRLLLDLUDDDLUULRDRLLLRLLUULUDDDRLDUUUURULRDDURRDRLUURLUDRLRLLLDDLRDDUULRRRRURDLDDDRLDLDRRLLDRDDUDDUURDLDUUDRDLDLDDULULUDDLRDDRLRLDDLUDLLDRLUDUDDRULLRLDLLRULRUURDDRDRDRURDRRLRDLLUDDRRDRRLDDULLLDLUDRRUDLDULDRURRDURLURRLDLRDLRUDLULUDDRULRLLDUURULURULURRLURRUULRULRRRLRDLULRLRLUDURDDRUUURDRLLRRRDDLDRRRULLDLRDRULDRRLRRDLUDDRDDDUUURRLULLDRRUULULLRRRRLDDRDDLUURLLUDLLDUDLULUULUDLLUUURRRUDDDRLLLRDRUUDUUURDRULURRLRDLLUURLRDURULDRRUDURRDDLDRLDRUUDRLLUDLRRU
"

# COMMAND ----------

dial_number <- function(delta_x, delta_y) {
  x <- 2
  y <- 2
  result_x <- integer(length(delta_x))
  result_y <- integer(length(delta_y))
  
  for (i in seq_along(delta_x)){
    new_pos <- c(x + delta_x[i], y + delta_y[i])
    if (all(new_pos <= 3) && all(new_pos > 0)) {
      x <- new_pos[1]
      y <- new_pos[2]
    }
    
    result_x[i] <- x
    result_y[i] <- y
  }
  (result_y - 1) * 3 + result_x
}

# COMMAND ----------

x_coef <- c(U = 0, R = 1, D = 0, L = -1)
y_coef <- c(U = -1, R = 0, D = 1, L = 0)

instructions <-
  read_lines(input) %>%
  str_split("") %>%
  map_dfr(~tibble(direction = .), .id = "id") %>%
  mutate(
    number = dial_number(x_coef[direction], y_coef[direction])
  )

answer <-
  instructions %>%
  group_by(id) %>%
  slice(n()) %>%
  pull(number) %>%
  str_c(collapse = "")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code.  Much to your bladder's dismay, the keypad is not at all like you imagined it.  Instead, you are confronted with the result of hundreds of man-hours of <span title="User Group 143 found a diamond shape to be the most environmentally friendly.">bathroom-keypad-design meetings:</span></p>
# MAGIC <pre><code>    1
# MAGIC   2 3 4
# MAGIC 5 6 7 8 9
# MAGIC   A B C
# MAGIC     D
# MAGIC </code></pre>
# MAGIC <p>You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:</p>
# MAGIC <ul>
# MAGIC <li>You start at "5" and don't move at all (up and left are both edges), ending at <code>5</code>.</li>
# MAGIC <li>Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at <code>D</code>.</li>
# MAGIC <li>Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at <code>B</code>.</li>
# MAGIC <li>Finally, after five more moves, you end at <code>3</code>.</li>
# MAGIC </ul>
# MAGIC <p>So, given the actual keypad layout, the code would be <code>5DB3</code>.</p>
# MAGIC <p>Using the same instructions in your puzzle input, what is the correct <em>bathroom code</em>?</p>
# MAGIC </article>

# COMMAND ----------

diamond_number <- function(delta_x, delta_y) {
  x <- -2
  y <- 0
  result_x <- integer(length(delta_x))
  result_y <- integer(length(delta_y))
  
  for (i in seq_along(delta_x)){
    new_pos <- c(x + delta_x[i], y + delta_y[i])
    if (
      all(abs(new_pos) <= 2) &&
      sum(abs(new_pos)) <= 2
    ) {
      x <- new_pos[1]
      y <- new_pos[2]
    }
    
    result_x[i] <- x
    result_y[i] <- y
  }
  matrix(
    c(
      NA,  NA,   1,  NA, NA,
      NA,   2,   3,   4, NA,
       5,   6,   7,   8,  9,
      NA, "A", "B", "C", NA,
      NA,  NA, "D",  NA, NA
    ),
    ncol = 5,
    byrow = TRUE
  )[cbind(result_y + 3, result_x + 3)] %>% as.vector()
}

# COMMAND ----------

answer <-
  instructions %>%
  mutate(
    number = diamond_number(x_coef[direction], y_coef[direction])
  ) %>%
  group_by(id) %>%
  slice(n()) %>%
  pull(number) %>%
  str_c(collapse = "")
answer
