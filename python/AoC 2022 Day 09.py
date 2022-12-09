# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/9

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 9: Rope Bridge ---</h2><p>This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.</p>
# MAGIC <p>It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.</p>
# MAGIC <p>You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where <em>not</em> to step.</p>
# MAGIC <p>Consider a rope with a knot at each end; these knots mark the <em>head</em> and the <em>tail</em> of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.</p>
# MAGIC <p>Due to nebulous reasoning involving <a href="https://en.wikipedia.org/wiki/Planck_units#Planck_length" target="_blank">Planck lengths</a>, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical <em>series of motions</em> (your puzzle input) for the head, you can determine how the tail will move.</p>
# MAGIC <p><span title="I'm an engineer, not a physicist!">Due to the aforementioned Planck lengths</span>, the rope must be quite short; in fact, the head (<code>H</code>) and tail (<code>T</code>) must <em>always be touching</em> (diagonally adjacent and even overlapping both count as touching):</p>
# MAGIC <pre><code>....
# MAGIC .TH.
# MAGIC ....
# MAGIC 
# MAGIC ....
# MAGIC .H..
# MAGIC ..T.
# MAGIC ....
# MAGIC 
# MAGIC ...
# MAGIC .H. (H covers T)
# MAGIC ...
# MAGIC </code></pre>
# MAGIC <p>If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:</p>
# MAGIC <pre><code>.....    .....    .....
# MAGIC .TH.. -&gt; .T.H. -&gt; ..TH.
# MAGIC .....    .....    .....
# MAGIC 
# MAGIC ...    ...    ...
# MAGIC .T.    .T.    ...
# MAGIC .H. -&gt; ... -&gt; .T.
# MAGIC ...    .H.    .H.
# MAGIC ...    ...    ...
# MAGIC </code></pre>
# MAGIC <p>Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:</p>
# MAGIC <pre><code>.....    .....    .....
# MAGIC .....    ..H..    ..H..
# MAGIC ..H.. -&gt; ..... -&gt; ..T..
# MAGIC .T...    .T...    .....
# MAGIC .....    .....    .....
# MAGIC 
# MAGIC .....    .....    .....
# MAGIC .....    .....    .....
# MAGIC ..H.. -&gt; ...H. -&gt; ..TH.
# MAGIC .T...    .T...    .....
# MAGIC .....    .....    .....
# MAGIC </code></pre>
# MAGIC <p>You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>R 4
# MAGIC U 4
# MAGIC L 3
# MAGIC D 1
# MAGIC R 4
# MAGIC D 1
# MAGIC L 5
# MAGIC R 2
# MAGIC </code></pre>
# MAGIC <p>This series of motions moves the head <em>right</em> four steps, then <em>up</em> four steps, then <em>left</em> three steps, then <em>down</em> one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (<code>s</code> marks the starting position as a reference point):</p>
# MAGIC <pre><code>== Initial State ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC H.....  (H covers T, s)
# MAGIC 
# MAGIC == R 4 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC TH....  (T covers s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC sTH...
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC s.TH..
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC s..TH.
# MAGIC 
# MAGIC == U 4 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ....H.
# MAGIC s..T..
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ....H.
# MAGIC ....T.
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ....H.
# MAGIC ....T.
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ....H.
# MAGIC ....T.
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == L 3 ==
# MAGIC 
# MAGIC ...H..
# MAGIC ....T.
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ..HT..
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC .HT...
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == D 1 ==
# MAGIC 
# MAGIC ..T...
# MAGIC .H....
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == R 4 ==
# MAGIC 
# MAGIC ..T...
# MAGIC ..H...
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ..T...
# MAGIC ...H..
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ...TH.
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ....TH
# MAGIC ......
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == D 1 ==
# MAGIC 
# MAGIC ......
# MAGIC ....T.
# MAGIC .....H
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == L 5 ==
# MAGIC 
# MAGIC ......
# MAGIC ....T.
# MAGIC ....H.
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ....T.
# MAGIC ...H..
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ..HT..
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC .HT...
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC HT....
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC == R 2 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC .H....  (H covers T)
# MAGIC ......
# MAGIC s.....
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC .TH...
# MAGIC ......
# MAGIC s.....
# MAGIC </code></pre>
# MAGIC <p>After simulating the rope, you can count up all of the positions the <em>tail visited at least once</em>. In this diagram, <code>s</code> again marks the starting position (which the tail also visited) and <code>#</code> marks other positions the tail visited:</p>
# MAGIC <pre><code>..##..
# MAGIC ...##.
# MAGIC .####.
# MAGIC ....#.
# MAGIC s###..
# MAGIC </code></pre>
# MAGIC <p>So, there are <code><em>13</em></code> positions the tail visited at least once.</p>
# MAGIC <p>Simulate your complete hypothetical series of motions. <em>How many positions does the tail of the rope visit at least once?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''U 1
R 1
L 1
D 1
R 1
L 1
D 1
L 2
D 1
R 1
D 2
L 1
R 1
D 2
U 2
L 1
R 1
U 1
D 1
R 1
L 2
R 2
L 1
R 2
D 1
U 1
R 1
L 2
R 2
D 2
U 1
L 2
D 2
U 2
L 2
U 1
R 1
L 1
D 2
L 1
U 2
L 1
D 1
U 2
R 2
U 1
D 2
U 2
D 1
L 2
R 1
D 1
R 1
D 2
L 1
U 2
D 1
L 2
U 1
D 1
L 2
R 2
D 2
L 2
U 1
D 1
L 2
U 2
L 2
U 2
R 1
L 1
R 2
D 2
R 1
L 2
R 1
D 1
R 1
U 2
D 2
L 1
U 2
D 2
L 2
U 1
R 1
D 1
U 1
R 1
L 2
U 2
L 1
R 2
L 2
D 2
U 1
D 2
U 1
L 1
U 2
D 2
R 1
D 1
L 2
R 2
D 1
L 1
R 1
U 1
L 2
R 2
U 1
R 3
D 2
U 2
L 3
R 3
D 3
U 3
R 1
D 2
R 1
D 1
L 2
R 3
D 3
U 3
D 3
R 1
U 2
D 3
L 3
R 2
L 2
D 3
U 2
D 1
R 3
D 1
U 1
L 2
D 1
U 1
L 1
D 1
R 3
D 2
L 1
R 1
L 2
U 3
L 1
U 1
L 3
R 3
L 3
R 2
D 2
R 1
U 2
R 1
D 3
U 3
L 1
U 2
D 3
R 2
D 1
U 1
D 1
R 3
U 1
R 2
L 1
D 1
U 1
R 2
L 1
U 3
L 1
R 1
U 3
L 3
D 2
R 2
D 1
L 3
R 3
D 1
L 2
U 3
D 1
U 1
R 1
L 1
U 2
D 2
R 3
U 3
R 1
U 2
D 2
R 2
D 2
R 1
L 2
D 1
U 2
L 3
U 2
D 3
L 2
R 1
D 1
L 1
U 2
D 1
L 3
R 2
D 2
R 3
L 3
D 3
U 1
R 1
L 3
R 2
L 1
U 2
L 4
D 1
L 4
D 3
L 3
D 2
U 3
L 3
D 4
U 4
D 4
L 3
D 1
R 4
D 4
R 2
L 3
D 4
R 3
D 3
R 3
L 4
U 3
R 1
D 4
U 2
R 3
U 2
L 4
R 3
L 2
R 4
L 2
R 4
U 2
R 4
U 3
L 3
D 4
R 3
U 4
R 3
D 4
U 2
D 4
U 1
R 1
U 3
D 4
U 2
D 3
L 2
U 4
L 1
U 1
L 1
U 3
R 2
U 1
R 3
D 1
U 2
R 1
U 4
D 3
L 4
U 4
R 1
D 2
L 4
R 3
U 2
L 1
U 1
L 2
U 4
D 1
L 3
R 3
L 3
R 4
L 2
R 4
U 2
D 3
R 4
L 3
R 1
L 3
D 4
L 1
R 4
U 3
R 3
L 4
D 3
R 4
L 4
R 2
L 4
D 4
R 4
D 4
R 4
L 3
D 1
U 4
R 5
L 3
R 3
L 1
R 3
D 3
U 5
R 2
U 4
D 1
R 3
D 1
R 3
U 5
D 5
U 5
L 2
D 1
U 3
L 5
R 1
D 5
L 3
U 5
L 3
R 5
L 1
U 3
D 1
L 5
R 2
U 5
L 1
D 1
U 1
D 5
L 2
U 4
R 2
D 1
U 3
L 3
D 1
R 4
D 3
U 2
D 3
R 5
U 5
D 1
L 3
U 2
R 2
D 3
U 5
R 1
L 4
D 3
R 3
D 4
L 3
D 5
R 5
D 3
R 1
U 3
R 1
L 3
D 3
L 3
D 1
R 1
U 4
D 4
R 2
D 4
L 4
U 5
L 2
R 5
D 5
R 1
D 1
R 1
L 1
R 4
U 4
L 2
R 2
L 5
D 3
R 5
L 5
D 2
R 1
D 2
R 2
L 1
U 1
R 5
U 4
D 2
U 3
D 3
R 4
L 2
D 5
U 5
L 5
R 4
D 1
U 3
R 3
L 6
U 6
R 6
L 2
D 2
U 3
R 4
D 2
L 1
R 1
L 1
R 1
L 4
U 2
D 2
U 4
R 1
L 3
U 1
L 3
U 1
L 3
D 6
U 5
D 2
L 3
D 4
L 3
U 5
D 4
R 3
L 2
U 6
L 3
D 5
L 3
R 2
D 3
R 1
U 4
D 2
U 3
R 5
D 1
R 1
U 5
L 3
U 6
R 1
U 1
R 2
L 3
D 5
R 1
U 5
L 4
D 4
R 5
L 6
R 4
U 3
R 5
U 2
D 4
R 1
U 1
L 6
D 3
L 5
U 4
R 1
D 5
U 3
D 3
R 6
L 3
D 4
U 6
L 3
D 3
L 2
U 1
R 3
D 1
L 3
U 3
R 2
D 2
L 1
R 4
D 6
U 6
R 4
D 6
R 5
D 2
U 1
L 5
D 6
L 2
U 3
D 2
R 4
L 6
U 6
L 3
D 4
L 2
U 3
R 6
D 5
R 7
L 3
D 4
R 5
U 5
L 2
D 6
R 1
D 1
L 6
D 4
U 2
D 4
R 7
L 1
U 4
R 4
D 4
U 5
D 2
L 2
R 6
U 6
R 4
L 6
U 1
R 7
U 3
L 1
R 2
L 4
D 2
U 6
R 1
U 2
L 6
U 6
L 6
U 7
L 3
D 7
L 7
D 6
U 2
R 6
L 7
R 4
D 4
R 2
U 1
D 7
U 6
L 2
D 7
U 2
R 7
U 6
D 3
L 5
U 2
D 4
R 4
U 1
D 2
L 1
R 2
U 6
R 2
U 2
D 2
L 1
U 7
R 6
L 1
R 2
D 1
R 2
L 5
U 7
R 7
U 3
D 1
R 6
L 6
U 1
D 4
R 4
L 1
R 4
U 6
D 7
L 2
R 6
L 1
D 2
R 2
L 4
D 3
U 4
L 5
R 1
L 3
U 2
D 1
U 3
R 7
D 2
U 2
L 7
R 7
D 2
R 4
L 8
R 2
L 5
D 6
L 8
R 3
D 3
R 1
D 6
U 5
R 5
U 8
R 7
U 2
L 2
R 5
L 1
U 6
D 7
R 7
U 5
R 7
L 4
R 4
U 8
L 3
U 2
D 2
U 1
R 1
U 7
D 3
R 2
D 5
U 7
L 8
R 4
L 5
D 1
U 7
D 3
R 7
U 1
R 6
U 4
L 8
R 8
U 5
L 5
U 3
L 7
D 5
U 5
R 8
U 1
D 1
U 1
R 7
D 2
U 2
D 5
L 4
D 4
U 5
L 2
R 5
U 7
R 6
U 5
L 1
D 2
U 8
L 7
D 2
R 2
D 6
U 1
D 3
L 2
D 7
R 3
D 2
U 6
D 6
U 7
L 2
R 8
U 2
D 4
L 3
R 3
D 7
L 5
U 7
R 2
L 8
R 8
L 1
D 6
L 2
U 6
L 8
D 5
R 8
U 1
R 4
D 1
L 7
U 2
D 9
L 5
U 2
D 8
L 6
D 9
U 9
R 1
D 8
L 8
D 9
U 3
R 4
U 6
D 9
L 3
R 1
U 5
L 5
D 5
L 8
D 1
U 9
L 4
D 3
L 9
R 5
L 9
D 5
L 2
U 7
R 6
D 4
U 8
L 7
D 7
U 5
L 9
R 3
L 9
U 4
L 4
R 7
L 5
R 2
D 1
U 2
R 3
L 5
R 9
L 3
D 9
L 9
U 5
D 3
U 6
D 3
L 3
U 5
D 1
R 1
L 8
R 1
D 6
R 2
U 6
L 6
R 3
D 2
R 4
U 6
R 8
U 4
D 8
R 1
U 8
D 4
L 9
U 8
L 2
U 1
R 2
D 7
R 1
D 9
R 3
L 6
U 6
L 2
R 7
U 5
R 8
L 3
D 5
R 3
U 9
D 5
R 5
U 1
L 6
D 2
R 2
D 3
L 2
U 2
L 5
U 9
L 8
D 2
U 7
R 6
U 3
L 8
U 5
D 4
U 4
R 2
D 1
L 7
U 4
R 1
L 3
D 7
R 5
D 8
R 4
U 3
L 3
D 3
U 5
L 3
D 1
R 10
D 4
U 6
D 4
R 7
U 5
L 2
R 5
D 8
R 3
U 6
R 5
L 9
R 7
D 6
U 10
R 10
D 5
R 9
U 4
R 6
L 8
U 5
L 9
R 8
D 2
U 5
D 4
R 3
D 10
U 9
L 5
U 5
L 10
D 7
U 4
D 10
U 1
D 8
L 6
D 9
R 5
U 2
R 3
U 1
D 8
R 3
U 4
D 6
U 10
D 4
U 3
D 5
R 1
L 8
R 9
D 2
U 8
L 1
R 8
U 5
R 9
U 9
R 7
D 5
L 5
D 8
L 7
U 1
L 4
D 2
R 3
D 1
U 2
L 1
D 1
U 6
R 5
U 5
R 6
L 1
U 5
R 5
U 8
L 9
D 2
R 10
U 2
R 6
U 8
R 2
L 11
U 3
D 4
R 6
L 8
R 10
U 10
R 6
L 4
R 11
U 11
R 3
U 11
L 7
R 4
L 7
U 5
D 2
U 8
R 9
D 9
R 1
U 9
D 6
U 3
D 10
L 7
D 8
R 9
U 9
D 7
L 11
D 8
R 8
U 11
L 11
U 4
D 6
R 1
D 8
R 2
U 1
L 11
R 10
L 6
U 8
L 10
U 5
L 11
U 6
L 5
U 10
R 5
U 11
R 6
D 4
U 7
L 11
D 3
U 8
R 8
L 2
D 10
L 5
D 10
R 4
U 3
L 7
U 10
D 4
U 10
R 2
U 1
D 6
L 6
U 7
D 4
R 6
D 11
L 1
U 5
L 1
D 9
R 11
L 8
D 3
U 7
R 9
D 1
U 3
R 1
L 8
D 6
U 9
D 9
L 10
U 8
D 5
L 1
U 2
D 3
L 11
R 3
L 7
D 1
U 8
D 5
L 8
R 7
L 8
D 4
R 7
D 11
R 3
L 1
R 6
U 3
R 11
L 5
R 4
L 1
D 6
R 7
U 2
L 2
R 11
L 1
D 4
L 5
U 3
R 9
U 4
D 10
U 3
R 10
L 4
R 7
D 9
U 11
D 10
R 5
U 6
L 3
R 5
D 1
R 3
L 10
D 4
U 8
R 9
U 5
R 6
U 3
D 2
R 6
U 3
L 3
R 8
L 9
D 6
U 7
D 11
U 12
R 7
D 7
U 12
L 6
U 6
D 3
L 11
R 8
U 10
L 7
R 2
U 8
L 3
R 12
D 4
L 4
U 10
L 9
R 8
L 12
D 3
R 4
L 9
U 4
L 6
D 11
U 3
R 7
U 3
D 3
U 4
L 12
R 11
U 5
D 3
R 7
U 1
D 11
R 7
L 3
R 6
U 10
L 11
U 2
L 11
U 11
R 8
D 12
U 4
L 1
D 3
R 6
L 2
U 4
D 3
R 8
L 2
D 9
L 9
U 8
R 12
D 7
U 13
R 7
L 10
U 6
L 11
D 6
U 13
R 4
U 8
D 7
U 7
R 5
U 2
R 2
D 2
L 6
D 12
U 2
R 4
U 7
D 7
L 13
R 7
U 12
L 11
U 1
L 1
D 7
U 1
D 4
U 10
D 10
R 4
L 13
R 2
U 7
D 5
R 2
D 5
L 13
R 2
U 3
R 9
U 12
L 9
U 9
R 1
L 9
D 9
R 8
U 8
D 8
U 8
R 5
D 7
R 12
L 11
U 1
D 7
L 8
D 3
R 4
L 1
U 2
R 10
U 6
R 8
U 13
L 3
D 1
R 9
L 5
U 5
L 11
R 1
D 8
U 6
R 13
U 4
L 3
U 6
D 12
R 5
D 7
L 4
D 8
L 13
R 13
U 4
D 12
L 1
U 9
L 8
U 11
R 7
D 2
L 11
U 11
L 13
D 6
R 10
D 9
U 8
R 3
U 10
L 8
U 13
D 10
R 2
D 7
R 11
L 10
D 3
U 1
D 13
L 4
D 14
L 14
U 6
L 10
D 7
L 13
U 7
R 14
D 2
U 1
L 12
R 11
D 7
L 9
D 5
L 6
U 11
D 7
L 10
U 11
L 2
R 8
L 2
U 10
D 3
R 14
D 2
R 1
D 2
U 13
D 2
L 5
D 3
U 11
D 8
R 11
L 5
R 10
U 4
R 3
L 9
U 2
R 3
L 5
U 10
L 6
D 8
R 13
U 10
L 13
U 5
L 9
R 14
U 2
D 8
L 3
R 13
U 3
D 12
R 7
U 13
L 2
U 4
D 2
L 13
U 2
L 8
D 10
U 13
L 4
U 1
D 3
U 1
R 8
L 4
U 10
R 2
U 8
D 9
R 10
D 8
U 12
R 11
L 11
R 14
U 5
R 10
D 1
U 6
D 4
R 5
U 11
D 14
U 6
R 7
D 6
R 13
D 7
R 14
D 15
R 6
D 13
L 7
U 9
L 1
R 12
U 8
L 14
D 4
R 8
L 13
D 3
U 9
D 13
L 5
R 9
U 12
D 8
U 11
L 8
R 13
D 6
R 8
D 13
R 4
D 6
L 4
D 13
U 2
D 3
R 1
L 15
D 11
L 8
D 8
L 7
R 1
D 12
R 7
D 2
U 3
L 9
D 1
R 8
L 2
D 9
L 2
U 2
R 4
L 11
U 6
D 11
L 2
U 7
D 7
U 11
R 9
U 4
R 14
L 9
D 5
R 5
D 4
R 1
D 15
U 5
R 8
U 10
R 1
L 1
U 11
L 11
U 15
R 5
D 5
U 3
L 5
U 5
L 5
D 15
U 7
D 13
R 3
L 9
U 12
L 3
U 13
R 1
U 2
R 4
D 9
L 6
R 8
D 13
L 14
R 9
D 10
L 15
U 14
R 14
U 4
R 13
D 12
L 5
D 5
L 13
U 15
D 13
L 12
U 6
D 10
U 10
L 2
R 9
D 5
U 5
D 16
R 12
D 2
R 15
L 1
D 9
L 14
R 9
L 10
R 6
D 16
L 9
U 4
D 1
U 7
R 12
D 2
R 1
D 5
R 15
L 16
U 14
D 16
L 6
U 11
L 16
R 8
L 2
U 16
R 1
U 8
R 16
D 10
L 2
D 14
U 4
L 12
D 9
R 4
D 13
R 1
U 3
R 7
L 3
U 12
R 15
D 16
R 13
L 1
D 16
U 14
R 5
L 7
R 12
U 3
L 14
R 6
U 11
R 14
L 12
U 11
R 6
L 1
D 1
U 5
D 14
L 10
R 1
U 4
R 11
U 16
D 12
R 7
U 2
R 1
D 15
U 16
D 7
L 2
D 3
R 1
D 6
U 16
D 12
U 14
R 13
U 13
L 14
D 5
U 1
L 8
R 7
L 9
D 11
R 10
D 16
R 16
U 10
R 14
L 1
D 7
U 2
R 7
D 15
R 16
U 8
D 12
U 17
R 12
U 7
R 6
L 7
D 8
R 4
U 4
D 14
U 17
D 11
U 3
R 1
D 15
R 11
D 13
L 13
R 9
L 1
U 3
R 12
L 9
U 3
L 17
D 15
R 6
U 9
R 16
L 11
U 3
L 5
D 9
R 6
U 12
R 2
U 4
L 11
U 2
R 11
D 4
L 16
U 2
R 10
U 16
L 12
D 9
U 6
D 16
L 6
R 9
U 14
D 14
U 4
D 14
R 16
L 9
D 14
R 4
U 9
D 11
R 8
D 9
U 1
D 3
R 15
D 10
R 13
D 6
U 2
R 8
U 7
L 2
R 10
D 7
U 10
R 3
L 9
R 1
D 2
U 6
L 17
U 16
L 6
U 16
L 1
R 11
D 16
R 2
L 4
R 6
L 9
R 2
D 11
U 8
D 3
L 15
D 17
U 5
L 3
D 15
L 3
U 12
R 15
U 9
L 11
D 3
R 3
U 12
R 11
D 13
R 7
U 11
L 15
D 5
L 15
D 13
U 10
R 17
D 7
L 16
R 2
L 9
R 13
L 4
R 6
D 9
L 17
D 12
R 14
U 3
D 2
R 6
U 14
D 15
U 7
L 17
U 14
L 8
U 15
R 13
U 3
R 10
D 11
L 14
U 18
R 13
U 13
R 2
D 3
R 5
U 16
R 16
D 13
U 3
R 14
D 17
U 4
L 18
U 8
R 6
U 12
R 17
L 18
U 17
R 18
D 10
U 17
D 2
R 2
D 9
U 13
R 15
L 13
R 8
D 6
U 4
R 12
U 15
D 8
L 16
D 6
L 15
U 8
L 10
D 18
R 8
U 2
D 17
U 8
R 18
D 6
U 7
L 15
U 16
R 16
D 11
U 7
D 12
R 7
U 5
L 16
D 7
L 14
U 1
L 11
D 1
U 17
R 1
U 18
R 1
U 11
D 18
U 16
R 14
U 12
L 5
D 5
L 7
U 10
R 2
D 4
L 10
R 9
D 2
L 17
R 15
L 6
R 2
D 6
L 9
R 10
L 4
D 2
R 12
D 1
R 16
U 15
D 15
L 10
D 16
L 16
U 18
L 5
R 8
L 16
R 10
D 7
U 2
D 8
U 11
R 1
U 1
L 14
D 11
R 8
U 18
L 4
R 14
L 7
U 6
L 17
U 10
L 4
U 6
L 6
R 8
L 15
D 2
R 5
L 13
D 1
R 6
L 11
U 15
L 16
D 13
R 11
U 4
R 1
L 10
U 16
L 2
R 11
L 5
D 19
R 15
L 5
U 17
R 19
D 2
R 9
U 11
L 19
U 16
D 16
R 5
D 13
U 18
D 3
R 15
U 12
L 1
D 11
U 2
R 13
D 1
R 2
D 7
R 2
U 17
R 8
L 2
U 2
R 12
L 2
R 1
D 5
U 7
L 5
U 10
L 14
R 15
D 19
L 13
U 4
L 8
U 8
L 7
D 5
R 17
U 8'''

# COMMAND ----------

def to_unit(x):
  if x > 0:
    return 1
  if x < 0:
    return -1
  return 0


def count_tail_visits(rope_length, instructions):
  rope = [[0, 0] for _ in range(rope_length)]
  visited = {(0, 0)}
  
  for direction, d in instructions:
    for _ in range(d):
      rope[0][0] += (direction == 'D') - (direction == 'U')
      rope[0][1] += (direction == 'R') - (direction == 'L')
      
      for head, tail in zip(rope[:-1], rope[1:]):
        dr = head[0] - tail[0]
        dc = head[1] - tail[1]
        
        if abs(dr) <= 1 and abs(dc) <= 1:
          pass
        elif dr == 0:
          tail[1] += to_unit(dc)
        elif dc == 0:
          tail[0] += to_unit(dr)
        else:
          tail[0] += to_unit(dr)
          tail[1] += to_unit(dc)

      visited.add(tuple(rope[-1]))

  return len(visited)


instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in inp.splitlines()]

answer = count_tail_visits(2, instructions)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!</p>
# MAGIC <p>The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.</p>
# MAGIC <p>Rather than two knots, you now must simulate a rope consisting of <em>ten</em> knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.</p>
# MAGIC <p>Using the same series of motions as the above example, but with the knots marked <code>H</code>, <code>1</code>, <code>2</code>, ..., <code>9</code>, the motions now occur as follows:</p>
# MAGIC <pre><code>== Initial State ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC H.....  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC == R 4 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC 1H....  (1 covers 2, 3, 4, 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC 21H...  (2 covers 3, 4, 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC 321H..  (3 covers 4, 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC 4321H.  (4 covers 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC == U 4 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ......
# MAGIC ....H.
# MAGIC 4321..  (4 covers 5, 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC ....H.
# MAGIC .4321.
# MAGIC 5.....  (5 covers 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ....H.
# MAGIC ....1.
# MAGIC .432..
# MAGIC 5.....  (5 covers 6, 7, 8, 9, s)
# MAGIC 
# MAGIC ....H.
# MAGIC ....1.
# MAGIC ..432.
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == L 3 ==
# MAGIC 
# MAGIC ...H..
# MAGIC ....1.
# MAGIC ..432.
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ..H1..
# MAGIC ...2..
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC .H1...
# MAGIC ...2..
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == D 1 ==
# MAGIC 
# MAGIC ..1...
# MAGIC .H.2..
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == R 4 ==
# MAGIC 
# MAGIC ..1...
# MAGIC ..H2..
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ..1...
# MAGIC ...H..  (H covers 2)
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ...1H.  (1 covers 2)
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ...21H
# MAGIC ..43..
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == D 1 ==
# MAGIC 
# MAGIC ......
# MAGIC ...21.
# MAGIC ..43.H
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == L 5 ==
# MAGIC 
# MAGIC ......
# MAGIC ...21.
# MAGIC ..43H.
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ...21.
# MAGIC ..4H..  (H covers 3)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ...2..
# MAGIC ..H1..  (H covers 4; 1 covers 3)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ...2..
# MAGIC .H13..  (1 covers 4)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC H123..  (2 covers 4)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC == R 2 ==
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC .H23..  (H covers 1; 2 covers 4)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC 
# MAGIC ......
# MAGIC ......
# MAGIC .1H3..  (H covers 2, 4)
# MAGIC .5....
# MAGIC 6.....  (6 covers 7, 8, 9, s)
# MAGIC </code></pre>
# MAGIC <p>Now, you need to keep track of the positions the new tail, <code>9</code>, visits. In this example, the tail never moves, and so it only visits <code><em>1</em></code> position. However, <em>be careful</em>: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.</p>
# MAGIC <p>Here's a larger example:</p>
# MAGIC <pre><code>R 5
# MAGIC U 8
# MAGIC L 8
# MAGIC D 3
# MAGIC R 17
# MAGIC D 10
# MAGIC L 25
# MAGIC U 20
# MAGIC </code></pre>
# MAGIC <p>These motions occur as follows (individual steps are not shown):</p>
# MAGIC <pre><code>== Initial State ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == R 5 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........54321H.........  (5 covers 6, 7, 8, 9, s)
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == U 8 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ................H.........
# MAGIC ................1.........
# MAGIC ................2.........
# MAGIC ................3.........
# MAGIC ...............54.........
# MAGIC ..............6...........
# MAGIC .............7............
# MAGIC ............8.............
# MAGIC ...........9..............  (9 covers s)
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == L 8 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ........H1234.............
# MAGIC ............5.............
# MAGIC ............6.............
# MAGIC ............7.............
# MAGIC ............8.............
# MAGIC ............9.............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s..............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == D 3 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC .........2345.............
# MAGIC ........1...6.............
# MAGIC ........H...7.............
# MAGIC ............8.............
# MAGIC ............9.............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s..............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == R 17 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ................987654321H
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s..............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC == D 10 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s.........98765
# MAGIC .........................4
# MAGIC .........................3
# MAGIC .........................2
# MAGIC .........................1
# MAGIC .........................H
# MAGIC 
# MAGIC == L 25 ==
# MAGIC 
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s..............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC H123456789................
# MAGIC 
# MAGIC == U 20 ==
# MAGIC 
# MAGIC H.........................
# MAGIC 1.........................
# MAGIC 2.........................
# MAGIC 3.........................
# MAGIC 4.........................
# MAGIC 5.........................
# MAGIC 6.........................
# MAGIC 7.........................
# MAGIC 8.........................
# MAGIC 9.........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ...........s..............
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC 
# MAGIC </code></pre>
# MAGIC <p>Now, the tail (<code>9</code>) visits <code><em>36</em></code> positions (including <code>s</code>) at least once:</p>
# MAGIC <pre><code>..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC ..........................
# MAGIC #.........................
# MAGIC #.............###.........
# MAGIC #............#...#........
# MAGIC .#..........#.....#.......
# MAGIC ..#..........#.....#......
# MAGIC ...#........#.......#.....
# MAGIC ....#......s.........#....
# MAGIC .....#..............#.....
# MAGIC ......#............#......
# MAGIC .......#..........#.......
# MAGIC ........#........#........
# MAGIC .........########.........
# MAGIC </code></pre>
# MAGIC <p>Simulate your complete series of motions on a larger rope with ten knots. <em>How many positions does the tail of the rope visit at least once?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = count_tail_visits(10, instructions)
print(answer)
