# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/20

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 20: Donut Maze ---</h2><p>You notice a strange pattern on the surface of Pluto and land nearby to get a closer look. Upon closer inspection, you realize you've come across one of the famous space-warping mazes of the long-lost Pluto civilization!</p>
# MAGIC <p>Because there isn't much space on Pluto, the civilization that used to live here thrived by inventing a method for folding spacetime.  Although the technology is no longer understood, mazes like this one provide a small glimpse into the <span title="So really, this puzzle is more archaeology than math, right?">daily life of an ancient Pluto citizen</span>.</p>
# MAGIC <p>This maze is shaped like a <a href="https://en.wikipedia.org/wiki/Torus">donut</a>. Portals along the inner and outer edge of the donut can instantly teleport you from one side to the other.  For example:</p>
# MAGIC <pre><code>         A           
# MAGIC          A           
# MAGIC   #######.#########  
# MAGIC   #######.........#  
# MAGIC   #######.#######.#  
# MAGIC   #######.#######.#  
# MAGIC   #######.#######.#  
# MAGIC   #####  B    ###.#  
# MAGIC BC...##  C    ###.#  
# MAGIC   ##.##       ###.#  
# MAGIC   ##...DE  F  ###.#  
# MAGIC   #####    G  ###.#  
# MAGIC   #########.#####.#  
# MAGIC DE..#######...###.#  
# MAGIC   #.#########.###.#  
# MAGIC FG..#########.....#  
# MAGIC   ###########.#####  
# MAGIC              Z       
# MAGIC              Z       
# MAGIC </code></pre>
# MAGIC <p>This map of the maze shows solid walls (<code>#</code>) and open passages (<code>.</code>). Every maze on Pluto has a start (the open tile next to <code>AA</code>) and an end (the open tile next to <code>ZZ</code>). Mazes on Pluto also have portals; this maze has three pairs of portals: <code>BC</code>, <code>DE</code>, and <code>FG</code>. When on an open tile next to one of these labels, a single step can take you to the other tile with the same label. (You can only walk on <code>.</code> tiles; labels and empty space are not traversable.)</p>
# MAGIC <p>One path through the maze doesn't require any portals.  Starting at <code>AA</code>, you could go down 1, right 8, down 12, left 4, and down 1 to reach <code>ZZ</code>, a total of 26 steps.</p>
# MAGIC <p>However, there is a shorter path:  You could walk from <code>AA</code> to the inner <code>BC</code> portal (4 steps), warp to the outer <code>BC</code> portal (1 step), walk to the inner <code>DE</code> (6 steps), warp to the outer <code>DE</code> (1 step), walk to the outer <code>FG</code> (4 steps), warp to the inner <code>FG</code> (1 step), and finally walk to <code>ZZ</code> (6 steps). In total, this is only <em>23</em> steps.</p>
# MAGIC <p>Here is a larger example:</p>
# MAGIC <pre><code>                   A               
# MAGIC                    A               
# MAGIC   #################.#############  
# MAGIC   #.#...#...................#.#.#  
# MAGIC   #.#.#.###.###.###.#########.#.#  
# MAGIC   #.#.#.......#...#.....#.#.#...#  
# MAGIC   #.#########.###.#####.#.#.###.#  
# MAGIC   #.............#.#.....#.......#  
# MAGIC   ###.###########.###.#####.#.#.#  
# MAGIC   #.....#        A   C    #.#.#.#  
# MAGIC   #######        S   P    #####.#  
# MAGIC   #.#...#                 #......VT
# MAGIC   #.#.#.#                 #.#####  
# MAGIC   #...#.#               YN....#.#  
# MAGIC   #.###.#                 #####.#  
# MAGIC DI....#.#                 #.....#  
# MAGIC   #####.#                 #.###.#  
# MAGIC ZZ......#               QG....#..AS
# MAGIC   ###.###                 #######  
# MAGIC JO..#.#.#                 #.....#  
# MAGIC   #.#.#.#                 ###.#.#  
# MAGIC   #...#..DI             BU....#..LF
# MAGIC   #####.#                 #.#####  
# MAGIC YN......#               VT..#....QG
# MAGIC   #.###.#                 #.###.#  
# MAGIC   #.#...#                 #.....#  
# MAGIC   ###.###    J L     J    #.#.###  
# MAGIC   #.....#    O F     P    #.#...#  
# MAGIC   #.###.#####.#.#####.#####.###.#  
# MAGIC   #...#.#.#...#.....#.....#.#...#  
# MAGIC   #.#####.###.###.#.#.#########.#  
# MAGIC   #...#.#.....#...#.#.#.#.....#.#  
# MAGIC   #.###.#####.###.###.#.#.#######  
# MAGIC   #.#.........#...#.............#  
# MAGIC   #########.###.###.#############  
# MAGIC            B   J   C               
# MAGIC            U   P   P               
# MAGIC </code></pre>
# MAGIC <p>Here, <code>AA</code> has no direct path to <code>ZZ</code>, but it does connect to <code>AS</code> and <code>CP</code>. By passing through <code>AS</code>, <code>QG</code>, <code>BU</code>, and <code>JO</code>, you can reach <code>ZZ</code> in <em>58</em> steps.</p>
# MAGIC <p>In your maze, <em>how many steps does it take to get from the open tile marked <code>AA</code> to the open tile marked <code>ZZ</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "                                           C   I         O     M       H             G                                       
                                           T   F         E     C       U             C                                       
  #########################################.###.#########.#####.#######.#############.#####################################  
  #...................#...#.......#.#.#.#.....#.#...#.....#...#...#.....#...#.......#.#.....#.#...#.#.#...#...#.#...#...#.#  
  #.###.#######.###.#####.#.#.#.###.#.#.#####.#.#.#.###.#.#.#.#.###.###.###.###.#.#.#.###.###.#.###.#.#.###.###.###.#.###.#  
  #.#.#.#.#.....#...........#.#.......#.......#...#...#.#.#.#.#.#.#.#.#.#.....#.#.#.#.#...#...#.#.#.....#.#.#...#.........#  
  ###.#.#.###.#####.#.###.#########.###.###.#.#######.#.###.#.#.#.###.#.#.#.###.#.#.#.#.#####.#.#.###.###.#.###.###.#.#.#.#  
  #.....#...#.#.....#.#...#.#...#.....#.#.#.#.#.#...#.#.....#.#.#.#...#...#.#.#.#.#.#...#...#...#...#...#.#.#.#.#.#.#.#.#.#  
  #.#######.###############.#.#####.###.#.#.###.#.#.#.###.###.#.###.#.###.###.#.#.#.#.###.###.#####.#.###.#.#.#.#.#.#.#.###  
  #.#...........#.#.#...#.................#.#.#...#.....#.#.#.#.....#.#.....#...#.#.#.#.......#.#.#.#.#.#...........#.#...#  
  #############.#.#.###.###.#.#.###.#####.###.#.#####.#####.#.###.###.#.#.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.###.###.#.###.#  
  #.#.....#.#.#.............#.#.#...#.....#.#.....#...#...#...#.#.#...#.#.#.#.#.#.#...........#.#.#.#.....#...#...#.#.#...#  
  #.###.#.#.#.#.#.###.###.###.#######.#.###.###.#######.#.#.#.#.###.#######.###.###.#.###.###.#.#.#.#.###.#############.#.#  
  #...#.#.#.....#.#.#.#...#.#.#.#.....#.....#.#.....#...#...#.....#...#.....#.#.#.#.#.#...#.............#.......#...#.#.#.#  
  ###.#.#####.#.###.#.#.#.#.###.#.#######.###.#.#######.###.###.###.#.#.#####.#.#.###.#.###.#.###.#.#.#.###.#####.###.###.#  
  #...........#...#...#.#.#.#...#.#.....#.....#...#...#.#.....#.#...#.#.......#.....#.#...#.#.#.#.#.#.#...#.............#.#  
  #.#.#######.#.#.###.###.#.###.###.###.#####.#.###.###.#.#.#########.#.#.#.#.###.###.#.#######.#.#.###########.###########  
  #.#.#.#.#...#.#.#.....#.#...#.....#.#.#.....#...#...#.#.#.#.#.#.#.#.#.#.#.#.#.....#.#.......#...#.......#...#...#.......#  
  #.###.#.#.###.#######.#####.#######.#.#.#####.#####.#.#####.#.#.#.#.###.###.#.#.###.#############.###.###.#######.#######  
  #.#.....#.#.#.....#...#.............#...#.#...#.#.....#.......#.#.#...#.#.#.#.#...#.....#.....#...#...#...#...#.#.#.#...#  
  #.###.#.###.#.#####.###.###########.#.###.###.#.#####.#.###.#.#.#.#.###.#.#.#.#######.###.###############.#.#.#.#.#.#.#.#  
  #.#.#.#.....#.#...#.#.#.#.......#...........#.......#...#.#.#.#.......#.#...#.....#.#.#...#.#.........#.....#.#.....#.#.#  
  ###.###.###.#.#.#####.#########.#.#.#.#.#####.#.###.#.#.#.#####.#.#######.#.###.###.#####.#.###.#########.#######.###.#.#  
  #.....#.#.#.#.#...#...............#.#.#.....#.#.#.#.#.#.......#.#.....#...#...#.....#.......#.#...#...#.......#.#.....#.#  
  ###.###.#.#####.###.#.###.#.#.###.#.###.#####.###.#####.###.#.###.#.###.###.#.#.#.###.#.#.#.#.#.#.#.###.#######.#.#.#####  
  #...#...#...#...#.#.#...#.#.#...#.#.#.....#.#...#...#...#...#.#...#.#.#.#...#.#.#...#.#.#.#.#...#.#.#...#...#...#.#.#...#  
  ###.###.#.#####.#.#####################.#.#.###.#.#########.#######.#.###.#######.#.#.#####.#.#.###.###.###.###.#.#.###.#  
  #.#.....#.#.#.........#...........#.....#.#...#.#.#...#.#.#...#...#...#...#.....#.#.#...#.....#.#...#.......#.#...#.#.#.#  
  #.#####.#.#.#####.###########.###.###.###.###.#.#.#.###.#.#.###.#.#.###.#.###.#####.#.#.#####.#####.#.#######.#.#####.#.#  
  #...#.......#.#...#.#.....#...#.....#...#...#.....#.......#...#.#...#.#.#.#...........#...#.#.#.......#.#.#...#.....#...#  
  #.#######.###.###.#.#####.#####.###.#.#######.###.###.###.#.###.###.#.###.###.#########.#.#.#######.###.#.#.#####.###.###  
  #.#...#.#.......#.#.#.#...#.#...#.......#.#...#...#...#.#.#.#...#.#.#...#...#.........#.#.#.#.#.#.#.#.......#.#.....#...#  
  #.###.#.#.#######.#.#.#.###.#########.###.###.#######.#.#.#.#.###.###.#.###.###.#.#.#######.#.#.#.#.#.#######.#####.#.###  
  #...........#.#.....#.....#.....#...........#...#.......#...#.......#.#.......#.#.#...#...#.......#.#.....#.#.#.........#  
  #.#####.#.#.#.###.#.#.#.###.###.#########.#####.#####.###########.###.#########.#########.#.#######.###.###.#.#####.#####  
  #.#.#.#.#.#.#.#.#.#...#.#...#...#        G     N     H           Q   I         H        #...#...#.#.#.....#.#.#...#.#.#.#  
  ###.#.###.###.#.#####.#########.#        C     W     L           B   F         U        #.#####.#.#.###.###.#.#.###.#.#.#  
  #...#...#...#.#.#.#.#...#.#...#.#                                                       #...#.......#...................#  
  #.###.###.###.#.#.#.#.#.#.###.#.#                                                       #.#.#.#####.#.###.###.#.#.###.###  
  #.#.#...#...#.....#.#.#.#...#...#                                                     IH..#...#.#...#.#.#...#.#.#...#...#  
  #.#.#.###.#.###.###.###.#.###.###                                                       #.#.#.#.###.#.#.#######.#######.#  
  #.......#.#.......#.#...........#                                                       #.#.#.#.#.....#.#.#.#...#.#.#....WD
  #.#.#########.#.###.#####.#.#####                                                       #######.#######.#.#.###.#.#.#####  
  #.#.....#...#.#.#.#...#.#.#...#.#                                                       #.#.#...#.............#.#.#.#...#  
  #.#.#####.#.#.#.#.#.###.#.###.#.#                                                       #.#.#.#.#.###.#.###.#.###.#.#.#.#  
UQ..#.....#.#...#...#.#.#.....#....XT                                                   UZ....#.#.....#.#...#.#.......#.#.#  
  ###.###.#.###.#.#.#.#.#####.#.###                                                       ###.#.###.#.###.#.#.#######.#.#.#  
  #.#.#.....#.#.#.#...........#.#.#                                                       #...#.#.#.#.#...#.#.#.#.....#.#..AH
  #.###.#####.#####.#.#.#########.#                                                       #.###.#.#######.#####.#####.#.###  
YI....#.#.#.#.....#.#.#.#..........RV                                                     #...........#.#.#...#.....#...#.#  
  ###.###.#.#.#######.###.#####.###                                                       #########.###.###.#####.#.#####.#  
  #.....#.......#...#.#...#.......#                                                       #.......#.#...#.#...#.#.#.....#..OS
  ###.#.#####.###.#########.###.#.#                                                       #.#####.#####.#.#.#.#.###.###.#.#  
  #...#.#.#.......#.#.....#...#.#.#                                                       #.#.......#.....#.#.#.....#...#.#  
  #.#.###.###.#.#.#.#.###.###.###.#                                                       #.#.#########.#####.#####.#.###.#  
  #.#.........#.#.....#.#.....#...#                                                       #.#...#.#.....#.#.#.#.#.#.#.#...#  
  #######.#######.###.#.#.###.#####                                                       #.###.#.#####.#.#.#.#.#.#.#.###.#  
  #.....#.#...#...#.#.#.....#.#....ZO                                                   AH..#.#.....................#.....#  
  #.#.#####.#######.###.#.###.###.#                                                       ###.#.#######################.###  
UZ..#...#.....#.#.#.#.#.#...#.#.#.#                                                     UP..#.#...#.#.............#.#.#.#.#  
  ###.###.###.#.#.#.#.#########.#.#                                                       #.#.#.###.###.###.###.#.#.#.###.#  
  #.....#...#.......#...#.#.....#.#                                                       #...#.#...#.....#...#.#.......#..KD
  #.#######.#.#.#.#.#.#.#.###.###.#                                                       #.#####.#.###.#.###.#######.###.#  
  #.........#.#.#.#...#...........#                                                       #.......#.#...#.#.....#.#.....#.#  
  ###.###.#######.#.###.#.#########                                                       ###.#.#######.###.#####.#####.#.#  
  #.....#.#...#.#.#...#.#.#.#...#.#                                                       #.#.#.........#.#.#.....#.......#  
  ###########.#.###########.#.#.#.#                                                       #.#############.###.###.#######.#  
  #.#.#.#.#.....#.#.#.....#...#...#                                                     YI....#...........#.....#.#.#.#...#  
  #.#.#.#.###.#.#.#.###.###.###.#.#                                                       ###.#.###.###.#.#.#.#.###.#.#####  
  #.........#.#.#.#.......#...#.#.#                                                       #...#.#.....#.#...#.#.....#.....#  
  #.#####.###.###.#####.#.###.#.###                                                       #.#.#.#####.#.#########.###.#.###  
MI......#...............#.....#....KD                                                     #.#.#.#.#.#.#.#...#.#.....#.#.#..ZZ
  #.#######################.#######                                                       #.###.#.#.#######.#.###.#.###.#.#  
  #.....#...#...........#.#.#.....#                                                       #.....#.....#.#.#...#.#.#........ZO
  #.#####.#.#.#.#.#.#.#.#.###.###.#                                                       #.#####.###.#.#.#.###.###########  
  #.#.#.#.#...#.#.#.#.#.....#...#..CT                                                     #.#.#.....#.#.........#.........#  
  ###.#.#.#####.###########.#.#.###                                                       ###.#.#.#.###.#######.###.#.#.###  
UP......#...#.#.....#.#.....#.#....NG                                                     #...#.#.#.......#.........#.#...#  
  #.#.#.#.#.#.###.###.#.#########.#                                                       #.#.#.#.#####.#########.#.#####.#  
VH..#.#...#.#...#.#...#...........#                                                       #.#.#.#.....#.....#.....#...#...#  
  #.#########.#######.#########.###                                                       #.#.#####.###.###.#.#.#.#######.#  
  #...#.......#.#...#...#...#...#.#                                                     VO..#.......#...#...#.#.#.#...#....IH
  #####.#####.#.###.#.#.#.#.###.#.#                                                       #.#########################.#####  
AA....#.#...#...#.#...#...#.#.#.#.#                                                       #.#.#...#...............#........VO
  ###.#.###.#.###.###.#####.#.#.#.#                                                       ###.#.#.#.###.#.###.###.#.#.###.#  
NW....#.....#.#.#.#.#...#.#...#.#..MI                                                   IU..#...#...#...#...#.#.....#...#.#  
  #.#######.#.#.#.#.###.#.###.###.#                                                       #.###.#.#######.#######.###.#.###  
  #.........#...........#.........#                                                       #...#.#.......#.#.........#.#...#  
  #.#.#####.###.#.#.###.###.###.###                                                       #.#.#.#########.###.###.#####.###  
  #.#...#...#.#.#.#...#.#.#.#.#...#                                                       #.#.........#...#.#.#.......#...#  
  #.#.###.###.#.#.###.#.#.#.#.#.###      V         N M     O       O     W         U      #.#.#.#.###.#####.#.#######.#####  
  #.#.#.......#.#...#.#...#...#...#      H         B C     S       E     D         Q      #.#.#.#...#.....#.........#.....#  
  #.###.#.#.#####.#####.#.#####.#.#######.#########.#.#####.#######.#####.#########.###########.###########.#.#####.#.#.#.#  
  #...#.#.#.#.....#.....#.#.....#.#.#.....#.........#.#.......#.....#.#.#.....#...#.#.......#.....#.....#.#.#.#.#.#.#.#.#.#  
  #.#.#.#.#######.#######.###.#.###.#.###.###.###.###.#.#.#######.###.#.###.#####.#.#######.#.###.#.#####.###.#.#.###.###.#  
  #.#.#.#.#.#.#.......#.....#.#...#.....#.#.....#.#...#.#.#...#.........#...#.....#.....#.....#.....#.#.....#.......#...#.#  
  #.#.#.###.#.###.#######.###########.#########.#####.###.###.#########.###.###.#####.#####.#.#.#.#.#.#.#.#.#####.#####.#.#  
  #.#.#.#.............#.....#.......#.#.....#...#...#...#.......#.........#.......#.....#...#.#.#.#.#...#.#...#.....#.#.#.#  
  #.#.###.#.#.#####.#####.#.#######.#.#.#.###.#.###.###.###.#####.###.#.#######.###.###############.#.#.###.#####.###.###.#  
  #.#...#.#.#.#.#.#.#.#...#...#...#...#.#...#.#.......#.#.......#...#.#.#.....#.#.......#.......#.....#...#.#.......#.....#  
  #.#.###.#.###.#.#.#.###.#####.#####.#.#.#########.###.#######.#.#######.###.#.#####.#####.#.#####.#.#.#########.#.#####.#  
  #.#.#.#.#.#.........#.....#.........#.#...#.......#.....#.#.#.#.....#...#.....#.#.#.......#.#.....#.#...#.#.#...#.#.....#  
  #.###.###.###.###.#########.#.###.#.#.###.###.###.#.#####.#.#.#.#######.###.###.#.###.###.#####.#.#######.#.#########.#.#  
  #.......#.#.#.#.#...#...#.#.#.#...#.#.#.#.#.....#.#...#.#.....#...#.#.#.#...#...#.....#.....#...#...............#.....#.#  
  #.#.#######.#.#.###.#.#.#.#########.#.#.#.###.###.###.#.###.#.#.#.#.#.#.#####.#####.#.#####.#.#.###.#####.###.#.#######.#  
  #.#...#...........#.#.#.#...#...........#...#...#.#...#.#...#.#.#...#.#...#.........#...#...#.#...#.....#.#.#.#.....#...#  
  #.#.#.#.#.#.#.#.#######.###.#.#.#.###.#.#.#######.#.###.#####.#.#####.#.#######.#.###.###.#####.###.###.###.###.#.###.###  
  #.#.#.#.#.#.#.#.#.#.#.........#.#.#.#.#.#...#...#.#.......#.#.#.#...#...#...#.#.#.#.#...#.#.......#.#.........#.#...#...#  
  #.#.#######.#.###.#.###.###########.#.#.#.#####.#.###.#####.#.#.###.###.#.###.#.###.###.#.#####.#.###.#.#.#.#############  
  #.#.#.....#.#.#.....#...#...#...#.#.#.#.#...#.....#.....#.#...#.......#...#.#.......#.#.#.#.....#...#.#.#.#...#.........#  
  ###.#####.#########.#######.###.#.#.#####.###.#.###.#####.###.#.#.#####.###.###.#####.#########.#.#####.###.#.#####.###.#  
  #.#.#.........#.#...#.#...............#.#.#.#.#...#.....#.#.#.#.#.#.......#.....#...........#...#.#.......#.#.#.#.....#.#  
  #.#.#######.###.###.#.#####.#.#.#.#.###.#.#.#####.#.###.#.#.#.#.#####.#.#######.#.#####.#######.#####.#.###.###.#.#.#####  
  #...#.....#.#...#.#.....#.#.#.#.#.#.#.......#.....#.#.#.#.....#...#...#...#.........#.#.#.#.#.#.....#.#...#.......#.#...#  
  #.#.###.###.#.###.###.###.#######.###.###########.#.#.###.#.###.#######.#######.#.###.###.#.#.#################.#.#.#.#.#  
  #.#.#.....#.#.#.#.#...#.#.#.......#...........#.#.#...#...#...#.#...#...#.....#.#.#...........#.............#...#.#...#.#  
  #.#.###.#.#.#.#.#.###.#.#.###.###.#######.#.###.#.###.###.#.#.#.###.###.###.#.#.#.#.#######.#.#.###.###.#.#####.#.###.###  
  #.#.#.#.#.........#...#.#.#...#.#.........#...#.....#.#...#.#.#.......#.....#.#.#.#...#...#.#.....#...#.#.#.....#.#.....#  
  #.###.#####.#####.###.#.#.#.###.###.###.#.#######.###.#.#######.#####.#.#####.#.###.#####.###.#.#.#######.###.#######.#.#  
  #.#.......#.#...............#.........#.#.#.........#.#...#...#.#.#...#.#.....#.#.....#.#.#.#.#.#.....#...#.........#.#.#  
  #########.#######.#.#.###.#.###.#.#.#########.#######.###.#.###.#.###.###.#####.###.###.#.#.#####.#.#####.#####.#.#.###.#  
  #.#.#.#.#.#...#.#.#.#.#...#...#.#.#.........#.......#...#.#...#.....#.#.....#.......#...#...#.#.#.#...#.#...#...#.#...#.#  
  #.#.#.#.#.###.#.#.#.###.#######.#######.#####.###.###.###.#.#######.###.###########.###.#.#.#.#.#.#.###.#######.###.#####  
  #.................#...#.....#...#.........#.....#.#...#.....#.........#.........#.........#.....#.#...........#...#.....#  
  #####################################.###########.###.#####.###.#########.#########.#####################################  
                                       N           I   R     H   N         X         Q                                       
                                       B           U   V     L   G         T         B                                       
"

# COMMAND ----------

m <-
  read_lines(input) %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

# COMMAND ----------

portals <- arrayInd(which(m %in% LETTERS), dim(m), useNames = TRUE) %>% as_tibble()

for (i in seq_len(nrow(portals))) {
  prefix_row <- portals$row[i]
  prefix_col <- portals$col[i]
  
  for (direction in c("N", "E", "S", "W")) {
    suffix_row <- prefix_row + (direction == "S") - (direction == "N")
    suffix_col <- prefix_col + (direction == "E") - (direction == "W")
    target_row <- suffix_row + (direction == "S") - (direction == "N")
    target_col <- suffix_col + (direction == "E") - (direction == "W")
    
    if (suffix_row == 0 || suffix_col == 0 || suffix_row > nrow(m) || suffix_col > ncol(m)) next
    if (target_row == 0 || target_col == 0 || target_row > nrow(m) || target_col > ncol(m)) next
    
    if (m[suffix_row, suffix_col] %in% LETTERS && m[target_row, target_col] == ".") {
      if (direction %in% c("N", "W")) {
        temp_row <- prefix_row
        temp_col <- prefix_col
        prefix_row <- suffix_row
        prefix_col <- suffix_col
        suffix_row <- temp_row
        suffix_col <- temp_col
      }
      m[target_row, target_col] <- str_c(m[prefix_row, prefix_col], m[suffix_row, suffix_col])
    }
  }
}
m[m %in% LETTERS] <- " "

# COMMAND ----------

coords <-
  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m)) %>%
  filter(value != " ")

coords <-
  left_join(
    coords,
    coords %>% filter(!(value %in% c("#", "."))),
    by = "value",
    suffix = c("", "_to")
  ) %>%
  filter(value %in% c("AA", "ZZ") | is.na(row_to) | !(row == row_to & col == col_to)) %>%
  mutate(
    row_to = coalesce(row_to, row),
    col_to = coalesce(col_to, col)
  )

coords

# COMMAND ----------

coords %>%
  mutate(
    label = ifelse(str_detect(value, "\\w"), value, NA),
    fill = case_when(
      !is.na(label) ~ "#DEDEDE",
      value == "#" ~ "#2F4858",
      value == "@" ~ "#F26419",
      value == "." ~ "#DEDEDE"
    )
  ) %>%
  ggplot(aes(col, row, fill = I(fill), label = label)) +
    geom_tile() +
    geom_label(size = 3, mapping = aes(col = label), fill = "white", label.padding = unit(0.05, "lines")) +
    scale_y_reverse() +
    theme_void() +
    theme(legend.position = "none")

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp(std::vector<int> rows, std::vector<int> cols, std::vector<std::string> values, std::vector<int> to_rows, std::vector<int> to_cols) {
  using State = std::tuple<int, int, std::string, int>; // row, col, value, d

  std::map<std::pair<int, int>, std::string> coords; // row, col -> value
  std::set<std::pair<int, int>> visited; // row, col
  std::vector<State> states;
  std::map<std::pair<int, int>, std::pair<int, int>> portals; // row, col -> row, col

  auto comp = [](const State& lhs, const State& rhs){ return std::get<3>(rhs) < std::get<3>(lhs); };

  for (int i = 0; i < rows.size(); ++i) {
    coords[std::make_pair(rows[i], cols[i])] = values[i];

    if (values[i] == "AA") {
      states.push_back(std::make_tuple(rows[i], cols[i], values[i], 0));
    }

    portals[std::make_pair(rows[i], cols[i])] = std::pair(to_rows[i], to_cols[i]);
  }

  while (states.size()) {
    auto [row, col, value, d] = states.front();
    std::pop_heap(states.begin(), states.end(), comp);
    states.pop_back();

    auto state_id = std::pair(row, col);
    if (visited.find(state_id) != visited.end()) continue;
    visited.insert(state_id);

    for (char direction : {\'N\', \'E\', \'S\', \'W\'}) {
      auto [new_row, new_col] = portals[std::make_pair(
        row + (direction == \'S\') - (direction == \'N\'),
        col + (direction == \'E\') - (direction == \'W\')
      )];
      std::string new_value = coords[std::make_pair(new_row, new_col)];
      int new_d = d + 1 + (value != "." && value != "#");

      if (new_value == "ZZ") return new_d - 1;
      if (new_value == "" || new_value == "#") continue;

      states.push_back(std::make_tuple(new_row, new_col, new_value, new_d));
      std::push_heap(states.begin(), states.end(), comp);
    }
  }

  Rcpp::stop("Unable to find solution");
}
',
  plugins = "cpp17" # For structured bindings
)

# COMMAND ----------

answer <- solve_cpp(
  rows = coords$row,
  cols = coords$col, 
  values = coords$value,
  to_rows = coords$row_to,
  to_cols = coords$col_to
)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Strangely, the exit isn't open when you reach it.  Then, you remember: the ancient Plutonians were famous for building <em>recursive spaces</em>.</p>
# MAGIC <p>The marked connections in the maze aren't portals: they <em>physically connect</em> to a larger or smaller copy of the maze. Specifically, the labeled tiles around the inside edge actually connect to a smaller copy of the same maze, and the smaller copy's inner labeled tiles connect to yet a <em>smaller</em> copy, and so on.</p>
# MAGIC <p>When you enter the maze, you are at the outermost level; when at the outermost level, only the outer labels <code>AA</code> and <code>ZZ</code> function (as the start and end, respectively); all other outer labeled tiles are effectively walls. At any other level, <code>AA</code> and <code>ZZ</code> count as walls, but the other outer labeled tiles bring you one level outward.</p>
# MAGIC <p>Your goal is to find a path through the maze that brings you back to <code>ZZ</code> at the outermost level of the maze.</p>
# MAGIC <p>In the first example above, the shortest path is now the loop around the right side. If the starting level is <code>0</code>, then taking the previously-shortest path would pass through <code>BC</code> (to level <code>1</code>), <code>DE</code> (to level <code>2</code>), and <code>FG</code> (back to level <code>1</code>). Because this is not the outermost level, <code>ZZ</code> is a wall, and the only option is to go back around to <code>BC</code>, which would only send you even deeper into the recursive maze.</p>
# MAGIC <p>In the second example above, there is no path that brings you to <code>ZZ</code> at the outermost level.</p>
# MAGIC <p>Here is a more interesting example:</p>
# MAGIC <pre><code>             Z L X W       C                 
# MAGIC              Z P Q B       K                 
# MAGIC   ###########.#.#.#.#######.###############  
# MAGIC   #...#.......#.#.......#.#.......#.#.#...#  
# MAGIC   ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
# MAGIC   #.#...#.#.#...#.#.#...#...#...#.#.......#  
# MAGIC   #.###.#######.###.###.#.###.###.#.#######  
# MAGIC   #...#.......#.#...#...#.............#...#  
# MAGIC   #.#########.#######.#.#######.#######.###  
# MAGIC   #...#.#    F       R I       Z    #.#.#.#  
# MAGIC   #.###.#    D       E C       H    #.#.#.#  
# MAGIC   #.#...#                           #...#.#  
# MAGIC   #.###.#                           #.###.#  
# MAGIC   #.#....OA                       WB..#.#..ZH
# MAGIC   #.###.#                           #.#.#.#  
# MAGIC CJ......#                           #.....#  
# MAGIC   #######                           #######  
# MAGIC   #.#....CK                         #......IC
# MAGIC   #.###.#                           #.###.#  
# MAGIC   #.....#                           #...#.#  
# MAGIC   ###.###                           #.#.#.#  
# MAGIC XF....#.#                         RF..#.#.#  
# MAGIC   #####.#                           #######  
# MAGIC   #......CJ                       NM..#...#  
# MAGIC   ###.#.#                           #.###.#  
# MAGIC RE....#.#                           #......RF
# MAGIC   ###.###        X   X       L      #.#.#.#  
# MAGIC   #.....#        F   Q       P      #.#.#.#  
# MAGIC   ###.###########.###.#######.#########.###  
# MAGIC   #.....#...#.....#.......#...#.....#.#...#  
# MAGIC   #####.#.###.#######.#######.###.###.#.#.#  
# MAGIC   #.......#.......#.#.#.#.#...#...#...#.#.#  
# MAGIC   #####.###.#####.#.#.#.#.###.###.#.###.###  
# MAGIC   #.......#.....#.#...#...............#...#  
# MAGIC   #############.#.#.###.###################  
# MAGIC                A O F   N                     
# MAGIC                A A D   M                     
# MAGIC </code></pre>
# MAGIC <p>One shortest path through the maze is the following:</p>
# MAGIC <ul>
# MAGIC <li>Walk from <code>AA</code> to <code>XF</code> (16 steps)</li>
# MAGIC <li>Recurse into level 1 through <code>XF</code> (1 step)</li>
# MAGIC <li>Walk from <code>XF</code> to <code>CK</code> (10 steps)</li>
# MAGIC <li>Recurse into level 2 through <code>CK</code> (1 step)</li>
# MAGIC <li>Walk from <code>CK</code> to <code>ZH</code> (14 steps)</li>
# MAGIC <li>Recurse into level 3 through <code>ZH</code> (1 step)</li>
# MAGIC <li>Walk from <code>ZH</code> to <code>WB</code> (10 steps)</li>
# MAGIC <li>Recurse into level 4 through <code>WB</code> (1 step)</li>
# MAGIC <li>Walk from <code>WB</code> to <code>IC</code> (10 steps)</li>
# MAGIC <li>Recurse into level 5 through <code>IC</code> (1 step)</li>
# MAGIC <li>Walk from <code>IC</code> to <code>RF</code> (10 steps)</li>
# MAGIC <li>Recurse into level 6 through <code>RF</code> (1 step)</li>
# MAGIC <li>Walk from <code>RF</code> to <code>NM</code> (8 steps)</li>
# MAGIC <li>Recurse into level 7 through <code>NM</code> (1 step)</li>
# MAGIC <li>Walk from <code>NM</code> to <code>LP</code> (12 steps)</li>
# MAGIC <li>Recurse into level 8 through <code>LP</code> (1 step)</li>
# MAGIC <li>Walk from <code>LP</code> to <code>FD</code> (24 steps)</li>
# MAGIC <li>Recurse into level 9 through <code>FD</code> (1 step)</li>
# MAGIC <li>Walk from <code>FD</code> to <code>XQ</code> (8 steps)</li>
# MAGIC <li>Recurse into level 10 through <code>XQ</code> (1 step)</li>
# MAGIC <li>Walk from <code>XQ</code> to <code>WB</code> (4 steps)</li>
# MAGIC <li>Return to level 9 through <code>WB</code> (1 step)</li>
# MAGIC <li>Walk from <code>WB</code> to <code>ZH</code> (10 steps)</li>
# MAGIC <li>Return to level 8 through <code>ZH</code> (1 step)</li>
# MAGIC <li>Walk from <code>ZH</code> to <code>CK</code> (14 steps)</li>
# MAGIC <li>Return to level 7 through <code>CK</code> (1 step)</li>
# MAGIC <li>Walk from <code>CK</code> to <code>XF</code> (10 steps)</li>
# MAGIC <li>Return to level 6 through <code>XF</code> (1 step)</li>
# MAGIC <li>Walk from <code>XF</code> to <code>OA</code> (14 steps)</li>
# MAGIC <li>Return to level 5 through <code>OA</code> (1 step)</li>
# MAGIC <li>Walk from <code>OA</code> to <code>CJ</code> (8 steps)</li>
# MAGIC <li>Return to level 4 through <code>CJ</code> (1 step)</li>
# MAGIC <li>Walk from <code>CJ</code> to <code>RE</code> (8 steps)</li>
# MAGIC <li>Return to level 3 through <code>RE</code> (1 step)</li>
# MAGIC <li>Walk from <code>RE</code> to <code>IC</code> (4 steps)</li>
# MAGIC <li>Recurse into level 4 through <code>IC</code> (1 step)</li>
# MAGIC <li>Walk from <code>IC</code> to <code>RF</code> (10 steps)</li>
# MAGIC <li>Recurse into level 5 through <code>RF</code> (1 step)</li>
# MAGIC <li>Walk from <code>RF</code> to <code>NM</code> (8 steps)</li>
# MAGIC <li>Recurse into level 6 through <code>NM</code> (1 step)</li>
# MAGIC <li>Walk from <code>NM</code> to <code>LP</code> (12 steps)</li>
# MAGIC <li>Recurse into level 7 through <code>LP</code> (1 step)</li>
# MAGIC <li>Walk from <code>LP</code> to <code>FD</code> (24 steps)</li>
# MAGIC <li>Recurse into level 8 through <code>FD</code> (1 step)</li>
# MAGIC <li>Walk from <code>FD</code> to <code>XQ</code> (8 steps)</li>
# MAGIC <li>Recurse into level 9 through <code>XQ</code> (1 step)</li>
# MAGIC <li>Walk from <code>XQ</code> to <code>WB</code> (4 steps)</li>
# MAGIC <li>Return to level 8 through <code>WB</code> (1 step)</li>
# MAGIC <li>Walk from <code>WB</code> to <code>ZH</code> (10 steps)</li>
# MAGIC <li>Return to level 7 through <code>ZH</code> (1 step)</li>
# MAGIC <li>Walk from <code>ZH</code> to <code>CK</code> (14 steps)</li>
# MAGIC <li>Return to level 6 through <code>CK</code> (1 step)</li>
# MAGIC <li>Walk from <code>CK</code> to <code>XF</code> (10 steps)</li>
# MAGIC <li>Return to level 5 through <code>XF</code> (1 step)</li>
# MAGIC <li>Walk from <code>XF</code> to <code>OA</code> (14 steps)</li>
# MAGIC <li>Return to level 4 through <code>OA</code> (1 step)</li>
# MAGIC <li>Walk from <code>OA</code> to <code>CJ</code> (8 steps)</li>
# MAGIC <li>Return to level 3 through <code>CJ</code> (1 step)</li>
# MAGIC <li>Walk from <code>CJ</code> to <code>RE</code> (8 steps)</li>
# MAGIC <li>Return to level 2 through <code>RE</code> (1 step)</li>
# MAGIC <li>Walk from <code>RE</code> to <code>XQ</code> (14 steps)</li>
# MAGIC <li>Return to level 1 through <code>XQ</code> (1 step)</li>
# MAGIC <li>Walk from <code>XQ</code> to <code>FD</code> (8 steps)</li>
# MAGIC <li>Return to level 0 through <code>FD</code> (1 step)</li>
# MAGIC <li>Walk from <code>FD</code> to <code>ZZ</code> (18 steps)</li>
# MAGIC </ul>
# MAGIC <p>This path takes a total of <em>396</em> steps to move from <code>AA</code> at the outermost layer to <code>ZZ</code> at the outermost layer.</p>
# MAGIC <p>In your maze, when accounting for recursion, <em>how many steps does it take to get from the open tile marked <code>AA</code> to the open tile marked <code>ZZ</code>, both at the outermost layer?</em></p>
# MAGIC </article>

# COMMAND ----------

coords <-
  which(m != "", arr.ind = TRUE) %>%
  as_tibble() %>%
  mutate(value = c(m)) %>%
  filter(value != " ")

coords <-
  left_join(
    coords,
    coords %>% filter(!(value %in% c("#", "."))),
    by = "value",
    suffix = c("", "_to")
  ) %>%
  filter(value %in% c("AA", "ZZ") | is.na(row_to) | !(row == row_to & col == col_to)) %>%
  mutate(
    row_to = coalesce(row_to, row),
    col_to = coalesce(col_to, col),
    depth_change = case_when(
      str_length(value) == 1 ~ 0,
      pmin(row, col, max(row) - row, max(col) - col) <= 3 ~ -1,
      TRUE ~ 1
    )
  )

coords

# COMMAND ----------

Rcpp::cppFunction('
int solve_cpp2(std::vector<int> rows, std::vector<int> cols, std::vector<std::string> values, std::vector<int> to_rows, std::vector<int> to_cols, std::vector<int> depth_changes) {
  using State = std::tuple<int, int, std::string, int, int>; // row, col, value, d, depth

  std::map<std::pair<int, int>, std::string> coords; // row, col -> value
  std::set<std::tuple<int, int, int>> visited; // row, col, depth
  std::vector<State> states;
  std::map<std::pair<int, int>, std::tuple<int, int, int>> portals; // row, col -> row, col, depth_change

  auto comp = [](const State& lhs, const State& rhs){ return std::get<3>(rhs) < std::get<3>(lhs); };

  for (int i = 0; i < rows.size(); ++i) {
    coords[std::make_pair(rows[i], cols[i])] = values[i];

    if (values[i] == "AA") {
      states.push_back(std::make_tuple(rows[i], cols[i], values[i], 0, 0));
    }

    portals[std::make_pair(rows[i], cols[i])] = std::make_tuple(to_rows[i], to_cols[i], depth_changes[i]);
  }

  while (states.size()) {
    auto [row, col, value, d, depth] = states.front();
    std::pop_heap(states.begin(), states.end(), comp);
    states.pop_back();

    auto state_id = std::make_tuple(row, col, depth);
    if (visited.find(state_id) != visited.end()) continue;
    visited.insert(state_id);

    for (char direction : {\'N\', \'E\', \'S\', \'W\'}) {
      auto [new_row, new_col, depth_change] = portals[std::make_pair(
        row + (direction == \'S\') - (direction == \'N\'),
        col + (direction == \'E\') - (direction == \'W\')
      )];
      std::string new_value = coords[std::make_pair(new_row, new_col)];
      int new_d = d + 1 + (value != "." && value != "#");
      int new_depth = depth + depth_change;

      if (new_value == "ZZ" && depth == 0) return new_d - 1;

      if (new_value == "ZZ" || new_value == "AA") continue;
      if (new_value == "" || new_value == "#") continue;
      if (new_depth < 0) continue;

      states.push_back(std::make_tuple(new_row, new_col, new_value, new_d, new_depth));
      std::push_heap(states.begin(), states.end(), comp);
    }
  }

  Rcpp::stop("Unable to find solution");
}
',
  plugins = "cpp17" # For structured bindings
)

# COMMAND ----------

answer <- solve_cpp2(
  rows = coords$row,
  cols = coords$col, 
  values = coords$value,
  to_rows = coords$row_to,
  to_cols = coords$col_to,
  depth_changes = coords$depth_change
)
answer
