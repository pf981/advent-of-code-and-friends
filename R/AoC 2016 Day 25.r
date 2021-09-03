# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/25

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 25: Clock Signal ---</h2><p>You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.</p>
# MAGIC <p>There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.</p>
# MAGIC <p>However, maybe the <em>huge antenna</em> up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.</p>
# MAGIC <p>You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.</p>
# MAGIC <p><span title="Then again, if something ever works on the first try, you should be *very* suspicious.">Nothing happens.</span></p>
# MAGIC <p>You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.</p>
# MAGIC <p>"No, no, a <a href="https://en.wikipedia.org/wiki/Clock_signal">clock signal</a> - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>...." He trails off.</p>
# MAGIC <p>You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's <em>no way</em> it can! The only antenna we've installed capable of <em>that</em> is on top of a top-secret Easter Bunny installation, and you're <em>definitely</em> not-" You hang up the phone.</p>
# MAGIC <p>You've extracted the antenna's clock signal generation <a href="12">assembunny</a> code (your puzzle input); it looks mostly compatible with code you worked on <a href="23">just recently</a>.</p>
# MAGIC <p>This antenna code, being a signal generator, uses one extra instruction:</p>
# MAGIC <ul>
# MAGIC <li><code>out x</code> <em>transmits</em> <code>x</code> (either an integer or the <em>value</em> of a register) as the next value for the clock signal.</li>
# MAGIC </ul>
# MAGIC <p>The code takes a value (via register <code>a</code>) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.</p>
# MAGIC <p><em>What is the lowest positive integer</em> that can be used to initialize register <code>a</code> and cause the code to output a clock signal of <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>... repeating forever?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "cpy a d
cpy 7 c
cpy 362 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21
"

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
bool is_clock(std::vector<std::string> instructions, std::vector<std::string> xs, std::vector<std::string> ys, int a) { 
    std::unordered_map<std::string, int> registers;
    registers["a"] = a;

    int clock_i = 0;

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
        else if (instruction == "out")  {
          if (clock_i % 2 != getValue(x)) return false;
          
          if (clock_i >= 100) return true;

          ++clock_i;
        }
    }

    return false;
} 
')

# COMMAND ----------

for (answer in seq_len(100000)) {
  if (is_clock(df$instruction, df$x, df$y, i)) break
}
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The antenna is ready. Now, all you need is the <em class="star">fifty stars</em> required to generate the signal for the sleigh, but you don't have enough.</p>
# MAGIC <p>You look toward the sky in desperation... suddenly noticing that a lone star has been installed at the top of the antenna!  Only <em>49 more</em> to go.</p>
# MAGIC </article>

# COMMAND ----------

# No puzzle here - just need 49 stars.
