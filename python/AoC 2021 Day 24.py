# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 24: Arithmetic Logic Unit ---</h2><p><a href="https://en.wikipedia.org/wiki/Magic_smoke" target="_blank">Magic smoke</a> starts leaking from the submarine's <a href="https://en.wikipedia.org/wiki/Arithmetic_logic_unit">arithmetic logic unit</a> (ALU). Without the ability to perform basic arithmetic and logic functions, the submarine can't produce cool patterns with its Christmas lights!</p>
# MAGIC <p>It also can't navigate. Or run the oxygen system.</p>
# MAGIC <p>Don't worry, though - you <em>probably</em> have enough oxygen left to give you enough time to build a new ALU.</p>
# MAGIC <p>The ALU is a four-dimensional processing unit: it has integer variables <code>w</code>, <code>x</code>, <code>y</code>, and <code>z</code>. These variables all start with the value <code>0</code>. The ALU also supports <em>six instructions</em>:</p>
# MAGIC <ul>
# MAGIC <li><code>inp a</code> - Read an input value and write it to variable <code>a</code>.</li>
# MAGIC <li><code>add a b</code> - Add the value of <code>a</code> to the value of <code>b</code>, then store the result in variable <code>a</code>.</li>
# MAGIC <li><code>mul a b</code> - Multiply the value of <code>a</code> by the value of <code>b</code>, then store the result in variable <code>a</code>.</li>
# MAGIC <li><code>div a b</code> - Divide the value of <code>a</code> by the value of <code>b</code>, truncate the result to an integer, then store the result in variable <code>a</code>. (Here, "truncate" means to round the value toward zero.)</li>
# MAGIC <li><code>mod a b</code> - Divide the value of <code>a</code> by the value of <code>b</code>, then store the <em>remainder</em> in variable <code>a</code>. (This is also called the <a href="https://en.wikipedia.org/wiki/Modulo_operation" target="_blank">modulo</a> operation.)</li>
# MAGIC <li><code>eql a b</code> - If the value of <code>a</code> and <code>b</code> are equal, then store the value <code>1</code> in variable <code>a</code>. Otherwise, store the value <code>0</code> in variable <code>a</code>.</li>
# MAGIC </ul>
# MAGIC <p>In all of these instructions, <code>a</code> and <code>b</code> are placeholders; <code>a</code> will always be the variable where the result of the operation is stored (one of <code>w</code>, <code>x</code>, <code>y</code>, or <code>z</code>), while <code>b</code> can be either a variable or a number. Numbers can be positive or negative, but will always be integers.</p>
# MAGIC <p>The ALU has no <em>jump</em> instructions; in an ALU program, every instruction is run exactly once in order from top to bottom. The program halts after the last instruction has finished executing.</p>
# MAGIC <p>(Program authors should be especially cautious; attempting to execute <code>div</code> with <code>b=0</code> or attempting to execute <code>mod</code> with <code>a&lt;0</code> or <code>b&lt;=0</code>  will cause the program to crash and might even <span title="Maybe this is what happened to the last one.">damage the ALU</span>. These operations are never intended in any serious ALU program.)</p>
# MAGIC <p>For example, here is an ALU program which takes an input number, negates it, and stores it in <code>x</code>:</p>
# MAGIC <pre><code>inp x
# MAGIC mul x -1
# MAGIC </code></pre>
# MAGIC <p>Here is an ALU program which takes two input numbers, then sets <code>z</code> to <code>1</code> if the second input number is three times larger than the first input number, or sets <code>z</code> to <code>0</code> otherwise:</p>
# MAGIC <pre><code>inp z
# MAGIC inp x
# MAGIC mul z 3
# MAGIC eql z x
# MAGIC </code></pre>
# MAGIC <p>Here is an ALU program which takes a non-negative integer as input, converts it into binary, and stores the lowest (1's) bit in <code>z</code>, the second-lowest (2's) bit in <code>y</code>, the third-lowest (4's) bit in <code>x</code>, and the fourth-lowest (8's) bit in <code>w</code>:</p>
# MAGIC <pre><code>inp w
# MAGIC add z w
# MAGIC mod z 2
# MAGIC div w 2
# MAGIC add y w
# MAGIC mod y 2
# MAGIC div w 2
# MAGIC add x w
# MAGIC mod x 2
# MAGIC div w 2
# MAGIC mod w 2
# MAGIC </code></pre>
# MAGIC <p>Once you have built a replacement ALU, you can install it in the submarine, which will immediately resume what it was doing when the ALU failed: validating the submarine's <em>model number</em>. To do this, the ALU will run the MOdel Number Automatic Detector program (MONAD, your puzzle input).</p>
# MAGIC <p>Submarine model numbers are always <em>fourteen-digit numbers</em> consisting only of digits <code>1</code> through <code>9</code>. The digit <code>0</code> <em>cannot</em> appear in a model number.</p>
# MAGIC <p>When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen separate <code>inp</code> instructions, each expecting a <em>single digit</em> of the model number in order of most to least significant. (So, to check the model number <code>13579246899999</code>, you would give <code>1</code> to the first <code>inp</code> instruction, <code>3</code> to the second <code>inp</code> instruction, <code>5</code> to the third <code>inp</code> instruction, and so on.) This means that when operating MONAD, each input instruction should only ever be given an integer value of at least <code>1</code> and at most <code>9</code>.</p>
# MAGIC <p>Then, after MONAD has finished running all of its instructions, it will indicate that the model number was <em>valid</em> by leaving a <code>0</code> in variable <code>z</code>. However, if the model number was <em>invalid</em>, it will leave some other non-zero value in <code>z</code>.</p>
# MAGIC <p>MONAD imposes additional, mysterious restrictions on model numbers, and legend says the last copy of the MONAD documentation was eaten by a <a href="https://en.wikipedia.org/wiki/Japanese_raccoon_dog" target="_blank">tanuki</a>. You'll need to <em>figure out what MONAD does</em> some other way.</p>
# MAGIC <p>To enable as many submarine features as possible, find the largest valid fourteen-digit model number that contains no <code>0</code> digits. <em>What is the largest model number accepted by MONAD?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y'''

# COMMAND ----------

import functools

ops = [line.split(' ') for line in inp.splitlines()]


def run(step, input_z, digit):
  input_i = 0
  r = {
    'w': digit,
    'x': 0,
    'y': 0,
    'z': input_z,
  }
  for i in range(18 * step + 1, 18 * (step + 1)):
    op, *args = ops[i]
    arg_values = [r[arg] if arg in r else int(arg) for arg in args]

    if op == 'add':
      r[args[0]] += arg_values[1]
    elif op == 'mul':
      r[args[0]] *= arg_values[1]
    elif op == 'div':
      r[args[0]] //= arg_values[1]
    elif op == 'mod':
      r[args[0]] %= arg_values[1]
    elif op == 'eql':
      r[args[0]] = int(arg_values[0] == arg_values[1])

  return r['z']


@functools.lru_cache(maxsize=None)
def solve(step, input_z, find_min):
  if step == 14:
    return '' if input_z == 0 else None
  
  digit_order = range(1, 10) if find_min else range(9, -1, -1)
    
  for digit in digit_order:
    output_z = run(step, input_z, digit)
    other_digits = solve(step + 1, output_z, find_min)

    if other_digits is not None:
      return str(digit) + other_digits
    

solve.cache_clear()

answer = solve(0, 0, False) # 1.5 hrs
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As the submarine starts booting up things like the <a href="https://www.youtube.com/watch?v=RXJKdh1KZ0w" target="_blank">Retro Encabulator</a>, you realize that maybe you don't need all these submarine features after all.</p>
# MAGIC <p><em>What is the smallest model number accepted by MONAD?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = solve(0, 0, True) # 1 minute
print(answer)
