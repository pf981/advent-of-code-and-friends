# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/25

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 25: Full of Hot Air ---</h2><p>As the expedition finally reaches the extraction point, several large <a href="https://en.wikipedia.org/wiki/Hot_air_balloon" target="_blank">hot air balloons</a> drift down to meet you. Crews quickly start unloading the equipment the balloons brought: many hot air balloon kits, some fuel tanks, and a <em>fuel heating machine</em>.</p>
# MAGIC <p>The fuel heating machine is a new addition to the process. When this mountain was a volcano, the ambient temperature was more reasonable; now, it's so cold that the fuel won't work at all without being warmed up first.</p>
# MAGIC <p>The Elves, seemingly in an attempt to make the new machine feel welcome, have already attached a pair of <a href="https://en.wikipedia.org/wiki/Googly_eyes" target="_blank">googly eyes</a> and started calling it "Bob".</p>
# MAGIC <p>To heat the fuel, Bob needs to know the total amount of fuel that will be processed ahead of time so it can correctly calibrate heat output and flow rate. This amount is simply the <em>sum</em> of the fuel requirements of all of the hot air balloons, and those fuel requirements are even listed clearly on the side of each hot air balloon's burner.</p>
# MAGIC <p>You assume the Elves will have no trouble adding up some numbers and are about to go back to figuring out which balloon is yours when you get a tap on the shoulder. Apparently, the fuel requirements use numbers written in a format the Elves don't recognize; predictably, they'd like your help deciphering them.</p>
# MAGIC <p>You make a list of all of the fuel requirements (your puzzle input), but you don't recognize the number format either. For example:</p>
# MAGIC <pre><code>1=-0-2
# MAGIC 12111
# MAGIC 2=0=
# MAGIC 21
# MAGIC 2=01
# MAGIC 111
# MAGIC 20012
# MAGIC 112
# MAGIC 1=-1=
# MAGIC 1-12
# MAGIC 12
# MAGIC 1=
# MAGIC 122
# MAGIC </code></pre>
# MAGIC <p>Fortunately, Bob is labeled with a support phone number. Not to be deterred, you call and ask for help.</p>
# MAGIC <p>"That's right, just supply the fuel amount to the-- oh, for more than one burner? No problem, you just need to add together our Special Numeral-Analogue Fuel Units. Patent pending! They're way better than normal numbers for--"</p>
# MAGIC <p>You mention that it's quite cold up here and ask if they can skip ahead.</p>
# MAGIC <p>"Okay, our Special Numeral-Analogue Fuel Units - SNAFU for short - are sort of like normal numbers. You know how starting on the right, normal numbers have a ones place, a tens place, a hundreds place, and so on, where the digit in each place tells you how many of that value you have?"</p>
# MAGIC <p>"SNAFU works the same way, except it uses powers of five instead of ten. Starting from the right, you have a ones place, a fives place, a twenty-fives place, a one-hundred-and-twenty-fives place, and so on. It's that easy!"</p>
# MAGIC <p>You ask why some of the digits look like <code>-</code> or <code>=</code> instead of "digits".</p>
# MAGIC <p>"You know, I never did ask the engineers why they did that. Instead of using digits four through zero, the digits are <code><em>2</em></code>, <code><em>1</em></code>, <code><em>0</em></code>, <em>minus</em> (written <code>-</code>), and <em>double-minus</em> (written <code>=</code>). Minus is worth -1, and double-minus is worth -2."</p>
# MAGIC <p>"So, because ten (in normal numbers) is two fives and no ones, in SNAFU it is written <code>20</code>. Since eight (in normal numbers) is two fives minus two ones, it is written <code>2=</code>."</p>
# MAGIC <p>"You can do it the other direction, too. Say you have the SNAFU number <code>2=-01</code>. That's <code>2</code> in the 625s place, <code>=</code> (double-minus) in the 125s place, <code>-</code> (minus) in the 25s place, <code>0</code> in the 5s place, and <code>1</code> in the 1s place. (2 times 625) plus (-2 times 125) plus (-1 times 25) plus (0 times 5) plus (1 times 1). That's 1250 plus -250 plus -25 plus 0 plus 1. <em>976</em>!"</p>
# MAGIC <p>"I see here that you're connected via our premium uplink service, so I'll transmit our handy SNAFU brochure to you now. Did you need anything else?"</p>
# MAGIC <p>You ask if the fuel will even work in these temperatures.</p>
# MAGIC <p>"Wait, it's <em>how</em> cold? There's no <em>way</em> the fuel - or <em>any</em> fuel - would work in those conditions! There are only a few places in the-- where did you say you are again?"</p>
# MAGIC <p>Just then, you notice one of the Elves pour a few drops from a snowflake-shaped container into one of the fuel tanks, thank the support representative for their time, and disconnect the call.</p>
# MAGIC <p>The SNAFU brochure contains a few more examples of decimal ("normal") numbers and their SNAFU counterparts:</p>
# MAGIC <pre><code>  Decimal          SNAFU
# MAGIC         1              1
# MAGIC         2              2
# MAGIC         3             1=
# MAGIC         4             1-
# MAGIC         5             10
# MAGIC         6             11
# MAGIC         7             12
# MAGIC         8             2=
# MAGIC         9             2-
# MAGIC        10             20
# MAGIC        15            1=0
# MAGIC        20            1-0
# MAGIC      2022         1=11-2
# MAGIC     12345        1-0---0
# MAGIC 314159265  1121-1110-1=0
# MAGIC </code></pre>
# MAGIC <p>Based on this process, the SNAFU numbers in the example above can be converted to decimal numbers as follows:</p>
# MAGIC <pre><code> SNAFU  Decimal
# MAGIC 1=-0-2     1747
# MAGIC  12111      906
# MAGIC   2=0=      198
# MAGIC     21       11
# MAGIC   2=01      201
# MAGIC    111       31
# MAGIC  20012     1257
# MAGIC    112       32
# MAGIC  1=-1=      353
# MAGIC   1-12      107
# MAGIC     12        7
# MAGIC     1=        3
# MAGIC    122       37
# MAGIC </code></pre>
# MAGIC <p>In decimal, the sum of these numbers is <code>4890</code>.</p>
# MAGIC <p>As you go to input this number on Bob's console, you discover that some buttons you expected are missing. Instead, you are met with buttons labeled <code>=</code>, <code>-</code>, <code>0</code>, <code>1</code>, and <code>2</code>. Bob needs the input value expressed as a SNAFU number, not in decimal.</p>
# MAGIC <p>Reversing the process, you can determine that for the decimal number <code>4890</code>, the SNAFU number you need to supply to Bob's console is <code><em>2=-1=0</em></code>.</p>
# MAGIC <p>The Elves are starting to get cold. <em>What SNAFU number do you supply to Bob's console?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''212===
1-1=1-1=1=0-=2
1=12002=011-
1220221=2==0
10=22-1-1121=
100--2
1-0002-2020=2-1=
2
2-20020
202120-=-11-22-12-
1-==1-=0-=211-2
120=-02
1=11=-21210-
10=-1-11=110--=22=
1=10-1-00
11-=
22
21=2-121-2
12101122=
1=01=20=
1--=2-20
220=121001-1==1-
1=01122
21=2212-=000200
1210
2102=-
22-010=-1=2=--=-
1-2-=
1-10==22=0
1-=0-101222
20000-==-==00=1
11-21120----20-1
1=02022012=12=20-2
1=1
2-=11=00=-202
1-022211
1221-
1--=
21=010202
1==110=-02022=
2-20=01-=011-10
11-0=
1=0-20-22-11-=-
1010-01202==0221=2
122=-==2001
1001-0-=-1=-1-=
100111==10----1010
112-20-0==-02
20=22-21200
22-212-010===-21=0
2-2122
2-
21022011=122=1-1
10=0=22101-=0--22=
21-110121--12
1==102102==-=-12=
1---2-2----222-2
2=2==12-0==110120
2-1=
10-0=2=-1=1=10-
22=0-2202210-10222
1==
2-20212=1-
2-01--==12-2=2
200=1
1-2020--=111101-1
1=111-0=0
1=11
2-=-
10100200--
2=102=121
1=020=0-2
11-11-01001001-2
20-0-120====-
1=-=-21120021-12===
1000-2
201022020-12
12=-2222=200=--0=20
1===201-220
10-2-
102==---=-1=-01=
1----=0=-===2020-22
1=011212-10=
1=1-1022
1==12200-0=211---21=
1=100==--=2--0001-
11021=
12
2001
202
222
10-20221-2-2
1-=20-2=1
1-0=10-0-
2-0-12-=1
2--1-2-==0-2101=
12=02121
12210=--1=-2-0
2=221-
122-=-21-02
1=0112-=0=2=0-
1=20--22
1=11=
1-2210=--202=--1
202=0=102=
10-=0=-0-02=
1-02=2=021
12=-21221
2-110=1--001=112-2
111-12==--=
10200=020-2=0221==
2-0--=-'''

# COMMAND ----------

import functools
import math


to_num = {
  '2': 2,
  '1': 1,
  '0': 0,
  '-': -1,
  '=': -2
}
to_string = {
  2: '2',
  1: '1',
  0: '0',
  -1: '-',
  -2: '='
}


def get_value(s):
  return sum((5**exponent) * to_num[c] for exponent, c in enumerate(s[::-1]))


@functools.cache
def make_string(target, digits):
  if digits == 1:
    return to_string.get(target)

  if abs(target) > 5**digits:
    return None
  
  coef = 5**(digits-1)
  for value, c in to_string.items():
    if (result := make_string(target - value*coef, digits - 1)) is not None:
      return c + result


target = sum(get_value(line) for line in inp.splitlines())
digits_upper_bound = int(math.log(target, 5) + 2)
answer = make_string(target, digits_upper_bound).lstrip('0')
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The <span title="You notice an engraving on the equipment: Balanced Quinary Industries.">hot air balloons</span> quickly carry you to the North Pole. As soon as you land, most of the expedition is escorted directly to a small building attached to the reindeer stables.</p>
# MAGIC <p>The <em>head smoothie chef</em> has just finished warming up the industrial-grade smoothie blender as you arrive. It will take <em class="star">50 stars</em> to fill the blender. The expedition Elves turn their attention to you, and you begin emptying the fruit from your pack onto the table.</p>
# MAGIC <p>As you do, a very young Elf - one you recognize from the expedition team - approaches the table and holds up a single <em class="star">star</em> fruit he found. The head smoothie chef places it in the blender.</p>
# MAGIC <p>Only <em class="star">49 stars</em> to go.</p>
# MAGIC </article>

# COMMAND ----------

# No puzzle here - just need 49 stars.
