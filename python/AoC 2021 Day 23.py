# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 23: Amphipod ---</h2><p>A group of <a href="https://en.wikipedia.org/wiki/Amphipoda" target="_blank">amphipods</a> notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod <span title="What? You didn't know amphipods can talk?">says</span>, "surely you can help us with a question that has stumped our best scientists."</p>
# MAGIC <p>They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: <em>Amber</em> (<code>A</code>), <em>Bronze</em> (<code>B</code>), <em>Copper</em> (<code>C</code>), and <em>Desert</em> (<code>D</code>). They live in a burrow that consists of a <em>hallway</em> and four <em>side rooms</em>. The side rooms are initially full of amphipods, and the hallway is initially empty.</p>
# MAGIC <p>They give you a <em>diagram of the situation</em> (your puzzle input), including locations of each amphipod (<code>A</code>, <code>B</code>, <code>C</code>, or <code>D</code>, each of which is occupying an otherwise open space), walls (<code>#</code>), and open space (<code>.</code>).</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###B#C#B#D###
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted <code>A</code>-<code>D</code> going left to right, like this:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###A#B#C#D###
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of <em>energy</em> to move one step: Amber amphipods require <code>1</code> energy per step, Bronze amphipods require <code>10</code> energy, Copper amphipods require <code>100</code>, and Desert ones require <code>1000</code>. The amphipods would like you to find a way to organize the amphipods that requires the <em>least total energy</em>.</p>
# MAGIC <p>However, because they are timid and stubborn, the amphipods have some extra rules:</p>
# MAGIC <ul>
# MAGIC <li>Amphipods will never <em>stop on the space immediately outside any room</em>. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)</li>
# MAGIC <li>Amphipods will never <em>move from the hallway into a room</em> unless that room is their destination room <em>and</em> that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)</li>
# MAGIC <li>Once an amphipod stops moving in the hallway, <em>it will stay in that spot until it can move into a room</em>. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)</li>
# MAGIC </ul>
# MAGIC <p>In the above example, the amphipods can be organized using a minimum of <code><em>12521</em></code> energy. One way to do this is shown below.</p>
# MAGIC <p>Starting configuration:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###B#C#B#D###
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>One Bronze amphipod moves into the hallway, taking 4 steps and using <code>40</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #...B.......#
# MAGIC ###B#C#.#D###
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>The only Copper amphipod not in its side room moves there, taking 4 steps and using <code>400</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #...B.......#
# MAGIC ###B#.#C#D###
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>A Desert amphipod moves out of the way, taking 3 steps and using <code>3000</code> energy, and then the Bronze amphipod takes its place, taking 3 steps and using <code>30</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #.....D.....#
# MAGIC ###B#.#C#D###
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>The leftmost Bronze amphipod moves to its room using <code>40</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #.....D.....#
# MAGIC ###.#B#C#D###
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>Both amphipods in the rightmost room move into the hallway, using <code>2003</code> energy in total:</p>
# MAGIC <pre><code>#############
# MAGIC #.....D.D.A.#
# MAGIC ###.#B#C#.###
# MAGIC   #A#B#C#.#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>Both Desert amphipods move into the rightmost room using <code>7000</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #.........A.#
# MAGIC ###.#B#C#D###
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>Finally, the last Amber amphipod moves into its room, using <code>8</code> energy:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###A#B#C#D###
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p><em>What is the least energy required to organize the amphipods?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''#############
#...........#
###C#B#A#D###
  #C#D#A#B#
  #########'''

# COMMAND ----------

import heapq

goals = {
  'A': 2,
  'B': 4,
  'C': 6,
  'D': 8
}


def is_solved(amphipods):
  return all(x == goals[letter] for (x, y), letter in amphipods.items())


def update_state(amphipod, move_to, energy, amphipods):
  (start_x, start_y), letter = amphipod
  x, y = start_x, start_y
  n_moves = 0
  
  # Go to hall
  while y != 0:
    y -= 1
    n_moves += 1
    if (x, y) in amphipods:
      return None
    
  # Go to x
  dx = 1 if x < move_to[0] else -1
  while x != move_to[0]:
    x += dx
    n_moves += 1
    if (x, y) in amphipods:
      return None
  
  # Go to room
  while y != move_to[1]:
    y += 1
    n_moves += 1
    if (x, y) in amphipods:
      return None
    
  amphipods = amphipods.copy()
  del amphipods[(start_x, start_y)]
  amphipods[(x, y)] = letter

  cost_per_move = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[letter]
  
  return (energy + cost_per_move * n_moves, tie_break(), amphipods)


def tie_break():
  tie_break.counter = getattr(tie_break, 'counter', 0) + 1
  return tie_break.counter


def smallest_energy_path(amphipods):
  rooms_y = sorted(set(y for _, y in amphipods))
  
  states = [(0, tie_break(), amphipods)]
  visited = set()

  while states:
    energy, _, amphipods = heapq.heappop(states)
    
    if is_solved(amphipods):
      return energy
    
    h = frozenset(amphipods.items())
    if h in visited:
      continue
    visited.add(h)

    # Find if any can move to their target room
    found_goal = False
    invalid_goals = {x for x in [2, 4, 6, 8] for y in rooms_y if (x, y) in amphipods and goals[amphipods[(x, y)]] != x}
    
    for (x, y), letter in amphipods.items():
      goal_x = goals[letter]
      if x == goal_x or goal_x in invalid_goals:
        continue
      
      goal_y = next(y for y in rooms_y[::-1] if (goal_x, y) not in amphipods)
      
      new_state = update_state(((x, y), letter), (goal_x, goal_y), energy, amphipods)
      if new_state:
        heapq.heappush(states, new_state)
        found_goal = True
    
    # Don't bother making other moves if you found a move to a room
    if found_goal:
      continue
      
    # Move from room to hallway
    available_squares = ((x, 0) for x in [0, 1, 3, 5, 7, 9, 10] if (x, 0) not in amphipods)
    for pos in available_squares:
      for (x, y), letter in amphipods.items():
        # Don't move from hallway
        if y == 0:
          continue

        new_state = update_state(((x, y), letter), pos, energy, amphipods)
        if new_state:
          heapq.heappush(states, new_state)

          
amphipods = {(x - 1, y - 1): letter for y, line in enumerate(inp.splitlines()) for x, letter in enumerate(line) if letter not in '.# '}

answer = smallest_energy_path(amphipods)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.</p>
# MAGIC <p>Between the first and second lines of text that contain amphipod starting positions, insert the following lines:</p>
# MAGIC <pre><code>  #D#C#B#A#
# MAGIC   #D#B#A#C#
# MAGIC </code></pre>
# MAGIC <p>So, the above example now becomes:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###B#C#B#D###
# MAGIC   <em>#D#C#B#A#
# MAGIC   #D#B#A#C#</em>
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>The amphipods still want to be organized into rooms similar to before:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###A#B#C#D###
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>In this updated example, the least energy required to organize these amphipods is <code><em>44169</em></code>:</p>
# MAGIC <pre><code>#############
# MAGIC #...........#
# MAGIC ###B#C#B#D###
# MAGIC   #D#C#B#A#
# MAGIC   #D#B#A#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #..........D#
# MAGIC ###B#C#B#.###
# MAGIC   #D#C#B#A#
# MAGIC   #D#B#A#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #A.........D#
# MAGIC ###B#C#B#.###
# MAGIC   #D#C#B#.#
# MAGIC   #D#B#A#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #A........BD#
# MAGIC ###B#C#.#.###
# MAGIC   #D#C#B#.#
# MAGIC   #D#B#A#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #A......B.BD#
# MAGIC ###B#C#.#.###
# MAGIC   #D#C#.#.#
# MAGIC   #D#B#A#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.....B.BD#
# MAGIC ###B#C#.#.###
# MAGIC   #D#C#.#.#
# MAGIC   #D#B#.#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.....B.BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#C#.#.#
# MAGIC   #D#B#C#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.....B.BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#.#C#.#
# MAGIC   #D#B#C#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA...B.B.BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#.#C#.#
# MAGIC   #D#.#C#C#
# MAGIC   #A#D#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D.B.B.BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#.#C#.#
# MAGIC   #D#.#C#C#
# MAGIC   #A#.#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D...B.BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#.#C#.#
# MAGIC   #D#.#C#C#
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D.....BD#
# MAGIC ###B#.#.#.###
# MAGIC   #D#.#C#.#
# MAGIC   #D#B#C#C#
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D......D#
# MAGIC ###B#.#.#.###
# MAGIC   #D#B#C#.#
# MAGIC   #D#B#C#C#
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D......D#
# MAGIC ###B#.#C#.###
# MAGIC   #D#B#C#.#
# MAGIC   #D#B#C#.#
# MAGIC   #A#B#C#A#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D.....AD#
# MAGIC ###B#.#C#.###
# MAGIC   #D#B#C#.#
# MAGIC   #D#B#C#.#
# MAGIC   #A#B#C#.#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.......AD#
# MAGIC ###B#.#C#.###
# MAGIC   #D#B#C#.#
# MAGIC   #D#B#C#.#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.......AD#
# MAGIC ###.#B#C#.###
# MAGIC   #D#B#C#.#
# MAGIC   #D#B#C#.#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.......AD#
# MAGIC ###.#B#C#.###
# MAGIC   #.#B#C#.#
# MAGIC   #D#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #AA.D.....AD#
# MAGIC ###.#B#C#.###
# MAGIC   #.#B#C#.#
# MAGIC   #.#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #A..D.....AD#
# MAGIC ###.#B#C#.###
# MAGIC   #.#B#C#.#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #...D.....AD#
# MAGIC ###.#B#C#.###
# MAGIC   #A#B#C#.#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #.........AD#
# MAGIC ###.#B#C#.###
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #..........D#
# MAGIC ###A#B#C#.###
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC 
# MAGIC #############
# MAGIC #...........#
# MAGIC ###A#B#C#D###
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #A#B#C#D#
# MAGIC   #########
# MAGIC </code></pre>
# MAGIC <p>Using the initial configuration from the full diagram, <em>what is the least energy required to organize the amphipods?</em></p>
# MAGIC </article>

# COMMAND ----------

extended_amphipods = {(x, y if y == 1 else 4): letter for (x, y), letter in amphipods.items()}
extended_amphipods.update({
  (2, 2): 'D',
  (2, 3): 'D',
  (4, 2): 'C',
  (4, 3): 'B',
  (6, 2): 'B',
  (6, 3): 'A',
  (8, 2): 'A',
  (8, 3): 'C'
})

answer = smallest_energy_path(extended_amphipods)
print(answer)
