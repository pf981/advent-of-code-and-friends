# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 13: Packet Scanners ---</h2><p>You need to cross a vast <em>firewall</em>. The firewall consists of several layers, each with a <em>security scanner</em> that moves back and forth across the layer. To succeed, you must not be detected by a scanner.</p>
# MAGIC <p>By studying the firewall briefly, you are able to record (in your puzzle input) the <em>depth</em> of each layer and the <em>range</em> of the scanning area for the scanner within it, written as <code>depth: range</code>. Each layer has a thickness of exactly <code>1</code>. A layer at depth <code>0</code> begins immediately inside the firewall; a layer at depth <code>1</code> would start immediately after that.</p>
# MAGIC <p>For example, suppose you've recorded the following:</p>
# MAGIC <pre><code>0: 3
# MAGIC 1: 2
# MAGIC 4: 4
# MAGIC 6: 4
# MAGIC </code></pre>
# MAGIC <p>This means that there is a layer immediately inside the firewall (with range <code>3</code>), a second layer immediately after that (with range <code>2</code>), a third layer which begins at depth <code>4</code> (with range <code>4</code>), and a fourth layer which begins at depth 6 (also with range <code>4</code>). Visually, it might look like this:</p>
# MAGIC <pre><code> 0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC </code></pre>
# MAGIC <p>Within each layer, a security scanner moves back and forth within its range. Each security scanner starts at the top and moves down until it reaches the bottom, then moves up until it reaches the top, and repeats. A security scanner takes <em>one picosecond</em> to move one step.  Drawing scanners as <code>S</code>, the first few picoseconds look like this:</p>
# MAGIC <pre><code>
# MAGIC Picosecond 0:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... ... [S] ... [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC Picosecond 1:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC Picosecond 2:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC Picosecond 3:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] ... [ ]
# MAGIC [S] [S]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [S]     [S]
# MAGIC </code></pre>
# MAGIC <p>Your plan is to hitch a ride on a packet about to move through the firewall.  The packet will travel along the top of each layer, and it moves at <em>one layer per picosecond</em>. Each picosecond, the packet moves one layer forward (its first move takes it into layer 0), and then the scanners move one step. If there is a scanner at the top of the layer <em>as your packet enters it</em>, you are <em>caught</em>. (If a scanner moves into the top of its layer while you are there, you are <em>not</em> caught: it doesn't have time to notice you before you leave.) If you were to do this in the configuration above, marking your current position with parentheses, your passage through the firewall would look like this:</p>
# MAGIC <pre><code>Initial state:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... ... [S] ... [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC Picosecond 0:
# MAGIC  0   1   2   3   4   5   6
# MAGIC (S) [S] ... ... [S] ... [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC ( ) [ ] ... ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 1:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] ( ) ... ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] (S) ... ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 2:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] (.) ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] (.) ... [ ] ... [ ]
# MAGIC [S] [S]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [S]     [S]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 3:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... (.) [ ] ... [ ]
# MAGIC [S] [S]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [S]     [S]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... (.) [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 4:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... ... ( ) ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... ( ) ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 5:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] (.) [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... ... [S] (.) [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 6:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... ... [S] ... (S)
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] ... ( )
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC </code></pre>
# MAGIC <p>In this situation, you are <em>caught</em> in layers <code>0</code> and <code>6</code>, because your packet entered the layer when its scanner was at the top when you entered it. You are <em>not</em> caught in layer <code>1</code>, since the scanner moved into the top of the layer once you were already there.</p>
# MAGIC <p>The <em>severity</em> of getting caught on a layer is equal to its <em>depth</em> multiplied by its <em>range</em>. (Ignore layers in which you do not get caught.) The severity of the whole trip is the sum of these values.  In the example above, the trip severity is <code>0*3 + 6*4 = <em>24</em></code>.</p>
# MAGIC <p>Given the details of the firewall you've recorded, if you leave immediately, <em>what is the severity of your whole trip</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "0: 4
1: 2
2: 3
4: 4
6: 6
8: 5
10: 6
12: 6
14: 6
16: 8
18: 8
20: 9
22: 12
24: 8
26: 8
28: 8
30: 12
32: 12
34: 8
36: 12
38: 10
40: 12
42: 12
44: 10
46: 12
48: 14
50: 12
52: 14
54: 14
56: 12
58: 14
60: 12
62: 14
64: 18
66: 14
68: 14
72: 14
76: 14
82: 14
86: 14
88: 18
90: 14
92: 17
"

# COMMAND ----------

# input <- "0: 3
# 1: 2
# 4: 4
# 6: 4
# "

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    depth = str_extract(line, "^\\d+") %>% parse_integer(),
    range = str_extract(line, "\\d+$") %>% parse_integer(),
    severity = depth * range,
    period = (range - 2) * 2 + 2,
    is_caught = (depth %% period) == 0
  )
df

# COMMAND ----------

answer <-
  df %>%
  filter(is_caught) %>%
  pull(severity) %>%
  sum()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, you need to pass through the firewall without being caught - easier said than done.</p>
# MAGIC <p>You can't control the <span title="Seriously, what network stack doesn't let you adjust the speed of light?">speed of the packet</span>, but you can <em>delay</em> it any number of picoseconds. For each picosecond you delay the packet before beginning your trip, all security scanners move one step. You're not in the firewall during this time; you don't enter layer <code>0</code> until you stop delaying the packet.</p>
# MAGIC <p>In the example above, if you delay <code>10</code> picoseconds (picoseconds <code>0</code> - <code>9</code>), you won't get caught:</p>
# MAGIC <pre><code>State after delaying:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC Picosecond 10:
# MAGIC  0   1   2   3   4   5   6
# MAGIC ( ) [S] ... ... [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC ( ) [ ] ... ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 11:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] ( ) ... ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] (S) ... ... [S] ... [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 12:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] (.) ... [S] ... [S]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] (.) ... [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 13:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... (.) [ ] ... [ ]
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... (.) [ ] ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 14:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [S] ... ... ( ) ... [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [S]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... ( ) ... [ ]
# MAGIC [S] [S]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [S]     [S]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 15:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] (.) [ ]
# MAGIC [S] [S]         [ ]     [ ]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [S]     [S]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... ... [ ] (.) [ ]
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC 
# MAGIC Picosecond 16:
# MAGIC  0   1   2   3   4   5   6
# MAGIC [S] [S] ... ... [ ] ... ( )
# MAGIC [ ] [ ]         [ ]     [ ]
# MAGIC [ ]             [S]     [S]
# MAGIC                 [ ]     [ ]
# MAGIC 
# MAGIC  0   1   2   3   4   5   6
# MAGIC [ ] [ ] ... ... [ ] ... ( )
# MAGIC [S] [S]         [S]     [S]
# MAGIC [ ]             [ ]     [ ]
# MAGIC                 [ ]     [ ]
# MAGIC </code></pre>
# MAGIC <p>Because all smaller delays would get you caught, the fewest number of picoseconds you would need to delay to get through safely is <code>10</code>.</p>
# MAGIC <p><em>What is the fewest number of picoseconds</em> that you need to delay the packet to pass through the firewall without being caught?</p>
# MAGIC </article>

# COMMAND ----------

# This is too slow
# t <- 0
# repeat {
#   caught <-
#     df %>%
#     mutate(
#       depth = depth + t,
#       period = (range - 2) * 2 + 2,
#       is_caught = (depth %% period) == 0
#     ) %>%
#     pull(is_caught) %>%
#     any()
#   if (!caught) break
#   t <- t + 1
# }

# answer <- t
# answer

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp(std::vector<int> depth, std::vector<int> period) {
  bool done = false;
  int t = 0;
  while (!done) {
    done = true;
    for (int i = 0; i < depth.size(); ++i) {
      if ((depth[i] + t) % period[i] == 0) {
        done = false;
        break;
      }
    }
    ++t;
  }
  return t - 1;
}
')

# COMMAND ----------

answer <- solve_cpp(df$depth, df$period)
answer
