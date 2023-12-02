# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/2

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 2: Cube Conundrum ---</h2><p>You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.</p>
# MAGIC <p>The Elf explains that you've arrived at <em>Snow Island</em> and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; <span title="No, the Elf's name is not 'WOPR'. It's Joshua.">would you like to play a game</span> in the meantime?</p>
# MAGIC <p>As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.</p>
# MAGIC <p>To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.</p>
# MAGIC <p>You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the <code>11</code> in <code>Game 11: ...</code>) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like <code>3 red, 5 green, 4 blue</code>).</p>
# MAGIC <p>For example, the record of a few games might look like this:</p>
# MAGIC <pre><code>Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# MAGIC Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# MAGIC Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# MAGIC Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# MAGIC Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# MAGIC </code></pre>
# MAGIC <p>In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.</p>
# MAGIC <p>The Elf would first like to know which games would have been possible if the bag contained <em>only 12 red cubes, 13 green cubes, and 14 blue cubes</em>?</p>
# MAGIC <p>In the example above, games 1, 2, and 5 would have been <em>possible</em> if the bag had been loaded with that configuration. However, game 3 would have been <em>impossible</em> because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been <em>impossible</em> because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get <code><em>8</em></code>.</p>
# MAGIC <p>Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. <em>What is the sum of the IDs of those games?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Game 1: 10 green, 5 blue; 1 red, 9 green, 10 blue; 5 blue, 6 green, 2 red; 7 green, 9 blue, 1 red; 2 red, 10 blue, 10 green; 7 blue, 1 red
Game 2: 7 green, 5 red, 3 blue; 4 blue, 7 green, 8 red; 9 blue, 4 green; 6 green, 3 red, 4 blue
Game 3: 2 green, 4 blue, 13 red; 15 blue, 9 red, 3 green; 3 red, 18 blue, 3 green; 6 red, 4 green, 2 blue; 6 blue, 13 red
Game 4: 9 red, 1 green, 13 blue; 3 red; 2 blue, 6 red, 1 green; 12 blue, 2 red
Game 5: 1 red, 8 green; 2 red, 8 green, 8 blue; 1 red, 11 green; 5 blue, 11 green; 11 blue, 2 green; 10 blue, 2 red, 1 green
Game 6: 1 red, 12 blue; 20 blue, 3 green, 2 red; 4 red, 15 blue
Game 7: 13 red, 9 green, 1 blue; 8 green, 2 red, 6 blue; 4 green, 5 blue; 7 red, 3 green, 7 blue; 19 red, 5 blue, 1 green
Game 8: 11 red, 14 green, 4 blue; 2 blue, 5 green, 16 red; 18 blue, 11 red, 2 green; 2 blue, 15 red; 13 green, 8 blue
Game 9: 7 green, 5 blue, 11 red; 10 red, 7 green, 4 blue; 1 red; 6 green, 2 blue, 9 red; 8 green, 10 red, 6 blue; 5 red, 5 green, 7 blue
Game 10: 4 blue, 2 green, 1 red; 5 green, 2 red, 1 blue; 3 green, 8 blue, 1 red; 2 blue, 6 green, 2 red; 1 red, 4 green, 2 blue
Game 11: 3 red, 4 blue; 8 blue, 7 green, 2 red; 7 blue, 1 red, 6 green; 13 blue, 4 green
Game 12: 2 red, 3 blue, 4 green; 2 blue, 9 red, 8 green; 10 red, 1 blue; 1 green, 7 red, 3 blue; 7 red, 2 blue, 9 green
Game 13: 12 red, 6 green, 2 blue; 15 green, 2 red, 4 blue; 7 green, 1 red, 3 blue
Game 14: 9 green, 4 red; 6 blue, 1 red, 7 green; 3 blue, 5 green
Game 15: 7 red, 3 green, 2 blue; 3 blue, 4 green; 4 blue, 4 green, 9 red
Game 16: 12 blue, 11 green, 4 red; 8 blue, 9 red, 10 green; 9 green, 11 blue, 13 red; 10 red, 5 blue, 6 green; 2 red; 2 blue, 5 green, 5 red
Game 17: 3 red, 2 green, 2 blue; 1 blue, 3 red, 1 green; 10 green
Game 18: 3 green, 1 blue, 4 red; 12 red, 5 green; 3 red, 3 green, 3 blue; 13 red, 2 blue
Game 19: 13 blue, 8 green, 6 red; 10 red, 12 blue; 8 green, 13 red, 9 blue; 13 green, 3 red, 5 blue; 5 green, 1 blue, 2 red
Game 20: 19 red, 13 blue, 4 green; 1 red, 4 green, 8 blue; 14 red, 6 blue, 7 green; 11 red, 13 blue, 8 green
Game 21: 3 green, 13 red, 7 blue; 1 blue, 1 green, 1 red; 3 blue, 15 red, 5 green; 3 blue, 15 red, 2 green; 6 green, 9 red, 14 blue
Game 22: 2 red, 6 green, 4 blue; 6 green, 2 red; 1 blue, 4 red, 3 green; 11 green, 7 blue, 1 red; 4 red, 8 green, 3 blue
Game 23: 14 blue; 3 green, 2 red, 3 blue; 5 blue, 1 red
Game 24: 12 red; 5 blue, 16 red; 2 blue, 1 green, 16 red; 1 green, 11 red; 2 blue, 8 red, 1 green
Game 25: 4 red, 11 blue, 1 green; 7 red, 9 blue; 6 blue, 10 green
Game 26: 3 green, 13 red; 7 blue, 13 red, 5 green; 5 blue, 8 green, 11 red; 7 blue, 18 green, 6 red
Game 27: 6 green, 6 red, 5 blue; 2 blue, 4 green, 11 red; 15 red, 6 green; 4 green, 12 red, 2 blue; 3 blue, 5 red
Game 28: 16 blue, 6 red, 1 green; 7 red, 4 green, 10 blue; 1 red, 4 green
Game 29: 5 blue, 4 red; 6 blue, 3 red, 4 green; 2 green, 4 red, 5 blue; 1 green, 7 blue, 4 red; 3 green, 2 blue, 4 red
Game 30: 2 green; 14 green, 1 blue, 2 red; 5 red, 14 green
Game 31: 9 blue, 6 red, 7 green; 20 red, 1 green, 15 blue; 6 blue, 7 green, 17 red; 2 blue, 3 green, 6 red; 1 red, 3 blue, 2 green; 5 green, 18 red, 6 blue
Game 32: 7 green, 9 blue, 8 red; 8 red, 13 green, 19 blue; 2 red, 9 blue, 3 green; 9 green, 6 blue, 6 red
Game 33: 6 blue, 12 red; 13 blue, 3 green, 15 red; 5 red, 10 blue, 4 green; 11 blue, 6 red
Game 34: 5 green, 16 blue, 6 red; 10 green, 1 blue, 4 red; 2 red, 7 blue, 6 green; 12 green, 4 blue, 4 red
Game 35: 11 green, 3 blue; 1 red, 6 blue, 10 green; 11 green, 3 blue; 1 red, 2 blue; 11 green, 3 blue, 1 red; 3 blue, 2 green
Game 36: 10 green, 6 red, 4 blue; 3 green, 3 blue, 5 red; 6 red, 5 blue, 10 green
Game 37: 8 red, 7 blue, 5 green; 8 blue, 5 green, 14 red; 8 red, 2 blue
Game 38: 4 green, 1 red, 4 blue; 8 green, 11 blue; 7 red, 5 blue
Game 39: 2 blue, 4 red, 4 green; 8 green, 8 red, 1 blue; 3 red
Game 40: 4 green, 3 red, 14 blue; 4 blue, 13 green, 3 red; 12 green, 2 red, 2 blue; 8 green, 1 red, 11 blue; 4 green, 1 red, 1 blue
Game 41: 4 red, 1 green, 2 blue; 4 red; 4 red
Game 42: 12 red, 8 blue, 1 green; 8 green, 6 red, 5 blue; 12 green, 3 red, 13 blue; 1 red, 2 green, 8 blue; 3 green, 5 red, 6 blue
Game 43: 12 green, 3 blue; 13 green, 7 red, 5 blue; 10 green, 4 red, 4 blue
Game 44: 6 green, 2 red, 4 blue; 10 green, 6 red; 5 blue, 15 red, 13 green; 1 blue, 6 red, 3 green; 9 red, 5 green, 3 blue; 6 green, 4 blue, 5 red
Game 45: 10 blue, 14 green; 2 green, 2 red, 12 blue; 7 green, 1 red; 8 blue, 6 green, 1 red
Game 46: 8 red, 10 green, 15 blue; 9 green, 3 red, 17 blue; 2 blue, 10 red, 5 green; 11 blue, 3 green, 9 red; 5 red, 11 blue, 1 green; 7 green, 5 red, 16 blue
Game 47: 10 blue, 1 green, 1 red; 3 red, 8 blue, 7 green; 8 red, 9 blue; 2 green, 8 red, 1 blue
Game 48: 5 blue, 2 green; 2 red, 7 green, 2 blue; 1 blue, 3 green, 1 red
Game 49: 2 green, 6 red, 5 blue; 6 green; 4 blue, 17 red, 5 green
Game 50: 5 blue, 10 green; 6 blue, 4 red, 9 green; 7 red, 4 blue; 7 red, 3 blue, 14 green; 5 blue, 10 green, 9 red; 13 green, 1 blue, 9 red
Game 51: 1 blue, 15 green; 6 green, 2 blue; 5 blue, 1 red, 12 green
Game 52: 3 red, 15 green; 7 blue, 1 red, 14 green; 8 green, 1 red, 12 blue; 1 red, 9 green, 7 blue
Game 53: 2 green, 4 red; 1 red, 1 blue; 3 blue, 1 green; 2 red, 2 blue, 2 green
Game 54: 7 blue, 13 red, 7 green; 1 red, 2 green; 11 red, 10 green, 5 blue; 10 red, 8 green, 5 blue; 8 green, 12 blue, 12 red
Game 55: 18 red, 3 green, 5 blue; 5 green, 3 blue, 7 red; 3 blue, 3 green, 4 red
Game 56: 14 red, 17 green, 2 blue; 5 green, 13 red, 1 blue; 11 red, 20 green
Game 57: 3 red, 6 green, 2 blue; 3 red, 2 green; 2 green, 5 red; 1 blue, 1 green, 2 red
Game 58: 7 blue, 5 green, 9 red; 10 red, 5 green, 9 blue; 2 blue, 3 red, 8 green; 8 blue, 9 red; 7 red, 3 blue, 7 green; 2 green, 7 red, 1 blue
Game 59: 4 green, 3 blue; 10 red, 4 green, 4 blue; 2 green, 14 red, 12 blue; 1 blue, 1 green, 13 red; 10 red, 3 green, 3 blue; 2 green
Game 60: 9 red, 13 blue; 2 green, 5 red, 9 blue; 3 green, 10 blue
Game 61: 2 red, 8 green, 4 blue; 3 green, 2 red; 10 red, 9 green, 12 blue; 11 green, 17 blue, 3 red; 7 green, 1 red, 14 blue
Game 62: 1 green, 5 red, 13 blue; 5 blue, 1 green, 8 red; 2 green, 8 blue, 3 red; 1 green, 8 red
Game 63: 8 green, 15 red, 2 blue; 4 blue, 3 red, 12 green; 4 green, 1 blue, 17 red; 9 green, 18 red, 4 blue
Game 64: 7 blue, 17 red, 17 green; 3 blue, 4 green, 3 red; 4 red, 19 green, 1 blue; 11 blue, 14 red; 4 blue, 19 green, 7 red; 1 red, 10 green, 11 blue
Game 65: 1 blue, 17 red, 5 green; 17 red, 3 blue, 2 green; 10 blue, 9 green
Game 66: 5 blue, 6 red; 8 red, 2 blue, 1 green; 2 green, 3 blue; 8 blue, 10 red; 1 green, 2 red, 5 blue; 1 red, 3 blue
Game 67: 12 green, 16 blue, 12 red; 15 red, 1 blue, 3 green; 10 red, 3 green, 10 blue; 2 blue, 6 green, 6 red; 9 red, 8 blue, 7 green
Game 68: 10 red, 7 blue; 12 blue, 9 red; 12 blue, 9 red, 2 green
Game 69: 14 blue, 3 red, 3 green; 7 green, 7 red, 2 blue; 8 blue, 4 green, 8 red; 6 blue, 14 red, 3 green
Game 70: 7 blue, 6 green, 2 red; 2 red, 4 blue, 4 green; 2 red, 5 blue, 3 green; 6 green, 2 blue; 5 blue, 2 red, 2 green
Game 71: 7 green, 15 blue, 3 red; 15 blue, 15 red, 2 green; 10 red, 9 blue; 6 green, 20 blue, 11 red; 12 blue, 3 green, 7 red; 1 red, 7 blue
Game 72: 2 green, 9 blue, 7 red; 5 green, 3 blue, 5 red; 10 blue, 8 red, 7 green
Game 73: 18 blue, 5 red, 1 green; 18 blue, 3 red, 9 green; 2 red, 4 blue, 9 green; 5 blue, 5 red; 2 blue, 10 green, 6 red
Game 74: 1 blue, 10 green, 5 red; 4 green, 12 blue, 6 red; 7 red, 13 green, 3 blue; 5 blue, 8 green, 4 red
Game 75: 4 red, 2 blue, 5 green; 2 blue, 7 red, 4 green; 2 blue, 4 green, 3 red; 12 green, 2 blue; 10 green, 1 blue, 2 red
Game 76: 8 green, 6 blue, 5 red; 1 red, 2 blue, 9 green; 7 red, 9 green; 5 green, 1 blue, 11 red
Game 77: 3 blue, 10 red, 9 green; 7 blue, 6 red, 4 green; 4 red, 1 green, 8 blue
Game 78: 2 blue, 1 red, 14 green; 11 green, 1 blue; 15 green, 1 red
Game 79: 3 green, 17 blue, 1 red; 3 red, 2 blue, 10 green; 13 blue, 11 green, 5 red; 16 blue, 2 green, 16 red; 11 green, 1 blue, 14 red
Game 80: 7 red, 10 blue, 5 green; 6 blue, 6 green, 8 red; 6 blue, 3 green, 5 red
Game 81: 1 blue, 14 red, 6 green; 1 red, 13 blue, 12 green; 2 green, 15 red, 15 blue
Game 82: 5 blue, 8 red, 6 green; 19 blue, 4 green; 9 green, 15 blue, 3 red
Game 83: 19 red, 15 green, 2 blue; 17 red, 4 green, 1 blue; 13 green, 18 red
Game 84: 9 green, 14 red; 11 green, 14 red, 1 blue; 1 blue, 2 red, 3 green; 13 green, 10 red; 1 green, 5 red
Game 85: 4 red, 2 green, 11 blue; 8 blue, 3 red; 4 red, 1 blue, 5 green; 2 red, 3 green; 1 green, 8 red, 12 blue
Game 86: 5 blue, 1 red; 8 blue; 2 red, 1 green, 12 blue; 12 blue, 2 red
Game 87: 3 red, 10 green, 3 blue; 13 blue, 6 red, 2 green; 1 green, 2 red, 10 blue
Game 88: 10 red, 3 green, 8 blue; 3 red, 18 blue, 2 green; 3 green, 15 blue; 15 green, 16 blue, 8 red
Game 89: 10 blue, 1 red; 4 green, 9 red, 13 blue; 10 red, 3 green, 12 blue; 2 green, 1 red, 16 blue; 10 blue, 1 red, 6 green
Game 90: 4 red, 2 blue, 15 green; 5 red, 1 blue, 12 green; 3 blue, 3 red, 7 green; 4 blue, 3 red, 7 green; 1 red, 2 green, 1 blue; 1 blue, 4 green, 3 red
Game 91: 16 red, 10 blue, 1 green; 13 green, 13 red, 19 blue; 11 blue, 12 green, 2 red
Game 92: 8 blue, 4 green, 5 red; 7 blue, 4 red; 2 green, 15 blue; 16 blue, 4 red; 1 red, 7 green, 16 blue; 11 blue, 1 red, 3 green
Game 93: 12 green, 2 blue, 2 red; 8 red, 16 green, 8 blue; 15 red, 4 blue, 7 green; 1 red, 4 blue, 15 green; 13 green, 5 red, 4 blue; 5 green, 8 blue, 12 red
Game 94: 13 green, 10 red; 11 red, 19 green, 1 blue; 1 blue, 10 red, 12 green; 18 green, 9 red, 1 blue; 8 green, 1 red
Game 95: 3 green, 4 blue; 2 red, 2 green, 2 blue; 7 red, 3 green
Game 96: 5 red, 7 green; 4 blue, 14 green, 10 red; 13 green; 13 green, 3 blue; 13 green, 1 red, 3 blue; 12 red, 1 green
Game 97: 2 green, 1 blue; 9 red; 4 blue, 8 red; 4 green, 1 red, 14 blue; 2 green, 9 blue; 1 red, 6 blue, 2 green
Game 98: 12 green, 9 blue, 13 red; 6 red, 7 blue; 2 blue, 2 green
Game 99: 9 red, 3 green, 10 blue; 10 red, 10 blue, 4 green; 2 green, 15 blue, 3 red; 12 blue, 4 red
Game 100: 15 blue, 6 red; 1 green, 2 red; 12 blue, 8 green, 1 red; 1 red, 7 blue
'''

# COMMAND ----------

import re


def extract_cubes(line):
    return [extract_max(line, color) for color in ['red', 'green', 'blue']]


def extract_max(line, c):
    return max(int(num) for num in re.findall(r'(\d+) ' + c, line))


min_cubes = [extract_cubes(line) for line in inp.splitlines()]
answer = sum(i * (cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14) for i, cubes in enumerate(min_cubes, 1))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Elf says they've stopped producing snow because they aren't getting any <em>water</em>! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!</p>
# MAGIC <p>As you continue your walk, the Elf poses a second question: in each game you played, what is the <em>fewest number of cubes of each color</em> that could have been in the bag to make the game possible?</p>
# MAGIC <p>Again consider the example games from earlier:</p>
# MAGIC <pre><code>Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# MAGIC Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# MAGIC Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# MAGIC Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# MAGIC Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.</li>
# MAGIC <li>Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.</li><li>
# MAGIC </li><li>Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.</li>
# MAGIC <li>Game 4 required at least 14 red, 3 green, and 15 blue cubes.</li>
# MAGIC <li>Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.</li>
# MAGIC </ul>
# MAGIC <p>The <em>power</em> of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is <code>48</code>. In games 2-5 it was <code>12</code>, <code>1560</code>, <code>630</code>, and <code>36</code>, respectively. Adding up these five powers produces the sum <code><em>2286</em></code>.</p>
# MAGIC <p>For each game, find the minimum set of cubes that must have been present. <em>What is the sum of the power of these sets?</em></p>
# MAGIC </article>

# COMMAND ----------

import math


answer = sum(math.prod(cubes) for cubes in min_cubes)
print(answer)
