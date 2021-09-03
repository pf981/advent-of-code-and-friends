# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/13

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 13: Knights of the Dinner Table ---</h2><p>In years past, the holiday feast with your family hasn't gone so well.  Not everyone gets along!  This year, you resolve, will be different.  You're going to find the <em>optimal seating arrangement</em> and avoid all those awkward conversations.</p>
# MAGIC <p>You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person.  You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.</p>
# MAGIC <p>For example, suppose you have only four attendees planned, and you <span title="Finding a method to calculate happiness units is left as an exercise for the reader.">calculate</span> their potential happiness as follows:</p>
# MAGIC <pre><code>Alice would gain 54 happiness units by sitting next to Bob.
# MAGIC Alice would lose 79 happiness units by sitting next to Carol.
# MAGIC Alice would lose 2 happiness units by sitting next to David.
# MAGIC Bob would gain 83 happiness units by sitting next to Alice.
# MAGIC Bob would lose 7 happiness units by sitting next to Carol.
# MAGIC Bob would lose 63 happiness units by sitting next to David.
# MAGIC Carol would lose 62 happiness units by sitting next to Alice.
# MAGIC Carol would gain 60 happiness units by sitting next to Bob.
# MAGIC Carol would gain 55 happiness units by sitting next to David.
# MAGIC David would gain 46 happiness units by sitting next to Alice.
# MAGIC David would lose 7 happiness units by sitting next to Bob.
# MAGIC David would gain 41 happiness units by sitting next to Carol.
# MAGIC </code></pre>
# MAGIC <p>Then, if you seat Alice next to David, Alice would lose <code>2</code> happiness units (because David talks so much), but David would gain <code>46</code> happiness units (because Alice is such a good listener), for a total change of <code>44</code>.</p>
# MAGIC <p>If you continue around the table, you could then seat Bob next to Alice (Bob gains <code>83</code>, Alice gains <code>54</code>).  Finally, seat Carol, who sits next to Bob (Carol gains <code>60</code>, Bob loses <code>7</code>) and David (Carol gains <code>55</code>, David gains <code>41</code>).  The arrangement looks like this:</p>
# MAGIC <pre><code>     +41 +46
# MAGIC +55   David    -2
# MAGIC Carol       Alice
# MAGIC +60    Bob    +54
# MAGIC      -7  +83
# MAGIC </code></pre>
# MAGIC <p>After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of <code>330</code>.</p>
# MAGIC <p>What is the <em>total change in happiness</em> for the optimal seating arrangement of the actual guest list?</p>
# MAGIC </article>

# COMMAND ----------

install.packages("combinat")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Alice would lose 2 happiness units by sitting next to Bob.
Alice would lose 62 happiness units by sitting next to Carol.
Alice would gain 65 happiness units by sitting next to David.
Alice would gain 21 happiness units by sitting next to Eric.
Alice would lose 81 happiness units by sitting next to Frank.
Alice would lose 4 happiness units by sitting next to George.
Alice would lose 80 happiness units by sitting next to Mallory.
Bob would gain 93 happiness units by sitting next to Alice.
Bob would gain 19 happiness units by sitting next to Carol.
Bob would gain 5 happiness units by sitting next to David.
Bob would gain 49 happiness units by sitting next to Eric.
Bob would gain 68 happiness units by sitting next to Frank.
Bob would gain 23 happiness units by sitting next to George.
Bob would gain 29 happiness units by sitting next to Mallory.
Carol would lose 54 happiness units by sitting next to Alice.
Carol would lose 70 happiness units by sitting next to Bob.
Carol would lose 37 happiness units by sitting next to David.
Carol would lose 46 happiness units by sitting next to Eric.
Carol would gain 33 happiness units by sitting next to Frank.
Carol would lose 35 happiness units by sitting next to George.
Carol would gain 10 happiness units by sitting next to Mallory.
David would gain 43 happiness units by sitting next to Alice.
David would lose 96 happiness units by sitting next to Bob.
David would lose 53 happiness units by sitting next to Carol.
David would lose 30 happiness units by sitting next to Eric.
David would lose 12 happiness units by sitting next to Frank.
David would gain 75 happiness units by sitting next to George.
David would lose 20 happiness units by sitting next to Mallory.
Eric would gain 8 happiness units by sitting next to Alice.
Eric would lose 89 happiness units by sitting next to Bob.
Eric would lose 69 happiness units by sitting next to Carol.
Eric would lose 34 happiness units by sitting next to David.
Eric would gain 95 happiness units by sitting next to Frank.
Eric would gain 34 happiness units by sitting next to George.
Eric would lose 99 happiness units by sitting next to Mallory.
Frank would lose 97 happiness units by sitting next to Alice.
Frank would gain 6 happiness units by sitting next to Bob.
Frank would lose 9 happiness units by sitting next to Carol.
Frank would gain 56 happiness units by sitting next to David.
Frank would lose 17 happiness units by sitting next to Eric.
Frank would gain 18 happiness units by sitting next to George.
Frank would lose 56 happiness units by sitting next to Mallory.
George would gain 45 happiness units by sitting next to Alice.
George would gain 76 happiness units by sitting next to Bob.
George would gain 63 happiness units by sitting next to Carol.
George would gain 54 happiness units by sitting next to David.
George would gain 54 happiness units by sitting next to Eric.
George would gain 30 happiness units by sitting next to Frank.
George would gain 7 happiness units by sitting next to Mallory.
Mallory would gain 31 happiness units by sitting next to Alice.
Mallory would lose 32 happiness units by sitting next to Bob.
Mallory would gain 95 happiness units by sitting next to Carol.
Mallory would gain 91 happiness units by sitting next to David.
Mallory would lose 66 happiness units by sitting next to Eric.
Mallory would lose 75 happiness units by sitting next to Frank.
Mallory would lose 99 happiness units by sitting next to George.
"

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    a = str_extract(line, "^\\w+"),
    b = str_extract(line, "\\w+(?=\\.$)"),
    happiness = parse_number(line) * ifelse(str_detect(line, "would lose"), -1, 1),
    index = str_c(a, b)
  )
df

# COMMAND ----------

people <- df %>% pull(a) %>% unique()
people

# COMMAND ----------

standardize_start <- function(x) {
  start_i <- order(x)[1] - 1
  
  if (start_i == 0) {
    x
  } else {
    c(tail(x, -start_i), head(x, start_i))
  }
}

# COMMAND ----------

permutations <-
  combinat::permn(people) %>%
  map(standardize_start) %>%
  discard(duplicated(map_chr(., str_c, collapse = "")))

# COMMAND ----------

compute_happiness <- function(seating) {
  indices <- c(
    str_c(seating, lead(seating, default = first(seating))),
    str_c(seating, lag(seating, default = last(seating)))
  )
  df %>%
    filter(index %in% indices) %>%
    pull(happiness) %>%
    sum()
}

# COMMAND ----------

answer <- permutations %>% map_dbl(compute_happiness) %>% max()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>In all the commotion, you realize that you forgot to seat yourself.  At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to.  You assume everyone else would be just as ambivalent about sitting next to you, too.</p>
# MAGIC <p>So, add yourself to the list, and give all happiness relationships that involve you a score of <code>0</code>.</p>
# MAGIC <p>What is the <em>total change in happiness</em> for the optimal seating arrangement that actually includes yourself?</p>
# MAGIC </article>

# COMMAND ----------

new_rows <-
  bind_rows(
    tibble(
      a = people,
      b = "paul"
    ),
    tibble(
      a = "paul",
      b = people
    )
  ) %>%
  mutate(index = str_c(a, b), happiness = 0)

# COMMAND ----------

df <- bind_rows(df, new_rows)

# COMMAND ----------

people <- c(people, "paul")

# COMMAND ----------

permutations <-
  combinat::permn(people) %>%
  map(standardize_start) %>%
  discard(duplicated(map_chr(., str_c, collapse = "")))

# COMMAND ----------

answer <- permutations %>% map_dbl(compute_happiness) %>% max()
answer
