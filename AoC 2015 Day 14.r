# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 14: Reindeer Olympics ---</h2><p>This year is the Reindeer Olympics!  Reindeer can fly at high speeds, but must rest occasionally to recover their energy.  Santa would like to know which of his reindeer is fastest, and so he has them race.</p>
# MAGIC <p>Reindeer can only either be <em>flying</em> (always at their top speed) or <em>resting</em> (not moving at all), and always spend whole seconds in either state.</p>
# MAGIC <p>For example, suppose you have the following Reindeer:</p>
# MAGIC <ul>
# MAGIC <li>Comet can fly <em>14 km/s for 10 seconds</em>, but then must rest for <em>127 seconds</em>.</li>
# MAGIC <li>Dancer can fly <em>16 km/s for 11 seconds</em>, but then must rest for <em>162 seconds</em>.</li>
# MAGIC </ul>
# MAGIC <p>After one second, Comet has gone 14 km, while Dancer has gone 16 km.  After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.  On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km.  On the 12th second, both reindeer are resting.  They continue to rest until the 138th second, when Comet flies for another ten seconds.  On the 174th second, Dancer flies for another 11 seconds.</p>
# MAGIC <p>In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at <em><code>1120</code></em> km (poor Dancer has only gotten <code>1056</code> km by that point).  So, in this situation, Comet would win (if the race ended at 1000 seconds).</p>
# MAGIC <p>Given the descriptions of each reindeer (in your puzzle input), after exactly <code>2503</code> seconds, <em>what distance has the winning reindeer traveled</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.
"

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    reindeer = str_extract(line, "^\\w+"),
    speed = str_extract(line, "\\d+") %>% parse_number(),
    flight_time = str_extract(line, "(?<=for )\\d+") %>% parse_number(),
    rest_time = str_extract(line, "(?<=rest for )\\d+") %>% parse_number()
  )
df

# COMMAND ----------

t <- 2503

answer <-
  df %>%
  mutate(
    d_round = t %/% (flight_time + rest_time) * (flight_time * speed),
    d_extra = pmin(t %% (flight_time + rest_time), flight_time) * speed,
    d = d_round + d_extra
  ) %>%
  pull(d) %>%
  max()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.</p>
# MAGIC <p>Instead, at the end of each second, he awards one point to the reindeer currently in the lead.  (If there are multiple reindeer tied for the lead, they each get one point.)  He keeps the traditional 2503 second time limit, of course, as doing otherwise would be <span title="It also risks choosing a duration that isn't coprime with the cycle times of each reindeer.">entirely ridiculous</span>.</p>
# MAGIC <p>Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point.  He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point.  Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.</p>
# MAGIC <p>After the 1000th second, Dancer has accumulated <em><code>689</code></em> points, while poor Comet, our old champion, only has <code>312</code>.  So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).</p>
# MAGIC <p>Again given the descriptions of each reindeer (in your puzzle input), after exactly <code>2503</code> seconds, <em>how many points does the winning reindeer have</em>?</p>
# MAGIC </article>

# COMMAND ----------

answer <-
  df %>%
  crossing(t = seq_len(2503))  %>%
  mutate(
    d_round = t %/% (flight_time + rest_time) * (flight_time * speed),
    d_extra = pmin(t %% (flight_time + rest_time), flight_time) * speed,
    d = d_round + d_extra
  ) %>%
  group_by(t) %>%
  filter(d == max(d)) %>%
  ungroup() %>%
  count(reindeer) %>%
  pull(n) %>%
  max()
answer
