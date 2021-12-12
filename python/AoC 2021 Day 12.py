# Databricks notebook source
# %pip install z3-solver

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

inp = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

# COMMAND ----------

edges = {}
for a, b in [line.split('-') for line in inp.splitlines()]:
  edges[a] = b
  edges[b] = a
edges

# COMMAND ----------

# edges = dict([line.split('-') for line in inp.splitlines()])
# edges

# COMMAND ----------

states = [('start', tuple())]
a, b = states.pop()
b

# COMMAND ----------

states = [('start', tuple(), set())]
paths = set()
done_paths = set()

while states:
  node, path, visited = states.pop()
  print(node)
  # print(node, path)
  
  new_path = path + tuple(node)
  
  if new_path in done_paths or node in visited:
    continue
  done_paths.add(new_path)
  if node.isupper():
    visied.add(node)
  
  
  if node == 'end':
    paths.add(new_path)
    continue
  
  for new_node in edges[node]:
    # if new_path + tuple(new_node) in done_paths:
    #   continue
    states.append((new_node, new_path))

# COMMAND ----------

(1,2) + (3,4)

# COMMAND ----------

a=[1,2]
a.append([3,4])
a
