# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 24: Electromagnetic Moat ---</h2><p>The CPU itself is a large, black building surrounded by a bottomless pit. Enormous metal tubes extend outward from the side of the building at regular intervals and descend down into the void. There's no way to cross, but you need to get inside.</p>
# MAGIC <p>No way, of course, other than building a <em>bridge</em> out of the magnetic components strewn about nearby.</p>
# MAGIC <p>Each component has two <em>ports</em>, one on each end.  The ports come in all different types, and only matching types can be connected.  You take an inventory of the components by their port types (your puzzle input). Each port is identified by the number of <em>pins</em> it uses; more pins mean a stronger connection for your bridge. A <code>3/7</code> component, for example, has a type-<code>3</code> port on one side, and a type-<code>7</code> port on the other.</p>
# MAGIC <p>Your side of the pit is metallic; a perfect surface to connect a magnetic, <em>zero-pin port</em>. Because of this, the first port you use must be of type <code>0</code>. It doesn't matter what type of port you end with; your goal is just to make the bridge as strong as possible.</p>
# MAGIC <p>The <em>strength</em> of a bridge is the sum of the port types in each component. For example, if your bridge is made of components <code>0/3</code>, <code>3/7</code>, and <code>7/4</code>, your bridge has a strength of <code>0+3 + 3+7 + 7+4 = 24</code>.</p>
# MAGIC <p>For example, suppose you had the following components:</p>
# MAGIC <pre><code>0/2
# MAGIC 2/2
# MAGIC 2/3
# MAGIC 3/4
# MAGIC 3/5
# MAGIC 0/1
# MAGIC 10/1
# MAGIC 9/10
# MAGIC </code></pre>
# MAGIC <p>With them, you could make the following valid bridges:</p>
# MAGIC <ul>
# MAGIC <li><code>0/1</code></li>
# MAGIC <li><code>0/1</code>--<code>10/1</code></li>
# MAGIC <li><code>0/1</code>--<code>10/1</code>--<code>9/10</code></li>
# MAGIC <li><code>0/2</code></li>
# MAGIC <li><code>0/2</code>--<code>2/3</code></li>
# MAGIC <li><code>0/2</code>--<code>2/3</code>--<code>3/4</code></li>
# MAGIC <li><code>0/2</code>--<code>2/3</code>--<code>3/5</code></li>
# MAGIC <li><code>0/2</code>--<code>2/2</code></li>
# MAGIC <li><code>0/2</code>--<code>2/2</code>--<code>2/3</code></li>
# MAGIC <li><code>0/2</code>--<code>2/2</code>--<code>2/3</code>--<code>3/4</code></li>
# MAGIC <li><code>0/2</code>--<code>2/2</code>--<code>2/3</code>--<code>3/5</code></li>
# MAGIC </ul>
# MAGIC <p>(Note how, as shown by <code>10/1</code>, order of ports within a component doesn't matter. However, you may only use each port on a component once.)</p>
# MAGIC <p>Of these bridges, the <em>strongest</em> one is <code>0/1</code>--<code>10/1</code>--<code>9/10</code>; it has a strength of <code>0+1 + 1+10 + 10+9 = <em>31</em></code>.</p>
# MAGIC <p><em>What is the strength of the strongest bridge you can make</em> with the components you have available?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "31/13
34/4
49/49
23/37
47/45
32/4
12/35
37/30
41/48
0/47
32/30
12/5
37/31
7/41
10/28
35/4
28/35
20/29
32/20
31/43
48/14
10/11
27/6
9/24
8/28
45/48
8/1
16/19
45/45
0/4
29/33
2/5
33/9
11/7
32/10
44/1
40/32
2/45
16/16
1/18
38/36
34/24
39/44
32/37
26/46
25/33
9/10
0/29
38/8
33/33
49/19
18/20
49/39
18/39
26/13
19/32
"

# COMMAND ----------

# input <- "0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10
# "

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_split("/") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("a", "b"))
df

# COMMAND ----------

get_strongest_bridge <- function(df, previous_port = 0) {
  strongest <- 0
  for (i in seq_len(nrow(df))) {
    if (df$a[i] == previous_port || df$b[i] == previous_port) {
      strength <- df$a[i] + df$b[i] + get_strongest_bridge(filter(df, !(a == df$a[i] & b == df$b[i])), ifelse(df$a[i] == previous_port, df$b[i], df$a[i]))
      strongest <- max(strongest, strength)
    }
  }
  strongest
}

# COMMAND ----------

answer <- get_strongest_bridge(df)
answer # 26 minutes

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The bridge you've built isn't long enough; you can't <span title="Who do you think you are, Mario?">jump the rest of the way</span>.</p>
# MAGIC <p>In the example above, there are two longest bridges:</p>
# MAGIC <ul>
# MAGIC <li><code>0/2</code>--<code>2/2</code>--<code>2/3</code>--<code>3/4</code></li>
# MAGIC <li><code>0/2</code>--<code>2/2</code>--<code>2/3</code>--<code>3/5</code></li>
# MAGIC </ul>
# MAGIC <p>Of them, the one which uses the <code>3/5</code> component is stronger; its strength is <code>0+2 + 2+2 + 2+3 + 3+5 = <em>19</em></code>.</p>
# MAGIC <p><em>What is the strength of the longest bridge you can make?</em> If you can make multiple bridges of the longest length, pick the <em>strongest</em> one.</p>
# MAGIC </article>

# COMMAND ----------

get_longest_bridge <- function(df, previous_port = 0) {
  longest_length <- 0
  longest_strength <- 0
  for (i in seq_len(nrow(df))) {
    if (df$a[i] == previous_port || df$b[i] == previous_port) {
      result <- get_longest_bridge(
        filter(df, !(a == df$a[i] & b == df$b[i])),
        ifelse(df$a[i] == previous_port, df$b[i], df$a[i])
      )
      this_strength <- df$a[i] + df$b[i] + result$longest_strength
      this_length <- result$longest_length + 1
      if (this_length > longest_length || (this_length == longest_length && this_strength > longest_strength)) {
        longest_strength <- this_strength
        longest_length<- this_length
      }
    }
  }
  lst(longest_length, longest_strength)
}

# COMMAND ----------

result <- get_longest_bridge(df)
answer <- result$longest_strength
answer # 29 minutes
