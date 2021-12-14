# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 14: Extended Polymerization ---</h2><p>The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has <a href="https://en.wikipedia.org/wiki/Polymerization" target="_blank">polymerization</a> equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.</p>
# MAGIC <p>The submarine manual contains <span title="HO
# MAGIC 
# MAGIC HO -> OH">instructions</span> for finding the optimal polymer formula; specifically, it offers a <em>polymer template</em> and a list of <em>pair insertion</em> rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>NNCB
# MAGIC 
# MAGIC CH -&gt; B
# MAGIC HH -&gt; N
# MAGIC CB -&gt; H
# MAGIC NH -&gt; C
# MAGIC HB -&gt; C
# MAGIC HC -&gt; B
# MAGIC HN -&gt; C
# MAGIC NN -&gt; C
# MAGIC BH -&gt; H
# MAGIC NC -&gt; B
# MAGIC NB -&gt; B
# MAGIC BN -&gt; B
# MAGIC BB -&gt; N
# MAGIC BC -&gt; B
# MAGIC CC -&gt; N
# MAGIC CN -&gt; C
# MAGIC </code></pre>
# MAGIC <p>The first line is the <em>polymer template</em> - this is the starting point of the process.</p>
# MAGIC <p>The following section defines the <em>pair insertion</em> rules. A rule like <code>AB -&gt; C</code> means that when elements <code>A</code> and <code>B</code> are immediately adjacent, element <code>C</code> should be inserted between them. These insertions all happen simultaneously.</p>
# MAGIC <p>So, starting with the polymer template <code>NNCB</code>, the first step simultaneously considers all three pairs:</p>
# MAGIC <ul>
# MAGIC <li>The first pair (<code>NN</code>) matches the rule <code>NN -&gt; C</code>, so element <code><em>C</em></code> is inserted between the first <code>N</code> and the second <code>N</code>.</li>
# MAGIC <li>The second pair (<code>NC</code>) matches the rule <code>NC -&gt; B</code>, so element <code><em>B</em></code> is inserted between the <code>N</code> and the <code>C</code>.</li>
# MAGIC <li>The third pair (<code>CB</code>) matches the rule <code>CB -&gt; H</code>, so element <code><em>H</em></code> is inserted between the <code>C</code> and the <code>B</code>.</li>
# MAGIC </ul>
# MAGIC <p>Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.</p>
# MAGIC <p>After the first step of this process, the polymer becomes <code>N<em>C</em>N<em>B</em>C<em>H</em>B</code>.</p>
# MAGIC <p>Here are the results of a few steps using the above rules:</p>
# MAGIC <pre><code>Template:     NNCB
# MAGIC After step 1: NCNBCHB
# MAGIC After step 2: NBCCNBBBCBHCB
# MAGIC After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# MAGIC After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# MAGIC </code></pre>
# MAGIC <p>This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, <code>B</code> occurs 1749 times, <code>C</code> occurs 298 times, <code>H</code> occurs 191 times, and <code>N</code> occurs 865 times; taking the quantity of the most common element (<code>B</code>, 1749) and subtracting the quantity of the least common element (<code>H</code>, 161) produces <code>1749 - 161 = <em>1588</em></code>.</p>
# MAGIC <p>Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. <em>What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''CBNBOKHVBONCPPBBCKVH

FK -> O
BK -> B
PB -> N
VS -> P
OF -> H
KP -> K
PS -> K
OV -> N
FO -> H
KN -> P
HF -> K
BV -> N
OO -> B
KC -> V
CK -> H
BC -> P
VV -> S
NS -> C
SF -> O
BN -> V
NH -> N
VP -> F
KH -> S
BO -> N
VN -> K
BB -> H
CH -> H
HP -> O
KK -> O
CB -> S
VC -> P
FH -> B
SP -> C
NF -> O
HN -> N
PO -> P
PP -> C
SO -> F
FB -> B
SB -> B
SC -> B
HK -> O
BF -> V
OB -> B
NC -> V
HC -> F
KO -> C
NV -> C
HB -> H
FP -> S
OS -> O
HH -> K
OK -> B
OH -> C
NP -> V
SN -> H
SK -> B
HV -> F
VF -> P
CP -> H
FN -> H
FV -> B
CN -> H
OC -> O
KV -> P
CF -> B
OP -> B
FC -> O
PC -> B
CV -> S
PV -> H
VK -> N
SS -> C
HO -> F
VH -> C
NB -> S
NN -> F
FF -> K
CC -> H
SV -> H
CO -> K
BP -> O
SH -> H
KS -> K
FS -> F
PF -> S
BS -> H
VO -> H
NK -> F
PK -> B
KB -> K
CS -> C
VB -> V
BH -> O
KF -> N
HS -> H
PH -> K
ON -> H
PN -> K
NO -> S'''

# COMMAND ----------

import collections
import functools

starting_polymer, mapping = inp.split('\n\n')
mapping = dict([x.split(' -> ') for x in mapping.splitlines()])


@functools.lru_cache(maxsize=None)
def get_counts_from_pair(pair, n_steps):
  if pair not in mapping or n_steps == 0:
    return collections.Counter(pair)

  middle_character = mapping[pair]
  left_pair = pair[0] + middle_character
  right_pair =  middle_character + pair[1]

  left_counts = get_counts_from_pair(left_pair, n_steps - 1)
  right_counts = get_counts_from_pair(right_pair, n_steps - 1)

  return left_counts + right_counts


def solve(polymer, n_steps):
  letter_counts_doubled = sum(
    (get_counts_from_pair(''.join(pair), n_steps) for pair in zip(polymer[:-1], polymer[1:])),
    collections.Counter(polymer[0] + polymer[-1])
  )
  most_common, *_, least_common = (count_doubled // 2 for _, count_doubled in letter_counts_doubled.most_common())
  return most_common - least_common


get_counts_from_pair.cache_clear()

answer = solve(starting_polymer, 10)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of <em>40 steps</em> should do it.</p>
# MAGIC <p>In the above example, the most common element is <code>B</code> (occurring <code>2192039569602</code> times) and the least common element is <code>H</code> (occurring <code>3849876073</code> times); subtracting these produces <code><em>2188189693529</em></code>.</p>
# MAGIC <p>Apply <em>40</em> steps of pair insertion to the polymer template and find the most and least common elements in the result. <em>What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = solve(starting_polymer, 40)
print(answer)
