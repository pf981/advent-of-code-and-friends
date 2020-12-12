# Databricks notebook source
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