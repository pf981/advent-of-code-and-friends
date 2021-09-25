# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/16

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: Chronal Classification ---</h2><p>As you see the Elves defend their hot chocolate successfully, you go back to falling through time. This is going to become a problem.</p>
# MAGIC <p>If you're ever going to return to your own time, you need to understand how this device on your wrist works. You have a little while before you reach your next destination, and with a bit of trial and error, you manage to pull up a programming manual on the device's tiny screen.</p>
# MAGIC <p>According to the manual, the device has four <a href="https://en.wikipedia.org/wiki/Hardware_register">registers</a> (numbered <code>0</code> through <code>3</code>) that can be manipulated by <a href="https://en.wikipedia.org/wiki/Instruction_set_architecture#Instructions">instructions</a> containing one of 16 opcodes. The registers start with the value <code>0</code>.</p>
# MAGIC <p>Every instruction consists of four values: an <em>opcode</em>, two <em>inputs</em> (named <code>A</code> and <code>B</code>), and an <em>output</em> (named <code>C</code>), in that order. The opcode specifies the behavior of the instruction and how the inputs are interpreted. The output, <code>C</code>, is always treated as a register.</p>
# MAGIC <p>In the opcode descriptions below, if something says "<em>value <code>A</code></em>", it means to take the number given as <code>A</code> <em>literally</em>. (This is also called an "immediate" value.) If something says "<em>register <code>A</code></em>", it means to use the number given as <code>A</code> to read from (or write to) the <em>register with that number</em>. So, if the opcode <code>addi</code> adds register <code>A</code> and value <code>B</code>, storing the result in register <code>C</code>, and the instruction <code>addi 0 7 3</code> is encountered, it would add <code>7</code> to the value contained by register <code>0</code> and store the sum in register <code>3</code>, never modifying registers <code>0</code>, <code>1</code>, or <code>2</code> in the process.</p>
# MAGIC <p>Many opcodes are similar except for how they interpret their arguments. The opcodes fall into seven general categories:</p>
# MAGIC <p>Addition:</p>
# MAGIC <ul>
# MAGIC <li><code>addr</code> (add register) stores into register <code>C</code> the result of adding register <code>A</code> and register <code>B</code>.</li>
# MAGIC <li><code>addi</code> (add immediate) stores into register <code>C</code> the result of adding register <code>A</code> and value <code>B</code>.</li>
# MAGIC </ul>
# MAGIC <p>Multiplication:</p>
# MAGIC <ul>
# MAGIC <li><code>mulr</code> (multiply register) stores into register <code>C</code> the result of multiplying register <code>A</code> and register <code>B</code>.</li>
# MAGIC <li><code>muli</code> (multiply immediate) stores into register <code>C</code> the result of multiplying register <code>A</code> and value <code>B</code>.</li>
# MAGIC </ul>
# MAGIC <p><a href="https://en.wikipedia.org/wiki/Bitwise_AND">Bitwise AND</a>:</p>
# MAGIC <ul>
# MAGIC <li><code>banr</code> (bitwise AND register) stores into register <code>C</code> the result of the bitwise AND of register <code>A</code> and register <code>B</code>.</li>
# MAGIC <li><code>bani</code> (bitwise AND immediate) stores into register <code>C</code> the result of the bitwise AND of register <code>A</code> and value <code>B</code>.</li>
# MAGIC </ul>
# MAGIC <p><a href="https://en.wikipedia.org/wiki/Bitwise_OR">Bitwise OR</a>:</p>
# MAGIC <ul>
# MAGIC <li><code>borr</code> (bitwise OR register) stores into register <code>C</code> the result of the bitwise OR of register <code>A</code> and register <code>B</code>.</li>
# MAGIC <li><code>bori</code> (bitwise OR immediate) stores into register <code>C</code> the result of the bitwise OR of register <code>A</code> and value <code>B</code>.</li>
# MAGIC </ul>
# MAGIC <p>Assignment:</p>
# MAGIC <ul>
# MAGIC <li><code>setr</code> (set register) copies the contents of register <code>A</code> into register <code>C</code>. (Input <code>B</code> is ignored.)</li>
# MAGIC <li><code>seti</code> (set immediate) stores value <code>A</code> into register <code>C</code>. (Input <code>B</code> is ignored.)</li>
# MAGIC </ul>
# MAGIC <p>Greater-than testing:</p>
# MAGIC <ul>
# MAGIC <li><code>gtir</code> (greater-than immediate/register) sets register <code>C</code> to <code>1</code> if value <code>A</code> is greater than register <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC <li><code>gtri</code> (greater-than register/immediate) sets register <code>C</code> to <code>1</code> if register <code>A</code> is greater than value <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC <li><code>gtrr</code> (greater-than register/register) sets register <code>C</code> to <code>1</code> if register <code>A</code> is greater than register <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC </ul>
# MAGIC <p>Equality testing:</p>
# MAGIC <ul>
# MAGIC <li><code>eqir</code> (equal immediate/register) sets register <code>C</code> to <code>1</code> if value <code>A</code> is equal to register <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC <li><code>eqri</code> (equal register/immediate) sets register <code>C</code> to <code>1</code> if register <code>A</code> is equal to value <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC <li><code>eqrr</code> (equal register/register) sets register <code>C</code> to <code>1</code> if register <code>A</code> is equal to register <code>B</code>. Otherwise, register <code>C</code> is set to <code>0</code>.</li>
# MAGIC </ul>
# MAGIC <p>Unfortunately, while the manual gives the <em>name</em> of each opcode, it doesn't seem to indicate the <em>number</em>. However, you can monitor the CPU to see the contents of the registers before and after instructions are executed to try to work them out.  Each opcode has a number from <code>0</code> through <code>15</code>, but the manual doesn't say which is which. For example, suppose you capture the following sample:</p>
# MAGIC <pre><code>Before: [3, 2, 1, 1]
# MAGIC 9 2 1 2
# MAGIC After:  [3, 2, 2, 1]
# MAGIC </code></pre>
# MAGIC <p>This sample shows the effect of the instruction <code>9 2 1 2</code> on the registers. Before the instruction is executed, register <code>0</code> has value <code>3</code>, register <code>1</code> has value <code>2</code>, and registers <code>2</code> and <code>3</code> have value <code>1</code>. After the instruction is executed, register <code>2</code>'s value becomes <code>2</code>.</p>
# MAGIC <p>The instruction itself, <code>9 2 1 2</code>, means that opcode <code>9</code> was executed with <code>A=2</code>, <code>B=1</code>, and <code>C=2</code>. Opcode <code>9</code> could be any of the 16 opcodes listed above, but only three of them behave in a way that would cause the result shown in the sample:</p>
# MAGIC <ul>
# MAGIC <li>Opcode <code>9</code> could be <code>mulr</code>: register <code>2</code> (which has a value of <code>1</code>) times register <code>1</code> (which has a value of <code>2</code>) produces <code>2</code>, which matches the value stored in the output register, register <code>2</code>.</li>
# MAGIC <li>Opcode <code>9</code> could be <code>addi</code>: register <code>2</code> (which has a value of <code>1</code>) plus value <code>1</code> produces <code>2</code>, which matches the value stored in the output register, register <code>2</code>.</li>
# MAGIC <li>Opcode <code>9</code> could be <code>seti</code>: value <code>2</code> matches the value stored in the output register, register <code>2</code>; the number given for <code>B</code> is irrelevant.</li>
# MAGIC </ul>
# MAGIC <p>None of the other opcodes produce the result captured in the sample. Because of this, the sample above <em>behaves like three opcodes</em>.</p>
# MAGIC <p>You collect many of these samples (the first section of your puzzle input). The manual also includes a small test program (the second section of your puzzle input) - you can <em>ignore it for now</em>.</p>
# MAGIC <p>Ignoring the opcode numbers, <em>how many samples in your puzzle input behave like three or more opcodes?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Before: [3, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [3, 3, 1, 1]
7 3 3 3
After:  [3, 3, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 2
After:  [1, 3, 0, 0]

Before: [3, 0, 0, 2]
12 2 3 2
After:  [3, 0, 1, 2]

Before: [0, 3, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [1, 1, 0, 2]
2 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 2, 1]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [2, 1, 3, 0]
14 0 3 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 1, 3, 0]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 1, 0, 0]
14 0 3 0
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 1]
4 3 1 2
After:  [2, 1, 0, 1]

Before: [1, 0, 1, 1]
7 3 3 1
After:  [1, 0, 1, 1]

Before: [0, 1, 0, 1]
7 3 3 2
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 2]
0 1 2 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 2]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 2]
10 1 0 0
After:  [0, 0, 2, 2]

Before: [2, 1, 3, 1]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [1, 1, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 0, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 0, 0, 1]
4 0 1 1
After:  [2, 1, 0, 1]

Before: [2, 0, 3, 3]
10 1 0 3
After:  [2, 0, 3, 0]

Before: [0, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [2, 1, 3, 3]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [0, 1, 2, 1]
11 3 2 3
After:  [0, 1, 2, 1]

Before: [0, 2, 2, 3]
13 0 2 1
After:  [0, 0, 2, 3]

Before: [0, 2, 3, 2]
13 0 1 3
After:  [0, 2, 3, 0]

Before: [1, 1, 2, 2]
4 3 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 1]
11 3 2 2
After:  [1, 1, 1, 1]

Before: [0, 2, 1, 0]
13 0 1 1
After:  [0, 0, 1, 0]

Before: [2, 1, 2, 2]
9 2 0 0
After:  [1, 1, 2, 2]

Before: [1, 1, 1, 1]
1 2 0 3
After:  [1, 1, 1, 2]

Before: [3, 3, 0, 2]
12 2 3 2
After:  [3, 3, 1, 2]

Before: [0, 1, 2, 2]
3 3 2 1
After:  [0, 4, 2, 2]

Before: [0, 2, 2, 3]
13 0 3 0
After:  [0, 2, 2, 3]

Before: [1, 3, 1, 0]
1 2 0 0
After:  [2, 3, 1, 0]

Before: [0, 1, 1, 3]
15 1 3 3
After:  [0, 1, 1, 0]

Before: [3, 2, 3, 0]
12 3 2 3
After:  [3, 2, 3, 1]

Before: [1, 0, 1, 3]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [3, 1, 2, 1]
11 3 2 2
After:  [3, 1, 1, 1]

Before: [0, 0, 0, 2]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 0, 0, 1]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [0, 3, 0, 2]
6 0 0 0
After:  [0, 3, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 1, 0, 3]
15 1 3 0
After:  [0, 1, 0, 3]

Before: [3, 2, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [0, 2, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [0, 3, 3, 1]
6 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 2, 0]
3 2 2 3
After:  [0, 1, 2, 4]

Before: [3, 0, 0, 0]
4 0 2 1
After:  [3, 1, 0, 0]

Before: [0, 2, 2, 1]
11 3 2 3
After:  [0, 2, 2, 1]

Before: [2, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 2]
5 1 2 2
After:  [2, 1, 0, 2]

Before: [1, 1, 2, 2]
5 1 2 2
After:  [1, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 3
After:  [0, 1, 0, 0]

Before: [1, 3, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 2]
3 2 2 2
After:  [3, 0, 4, 2]

Before: [2, 1, 2, 1]
3 2 2 0
After:  [4, 1, 2, 1]

Before: [1, 3, 2, 3]
8 0 2 2
After:  [1, 3, 0, 3]

Before: [2, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [2, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [3, 0, 0, 3]
10 1 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 3, 1]
0 1 2 1
After:  [1, 0, 3, 1]

Before: [0, 0, 1, 2]
6 0 0 2
After:  [0, 0, 0, 2]

Before: [3, 3, 0, 2]
10 2 0 2
After:  [3, 3, 0, 2]

Before: [2, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 0
After:  [0, 0, 0, 1]

Before: [0, 2, 2, 0]
6 0 0 3
After:  [0, 2, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 0
After:  [0, 1, 2, 0]

Before: [2, 3, 2, 0]
9 2 0 2
After:  [2, 3, 1, 0]

Before: [1, 3, 0, 2]
2 0 2 0
After:  [0, 3, 0, 2]

Before: [3, 0, 0, 0]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 1, 0, 1]
6 0 0 0
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 0]
12 3 2 2
After:  [0, 1, 1, 0]

Before: [2, 3, 1, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 1, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [0, 3, 0, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [0, 3, 2, 1]
11 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 2, 2, 1]
3 1 2 3
After:  [2, 2, 2, 4]

Before: [2, 1, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 3, 3]
9 3 2 2
After:  [0, 3, 1, 3]

Before: [0, 3, 3, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [0, 1, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 1]
3 2 2 2
After:  [2, 0, 4, 1]

Before: [0, 2, 2, 1]
9 2 1 1
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 1]
7 3 3 3
After:  [2, 1, 0, 0]

Before: [0, 0, 1, 3]
13 0 3 0
After:  [0, 0, 1, 3]

Before: [3, 3, 1, 3]
15 2 3 3
After:  [3, 3, 1, 0]

Before: [0, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 1
After:  [2, 0, 3, 3]

Before: [2, 0, 3, 3]
4 2 0 1
After:  [2, 1, 3, 3]

Before: [0, 0, 2, 3]
13 0 3 1
After:  [0, 0, 2, 3]

Before: [1, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [0, 0, 0, 1]
6 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 0, 3, 2]
13 0 2 3
After:  [0, 0, 3, 0]

Before: [1, 3, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 0, 1]
13 0 1 2
After:  [0, 1, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [2, 0, 2, 1]
7 3 3 1
After:  [2, 0, 2, 1]

Before: [3, 3, 2, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 3, 1, 2]
6 0 0 3
After:  [0, 3, 1, 0]

Before: [1, 0, 1, 1]
1 2 0 2
After:  [1, 0, 2, 1]

Before: [2, 1, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 3, 3, 3]
9 3 0 3
After:  [3, 3, 3, 1]

Before: [1, 1, 1, 1]
1 2 3 0
After:  [2, 1, 1, 1]

Before: [3, 1, 3, 1]
0 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 1, 2, 0]
5 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
5 1 2 2
After:  [1, 1, 0, 3]

Before: [2, 0, 0, 3]
10 1 0 1
After:  [2, 0, 0, 3]

Before: [1, 2, 0, 1]
7 3 3 3
After:  [1, 2, 0, 0]

Before: [0, 3, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 2, 3, 1]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [3, 0, 2, 1]
11 3 2 2
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 3, 1, 1]
1 2 3 2
After:  [2, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 3, 3, 0]
12 3 2 0
After:  [1, 3, 3, 0]

Before: [2, 3, 0, 2]
12 2 3 2
After:  [2, 3, 1, 2]

Before: [3, 1, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [0, 2, 0, 0]
13 0 1 0
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 2]
13 0 1 2
After:  [0, 2, 0, 2]

Before: [3, 2, 2, 3]
15 2 3 2
After:  [3, 2, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 2, 0, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 0
After:  [0, 3, 2, 0]

Before: [3, 2, 3, 1]
9 2 3 1
After:  [3, 0, 3, 1]

Before: [0, 1, 1, 0]
4 2 1 1
After:  [0, 0, 1, 0]

Before: [0, 3, 2, 3]
13 0 3 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
7 3 3 3
After:  [3, 1, 0, 0]

Before: [1, 3, 3, 3]
9 3 2 3
After:  [1, 3, 3, 1]

Before: [2, 3, 3, 1]
4 2 0 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 1]
7 3 3 0
After:  [0, 3, 3, 1]

Before: [1, 2, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 2, 2, 2]
13 0 2 2
After:  [0, 2, 0, 2]

Before: [1, 1, 3, 3]
0 1 2 1
After:  [1, 0, 3, 3]

Before: [2, 0, 3, 2]
4 0 1 0
After:  [1, 0, 3, 2]

Before: [3, 1, 3, 0]
12 3 2 2
After:  [3, 1, 1, 0]

Before: [0, 2, 1, 1]
1 2 3 3
After:  [0, 2, 1, 2]

Before: [2, 3, 1, 0]
14 0 3 3
After:  [2, 3, 1, 1]

Before: [2, 0, 1, 0]
14 0 3 0
After:  [1, 0, 1, 0]

Before: [0, 3, 1, 1]
7 3 3 3
After:  [0, 3, 1, 0]

Before: [2, 3, 3, 3]
9 3 2 3
After:  [2, 3, 3, 1]

Before: [2, 1, 2, 3]
15 2 3 1
After:  [2, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 1]
7 3 3 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 1]
7 3 3 1
After:  [1, 0, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 2
After:  [2, 1, 0, 1]

Before: [3, 1, 3, 2]
0 1 2 1
After:  [3, 0, 3, 2]

Before: [2, 1, 1, 3]
15 1 3 3
After:  [2, 1, 1, 0]

Before: [3, 2, 0, 1]
10 2 0 3
After:  [3, 2, 0, 0]

Before: [1, 3, 0, 1]
2 0 2 2
After:  [1, 3, 0, 1]

Before: [1, 1, 3, 2]
0 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 2]
7 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 3]
9 3 0 3
After:  [3, 1, 0, 1]

Before: [1, 1, 0, 1]
2 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 3, 3, 0]
14 0 3 0
After:  [1, 3, 3, 0]

Before: [3, 0, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 3, 3, 0]
14 0 3 3
After:  [2, 3, 3, 1]

Before: [0, 1, 2, 2]
5 1 2 2
After:  [0, 1, 0, 2]

Before: [3, 0, 2, 3]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [1, 1, 2, 3]
8 0 2 2
After:  [1, 1, 0, 3]

Before: [0, 0, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 1]
11 3 2 2
After:  [1, 3, 1, 1]

Before: [0, 3, 1, 3]
13 0 3 1
After:  [0, 0, 1, 3]

Before: [2, 0, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [0, 2, 0, 3]
13 0 3 3
After:  [0, 2, 0, 0]

Before: [1, 0, 2, 0]
8 0 2 2
After:  [1, 0, 0, 0]

Before: [1, 3, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 0, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 0, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 3, 0, 2]
7 3 3 1
After:  [3, 0, 0, 2]

Before: [2, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 3, 3, 2]
13 0 1 1
After:  [0, 0, 3, 2]

Before: [0, 3, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
8 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 0, 0, 3]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 3, 2, 1]
9 2 0 2
After:  [2, 3, 1, 1]

Before: [1, 3, 1, 2]
1 2 0 0
After:  [2, 3, 1, 2]

Before: [2, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 2, 2, 1]
9 2 1 2
After:  [3, 2, 1, 1]

Before: [2, 1, 3, 1]
0 1 2 2
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [1, 1, 0, 3]
15 1 3 1
After:  [1, 0, 0, 3]

Before: [0, 3, 3, 3]
9 3 2 3
After:  [0, 3, 3, 1]

Before: [3, 1, 3, 1]
7 3 3 3
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 1]
11 3 2 3
After:  [2, 2, 2, 1]

Before: [3, 2, 2, 3]
9 3 0 1
After:  [3, 1, 2, 3]

Before: [3, 2, 2, 0]
3 1 2 1
After:  [3, 4, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [0, 1, 3, 0]
0 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 2, 3, 0]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [2, 0, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [1, 1, 0, 0]
2 0 2 0
After:  [0, 1, 0, 0]

Before: [0, 2, 3, 2]
6 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 3, 2, 3]
3 2 2 0
After:  [4, 3, 2, 3]

Before: [1, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 0
After:  [1, 2, 2, 0]

Before: [1, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [1, 1, 0, 0]
2 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [3, 3, 1, 3]
15 2 3 2
After:  [3, 3, 0, 3]

Before: [0, 1, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [1, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 2]
3 3 2 2
After:  [2, 1, 4, 2]

Before: [1, 1, 3, 2]
0 1 2 1
After:  [1, 0, 3, 2]

Before: [3, 1, 2, 3]
5 1 2 1
After:  [3, 0, 2, 3]

Before: [0, 1, 3, 1]
0 1 2 1
After:  [0, 0, 3, 1]

Before: [3, 2, 2, 1]
7 3 3 1
After:  [3, 0, 2, 1]

Before: [0, 1, 2, 3]
5 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 1, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 0
After:  [1, 0, 2, 0]

Before: [0, 2, 1, 0]
6 0 0 2
After:  [0, 2, 0, 0]

Before: [0, 2, 0, 1]
13 0 1 0
After:  [0, 2, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 0
After:  [1, 3, 0, 0]

Before: [3, 1, 1, 3]
15 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 2, 1, 3]
15 2 3 3
After:  [1, 2, 1, 0]

Before: [3, 1, 2, 1]
5 1 2 1
After:  [3, 0, 2, 1]

Before: [1, 1, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 3]
8 0 2 0
After:  [0, 2, 2, 3]

Before: [0, 2, 2, 3]
15 2 3 2
After:  [0, 2, 0, 3]

Before: [1, 0, 2, 0]
8 0 2 0
After:  [0, 0, 2, 0]

Before: [0, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [3, 3, 2, 1]
11 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 2, 2, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 1, 2, 1]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 1, 2, 1]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [1, 3, 2, 1]
11 3 2 3
After:  [1, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 1 2
After:  [0, 1, 0, 2]

Before: [1, 2, 2, 0]
3 1 2 1
After:  [1, 4, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 0
After:  [0, 0, 0, 0]

Before: [1, 2, 1, 1]
1 2 0 3
After:  [1, 2, 1, 2]

Before: [3, 3, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 1, 3]
4 2 1 3
After:  [1, 1, 1, 0]

Before: [2, 0, 2, 2]
7 3 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 2, 0, 3]
10 2 0 0
After:  [0, 2, 0, 3]

Before: [1, 1, 2, 0]
5 1 2 1
After:  [1, 0, 2, 0]

Before: [2, 0, 3, 1]
9 2 3 2
After:  [2, 0, 0, 1]

Before: [1, 0, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 2, 0, 3]
15 1 3 3
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 0]
6 0 0 0
After:  [0, 2, 2, 0]

Before: [0, 0, 1, 1]
1 2 3 2
After:  [0, 0, 2, 1]

Before: [1, 0, 1, 3]
15 2 3 3
After:  [1, 0, 1, 0]

Before: [2, 1, 2, 3]
15 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 2, 2, 3]
8 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 2, 3, 0]
12 3 2 2
After:  [2, 2, 1, 0]

Before: [3, 1, 3, 1]
9 2 3 3
After:  [3, 1, 3, 0]

Before: [3, 0, 3, 1]
7 3 3 1
After:  [3, 0, 3, 1]

Before: [0, 3, 0, 2]
6 0 0 3
After:  [0, 3, 0, 0]

Before: [1, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 3, 3, 0]
12 3 2 3
After:  [1, 3, 3, 1]

Before: [3, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [2, 1, 2, 0]
14 0 3 3
After:  [2, 1, 2, 1]

Before: [2, 3, 2, 1]
11 3 2 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 0]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [0, 1, 3, 0]
12 3 2 3
After:  [0, 1, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 3
After:  [1, 2, 3, 1]

Before: [2, 1, 0, 2]
12 2 3 3
After:  [2, 1, 0, 1]

Before: [0, 3, 0, 2]
7 3 3 3
After:  [0, 3, 0, 0]

Before: [3, 0, 3, 0]
12 3 2 2
After:  [3, 0, 1, 0]

Before: [2, 2, 0, 0]
14 0 3 3
After:  [2, 2, 0, 1]

Before: [1, 2, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [0, 2, 3, 1]
9 2 3 2
After:  [0, 2, 0, 1]

Before: [2, 1, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 1, 3, 3]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 2, 3]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 3, 1, 0]
1 2 0 2
After:  [1, 3, 2, 0]

Before: [0, 3, 3, 2]
13 0 1 3
After:  [0, 3, 3, 0]

Before: [1, 2, 0, 2]
2 0 2 0
After:  [0, 2, 0, 2]

Before: [2, 2, 0, 0]
14 0 3 0
After:  [1, 2, 0, 0]

Before: [3, 2, 0, 0]
10 2 0 0
After:  [0, 2, 0, 0]

Before: [1, 2, 2, 0]
8 0 2 0
After:  [0, 2, 2, 0]

Before: [2, 0, 2, 2]
3 3 2 1
After:  [2, 4, 2, 2]

Before: [1, 3, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 1, 1, 2]
7 3 3 3
After:  [0, 1, 1, 0]

Before: [0, 0, 1, 2]
7 3 3 1
After:  [0, 0, 1, 2]

Before: [0, 1, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 3, 3]
15 1 3 1
After:  [2, 0, 3, 3]

Before: [0, 3, 2, 3]
13 0 2 3
After:  [0, 3, 2, 0]

Before: [0, 1, 2, 2]
13 0 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 0, 1, 2]
13 0 3 2
After:  [0, 0, 0, 2]

Before: [1, 3, 1, 2]
1 2 0 3
After:  [1, 3, 1, 2]

Before: [0, 1, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [2, 1, 3, 1]
4 2 0 0
After:  [1, 1, 3, 1]

Before: [1, 1, 2, 2]
8 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 0, 0, 2]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 3, 1, 2]
7 3 3 2
After:  [0, 3, 0, 2]

Before: [3, 2, 2, 2]
9 2 1 2
After:  [3, 2, 1, 2]

Before: [0, 3, 2, 2]
4 3 2 1
After:  [0, 0, 2, 2]

Before: [0, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 0, 3]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 3, 2, 3]
13 0 2 0
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 0]
8 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 0]
2 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 0, 2, 1]
11 3 2 2
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 1, 1, 1]
4 3 1 1
After:  [1, 0, 1, 1]

Before: [0, 3, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [1, 1, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 0, 0, 0]
14 0 3 0
After:  [1, 0, 0, 0]

Before: [0, 1, 3, 2]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 0, 2, 3]
15 2 3 2
After:  [3, 0, 0, 3]

Before: [1, 1, 1, 2]
1 2 0 0
After:  [2, 1, 1, 2]

Before: [3, 3, 2, 2]
3 2 2 2
After:  [3, 3, 4, 2]

Before: [0, 1, 0, 2]
7 3 3 2
After:  [0, 1, 0, 2]

Before: [0, 2, 2, 2]
13 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 0]
10 2 0 3
After:  [3, 1, 0, 0]

Before: [2, 1, 3, 0]
0 1 2 1
After:  [2, 0, 3, 0]

Before: [1, 0, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [2, 0, 1, 2]
10 1 0 1
After:  [2, 0, 1, 2]

Before: [2, 3, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 1, 1, 1]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 2
After:  [2, 0, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 1
After:  [2, 0, 3, 2]

Before: [2, 1, 2, 0]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 3]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 3, 1, 1]
1 2 3 3
After:  [1, 3, 1, 2]

Before: [2, 0, 2, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [3, 2, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 2, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 0, 0, 3]
10 1 0 3
After:  [2, 0, 0, 0]

Before: [2, 1, 0, 3]
15 1 3 1
After:  [2, 0, 0, 3]

Before: [3, 0, 2, 2]
4 3 2 1
After:  [3, 0, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 2
After:  [3, 2, 1, 1]

Before: [2, 0, 0, 2]
12 2 3 2
After:  [2, 0, 1, 2]

Before: [0, 1, 2, 2]
6 0 0 0
After:  [0, 1, 2, 2]

Before: [2, 2, 2, 3]
3 2 2 1
After:  [2, 4, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 3, 2]
6 0 0 0
After:  [0, 3, 3, 2]

Before: [3, 0, 3, 1]
7 3 3 0
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [0, 1, 3, 3]
15 1 3 3
After:  [0, 1, 3, 0]

Before: [2, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [0, 0, 2, 2]
7 3 3 2
After:  [0, 0, 0, 2]

Before: [2, 1, 1, 2]
4 2 1 1
After:  [2, 0, 1, 2]

Before: [1, 2, 0, 3]
2 0 2 0
After:  [0, 2, 0, 3]

Before: [3, 1, 2, 3]
9 3 0 3
After:  [3, 1, 2, 1]

Before: [0, 0, 0, 3]
13 0 3 0
After:  [0, 0, 0, 3]

Before: [1, 2, 2, 1]
8 0 2 2
After:  [1, 2, 0, 1]

Before: [3, 0, 1, 3]
9 3 0 3
After:  [3, 0, 1, 1]

Before: [1, 1, 2, 2]
5 1 2 1
After:  [1, 0, 2, 2]

Before: [1, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 2, 3, 0]
12 3 2 3
After:  [0, 2, 3, 1]

Before: [3, 1, 3, 3]
0 1 2 1
After:  [3, 0, 3, 3]

Before: [3, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [1, 2, 0, 1]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [1, 0, 2, 1]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [2, 0, 2, 0]
10 1 0 1
After:  [2, 0, 2, 0]

Before: [3, 0, 3, 1]
10 1 0 2
After:  [3, 0, 0, 1]

Before: [3, 0, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [0, 1, 3, 1]
13 0 2 1
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 0]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [0, 3, 3, 1]
13 0 3 3
After:  [0, 3, 3, 0]

Before: [1, 3, 0, 3]
2 0 2 0
After:  [0, 3, 0, 3]

Before: [2, 3, 3, 0]
12 3 2 2
After:  [2, 3, 1, 0]

Before: [3, 2, 1, 3]
15 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 3, 2, 1]
8 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 0, 3, 2]
10 1 0 1
After:  [3, 0, 3, 2]

Before: [3, 0, 2, 0]
10 1 0 2
After:  [3, 0, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 2]
5 1 2 1
After:  [3, 0, 2, 2]

Before: [1, 1, 2, 1]
5 1 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 2, 1]
11 3 2 2
After:  [1, 2, 1, 1]

Before: [3, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 1, 2, 1]
11 3 2 2
After:  [2, 1, 1, 1]

Before: [1, 1, 3, 0]
0 1 2 1
After:  [1, 0, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 2
After:  [3, 1, 0, 0]

Before: [0, 1, 2, 1]
5 1 2 2
After:  [0, 1, 0, 1]

Before: [0, 2, 3, 1]
13 0 1 1
After:  [0, 0, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [1, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [2, 3, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 1, 1]
7 3 3 1
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 3, 1]
9 2 3 1
After:  [0, 0, 3, 1]

Before: [3, 3, 0, 2]
12 2 3 3
After:  [3, 3, 0, 1]

Before: [1, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [1, 3, 3, 1]
7 3 3 3
After:  [1, 3, 3, 0]

Before: [2, 1, 2, 2]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 3, 1]
9 2 3 1
After:  [2, 0, 3, 1]

Before: [0, 2, 2, 1]
13 0 1 0
After:  [0, 2, 2, 1]

Before: [0, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 0, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [1, 0, 1, 3]
1 2 0 2
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 0]
3 0 2 3
After:  [2, 1, 2, 4]

Before: [3, 0, 2, 2]
7 3 3 0
After:  [0, 0, 2, 2]

Before: [3, 0, 0, 2]
10 1 0 0
After:  [0, 0, 0, 2]

Before: [2, 1, 3, 2]
7 3 3 3
After:  [2, 1, 3, 0]

Before: [2, 0, 2, 1]
4 0 1 1
After:  [2, 1, 2, 1]

Before: [3, 3, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 0
After:  [0, 0, 2, 3]

Before: [0, 1, 1, 3]
15 1 3 0
After:  [0, 1, 1, 3]

Before: [2, 0, 3, 3]
9 3 2 2
After:  [2, 0, 1, 3]

Before: [2, 3, 0, 0]
14 0 3 3
After:  [2, 3, 0, 1]

Before: [2, 3, 2, 1]
11 3 2 3
After:  [2, 3, 2, 1]

Before: [2, 0, 0, 3]
4 0 1 2
After:  [2, 0, 1, 3]

Before: [0, 1, 1, 2]
6 0 0 0
After:  [0, 1, 1, 2]

Before: [1, 0, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 1, 1, 1]
1 2 3 2
After:  [2, 1, 2, 1]

Before: [1, 3, 2, 2]
3 2 2 3
After:  [1, 3, 2, 4]

Before: [0, 1, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [1, 0, 2, 0]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 3, 2, 3]
3 2 2 2
After:  [0, 3, 4, 3]

Before: [1, 2, 1, 1]
1 2 3 3
After:  [1, 2, 1, 2]

Before: [2, 3, 2, 1]
3 2 2 3
After:  [2, 3, 2, 4]

Before: [3, 1, 1, 1]
1 2 3 2
After:  [3, 1, 2, 1]

Before: [2, 3, 2, 0]
9 2 0 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 3
After:  [2, 0, 2, 1]

Before: [1, 1, 2, 0]
3 2 2 2
After:  [1, 1, 4, 0]

Before: [2, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 0, 0, 2]
2 0 2 0
After:  [0, 0, 0, 2]

Before: [1, 0, 3, 0]
12 3 2 3
After:  [1, 0, 3, 1]

Before: [3, 1, 0, 3]
4 0 2 3
After:  [3, 1, 0, 1]

Before: [3, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [3, 1, 2, 3]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [3, 1, 2, 2]
3 2 2 2
After:  [3, 1, 4, 2]

Before: [3, 0, 1, 1]
7 3 3 0
After:  [0, 0, 1, 1]

Before: [1, 0, 3, 0]
12 3 2 2
After:  [1, 0, 1, 0]

Before: [2, 3, 3, 0]
4 2 0 0
After:  [1, 3, 3, 0]

Before: [2, 2, 1, 0]
14 0 3 3
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [0, 2, 2, 1]
9 2 1 0
After:  [1, 2, 2, 1]

Before: [3, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [0, 1, 2, 3]
6 0 0 0
After:  [0, 1, 2, 3]

Before: [3, 0, 1, 2]
10 1 0 1
After:  [3, 0, 1, 2]

Before: [2, 2, 2, 1]
7 3 3 3
After:  [2, 2, 2, 0]

Before: [3, 0, 1, 3]
10 1 0 0
After:  [0, 0, 1, 3]

Before: [0, 0, 3, 0]
12 3 2 3
After:  [0, 0, 3, 1]

Before: [2, 1, 2, 0]
5 1 2 1
After:  [2, 0, 2, 0]

Before: [2, 2, 2, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [2, 0, 3, 0]
14 0 3 3
After:  [2, 0, 3, 1]

Before: [1, 1, 3, 3]
0 1 2 2
After:  [1, 1, 0, 3]

Before: [0, 1, 1, 2]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [2, 2, 2, 3]
15 1 3 3
After:  [2, 2, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 3
After:  [2, 3, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [2, 1, 1, 3]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 1, 0, 0]
14 0 3 3
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 0]
0 1 2 2
After:  [2, 1, 0, 0]

Before: [1, 2, 0, 2]
12 2 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 0, 3]
13 0 3 3
After:  [0, 3, 0, 0]

Before: [3, 3, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [2, 1, 1, 0]
14 0 3 3
After:  [2, 1, 1, 1]

Before: [1, 2, 2, 0]
8 0 2 2
After:  [1, 2, 0, 0]

Before: [2, 0, 0, 3]
4 0 1 0
After:  [1, 0, 0, 3]

Before: [1, 1, 2, 1]
5 1 2 2
After:  [1, 1, 0, 1]

Before: [3, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [1, 2, 2, 3]
9 2 1 0
After:  [1, 2, 2, 3]

Before: [2, 3, 2, 0]
14 0 3 0
After:  [1, 3, 2, 0]

Before: [3, 2, 3, 1]
7 3 3 3
After:  [3, 2, 3, 0]

Before: [0, 1, 3, 0]
0 1 2 1
After:  [0, 0, 3, 0]

Before: [3, 3, 0, 3]
9 3 0 2
After:  [3, 3, 1, 3]

Before: [3, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 0, 2, 1]
11 3 2 3
After:  [0, 0, 2, 1]

Before: [0, 2, 1, 3]
13 0 1 3
After:  [0, 2, 1, 0]

Before: [1, 2, 2, 2]
3 1 2 3
After:  [1, 2, 2, 4]

Before: [0, 1, 2, 3]
5 1 2 1
After:  [0, 0, 2, 3]

Before: [2, 0, 3, 2]
10 1 0 0
After:  [0, 0, 3, 2]

Before: [1, 1, 0, 2]
12 2 3 0
After:  [1, 1, 0, 2]

Before: [3, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [1, 3, 1, 1]
1 2 0 2
After:  [1, 3, 2, 1]

Before: [2, 1, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
4 0 1 3
After:  [2, 0, 2, 1]

Before: [2, 0, 2, 0]
14 0 3 3
After:  [2, 0, 2, 1]

Before: [0, 1, 3, 1]
0 1 2 2
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 0, 1, 1]
1 2 3 3
After:  [1, 0, 1, 2]

Before: [1, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 2, 2, 2]
9 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 1, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [1, 2, 1, 3]
1 2 0 0
After:  [2, 2, 1, 3]

Before: [1, 0, 0, 0]
2 0 2 2
After:  [1, 0, 0, 0]

Before: [2, 0, 2, 2]
3 2 2 0
After:  [4, 0, 2, 2]

Before: [2, 0, 3, 2]
4 0 1 3
After:  [2, 0, 3, 1]

Before: [2, 1, 2, 1]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 2, 2, 3]
15 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 0, 0, 3]
2 0 2 2
After:  [1, 0, 0, 3]

Before: [1, 3, 2, 2]
8 0 2 0
After:  [0, 3, 2, 2]

Before: [0, 2, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 3]
9 2 0 1
After:  [2, 1, 2, 3]

Before: [2, 1, 2, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [1, 0, 1, 2]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [2, 2, 3, 0]
12 3 2 3
After:  [2, 2, 3, 1]

Before: [3, 3, 3, 3]
9 3 2 1
After:  [3, 1, 3, 3]

Before: [0, 2, 2, 2]
3 1 2 3
After:  [0, 2, 2, 4]

Before: [2, 2, 2, 1]
9 2 1 1
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 1, 2, 0]
14 0 3 0
After:  [1, 1, 2, 0]

Before: [1, 3, 0, 1]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 3, 1, 1]
1 2 3 1
After:  [1, 2, 1, 1]

Before: [1, 3, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 1, 2, 3]
15 2 3 2
After:  [3, 1, 0, 3]

Before: [2, 3, 3, 3]
9 3 2 0
After:  [1, 3, 3, 3]

Before: [0, 1, 3, 1]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 0, 1, 1]
1 2 0 1
After:  [1, 2, 1, 1]

Before: [1, 0, 2, 1]
8 0 2 0
After:  [0, 0, 2, 1]

Before: [1, 2, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 2, 1, 3]
9 3 0 0
After:  [1, 2, 1, 3]

Before: [2, 1, 3, 2]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 2, 2, 0]
3 2 2 0
After:  [4, 2, 2, 0]

Before: [3, 3, 2, 3]
15 2 3 1
After:  [3, 0, 2, 3]

Before: [3, 0, 1, 1]
10 1 0 3
After:  [3, 0, 1, 0]

Before: [0, 1, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [0, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [0, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [2, 3, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
9 3 0 1
After:  [3, 1, 0, 3]

Before: [0, 0, 0, 2]
6 0 0 0
After:  [0, 0, 0, 2]

Before: [1, 3, 2, 0]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 3, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [1, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [0, 1, 1, 2]
13 0 1 3
After:  [0, 1, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 0
After:  [0, 2, 0, 0]

Before: [0, 0, 0, 0]
6 0 0 1
After:  [0, 0, 0, 0]

Before: [0, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [0, 3, 2, 2]
4 3 2 3
After:  [0, 3, 2, 0]

Before: [3, 3, 3, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 2, 0, 1]
13 0 3 1
After:  [0, 0, 0, 1]

Before: [3, 1, 3, 1]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 1, 3, 3]
0 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 0, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [2, 3, 1, 3]
15 2 3 2
After:  [2, 3, 0, 3]

Before: [2, 2, 1, 2]
7 3 3 1
After:  [2, 0, 1, 2]

Before: [0, 1, 0, 2]
7 3 3 3
After:  [0, 1, 0, 0]

Before: [1, 1, 2, 2]
3 3 2 2
After:  [1, 1, 4, 2]

Before: [2, 0, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 1]
2 0 2 2
After:  [1, 2, 0, 1]

Before: [0, 1, 1, 0]
6 0 0 2
After:  [0, 1, 0, 0]

Before: [2, 0, 2, 3]
3 0 2 1
After:  [2, 4, 2, 3]

Before: [0, 1, 2, 0]
5 1 2 1
After:  [0, 0, 2, 0]

Before: [2, 2, 2, 3]
3 0 2 0
After:  [4, 2, 2, 3]

Before: [1, 1, 2, 3]
15 2 3 0
After:  [0, 1, 2, 3]

Before: [0, 1, 2, 1]
3 2 2 2
After:  [0, 1, 4, 1]

Before: [2, 1, 2, 3]
5 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 3, 0, 2]
12 2 3 0
After:  [1, 3, 0, 2]

Before: [3, 1, 3, 1]
0 1 2 1
After:  [3, 0, 3, 1]

Before: [3, 0, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [1, 1, 0, 1]
2 0 2 0
After:  [0, 1, 0, 1]

Before: [3, 3, 1, 1]
1 2 3 3
After:  [3, 3, 1, 2]

Before: [0, 3, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 2]
3 2 2 0
After:  [4, 1, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 3
After:  [3, 2, 2, 1]

Before: [0, 1, 2, 1]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 3, 2, 1]
11 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 1, 3, 3]
0 1 2 3
After:  [1, 1, 3, 0]

Before: [3, 1, 0, 2]
4 0 2 0
After:  [1, 1, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 0, 1, 2]
1 2 0 0
After:  [2, 0, 1, 2]

Before: [3, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 1]
11 3 2 2
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 3, 1, 2]
7 3 3 1
After:  [3, 0, 1, 2]

Before: [3, 1, 2, 2]
5 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 3, 0, 3]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 2]
3 3 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 1]
10 1 0 0
After:  [0, 0, 2, 1]

Before: [0, 0, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [0, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [3, 3, 0, 3]
10 2 0 1
After:  [3, 0, 0, 3]

Before: [2, 2, 3, 1]
9 2 3 2
After:  [2, 2, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 2]
12 2 3 2
After:  [1, 0, 1, 2]

Before: [1, 3, 2, 1]
8 0 2 0
After:  [0, 3, 2, 1]

Before: [3, 2, 2, 3]
3 1 2 2
After:  [3, 2, 4, 3]

Before: [0, 2, 2, 2]
4 3 2 3
After:  [0, 2, 2, 0]

Before: [3, 1, 2, 1]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 2, 0, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [3, 1, 0, 3]
15 1 3 1
After:  [3, 0, 0, 3]

Before: [2, 2, 2, 0]
3 0 2 0
After:  [4, 2, 2, 0]

Before: [0, 0, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [3, 1, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 2, 1]
11 3 2 3
After:  [1, 0, 2, 1]

Before: [2, 1, 0, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [3, 0, 2, 2]
10 1 0 1
After:  [3, 0, 2, 2]

Before: [2, 2, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [0, 2, 2, 3]
15 1 3 2
After:  [0, 2, 0, 3]

Before: [1, 3, 0, 3]
2 0 2 2
After:  [1, 3, 0, 3]

Before: [3, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 1, 0, 2]
7 3 3 1
After:  [1, 0, 0, 2]

Before: [0, 0, 2, 3]
15 2 3 2
After:  [0, 0, 0, 3]

Before: [1, 3, 0, 0]
2 0 2 0
After:  [0, 3, 0, 0]

Before: [3, 2, 2, 2]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [2, 3, 3, 0]
12 3 2 3
After:  [2, 3, 3, 1]

Before: [3, 0, 1, 1]
7 2 3 0
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 2
After:  [0, 2, 1, 1]

Before: [1, 1, 1, 3]
15 1 3 2
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 1]
9 2 3 2
After:  [2, 3, 0, 1]

Before: [0, 2, 0, 3]
6 0 0 0
After:  [0, 2, 0, 3]

Before: [2, 3, 1, 0]
14 0 3 0
After:  [1, 3, 1, 0]

Before: [2, 3, 2, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 3, 1, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 1]
1 2 3 3
After:  [2, 0, 1, 2]

Before: [1, 2, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 1, 2, 1]
5 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 3, 2, 3]
8 0 2 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
4 3 1 0
After:  [0, 1, 0, 1]

Before: [0, 3, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 2]
0 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 2, 1, 0]
14 0 3 0
After:  [1, 2, 1, 0]

Before: [1, 2, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 3
After:  [2, 2, 2, 1]

Before: [3, 1, 1, 1]
1 2 3 3
After:  [3, 1, 1, 2]

Before: [1, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [3, 3, 0, 2]
4 0 2 1
After:  [3, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 3, 2, 3]
9 3 0 0
After:  [1, 3, 2, 3]

Before: [0, 2, 1, 3]
13 0 2 3
After:  [0, 2, 1, 0]

Before: [0, 2, 1, 1]
6 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [2, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 1]
11 3 2 3
After:  [3, 1, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [1, 2, 2, 1]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [0, 0, 2, 2]
6 0 0 0
After:  [0, 0, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [3, 2, 0, 2]
12 2 3 3
After:  [3, 2, 0, 1]

Before: [2, 1, 3, 0]
12 3 2 1
After:  [2, 1, 3, 0]

Before: [3, 1, 1, 0]
4 2 1 1
After:  [3, 0, 1, 0]

Before: [2, 1, 2, 1]
11 3 2 3
After:  [2, 1, 2, 1]

Before: [1, 0, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [2, 2, 1, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [1, 0, 3, 1]
7 3 3 1
After:  [1, 0, 3, 1]

Before: [0, 1, 2, 1]
11 3 2 2
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 0]
1 2 0 1
After:  [1, 2, 1, 0]

Before: [0, 1, 3, 3]
13 0 1 1
After:  [0, 0, 3, 3]

Before: [1, 3, 0, 0]
2 0 2 2
After:  [1, 3, 0, 0]

Before: [0, 1, 1, 1]
13 0 1 0
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 2]
1 2 0 2
After:  [1, 0, 2, 2]

Before: [0, 3, 2, 1]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [2, 0, 0, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [1, 1, 1, 1]
1 2 0 0
After:  [2, 1, 1, 1]

Before: [3, 0, 1, 3]
10 1 0 1
After:  [3, 0, 1, 3]

Before: [1, 2, 1, 2]
7 3 3 1
After:  [1, 0, 1, 2]

Before: [0, 1, 2, 2]
5 1 2 1
After:  [0, 0, 2, 2]

Before: [0, 0, 2, 1]
6 0 0 0
After:  [0, 0, 2, 1]

Before: [1, 1, 0, 2]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 1, 3, 1]
0 1 2 2
After:  [1, 1, 0, 1]

Before: [1, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [0, 0, 3, 0]
6 0 0 1
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 0]
0 1 2 1
After:  [3, 0, 3, 0]

Before: [1, 2, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 0, 3]
2 0 2 2
After:  [1, 2, 0, 3]

Before: [1, 1, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 0, 3, 0]
12 3 2 2
After:  [0, 0, 1, 0]

Before: [1, 2, 0, 2]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 2, 3, 1]
13 0 3 3
After:  [0, 2, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 2, 2]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 0, 0, 1]
10 1 0 0
After:  [0, 0, 0, 1]

Before: [2, 1, 1, 1]
7 2 3 0
After:  [0, 1, 1, 1]

Before: [0, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 2, 1, 2]
6 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 3, 3, 1]
7 3 3 2
After:  [0, 3, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 1]
11 3 2 3
After:  [1, 1, 2, 1]

Before: [0, 1, 1, 3]
13 0 2 2
After:  [0, 1, 0, 3]

Before: [2, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [0, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 2
After:  [1, 1, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 1, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [3, 2, 1, 1]
1 2 3 2
After:  [3, 2, 2, 1]

Before: [2, 3, 2, 3]
9 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 0, 1]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [2, 2, 3, 3]
15 1 3 3
After:  [2, 2, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 2]
2 0 2 0
After:  [0, 1, 0, 2]

Before: [1, 1, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [0, 0, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [1, 3, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [2, 0, 1, 0]
10 1 0 2
After:  [2, 0, 0, 0]

Before: [1, 2, 0, 1]
2 0 2 0
After:  [0, 2, 0, 1]

Before: [0, 2, 2, 3]
15 1 3 3
After:  [0, 2, 2, 0]

Before: [2, 1, 2, 3]
5 1 2 1
After:  [2, 0, 2, 3]

Before: [1, 3, 2, 1]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 1]
4 3 1 1
After:  [0, 0, 2, 1]

Before: [3, 1, 3, 0]
0 1 2 2
After:  [3, 1, 0, 0]

Before: [2, 0, 2, 2]
3 0 2 0
After:  [4, 0, 2, 2]

Before: [0, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [2, 1, 2, 2]
5 1 2 1
After:  [2, 0, 2, 2]

Before: [1, 3, 0, 0]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [0, 3, 2, 0]
6 0 0 2
After:  [0, 3, 0, 0]

Before: [0, 3, 2, 3]
13 0 3 3
After:  [0, 3, 2, 0]

Before: [3, 0, 0, 0]
4 0 2 3
After:  [3, 0, 0, 1]

Before: [2, 3, 2, 2]
4 3 2 1
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 0]
3 0 2 2
After:  [2, 2, 4, 0]

Before: [3, 0, 3, 3]
9 3 0 3
After:  [3, 0, 3, 1]

Before: [0, 1, 2, 2]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 1]
1 2 3 3
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 2]
4 2 0 0
After:  [1, 2, 3, 2]

Before: [3, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 1, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [0, 3, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [3, 0, 0, 3]
9 3 0 2
After:  [3, 0, 1, 3]

Before: [0, 3, 3, 1]
9 2 3 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 0]
14 0 3 3
After:  [2, 0, 1, 1]

Before: [0, 2, 3, 0]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 2, 2]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 0, 2]
2 0 2 2
After:  [1, 0, 0, 2]

Before: [2, 0, 3, 0]
12 3 2 3
After:  [2, 0, 3, 1]

Before: [1, 1, 2, 1]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 3, 0, 0]
10 2 0 2
After:  [3, 3, 0, 0]

Before: [0, 3, 2, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 0, 3, 1]
10 1 0 0
After:  [0, 0, 3, 1]

Before: [2, 3, 1, 1]
7 2 3 1
After:  [2, 0, 1, 1]

Before: [3, 1, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [0, 2, 2, 3]
15 1 3 1
After:  [0, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 0
After:  [0, 3, 2, 1]

Before: [0, 1, 3, 0]
6 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 3, 2, 1]
7 3 3 1
After:  [1, 0, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 1, 0, 2]
12 2 3 3
After:  [3, 1, 0, 1]

Before: [3, 0, 2, 3]
10 1 0 0
After:  [0, 0, 2, 3]

Before: [3, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
5 1 2 1
After:  [1, 0, 2, 3]

Before: [1, 1, 0, 1]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 3, 3, 1]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [3, 2, 2, 3]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [1, 1, 2, 1]
8 0 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 1, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [3, 2, 2, 3]
9 2 1 2
After:  [3, 2, 1, 3]

Before: [1, 2, 2, 2]
8 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 0, 2, 2]
8 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 3, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 2, 3, 3]
15 1 3 3
After:  [3, 2, 3, 0]

Before: [0, 2, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 1
After:  [2, 0, 3, 1]

Before: [1, 3, 0, 1]
2 0 2 0
After:  [0, 3, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 3, 0, 2]
12 2 3 2
After:  [1, 3, 1, 2]

Before: [0, 3, 0, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [3, 3, 0, 1]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 3, 0, 0]
13 0 1 2
After:  [0, 3, 0, 0]

Before: [2, 1, 1, 0]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
10 1 0 1
After:  [3, 0, 0, 3]

Before: [2, 0, 2, 3]
15 2 3 0
After:  [0, 0, 2, 3]

Before: [1, 0, 0, 2]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [1, 1, 0, 3]
2 0 2 0
After:  [0, 1, 0, 3]

Before: [3, 0, 0, 0]
10 2 0 3
After:  [3, 0, 0, 0]

Before: [3, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 0, 0, 3]
10 2 0 2
After:  [3, 0, 0, 3]



13 0 0 0
3 0 2 0
8 3 0 1
13 0 0 3
3 3 1 3
4 0 1 0
13 0 1 0
1 2 0 2
8 2 1 3
8 1 2 0
13 0 0 1
3 1 0 1
2 0 3 1
13 1 3 1
13 1 3 1
1 2 1 2
11 2 0 0
8 3 0 2
8 3 2 1
8 0 0 3
12 3 2 2
13 2 2 2
13 2 1 2
1 0 2 0
11 0 3 1
8 3 1 3
8 0 2 2
8 0 3 0
0 3 2 3
13 3 1 3
1 1 3 1
11 1 1 3
8 3 1 0
8 0 2 1
13 3 0 2
3 2 2 2
4 2 0 1
13 1 3 1
1 3 1 3
11 3 2 1
8 0 2 3
8 1 0 0
15 3 2 2
13 2 3 2
1 1 2 1
11 1 2 3
8 3 0 1
8 2 0 2
11 0 2 2
13 2 3 2
1 2 3 3
11 3 2 0
13 2 0 2
3 2 3 2
8 3 1 3
0 3 2 3
13 3 1 3
1 3 0 0
11 0 3 1
8 2 2 3
8 2 1 2
8 3 0 0
4 2 0 3
13 3 1 3
1 3 1 1
11 1 0 2
8 3 3 3
8 2 2 0
13 1 0 1
3 1 0 1
5 3 0 3
13 3 1 3
1 2 3 2
11 2 3 1
8 1 1 0
8 0 2 3
8 2 0 2
11 0 2 3
13 3 1 3
1 3 1 1
13 2 0 3
3 3 3 3
8 2 3 0
13 2 0 2
3 2 3 2
7 0 2 3
13 3 3 3
1 3 1 1
8 2 0 2
13 3 0 3
3 3 1 3
2 3 0 0
13 0 2 0
13 0 1 0
1 1 0 1
8 2 3 0
8 2 0 3
10 2 3 2
13 2 3 2
13 2 3 2
1 2 1 1
11 1 1 0
8 0 1 1
8 1 0 3
13 2 0 2
3 2 0 2
3 3 1 3
13 3 3 3
1 0 3 0
11 0 2 2
8 2 0 3
13 0 0 0
3 0 2 0
9 0 3 0
13 0 1 0
13 0 2 0
1 2 0 2
8 3 1 1
8 3 2 3
8 2 1 0
5 1 0 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 3 0
13 1 0 2
3 2 2 2
8 1 2 1
2 1 0 2
13 2 3 2
1 3 2 3
11 3 3 2
8 1 3 0
8 3 0 3
1 1 0 3
13 3 3 3
1 2 3 2
11 2 2 1
8 3 3 3
8 2 2 2
11 0 2 0
13 0 2 0
13 0 3 0
1 0 1 1
11 1 1 0
8 2 3 3
8 2 1 1
10 1 3 3
13 3 2 3
1 0 3 0
11 0 2 2
8 1 2 0
8 3 2 3
1 0 0 3
13 3 2 3
13 3 1 3
1 2 3 2
11 2 2 0
8 1 1 1
13 2 0 2
3 2 2 2
13 2 0 3
3 3 0 3
15 3 2 1
13 1 1 1
13 1 2 1
1 1 0 0
11 0 0 3
8 1 1 2
13 0 0 1
3 1 2 1
8 3 3 0
0 0 2 0
13 0 1 0
13 0 2 0
1 3 0 3
11 3 0 0
8 1 3 1
8 2 0 3
8 0 1 2
13 1 2 3
13 3 1 3
1 3 0 0
13 1 0 3
3 3 0 3
8 3 0 2
8 0 2 1
12 3 2 3
13 3 1 3
13 3 2 3
1 0 3 0
11 0 3 2
8 0 0 3
13 1 0 0
3 0 1 0
8 2 1 1
10 1 3 1
13 1 2 1
1 1 2 2
11 2 1 3
8 2 0 2
8 2 3 1
11 0 2 2
13 2 2 2
13 2 2 2
1 2 3 3
11 3 3 2
8 1 0 3
13 0 0 1
3 1 0 1
3 3 1 3
13 3 1 3
1 3 2 2
11 2 3 1
8 2 1 2
8 2 3 3
11 0 2 2
13 2 1 2
1 2 1 1
11 1 2 2
8 1 0 3
13 3 0 0
3 0 2 0
8 0 1 1
14 0 3 1
13 1 3 1
1 1 2 2
11 2 2 1
8 1 1 0
8 3 1 2
1 0 0 0
13 0 1 0
1 0 1 1
13 2 0 0
3 0 3 0
13 3 0 2
3 2 1 2
8 0 3 3
0 0 2 2
13 2 1 2
1 1 2 1
11 1 3 0
8 1 1 3
8 2 1 2
8 3 3 1
3 3 1 3
13 3 2 3
1 3 0 0
8 1 0 2
8 2 1 1
8 0 3 3
10 1 3 1
13 1 1 1
1 0 1 0
11 0 3 3
8 3 0 1
8 1 1 0
8 0 1 2
3 0 1 2
13 2 1 2
1 2 3 3
13 2 0 2
3 2 3 2
8 2 2 0
5 1 0 2
13 2 2 2
1 3 2 3
11 3 0 0
8 2 2 2
8 2 1 3
5 1 3 3
13 3 1 3
1 3 0 0
11 0 1 1
8 3 0 2
8 1 2 0
8 0 1 3
8 2 3 3
13 3 3 3
1 3 1 1
8 2 3 2
8 3 3 0
8 1 3 3
6 2 0 0
13 0 2 0
13 0 1 0
1 1 0 1
11 1 3 3
8 1 2 0
13 2 0 1
3 1 3 1
4 2 1 2
13 2 1 2
1 2 3 3
8 3 0 0
8 2 3 2
4 2 0 1
13 1 1 1
1 3 1 3
11 3 1 0
8 2 3 1
8 0 1 3
15 3 2 1
13 1 1 1
13 1 1 1
1 1 0 0
11 0 1 1
8 0 3 0
15 3 2 3
13 3 2 3
13 3 3 3
1 1 3 1
13 3 0 0
3 0 2 0
8 0 2 2
13 1 0 3
3 3 1 3
13 3 2 0
13 0 3 0
1 1 0 1
8 0 0 3
8 3 2 0
7 2 0 0
13 0 3 0
1 0 1 1
11 1 1 2
8 1 0 0
8 1 1 3
8 1 2 1
1 3 0 3
13 3 3 3
1 3 2 2
11 2 1 3
8 0 2 1
8 0 3 2
13 0 2 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 1
8 3 3 2
8 0 3 3
8 2 0 0
10 0 3 3
13 3 2 3
1 3 1 1
11 1 0 3
8 2 2 1
8 2 2 2
8 3 1 0
4 2 0 2
13 2 1 2
1 3 2 3
8 1 0 0
13 2 0 2
3 2 0 2
8 1 1 1
1 0 0 0
13 0 1 0
1 3 0 3
11 3 3 1
8 2 2 3
8 2 2 0
9 0 3 3
13 3 2 3
13 3 2 3
1 1 3 1
11 1 3 3
8 1 3 0
8 3 1 1
8 2 3 2
11 0 2 0
13 0 1 0
1 0 3 3
11 3 1 0
8 3 2 3
13 0 0 1
3 1 2 1
8 1 3 2
0 3 2 2
13 2 3 2
13 2 2 2
1 2 0 0
11 0 0 1
8 3 1 0
8 2 0 3
8 0 0 2
7 2 0 2
13 2 3 2
13 2 2 2
1 1 2 1
11 1 3 3
8 2 1 2
8 1 2 0
8 0 2 1
11 0 2 0
13 0 2 0
1 3 0 3
11 3 3 2
8 2 2 0
8 0 0 3
10 0 3 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 2 0
8 1 1 1
8 3 3 2
13 1 2 0
13 0 3 0
13 0 3 0
1 0 3 3
11 3 0 1
8 1 0 3
8 2 3 0
7 0 2 0
13 0 1 0
1 1 0 1
11 1 3 2
8 2 1 0
13 2 0 1
3 1 3 1
14 0 3 3
13 3 1 3
1 3 2 2
11 2 0 0
8 2 2 1
13 0 0 2
3 2 0 2
13 0 0 3
3 3 2 3
12 2 3 2
13 2 1 2
13 2 2 2
1 2 0 0
11 0 0 1
13 2 0 3
3 3 1 3
8 3 3 2
8 2 2 0
14 0 3 2
13 2 1 2
13 2 2 2
1 2 1 1
11 1 0 0
8 3 1 3
13 1 0 2
3 2 3 2
13 0 0 1
3 1 2 1
6 1 2 1
13 1 1 1
1 0 1 0
11 0 1 2
8 2 1 0
8 1 1 3
8 0 2 1
2 3 0 0
13 0 2 0
13 0 1 0
1 0 2 2
11 2 3 0
8 3 1 3
8 3 1 1
8 2 2 2
4 2 1 3
13 3 2 3
13 3 3 3
1 3 0 0
8 3 3 2
13 0 0 3
3 3 3 3
8 1 3 1
13 1 2 2
13 2 2 2
13 2 2 2
1 0 2 0
11 0 3 2
8 2 2 0
13 0 0 1
3 1 2 1
8 2 2 3
10 0 3 1
13 1 2 1
1 1 2 2
11 2 3 3
13 3 0 0
3 0 3 0
8 0 1 2
8 3 2 1
7 2 0 1
13 1 2 1
1 3 1 3
13 2 0 1
3 1 1 1
7 2 0 0
13 0 1 0
13 0 3 0
1 3 0 3
11 3 3 1
8 2 1 2
8 3 2 3
13 0 0 0
3 0 3 0
4 2 0 0
13 0 2 0
1 1 0 1
11 1 3 3
8 1 3 2
8 2 3 0
8 3 3 1
5 1 0 0
13 0 1 0
1 0 3 3
8 2 0 2
8 1 0 0
8 0 0 1
11 0 2 2
13 2 3 2
1 3 2 3
11 3 0 1
13 0 0 0
3 0 2 0
8 2 1 3
8 3 2 2
9 0 3 3
13 3 2 3
1 3 1 1
11 1 1 3
8 3 3 1
8 2 2 2
13 2 0 0
3 0 1 0
4 2 1 0
13 0 3 0
1 3 0 3
11 3 0 1
13 1 0 3
3 3 1 3
13 0 0 2
3 2 3 2
8 1 2 0
13 0 2 3
13 3 1 3
13 3 3 3
1 1 3 1
11 1 3 0
8 0 2 1
8 0 1 3
8 2 3 2
13 2 1 2
1 2 0 0
13 3 0 2
3 2 2 2
13 2 0 1
3 1 3 1
4 2 1 1
13 1 3 1
1 0 1 0
11 0 0 1
8 1 2 2
8 2 3 0
8 3 0 2
13 2 2 2
1 2 1 1
11 1 1 0
8 1 0 1
8 1 1 2
8 1 3 3
1 3 3 2
13 2 2 2
1 0 2 0
11 0 1 1
8 3 2 0
8 2 3 2
8 0 0 3
4 2 0 3
13 3 3 3
1 1 3 1
11 1 0 0
8 3 2 2
8 0 0 1
8 3 0 3
8 2 3 3
13 3 1 3
1 3 0 0
11 0 0 2
13 2 0 0
3 0 2 0
8 1 0 1
8 2 1 3
9 0 3 1
13 1 1 1
13 1 2 1
1 2 1 2
11 2 2 0
8 3 0 1
8 1 0 2
0 1 2 2
13 2 3 2
13 2 3 2
1 2 0 0
8 2 2 1
8 2 1 2
8 0 0 3
15 3 2 3
13 3 1 3
1 3 0 0
11 0 2 3
8 3 3 0
8 3 3 2
8 0 1 1
0 0 2 0
13 0 2 0
13 0 2 0
1 3 0 3
11 3 1 1
8 2 0 0
8 3 2 3
7 0 2 2
13 2 2 2
1 1 2 1
11 1 1 0
8 0 3 3
13 1 0 2
3 2 2 2
8 0 0 1
15 3 2 1
13 1 3 1
1 0 1 0
11 0 0 1
8 3 3 0
13 3 0 2
3 2 1 2
8 1 1 3
1 3 3 0
13 0 2 0
1 0 1 1
11 1 1 0
8 3 0 3
13 0 0 2
3 2 3 2
8 2 2 1
8 2 3 1
13 1 2 1
1 1 0 0
11 0 0 2
8 2 2 0
8 1 2 1
8 1 2 3
2 3 0 3
13 3 2 3
1 3 2 2
8 3 0 1
13 1 0 3
3 3 2 3
9 0 3 1
13 1 2 1
13 1 2 1
1 1 2 2
8 1 3 0
8 2 3 1
10 1 3 3
13 3 1 3
1 2 3 2
11 2 1 1
8 2 1 3
8 3 3 2
1 0 0 2
13 2 3 2
1 1 2 1
8 2 2 0
13 3 0 2
3 2 2 2
9 0 3 3
13 3 1 3
1 3 1 1
8 2 2 3
8 1 2 2
13 0 0 0
3 0 1 0
2 0 3 2
13 2 1 2
1 1 2 1
8 0 1 0
8 3 3 2
8 3 0 2
13 2 1 2
1 2 1 1
11 1 1 2
8 3 0 0
8 0 1 1
5 0 3 1
13 1 1 1
13 1 1 1
1 1 2 2
11 2 0 1
13 2 0 0
3 0 1 0
8 3 0 2
8 0 2 3
12 3 2 0
13 0 1 0
1 0 1 1
11 1 2 0
8 3 0 1
13 1 0 2
3 2 0 2
8 3 2 3
8 2 1 1
13 1 3 1
13 1 3 1
1 1 0 0
11 0 3 1
8 0 3 3
8 3 2 2
8 1 1 0
12 3 2 2
13 2 3 2
13 2 2 2
1 2 1 1
11 1 0 3
13 0 0 0
3 0 0 0
8 1 2 1
13 1 0 2
3 2 0 2
8 2 1 0
13 0 2 0
1 0 3 3
11 3 1 0
13 0 0 3
3 3 0 3
8 3 3 1
13 3 0 2
3 2 2 2
15 3 2 2
13 2 2 2
13 2 2 2
1 0 2 0
8 1 0 1
8 0 3 2
8 2 2 3
2 1 3 1
13 1 2 1
1 1 0 0
11 0 2 1
8 2 2 2
8 2 3 0
9 0 3 0
13 0 1 0
13 0 3 0
1 1 0 1
8 0 2 0
13 3 0 2
3 2 0 2
12 2 3 2
13 2 3 2
13 2 1 2
1 2 1 1
11 1 2 0
13 3 0 2
3 2 1 2
8 2 1 1
8 0 0 3
10 1 3 2
13 2 1 2
13 2 2 2
1 0 2 0
11 0 3 3
8 1 1 1
8 3 2 0
8 3 0 2
13 1 2 0
13 0 2 0
1 3 0 3
11 3 3 0
8 2 0 1
8 0 2 3
6 1 2 2
13 2 2 2
1 2 0 0
11 0 2 2
8 0 0 1
8 2 1 0
8 3 0 0
13 0 1 0
13 0 2 0
1 0 2 2
11 2 3 3
8 3 3 2
8 3 0 1
8 2 1 0
4 0 1 2
13 2 3 2
1 3 2 3
11 3 2 2
8 2 2 3
13 1 0 1
3 1 2 1
10 1 3 3
13 3 3 3
1 2 3 2
11 2 3 3
8 0 3 0
8 0 1 2
8 3 3 1
0 1 2 1
13 1 1 1
13 1 2 1
1 1 3 3
11 3 1 2
8 1 1 1
13 2 0 3
3 3 2 3
2 1 3 1
13 1 2 1
13 1 2 1
1 2 1 2
11 2 1 3
8 2 2 2
13 2 0 1
3 1 0 1
8 3 3 0
6 2 0 2
13 2 1 2
13 2 3 2
1 3 2 3
11 3 2 0
13 0 0 3
3 3 0 3
8 3 0 2
8 3 2 1
12 3 2 1
13 1 3 1
13 1 2 1
1 0 1 0
11 0 2 2
8 1 2 1
8 2 0 0
10 0 3 3
13 3 2 3
1 3 2 2
11 2 1 1
8 2 1 3
8 3 0 2
6 0 2 3
13 3 1 3
13 3 2 3
1 3 1 1
11 1 1 2
13 2 0 3
3 3 1 3
8 0 2 1
14 0 3 0
13 0 1 0
1 2 0 2
11 2 3 0
8 1 0 2
8 2 3 3
8 1 3 3
13 3 2 3
13 3 2 3
1 3 0 0
11 0 0 3
8 3 1 2
13 0 0 0
3 0 2 0
7 0 2 2
13 2 1 2
1 2 3 3
11 3 1 1
8 2 0 2
8 0 0 0
8 1 1 3
8 3 0 2
13 2 1 2
1 1 2 1
11 1 0 0
8 2 0 3
8 1 1 1
13 1 0 2
3 2 3 2
2 1 3 2
13 2 2 2
1 2 0 0
8 3 2 1
8 0 0 2
5 1 3 2
13 2 3 2
1 0 2 0
11 0 2 3
8 2 2 2
8 2 1 0
8 1 3 1
2 1 0 0
13 0 1 0
1 3 0 3
11 3 0 1
8 2 1 3
13 0 0 2
3 2 1 2
8 1 1 0
1 0 0 3
13 3 3 3
1 3 1 1
8 2 0 0
8 2 3 3
13 2 0 2
3 2 0 2
9 0 3 0
13 0 3 0
1 0 1 1
11 1 3 0
8 2 2 2
8 0 3 3
8 0 1 1
15 3 2 2
13 2 3 2
1 0 2 0
11 0 2 3
8 3 2 0
13 3 0 2
3 2 2 2
6 2 0 0
13 0 1 0
1 0 3 3
11 3 3 0
8 3 3 3
8 0 3 2
8 2 2 1
5 3 1 2
13 2 3 2
13 2 1 2
1 0 2 0
11 0 0 1
8 2 0 0
8 0 0 3
8 0 0 2
10 0 3 3
13 3 1 3
1 3 1 1
11 1 2 3
8 3 3 2
8 0 1 1
8 2 1 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 0'''

# COMMAND ----------

import re

all_ops = ('addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr')

def execute(op, a, b, c, r):
  if op in ('addi', 'addr', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'gtri', 'gtrr', 'eqri', 'eqrr'):
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

def get_possible_ops(before, instruction, after):
  possible_ops = set()
  _, a, b, c = instruction
  for op in all_ops:
    r = before.copy()
    execute(op, a, b, c, r)
    if r == after:
      possible_ops.add(op)
  return possible_ops

effects, instructions = inp.split('\n\n\n\n')
effects = [[[int(x) for x in group] for group in re.findall(r'(\d+),? (\d+),? (\d+),? (\d+)', line)] for line in effects.split('\n\n')]
instructions = [[int(x) for x in line.split(' ')] for line in instructions.splitlines()]

possible_ops = [get_possible_ops(before, instruction, after) for before, instruction, after in effects]

answer = sum(len(x) >= 3 for x in possible_ops)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Using the samples you collected, <span title="This is one of my favorite puzzles.">work out the number of each opcode</span> and execute the test program (the second section of your puzzle input).</p>
# MAGIC <p><em>What value is contained in register <code>0</code> after executing the test program?</em></p>
# MAGIC </article>

# COMMAND ----------

import collections

def get_mapping(possible_mapping, op_mapping):
  if len(op_mapping) == 16:
    return op_mapping
  
  opcode, ops = min(possible_mapping.items(), key=lambda x: len(x[1]))

  for op in ops:
    if op in op_mapping.values():
      continue

    new_possible_mapping = possible_mapping.copy()
    del new_possible_mapping[opcode]
    
    new_op_mapping = op_mapping.copy()
    new_op_mapping[opcode] = op
    
    result = get_mapping(new_possible_mapping, new_op_mapping)
    if result:
      return result
  return None


def solve(effects):
  possible_mapping = collections.defaultdict(lambda: set(all_ops))
  for opcode, ops in zip([op for _, (op, _, _, _), _ in effects], possible_ops):
    possible_mapping[opcode] &= ops

  mapping = get_mapping(possible_mapping, {})

  r = [0] * 4
  for opcode, a, b, c in instructions:
    execute(mapping[opcode], a, b, c, r)
  
  return r[0]

answer = solve(effects)
print(answer)
