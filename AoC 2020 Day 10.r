# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/10
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 10: Adapter Array ---</h2><p>Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!</p>
# MAGIC <p>Its battery is dead.</p>
# MAGIC <p>You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of <em>jolts</em>. Always prepared, you make a list of all of the joltage adapters in your bag.</p>
# MAGIC <p>Each of your joltage adapters is rated for a specific <em>output joltage</em> (your puzzle input). Any given adapter can take an input <code>1</code>, <code>2</code>, or <code>3</code> jolts <em>lower</em> than its rating and still produce its rated output joltage.</p>
# MAGIC <p>In addition, your device has a built-in joltage adapter rated for <em><code>3</code> jolts higher</em> than the highest-rated adapter in your bag. (If your adapter list were <code>3</code>, <code>9</code>, and <code>6</code>, your device's built-in adapter would be rated for <code>12</code> jolts.)</p>
# MAGIC <p>Treat the charging outlet near your seat as having an effective joltage rating of <code>0</code>.</p>
# MAGIC <p>Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!</p>
# MAGIC <p>If you <em>use every adapter in your bag</em> at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?</p>
# MAGIC <p>For example, suppose that in your bag, you have adapters with the following joltage ratings:</p>
# MAGIC <pre><code>16
# MAGIC 10
# MAGIC 15
# MAGIC 5
# MAGIC 1
# MAGIC 11
# MAGIC 7
# MAGIC 19
# MAGIC 6
# MAGIC 12
# MAGIC 4
# MAGIC </code></pre>
# MAGIC <p>With these adapters, your device's built-in joltage adapter would be rated for <code>19 + 3 = <em>22</em></code> jolts, 3 higher than the highest-rated adapter.</p>
# MAGIC <p>Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this:</p>
# MAGIC <ul>
# MAGIC <li>The charging outlet has an effective rating of <code>0</code> jolts, so the only adapters that could connect to it directly would need to have a joltage rating of <code>1</code>, <code>2</code>, or <code>3</code> jolts. Of these, only one you have is an adapter rated <code>1</code> jolt (difference of <em><code>1</code></em>).</li>
# MAGIC <li>From your <code>1</code>-jolt rated adapter, the only choice is your <code>4</code>-jolt rated adapter (difference of <em><code>3</code></em>).</li>
# MAGIC <li>From the <code>4</code>-jolt rated adapter, the adapters rated <code>5</code>, <code>6</code>, or <code>7</code> are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated <code>5</code> jolts (difference of <em><code>1</code></em>).</li>
# MAGIC <li>Similarly, the next choices would need to be the adapter rated <code>6</code> and then the adapter rated <code>7</code> (with difference of <em><code>1</code></em> and <em><code>1</code></em>).</li>
# MAGIC <li>The only adapter that works with the <code>7</code>-jolt rated adapter is the one rated <code>10</code> jolts (difference of <em><code>3</code></em>).</li>
# MAGIC <li>From <code>10</code>, the choices are <code>11</code> or <code>12</code>; choose <code>11</code> (difference of <em><code>1</code></em>) and then <code>12</code> (difference of <em><code>1</code></em>).</li>
# MAGIC <li>After <code>12</code>, only valid adapter has a rating of <code>15</code> (difference of <em><code>3</code></em>), then <code>16</code> (difference of <em><code>1</code></em>), then <code>19</code> (difference of <em><code>3</code></em>).</li>
# MAGIC <li>Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is <code>22</code> jolts (always a difference of <em><code>3</code></em>).</li>
# MAGIC </ul>
# MAGIC <p>In this example, when using every adapter, there are <em><code>7</code></em> differences of 1 jolt and <em><code>5</code></em> differences of 3 jolts.</p>
# MAGIC <p>Here is a larger example:</p>
# MAGIC <pre><code>28
# MAGIC 33
# MAGIC 18
# MAGIC 42
# MAGIC 31
# MAGIC 14
# MAGIC 46
# MAGIC 20
# MAGIC 48
# MAGIC 47
# MAGIC 24
# MAGIC 23
# MAGIC 49
# MAGIC 45
# MAGIC 19
# MAGIC 38
# MAGIC 39
# MAGIC 11
# MAGIC 1
# MAGIC 32
# MAGIC 25
# MAGIC 35
# MAGIC 8
# MAGIC 17
# MAGIC 7
# MAGIC 9
# MAGIC 4
# MAGIC 2
# MAGIC 34
# MAGIC 10
# MAGIC 3
# MAGIC </code></pre>
# MAGIC <p>In this larger example, in a chain that uses all of the adapters, there are <em><code>22</code></em> differences of 1 jolt and <em><code>10</code></em> differences of 3 jolts.</p>
# MAGIC <p>Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. <em>What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>2201</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.</p>
# MAGIC <p>The first example above (the one that starts with <code>16</code>, <code>10</code>, <code>15</code>) supports the following arrangements:</p>
# MAGIC <pre><code>(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# MAGIC (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
# MAGIC </code></pre>
# MAGIC <p>(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is <em><code>8</code></em>.</p>
# MAGIC <p>The second example above (the one that starts with <code>28</code>, <code>33</code>, <code>18</code>) has many arrangements. Here are a few:</p>
# MAGIC <pre><code>(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# MAGIC 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
# MAGIC 
# MAGIC (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# MAGIC 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)
# MAGIC 
# MAGIC (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# MAGIC 32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)
# MAGIC 
# MAGIC (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# MAGIC 32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)
# MAGIC 
# MAGIC (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# MAGIC 32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)
# MAGIC 
# MAGIC (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# MAGIC 46, 48, 49, (52)
# MAGIC 
# MAGIC (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# MAGIC 46, 49, (52)
# MAGIC 
# MAGIC (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# MAGIC 47, 48, 49, (52)
# MAGIC 
# MAGIC (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# MAGIC 47, 49, (52)
# MAGIC 
# MAGIC (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# MAGIC 48, 49, (52)
# MAGIC </code></pre>
# MAGIC <p>In total, this set of adapters can connect the charging outlet to your device in <em><code>19208</code></em> distinct arrangements.</p>
# MAGIC <p>You glance back down at your bag and try to remember why you brought so many adapters; there must be <em>more than a trillion</em> valid ways to arrange them! Surely, there must be <span title="Definitely itertools.">an efficient way</span> to count the arrangements.</p>
# MAGIC <p><em>What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>169255295254528</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
# MAGIC <p>At this point, you should <a href="/2020">return to your Advent calendar</a> and try another puzzle.</p>
# MAGIC <p>If you still want to see it, you can <a href="10/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Adapter+Array%22+%2D+Day+10+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F10&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Adapter+Array%22+%2D+Day+10+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F10'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "104
83
142
123
87
48
102
159
122
69
127
151
147
64
152
90
117
132
63
109
27
47
7
52
59
11
161
12
148
155
129
10
135
17
153
96
3
93
82
55
34
65
89
126
19
72
20
38
103
146
14
105
53
77
120
39
46
24
139
95
140
33
21
84
56
1
32
31
28
4
73
128
49
18
62
81
66
121
54
160
158
138
94
43
2
114
111
110
78
13
99
108
141
40
25
154
26
35
88
76
145
"

# COMMAND ----------

# input <- "16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# "

# COMMAND ----------

nums <- input %>% read_lines() %>% parse_integer()

sequence <- sort(c(0, nums, max(nums) + 3))

sum(diff(sequence) == 1) * sum(diff(sequence) == 3)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

ways <- integer(max(sequence) + 1)
ways[length(ways)] <- 1

for (num in rev(sequence)[-1]) {
  next_nums <- sequence[sequence %in% (num + 1:3)]
  ways[num + 1] <- sum(ways[next_nums + 1])
}

# COMMAND ----------

format(ways[[1]], scientific = FALSE)