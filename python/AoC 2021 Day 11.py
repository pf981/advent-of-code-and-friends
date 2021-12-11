# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 11: Dumbo Octopus ---</h2><p>You enter a large cavern full of rare bioluminescent <a href="https://www.youtube.com/watch?v=eih-VSaS2g0" target="_blank">dumbo octopuses</a>! They seem to not like the Christmas lights on your submarine, so you turn them off for now.</p>
# MAGIC <p>There are 100 <span title="I know it's weird; I grew saying 'octopi' too.">octopuses</span> arranged neatly in a 10 by 10 grid. Each octopus slowly gains <em>energy</em> over time and <em>flashes</em> brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.</p>
# MAGIC <p>Each octopus has an <em>energy level</em> - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:</p>
# MAGIC <pre><code>5483143223
# MAGIC 2745854711
# MAGIC 5264556173
# MAGIC 6141336146
# MAGIC 6357385478
# MAGIC 4167524645
# MAGIC 2176841721
# MAGIC 6882881134
# MAGIC 4846848554
# MAGIC 5283751526
# MAGIC </code></pre>
# MAGIC <p>The energy level of each octopus is a value between <code>0</code> and <code>9</code>. Here, the top-left octopus has an energy level of <code>5</code>, the bottom-right one has an energy level of <code>6</code>, and so on.</p>
# MAGIC <p>You can model the energy levels and flashes of light in <em>steps</em>. During a single step, the following occurs:</p>
# MAGIC <ul>
# MAGIC <li>First, the energy level of each octopus increases by <code>1</code>.</li>
# MAGIC <li>Then, any octopus with an energy level greater than <code>9</code> <em>flashes</em>. This increases the energy level of all adjacent octopuses by <code>1</code>, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than <code>9</code>, it <em>also flashes</em>. This process continues as long as new octopuses keep having their energy level increased beyond <code>9</code>. (An octopus can only flash <em>at most once per step</em>.)</li>
# MAGIC <li>Finally, any octopus that flashed during this step has its energy level set to <code>0</code>, as it used all of its energy to flash.</li>
# MAGIC </ul>
# MAGIC <p>Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy. Consider the middle octopus with <code>1</code> energy in this situation:</p>
# MAGIC <pre><code>Before any steps:
# MAGIC 11111
# MAGIC 19991
# MAGIC 19191
# MAGIC 19991
# MAGIC 11111
# MAGIC 
# MAGIC After step 1:
# MAGIC 34543
# MAGIC 4<em>000</em>4
# MAGIC 5<em>000</em>5
# MAGIC 4<em>000</em>4
# MAGIC 34543
# MAGIC 
# MAGIC After step 2:
# MAGIC 45654
# MAGIC 51115
# MAGIC 61116
# MAGIC 51115
# MAGIC 45654
# MAGIC </code></pre>
# MAGIC <p>An octopus is <em>highlighted</em> when it flashed during the given step.</p>
# MAGIC <p>Here is how the larger example above progresses:</p>
# MAGIC <pre><code>Before any steps:
# MAGIC 5483143223
# MAGIC 2745854711
# MAGIC 5264556173
# MAGIC 6141336146
# MAGIC 6357385478
# MAGIC 4167524645
# MAGIC 2176841721
# MAGIC 6882881134
# MAGIC 4846848554
# MAGIC 5283751526
# MAGIC 
# MAGIC After step 1:
# MAGIC 6594254334
# MAGIC 3856965822
# MAGIC 6375667284
# MAGIC 7252447257
# MAGIC 7468496589
# MAGIC 5278635756
# MAGIC 3287952832
# MAGIC 7993992245
# MAGIC 5957959665
# MAGIC 6394862637
# MAGIC 
# MAGIC After step 2:
# MAGIC 88<em>0</em>7476555
# MAGIC 5<em>0</em>89<em>0</em>87<em>0</em>54
# MAGIC 85978896<em>0</em>8
# MAGIC 84857696<em>00</em>
# MAGIC 87<em>00</em>9<em>0</em>88<em>00</em>
# MAGIC 66<em>000</em>88989
# MAGIC 68<em>0000</em>5943
# MAGIC <em>000000</em>7456
# MAGIC 9<em>000000</em>876
# MAGIC 87<em>0000</em>6848
# MAGIC 
# MAGIC After step 3:
# MAGIC <em>00</em>5<em>0</em>9<em>00</em>866
# MAGIC 85<em>00</em>8<em>00</em>575
# MAGIC 99<em>000000</em>39
# MAGIC 97<em>000000</em>41
# MAGIC 9935<em>0</em>8<em>00</em>63
# MAGIC 77123<em>00000</em>
# MAGIC 791125<em>000</em>9
# MAGIC 221113<em>0000</em>
# MAGIC <em>0</em>421125<em>000</em>
# MAGIC <em>00</em>21119<em>000</em>
# MAGIC 
# MAGIC After step 4:
# MAGIC 2263<em>0</em>31977
# MAGIC <em>0</em>923<em>0</em>31697
# MAGIC <em>00</em>3222115<em>0</em>
# MAGIC <em>00</em>41111163
# MAGIC <em>00</em>76191174
# MAGIC <em>00</em>53411122
# MAGIC <em>00</em>4236112<em>0</em>
# MAGIC 5532241122
# MAGIC 1532247211
# MAGIC 113223<em>0</em>211
# MAGIC 
# MAGIC After step 5:
# MAGIC 4484144<em>000</em>
# MAGIC 2<em>0</em>44144<em>000</em>
# MAGIC 2253333493
# MAGIC 1152333274
# MAGIC 11873<em>0</em>3285
# MAGIC 1164633233
# MAGIC 1153472231
# MAGIC 6643352233
# MAGIC 2643358322
# MAGIC 2243341322
# MAGIC 
# MAGIC After step 6:
# MAGIC 5595255111
# MAGIC 3155255222
# MAGIC 33644446<em>0</em>5
# MAGIC 2263444496
# MAGIC 2298414396
# MAGIC 2275744344
# MAGIC 2264583342
# MAGIC 7754463344
# MAGIC 3754469433
# MAGIC 3354452433
# MAGIC 
# MAGIC After step 7:
# MAGIC 67<em>0</em>7366222
# MAGIC 4377366333
# MAGIC 4475555827
# MAGIC 34966557<em>0</em>9
# MAGIC 35<em>00</em>6256<em>0</em>9
# MAGIC 35<em>0</em>9955566
# MAGIC 3486694453
# MAGIC 8865585555
# MAGIC 486558<em>0</em>644
# MAGIC 4465574644
# MAGIC 
# MAGIC After step 8:
# MAGIC 7818477333
# MAGIC 5488477444
# MAGIC 5697666949
# MAGIC 46<em>0</em>876683<em>0</em>
# MAGIC 473494673<em>0</em>
# MAGIC 474<em>00</em>97688
# MAGIC 69<em>0000</em>7564
# MAGIC <em>000000</em>9666
# MAGIC 8<em>00000</em>4755
# MAGIC 68<em>0000</em>7755
# MAGIC 
# MAGIC After step 9:
# MAGIC 9<em>0</em>6<em>0000</em>644
# MAGIC 78<em>00000</em>976
# MAGIC 69<em>000000</em>8<em>0</em>
# MAGIC 584<em>00000</em>82
# MAGIC 5858<em>0000</em>93
# MAGIC 69624<em>00000</em>
# MAGIC 8<em>0</em>2125<em>000</em>9
# MAGIC 222113<em>000</em>9
# MAGIC 9111128<em>0</em>97
# MAGIC 7911119976
# MAGIC 
# MAGIC After step 10:
# MAGIC <em>0</em>481112976
# MAGIC <em>00</em>31112<em>00</em>9
# MAGIC <em>00</em>411125<em>0</em>4
# MAGIC <em>00</em>811114<em>0</em>6
# MAGIC <em>00</em>991113<em>0</em>6
# MAGIC <em>00</em>93511233
# MAGIC <em>0</em>44236113<em>0</em>
# MAGIC 553225235<em>0</em>
# MAGIC <em>0</em>53225<em>0</em>6<em>00</em>
# MAGIC <em>00</em>3224<em>0000</em>
# MAGIC </code></pre>
# MAGIC 
# MAGIC <p>After step 10, there have been a total of <code>204</code> flashes. Fast forwarding, here is the same configuration every 10 steps:</p>
# MAGIC 
# MAGIC <pre><code>After step 20:
# MAGIC 3936556452
# MAGIC 56865568<em>0</em>6
# MAGIC 449655569<em>0</em>
# MAGIC 444865558<em>0</em>
# MAGIC 445686557<em>0</em>
# MAGIC 568<em>00</em>86577
# MAGIC 7<em>00000</em>9896
# MAGIC <em>0000000</em>344
# MAGIC 6<em>000000</em>364
# MAGIC 46<em>0000</em>9543
# MAGIC 
# MAGIC After step 30:
# MAGIC <em>0</em>643334118
# MAGIC 4253334611
# MAGIC 3374333458
# MAGIC 2225333337
# MAGIC 2229333338
# MAGIC 2276733333
# MAGIC 2754574565
# MAGIC 5544458511
# MAGIC 9444447111
# MAGIC 7944446119
# MAGIC 
# MAGIC After step 40:
# MAGIC 6211111981
# MAGIC <em>0</em>421111119
# MAGIC <em>00</em>42111115
# MAGIC <em>000</em>3111115
# MAGIC <em>000</em>3111116
# MAGIC <em>00</em>65611111
# MAGIC <em>0</em>532351111
# MAGIC 3322234597
# MAGIC 2222222976
# MAGIC 2222222762
# MAGIC 
# MAGIC After step 50:
# MAGIC 9655556447
# MAGIC 48655568<em>0</em>5
# MAGIC 448655569<em>0</em>
# MAGIC 445865558<em>0</em>
# MAGIC 457486557<em>0</em>
# MAGIC 57<em>000</em>86566
# MAGIC 6<em>00000</em>9887
# MAGIC 8<em>000000</em>533
# MAGIC 68<em>00000</em>633
# MAGIC 568<em>0000</em>538
# MAGIC 
# MAGIC After step 60:
# MAGIC 25333342<em>00</em>
# MAGIC 274333464<em>0</em>
# MAGIC 2264333458
# MAGIC 2225333337
# MAGIC 2225333338
# MAGIC 2287833333
# MAGIC 3854573455
# MAGIC 1854458611
# MAGIC 1175447111
# MAGIC 1115446111
# MAGIC 
# MAGIC After step 70:
# MAGIC 8211111164
# MAGIC <em>0</em>421111166
# MAGIC <em>00</em>42111114
# MAGIC <em>000</em>4211115
# MAGIC <em>0000</em>211116
# MAGIC <em>00</em>65611111
# MAGIC <em>0</em>532351111
# MAGIC 7322235117
# MAGIC 5722223475
# MAGIC 4572222754
# MAGIC 
# MAGIC After step 80:
# MAGIC 1755555697
# MAGIC 59655556<em>0</em>9
# MAGIC 448655568<em>0</em>
# MAGIC 445865558<em>0</em>
# MAGIC 457<em>0</em>86557<em>0</em>
# MAGIC 57<em>000</em>86566
# MAGIC 7<em>00000</em>8666
# MAGIC <em>0000000</em>99<em>0</em>
# MAGIC <em>0000000</em>8<em>00</em>
# MAGIC <em>0000000000</em>
# MAGIC 
# MAGIC After step 90:
# MAGIC 7433333522
# MAGIC 2643333522
# MAGIC 2264333458
# MAGIC 2226433337
# MAGIC 2222433338
# MAGIC 2287833333
# MAGIC 2854573333
# MAGIC 4854458333
# MAGIC 3387779333
# MAGIC 3333333333
# MAGIC 
# MAGIC After step 100:
# MAGIC <em>0</em>397666866
# MAGIC <em>0</em>749766918
# MAGIC <em>00</em>53976933
# MAGIC <em>000</em>4297822
# MAGIC <em>000</em>4229892
# MAGIC <em>00</em>53222877
# MAGIC <em>0</em>532222966
# MAGIC 9322228966
# MAGIC 7922286866
# MAGIC 6789998766
# MAGIC </code></pre>
# MAGIC <p>After 100 steps, there have been a total of <code><em>1656</em></code> flashes.</p>
# MAGIC <p>Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. <em>How many total flashes are there after 100 steps?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''8826876714
3127787238
8182852861
4655371483
3864551365
1878253581
8317422437
1517254266
2621124761
3473331514'''

# COMMAND ----------

def step(octopuses):
  for pos in octopuses:
    octopuses[pos] += 1

  flashed = set()
  for _ in range(100):
    for (row, col), energy in octopuses.items():
      if energy > 9 and (row, col) not in flashed:
        flashed.add((row, col))
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
          if (row + dr, col + dc) in octopuses:
            octopuses[(row + dr, col + dc)] += 1

  for (row, col) in flashed:
    octopuses[(row, col)] = 0

  return len(flashed)

def count_flashes(octopuses, n_steps):
  octopuses = octopuses.copy()
  return sum(step(octopuses) for _ in range(n_steps))

octopuses = {(row, col): int(energy) for row, line in enumerate(inp.splitlines()) for col, energy in enumerate(line)}
  
answer = count_flashes(octopuses, 100)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It seems like the individual flashes aren't bright enough to navigate. However, you might have a better option: the flashes seem to be <em>synchronizing</em>!</p>
# MAGIC <p>In the example above, the first time all octopuses flash simultaneously is step <code><em>195</em></code>:</p>
# MAGIC <pre><code>After step 193:
# MAGIC 5877777777
# MAGIC 8877777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 7777777777
# MAGIC 
# MAGIC After step 194:
# MAGIC 6988888888
# MAGIC 9988888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 8888888888
# MAGIC 
# MAGIC After step 195:
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC <em>0000000000</em>
# MAGIC </code></pre>
# MAGIC <p>If you can calculate the exact moments when the octopuses will all flash simultaneously, you should be able to navigate through the cavern. <em>What is the first step during which all octopuses flash?</em></p>
# MAGIC </article>

# COMMAND ----------

import itertools

def find_all_flash_step(octopuses):
  octopuses = octopuses.copy()
  return next(i + 1 for i in itertools.count() if step(octopuses) == 100)

answer = find_all_flash_step(octopuses)
print(answer)
