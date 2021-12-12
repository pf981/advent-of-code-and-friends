# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 12: Passage Pathing ---</h2><p>With your <span title="Sublime.">submarine's subterranean subsystems subsisting suboptimally</span>, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just <em>a</em> path - the only way to know if you've found the <em>best</em> path is to find <em>all</em> of them.</p>
# MAGIC <p>Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:</p>
# MAGIC <pre><code>start-A
# MAGIC start-b
# MAGIC A-c
# MAGIC A-b
# MAGIC b-d
# MAGIC A-end
# MAGIC b-end
# MAGIC </code></pre>
# MAGIC <p>This is a list of how all of the caves are connected. You start in the cave named <code>start</code>, and your destination is the cave named <code>end</code>. An entry like <code>b-d</code> means that cave <code>b</code> is connected to cave <code>d</code> - that is, you can move between them.</p>
# MAGIC <p>So, the above cave system looks roughly like this:</p>
# MAGIC <pre><code>    start
# MAGIC     /   \
# MAGIC c--A-----b--d
# MAGIC     \   /
# MAGIC      end
# MAGIC </code></pre>
# MAGIC <p>Your goal is to find the number of distinct <em>paths</em> that start at <code>start</code>, end at <code>end</code>, and don't visit small caves more than once. There are two types of caves: <em>big</em> caves (written in uppercase, like <code>A</code>) and <em>small</em> caves (written in lowercase, like <code>b</code>). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should <em>visit small caves at most once</em>, and can <em>visit big caves any number of times</em>.</p>
# MAGIC <p>Given these rules, there are <code><em>10</em></code> paths through this example cave system:</p>
# MAGIC <pre><code>start,A,b,A,c,A,end
# MAGIC start,A,b,A,end
# MAGIC start,A,b,end
# MAGIC start,A,c,A,b,A,end
# MAGIC start,A,c,A,b,end
# MAGIC start,A,c,A,end
# MAGIC start,A,end
# MAGIC start,b,A,c,A,end
# MAGIC start,b,A,end
# MAGIC start,b,end
# MAGIC </code></pre>
# MAGIC <p>(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)</p>
# MAGIC <p>Note that in this cave system, cave <code>d</code> is never visited by any path: to do so, cave <code>b</code> would need to be visited twice (once on the way to cave <code>d</code> and a second time when returning from cave <code>d</code>), and since cave <code>b</code> is small, this is not allowed.</p>
# MAGIC <p>Here is a slightly larger example:</p>
# MAGIC <pre><code>dc-end
# MAGIC HN-start
# MAGIC start-kj
# MAGIC dc-start
# MAGIC dc-HN
# MAGIC LN-dc
# MAGIC HN-end
# MAGIC kj-sa
# MAGIC kj-HN
# MAGIC kj-dc
# MAGIC </code></pre>
# MAGIC <p>The <code>19</code> paths through it are as follows:</p>
# MAGIC <pre><code>start,HN,dc,HN,end
# MAGIC start,HN,dc,HN,kj,HN,end
# MAGIC start,HN,dc,end
# MAGIC start,HN,dc,kj,HN,end
# MAGIC start,HN,end
# MAGIC start,HN,kj,HN,dc,HN,end
# MAGIC start,HN,kj,HN,dc,end
# MAGIC start,HN,kj,HN,end
# MAGIC start,HN,kj,dc,HN,end
# MAGIC start,HN,kj,dc,end
# MAGIC start,dc,HN,end
# MAGIC start,dc,HN,kj,HN,end
# MAGIC start,dc,end
# MAGIC start,dc,kj,HN,end
# MAGIC start,kj,HN,dc,HN,end
# MAGIC start,kj,HN,dc,end
# MAGIC start,kj,HN,end
# MAGIC start,kj,dc,HN,end
# MAGIC start,kj,dc,end
# MAGIC </code></pre>
# MAGIC <p>Finally, this even larger example has <code>226</code> paths through it:</p>
# MAGIC <pre><code>fs-end
# MAGIC he-DX
# MAGIC fs-he
# MAGIC start-DX
# MAGIC pj-DX
# MAGIC end-zg
# MAGIC zg-sl
# MAGIC zg-pj
# MAGIC pj-he
# MAGIC RW-he
# MAGIC fs-DX
# MAGIC pj-RW
# MAGIC zg-RW
# MAGIC start-pj
# MAGIC he-WI
# MAGIC zg-he
# MAGIC pj-fs
# MAGIC start-RW
# MAGIC </code></pre>
# MAGIC <p><em>How many paths through this cave system are there that visit small caves at most once?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''DA-xn
KD-ut
gx-ll
dj-PW
xn-dj
ll-ut
xn-gx
dg-ak
DA-start
ut-gx
YM-ll
dj-DA
ll-xn
dj-YM
start-PW
dj-start
PW-gx
YM-gx
xn-ak
PW-ak
xn-PW
YM-end
end-ll
ak-end
ak-DA'''

# COMMAND ----------

import collections


def count_paths(edges, allow_small_cave_visited_twice=False):
  states = [(('start', ), collections.defaultdict(int))]
  full_paths = set()
  partial_paths = set()

  while states:
    path, node_counts = states.pop()
    node_counts = node_counts.copy()
    node = path[-1]
    
    if path in partial_paths:
      continue
    partial_paths.add(path)

    if node == 'end':
      full_paths.add(path)
      continue

    if node.islower():
      if not allow_small_cave_visited_twice and node_counts[node] == 1:
        continue
      if node_counts[node] == 2:
        continue
      if node_counts[node] == 1 and max(node_counts.values()) == 2:
        continue
      node_counts[node] += 1

    for new_node in edges[node]:
      if new_node != 'start':
        states.append((path + (new_node, ), node_counts))
      
  return len(full_paths)


edges = collections.defaultdict(list)
for line in inp.splitlines():
  a, b = line.split('-')
  edges[a].append(b)
  edges[b].append(a)

answer = count_paths(edges)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After reviewing the available paths, you realize you might have time to visit a single small cave <em>twice</em>. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named <code>start</code> and <code>end</code> can only be visited <em>exactly once each</em>: once you leave the <code>start</code> cave, you may not return to it, and once you reach the <code>end</code> cave, the path must end immediately.</p>
# MAGIC <p>Now, the <code>36</code> possible paths through the first example above are:</p>
# MAGIC <pre><code>start,A,b,A,b,A,c,A,end
# MAGIC start,A,b,A,b,A,end
# MAGIC start,A,b,A,b,end
# MAGIC start,A,b,A,c,A,b,A,end
# MAGIC start,A,b,A,c,A,b,end
# MAGIC start,A,b,A,c,A,c,A,end
# MAGIC start,A,b,A,c,A,end
# MAGIC start,A,b,A,end
# MAGIC start,A,b,d,b,A,c,A,end
# MAGIC start,A,b,d,b,A,end
# MAGIC start,A,b,d,b,end
# MAGIC start,A,b,end
# MAGIC start,A,c,A,b,A,b,A,end
# MAGIC start,A,c,A,b,A,b,end
# MAGIC start,A,c,A,b,A,c,A,end
# MAGIC start,A,c,A,b,A,end
# MAGIC start,A,c,A,b,d,b,A,end
# MAGIC start,A,c,A,b,d,b,end
# MAGIC start,A,c,A,b,end
# MAGIC start,A,c,A,c,A,b,A,end
# MAGIC start,A,c,A,c,A,b,end
# MAGIC start,A,c,A,c,A,end
# MAGIC start,A,c,A,end
# MAGIC start,A,end
# MAGIC start,b,A,b,A,c,A,end
# MAGIC start,b,A,b,A,end
# MAGIC start,b,A,b,end
# MAGIC start,b,A,c,A,b,A,end
# MAGIC start,b,A,c,A,b,end
# MAGIC start,b,A,c,A,c,A,end
# MAGIC start,b,A,c,A,end
# MAGIC start,b,A,end
# MAGIC start,b,d,b,A,c,A,end
# MAGIC start,b,d,b,A,end
# MAGIC start,b,d,b,end
# MAGIC start,b,end
# MAGIC </code></pre>
# MAGIC <p>The slightly larger example above now has <code>103</code> paths through it, and the even larger example now has <code>3509</code> paths through it.</p>
# MAGIC <p>Given these new rules, <em>how many paths through this cave system are there?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = count_paths(edges, True)
print(answer)
