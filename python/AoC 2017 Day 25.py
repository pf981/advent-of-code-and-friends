# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/25

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 25: The Halting Problem ---</h2><p>Following the twisty passageways deeper and deeper into the CPU, you finally reach the <span title="Get it? CPU core?">core</span> of the computer. Here, in the expansive central chamber, you find a grand apparatus that fills the entire room, suspended nanometers above your head.</p>
# MAGIC <p>You had always imagined CPUs to be noisy, chaotic places, bustling with activity. Instead, the room is quiet, motionless, and dark.</p>
# MAGIC <p>Suddenly, you and the CPU's <em>garbage collector</em> startle each other. "It's not often we get  many visitors here!", he says. You inquire about the stopped machinery.</p>
# MAGIC <p>"It stopped milliseconds ago; not sure why. I'm a garbage collector, not a doctor." You ask what the machine is for.</p>
# MAGIC <p>"Programs these days, don't know their origins. That's the <em>Turing machine</em>! It's what makes the whole computer work." You try to explain that Turing machines are merely models of computation, but he cuts you off. "No, see, that's just what they <em>want</em> you to think. Ultimately, inside every CPU, there's a Turing machine driving the whole thing! Too bad this one's broken. <a href="https://www.youtube.com/watch?v=cTwZZz0HV8I">We're doomed!</a>"</p>
# MAGIC <p>You ask how you can help. "Well, unfortunately, the only way to get the computer running again would be to create a whole new Turing machine from scratch, but there's no <em>way</em> you can-" He notices the look on your face, gives you a curious glance, shrugs, and goes back to sweeping the floor.</p>
# MAGIC <p>You find the <em>Turing machine blueprints</em> (your puzzle input) on a tablet in a nearby pile of debris. Looking back up at the broken Turing machine above, you can start to identify its parts:</p>
# MAGIC <ul>
# MAGIC <li>A <em>tape</em> which contains <code>0</code> repeated infinitely to the left and right.</li>
# MAGIC <li>A <em>cursor</em>, which can move left or right along the tape and read or write values at its current position.</li>
# MAGIC <li>A set of <em>states</em>, each containing rules about what to do based on the current value under the cursor.</li>
# MAGIC </ul>
# MAGIC <p>Each slot on the tape has two possible values: <code>0</code> (the starting value for all slots) and <code>1</code>. Based on whether the cursor is pointing at a <code>0</code> or a <code>1</code>, the current state says <em>what value to write</em> at the current position of the cursor, whether to <em>move the cursor</em> left or right one slot, and <em>which state to use next</em>.</p>
# MAGIC <p>For example, suppose you found the following blueprint:</p>
# MAGIC <pre><code>Begin in state A.
# MAGIC Perform a diagnostic checksum after 6 steps.
# MAGIC 
# MAGIC In state A:
# MAGIC   If the current value is 0:
# MAGIC     - Write the value 1.
# MAGIC     - Move one slot to the right.
# MAGIC     - Continue with state B.
# MAGIC   If the current value is 1:
# MAGIC     - Write the value 0.
# MAGIC     - Move one slot to the left.
# MAGIC     - Continue with state B.
# MAGIC 
# MAGIC In state B:
# MAGIC   If the current value is 0:
# MAGIC     - Write the value 1.
# MAGIC     - Move one slot to the left.
# MAGIC     - Continue with state A.
# MAGIC   If the current value is 1:
# MAGIC     - Write the value 1.
# MAGIC     - Move one slot to the right.
# MAGIC     - Continue with state A.
# MAGIC </code></pre>
# MAGIC <p>Running it until the number of steps required to take the listed <em>diagnostic checksum</em> would result in the following tape configurations (with the <em>cursor</em> marked in square brackets):</p>
# MAGIC <pre><code>... 0  0  0 [0] 0  0 ... (before any steps; about to run state A)
# MAGIC ... 0  0  0  1 [0] 0 ... (after 1 step;     about to run state B)
# MAGIC ... 0  0  0 [1] 1  0 ... (after 2 steps;    about to run state A)
# MAGIC ... 0  0 [0] 0  1  0 ... (after 3 steps;    about to run state B)
# MAGIC ... 0 [0] 1  0  1  0 ... (after 4 steps;    about to run state A)
# MAGIC ... 0  1 [1] 0  1  0 ... (after 5 steps;    about to run state B)
# MAGIC ... 0  1  1 [0] 1  0 ... (after 6 steps;    about to run state A)
# MAGIC </code></pre>
# MAGIC <p>The CPU can confirm that the Turing machine is working by taking a <em>diagnostic checksum</em> after a specific number of steps (given in the blueprint). Once the specified number of steps have been executed, the Turing machine should pause; once it does, count the number of times <code>1</code> appears on the tape. In the above example, the <em>diagnostic checksum</em> is <em><code>3</code></em>.</p>
# MAGIC <p>Recreate the Turing machine and save the computer! <em>What is the diagnostic checksum</em> it produces once it's working again?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''Begin in state A.
Perform a diagnostic checksum after 12523873 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state B.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.'''

# COMMAND ----------

import collections
import re

start_info, *states_info = inp.split('\n\n')
start_state = re.search(r'(\w)\.', start_info).group(1)
n_steps = int(re.search(r'\d+', start_info)[0])

states = {}
for state_info in states_info:
  state_name, _, write0, direction0, state0, _, write1, direction1, state1 = re.findall(r'(\w+)[\.:]', state_info)
  states[state_name] = {
    0: (int(write0), 1 if direction0 == 'right' else -1, state0),
    1: (int(write1), 1 if direction1 == 'right' else -1, state1)
  }


def solve(current_state, states, n_steps):
  tape = collections.defaultdict(int)
  cursor = 0
  
  for _ in range(n_steps):
    write, move, state = states[current_state][tape[cursor]]
    tape[cursor] = write
    cursor += move
    current_state = state
  
  return sum(tape.values())

answer = solve(start_state, states, n_steps)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Turing machine, and soon the entire computer, springs back to life.  A console glows dimly nearby, awaiting your command.</p>
# MAGIC <pre><code>&gt; reboot printer
# MAGIC Error: That command requires <em>priority 50</em>. You currently have <em>priority 0</em>.
# MAGIC You must deposit <em class="star">50 stars</em> to increase your priority to the required level.
# MAGIC </code></pre>
# MAGIC <p>The console flickers for a moment, and then prints another message:</p>
# MAGIC <pre><code><em class="star">Star</em> accepted.
# MAGIC You must deposit <em class="star">49 stars</em> to increase your priority to the required level.
# MAGIC </code></pre>
# MAGIC <p>The <em>garbage collector</em> winks at you, then continues sweeping.</p>
# MAGIC </article>

# COMMAND ----------

# No puzzle here - just need 49 stars.
