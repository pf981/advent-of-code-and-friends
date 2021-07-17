# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 12: Leonardo's Monorail ---</h2><p>You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.</p>
# MAGIC <p>While sitting on a nearby bench amidst some <a href="https://www.google.com/search?q=tiger+lilies&amp;tbm=isch">tiger lilies</a>, you manage to decrypt some of the files you extracted from the servers downstairs.</p>
# MAGIC <p>According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.</p>
# MAGIC <p>You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's <span title="Strangely, this assembunny code doesn't seem to be very good at multiplying.">assembunny</span> code designed for the <a href="11">new computer</a> you just assembled. You'll have to execute the code and get the password.</p>
# MAGIC <p>The assembunny code you've extracted operates on four <a href="https://en.wikipedia.org/wiki/Processor_register">registers</a> (<code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>) that start at <code>0</code> and can hold any <a href="https://en.wikipedia.org/wiki/Integer">integer</a>. However, it seems to make use of only a few <a href="https://en.wikipedia.org/wiki/Instruction_set">instructions</a>:</p>
# MAGIC <ul>
# MAGIC <li><code>cpy x y</code> <em>copies</em> <code>x</code> (either an integer or the <em>value</em> of a register) into register <code>y</code>.</li>
# MAGIC <li><code>inc x</code> <em>increases</em> the value of register <code>x</code> by one.</li>
# MAGIC <li><code>dec x</code> <em>decreases</em> the value of register <code>x</code> by one.</li>
# MAGIC <li><code>jnz x y</code> <em>jumps</em> to an instruction <code>y</code> away (positive means forward; negative means backward), but only if <code>x</code> is <em>not zero</em>.</li>
# MAGIC </ul>
# MAGIC <p>The <code>jnz</code> instruction moves relative to itself: an offset of <code>-1</code> would continue at the previous instruction, while an offset of <code>2</code> would <em>skip over</em> the next instruction.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>cpy 41 a
# MAGIC inc a
# MAGIC inc a
# MAGIC dec a
# MAGIC jnz a 2
# MAGIC dec a
# MAGIC </code></pre>
# MAGIC <p>The above code would set register <code>a</code> to <code>41</code>, increase its value by <code>2</code>, decrease its value by <code>1</code>, and then skip the last <code>dec a</code> (because <code>a</code> is not zero, so the <code>jnz a 2</code> skips it), leaving register <code>a</code> at <code>42</code>. When you move past the last instruction, the program halts.</p>
# MAGIC <p>After executing the assembunny code in your puzzle input, <em>what value is left in register <code>a</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
"

# COMMAND ----------

# input <- "cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
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

get_value <- function(state, x) {
  value <- suppressWarnings(parse_integer(x))
  if (is.na(value)) {
    value <- state[[x]]
  }
  if (is.null(value)) {
    value <- 0
  }
  value
}

cpy <- function(state, x, y) {
  value <- get_value(state, x)
  
  state[[y]] <- value
  state[["line"]] <- state[["line"]] + 1
  state
}

inc <- function(state, x, y) {
  state[[x]] <- get_value(state, x) + 1
  state[["line"]] <- state[["line"]] + 1
  state
}

dec <- function(state, x, y) {
  state[[x]] <- get_value(state, x) - 1
  state[["line"]] <- state[["line"]] + 1
  state
}

jnz <- function(state, x, y) {
  jump <- 1
  if (get_value(state, x) != 0) {
    jump <- get_value(state, y)
  }
  
  state[["line"]] <- state[["line"]] + jump
  state
}

# COMMAND ----------

state <- list(line = 1, a = 0, b = 0)

while (state$line <= nrow(df)) {
  inst <- df %>% slice(state$line)
  
  f <- get(inst$instruction)
  state <- f(state, inst$x, inst$y)
}
state # Took 1.3 hrs

# COMMAND ----------

answer <- state$a
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you head down the fire escape to the monorail, you notice it didn't start; register <code>c</code> needs to be initialized to the position of the ignition key.</p>
# MAGIC <p>If you instead <em>initialize register <code>c</code> to be <code>1</code></em>, what value is now left in register <code>a</code>?</p>
# MAGIC </article>

# COMMAND ----------

# This R solution was way too slow, so I did it in c++

# get_value <- function(state, x) {
#   value <- as.integer(x)
#   if (is.na(value)) {
#     value <- state[[x]]
#   }
#   if (is.null(value)) {
#     value <- 0
#   }
#   value
# }

# line <- 1
# state <- list(c = 1)
# while (line <= nrow(df)) {
#   instruction <- df$instruction[line]
#   x <- df$x[line]
#   y <- df$y[line]
  
#   if (instruction == "cpy") {
    
#   } else if (instruction == "cpy") {
#     state[[y]] <- get_value(state, x)
#   } else if (instruction == "inc") {
#     state[[x]] <- get_value(state, x) + 1
#   } else if (instruction == "dec") {
#     state[[x]] <- get_value(state, x) - 1
#   } else if (instruction == "jnz") {
#     if (get_value(state, x) != 0) {
#       line <- line + get_value(state, y) - 1
#     }
#   }
  
#   line <- line + 1
# }

# answer <- state$a
# answer

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp(std::vector<std::string> instructions, std::vector<std::string> xs, std::vector<std::string> ys) { 
    std::unordered_map<std::string, int> registers;
    registers["c"] = 1;

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
          registers[y] = getValue(x);
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
    }

    return registers["a"];
} 
')

# COMMAND ----------

answer <- solve_cpp(df$instruction, df$x, df$y)
answer
