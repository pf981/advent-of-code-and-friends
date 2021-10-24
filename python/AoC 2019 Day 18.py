# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/18

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 18: Many-Worlds Interpretation ---</h2><p>As you approach Neptune, a planetary security system detects you and activates a giant <a href="https://en.wikipedia.org/wiki/Tractor_beam">tractor beam</a> on <a href="https://en.wikipedia.org/wiki/Triton_(moon)">Triton</a>!  You have no choice but to land.</p>
# MAGIC <p>A scan of the local area reveals only one interesting feature: a massive underground vault.  You generate a map of the tunnels (your puzzle input).  The tunnels are too narrow to move diagonally.</p>
# MAGIC <p>Only one <em>entrance</em> (marked <code>@</code>) is present among the <em>open passages</em> (marked <code>.</code>) and <em>stone walls</em> (<code>#</code>), but you also detect an assortment of <em>keys</em> (shown as lowercase letters) and <em>doors</em> (shown as uppercase letters). Keys of a given letter open the door of the same letter: <code>a</code> opens <code>A</code>, <code>b</code> opens <code>B</code>, and so on.  You aren't sure which key you need to disable the tractor beam, so you'll need to <em>collect all of them</em>.</p>
# MAGIC <p>For example, suppose you have the following map:</p>
# MAGIC <pre><code>#########
# MAGIC #b.A.@.a#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Starting from the entrance (<code>@</code>), you can only access a large door (<code>A</code>) and a key (<code>a</code>). Moving toward the door doesn't help you, but you can move <code>2</code> steps to collect the key, unlocking <code>A</code> in the process:</p>
# MAGIC <pre><code>#########
# MAGIC #b.....@#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Then, you can move <code>6</code> steps to collect the only other key, <code>b</code>:</p>
# MAGIC <pre><code>#########
# MAGIC #@......#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>So, collecting every key took a total of <code><em>8</em></code> steps.</p>
# MAGIC <p>Here is a larger example:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.b.A.@.a.B.c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>The only reasonable move is to take key <code>a</code> and unlock door <code>A</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.b.....@.B.c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Then, do the same with key <code>b</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.C.@.........c.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>...and the same with key <code>c</code>:</p>
# MAGIC <pre><code>########################
# MAGIC #f.D.E.e.............@.#
# MAGIC ######################.#
# MAGIC #d.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Now, you have a choice between keys <code>d</code> and <code>e</code>.  While key <code>e</code> is closer, collecting it now would be slower in the long run than collecting key <code>d</code> first, so that's the best choice:</p>
# MAGIC <pre><code>########################
# MAGIC #f...E.e...............#
# MAGIC ######################.#
# MAGIC #@.....................#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Finally, collect key <code>e</code> to unlock door <code>E</code>, then collect key <code>f</code>, taking a grand total of <code><em>86</em></code> steps.</p>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <ul>
# MAGIC <li><pre><code>########################
# MAGIC #...............b.C.D.f#
# MAGIC #.######################
# MAGIC #.....@.a.B.c.d.A.e.F.g#
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Shortest path is <code>132</code> steps: <code>b</code>, <code>a</code>, <code>c</code>, <code>d</code>, <code>f</code>, <code>e</code>, <code>g</code></p></li>
# MAGIC <li><pre><code>#################
# MAGIC #i.G..c...e..H.p#
# MAGIC ########.########
# MAGIC #j.A..b...f..D.o#
# MAGIC ########@########
# MAGIC #k.E..a...g..B.n#
# MAGIC ########.########
# MAGIC #l.F..d...h..C.m#
# MAGIC #################
# MAGIC </code></pre>
# MAGIC <p>Shortest paths are <code>136</code> steps;<br>one is: <code>a</code>, <code>f</code>, <code>b</code>, <code>j</code>, <code>g</code>, <code>n</code>, <code>h</code>, <code>d</code>, <code>l</code>, <code>o</code>, <code>e</code>, <code>p</code>, <code>c</code>, <code>i</code>, <code>k</code>, <code>m</code></p></li>
# MAGIC <li><pre><code>########################
# MAGIC #@..............ac.GI.b#
# MAGIC ###d#e#f################
# MAGIC ###A#B#C################
# MAGIC ###g#h#i################
# MAGIC ########################
# MAGIC </code></pre>
# MAGIC <p>Shortest paths are <code>81</code> steps; one is: <code>a</code>, <code>c</code>, <code>f</code>, <code>i</code>, <code>d</code>, <code>g</code>, <code>b</code>, <code>e</code>, <code>h</code></p></li>
# MAGIC </ul>
# MAGIC <p><em>How many steps is the shortest path that collects all of the keys?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''#################################################################################
#.................C...#...#.......#.....#.#.........#.R.....#.....B............t#
#.###################.#.#.###.#.###.#.#V#.#.#####.#.#.#####.#.#####.###########.#
#...Z...#.......#.....#.#...#.#...#.#.#.#.#.#.#...#.#.#...#...#...#.#.....#.#...#
#.#####.#.#####.#.#####.###.#.###.#.#.###.#.#.#.#####.#.#.#####.#.#.#.###.#.#.###
#.#.....#k..#...#...#...#.#.#...#...#...#...#.#.......#.#.....#.#n#.....#.#...#.#
#.#.#.#####.#.#####.#.#.#.#.#.#########.#.###.#########.#.#####.#.#######.#.###.#
#.#.#.#.....#.#...F.#.#.#...#.#...#...#.#.#............m#.#.....#.......#.#.#...#
#.#.###.#####.#.#######.#.#####.#.#.#.#.#.#####.#####.#####.###########.#.#.#.#.#
#.#...#.#.....#...#.....#.......#.#.#.#.#.....#.#...#.#.....#.....#.......#.#.#.#
#.###.#.#.#######.#.#############.#.#.#.#####.#.#.#.###.#####.###.#########.#.#.#
#.#...#.#.......#.#...#...#.....#.#.#.#.#...#...#.#.#...#..q..#.#.#.....#.....#.#
#.#.###.#######.#.#.#.###.#.#.###.#.#.#.#.#.#.###.#.#.###.#####.#.#.###.#######.#
#.#...........#.#.#.#...#...#...#.#.#...#.#.#.#...#...#...#.....#...#.#w..#...#i#
#.###########.#.#.#####.#.#####.#.#.###U###.#.#.#######.###.#########.###.#.#.###
#...#.#.....#.#.#.......#.#...#.#.#...#.#...#.#.....#...#.........#.....#...#...#
###.#.#.###.#.#.#########.###.#.#.#.#.#.#.###.#####.#.#.#####.#.###.#.#########.#
#.#.#.#.#.#.#.#.#.......#.....#.#.#.#.#.#...#.#...#.#.#.#...#.#.#...#s......#...#
#.#.#.#.#.#.###.#####.#.#####.#.#.###.#.#.#.#.#.###.#.###.#.#.#.#.#######.###.###
#.....#.#.......#...#.#...#...#...#...#.#.#...#...#.#.....#.#.#...#..x..#....d#.#
#######.#########.#.#####.#.#######.###.#.#######.#.#######J###.###.###.#######.#
#.....#...#...#.S.#.#j..#...........#.#.#.#.......#.#.....#...#...#.#.#.#.#.....#
#.###.###.#.#.#.###.###.#############.#.#.#.#####.#.#.#.#########.#.#.#.#.#.#.#.#
#.#.....#.#.#.....#...#.......#.........#...#.....#...#.........#...#...#.#.#.#.#
#.#####.#.#.#######.#.#######.###.###########.###########.#.#########.###.#.#.###
#.#.E.#.#.#.#...#...#...#...#...#.....#.#.....#...........#.#.....#...#..e..#...#
#.#.#.#.#H#X#.#.#.#.#####W#.###Q#####.#.#.#####.###.#########.###.#.###########.#
#...#.#...#.#.#.#.#.#...#.#...#.#...#.#.#...#.#...#.#...#...#.#.#.#.............#
#####.#####.#.#.#.###.#.#.###.#.#.###.#.###.#.###.#.#.#.#.#.#.#.#.#############.#
#...#.#.....#.#.#...D.#...#.#.#.#.....#.#...#...#.#.#.#...#...#.#.#...........#.#
###.#.#.#####.#############.#.#.#.#####.#.#####.#.###.#########.#.#.###.#.#####.#
#...#...#..........o........#...#......g#.....#.#.....#...#.#...#.#.#.K.#.#....h#
#.#.#####.###########.#################.#####.#.#######.#.#.#.#.#.#.#.#####.#####
#.#.....#.#.....#...#.........#.......#.#.#...#.....#...#.#...#.#...#...#...#...#
#.#######.###.#.#.#.#######.#.#######.#.#.#.###.###.#.###.#####.#######.#.#####.#
#.#.....#...#.#...#...#...#.#.........#.#.#...#...#.#.#...........#.....#.....#.#
#.#.###.###.#.#######.#.###.#####.#####.#.###.#.#.#.#.###########.#.#########.#.#
#.#.#.#...#...#.#.....#...#.....#.#.....#.#...#.#.#.#...#.........#.#.........#.#
#.#.#.###.#####.#.#######.#####.###.#####.#.#####.#.###.#.#########.#.#########.#
#.......#.....................#...................#.....#.........#.............#
#######################################.@.#######################################
#.......#...........#.....#.....................#.....#.......#...........#.....#
#.#######.#.#######.#.###.#.#####.#####.#.#.#####.#.#.#######.#.#########.#####.#
#.#.......#.....#...#...#.#.#...#.....#.#.#.......#.#.........#.#.......#...#...#
#.#.###########.#.#####.###.#.#.#####.#.#.#####.###.###########.#.###.#.###.#.###
#b..#...........#.....#...#.#.#.#.#...#.#.#...#...#...#.........#.#...#.#...#...#
#.###.###############.###.#.#.#.#.#.###.###.#.#######.#.#########.#.#.###.#####.#
#...#...........#...#.#...#.#.#...#.#...#...#.......#.#.#.......#.#.#.#...#.....#
###.###########.###.#.#.#.#.#.###.#.###.#.#########.#.#.#.#####.###.#.#.###.###.#
#.............#...#.....#.#...#...#...#.#.#.#.....#.#.#.#.#...#.....#.#....l#...#
#.#########.#####.#####.#######.#####G#.#.#.#.#O###.#.#.#.#.#.#.#####.#######.###
#.#...#...#.#...#...#...#.....#...#...#.#.#.#.#...#...#.#.#.#.#.#.Y.#.......#.#.#
#.#.#.#.#.###.#.#.#.###.#.###.###.#.###.#.#.#.###.#.###.#.#.#.###.#.#######.#.#.#
#.#.#a..#.....#.#.#...#.#.#.#.....#.#.#.#.#.#...#...#...#.#.#.....#.....#...#.#.#
###.###########.#####.###.#.#####.#.#.#.#.#.###.#####.###.#.###########.#.###.#.#
#...#..y#.....#.#...#.......#...#.#.#...#.#.........#.#.......#.#.......#.#...#.#
#.###.#.#.#.#.#.#.#.#.#######.#.#.#.###.#.#.#########.#######.#.#.#######.#.###.#
#.....#.#.#.#.#...#.#.#.......#.#.#...#.#.#.#.......#.....#z#.#.#.#.....#.#p..#.#
#######.###.#######.#.#.#######.#####.###.###.#####.#####.#.#.#.#A#.###.#.###.#.#
#.....#.....#.....#.#.#.....#.......#...#...#...#.....#...#.....#.#...#.....#.#.#
#.###.#####.#.###.#.#######.#######.###.#.#.#.###.###.#.#######.#.#.#########.#.#
#...#.......#.#.#...#.....#...#...#...#.#.#...#...#...#.......#.#.#.#.........#.#
###.#########.#.#.#######.#.#.###.###.#.#.#####.###.###########.#.###.#########.#
#...#...#...P.#...#.......#.#...#.#...#.#.#.....#...#.......#.#.#.....#...#.....#
#.###.###.###.#####.#########.#.#.#.###.#.#.#######.#.#####.#.#.#######.#.#####.#
#.....#...#...#.....#.......#.#.#...#...#.#.......#...#...#...#.#.......#.......#
#####.#.###.###.#####.#####.###.###.#.#.#.#######.#####.#.###.#.###.###.#########
#...#c#...#.#...#.....#...#...#...#.#.#u#.#.....#.....#.#.....#...#...#.#.......#
###.#.###.###.###.#####.#####.###.#.#.#.#.#.###.#####.#.#########.###.#.#.#####.#
#...#...#.L.#.#.#...#.......#.#...#...#.#.#.#.#.#...#.#.....#...#.#...#.......#.#
#.#####.###.#.#.#.#.#.#####.#.#.#######.#.#.#.#.###.#.#####.#.#.#.#.#####.#####.#
#...#...#.#...#...#.#.....#.#.#.#.....#.#.#.#.#.....#...#...#.#...#.#...#.#...#.#
###.#.###.#########.###.###.#.#.#####.#.#.#.#.#####.###.#.###.#######.#.###.#.#.#
#...#...#.........#...#.#...#...#.....#.#...#.#...#.#.#.#.#...#.....#.#...N.#.#.#
#.#####.#.#####.#.###.#.#.#######.#####.#####.#.#.#.#.#.###.###.###.#.#######.#T#
#.I.#...#.#.....#.....#.#...#...#.......#.#.....#.#.#.#...#.#.....#...#...#...#.#
#.#.#.###.#.###############.#.#.#.#######.#.#####.#.#.###.#.#####.#####.#.#.###.#
#.#...#...#.#.....#.........#.#.#...#...#...#...#.#.#...#.#f......#.#...#.#.....#
#.#########.#.#####.###.#####.#.###.#.#.#.###.#.#.#.###.#.#########.#.#.#######.#
#...........#..r....M.#.......#v......#.#.....#.#.......#.............#.........#
#################################################################################'''

# COMMAND ----------

import collections
import heapq
import string

def solve(coords):
  visited = set()
  target_n_keys = sum(key in string.ascii_lowercase for key in coords.values())
  states = [(0, next(pos for pos, value in coords.items() if value == '@'), '@', frozenset())]
  
  while states:
    d, (row, col), value, keys = heapq.heappop(states)
    
    if (row, col, keys) in visited:
      continue
    visited.add((row, col, keys))
    
    # Key
    if value in string.ascii_lowercase:
      keys = keys.union({value})
      if len(keys) == target_n_keys:
        return d
    
    # Lock
    if value in string.ascii_uppercase:
      if value.lower() not in keys:
        continue
        
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      new_value = coords[(new_row, new_col)]

      if new_value != '#':
        heapq.heappush(states, (d + 1, (new_row, new_col), new_value, keys))


coords = collections.defaultdict(lambda: '#', {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line)})

answer = solve(coords)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You arrive at the vault only to <span title="To see the inspiration for this puzzle, look up 'Link to the Past Randomizer Multiworld'.">discover</span> that there is not one vault, but <em>four</em> - each with its own entrance.</p>
# MAGIC <p>On your map, find the area in the middle that looks like this:</p>
# MAGIC <pre><code>...
# MAGIC .@.
# MAGIC ...
# MAGIC </code></pre>
# MAGIC <p>Update your map to instead use the correct data:</p>
# MAGIC <pre><code>@#@
# MAGIC ###
# MAGIC @#@
# MAGIC </code></pre>
# MAGIC <p>This change will split your map into four separate sections, each with its own entrance:</p>
# MAGIC <pre><code>#######       #######
# MAGIC #a.#Cd#       #a.#Cd#
# MAGIC ##...##       ##<em>@#@</em>##
# MAGIC ##.@.##  --&gt;  ##<em>###</em>##
# MAGIC ##...##       ##<em>@#@</em>##
# MAGIC #cB#Ab#       #cB#Ab#
# MAGIC #######       #######
# MAGIC </code></pre>
# MAGIC <p>Because some of the keys are for doors in other vaults, it would take much too long to collect all of the keys by yourself.  Instead, you deploy four remote-controlled robots. Each starts at one of the entrances (<code>@</code>).</p>
# MAGIC <p>Your goal is still to <em>collect all of the keys in the fewest steps</em>, but now, each robot has its own position and can move independently.  You can only remotely control a single robot at a time. Collecting a key instantly unlocks any corresponding doors, regardless of the vault in which the key or door is found.</p>
# MAGIC <p>For example, in the map above, the top-left robot first collects key <code>a</code>, unlocking door <code>A</code> in the bottom-right vault:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#Cd#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##@#@##
# MAGIC #cB#.b#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Then, the bottom-right robot collects key <code>b</code>, unlocking door <code>B</code> in the bottom-left vault:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#Cd#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##@#.##
# MAGIC #c.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Then, the bottom-left robot collects key <code>c</code>:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#.d#
# MAGIC ##.#@##
# MAGIC #######
# MAGIC ##.#.##
# MAGIC #@.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>Finally, the top-right robot collects key <code>d</code>:</p>
# MAGIC <pre><code>#######
# MAGIC #@.#.@#
# MAGIC ##.#.##
# MAGIC #######
# MAGIC ##.#.##
# MAGIC #@.#.@#
# MAGIC #######
# MAGIC </code></pre>
# MAGIC <p>In this example, it only took <code><em>8</em></code> steps to collect all of the keys.</p>
# MAGIC <p>Sometimes, multiple robots might have keys available, or a robot might have to wait for multiple keys to be collected:</p>
# MAGIC <pre><code>###############
# MAGIC #d.ABC.#.....a#
# MAGIC ######@#@######
# MAGIC ###############
# MAGIC ######@#@######
# MAGIC #b.....#.....c#
# MAGIC ###############
# MAGIC </code></pre>
# MAGIC <p>First, the top-right, bottom-left, and bottom-right robots take turns collecting keys <code>a</code>, <code>b</code>, and <code>c</code>, a total of <code>6 + 6 + 6 = 18</code> steps. Then, the top-left robot can access key <code>d</code>, spending another <code>6</code> steps; collecting all of the keys here takes a minimum of <code><em>24</em></code> steps.</p>
# MAGIC <p>Here's a more complex example:</p>
# MAGIC <pre><code>#############
# MAGIC #DcBa.#.GhKl#
# MAGIC #.###@#@#I###
# MAGIC #e#d#####j#k#
# MAGIC ###C#@#@###J#
# MAGIC #fEbA.#.FgHi#
# MAGIC #############
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>Top-left robot collects key <code>a</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>b</code>.</li>
# MAGIC <li>Top-left robot collects key <code>c</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>d</code>.</li>
# MAGIC <li>Top-left robot collects key <code>e</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>f</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>g</code>.</li>
# MAGIC <li>Top-right robot collects key <code>h</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>i</code>.</li>
# MAGIC <li>Top-right robot collects key <code>j</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>k</code>.</li>
# MAGIC <li>Top-right robot collects key <code>l</code>.</li>
# MAGIC </ul>
# MAGIC <p>In the above example, the fewest steps to collect all of the keys is <code><em>32</em></code>.</p>
# MAGIC <p>Here's an example with more choices:</p>
# MAGIC <pre><code>#############
# MAGIC #g#f.D#..h#l#
# MAGIC #F###e#E###.#
# MAGIC #dCba@#@BcIJ#
# MAGIC #############
# MAGIC #nK.L@#@G...#
# MAGIC #M###N#H###.#
# MAGIC #o#m..#i#jk.#
# MAGIC #############
# MAGIC </code></pre>
# MAGIC <p>One solution with the fewest steps is:</p>
# MAGIC <ul>
# MAGIC <li>Top-left robot collects key <code>e</code>.</li>
# MAGIC <li>Top-right robot collects key <code>h</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>i</code>.</li>
# MAGIC <li>Top-left robot collects key <code>a</code>.</li>
# MAGIC <li>Top-left robot collects key <code>b</code>.</li>
# MAGIC <li>Top-right robot collects key <code>c</code>.</li>
# MAGIC <li>Top-left robot collects key <code>d</code>.</li>
# MAGIC <li>Top-left robot collects key <code>f</code>.</li>
# MAGIC <li>Top-left robot collects key <code>g</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>k</code>.</li>
# MAGIC <li>Bottom-right robot collects key <code>j</code>.</li>
# MAGIC <li>Top-right robot collects key <code>l</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>n</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>m</code>.</li>
# MAGIC <li>Bottom-left robot collects key <code>o</code>.</li>
# MAGIC </ul>
# MAGIC <p>This example requires at least <code><em>72</em></code> steps to collect all keys.</p>
# MAGIC <p>After updating your map and using the remote-controlled robots, <em>what is the fewest steps necessary to collect all of the keys?</em></p>
# MAGIC </article>

# COMMAND ----------

from operator import le, ge

coords2 = coords.copy()
mid = [dimension // 2 for dimension in max(coords2.keys())]

for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
  coords2[(mid[0] + dr, mid[1] + dc)] = '@'

for dr, dc in ((-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)):
  coords2[(mid[0] + dr, mid[1] + dc)] = '#'

quadrants = [{(row, col): value for (row, col), value in coords2.items() if f_row(row, mid[0]) and f_col(col, mid[1])}
             for f_row, f_col in [(le, le), (le, ge), (ge, le), (ge, ge)]]

# Remove locks where the key is in a different quadrant
quadrants = [{pos: value if value.lower() in quadrant.values() else '.' for pos, value in quadrant.items()}
             for quadrant in quadrants]

answer = sum(solve(quadrant) for quadrant in quadrants)
print(answer)
