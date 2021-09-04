# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/10

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 10: Balance Bots ---</h2><p>You come upon a factory in which many robots are <a href="https://www.youtube.com/watch?v=JnkMyfQ5YfY&amp;t=40">zooming around</a> handing small microchips to each other.</p>
# MAGIC <p>Upon closer examination, you notice that each bot only proceeds when it has <em>two</em> microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.</p>
# MAGIC <p>Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).</p>
# MAGIC <p>Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its <em>lower-value</em> or <em>higher-value</em> chip.</p>
# MAGIC <p>For example, consider the following instructions:</p>
# MAGIC <pre><code>value 5 goes to bot 2
# MAGIC bot 2 gives low to bot 1 and high to bot 0
# MAGIC value 3 goes to bot 1
# MAGIC bot 1 gives low to output 1 and high to bot 0
# MAGIC bot 0 gives low to output 2 and high to output 0
# MAGIC value 2 goes to bot 2
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Initially, bot <code>1</code> starts with a value-<code>3</code> chip, and bot <code>2</code> starts with a value-<code>2</code> chip and a value-<code>5</code> chip.</li>
# MAGIC <li>Because bot <code>2</code> has two microchips, it gives its lower one (<code>2</code>) to bot <code>1</code> and its higher one (<code>5</code>) to bot <code>0</code>.</li>
# MAGIC <li>Then, bot <code>1</code> has two microchips; it puts the value-<code>2</code> chip in output <code>1</code> and gives the value-<code>3</code> chip to bot <code>0</code>.</li>
# MAGIC <li>Finally, bot <code>0</code> has two microchips; it puts the <code>3</code> in output <code>2</code> and the <code>5</code> in output <code>0</code>.</li>
# MAGIC </ul>
# MAGIC <p>In the end, output bin <code>0</code> contains a value-<code>5</code> microchip, output bin <code>1</code> contains a value-<code>2</code> microchip, and output bin <code>2</code> contains a value-<code>3</code> microchip. In this configuration, bot number <em><code>2</code></em> is responsible for comparing value-<code>5</code> microchips with value-<code>2</code> microchips.</p>
# MAGIC <p>Based on your instructions, <em>what is the number of the bot</em> that is responsible for comparing value-<code>61</code> microchips with value-<code>17</code> microchips?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''bot 59 gives low to bot 176 and high to bot 120
bot 92 gives low to bot 42 and high to bot 187
value 31 goes to bot 114
bot 182 gives low to bot 49 and high to bot 176
bot 17 gives low to bot 181 and high to bot 162
bot 36 gives low to bot 118 and high to bot 121
bot 118 gives low to bot 164 and high to bot 55
bot 172 gives low to bot 79 and high to bot 123
bot 51 gives low to bot 60 and high to bot 31
bot 48 gives low to bot 107 and high to bot 58
bot 142 gives low to output 6 and high to bot 35
bot 133 gives low to output 4 and high to bot 47
bot 134 gives low to bot 122 and high to bot 66
bot 106 gives low to bot 155 and high to bot 99
bot 77 gives low to bot 93 and high to bot 84
bot 9 gives low to bot 173 and high to bot 197
bot 64 gives low to bot 123 and high to bot 48
bot 177 gives low to bot 21 and high to bot 132
bot 94 gives low to bot 6 and high to bot 25
bot 126 gives low to bot 193 and high to bot 56
bot 74 gives low to bot 187 and high to bot 125
bot 80 gives low to bot 41 and high to bot 191
bot 62 gives low to bot 157 and high to bot 138
bot 66 gives low to bot 1 and high to bot 209
bot 90 gives low to bot 104 and high to bot 34
bot 68 gives low to bot 23 and high to bot 87
bot 121 gives low to bot 55 and high to bot 126
bot 122 gives low to bot 137 and high to bot 1
bot 209 gives low to bot 168 and high to bot 26
bot 141 gives low to bot 170 and high to bot 6
bot 149 gives low to bot 62 and high to bot 13
bot 120 gives low to bot 179 and high to bot 71
bot 160 gives low to bot 194 and high to bot 151
bot 86 gives low to bot 96 and high to bot 106
value 13 goes to bot 9
bot 180 gives low to bot 189 and high to bot 27
value 67 goes to bot 88
bot 169 gives low to bot 99 and high to bot 159
bot 56 gives low to bot 98 and high to bot 147
bot 197 gives low to bot 174 and high to bot 81
bot 57 gives low to bot 113 and high to bot 179
bot 39 gives low to bot 115 and high to bot 3
bot 79 gives low to bot 22 and high to bot 40
bot 161 gives low to output 14 and high to bot 185
bot 21 gives low to bot 114 and high to bot 119
bot 136 gives low to bot 28 and high to bot 158
bot 105 gives low to bot 89 and high to bot 19
bot 168 gives low to bot 126 and high to bot 26
bot 193 gives low to bot 64 and high to bot 98
bot 186 gives low to bot 86 and high to bot 178
value 11 goes to bot 165
bot 33 gives low to bot 116 and high to bot 150
bot 32 gives low to bot 154 and high to bot 206
bot 166 gives low to bot 33 and high to bot 139
value 7 goes to bot 63
bot 203 gives low to bot 172 and high to bot 64
bot 200 gives low to bot 94 and high to bot 25
value 43 goes to bot 76
bot 145 gives low to bot 103 and high to bot 128
bot 119 gives low to bot 186 and high to bot 97
bot 12 gives low to bot 31 and high to bot 4
bot 23 gives low to bot 198 and high to bot 171
bot 34 gives low to bot 10 and high to bot 20
bot 198 gives low to bot 43 and high to bot 17
bot 50 gives low to output 1 and high to bot 127
bot 155 gives low to bot 191 and high to bot 32
bot 206 gives low to bot 12 and high to bot 43
bot 96 gives low to bot 80 and high to bot 155
bot 93 gives low to bot 44 and high to bot 70
bot 24 gives low to bot 85 and high to bot 83
bot 30 gives low to bot 159 and high to bot 68
bot 55 gives low to bot 203 and high to bot 193
bot 199 gives low to bot 68 and high to bot 135
bot 170 gives low to bot 97 and high to bot 5
bot 65 gives low to bot 152 and high to bot 194
bot 43 gives low to bot 4 and high to bot 181
bot 113 gives low to output 9 and high to bot 161
bot 81 gives low to bot 141 and high to bot 94
value 29 goes to bot 7
bot 46 gives low to bot 175 and high to bot 195
value 47 goes to bot 21
value 23 goes to bot 42
bot 13 gives low to bot 138 and high to bot 61
bot 135 gives low to bot 87 and high to bot 111
bot 194 gives low to bot 190 and high to bot 82
value 73 goes to bot 109
bot 154 gives low to bot 51 and high to bot 12
bot 1 gives low to bot 18 and high to bot 209
bot 98 gives low to bot 48 and high to bot 45
bot 147 gives low to bot 45 and high to bot 95
bot 47 gives low to output 19 and high to bot 152
bot 26 gives low to bot 56 and high to bot 147
bot 179 gives low to bot 161 and high to bot 71
bot 148 gives low to bot 204 and high to bot 137
bot 5 gives low to bot 67 and high to bot 85
bot 174 gives low to bot 132 and high to bot 141
bot 8 gives low to bot 13 and high to bot 75
bot 82 gives low to bot 146 and high to bot 22
bot 123 gives low to bot 40 and high to bot 107
bot 99 gives low to bot 32 and high to bot 201
bot 41 gives low to bot 196 and high to bot 192
bot 139 gives low to bot 150 and high to bot 153
bot 11 gives low to output 16 and high to bot 113
bot 72 gives low to bot 65 and high to bot 160
bot 195 gives low to bot 133 and high to bot 183
bot 54 gives low to output 12 and high to output 10
bot 158 gives low to bot 102 and high to bot 110
bot 112 gives low to bot 19 and high to bot 118
bot 31 gives low to bot 208 and high to bot 143
bot 167 gives low to bot 7 and high to bot 96
bot 63 gives low to bot 92 and high to bot 74
bot 116 gives low to bot 20 and high to bot 131
bot 184 gives low to bot 39 and high to bot 3
bot 162 gives low to bot 205 and high to bot 39
bot 108 gives low to output 11 and high to bot 175
value 53 goes to bot 207
bot 111 gives low to bot 202 and high to bot 184
bot 25 gives low to bot 24 and high to bot 83
value 71 goes to bot 77
bot 69 gives low to bot 142 and high to bot 0
bot 146 gives low to output 13 and high to bot 53
bot 7 gives low to bot 76 and high to bot 80
bot 131 gives low to bot 73 and high to bot 204
bot 102 gives low to bot 195 and high to bot 117
bot 76 gives low to bot 165 and high to bot 41
bot 153 gives low to bot 148 and high to bot 122
bot 208 gives low to bot 90 and high to bot 163
bot 70 gives low to bot 144 and high to bot 78
bot 125 gives low to bot 8 and high to bot 156
bot 83 gives low to bot 199 and high to bot 135
bot 75 gives low to bot 61 and high to bot 104
bot 67 gives low to bot 169 and high to bot 30
bot 14 gives low to bot 81 and high to bot 200
bot 159 gives low to bot 201 and high to bot 23
value 3 goes to bot 93
bot 110 gives low to bot 117 and high to bot 89
bot 128 gives low to bot 129 and high to bot 182
bot 87 gives low to bot 171 and high to bot 111
bot 45 gives low to bot 58 and high to bot 95
bot 4 gives low to bot 143 and high to bot 166
bot 60 gives low to bot 156 and high to bot 208
bot 27 gives low to bot 108 and high to bot 46
bot 42 gives low to bot 207 and high to bot 149
bot 117 gives low to bot 183 and high to bot 72
bot 115 gives low to bot 153 and high to bot 134
bot 140 gives low to bot 125 and high to bot 60
bot 173 gives low to bot 177 and high to bot 174
bot 138 gives low to bot 180 and high to bot 52
bot 100 gives low to bot 38 and high to bot 59
value 41 goes to bot 173
value 59 goes to bot 177
bot 165 gives low to bot 63 and high to bot 196
bot 84 gives low to bot 70 and high to bot 78
bot 2 gives low to bot 160 and high to bot 91
value 61 goes to bot 29
bot 114 gives low to bot 109 and high to bot 186
bot 205 gives low to bot 139 and high to bot 115
bot 175 gives low to output 17 and high to bot 133
bot 176 gives low to bot 57 and high to bot 120
bot 107 gives low to bot 124 and high to bot 15
bot 52 gives low to bot 27 and high to bot 28
bot 103 gives low to bot 50 and high to bot 129
bot 150 gives low to bot 131 and high to bot 148
bot 16 gives low to output 20 and high to bot 189
bot 190 gives low to output 18 and high to bot 146
bot 157 gives low to bot 16 and high to bot 180
bot 10 gives low to bot 158 and high to bot 130
bot 202 gives low to bot 162 and high to bot 184
bot 88 gives low to bot 77 and high to bot 84
bot 188 gives low to bot 128 and high to bot 38
bot 58 gives low to bot 15 and high to bot 101
bot 171 gives low to bot 17 and high to bot 202
bot 97 gives low to bot 178 and high to bot 67
bot 163 gives low to bot 34 and high to bot 116
bot 124 gives low to bot 0 and high to bot 145
bot 71 gives low to bot 185 and high to bot 54
bot 78 gives low to bot 14 and high to bot 200
bot 101 gives low to bot 188 and high to bot 100
bot 189 gives low to output 7 and high to bot 108
bot 95 gives low to bot 101 and high to bot 100
bot 0 gives low to bot 35 and high to bot 103
bot 207 gives low to bot 37 and high to bot 62
bot 49 gives low to bot 11 and high to bot 57
bot 85 gives low to bot 30 and high to bot 199
bot 89 gives low to bot 72 and high to bot 2
bot 3 gives low to bot 134 and high to bot 66
bot 181 gives low to bot 166 and high to bot 205
bot 91 gives low to bot 151 and high to bot 172
value 17 goes to bot 167
bot 20 gives low to bot 130 and high to bot 73
bot 196 gives low to bot 74 and high to bot 140
bot 18 gives low to bot 121 and high to bot 168
bot 185 gives low to output 15 and high to bot 54
bot 178 gives low to bot 106 and high to bot 169
bot 129 gives low to bot 127 and high to bot 49
bot 19 gives low to bot 2 and high to bot 164
bot 15 gives low to bot 145 and high to bot 188
bot 144 gives low to bot 197 and high to bot 14
bot 201 gives low to bot 206 and high to bot 198
bot 164 gives low to bot 91 and high to bot 203
bot 73 gives low to bot 105 and high to bot 112
bot 191 gives low to bot 192 and high to bot 154
bot 109 gives low to bot 167 and high to bot 86
bot 151 gives low to bot 82 and high to bot 79
bot 53 gives low to output 2 and high to bot 142
bot 37 gives low to bot 29 and high to bot 157
value 2 goes to bot 44
bot 204 gives low to bot 112 and high to bot 36
bot 40 gives low to bot 69 and high to bot 124
bot 22 gives low to bot 53 and high to bot 69
bot 104 gives low to bot 136 and high to bot 10
value 19 goes to bot 88
bot 127 gives low to output 5 and high to bot 11
bot 183 gives low to bot 47 and high to bot 65
bot 192 gives low to bot 140 and high to bot 51
bot 38 gives low to bot 182 and high to bot 59
bot 61 gives low to bot 52 and high to bot 136
bot 156 gives low to bot 75 and high to bot 90
value 37 goes to bot 37
bot 28 gives low to bot 46 and high to bot 102
bot 187 gives low to bot 149 and high to bot 8
bot 132 gives low to bot 119 and high to bot 170
bot 44 gives low to bot 9 and high to bot 144
bot 29 gives low to output 0 and high to bot 16
bot 6 gives low to bot 5 and high to bot 24
bot 137 gives low to bot 36 and high to bot 18
bot 130 gives low to bot 110 and high to bot 105
value 5 goes to bot 92
bot 35 gives low to output 3 and high to bot 50
bot 152 gives low to output 8 and high to bot 190
bot 143 gives low to bot 163 and high to bot 33'''

# COMMAND ----------

import re
from collections import defaultdict

two_chip_bots = set()
bots = defaultdict(lambda: {'has': [], 'gives_to': None})

for line in inp.split('\n'):
  args = re.findall(r'(?:output )?\d+', line)

  if line.startswith('value'):
    bots[args[1]]['has'].append(int(args[0]))

    if len(bots[args[1]]['has']) == 2:
      two_chip_bots.add(args[1])
  else:
    bots[args[0]]['gives_to'] = (args[1], args[2])

while two_chip_bots:
  bot_id = two_chip_bots.pop()
  bot = bots[bot_id]

  if 61 in bot['has'] and 17 in bot['has']:
    target_bot = bot_id

  for to_bot, to_value in zip(bot['gives_to'], sorted(bot['has'])):
    bots[to_bot]['has'].append(int(to_value))

    if len(bots[to_bot]['has']) == 2:
      two_chip_bots.add(to_bot)

        
answer = target_bot
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><span title="What do you get if you multiply six by nine?">What do you get</span> if you <em>multiply together the values</em> of one chip in each of outputs <code>0</code>, <code>1</code>, and <code>2</code>?</p>
# MAGIC </article>

# COMMAND ----------

from math import prod

answer = prod(bots[f'output {x}']['has'][0] for x in range(3))
answer
