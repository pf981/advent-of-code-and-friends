# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Coprocessor Conflagration ---</h2><p>You decide to head directly to the CPU and fix the printer from there. As you get close, you find an <em>experimental coprocessor</em> doing so much work that the local programs are afraid it will <a href="https://en.wikipedia.org/wiki/Halt_and_Catch_Fire">halt and catch fire</a>. This would cause serious issues for the rest of the computer, so you head in and see what you can do.</p>
# MAGIC <p>The code it's running seems to be a variant of the kind you saw recently on that <a href="18">tablet</a>. The general functionality seems <em>very similar</em>, but some of the instructions are different:</p>
# MAGIC <ul>
# MAGIC <li><code>set X Y</code> <em>sets</em> register <code>X</code> to the value of <code>Y</code>.</li>
# MAGIC <li><code>sub X Y</code> <em>decreases</em> register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>mul X Y</code> sets register <code>X</code> to the result of <em>multiplying</em> the value contained in register <code>X</code> by the value of <code>Y</code>.</li>
# MAGIC <li><code>jnz X Y</code> <em>jumps</em> with an offset of the value of <code>Y</code>, but only if the value of <code>X</code> is <em>not zero</em>. (An offset of <code>2</code> skips the next instruction, an offset of <code>-1</code> jumps to the previous instruction, and so on.)</li>
# MAGIC <p>Only the instructions listed above are used. The eight registers here, named <code>a</code> through <code>h</code>, all start at <code>0</code>.</p>
# MAGIC </ul>
# MAGIC <p>The coprocessor is currently set to some kind of <em>debug mode</em>, which allows for testing, but prevents it from doing any meaningful work.</p>
# MAGIC <p>If you run the program (your puzzle input), <em>how many times is the <code>mul</code> instruction invoked?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''set b 84
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''

# COMMAND ----------

# Label |  Line  |  Instruction   |    V1                  |    V2                   |  V3
# -----------------------------------------------------------------------------------|----------------------------
#       |  0     |  set b 84      | b = 84                 | b = 84                  | b = 84                     
#       |  1     |  set c b       | c = b                  | c = 84                  | c = 84                     
#       |  2     |  jnz a 2       | IF a != 0 THEN GOTO A  | IF part2:               | IF part2:                  
#       |  3     |  jnz 1 5       | GOTO B                 |   ;                     |   ;                        
# A:    |  4     |  mul b 100     | b *= 100               |   b = 108400            |   b = 108400               
#       |  5     |  sub b -100000 | b += 100000            |   ;                     |   ;                        
#       |  6     |  set c b       | c = b                  |   ;                     |   ;                        
#       |  7     |  sub c -17000  | c += 17000             |   c = 125400            |   c = 125400               
# B:    |  8     |  set f 1       | f = 1                  | REPEAT:                 | DO:                        
#       |  9     |  set d 2       | d = 2                  |   f = 1; d = 2          |   no_factors = TRUE        
# E:    |  10    |  set e 2       | e = 2                  |   DO:                   |   FOR d FROM 2 TO b:       
#                                                                e = 2               |     ;                      
# D:    |  11    |  set g d       | g = d                  |     DO:                 |     FOR e FROM 2 TO b:     
#       |  12    |  mul g e       | g *= e                 |       ;                 |       ;                    
#       |  13    |  sub g b       | g -= b                 |       ;                 |       ;                    
#       |  14    |  jnz g 2       | IF g != 0 THEN GOTO C  |       IF d*e == b:      |       IF d*e == b:         
#       |  15    |  set f 0       | f = 0                  |         f = 0           |         no_factors = FALSE 
# C:    |  16    |  sub e -1      | e++                    |       e++               |       ;                    
#       |  17    |  set g e       | g = e                  |       ;                 |       ;                    
#       |  18    |  sub g b       | g -= b                 |       ;                 |       ;                    
#       |  19    |  jnz g -8      | IF g != 0 GOTO D       |     WHILE e != b        |     ;                      
#       |  20    |  sub d -1      | d++                    |     d++                 |     ;                      
#       |  21    |  set g d       | g = d                  |     ;                   |     ;                      
#       |  22    |  sub g b       | g -= b                 |     ;                   |     ;                      
#       |  23    |  jnz g -13     | IF g != 0 GOTO E       |   WHILE d != b          |   ;                        
#       |  24    |  jnz f 2       | IF f != 0 GOTO F       |   IF f == 0             |   IF NOT no_factors:       
#       |  25    |  sub h -1      | h++                    |     h++                 |     n_factors++            
# F:    |  26    |  set g b       | g = b                  |   ;                     |   ;                        
#       |  27    |  sub g c       | g -= c                 |   ;                     |   ;                        
#       |  28    |  jnz g 2       | IF g != 0 GOTO G       |   IF b == c:            |   ;                        
#       |  29    |  jnz 1 3       | HALT                   |     HALT                |   ;                        
# G:    |  30    |  sub b -17     | b += 17                |   b += 17               |   b += 17                  
#       |  31    |  jnz 1 -23     | GOTO B                 |                         | WHILE b != c               

# COMMAND ----------

# When a = 0, the main loop runs only once
# The outer range loop runs b-2 times (82 times)
# The inner range loop runs b-2 times (82 times) for each outer loop
# mul is executed once per inner range loop run
answer = 82 * 82
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, it's time to fix the problem.</p>
# MAGIC <p>The <em>debug mode switch</em> is wired directly to register <code>a</code>.  You <span title="From 'magic' to 'more magic'.">flip the switch</span>, which makes <em>register <code>a</code> now start at <code>1</code></em> when the program is executed.</p>
# MAGIC <p>Immediately, the coprocessor begins to overheat.  Whoever wrote this program obviously didn't choose a very efficient implementation.  You'll need to <em>optimize the program</em> if it has any hope of completing before Santa needs that printer working.</p>
# MAGIC <p>The coprocessor's ultimate goal is to determine the final value left in register <code>h</code> once the program completes. Technically, if it had that... it wouldn't even need to run the program.</p>
# MAGIC <p>After setting register <code>a</code> to <code>1</code>, if the program were to run to completion, <em>what value would be left in register <code>h</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

import math

def is_prime(x):
  return all(x % y != 0 for y in range(2, int(math.sqrt(x))))

answer = sum(not is_prime(b) for b in range(108400, 125400 + 1, 17))
print(answer)
