# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/7

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 7: The Sum of Its Parts ---</h2><p>You find yourself standing on a snow-covered coastline; apparently, you landed a little off course.  The region is too hilly to see the North Pole from here, but you do spot some Elves that seem to be trying to unpack something that washed ashore. It's quite cold out, so you decide to risk creating a paradox by asking them for directions.</p>
# MAGIC <p>"Oh, are you the search party?" Somehow, you can understand whatever Elves from the year 1018 speak; you assume it's <a href="/2015/day/6">Ancient Nordic Elvish</a>. Could the device on your wrist also be a translator? "Those clothes don't look very warm; take this." They hand you a heavy coat.</p>
# MAGIC <p>"We do need to find our way back to the North Pole, but we have higher priorities at the moment. You see, believe it or not, this box contains something that will solve all of Santa's transportation problems - at least, that's what it looks like from the pictures in the instructions."  It doesn't seem like they can read whatever language it's in, but you can: "Sleigh kit. <span title="Just some oak and some pine and a handful of Norsemen.">Some assembly required.</span>"</p>
# MAGIC <p>"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at once!" They start excitedly pulling more parts out of the box.</p>
# MAGIC <p>The instructions specify a series of <em>steps</em> and requirements about which steps must be finished before others can begin (your puzzle input). Each step is designated by a single letter. For example, suppose you have the following instructions:</p>
# MAGIC <pre><code>Step C must be finished before step A can begin.
# MAGIC Step C must be finished before step F can begin.
# MAGIC Step A must be finished before step B can begin.
# MAGIC Step A must be finished before step D can begin.
# MAGIC Step B must be finished before step E can begin.
# MAGIC Step D must be finished before step E can begin.
# MAGIC Step F must be finished before step E can begin.
# MAGIC </code></pre>
# MAGIC <p>Visually, these requirements look like this:</p>
# MAGIC <pre><code>  --&gt;A---&gt;B--
# MAGIC  /    \      \
# MAGIC C      --&gt;D-----&gt;E
# MAGIC  \           /
# MAGIC   ----&gt;F-----
# MAGIC </code></pre>
# MAGIC <p>Your first goal is to determine the order in which the steps should be completed. If more than one step is ready, choose the step which is first alphabetically. In this example, the steps would be completed as follows:</p>
# MAGIC <ul>
# MAGIC <li>Only <em><code>C</code></em> is available, and so it is done first.</li>
# MAGIC <li>Next, both <code>A</code> and <code>F</code> are available. <em><code>A</code></em> is first alphabetically, so it is done next.</li>
# MAGIC <li>Then, even though <code>F</code> was available earlier, steps <code>B</code> and <code>D</code> are now also available, and <em><code>B</code></em> is the first alphabetically of the three.</li>
# MAGIC <li>After that, only <code>D</code> and <code>F</code> are available. <code>E</code> is not available because only some of its prerequisites are complete. Therefore, <em><code>D</code></em> is completed next.</li>
# MAGIC <li><em><code>F</code></em> is the only choice, so it is done next.</li>
# MAGIC <li>Finally, <em><code>E</code></em> is completed.</li>
# MAGIC </ul>
# MAGIC <p>So, in this example, the correct order is <em><code>CABDFE</code></em>.</p>
# MAGIC <p><em>In what order should the steps in your instructions be completed?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Step A must be finished before step L can begin.
Step B must be finished before step U can begin.
Step S must be finished before step K can begin.
Step L must be finished before step R can begin.
Step C must be finished before step I can begin.
Step F must be finished before step N can begin.
Step X must be finished before step H can begin.
Step Z must be finished before step U can begin.
Step P must be finished before step T can begin.
Step R must be finished before step U can begin.
Step H must be finished before step T can begin.
Step V must be finished before step G can begin.
Step E must be finished before step D can begin.
Step G must be finished before step W can begin.
Step N must be finished before step J can begin.
Step U must be finished before step D can begin.
Step Y must be finished before step K can begin.
Step K must be finished before step J can begin.
Step D must be finished before step M can begin.
Step I must be finished before step O can begin.
Step M must be finished before step Q can begin.
Step Q must be finished before step J can begin.
Step T must be finished before step J can begin.
Step W must be finished before step O can begin.
Step J must be finished before step O can begin.
Step C must be finished before step F can begin.
Step C must be finished before step J can begin.
Step Z must be finished before step I can begin.
Step K must be finished before step I can begin.
Step L must be finished before step W can begin.
Step I must be finished before step W can begin.
Step N must be finished before step O can begin.
Step B must be finished before step G can begin.
Step S must be finished before step O can begin.
Step P must be finished before step H can begin.
Step R must be finished before step J can begin.
Step N must be finished before step U can begin.
Step U must be finished before step J can begin.
Step E must be finished before step T can begin.
Step T must be finished before step O can begin.
Step L must be finished before step T can begin.
Step P must be finished before step Y can begin.
Step L must be finished before step C can begin.
Step D must be finished before step O can begin.
Step H must be finished before step Y can begin.
Step Q must be finished before step T can begin.
Step P must be finished before step G can begin.
Step G must be finished before step D can begin.
Step F must be finished before step H can begin.
Step G must be finished before step M can begin.
Step F must be finished before step V can begin.
Step X must be finished before step O can begin.
Step V must be finished before step Y can begin.
Step Y must be finished before step D can begin.
Step H must be finished before step G can begin.
Step A must be finished before step S can begin.
Step E must be finished before step U can begin.
Step Y must be finished before step O can begin.
Step C must be finished before step K can begin.
Step R must be finished before step W can begin.
Step G must be finished before step I can begin.
Step V must be finished before step E can begin.
Step V must be finished before step T can begin.
Step E must be finished before step K can begin.
Step X must be finished before step R can begin.
Step Q must be finished before step W can begin.
Step X must be finished before step P can begin.
Step K must be finished before step T can begin.
Step I must be finished before step T can begin.
Step P must be finished before step R can begin.
Step T must be finished before step W can begin.
Step X must be finished before step I can begin.
Step N must be finished before step Q can begin.
Step G must be finished before step Y can begin.
Step Y must be finished before step W can begin.
Step L must be finished before step D can begin.
Step F must be finished before step D can begin.
Step A must be finished before step T can begin.
Step R must be finished before step H can begin.
Step E must be finished before step I can begin.
Step W must be finished before step J can begin.
Step F must be finished before step M can begin.
Step V must be finished before step W can begin.
Step I must be finished before step J can begin.
Step Z must be finished before step P can begin.
Step H must be finished before step U can begin.
Step R must be finished before step V can begin.
Step V must be finished before step M can begin.
Step Y must be finished before step M can begin.
Step P must be finished before step M can begin.
Step K must be finished before step D can begin.
Step C must be finished before step T can begin.
Step Y must be finished before step T can begin.
Step U must be finished before step I can begin.
Step A must be finished before step O can begin.
Step E must be finished before step J can begin.
Step H must be finished before step V can begin.
Step F must be finished before step W can begin.
Step M must be finished before step T can begin.
Step S must be finished before step H can begin.
Step S must be finished before step G can begin.'''

# COMMAND ----------

import collections
import re
import string

def solve(remaining, dependencies):
  if len(remaining) == 1:
    return list(remaining)
  
  for s in remaining:
    if any(x in dependencies[s] for x in remaining):
      continue
    
    if (result := solve([x for x in remaining if x != s], dependencies)):
      return [s] + result
  return None

dependencies = collections.defaultdict(set)
for depends_on, step in (re.findall(r' ([A-Z]) ', line) for line in inp.splitlines()):
  dependencies[step].add(depends_on)

steps = solve(list(string.ascii_uppercase), dependencies)
  
answer = ''.join(steps)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you're about to begin construction, four of the Elves offer to help.  "The sun will set soon; it'll go faster if we work together."  Now, you need to account for multiple people working on steps simultaneously. If multiple steps are available, workers should still begin them in alphabetical order.</p>
# MAGIC <p>Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on. So, step A takes <code>60+1=61</code> seconds, while step Z takes <code>60+26=86</code> seconds. No time is required between steps.</p>
# MAGIC <p>To simplify things for the example, however, suppose you only have help from one Elf (a total of two workers) and that each step takes 60 fewer seconds (so that step A takes 1 second and step Z takes 26 seconds). Then, using the same instructions as above, this is how each second would be spent:</p>
# MAGIC <pre><code>Second   Worker 1   Worker 2   Done
# MAGIC    0        C          .        
# MAGIC    1        C          .        
# MAGIC    2        C          .        
# MAGIC    3        A          F       C
# MAGIC    4        B          F       CA
# MAGIC    5        B          F       CA
# MAGIC    6        D          F       CAB
# MAGIC    7        D          F       CAB
# MAGIC    8        D          F       CAB
# MAGIC    9        D          .       CABF
# MAGIC   10        E          .       CABFD
# MAGIC   11        E          .       CABFD
# MAGIC   12        E          .       CABFD
# MAGIC   13        E          .       CABFD
# MAGIC   14        E          .       CABFD
# MAGIC   15        .          .       CABFDE
# MAGIC </code></pre>
# MAGIC <p>Each row represents one second of time.  The Second column identifies how many seconds have passed as of the beginning of that second.  Each worker column shows the step that worker is currently doing (or <code>.</code> if they are idle).  The Done column shows completed steps.</p>
# MAGIC <p>Note that the order of the steps has changed; this is because steps now take time to finish and multiple workers can begin multiple steps simultaneously.</p>
# MAGIC <p>In this example, it would take <em>15</em> seconds for two workers to complete these steps.</p>
# MAGIC <p>With <em>5</em> workers and the <em>60+ second</em> step durations described above, <em>how long will it take to complete all of the steps?</em></p>
# MAGIC </article>

# COMMAND ----------

import itertools

def solve2(steps, dependencies):
  time_remaining = {step: 60 + i for i, step in enumerate(sorted(steps), 1)}
  for t in itertools.count(1):
    workers = list(itertools.islice((s for s in time_remaining if all(x not in dependencies[s] for x in time_remaining)), 5))
    
    for step in workers:
      time_remaining[step] -= 1
      if time_remaining[step] == 0:
        del time_remaining[step]
    
    if not time_remaining:
      break
  return t
  
solve2(steps, dependencies)
