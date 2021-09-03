# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/24

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 24: It Hangs in the Balance ---</h2><p>It's Christmas Eve, and Santa is loading up the sleigh for this year's deliveries.  However, there's one small problem: he can't get the sleigh to balance.  If it isn't balanced, he can't defy physics, and nobody gets presents this year.</p>
# MAGIC <p>No pressure.</p>
# MAGIC <p>Santa has provided you a list of the weights of every package he needs to fit on the sleigh.  The packages need to be split into <em>three groups of exactly the same weight</em>, and every package has to fit.  The first group goes in the passenger compartment of the sleigh, and the second and third go in containers on either side.  Only when all three groups weigh exactly the same amount will the sleigh be able to fly.  Defying physics has rules, you know!</p>
# MAGIC <p>Of course, that's not the only problem.  The first group - the one going in the passenger compartment - needs <em>as few packages as possible</em> so that Santa has some legroom left over.  It doesn't matter how many packages are in either of the other two groups, so long as all of the groups weigh the same.</p>
# MAGIC <p>Furthermore, Santa tells you, if there are multiple ways to arrange the packages such that the fewest possible are in the first group, you need to choose the way where the first group has <em>the smallest quantum entanglement</em> to reduce the chance of any <span title="Santa does not elaborate on what he means by this, but the cringe he makes indicates that it wouldn't be pretty.">"complications"</span>.  The quantum entanglement of a group of packages is the <a href="https://en.wikipedia.org/wiki/Product_%28mathematics%29">product</a> of their weights, that is, the value you get when you multiply their weights together.  Only consider quantum entanglement if the first group has the fewest possible number of packages in it and all groups weigh the same amount.</p>
# MAGIC <p>For example, suppose you have ten packages with weights <code>1</code> through <code>5</code> and <code>7</code> through <code>11</code>.  For this situation, some of the unique first groups, their quantum entanglements, and a way to divide the remaining packages are as follows:</p>
# MAGIC <pre><code>Group 1;             Group 2; Group 3
# MAGIC 11 9       (QE= 99); 10 8 2;  7 5 4 3 1
# MAGIC 10 9 1     (QE= 90); 11 7 2;  8 5 4 3
# MAGIC 10 8 2     (QE=160); 11 9;    7 5 4 3 1
# MAGIC 10 7 3     (QE=210); 11 9;    8 5 4 2 1
# MAGIC 10 5 4 1   (QE=200); 11 9;    8 7 3 2
# MAGIC 10 5 3 2   (QE=300); 11 9;    8 7 4 1
# MAGIC 10 4 3 2 1 (QE=240); 11 9;    8 7 5
# MAGIC 9 8 3      (QE=216); 11 7 2;  10 5 4 1
# MAGIC 9 7 4      (QE=252); 11 8 1;  10 5 3 2
# MAGIC 9 5 4 2    (QE=360); 11 8 1;  10 7 3
# MAGIC 8 7 5      (QE=280); 11 9;    10 4 3 2 1
# MAGIC 8 5 4 3    (QE=480); 11 9;    10 7 2 1
# MAGIC 7 5 4 3 1  (QE=420); 11 9;    10 8 2
# MAGIC </code></pre>
# MAGIC <p>Of these, although <code>10 9 1</code> has the smallest quantum entanglement (<code>90</code>), the configuration with only two packages, <code>11 9</code>, in the passenger compartment gives Santa the most legroom and wins.  In this situation, the quantum entanglement for the ideal configuration is therefore <code>99</code>.  Had there been two configurations with only two packages in the first group, the one with the smaller quantum entanglement would be chosen.</p>
# MAGIC <p>What is the <em>quantum entanglement</em> of the first group of packages in the ideal configuration?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "1
2
3
5
7
13
17
19
23
29
31
37
41
43
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"

# COMMAND ----------

packages <- read_lines(input) %>% parse_number()

# COMMAND ----------

create_groups <- function(nums, target = sum(nums / 3), previous_nums = NULL) {
  if (target == 0) {
    return(list(previous_nums))
  }
  
  if (target < 0 || length(nums) == 0) {
    return(list())
  }
  
  all_groups <- list()
  for (i in seq_along(nums)) {
    cur_groups <- create_groups(
      nums = nums[seq_along(nums) > i],
      target = target - nums[[i]],
      previous_nums = c(previous_nums, nums[[i]])
    )
    all_groups <- c(all_groups, cur_groups)
  }
  all_groups
}

# COMMAND ----------

possible_groups <-
  create_groups(packages) %>% # 3 minutes
  {.[order(map_dbl(., length), map_dbl(., prod))]}
length(possible_groups)

# COMMAND ----------

find_group_combination <- function(possible_groups) {
  for (group1 in possible_groups) {
    for (group2 in discard(possible_groups, ~any(. %in% group1))) {
      if (any(!map_lgl(possible_groups, ~any(. %in% c(group1, group2))))) {
        return(lst(
          group1,
          group2
        ))
      }
    }
  }
}

# COMMAND ----------

result <- find_group_combination(possible_groups)
result

# COMMAND ----------

answer <- prod(result$group1)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>That's weird... the sleigh still isn't balancing.</p>
# MAGIC <p>"Ho ho ho", Santa muses to himself. "I forgot the trunk".</p>
# MAGIC <p>Balance the sleigh again, but this time, separate the packages into <em>four groups</em> instead of three.  The other constraints still apply.</p>
# MAGIC <p>Given the example packages above, this would be some of the new unique first groups, their quantum entanglements, and one way to divide the remaining packages:</p>
# MAGIC <pre><code>
# MAGIC 11 4    (QE=44); 10 5;   9 3 2 1; 8 7
# MAGIC 10 5    (QE=50); 11 4;   9 3 2 1; 8 7
# MAGIC 9 5 1   (QE=45); 11 4;   10 3 2;  8 7
# MAGIC 9 4 2   (QE=72); 11 3 1; 10 5;    8 7
# MAGIC 9 3 2 1 (QE=54); 11 4;   10 5;    8 7
# MAGIC 8 7     (QE=56); 11 4;   10 5;    9 3 2 1
# MAGIC </code></pre>
# MAGIC <p>Of these, there are three arrangements that put the minimum (two) number of packages in the first group: <code>11 4</code>, <code>10 5</code>, and <code>8 7</code>.  Of these, <code>11 4</code> has the lowest quantum entanglement, and so it is selected.</p>
# MAGIC <p>Now, what is the <em>quantum entanglement</em> of the first group of packages in the ideal configuration?</p>
# MAGIC </article>

# COMMAND ----------

possible_groups <-
  create_groups(packages, sum(packages) / 4) %>% # 3 minutes
  {.[order(map_dbl(., length), map_dbl(., prod))]}
length(possible_groups)

# COMMAND ----------

find_group_combination <- function(possible_groups) {
  for (group1 in possible_groups) {
    for (group2 in discard(possible_groups, ~any(. %in% group1))) {
      for (group3 in discard(possible_groups, ~any(. %in% c(group1, group2)))) {
        if (any(!map_lgl(possible_groups, ~any(. %in% c(group1, group2, group3))))) {
          return(lst(
            group1,
            group2,
            group3
          ))
        }
      }
    }
  }
}

# COMMAND ----------

result <- find_group_combination(possible_groups)
result

# COMMAND ----------

answer <- prod(result$group1)
answer
