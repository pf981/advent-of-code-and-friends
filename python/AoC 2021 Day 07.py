# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 7: The Treachery of Whales ---</h2><p>A giant <a href="https://en.wikipedia.org/wiki/Sperm_whale" target="_blank">whale</a> has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!</p>
# MAGIC <p>Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a <em>massive underground cave system</em> just beyond where they're aiming!</p>
# MAGIC <p>The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?</p>
# MAGIC <p>There's one major catch - crab submarines can only move horizontally.</p>
# MAGIC <p>You quickly make a list of <em>the horizontal position of each crab</em> (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.</p>
# MAGIC <p>For example, consider the following horizontal positions:</p>
# MAGIC <pre><code>16,1,2,0,4,2,7,1,2,14</code></pre>
# MAGIC <p>This means there's a crab with horizontal position <code>16</code>, a crab with horizontal position <code>1</code>, and so on.</p>
# MAGIC <p>Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position <code>2</code>:</p>
# MAGIC <ul>
# MAGIC <li>Move from <code>16</code> to <code>2</code>: <code>14</code> fuel</li>
# MAGIC <li>Move from <code>1</code> to <code>2</code>: <code>1</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>2</code>: <code>0</code> fuel</li>
# MAGIC <li>Move from <code>0</code> to <code>2</code>: <code>2</code> fuel</li>
# MAGIC <li>Move from <code>4</code> to <code>2</code>: <code>2</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>2</code>: <code>0</code> fuel</li>
# MAGIC <li>Move from <code>7</code> to <code>2</code>: <code>5</code> fuel</li>
# MAGIC <li>Move from <code>1</code> to <code>2</code>: <code>1</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>2</code>: <code>0</code> fuel</li>
# MAGIC <li>Move from <code>14</code> to <code>2</code>: <code>12</code> fuel</li>
# MAGIC </ul>
# MAGIC <p>This costs a total of <code><em>37</em></code> fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position <code>1</code> (<code>41</code> fuel), position <code>3</code> (<code>39</code> fuel), or position <code>10</code> (<code>71</code> fuel).</p>
# MAGIC <p>Determine the horizontal position that the crabs can align to using the least fuel possible. <em>How much fuel must they spend to align to that position?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,485,546,350,100,791,199,115,144,649,41,1656,163,903,71,384,30,2,251,554,210,434,206,546,759,258,54,1478,48,438,601,326,5,1017,165,168,201,622,864,1338,24,1074,545,499,484,264,345,332,869,297,711,674,346,1139,317,875,242,725,250,1619,1408,956,380,366,187,1034,1555,467,170,114,1136,150,183,304,44,37,333,791,34,540,716,1923,342,6,922,18,24,1189,59,1726,636,442,426,1089,526,298,386,296,623,80,272,240,406,628,238,409,302,35,404,92,48,157,1545,409,1382,151,1656,3,76,14,115,566,650,197,448,573,161,86,140,875,128,319,4,822,530,189,247,667,82,316,274,110,206,1012,166,639,579,459,284,200,16,24,147,743,113,1562,387,60,84,797,14,30,1015,508,88,113,685,658,257,1507,348,30,808,416,9,835,671,16,474,885,230,47,463,1324,1263,183,603,739,0,296,789,1411,339,27,1154,31,882,409,646,92,153,147,974,497,308,85,311,135,627,811,295,698,2,20,1170,789,702,1194,1390,432,257,715,958,150,1295,144,1193,607,67,929,383,1051,1231,393,190,380,1203,1090,1238,143,206,210,1004,304,1305,392,143,1379,665,806,452,185,4,1,201,1104,633,274,493,472,141,674,1261,106,587,244,903,91,158,69,137,922,778,143,692,160,474,7,304,824,657,15,1110,806,295,1565,1162,358,725,877,440,690,13,69,111,304,300,493,249,105,746,20,163,561,913,558,252,13,193,508,12,845,120,205,154,1582,349,1471,529,268,23,689,6,776,565,401,0,623,186,62,95,148,275,1,137,320,0,19,1803,10,100,652,750,226,484,180,46,310,446,667,543,277,139,265,74,171,87,1753,337,162,59,1339,1040,1287,1084,192,169,50,1557,81,1120,271,167,977,76,295,12,54,710,36,364,521,989,1634,720,1031,1204,355,380,859,633,223,1207,221,31,138,1305,779,1026,52,92,216,221,0,980,130,1197,585,1213,63,157,213,993,1123,588,450,256,1021,90,1420,47,386,843,1188,1466,807,596,416,23,32,62,1289,317,368,491,907,1386,114,1620,39,344,1342,43,281,12,1202,257,1357,203,465,174,350,833,125,54,390,687,339,628,819,261,1341,840,643,414,82,373,428,1315,570,1070,686,893,70,728,70,358,1233,189,1247,244,1043,1135,42,531,962,35,30,1462,946,856,145,386,1134,1071,379,740,175,1205,234,354,5,1028,506,58,433,1055,749,854,99,298,1248,619,62,181,258,42,130,1698,1313,672,129,222,127,636,846,24,1324,946,622,689,168,329,301,458,173,591,772,93,282,8,320,106,233,412,556,2,522,369,8,1371,899,503,568,667,1199,92,115,899,952,81,629,175,274,763,204,339,236,317,257,731,1082,1724,211,516,165,91,334,1216,101,21,1340,235,336,1351,723,1745,183,841,104,172,1080,180,493,798,1468,45,1627,59,58,368,560,166,1125,136,26,1238,1580,420,1732,155,55,293,751,194,1723,175,11,30,10,307,57,66,704,285,685,241,565,368,50,181,1047,147,420,1341,20,37,400,798,476,1060,642,134,140,502,254,997,910,636,179,22,612,55,237,258,48,205,412,155,910,192,262,9,91,766,1426,71,5,315,285,186,629,422,1289,397,52,860,1390,106,887,1285,1196,684,36,703,199,4,277,151,82,293,1047,455,21,935,630,736,118,13,30,584,453,1446,381,585,810,177,1028,280,281,184,78,673,126,410,872,524,78,188,121,394,201,1764,609,350,706,428,88,783,189,643,305,516,259,582,309,985,338,21,235,73,44,585,71,983,175,1336,1056,10,8,537,701,1653,657,70,1242,442,52,973,203,173,959,964,272,348,3,567,714,1466,382,129,613,1042,686,461,57,523,740,726,149,1490,867,44,379,1270,547,649,1103,912,1354,985,458,887,603,1016,317,499,690,829,1231,364,772,29,57,357,467,484,202,150,109,95,414,444,383,62,124,645,723,772,881,1553,413,123,248,1085,453,260,214,113,1874,482,942,235,899,122,171,127,913,424,406,49,97,1848,295,1152,111,350,54,1160,2,16,156,448,394,740,49,1237,548,206,1206,775,748,728,48,238,148,109,18,56,64,515,163,609,273,301,396,207,51,478,1183,864,772,450,222,1387,269,40,87,426,164,1270,21,347,316,331,408,914,1046,173,48,398,177,431,47,1055,221,513,226,84,285,566,270,333,343,480,1802,101,683,168,1347,582,80,22,329,350,108,379,14,53,349,43,435,195,102,168,338'

# COMMAND ----------

def calc_min_fuel(crabs, fuel_cost_f):
  min_fuel = float('inf')
  for target in range(min(crabs), max(crabs) + 1):
    fuel = sum(fuel_cost_f(abs(crab - target)) for crab in crabs)
    min_fuel = min(min_fuel, fuel)
  
  return min_fuel

crabs = [int(x) for x in inp.split(',')]

answer = calc_min_fuel(crabs, lambda d: d)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?</p>
# MAGIC <p>As it turns out, crab submarine engines <span title="This appears to be due to the modial interaction of magneto-reluctance and capacitive duractance.">don't burn fuel at a constant rate</span>. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs <code>1</code>, the second step costs <code>2</code>, the third step costs <code>3</code>, and so on.</p>
# MAGIC <p>As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes <code>5</code>:</p>
# MAGIC <ul>
# MAGIC <li>Move from <code>16</code> to <code>5</code>: <code>66</code> fuel</li>
# MAGIC <li>Move from <code>1</code> to <code>5</code>: <code>10</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>5</code>: <code>6</code> fuel</li>
# MAGIC <li>Move from <code>0</code> to <code>5</code>: <code>15</code> fuel</li>
# MAGIC <li>Move from <code>4</code> to <code>5</code>: <code>1</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>5</code>: <code>6</code> fuel</li>
# MAGIC <li>Move from <code>7</code> to <code>5</code>: <code>3</code> fuel</li>
# MAGIC <li>Move from <code>1</code> to <code>5</code>: <code>10</code> fuel</li>
# MAGIC <li>Move from <code>2</code> to <code>5</code>: <code>6</code> fuel</li>
# MAGIC <li>Move from <code>14</code> to <code>5</code>: <code>45</code> fuel</li>
# MAGIC </ul>
# MAGIC <p>This costs a total of <code><em>168</em></code> fuel. This is the new cheapest possible outcome; the old alignment position (<code>2</code>) now costs <code>206</code> fuel instead.</p>
# MAGIC <p>Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! <em>How much fuel must they spend to align to that position?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = calc_min_fuel(crabs, lambda d: d * (d + 1) // 2)
print(answer)
