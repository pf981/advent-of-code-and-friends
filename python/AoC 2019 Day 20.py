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

inp = '''                                           C   I         O     M       H             G                                       
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
                                       B           U   V     L   G         T         B                                       '''

# COMMAND ----------

import collections
import heapq
import string


def parse_input(inp):
  coords = collections.defaultdict(str, {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line)})

  for (row, col), value in coords.copy().items():
    side, affix = next(
      ((side, coords[(row+dr, col+dc)])
       for side, (dr, dc) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)])
       if
        value in string.ascii_uppercase and
        coords[(row+dr, col+dc)] in string.ascii_uppercase and 
        coords[(row-dr, col-dc)] == '.'),
      (None, None)
    )
    if affix:
      coords[(row, col)] = affix + value if side < 2 else value + affix

  portals = {}
  for pos, value in coords.items():
    portals[pos] = pos, 0
    if len(value) != 2:
      continue
    for pos2, value2 in coords.items():
      if value2 == value and pos2 != pos:
        is_outer = any(min(x, edge - x) <= 3 for x, edge in zip(pos, (max(x) for x in zip(*coords))))
        depth_change = -1 if is_outer else 1
        portals[pos] = pos2, depth_change

  coords = collections.defaultdict(str, {k: v for k, v in coords.items() if v == '.' or len(v) == 2})
  return portals, coords


def solve(portals, coords):
  start = next((row, col) for (row, col), value in coords.items() if value == 'AA')
  
  states = [(0, start)]
  visited = set()
  
  while states:
    d, (row, col) = heapq.heappop(states)

    if (row, col) in visited:
      continue
    visited.add((row, col))
    
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      if not coords[(new_row, new_col)]:
        continue
      (new_row, new_col), _ = portals[(new_row, new_col)]
      
      if coords[(new_row, new_col)] == 'ZZ':
        return d - 1
      
      if coords[(new_row, new_col)]:
        new_d = d + 1 if coords[(new_row, new_col)] == '.' else d
        heapq.heappush(states, (new_d, (new_row, new_col)))


portals, coords = parse_input(inp)

answer = solve(portals, coords)
print(answer)

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

def solve2(portals, coords):
  start = next((row, col) for (row, col), value in coords.items() if value == 'AA')
  
  states = [(0, 0, start)]
  visited = set()
  
  while states:
    d, depth, (row, col) = heapq.heappop(states)

    if (row, col, depth) in visited or depth < 0:
      continue
    visited.add((row, col, depth))
    
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      
      if not coords[(new_row, new_col)]:
        continue
      (new_row, new_col), depth_change = portals[(new_row, new_col)]

      if coords[(new_row, new_col)] == 'ZZ' and depth == 0:
        return d - 1
      
      if coords[(new_row, new_col)] not in ['', 'ZZ', 'AA']:
        new_d = d + 1 if coords[(new_row, new_col)] == '.' else d
        heapq.heappush(states, (new_d, depth + depth_change, (new_row, new_col)))


answer = solve2(portals, coords)
print(answer)
