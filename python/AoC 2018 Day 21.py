# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Chronal Conversion ---</h2><p>You should have been watching where you were going, because as you wander the new North Pole base, you trip and fall into a very deep hole!</p>
# MAGIC <p><span title="The old time travel hole gag! Classic.">Just kidding.</span>  You're falling through time again.</p>
# MAGIC <p>If you keep up your current pace, you should have resolved all of the temporal anomalies by the next time the device activates. Since you have very little interest in browsing history in 500-year increments for the rest of your life, you need to find a way to get back to your present time.</p>
# MAGIC <p>After a little research, you discover two important facts about the behavior of the device:</p>
# MAGIC <p>First, you discover that the device is hard-wired to always send you back in time in 500-year increments. Changing this is probably not feasible.</p>
# MAGIC <p>Second, you discover the <em>activation system</em> (your puzzle input) for the time travel module.  Currently, it appears to <em>run forever without halting</em>.</p>
# MAGIC <p>If you can cause the activation system to <em>halt</em> at a specific moment, maybe you can make the device send you so far back in time that you cause an <a href="https://cwe.mitre.org/data/definitions/191.html">integer underflow</a> <em>in time itself</em> and wrap around back to your current time!</p>
# MAGIC <p>The device executes the program as specified in <a href="16">manual section one</a> and <a href="19">manual section two</a>.</p>
# MAGIC <p>Your goal is to figure out how the program works and cause it to halt.  You can only control <em>register <code>0</code></em>; every other register begins at <code>0</code> as usual.</p>
# MAGIC <p>Because time travel is a dangerous activity, the activation system begins with a few instructions which verify that <em>bitwise AND</em> (via <code>bani</code>) does a <em>numeric</em> operation and <em>not</em> an operation as if the inputs were interpreted as strings. If the test fails, it enters an infinite loop re-running the test instead of allowing the program to execute normally.  If the test passes, the program continues, and assumes that <em>all other bitwise operations</em> (<code>banr</code>, <code>bori</code>, and <code>borr</code>) also interpret their inputs as <em>numbers</em>. (Clearly, the Elves who wrote this system were worried that someone might introduce a bug while trying to emulate this system with a scripting language.)</p>
# MAGIC <p><em>What is the lowest non-negative integer value for register <code>0</code> that causes the program to halt after executing the fewest instructions?</em> (Executing the same instruction multiple times counts as multiple instructions executed.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''#ip 2
seti 123 0 3
bani 3 456 3
eqri 3 72 3
addr 3 2 2
seti 0 0 2
seti 0 4 3
bori 3 65536 4
seti 1107552 3 3
bani 4 255 5
addr 3 5 3
bani 3 16777215 3
muli 3 65899 3
bani 3 16777215 3
gtir 256 4 5
addr 5 2 2
addi 2 1 2
seti 27 0 2
seti 0 2 5
addi 5 1 1
muli 1 256 1
gtrr 1 4 1
addr 1 2 2
addi 2 1 2
seti 25 3 2
addi 5 1 5
seti 17 3 2
setr 5 3 4
seti 7 4 2
eqrr 3 0 5
addr 5 2 2
seti 5 8 2'''

# COMMAND ----------

# Label |  Line  |    Instruction          |    V1                             |    V2                     |  V3                         | V3
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
#       |  0     |    seti 123 0 3         |    r3 = 123                       |    ;                      |  ;                          | 
# Z:    |  1     |    bani 3 456 3         |    r3 = r3 & 456                  |    ;                      |  ;                          | 
#       |  2     |    eqri 3 72 3          |    r3 = r3 == 72                  |    ;                      |  ;                          | 
#       |  3     |    addr 3 2 2           |    r2 += r3; GOTO A               |    ;                      |  ;                          | 
#       |  4     |    seti 0 0 2           |    r2 = 0; GOTO Z                 |    ;                      |  ;                          | 
# A:    |  5     |    seti 0 4 3           |    r3 = 0;                        |    ;                      |  ;                          | 
# K:    |  6     |    bori 3 65536 4       |    r4 = r3 | 65536                |    r4 = r3 | 65536        |  REPEAT { r4 = 65536        | 
#       |  7     |    seti 1107552 3 3     |    r3 = 1107552                   |    r3 = 1107552           |    r3 = 1107552             | 
# J:    |  8     |    bani 4 255 5         |    r5 = r4 & 255                  |    r5 = r4 & 255          |J:  REPEAT { r5 = r4 & 255   | 
#       |  9     |    addr 3 5 3           |    r3 += r5                       |    r3 += r5               |      r3 += r5               | 
#       |  10    |    bani 3 16777215 3    |    r3 &= 16777215                 |    r3 &= 16777215         |      r3 &= 16777215         | 
#       |  11    |    muli 3 65899 3       |    r3 *= 65899                    |    r3 *= 65899            |      r3 *= 65899            | 
#       |  12    |    bani 3 16777215 3    |    r3 &= 16777215                 |    r3 &= 16777215         |      r3 &= 16777215         | 
#       |  13    |    gtir 256 4 5         |    r5 = 256 > r4                  |    ;                      |      ;                      | 
#       |  14    |    addr 5 2 2           |    r2 += r5; IF r5 THEN GOTO B    |    IF 256 > r4 GOTO D     |      IF 256 > r4 THEN BREAK | 
#       |  15    |    addi 2 1 2           |    r2 += 1; GOTO C                |    ;                      |      ;                      | 
# B:    |  16    |    seti 27 0 2          |    r2 = 27; GOTO D                |    ;                      |      ;                      | 
# C:    |  17    |    seti 0 2 5           |    r5 = 0                         |    r5 = 0                 |      r5 = 0                 |     
# I:    |  18    |    addi 5 1 1           |    r1 = r5 + 1                    |    r1 = r5 + 1            |I:    REPEAT { r1 = r5 + 1   |     ;
#       |  19    |    muli 1 256 1         |    r1 *= 256                      |    r1 *= 256              |        r1 *= 256            |     ;
#       |  20    |    gtrr 1 4 1           |    r1 = r1 > r4                   |    ;                      |        ;                    |     ;
#       |  21    |    addr 1 2 2           |    r2 += r1; IF r1 THEN GOTO E    |    IF r1 > r4 GOTO G      |        IF r1 > r4 THEN BREAK|     ;
#       |  22    |    addi 2 1 2           |    r2 += 1; GOTO F                |    ;                      |        ;                    |     ;
# E:    |  23    |    seti 25 3 2          |    r2 = 25; GOTO G                |    ;                      |        ;                    |     ;
# F:    |  24    |    addi 5 1 5           |    r5++                           |    r5++                   |        r5++                 |     ;
#       |  25    |    seti 17 3 2          |    r2 = 17; GOTO I                |    GOTO I                 |      }                      |     ;
# G:    |  26    |    setr 5 3 4           |    r4 = r5                        |    r4 = r5                |G:    r4 = r5                |     r4 = r4 // 256
#       |  27    |    seti 7 4 2           |    r2 = 7; GOTO J                 |    GOTO J                 |    }                        | 
# D:    |  28    |    eqrr 3 0 5           |    r5 = r3 == r0                  |    ;                      |D:  ;                        | 
#       |  29    |    addr 5 2 2           |    r2 += r5; IF r5 THEN HALT      |    IF r3 == r0 THEN HALT  |    IF r3 == r0 THEN HALT    | 
#       |  30    |    seti 5 8 2           |    r2 = 5; GOTO K                 |    GOTO K                 |  }                          | 

# COMMAND ----------

import collections
import re

def execute(op, a, b, c, r):
  if op in ('addi', 'addr', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'gtri', 'gtrr', 'eqri', 'eqrr', 'divi'):
    a = r[a]
  if op in ('addr', 'mulr', 'banr', 'borr', 'gtir', 'gtrr', 'eqir', 'eqrr'):
    b = r[b]
  
  if op.startswith('add'):
    r[c] = a + b
  elif op.startswith('mul'):
    r[c] = a * b
  elif op.startswith('ban'):
    r[c] = a & b
  elif op.startswith('bor'):
    r[c] = a | b
  elif op.startswith('set'):
    r[c] = a
  elif op.startswith('gt'):
    r[c] = int(a > b)
  elif op.startswith('eq'):
    r[c] = int(a == b)
  elif op.startswith('divi'):
    r[c] = a // b
  elif op.startswith('nop'):
    pass

def solve(ip, instructions):
  instructions = instructions.copy()
  instructions[29] = ['setr', 3, 0, -1]
  
  # Optimization
  for i in range(18, 26):
    instructions[i] = ['nop', 0, 0, 0]
  instructions[26] = ['divi', 4, 256, 4]
  
  first_result = None
  last_result = None
  
  seen = set()
  r = collections.defaultdict(int)
  while True:
    r[-1] = None
    execute(*instructions[r[ip]], r)
    
    if r[-1] is not None:
      if r[-1] in seen:
        break
      seen.add(r[-1])
      first_result = first_result or r[-1]
      last_result = r[-1]
    r[ip] += 1
  
  return first_result, last_result

ip, *instructions = inp.splitlines()
ip = int(re.findall(r'\d+', ip)[0])
instructions = [[f(x) for f, x in zip((str, int, int, int), line.split(' '))] for line in instructions]

first_result, last_result = solve(ip, instructions)

answer = first_result
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>In order to determine the timing window for your underflow exploit, you also need an upper bound:</p>
# MAGIC <p><em>What is the lowest non-negative integer value for register <code>0</code> that causes the program to halt after executing the most instructions?</em> (The program must actually halt; running forever does not count as halting.)</p>
# MAGIC </article>

# COMMAND ----------

answer = last_result
print(answer)
