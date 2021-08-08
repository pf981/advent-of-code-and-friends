# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 19: Go With The Flow ---</h2><p>With the Elves well on their way constructing the North Pole base, you turn your attention back to understanding the inner workings of programming the device.</p>
# MAGIC <p>You can't help but notice that the <a href="16">device's opcodes</a> don't contain any <em>flow control</em> like jump instructions. The device's <a href="16">manual</a> goes on to explain:</p>
# MAGIC <p>"In programs where flow control is required, the <a href="https://en.wikipedia.org/wiki/Program_counter">instruction pointer</a> can be <em>bound to a register</em> so that it can be manipulated directly. This way, <code>setr</code>/<code>seti</code> can function as absolute jumps, <code>addr</code>/<code>addi</code> can function as relative jumps, and other opcodes can cause <span title="Good luck maintaining a program that uses a bitwise operation on its instruction pointer, though.">truly fascinating</span> effects."</p>
# MAGIC <p>This mechanism is achieved through a declaration like <code>#ip 1</code>, which would modify register <code>1</code> so that accesses to it let the program indirectly access the instruction pointer itself. To compensate for this kind of binding, there are now <em>six</em> registers (numbered <code>0</code> through <code>5</code>); the five not bound to the instruction pointer behave as normal. Otherwise, the same rules apply as <a href="16">the last time you worked with this device</a>.</p>
# MAGIC <p>When the <em>instruction pointer</em> is bound to a register, its value is written to that register just before each instruction is executed, and the value of that register is written back to the instruction pointer immediately after each instruction finishes execution. Afterward, move to the next instruction by adding one to the instruction pointer, even if the value in the instruction pointer was just updated by an instruction. (Because of this, instructions must effectively set the instruction pointer to the instruction <em>before</em> the one they want executed next.)</p>
# MAGIC <p>The instruction pointer is <code>0</code> during the first instruction, <code>1</code> during the second, and so on. If the instruction pointer ever causes the device to attempt to load an instruction outside the instructions defined in the program, the program instead immediately halts. The instruction pointer starts at <code>0</code>.</p>
# MAGIC <p>It turns out that this new information is already proving useful: the CPU in the device is not very powerful, and a background process is occupying most of its time.  You dump the background process' declarations and instructions to a file (your puzzle input), making sure to use the names of the opcodes rather than the numbers.</p>
# MAGIC <p>For example, suppose you have the following program:</p>
# MAGIC <pre><code>#ip 0
# MAGIC seti 5 0 1
# MAGIC seti 6 0 2
# MAGIC addi 0 1 0
# MAGIC addr 1 2 3
# MAGIC setr 1 0 0
# MAGIC seti 8 0 4
# MAGIC seti 9 0 5
# MAGIC </code></pre>
# MAGIC <p>When executed, the following instructions are executed. Each line contains the value of the instruction pointer at the time the instruction started, the values of the six registers before executing the instructions (in square brackets), the instruction itself, and the values of the six registers after executing the instruction (also in square brackets).</p>
# MAGIC <pre><code>ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
# MAGIC ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
# MAGIC ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
# MAGIC ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
# MAGIC ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]
# MAGIC </code></pre>
# MAGIC <p>In detail, when running this program, the following events occur:</p>
# MAGIC <ul>
# MAGIC <li>The first line (<code>#ip 0</code>) indicates that the instruction pointer should be bound to register <code>0</code> in this program. This is not an instruction, and so the value of the instruction pointer does not change during the processing of this line.</li>
# MAGIC <li>The instruction pointer contains <code>0</code>, and so the first instruction is executed (<code>seti 5 0 1</code>).  It updates register <code>0</code> to the current instruction pointer value (<code>0</code>), sets register <code>1</code> to <code>5</code>, sets the instruction pointer to the value of register <code>0</code> (which has no effect, as the instruction did not modify register <code>0</code>), and then adds one to the instruction pointer.</li>
# MAGIC <li>The instruction pointer contains <code>1</code>, and so the second instruction, <code>seti 6 0 2</code>, is executed. This is very similar to the instruction before it: <code>6</code> is stored in register <code>2</code>, and the instruction pointer is left with the value <code>2</code>.</li>
# MAGIC <li>The instruction pointer is <code>2</code>, which points at the instruction <code>addi 0 1 0</code>.  This is like a <em>relative jump</em>: the value of the instruction pointer, <code>2</code>, is loaded into register <code>0</code>. Then, <code>addi</code> finds the result of adding the value in register <code>0</code> and the value <code>1</code>, storing the result, <code>3</code>, back in register <code>0</code>. Register <code>0</code> is then copied back to the instruction pointer, which will cause it to end up <code>1</code> larger than it would have otherwise and skip the next instruction (<code>addr 1 2 3</code>) entirely. Finally, <code>1</code> is added to the instruction pointer.</li>
# MAGIC <li>The instruction pointer is <code>4</code>, so the instruction <code>setr 1 0 0</code> is run. This is like an <em>absolute jump</em>: it copies the value contained in register <code>1</code>, <code>5</code>, into register <code>0</code>, which causes it to end up in the instruction pointer. The instruction pointer is then incremented, leaving it at <code>6</code>.</li>
# MAGIC <li>The instruction pointer is <code>6</code>, so the instruction <code>seti 9 0 5</code> stores <code>9</code> into register <code>5</code>. The instruction pointer is incremented, causing it to point outside the program, and so the program ends.</li>
# MAGIC </ul>
# MAGIC <p><em>What value is left in register <code>0</code></em> when the background process halts?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "#ip 1
addi 1 16 1
seti 1 5 3
seti 1 7 5
mulr 3 5 4
eqrr 4 2 4
addr 4 1 1
addi 1 1 1
addr 3 0 0
addi 5 1 5
gtrr 5 2 4
addr 1 4 1
seti 2 1 1
addi 3 1 3
gtrr 3 2 4
addr 4 1 1
seti 1 3 1
mulr 1 1 1
addi 2 2 2
mulr 2 2 2
mulr 1 2 2
muli 2 11 2
addi 4 7 4
mulr 4 1 4
addi 4 13 4
addr 2 4 2
addr 1 0 1
seti 0 9 1
setr 1 0 4
mulr 4 1 4
addr 1 4 4
mulr 1 4 4
muli 4 14 4
mulr 4 1 4
addr 2 4 2
seti 0 2 0
seti 0 0 1
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

Rcpp::cppFunction('
int solve_cpp(int ip_register, std::vector<std::string> ops, std::vector<int> as, std::vector<int> bs, std::vector<int> output_registers) {
  int ip = 0;
  int registers[6] = {0};
  
  while (true) {
    std::string op = ops[ip];
    int a = as[ip];
    int b = bs[ip];
    int output_register = output_registers[ip];
    
    // Execute instruction
    if (op == "addi" || op == "addr" || op == "mulr" || op == "muli" || op == "banr" || op == "bani" || op == "borr" || op == "bori" || op == "setr" || op == "gtri" || op == "gtrr" || op == "eqri" || op == "eqrr") {
      a = registers[a];
    }
    if (op == "addr" || op == "mulr" || op == "banr" || op == "borr" || op == "gtir" || op == "gtrr" || op == "eqir" || op == "eqrr") {
      b = registers[b];
    }
    
    if (op == "addr" || op == "addi") {
      registers[output_register] = a + b;
    } else if (op == "mulr" || op == "muli") {
      registers[output_register] = a * b;
    } else if (op == "banr" || op == "bani") {
      registers[output_register] = a & b;
    } else if (op == "borr" || op == "bori") {
      registers[output_register] = a | b;
    } else if (op == "setr" || op == "seti") {
      registers[output_register] = a;
    } else if (op == "gtir" || op == "gtri" || op == "gtrr") {
      registers[output_register] = a > b;
    } else if (op == "eqir" || op == "eqri" || op == "eqrr") {
      registers[output_register] = a == b;
    }
    
    
    if (registers[ip_register] + 1 >= ops.size()) break;
  
    registers[ip_register] = registers[ip_register] + 1;
    ip = registers[ip_register];
  }
  
  return registers[0];
}
')

# COMMAND ----------

answer <- solve_cpp(
  ip_register = ip_register,
  op = instructions$op,
  a = instructions$a,
  b = instructions$b,
  output_register = instructions$output_register
)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>A new background process immediately spins up in its place. It appears identical, but on closer inspection, you notice that <em>this time, register <code>0</code> started with the value <code>1</code></em>.</p>
# MAGIC <p><em>What value is left in register <code>0</code></em> when this new background process halts?</p>
# MAGIC </article>

# COMMAND ----------

# MAGIC %md ```
# MAGIC Label | Line |    Instruction   |    V1                             |    V2                                  |    V3
# MAGIC -------------------------------------------------------------------------------------------------------------------------------------------------------
# MAGIC       |      |                  |    r0 = 1                         |    r0 = 1                              |    ;
# MAGIC       |   0  |    addi 1 16 1   |    r1 += 16; GOTO A               |    GOTO A                              |    r2 = 10551403
# MAGIC B:    |   1  |    seti 1  5 3   |    r3 = 1                         |    r3 = 1                              |    r3 = 1
# MAGIC G:    |   2  |    seti 1  7 5   |    r5 = 1                         |    DO {                                |    DO {
# MAGIC I:    |   3  |    mulr 3  5 4   |    r4 = r3 * r5                   |      ;                                 |      ;
# MAGIC       |   4  |    eqrr 4  2 4   |    r4 = r4 == r2                  |      ;                                 |      DO {
# MAGIC       |   5  |    addr 4  1 1   |    r1 += r4; IF r4 THEN GOTO C    |      IF r3 * r5 == r2 THEN r0 += r3    |        IF r3 * r5 == r2 THEN r0 += r3
# MAGIC       |   6  |    addi 1  1 1   |    r1++; GOTO D                   |      ;                                 |        ;
# MAGIC C:    |   7  |    addr 3  0 0   |    r0 += r3                       |      ;                                 |        ;
# MAGIC D:    |   8  |    addi 5  1 5   |    r5++                           |      r5++                              |        r5++
# MAGIC       |   9  |    gtrr 5  2 4   |    r4 = r5 > r2                   |      ;                                 |    
# MAGIC       |  10  |    addr 1  4 1   |    r1 += r4; IF r4 THEN GOTO E    |      IF r5 <= r2 THEN GOTO I           |      } WHILE r5 <= r2
# MAGIC       |  11  |    seti 2  1 1   |    r1 = 2; GOTO I                 |      ;                                 |      ;
# MAGIC E:    |  12  |    addi 3  1 3   |    r3++                           |      r3++                              |      r3++
# MAGIC       |  13  |    gtrr 3  2 4   |    r4 = r3 > r2                   |      ;                                 |      ;
# MAGIC       |  14  |    addr 4  1 1   |    r1 += r4; IF r4 THEN GOTO F    |      ;                                 |      ;
# MAGIC       |  15  |    seti 1  3 1   |    r1 = 1; GOTO G                 |    } WHILE r3 <= r2                    |    } WHILE r3 <= r2
# MAGIC F:    |  16  |    mulr 1  1 1   |    r1 *= r1; HALT                 |    HALT                                |    HALT
# MAGIC A:    |  17  |    addi 2  2 2   |    r2 += 2                        |    r2 = 4*19*11                        |    ;
# MAGIC       |  18  |    mulr 2  2 2   |    r2 *= r2                       |    ;                                   |    ;
# MAGIC       |  19  |    mulr 1  2 2   |    r2 *= r1                       |    ;                                   |    ;
# MAGIC       |  20  |    muli 2 11 2   |    r2 *= 11                       |    ;                                   |    ;
# MAGIC       |  21  |    addi 4  7 4   |    r4 += 7                        |    r4 = 7*22+13                        |    ;
# MAGIC       |  22  |    mulr 4  1 4   |    r4 *= r1                       |    ;                                   |    ;
# MAGIC       |  23  |    addi 4 13 4   |    r4 += 13                       |    ;                                   |    ;
# MAGIC       |  24  |    addr 2  4 2   |    r2 += r4                       |    r2 += r4                            |    ;
# MAGIC       |  25  |    addr 1  0 1   |    r1 += r0; IF r0 THEN GOTO H    |    ;                                   |    ;
# MAGIC       |  26  |    seti 0  9 1   |    r1 = 0; GOTO B                 |    ;                                   |    ;
# MAGIC H:    |  27  |    setr 1  0 4   |    r4 = r1                        |    r4 = (27*28+29)*30*14*32            |    ;
# MAGIC       |  28  |    mulr 4  1 4   |    r4 *= r1                       |    ;                                   |    ;
# MAGIC       |  29  |    addr 1  4 4   |    r4 += r1                       |    ;                                   |    ;
# MAGIC       |  30  |    mulr 1  4 4   |    r4 *= r1                       |    ;                                   |    ;
# MAGIC       |  31  |    muli 4 14 4   |    r4 *= 14                       |    ;                                   |    ;
# MAGIC       |  32  |    mulr 4  1 4   |    r4 *= r1                       |    ;                                   |    ;
# MAGIC       |  33  |    addr 2  4 2   |    r2 *= r4                       |    r2 += r4                            |    ;
# MAGIC       |  34  |    seti 0  2 0   |    r0 = 0                         |    ;                                   |    ;
# MAGIC       |  35  |    seti 0  0 1   |    r1 = 0; GOTO B                 |    GOTO B                              |    ;
# MAGIC ```

# COMMAND ----------

# Sum of factors of 10551403
x <- 10551403
div <- seq_len(x)
factors <- div[x %% div == 0]
answer <- sum(factors)
answer
