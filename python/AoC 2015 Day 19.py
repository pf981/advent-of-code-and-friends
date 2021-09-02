# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/19

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 19: Medicine for Rudolph ---</h2><p>Rudolph the Red-Nosed Reindeer is sick!  His nose isn't shining very brightly, and he needs medicine.</p>
# MAGIC <p>Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine.  Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.</p>
# MAGIC <p>The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need.  It works by starting with some input molecule and then doing a series of <em>replacements</em>, one per step, until it has the right molecule.</p>
# MAGIC <p>However, the machine has to be calibrated before it can be used.  Calibration involves determining the number of molecules that can be generated in one step from a given starting point.</p>
# MAGIC <p>For example, imagine a simpler machine that supports only the following replacements:</p>
# MAGIC <pre><code>H =&gt; HO
# MAGIC H =&gt; OH
# MAGIC O =&gt; HH
# MAGIC </code></pre>
# MAGIC <p>Given the replacements above and starting with <code>HOH</code>, the following molecules could be generated:</p>
# MAGIC <ul>
# MAGIC <li><code>HOOH</code> (via <code>H =&gt; HO</code> on the first <code>H</code>).</li>
# MAGIC <li><code>HOHO</code> (via <code>H =&gt; HO</code> on the second <code>H</code>).</li>
# MAGIC <li><code>OHOH</code> (via <code>H =&gt; OH</code> on the first <code>H</code>).</li>
# MAGIC <li><code>HOOH</code> (via <code>H =&gt; OH</code> on the second <code>H</code>).</li>
# MAGIC <li><code>HHHH</code> (via <code>O =&gt; HH</code>).</li>
# MAGIC </ul>
# MAGIC <p>So, in the example above, there are <code>4</code> <em>distinct</em> molecules (not five, because <code>HOOH</code> appears twice) after one replacement from <code>HOH</code>. Santa's favorite molecule, <code>HOHOHO</code>, can become <code>7</code> <em>distinct</em> molecules (over nine replacements: six from <code>H</code>, and three from <code>O</code>).</p>
# MAGIC <p>The machine replaces without regard for the surrounding characters.  For example, given the string <code>H2O</code>, the transition <code>H =&gt; OO</code> would result in <code>OO2O</code>.</p>
# MAGIC <p>Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine.  <em>How many distinct molecules can be created</em> after all the different ways you can do one replacement on the medicine molecule?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'''

# COMMAND ----------

import re

replacements, medicine_molecule = inp.split('\n\n')
replacements = [line.split(' => ') for line in replacements.split('\n')]

molecules = set()
for source, dest in replacements:
  for new_molecule in [medicine_molecule[:m.start()] + dest + medicine_molecule[m.end():] for m in re.finditer(source, medicine_molecule)]:
    molecules.add(new_molecule)

answer = len(molecules)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that the machine is calibrated, you're ready to begin molecule fabrication.</p>
# MAGIC <p>Molecule fabrication always begins with just a single <span title="It's a Red-Nosed Reindeer electron.">electron</span>, <code>e</code>, and applying replacements one at a time, just like the ones during calibration.</p>
# MAGIC <p>For example, suppose you have the following replacements:</p>
# MAGIC <pre><code>e =&gt; H
# MAGIC e =&gt; O
# MAGIC H =&gt; HO
# MAGIC H =&gt; OH
# MAGIC O =&gt; HH
# MAGIC </code></pre>
# MAGIC <p>If you'd like to make <code>HOH</code>, you start with <code>e</code>, and then make the following replacements:</p>
# MAGIC <ul>
# MAGIC <li><code>e =&gt; O</code> to get <code>O</code></li>
# MAGIC <li><code>O =&gt; HH</code> to get <code>HH</code></li>
# MAGIC <li><code>H =&gt; OH</code> (on the second <code>H</code>) to get <code>HOH</code></li>
# MAGIC </ul>
# MAGIC <p>So, you could make <code>HOH</code> after <em><code>3</code> steps</em>.  Santa's favorite molecule, <code>HOHOHO</code>, can be made in <em><code>6</code> steps</em>.</p>
# MAGIC <p>How long will it take to make the medicine?  Given the available <em>replacements</em> and the <em>medicine molecule</em> in your puzzle input, what is the <em>fewest number of steps</em> to go from <code>e</code> to the medicine molecule?</p>
# MAGIC </article>

# COMMAND ----------

import random

molecule = medicine_molecule
n_steps = 0

while molecule != 'e':
  random.shuffle(replacements)

  no_progress = True
  for source, dest in replacements:
    if dest in molecule:
      molecule = molecule.replace(dest, source, 1)
      n_steps += 1
      no_progress = False

  if no_progress:
    n_steps = 0
    molecule = medicine_molecule

answer = n_steps
answer
