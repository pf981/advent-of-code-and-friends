# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/13

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 13: Shuttle Search ---</h2><p>Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.</p>
# MAGIC <p>Fortunately, a shuttle bus service is available to bring you from the sea port to the airport!  Each bus has an ID number that also indicates <em>how often the bus leaves for the airport</em>.</p>
# MAGIC <p>Bus schedules are defined based on a <em>timestamp</em> that measures the <em>number of minutes</em> since some fixed reference point in the past. At timestamp <code>0</code>, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.</p>
# MAGIC <p>The time this loop takes a particular bus is also its ID number: the bus with ID <code>5</code> departs from the sea port at timestamps <code>0</code>, <code>5</code>, <code>10</code>, <code>15</code>, and so on. The bus with ID <code>11</code> departs at <code>0</code>, <code>11</code>, <code>22</code>, <code>33</code>, and so on. If you are there when the bus departs, you can ride that bus to the airport!</p>
# MAGIC <p>Your notes (your puzzle input) consist of two lines.  The first line is your estimate of the <em>earliest timestamp you could depart on a bus</em>. The second line lists the bus IDs that are in service according to the shuttle company; entries that show <code>x</code> must be out of service, so you decide to ignore them.</p>
# MAGIC <p>To save time once you arrive, your goal is to figure out <em>the earliest bus you can take to the airport</em>. (There will be exactly one such bus.)</p>
# MAGIC <p>For example, suppose you have the following notes:</p>
# MAGIC <pre><code>939
# MAGIC 7,13,x,x,59,x,31,19
# MAGIC </code></pre>
# MAGIC <p>Here, the earliest timestamp you could depart is <code>939</code>, and the bus IDs in service are <code>7</code>, <code>13</code>, <code>59</code>, <code>31</code>, and <code>19</code>. Near timestamp <code>939</code>, these bus IDs depart at the times marked <code>D</code>:</p>
# MAGIC <pre><code>time   bus 7   bus 13  bus 59  bus 31  bus 19
# MAGIC 929      .       .       .       .       .
# MAGIC 930      .       .       .       D       .
# MAGIC 931      D       .       .       .       D
# MAGIC 932      .       .       .       .       .
# MAGIC 933      .       .       .       .       .
# MAGIC 934      .       .       .       .       .
# MAGIC 935      .       .       .       .       .
# MAGIC 936      .       D       .       .       .
# MAGIC 937      .       .       .       .       .
# MAGIC 938      D       .       .       .       .
# MAGIC <em>939      .       .       .       .       .</em>
# MAGIC 940      .       .       .       .       .
# MAGIC 941      .       .       .       .       .
# MAGIC 942      .       .       .       .       .
# MAGIC 943      .       .       .       .       .
# MAGIC <em>944      .       .       D       .       .</em>
# MAGIC 945      D       .       .       .       .
# MAGIC 946      .       .       .       .       .
# MAGIC 947      .       .       .       .       .
# MAGIC 948      .       .       .       .       .
# MAGIC 949      .       D       .       .       .
# MAGIC </code></pre>
# MAGIC <p>The earliest bus you could take is bus ID <code>59</code>. It doesn't depart until timestamp <code>944</code>, so you would need to wait <code>944 - 939 = 5</code> minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives <em><code>295</code></em>.</p>
# MAGIC <p><em>What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''1000303
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19'''

# COMMAND ----------

import math

start, buses = inp.splitlines()
start = int(start)
buses = {i: int(x) for i, x in enumerate(buses.split(',')) if x != 'x'}

t, bus = min((bus * math.ceil(start / bus), bus) for bus in buses.values())

answer = (t - start) * bus
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The shuttle company is running a <span title="This is why you should never let me design a contest for a shuttle company.">contest</span>: one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. (The first line in your input is no longer relevant.)</p>
# MAGIC <p>For example, suppose you have the same list of bus IDs as above:</p>
# MAGIC <pre><code>7,13,x,x,59,x,31,19</code></pre>
# MAGIC <p>An <code>x</code> in the schedule means there are no constraints on what bus IDs must depart at that time.</p>
# MAGIC <p>This means you are looking for the earliest timestamp (called <code>t</code>) such that:</p>
# MAGIC <ul>
# MAGIC <li>Bus ID <code>7</code> departs at timestamp <code>t</code>.
# MAGIC </li><li>Bus ID <code>13</code> departs one minute after timestamp <code>t</code>.</li>
# MAGIC <li>There are no requirements or restrictions on departures at two or three minutes after timestamp <code>t</code>.</li>
# MAGIC <li>Bus ID <code>59</code> departs four minutes after timestamp <code>t</code>.</li>
# MAGIC <li>There are no requirements or restrictions on departures at five minutes after timestamp <code>t</code>.</li>
# MAGIC <li>Bus ID <code>31</code> departs six minutes after timestamp <code>t</code>.</li>
# MAGIC <li>Bus ID <code>19</code> departs seven minutes after timestamp <code>t</code>.</li>
# MAGIC </ul>
# MAGIC <p>The only bus departures that matter are the listed bus IDs at their specific offsets from <code>t</code>. Those bus IDs can depart at other times, and other bus IDs can depart at those times.  For example, in the list above, because bus ID <code>19</code> must depart seven minutes after the timestamp at which bus ID <code>7</code> departs, bus ID <code>7</code> will always <em>also</em> be departing with bus ID <code>19</code> at seven minutes after timestamp <code>t</code>.</p>
# MAGIC <p>In this example, the earliest timestamp at which this occurs is <em><code>1068781</code></em>:</p>
# MAGIC <pre><code>time     bus 7   bus 13  bus 59  bus 31  bus 19
# MAGIC 1068773    .       .       .       .       .
# MAGIC 1068774    D       .       .       .       .
# MAGIC 1068775    .       .       .       .       .
# MAGIC 1068776    .       .       .       .       .
# MAGIC 1068777    .       .       .       .       .
# MAGIC 1068778    .       .       .       .       .
# MAGIC 1068779    .       .       .       .       .
# MAGIC 1068780    .       .       .       .       .
# MAGIC <em>1068781</em>    <em>D</em>       .       .       .       .
# MAGIC <em>1068782</em>    .       <em>D</em>       .       .       .
# MAGIC <em>1068783</em>    .       .       .       .       .
# MAGIC <em>1068784</em>    .       .       .       .       .
# MAGIC <em>1068785</em>    .       .       <em>D</em>       .       .
# MAGIC <em>1068786</em>    .       .       .       .       .
# MAGIC <em>1068787</em>    .       .       .       <em>D</em>       .
# MAGIC <em>1068788</em>    D       .       .       .       <em>D</em>
# MAGIC 1068789    .       .       .       .       .
# MAGIC 1068790    .       .       .       .       .
# MAGIC 1068791    .       .       .       .       .
# MAGIC 1068792    .       .       .       .       .
# MAGIC 1068793    .       .       .       .       .
# MAGIC 1068794    .       .       .       .       .
# MAGIC 1068795    D       D       .       .       .
# MAGIC 1068796    .       .       .       .       .
# MAGIC 1068797    .       .       .       .       .
# MAGIC </code></pre>
# MAGIC <p>In the above example, bus ID <code>7</code> departs at timestamp <code>1068788</code> (seven minutes after <code>t</code>). This is fine; the only requirement on that minute is that bus ID <code>19</code> departs then, and it does.</p>
# MAGIC <p>Here are some other examples:</p>
# MAGIC <ul>
# MAGIC <li>The earliest timestamp that matches the list <code>17,x,13,19</code> is <em><code>3417</code></em>.</li>
# MAGIC <li><code>67,7,59,61</code> first occurs at timestamp <em><code>754018</code></em>.</li>
# MAGIC <li><code>67,x,7,59,61</code> first occurs at timestamp <em><code>779210</code></em>.</li>
# MAGIC <li><code>67,7,x,59,61</code> first occurs at timestamp <em><code>1261476</code></em>.</li>
# MAGIC <li><code>1789,37,47,1889</code> first occurs at timestamp <em><code>1202161486</code></em>.</li>
# MAGIC </ul>
# MAGIC <p>However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than <code>100000000000000</code>!</p>
# MAGIC <p><em>What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?</em></p>
# MAGIC </article>

# COMMAND ----------

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
import functools

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
      return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    s = 0
    prod = functools.reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod

mod = buses.values()
a = [(bus - i) % bus for i, bus in buses.items()]

answer = chinese_remainder(mod, a)
print(answer)
