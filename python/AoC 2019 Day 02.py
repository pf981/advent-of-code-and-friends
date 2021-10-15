# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/2

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 2: 1202 Program Alarm ---</h2><p>On the way to your <a href="https://en.wikipedia.org/wiki/Gravity_assist">gravity assist</a> around the Moon, your ship computer beeps angrily about a "<a href="https://www.hq.nasa.gov/alsj/a11/a11.landing.html#1023832">1202 program alarm</a>". On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" The ship computer <a href="https://en.wikipedia.org/wiki/Halt_and_Catch_Fire">bursts into flames</a>.</p>
# MAGIC <p>You notify the Elves that the computer's <a href="https://en.wikipedia.org/wiki/Magic_smoke">magic smoke</a> seems to have <span title="Looks like SOMEONE forgot to change the switch to 'more magic'.">escaped</span>. "That computer ran <em>Intcode</em> programs like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"</p>
# MAGIC <p>An Intcode program is a list of <a href="https://en.wikipedia.org/wiki/Integer">integers</a> separated by commas (like <code>1,0,0,3,99</code>).  To run one, start by looking at the first integer (called position <code>0</code>). Here, you will find an <em>opcode</em> - either <code>1</code>, <code>2</code>, or <code>99</code>. The opcode indicates what to do; for example, <code>99</code> means that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.</p>
# MAGIC <p>Opcode <code>1</code> <em>adds</em> together numbers read from two positions and stores the result in a third position. The three integers <em>immediately after</em> the opcode tell you these three positions - the first two indicate the <em>positions</em> from which you should read the input values, and the third indicates the <em>position</em> at which the output should be stored.</p>
# MAGIC <p>For example, if your Intcode computer encounters <code>1,10,20,30</code>, it should read the values at positions <code>10</code> and <code>20</code>, add those values, and then overwrite the value at position <code>30</code> with their sum.</p>
# MAGIC <p>Opcode <code>2</code> works exactly like opcode <code>1</code>, except it <em>multiplies</em> the two inputs instead of adding them. Again, the three integers after the opcode indicate <em>where</em> the inputs and outputs are, not their values.</p>
# MAGIC <p>Once you're done processing an opcode, <em>move to the next one</em> by stepping forward <code>4</code> positions.</p>
# MAGIC <p>For example, suppose you have the following program:</p>
# MAGIC <pre><code>1,9,10,3,2,3,11,0,99,30,40,50</code></pre>
# MAGIC <p>For the purposes of illustration, here is the same program split into multiple lines:</p>
# MAGIC <pre><code>1,9,10,3,
# MAGIC 2,3,11,0,
# MAGIC 99,
# MAGIC 30,40,50
# MAGIC </code></pre>
# MAGIC <p>The first four integers, <code>1,9,10,3</code>, are at positions <code>0</code>, <code>1</code>, <code>2</code>, and <code>3</code>. Together, they represent the first opcode (<code>1</code>, addition), the positions of the two inputs (<code>9</code> and <code>10</code>), and the position of the output (<code>3</code>).  To handle this opcode, you first need to get the values at the input positions: position <code>9</code> contains <code>30</code>, and position <code>10</code> contains <code>40</code>.  <em>Add</em> these numbers together to get <code>70</code>.  Then, store this value at the output position; here, the output position (<code>3</code>) is <em>at</em> position <code>3</code>, so it overwrites itself.  Afterward, the program looks like this:</p>
# MAGIC <pre><code>1,9,10,<em>70</em>,
# MAGIC 2,3,11,0,
# MAGIC 99,
# MAGIC 30,40,50
# MAGIC </code></pre>
# MAGIC <p>Step forward <code>4</code> positions to reach the next opcode, <code>2</code>. This opcode works just like the previous, but it multiplies instead of adding.  The inputs are at positions <code>3</code> and <code>11</code>; these positions contain <code>70</code> and <code>50</code> respectively. Multiplying these produces <code>3500</code>; this is stored at position <code>0</code>:</p>
# MAGIC <pre><code><em>3500</em>,9,10,70,
# MAGIC 2,3,11,0,
# MAGIC 99,
# MAGIC 30,40,50
# MAGIC </code></pre>
# MAGIC <p>Stepping forward <code>4</code> more positions arrives at opcode <code>99</code>, halting the program.</p>
# MAGIC <p>Here are the initial and final states of a few more small programs:</p>
# MAGIC <ul>
# MAGIC <li><code>1,0,0,0,99</code> becomes <code><em>2</em>,0,0,0,99</code> (<code>1 + 1 = 2</code>).</li>
# MAGIC <li><code>2,3,0,3,99</code> becomes <code>2,3,0,<em>6</em>,99</code> (<code>3 * 2 = 6</code>).</li>
# MAGIC <li><code>2,4,4,5,99,0</code> becomes <code>2,4,4,5,99,<em>9801</em></code> (<code>99 * 99 = 9801</code>).</li>
# MAGIC <li><code>1,1,1,4,99,5,6,0,99</code> becomes <code><em>30</em>,1,1,4,<em>2</em>,5,6,0,99</code>.</li>
# MAGIC </ul>
# MAGIC <p>Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, <em>before running the program</em>, replace position <code>1</code> with the value <code>12</code> and replace position <code>2</code> with the value <code>2</code>. <em>What value is left at position <code>0</code></em> after the program halts?</p>
# MAGIC </article>

# COMMAND ----------

inp = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0'

# COMMAND ----------

import itertools
import operator

def run_instructions(nums, a, b):
  nums = nums.copy()
  nums[1] = a
  nums[2] = b
  for i in itertools.count(step=4):
    if nums[i] == 99:
      return nums[0]
    fn = operator.add if (nums[i] == 1) else operator.mul
    nums[nums[i + 3]] = fn(nums[nums[i + 1]], nums[nums[i + 2]])

nums = [int(x) for x in inp.split(',')]

answer = run_instructions(nums, 12, 2)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>"Good, the new computer seems to be working correctly!  <em>Keep it nearby</em> during this mission - you'll probably use it again. Real Intcode computers support many more features than your new one, but we'll let you know what they are as you need them."</p>
# MAGIC <p>"However, your current priority should be to complete your gravity assist around the Moon. For this mission to succeed, we should settle on some terminology for the parts you've already built."</p>
# MAGIC <p>Intcode programs are given as a list of integers; these values are used as the initial state for the computer's <em>memory</em>. When you run an Intcode program, make sure to start by initializing memory to the program's values. A position in memory is called an <em>address</em> (for example, the first value in memory is at "address 0").</p>
# MAGIC <p>Opcodes (like <code>1</code>, <code>2</code>, or <code>99</code>) mark the beginning of an <em>instruction</em>.  The values used immediately after an opcode, if any, are called the instruction's <em>parameters</em>.  For example, in the instruction <code>1,2,3,4</code>, <code>1</code> is the opcode; <code>2</code>, <code>3</code>, and <code>4</code> are the parameters. The instruction <code>99</code> contains only an opcode and has no parameters.</p>
# MAGIC <p>The address of the current instruction is called the <em>instruction pointer</em>; it starts at <code>0</code>.  After an instruction finishes, the instruction pointer increases by <em>the number of values in the instruction</em>; until you add more instructions to the computer, this is always <code>4</code> (<code>1</code> opcode + <code>3</code> parameters) for the add and multiply instructions. (The halt instruction would increase the instruction pointer by <code>1</code>, but it halts the program instead.)</p>
# MAGIC <p>"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to <em>determine what pair of inputs produces the output <code>19690720</code></em>."</p>
# MAGIC <p>The inputs should still be provided to the program by replacing the values at addresses <code>1</code> and <code>2</code>, just like before.  In this program, the value placed in address <code>1</code> is called the <em>noun</em>, and the value placed in address <code>2</code> is called the <em>verb</em>.   Each of the two input values will be between <code>0</code> and <code>99</code>, inclusive.</p>
# MAGIC <p>Once the program has halted, its output is available at address <code>0</code>, also just like before. Each time you try a pair of inputs, make sure you first <em>reset the computer's memory to the values in the program</em> (your puzzle input) - in other words, don't reuse memory from a previous attempt.</p>
# MAGIC <p>Find the input <em>noun</em> and <em>verb</em> that cause the program to produce the output <code>19690720</code>. <em>What is <code>100 * noun + verb</code>?</em> (For example, if <code>noun=12</code> and <code>verb=2</code>, the answer would be <code>1202</code>.)</p>
# MAGIC </article>

# COMMAND ----------

def solve(nums):
  for a in range(100):
    for b in range(100):
      if run_instructions(nums, a, b) == 19690720:
        return 100 * a + b

answer = solve(nums)
print(answer)
