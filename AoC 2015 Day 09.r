# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 9: All in a Single Night ---</h2><p>Every year, Santa manages to deliver all of his presents in a single night.</p>
# MAGIC <p>This year, however, he has some <span title="Bonus points if you recognize all of the locations.">new locations</span> to visit; his elves have provided him the distances between every pair of locations.  He can start and end at any two (different) locations he wants, but he must visit each location exactly once.  What is the <em>shortest distance</em> he can travel to achieve this?</p>
# MAGIC <p>For example, given the following distances:</p>
# MAGIC <pre><code>London to Dublin = 464
# MAGIC London to Belfast = 518
# MAGIC Dublin to Belfast = 141
# MAGIC </code></pre>
# MAGIC <p>The possible routes are therefore:</p>
# MAGIC <pre><code>Dublin -&gt; London -&gt; Belfast = 982
# MAGIC London -&gt; Dublin -&gt; Belfast = 605
# MAGIC London -&gt; Belfast -&gt; Dublin = 659
# MAGIC Dublin -&gt; Belfast -&gt; London = 659
# MAGIC Belfast -&gt; Dublin -&gt; London = 605
# MAGIC Belfast -&gt; London -&gt; Dublin = 982
# MAGIC </code></pre>
# MAGIC <p>The shortest of these is <code>London -&gt; Dublin -&gt; Belfast = 605</code>, and so the answer is <code>605</code> in this example.</p>
# MAGIC <p>What is the distance of the shortest route?</p>
# MAGIC </article>

# COMMAND ----------

install.packages("combinat")

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46
"

# COMMAND ----------

df <-
  tibble(text = read_lines(input)) %>%
  separate(text, into = c("from", "to"), sep = " to ") %>%
  separate(to, into = c("to", "d"), sep = " = ", convert = TRUE) %>%
  mutate(
    lookup = ifelse(from < to, str_c(from, to), str_c(to, from))
  )

df

# COMMAND ----------

nodes <- c(df$from, df$to) %>% unique()
nodes

# COMMAND ----------

permutations <- combinat::permn(nodes)

# Remove reverse
# permutations <- permutations[order(map_chr(permutations, first))] %>% head(., length(.) / 2)

# COMMAND ----------

compute_distance <- function(route) {
  route_from <- head(route, -1)
  route_to <- head(lead(route), -1)
  route_lookup <- ifelse(route_from < route_to, str_c(route_from, route_to), str_c(route_to, route_from))

  df %>% filter(lookup %in% route_lookup) %>% pull(d) %>% sum()
}

distances <- map_int(permutations, compute_distance)

# COMMAND ----------



# COMMAND ----------

answer <- min(distances)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The next year, just to show off, Santa decides to take the route with the <em>longest distance</em> instead.</p>
# MAGIC <p>He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.</p>
# MAGIC <p>For example, given the distances above, the longest route would be <code>982</code> via (for example) <code>Dublin -&gt; London -&gt; Belfast</code>.</p>
# MAGIC <p>What is the distance of the longest route?</p>
# MAGIC </article>

# COMMAND ----------

# permutations %>%
#   map_int(compute_distance) %>%
#   max()

# COMMAND ----------

answer <- max(distances)
answer
