# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 17: No Such Thing as Too Much ---</h2><p>The elves bought too much eggnog again - <code>150</code> liters this time.  To fit it all into your refrigerator, you'll need to move it into smaller containers.  You take an inventory of the capacities of the available containers.</p>
# MAGIC <p>For example, suppose you have containers of size <code>20</code>, <code>15</code>, <code>10</code>, <code>5</code>, and <code>5</code> liters.  If you need to store <code>25</code> liters, there are four ways to do it:</p>
# MAGIC <ul>
# MAGIC <li><code>15</code> and <code>10</code></li>
# MAGIC <li><code>20</code> and <code>5</code> (the first <code>5</code>)</li>
# MAGIC <li><code>20</code> and <code>5</code> (the second <code>5</code>)</li>
# MAGIC <li><code>15</code>, <code>5</code>, and <code>5</code></li>
# MAGIC </ul>
# MAGIC <p>Filling all containers entirely, how many different <em>combinations of containers</em> can exactly fit all <code>150</code> liters of eggnog?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38
"

# COMMAND ----------

items <- read_lines(input) %>% parse_number()
items

# COMMAND ----------

ways_to_fill <- function(items, capacity) {
  if (capacity == 0) {
    return(1)
  }
  if (capacity < 0) {
    return(0)
  }
  
  result <- 0
  for (item in items) {
    items <- items[items != item | duplicated(items)]
    result <- result + ways_to_fill(
      items,
      capacity - item
    )
  }
  result
}

# COMMAND ----------

ways_to_fill(items, 150)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>While playing with all the containers in the kitchen, another load of eggnog <span title="Apparently, Amazon ships to the North Pole now.">arrives</span>!  The shipping and receiving department is requesting as many containers as you can spare.</p>
# MAGIC <p>Find the minimum number of containers that can exactly fit all <code>150</code> liters of eggnog.  <em>How many different ways</em> can you fill that number of containers and still hold exactly <code>150</code> litres?</p>
# MAGIC <p>In the example above, the minimum number of containers was two.  There were three ways to use that many containers, and so the answer there would be <code>3</code>.</p>
# MAGIC <p></p>
# MAGIC </article>

# COMMAND ----------

ways_to_fill_min <- function(items, capacity, n_containers = 0) {
  if (capacity == 0) {
    return(lst(n_containers, n_ways = 1))
  }
  if (capacity < 0) {
    return(lst(n_containers, n_ways = 0))
  }
  
  cur_n_ways <- 0
  cur_n_containers <- Inf
  for (item in items) {
    items <- items[items != item | duplicated(items)]
    output <- ways_to_fill_min(
      items,
      capacity - item,
      n_containers + 1
    )
    
    if (output$n_containers == cur_n_containers) {
      cur_n_ways <- cur_n_ways + output$n_ways
    } else if (output$n_containers < cur_n_containers && output$n_ways > 0) {
      cur_n_ways <- output$n_ways
      cur_n_containers <- output$n_containers
    }
  }
  lst(
    n_containers = cur_n_containers,
    n_ways = cur_n_ways,
  )
}

# COMMAND ----------

result <- ways_to_fill_min(items, 150)
result

# COMMAND ----------

answer <- result$n_ways
answer
