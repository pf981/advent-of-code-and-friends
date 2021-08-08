# Databricks notebook source
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

library(tidyverse)

# COMMAND ----------

input <- "#ip 2
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
seti 5 8 2
"

# COMMAND ----------

ip_register <- read_lines(input, n_max = 1) %>% str_extract("\\d+") %>% parse_integer()
ip_register

# COMMAND ----------

instructions <-
  read_lines(input, skip = 1) %>%
  str_split(" ") %>%
  map_dfr(set_names, c("op", "a", "b", "output_register")) %>%
  mutate_at(vars(-op), parse_integer)
instructions

# COMMAND ----------

# MAGIC %md
# MAGIC ```
# MAGIC Label |  Line  |    Instruction          |    V1                             |    V2
# MAGIC ------------------------------------------------------------------------------------------------------
# MAGIC       |  0     |    seti 123 0 3         |    r3 = 123                       |    ;
# MAGIC Z:    |  1     |    bani 3 456 3         |    r3 = r3 & 456                  |    ;
# MAGIC       |  2     |    eqri 3 72 3          |    r3 = r3 == 72                  |    ;
# MAGIC       |  3     |    addr 3 2 2           |    r2 += r3; GOTO A               |    ;
# MAGIC       |  4     |    seti 0 0 2           |    r2 = 0; GOTO Z                 |    ;
# MAGIC A:    |  5     |    seti 0 4 3           |    r3 = 0;                        |    ;
# MAGIC K:    |  6     |    bori 3 65536 4       |    r4 = r3 | 65536                |    r4 = r3 | 65536
# MAGIC       |  7     |    seti 1107552 3 3     |    r3 = 1107552                   |    r3 = 1107552
# MAGIC J:    |  8     |    bani 4 255 5         |    r5 = r4 & 255                  |    r5 = r4 & 255
# MAGIC       |  9     |    addr 3 5 3           |    r3 += r5                       |    r3 += r5
# MAGIC       |  10    |    bani 3 16777215 3    |    r3 &= 16777215                 |    r3 &= 16777215
# MAGIC       |  11    |    muli 3 65899 3       |    r3 *= 65899                    |    r3 *= 65899
# MAGIC       |  12    |    bani 3 16777215 3    |    r3 &= 16777215                 |    r3 &= 16777215
# MAGIC       |  13    |    gtir 256 4 5         |    r5 = 256 > r4                  |    ;
# MAGIC       |  14    |    addr 5 2 2           |    r2 += r5; IF r5 THEN GOTO B    |    IF 256 > r4 GOTO D
# MAGIC       |  15    |    addi 2 1 2           |    r2 += 1; GOTO C                |    ;
# MAGIC B:    |  16    |    seti 27 0 2          |    r2 = 27; GOTO D                |    ;
# MAGIC C:    |  17    |    seti 0 2 5           |    r5 = 0                         |    r5 = 0
# MAGIC I:    |  18    |    addi 5 1 1           |    r1 = r5 + 1                    |    r1 = r5 + 1
# MAGIC       |  19    |    muli 1 256 1         |    r1 *= 256                      |    r1 *= 256
# MAGIC       |  20    |    gtrr 1 4 1           |    r1 = r1 > r4                   |    ;
# MAGIC       |  21    |    addr 1 2 2           |    r2 += r1; IF r1 THEN GOTO E    |    IF r1 > r4 GOTO G
# MAGIC       |  22    |    addi 2 1 2           |    r2 += 1; GOTO F                |    ;
# MAGIC E:    |  23    |    seti 25 3 2          |    r2 = 25; GOTO G                |    ;
# MAGIC F:    |  24    |    addi 5 1 5           |    r5++                           |    r5++
# MAGIC       |  25    |    seti 17 3 2          |    r2 = 17; GOTO I                |    GOTO I
# MAGIC G:    |  26    |    setr 5 3 4           |    r4 = r5                        |    r4 = r5
# MAGIC       |  27    |    seti 7 4 2           |    r2 = 7; GOTO J                 |    GOTO J
# MAGIC D:    |  28    |    eqrr 3 0 5           |    r5 = r3 == r0                  |    ;
# MAGIC       |  29    |    addr 5 2 2           |    r2 += r5; IF r5 THEN HALT      |    IF r3 == r0 THEN HALT
# MAGIC       |  30    |    seti 5 8 2           |    r2 = 5; GOTO K                 |    GOTO K
# MAGIC ```

# COMMAND ----------

Rcpp::cppFunction('
std::vector<int64_t> find_halt_values() {
  std::set<int64_t> halt_values_s;
  std::vector<int64_t> halt_values;

  int64_t result;
  int r0 = 0, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
K:	r4 = r3 | 65536;
	r3 = 1107552;
J:	r5 = r4 & 255;
	r3 += r5;
	r3 &= 16777215;
	r3 *= 65899;
	r3 &= 16777215;
	;
	if (256 > r4) goto D;
	;
B:	;
C:	r5 = 0;
I:	r1 = r5 + 1;
	r1 *= 256;
	;
	if (r1 > r4) goto G;
	;
E:	;
F:	r5++;
	goto I;
G:	r4 = r5;
	goto J;
D:	;

    // START NEW CODE
    if (halt_values_s.find(r3) != halt_values_s.end()) return halt_values; 
	halt_values_s.insert(r3);
	halt_values.push_back(r3);
    // END NEW CODE

	goto K;
}
')

# COMMAND ----------

halt_values <- find_halt_values()
answer <- first(halt_values)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>In order to determine the timing window for your underflow exploit, you also need an upper bound:</p>
# MAGIC <p><em>What is the lowest non-negative integer value for register <code>0</code> that causes the program to halt after executing the most instructions?</em> (The program must actually halt; running forever does not count as halting.)</p>
# MAGIC </article>

# COMMAND ----------

answer <- last(halt_values)
answer
