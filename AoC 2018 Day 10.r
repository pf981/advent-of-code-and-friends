# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 10: The Stars Align ---</h2><p>It's no use; your navigation system simply isn't capable of providing <span title="At the iceberg, use any lane to turn left. Then, swim for eight thousand miles.">walking directions</span> in the arctic circle, and certainly not in 1018.</p>
# MAGIC <p>The Elves suggest an alternative. In times like these, North Pole rescue operations will arrange points of light in the sky to guide missing Elves back to base. Unfortunately, the message is easy to miss: the points move slowly enough that it takes hours to align them, but have so much momentum that they only stay aligned for a second. If you blink at the wrong time, it might be hours before another message appears.</p>
# MAGIC <p>You can see these points of light floating in the distance, and record their position in the sky and their velocity, the relative change in position per second (your puzzle input). The coordinates are all given from your perspective; given enough time, those positions and velocities will move the points into a cohesive message!</p>
# MAGIC <p>Rather than wait, you decide to fast-forward the process and calculate what the points will eventually spell.</p>
# MAGIC <p>For example, suppose you note the following points:</p>
# MAGIC <pre><code>position=&lt; 9,  1&gt; velocity=&lt; 0,  2&gt;
# MAGIC position=&lt; 7,  0&gt; velocity=&lt;-1,  0&gt;
# MAGIC position=&lt; 3, -2&gt; velocity=&lt;-1,  1&gt;
# MAGIC position=&lt; 6, 10&gt; velocity=&lt;-2, -1&gt;
# MAGIC position=&lt; 2, -4&gt; velocity=&lt; 2,  2&gt;
# MAGIC position=&lt;-6, 10&gt; velocity=&lt; 2, -2&gt;
# MAGIC position=&lt; 1,  8&gt; velocity=&lt; 1, -1&gt;
# MAGIC position=&lt; 1,  7&gt; velocity=&lt; 1,  0&gt;
# MAGIC position=&lt;-3, 11&gt; velocity=&lt; 1, -2&gt;
# MAGIC position=&lt; 7,  6&gt; velocity=&lt;-1, -1&gt;
# MAGIC position=&lt;-2,  3&gt; velocity=&lt; 1,  0&gt;
# MAGIC position=&lt;-4,  3&gt; velocity=&lt; 2,  0&gt;
# MAGIC position=&lt;10, -3&gt; velocity=&lt;-1,  1&gt;
# MAGIC position=&lt; 5, 11&gt; velocity=&lt; 1, -2&gt;
# MAGIC position=&lt; 4,  7&gt; velocity=&lt; 0, -1&gt;
# MAGIC position=&lt; 8, -2&gt; velocity=&lt; 0,  1&gt;
# MAGIC position=&lt;15,  0&gt; velocity=&lt;-2,  0&gt;
# MAGIC position=&lt; 1,  6&gt; velocity=&lt; 1,  0&gt;
# MAGIC position=&lt; 8,  9&gt; velocity=&lt; 0, -1&gt;
# MAGIC position=&lt; 3,  3&gt; velocity=&lt;-1,  1&gt;
# MAGIC position=&lt; 0,  5&gt; velocity=&lt; 0, -1&gt;
# MAGIC position=&lt;-2,  2&gt; velocity=&lt; 2,  0&gt;
# MAGIC position=&lt; 5, -2&gt; velocity=&lt; 1,  2&gt;
# MAGIC position=&lt; 1,  4&gt; velocity=&lt; 2,  1&gt;
# MAGIC position=&lt;-2,  7&gt; velocity=&lt; 2, -2&gt;
# MAGIC position=&lt; 3,  6&gt; velocity=&lt;-1, -1&gt;
# MAGIC position=&lt; 5,  0&gt; velocity=&lt; 1,  0&gt;
# MAGIC position=&lt;-6,  0&gt; velocity=&lt; 2,  0&gt;
# MAGIC position=&lt; 5,  9&gt; velocity=&lt; 1, -2&gt;
# MAGIC position=&lt;14,  7&gt; velocity=&lt;-2,  0&gt;
# MAGIC position=&lt;-3,  6&gt; velocity=&lt; 2, -1&gt;
# MAGIC </code></pre>
# MAGIC <p>Each line represents one point. Positions are given as <code>&lt;X, Y&gt;</code> pairs: X represents how far left (negative) or right (positive) the point appears, while Y represents how far up (negative) or down (positive) the point appears.</p>
# MAGIC <p>At <code>0</code> seconds, each point has the position given. Each second, each point's velocity is added to its position. So, a point with velocity <code>&lt;1, -2&gt;</code> is moving to the right, but is moving upward twice as quickly. If this point's initial position were <code>&lt;3, 9&gt;</code>, after <code>3</code> seconds, its position would become <code>&lt;6, 3&gt;</code>.</p>
# MAGIC <p>Over time, the points listed above would move like this:</p>
# MAGIC <pre><code>Initially:
# MAGIC ........#.............
# MAGIC ................#.....
# MAGIC .........#.#..#.......
# MAGIC ......................
# MAGIC #..........#.#.......#
# MAGIC ...............#......
# MAGIC ....#.................
# MAGIC ..#.#....#............
# MAGIC .......#..............
# MAGIC ......#...............
# MAGIC ...#...#.#...#........
# MAGIC ....#..#..#.........#.
# MAGIC .......#..............
# MAGIC ...........#..#.......
# MAGIC #...........#.........
# MAGIC ...#.......#..........
# MAGIC 
# MAGIC After 1 second:
# MAGIC ......................
# MAGIC ......................
# MAGIC ..........#....#......
# MAGIC ........#.....#.......
# MAGIC ..#.........#......#..
# MAGIC ......................
# MAGIC ......#...............
# MAGIC ....##.........#......
# MAGIC ......#.#.............
# MAGIC .....##.##..#.........
# MAGIC ........#.#...........
# MAGIC ........#...#.....#...
# MAGIC ..#...........#.......
# MAGIC ....#.....#.#.........
# MAGIC ......................
# MAGIC ......................
# MAGIC 
# MAGIC After 2 seconds:
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC ..............#.......
# MAGIC ....#..#...####..#....
# MAGIC ......................
# MAGIC ........#....#........
# MAGIC ......#.#.............
# MAGIC .......#...#..........
# MAGIC .......#..#..#.#......
# MAGIC ....#....#.#..........
# MAGIC .....#...#...##.#.....
# MAGIC ........#.............
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC 
# MAGIC After 3 seconds:
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC ......#...#..###......
# MAGIC ......#...#...#.......
# MAGIC ......#...#...#.......
# MAGIC ......#####...#.......
# MAGIC ......#...#...#.......
# MAGIC ......#...#...#.......
# MAGIC ......#...#...#.......
# MAGIC ......#...#..###......
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC 
# MAGIC After 4 seconds:
# MAGIC ......................
# MAGIC ......................
# MAGIC ......................
# MAGIC ............#.........
# MAGIC ........##...#.#......
# MAGIC ......#.....#..#......
# MAGIC .....#..##.##.#.......
# MAGIC .......##.#....#......
# MAGIC ...........#....#.....
# MAGIC ..............#.......
# MAGIC ....#......#...#......
# MAGIC .....#.....##.........
# MAGIC ...............#......
# MAGIC ...............#......
# MAGIC ......................
# MAGIC ......................
# MAGIC </code></pre>
# MAGIC <p>After 3 seconds, the message appeared briefly: <code><em>HI</em></code>. Of course, your message will be much longer and will take many more seconds to appear.</p>
# MAGIC <p><em>What message will eventually appear in the sky?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "position=< 21188,  31669> velocity=<-2, -3>
position=<-10416, -31455> velocity=< 1,  3>
position=< 21144, -31450> velocity=<-2,  3>
position=< 42218,  21146> velocity=<-4, -2>
position=< 42223,  10633> velocity=<-4, -1>
position=<-52484,  42188> velocity=< 5, -4>
position=< 52759,  21154> velocity=<-5, -2>
position=<-41981,  21153> velocity=< 4, -2>
position=<-10386, -31452> velocity=< 1,  3>
position=< 10651, -10414> velocity=<-1,  1>
position=< 42234,  42197> velocity=<-4, -4>
position=<-52447,  42193> velocity=< 5, -4>
position=< 52763, -10408> velocity=<-5,  1>
position=< 31673,  21150> velocity=<-3, -2>
position=< 10660, -52501> velocity=<-1,  5>
position=<-31433, -31453> velocity=< 3,  3>
position=< 52750, -20933> velocity=<-5,  2>
position=< 42202, -31456> velocity=<-4,  3>
position=<-52442, -41971> velocity=< 5,  4>
position=<-52459,  52711> velocity=< 5, -5>
position=<-20916, -41972> velocity=< 2,  4>
position=< 10656,  42191> velocity=<-1, -4>
position=<-41966,  21153> velocity=< 4, -2>
position=<-20912,  21153> velocity=< 2, -2>
position=< 21172, -10415> velocity=<-2,  1>
position=<-41966, -20937> velocity=< 4,  2>
position=<-20898, -31455> velocity=< 2,  3>
position=<-20882, -52492> velocity=< 2,  5>
position=< 21163,  31671> velocity=<-2, -3>
position=<-20924,  21148> velocity=< 2, -2>
position=<-41926, -41975> velocity=< 4,  4>
position=<-31459, -52497> velocity=< 3,  5>
position=<-10384, -10413> velocity=< 1,  1>
position=<-52485, -41980> velocity=< 5,  4>
position=<-41937,  10626> velocity=< 4, -1>
position=< 21170,  42192> velocity=<-2, -4>
position=< 21170,  52713> velocity=<-2, -5>
position=<-31405,  52715> velocity=< 3, -5>
position=<-41934,  52718> velocity=< 4, -5>
position=<-31445, -10415> velocity=< 3,  1>
position=<-41937, -20938> velocity=< 4,  2>
position=< 31681, -52496> velocity=<-3,  5>
position=< 21177, -52494> velocity=<-2,  5>
position=< 52741, -20934> velocity=<-5,  2>
position=< 21184,  21146> velocity=<-2, -2>
position=<-20887,  10634> velocity=< 2, -1>
position=<-52502,  42191> velocity=< 5, -4>
position=< 42244,  21155> velocity=<-4, -2>
position=< 42191,  10625> velocity=<-4, -1>
position=<-52495,  52716> velocity=< 5, -5>
position=<-31413,  10625> velocity=< 3, -1>
position=<-10418, -31452> velocity=< 1,  3>
position=<-10378,  52715> velocity=< 1, -5>
position=< 52747, -31451> velocity=<-5,  3>
position=< 21178,  31672> velocity=<-2, -3>
position=<-20888,  31675> velocity=< 2, -3>
position=< 10657,  52714> velocity=<-1, -5>
position=< 21152,  10630> velocity=<-2, -1>
position=< 10676,  52718> velocity=<-1, -5>
position=< 31722, -10408> velocity=<-3,  1>
position=<-41974, -41979> velocity=< 4,  4>
position=<-31416, -10409> velocity=< 3,  1>
position=< 52715, -20930> velocity=<-5,  2>
position=< 52755, -20931> velocity=<-5,  2>
position=< 31669,  31674> velocity=<-3, -3>
position=< 52750, -10413> velocity=<-5,  1>
position=<-10383,  10628> velocity=< 1, -1>
position=< 31713,  21146> velocity=<-3, -2>
position=< 52763, -52499> velocity=<-5,  5>
position=< 42210, -52501> velocity=<-4,  5>
position=< 10656, -31453> velocity=<-1,  3>
position=< 31666,  21152> velocity=<-3, -2>
position=<-20896, -31453> velocity=< 2,  3>
position=< 21145, -10415> velocity=<-2,  1>
position=<-52461,  21151> velocity=< 5, -2>
position=<-10363, -41972> velocity=< 1,  4>
position=<-20890,  10628> velocity=< 2, -1>
position=<-41973, -41976> velocity=< 4,  4>
position=< 21186, -20934> velocity=<-2,  2>
position=<-52447,  42192> velocity=< 5, -4>
position=<-52458, -20937> velocity=< 5,  2>
position=<-20891,  52714> velocity=< 2, -5>
position=< 21173, -52501> velocity=<-2,  5>
position=< 52747, -31459> velocity=<-5,  3>
position=< 42230, -20931> velocity=<-4,  2>
position=< 52708, -52498> velocity=<-5,  5>
position=< 52755,  21146> velocity=<-5, -2>
position=< 21173,  31675> velocity=<-2, -3>
position=<-20904,  52715> velocity=< 2, -5>
position=< 52742, -20933> velocity=<-5,  2>
position=< 10659, -41973> velocity=<-1,  4>
position=< 52707, -10416> velocity=<-5,  1>
position=<-41974, -10414> velocity=< 4,  1>
position=<-10379, -52493> velocity=< 1,  5>
position=<-41981,  10628> velocity=< 4, -1>
position=<-10403, -41976> velocity=< 1,  4>
position=<-52466,  31676> velocity=< 5, -3>
position=< 52755, -20932> velocity=<-5,  2>
position=<-31425, -20932> velocity=< 3,  2>
position=<-10375, -41973> velocity=< 1,  4>
position=< 42210, -41971> velocity=<-4,  4>
position=< 21188, -20936> velocity=<-2,  2>
position=<-10371, -10415> velocity=< 1,  1>
position=<-31458, -10412> velocity=< 3,  1>
position=<-52454, -10413> velocity=< 5,  1>
position=<-31452, -20938> velocity=< 3,  2>
position=< 21152,  52710> velocity=<-2, -5>
position=<-31453, -10411> velocity=< 3,  1>
position=< 10631,  31667> velocity=<-1, -3>
position=< 31667,  31671> velocity=<-3, -3>
position=<-31453, -20938> velocity=< 3,  2>
position=<-41963,  42188> velocity=< 4, -4>
position=< 42238,  42189> velocity=<-4, -4>
position=< 31681, -41980> velocity=<-3,  4>
position=<-41974, -52498> velocity=< 4,  5>
position=<-31445,  52717> velocity=< 3, -5>
position=<-52453,  10628> velocity=< 5, -1>
position=<-10384,  52713> velocity=< 1, -5>
position=<-10394,  31670> velocity=< 1, -3>
position=< 42235,  42193> velocity=<-4, -4>
position=< 42236,  31670> velocity=<-4, -3>
position=<-41982,  21154> velocity=< 4, -2>
position=< 42234,  21151> velocity=<-4, -2>
position=< 52743, -31457> velocity=<-5,  3>
position=<-20908, -52500> velocity=< 2,  5>
position=< 10633, -10417> velocity=<-1,  1>
position=< 10624,  10627> velocity=<-1, -1>
position=< 31683, -31459> velocity=<-3,  3>
position=<-31453,  10627> velocity=< 3, -1>
position=< 10682, -52492> velocity=<-1,  5>
position=<-10408, -10413> velocity=< 1,  1>
position=<-41946, -41977> velocity=< 4,  4>
position=< 31706, -31452> velocity=<-3,  3>
position=<-52487,  10634> velocity=< 5, -1>
position=<-10371, -20932> velocity=< 1,  2>
position=< 42222,  31673> velocity=<-4, -3>
position=<-10402, -31459> velocity=< 1,  3>
position=< 10633, -20934> velocity=<-1,  2>
position=<-10377, -41975> velocity=< 1,  4>
position=<-52454,  42192> velocity=< 5, -4>
position=< 42214, -41973> velocity=<-4,  4>
position=<-52447,  21148> velocity=< 5, -2>
position=<-31451, -20934> velocity=< 3,  2>
position=< 42231, -52493> velocity=<-4,  5>
position=<-10368, -10415> velocity=< 1,  1>
position=< 10656, -31453> velocity=<-1,  3>
position=< 10635,  10625> velocity=<-1, -1>
position=<-10387, -52501> velocity=< 1,  5>
position=< 42234, -41976> velocity=<-4,  4>
position=<-52466,  10633> velocity=< 5, -1>
position=< 52760,  31667> velocity=<-5, -3>
position=<-10410,  31667> velocity=< 1, -3>
position=<-52469,  21150> velocity=< 5, -2>
position=<-52501, -10412> velocity=< 5,  1>
position=< 21152, -31450> velocity=<-2,  3>
position=<-20938, -10412> velocity=< 2,  1>
position=<-31420,  10627> velocity=< 3, -1>
position=<-31416, -41980> velocity=< 3,  4>
position=< 10671, -10409> velocity=<-1,  1>
position=< 31666, -10411> velocity=<-3,  1>
position=<-31435, -31454> velocity=< 3,  3>
position=< 42218,  10626> velocity=<-4, -1>
position=< 10627, -10415> velocity=<-1,  1>
position=< 31701,  21149> velocity=<-3, -2>
position=< 21149,  31676> velocity=<-2, -3>
position=<-31437,  52709> velocity=< 3, -5>
position=< 42242, -31452> velocity=<-4,  3>
position=<-41956,  10630> velocity=< 4, -1>
position=<-20907,  31669> velocity=< 2, -3>
position=<-20936, -20932> velocity=< 2,  2>
position=<-31441, -41976> velocity=< 3,  4>
position=<-20892, -41976> velocity=< 2,  4>
position=< 42215,  42196> velocity=<-4, -4>
position=<-31432, -52500> velocity=< 3,  5>
position=<-52476, -20934> velocity=< 5,  2>
position=< 21169,  52715> velocity=<-2, -5>
position=<-31445,  10632> velocity=< 3, -1>
position=< 21189,  52709> velocity=<-2, -5>
position=< 42214, -52499> velocity=<-4,  5>
position=<-20895, -41971> velocity=< 2,  4>
position=< 21170,  21151> velocity=<-2, -2>
position=<-52490,  52711> velocity=< 5, -5>
position=<-41966,  10626> velocity=< 4, -1>
position=< 52727,  42188> velocity=<-5, -4>
position=< 10657,  31672> velocity=<-1, -3>
position=< 21162,  21150> velocity=<-2, -2>
position=< 52744,  10626> velocity=<-5, -1>
position=<-31436,  42195> velocity=< 3, -4>
position=<-31457,  31674> velocity=< 3, -3>
position=< 10631, -41973> velocity=<-1,  4>
position=< 21147,  42193> velocity=<-2, -4>
position=< 52707, -52501> velocity=<-5,  5>
position=< 10623, -52492> velocity=<-1,  5>
position=<-41974, -20935> velocity=< 4,  2>
position=<-41934,  10633> velocity=< 4, -1>
position=< 21152, -31450> velocity=<-2,  3>
position=< 21188,  31670> velocity=<-2, -3>
position=<-52455,  52711> velocity=< 5, -5>
position=<-20892,  21147> velocity=< 2, -2>
position=<-20924,  31673> velocity=< 2, -3>
position=< 31665,  31668> velocity=<-3, -3>
position=< 52720, -41979> velocity=<-5,  4>
position=<-20905,  21151> velocity=< 2, -2>
position=< 42226,  31667> velocity=<-4, -3>
position=< 42221, -20933> velocity=<-4,  2>
position=< 31717, -20937> velocity=<-3,  2>
position=< 52708,  42194> velocity=<-5, -4>
position=<-52442, -10408> velocity=< 5,  1>
position=<-41942,  31668> velocity=< 4, -3>
position=< 21156,  52709> velocity=<-2, -5>
position=<-20932, -52499> velocity=< 2,  5>
position=<-41977, -10408> velocity=< 4,  1>
position=<-10371,  52713> velocity=< 1, -5>
position=<-20884, -10416> velocity=< 2,  1>
position=<-20915, -31456> velocity=< 2,  3>
position=<-31421, -31450> velocity=< 3,  3>
position=<-31419,  42192> velocity=< 3, -4>
position=<-10367, -31458> velocity=< 1,  3>
position=<-10410, -10417> velocity=< 1,  1>
position=< 31716, -10415> velocity=<-3,  1>
position=<-52479,  52717> velocity=< 5, -5>
position=< 10647,  52718> velocity=<-1, -5>
position=<-52471, -31450> velocity=< 5,  3>
position=< 42210,  52710> velocity=<-4, -5>
position=<-52453,  31673> velocity=< 5, -3>
position=< 42234, -10410> velocity=<-4,  1>
position=<-52459, -10411> velocity=< 5,  1>
position=<-52477, -31455> velocity=< 5,  3>
position=< 52726,  31671> velocity=<-5, -3>
position=< 21155, -10417> velocity=<-2,  1>
position=< 31689, -52492> velocity=<-3,  5>
position=<-41966, -41976> velocity=< 4,  4>
position=<-20921, -31459> velocity=< 2,  3>
position=< 31670,  52710> velocity=<-3, -5>
position=<-10363, -41977> velocity=< 1,  4>
position=<-20935,  10633> velocity=< 2, -1>
position=< 31721,  52709> velocity=<-3, -5>
position=<-10386, -52495> velocity=< 1,  5>
position=<-10359, -10408> velocity=< 1,  1>
position=< 42202,  10625> velocity=<-4, -1>
position=<-52455, -20933> velocity=< 5,  2>
position=< 52711,  31670> velocity=<-5, -3>
position=<-10363, -20933> velocity=< 1,  2>
position=< 21192, -20932> velocity=<-2,  2>
position=< 31702, -31451> velocity=<-3,  3>
position=<-41966, -20933> velocity=< 4,  2>
position=<-10382, -20937> velocity=< 1,  2>
position=< 42227, -52494> velocity=<-4,  5>
position=< 31713,  10627> velocity=<-3, -1>
position=< 42194, -10413> velocity=<-4,  1>
position=< 21146,  42193> velocity=<-2, -4>
position=<-20889, -41973> velocity=< 2,  4>
position=< 42223,  52718> velocity=<-4, -5>
position=< 10671, -31456> velocity=<-1,  3>
position=< 10668, -20929> velocity=<-1,  2>
position=< 21188, -41977> velocity=<-2,  4>
position=<-41965,  10629> velocity=< 4, -1>
position=<-41957,  31669> velocity=< 4, -3>
position=< 52728, -41980> velocity=<-5,  4>
position=<-10407,  21150> velocity=< 1, -2>
position=<-52463,  42197> velocity=< 5, -4>
position=< 31681,  21150> velocity=<-3, -2>
position=< 31681,  21154> velocity=<-3, -2>
position=< 10652,  21155> velocity=<-1, -2>
position=<-41934,  42191> velocity=< 4, -4>
position=< 10658,  21150> velocity=<-1, -2>
position=< 42202,  52711> velocity=<-4, -5>
position=<-41926, -41971> velocity=< 4,  4>
position=< 52752,  31668> velocity=<-5, -3>
position=<-52470, -20936> velocity=< 5,  2>
position=< 10671, -10412> velocity=<-1,  1>
position=<-52503, -31450> velocity=< 5,  3>
position=< 10623, -41979> velocity=<-1,  4>
position=< 21173,  10633> velocity=<-2, -1>
position=< 10656, -20931> velocity=<-1,  2>
position=<-31451,  42188> velocity=< 3, -4>
position=< 42211, -52498> velocity=<-4,  5>
position=<-20899, -20931> velocity=< 2,  2>
position=< 10647,  21146> velocity=<-1, -2>
position=<-41934, -52492> velocity=< 4,  5>
position=<-10386, -41977> velocity=< 1,  4>
position=< 31670, -52492> velocity=<-3,  5>
position=<-41930, -31451> velocity=< 4,  3>
position=<-10363,  52711> velocity=< 1, -5>
position=< 31689, -10416> velocity=<-3,  1>
position=<-52447, -52501> velocity=< 5,  5>
position=<-41931,  52716> velocity=< 4, -5>
position=<-41934,  42189> velocity=< 4, -4>
position=<-20892, -41977> velocity=< 2,  4>
position=< 52725,  52709> velocity=<-5, -5>
position=< 52720, -10414> velocity=<-5,  1>
position=<-41962, -31459> velocity=< 4,  3>
position=<-20937,  31671> velocity=< 2, -3>
position=< 31669, -10414> velocity=<-3,  1>
position=< 52755, -41979> velocity=<-5,  4>
position=<-41926, -52495> velocity=< 4,  5>
position=< 52744,  42189> velocity=<-5, -4>
position=<-10403,  52717> velocity=< 1, -5>
position=< 31681,  42194> velocity=<-3, -4>
position=<-52471,  42197> velocity=< 5, -4>
position=<-10390, -52501> velocity=< 1,  5>
position=< 21185,  21149> velocity=<-2, -2>
position=< 10651, -41978> velocity=<-1,  4>
position=<-20884,  42189> velocity=< 2, -4>
position=< 10676,  21146> velocity=<-1, -2>
position=<-31453, -20930> velocity=< 3,  2>
position=< 42214,  21153> velocity=<-4, -2>
position=< 21152,  31674> velocity=<-2, -3>
position=<-52487, -52496> velocity=< 5,  5>
position=< 52739,  42189> velocity=<-5, -4>
position=< 52717,  42188> velocity=<-5, -4>
position=< 10679,  21146> velocity=<-1, -2>
position=< 31686, -10417> velocity=<-3,  1>
position=<-31405, -10408> velocity=< 3,  1>
position=< 42234,  42195> velocity=<-4, -4>
position=< 31715, -31453> velocity=<-3,  3>
position=<-31453,  42190> velocity=< 3, -4>
position=< 42229,  10630> velocity=<-4, -1>
position=< 42191,  10626> velocity=<-4, -1>
position=<-31432, -20929> velocity=< 3,  2>
position=<-20884,  10626> velocity=< 2, -1>
position=<-52470, -41978> velocity=< 5,  4>
position=< 52766, -41971> velocity=<-5,  4>
position=<-31429,  52717> velocity=< 3, -5>
position=<-41921,  31676> velocity=< 4, -3>
position=<-31424,  21146> velocity=< 3, -2>
position=< 10650, -20933> velocity=<-1,  2>
position=<-31434, -52496> velocity=< 3,  5>
position=< 21194, -41974> velocity=<-2,  4>
position=< 21147,  42192> velocity=<-2, -4>
"

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_extract_all("-?\\d+") %>%
  map(parse_integer) %>%
  map_dfr(set_names, c("x", "y", "dx", "dy"))
df

# COMMAND ----------

df %>%
  mutate(t = list(seq(from = 0, to = 200, by = 1) + 10400)) %>%
  unnest() %>%
  mutate(
    x = x + t * dx,
    y = y + t * dy
  ) %>%
  ggplot(aes(x, y)) +
  geom_point(size = 0.1, alpha = 0.5) +
  scale_y_reverse() +
  theme_void() +
  facet_wrap(~t, scales = "free")

# COMMAND ----------

t <- 10521
df %>%
  mutate(x = x + t * dx, y = y + t * dy) %>%
  ggplot(aes(x, y)) +
    geom_point(size = 4, shape = 15) +
    scale_y_reverse(limits = c(200, 0)) +
    theme_void()

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Good thing you didn't have to wait, because that would have taken a long time - much longer than the <code><em>3</em></code> seconds in the example above.</p>
# MAGIC <p>Impressed by your sub-hour communication capabilities, the Elves are curious: <em>exactly how many seconds would they have needed to wait for that message to appear?</em></p>
# MAGIC </article>

# COMMAND ----------

answer <- t
answer
