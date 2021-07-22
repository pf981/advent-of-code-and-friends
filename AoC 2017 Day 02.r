# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 2: Corruption Checksum ---</h2><p>As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"</p>
# MAGIC <p>The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's <em>checksum</em>. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.</p>
# MAGIC <p>For example, given the following spreadsheet:</p>
# MAGIC <pre><code>5 1 9 5
# MAGIC 7 5 3
# MAGIC 2 4 6 8</code></pre>
# MAGIC <ul>
# MAGIC <li>The first row's largest and smallest values are <code>9</code> and <code>1</code>, and their difference is <code>8</code>.</li>
# MAGIC <li>The second row's largest and smallest values are <code>7</code> and <code>3</code>, and their difference is <code>4</code>.</li>
# MAGIC <li>The third row's difference is <code>6</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the spreadsheet's checksum would be <code>8 + 4 + 6 = 18</code>.</p>
# MAGIC <p><em>What is the checksum</em> for the spreadsheet in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "493	458	321	120	49	432	433	92	54	452	41	461	388	409	263	58
961	98	518	188	958	114	1044	881	948	590	972	398	115	116	451	492
76	783	709	489	617	72	824	452	748	737	691	90	94	77	84	756
204	217	90	335	220	127	302	205	242	202	259	110	118	111	200	112
249	679	4015	106	3358	1642	228	4559	307	193	4407	3984	3546	2635	3858	924
1151	1060	2002	168	3635	3515	3158	141	4009	3725	996	142	3672	153	134	1438
95	600	1171	1896	174	1852	1616	928	79	1308	2016	88	80	1559	1183	107
187	567	432	553	69	38	131	166	93	132	498	153	441	451	172	575
216	599	480	208	224	240	349	593	516	450	385	188	482	461	635	220
788	1263	1119	1391	1464	179	1200	621	1304	55	700	1275	226	57	43	51
1571	58	1331	1253	60	1496	1261	1298	1500	1303	201	73	1023	582	69	339
80	438	467	512	381	74	259	73	88	448	386	509	346	61	447	435
215	679	117	645	137	426	195	619	268	223	792	200	720	260	303	603
631	481	185	135	665	641	492	408	164	132	478	188	444	378	633	516
1165	1119	194	280	223	1181	267	898	1108	124	618	1135	817	997	129	227
404	1757	358	2293	2626	87	613	95	1658	147	75	930	2394	2349	86	385
"

# COMMAND ----------

nums <-
  input %>%
  read_lines() %>%
  str_extract_all("\\d+") %>%
  map(parse_integer)
  
answer <- nums %>% map_dbl(~max(.) - min(.)) %>% sum()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>"Great work; looks like we're on the right track after all.  Here's a <em class="star">star</em> for your effort." However, the program seems a little worried. Can programs <em>be</em> worried?</p>
# MAGIC <p>"Based on what we're seeing, it looks like all the User wanted is some information about the <em>evenly divisible values</em> in the spreadsheet.  Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in <span title="Bonus points if you solve this part using only bitwise operations.">bitwise operations</span>."</p>
# MAGIC <p>It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.</p>
# MAGIC <p>For example, given the following spreadsheet:</p>
# MAGIC <pre><code>5 9 2 8
# MAGIC 9 4 7 3
# MAGIC 3 8 6 5</code></pre>
# MAGIC <ul>
# MAGIC <li>In the first row, the only two numbers that evenly divide are <code>8</code> and <code>2</code>; the result of this division is <code>4</code>.</li>
# MAGIC <li>In the second row, the two numbers are <code>9</code> and <code>3</code>; the result is <code>3</code>.</li>
# MAGIC <li>In the third row, the result is <code>2</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the sum of the results would be <code>4 + 3 + 2 = 9</code>.</p>
# MAGIC <p>What is the <em>sum of each row's result</em> in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

div <- function(x) {
  for (a in x) {
    for (b in x[x < a]) {
      if (a / b == as.integer(a / b)) return(a / b)
    }
  }
}

# COMMAND ----------

answer <- nums %>% map_dbl(div) %>% sum()
answer
