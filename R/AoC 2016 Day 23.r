# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Safe Cracking ---</h2><p>This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who <em>wouldn't</em> hide a star in a safe behind a painting?</p>
# MAGIC <p>The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see <code>7</code>.</p>
# MAGIC <p>When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your <a href="11">prototype computer</a>! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.</p>
# MAGIC <p></p>Now, you just need to figure out what output the keypad would have sent to the safe. You extract the <a href="12">assembunny code</a> from the logic chip (your puzzle input).<p></p>
# MAGIC <p>The code looks like it uses <em>almost</em> the same architecture and instruction set that the <a href="12">monorail computer</a> used! You should be able to <em>use the same assembunny interpreter</em> for this as you did there, but with one new instruction:</p>
# MAGIC <p><code>tgl x</code> <em>toggles</em> the instruction <code>x</code> away (pointing at instructions like <code>jnz</code> does: positive means forward; negative means backward):</p>
# MAGIC <ul>
# MAGIC <li>For <em>one-argument</em> instructions, <code>inc</code> becomes <code>dec</code>, and all other one-argument instructions become <code>inc</code>.</li>
# MAGIC <li>For <em>two-argument</em> instructions, <code>jnz</code> becomes <code>cpy</code>, and all other two-instructions become <code>jnz</code>.</li>
# MAGIC <li>The arguments of a toggled instruction are <em>not affected</em>.</li>
# MAGIC <li>If an attempt is made to toggle an instruction outside the program, <em>nothing happens</em>.</li>
# MAGIC <li>If toggling produces an <em>invalid instruction</em> (like <code>cpy 1 2</code>) and an attempt is later made to execute that instruction, <em>skip it instead</em>.</li>
# MAGIC <li>If <code>tgl</code> toggles <em>itself</em> (for example, if <code>a</code> is <code>0</code>, <code>tgl a</code> would target itself and become <code>inc a</code>), the resulting instruction is not executed until the next time it is reached.</li>
# MAGIC </ul>
# MAGIC <p>For example, given this program:</p>
# MAGIC <pre><code>cpy 2 a
# MAGIC tgl a
# MAGIC tgl a
# MAGIC tgl a
# MAGIC cpy 1 a
# MAGIC dec a
# MAGIC dec a
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li><code>cpy 2 a</code> initializes register <code>a</code> to <code>2</code>.</li>
# MAGIC <li>The first <code>tgl a</code> toggles an instruction <code>a</code> (<code>2</code>) away from it, which changes the third <code>tgl a</code> into <code>inc a</code>.</li>
# MAGIC <li>The second <code>tgl a</code> also modifies an instruction <code>2</code> away from it, which changes the <code>cpy 1 a</code> into <code>jnz 1 a</code>.</li>
# MAGIC <li>The fourth line, which is now <code>inc a</code>, increments <code>a</code> to <code>3</code>.</li>
# MAGIC <li>Finally, the fifth line, which is now <code>jnz 1 a</code>, jumps <code>a</code> (<code>3</code>) instructions ahead, skipping the <code>dec a</code> instructions.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the final value in register <code>a</code> is <code>3</code>.</p>
# MAGIC <p>The rest of the electronics seem to place the keypad entry (the number of eggs, <code>7</code>) in register <code>a</code>, run the code, and then send the value left in register <code>a</code> to the safe.</p>
# MAGIC <p><em>What value</em> should be sent to the safe?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 95 c
jnz 99 d
inc a
inc d
jnz d -2
inc c
jnz c -5
"

# COMMAND ----------

# input <- "cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
# "

# COMMAND ----------

df <-
  tibble(line = read_lines(input)) %>%
  mutate(
    instruction = str_extract(line, "^\\w+"),
    x = str_extract(line, "(?<= )-?\\w+"),
    y = str_extract(line, "-?\\w+$")
  )
df

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp(std::vector<std::string> instructions, std::vector<std::string> xs, std::vector<std::string> ys, int eggs = 7) { 
    std::unordered_map<std::string, int> registers;
    registers["a"] = eggs;

    auto getValue = [&registers] (const std::string& s) {
      try {
        return std::stoi(s);
      }
      catch (...) {
        return registers[s];
      }
    };

    for(int line = 0; line < instructions.size(); ++line) {
        const std::string& instruction = instructions[line];
        const std::string& x = xs[line];
        const std::string& y = ys[line];

        if (instruction == "cpy") {
           try {
            registers[y] = getValue(x);
          }
          catch (...) {
            // If y is a number (from tgl making an invalid cpy command), dont do anything
          }
          
        }
        else if (instruction == "inc") {
          ++registers[x];
        }
        else if (instruction == "dec") {
          --registers[x];
        }
        else if (instruction == "jnz")  {
          if (getValue(x) != 0) {
            line = line + getValue(y) - 1;
          }
        }
        else if (instruction == "tgl")  {
          int target_i = line + getValue(x);

          if (target_i < 0 || target_i >= instructions.size()) continue;

          std::string& target_instruction = instructions[target_i];
          if (target_instruction == "inc") {
            target_instruction = "dec";
          }
          else if (target_instruction == "dec" || target_instruction == "tgl") {
            target_instruction = "inc";
          }
          else if (target_instruction == "jnz") {
            target_instruction = "cpy";
          }
          else if (target_instruction == "cpy") {
            target_instruction = "jnz";
          }
        }
    }

    return registers["a"];
} 
')

# COMMAND ----------

answer <- solve_cpp(df$instruction, df$x, df$y)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The safe doesn't open, but it <em>does</em> make several <span title="SUCH INCORRECT! VERY LOCK! WOW!">angry noises</span> to express its frustration.</p>
# MAGIC <p>You're quite sure your logic is working correctly, so the only other thing is... you check the painting again. As it turns out, colored eggs are still eggs. Now you count <code>12</code>.</p>
# MAGIC <p>As you run the program with this new input, the prototype computer begins to <em>overheat</em>. You wonder what's taking so long, and whether the lack of any instruction more powerful than "add one" has anything to do with it. Don't bunnies usually <em>multiply</em>?</p>
# MAGIC <p>Anyway, <em>what value</em> should actually be sent to the safe?</p>
# MAGIC </article>

# COMMAND ----------

# Just look at the code and see that it is doing this
answer <- 95 * 99 + factorial(12)
answer
