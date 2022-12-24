# Databricks notebook source
# MAGIC %sh
# MAGIC wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
# MAGIC %sh bash Anaconda3-2022.10-Linux-x86_64.sh -b
# MAGIC /root/anaconda3/condabin/conda config --add channels conda-forge
# MAGIC /root/anaconda3/condabin/conda config --set channel_priority strict
# MAGIC /root/anaconda3/condabin/conda create --yes -n pypy pypy
# MAGIC # /root/anaconda3/condabin/conda activate pypy

# COMMAND ----------

# MAGIC %sh
# MAGIC {
# MAGIC cat << EOF
# MAGIC inp = '''inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 15
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 15
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 12
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 5
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 13
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 6
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -14
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 7
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 15
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 9
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -7
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 6
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 14
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 14
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 15
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 3
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 1
# MAGIC add x 15
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 1
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -7
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 3
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -8
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 4
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -7
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 6
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -5
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 7
# MAGIC mul y x
# MAGIC add z y
# MAGIC inp w
# MAGIC mul x 0
# MAGIC add x z
# MAGIC mod x 26
# MAGIC div z 26
# MAGIC add x -10
# MAGIC eql x w
# MAGIC eql x 0
# MAGIC mul y 0
# MAGIC add y 25
# MAGIC mul y x
# MAGIC add y 1
# MAGIC mul z y
# MAGIC mul y 0
# MAGIC add y w
# MAGIC add y 1
# MAGIC mul y x
# MAGIC add z y'''
# MAGIC 
# MAGIC import functools
# MAGIC 
# MAGIC ops = [line.split(' ') for line in inp.splitlines()]
# MAGIC 
# MAGIC 
# MAGIC def run(step, input_z, digit):
# MAGIC   input_i = 0
# MAGIC   r = {
# MAGIC     'w': digit,
# MAGIC     'x': 0,
# MAGIC     'y': 0,
# MAGIC     'z': input_z,
# MAGIC   }
# MAGIC   for i in range(18 * step + 1, 18 * (step + 1)):
# MAGIC     op, *args = ops[i]
# MAGIC     arg_values = [r[arg] if arg in r else int(arg) for arg in args]
# MAGIC 
# MAGIC     if op == 'add':
# MAGIC       r[args[0]] += arg_values[1]
# MAGIC     elif op == 'mul':
# MAGIC       r[args[0]] *= arg_values[1]
# MAGIC     elif op == 'div':
# MAGIC       r[args[0]] //= arg_values[1]
# MAGIC     elif op == 'mod':
# MAGIC       r[args[0]] %= arg_values[1]
# MAGIC     elif op == 'eql':
# MAGIC       r[args[0]] = int(arg_values[0] == arg_values[1])
# MAGIC 
# MAGIC   return r['z']
# MAGIC 
# MAGIC 
# MAGIC @functools.cache
# MAGIC def solve(step, input_z, find_min):
# MAGIC   if step == 14:
# MAGIC     return '' if input_z == 0 else None
# MAGIC   
# MAGIC   digit_order = range(1, 10) if find_min else range(9, -1, -1)
# MAGIC     
# MAGIC   for digit in digit_order:
# MAGIC     output_z = run(step, input_z, digit)
# MAGIC     other_digits = solve(step + 1, output_z, find_min)
# MAGIC 
# MAGIC     if other_digits is not None:
# MAGIC       return str(digit) + other_digits
# MAGIC     
# MAGIC 
# MAGIC solve.cache_clear()
# MAGIC 
# MAGIC answer = solve(0, 0, False) # 1.5 hrs
# MAGIC print(answer)
# MAGIC 
# MAGIC EOF
# MAGIC } | /root/anaconda3/envs/pypy/bin/pypy3.9 -

# COMMAND ----------

# Eh. I was testing if JIT would magically make this faster. It didn't.
