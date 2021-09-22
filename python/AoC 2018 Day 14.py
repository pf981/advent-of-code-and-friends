# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/14

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 14: Chocolate Charts ---</h2><p>You finally have a chance to look at all of the produce moving around. Chocolate, cinnamon, mint, chili peppers, nutmeg, vanilla... the Elves must be growing these plants to <span title="Please do not use a programming puzzle as a recipe for hot chocolate. I cannot guarantee your safety.">make</span> <em>hot chocolate</em>! As you realize this, you hear a conversation in the distance. When you go to investigate, you discover two Elves in what appears to be a makeshift underground kitchen/laboratory.</p>
# MAGIC <p>The Elves are trying to come up with the ultimate hot chocolate recipe; they're even maintaining a scoreboard which tracks the quality <em>score</em> (<code>0</code>-<code>9</code>) of each recipe.</p>
# MAGIC <p>Only two recipes are on the board: the first recipe got a score of <code>3</code>, the second, <code>7</code>. Each of the two Elves has a <em>current recipe</em>: the first Elf starts with the first recipe, and the second Elf starts with the second recipe.</p>
# MAGIC <p>To create new recipes, the two Elves combine their current recipes.  This creates new recipes from the <em>digits of the sum</em> of the current recipes' scores.  With the current recipes' scores of <code>3</code> and <code>7</code>, their sum is <code>10</code>, and so two new recipes would be created: the first with score <code>1</code> and the second with score <code>0</code>. If the current recipes' scores were <code>2</code> and <code>3</code>, the sum, <code>5</code>, would only create one recipe (with a score of <code>5</code>) with its single digit.</p>
# MAGIC <p>The new recipes are added to the end of the scoreboard in the order they are created.  So, after the first round, the scoreboard is <code>3, 7, 1, 0</code>.</p>
# MAGIC <p>After all new recipes are added to the scoreboard, each Elf picks a new current recipe.  To do this, the Elf steps forward through the scoreboard a number of recipes equal to <em>1 plus the score of their current recipe</em>. So, after the first round, the first Elf moves forward <code>1 + 3 = 4</code> times, while the second Elf moves forward <code>1 + 7 = 8</code> times. If they run out of recipes, they loop back around to the beginning. After the first round, both Elves happen to loop around until they land on the same recipe that they had in the beginning; in general, they will move to different recipes.</p>
# MAGIC <p>Drawing the first Elf as parentheses and the second Elf as square brackets, they continue this process:</p>
# MAGIC <pre><code>(3)[7]
# MAGIC (3)[7] 1  0 
# MAGIC  3  7  1 [0](1) 0 
# MAGIC  3  7  1  0 [1] 0 (1)
# MAGIC (3) 7  1  0  1  0 [1] 2 
# MAGIC  3  7  1  0 (1) 0  1  2 [4]
# MAGIC  3  7  1 [0] 1  0 (1) 2  4  5 
# MAGIC  3  7  1  0 [1] 0  1  2 (4) 5  1 
# MAGIC  3 (7) 1  0  1  0 [1] 2  4  5  1  5 
# MAGIC  3  7  1  0  1  0  1  2 [4](5) 1  5  8 
# MAGIC  3 (7) 1  0  1  0  1  2  4  5  1  5  8 [9]
# MAGIC  3  7  1  0  1  0  1 [2] 4 (5) 1  5  8  9  1  6 
# MAGIC  3  7  1  0  1  0  1  2  4  5 [1] 5  8  9  1 (6) 7 
# MAGIC  3  7  1  0 (1) 0  1  2  4  5  1  5 [8] 9  1  6  7  7 
# MAGIC  3  7 [1] 0  1  0 (1) 2  4  5  1  5  8  9  1  6  7  7  9 
# MAGIC  3  7  1  0 [1] 0  1  2 (4) <em>5  1  5  8  9  1  6  7  7  9</em>  2 
# MAGIC </code></pre>
# MAGIC <p>The Elves think their skill will improve after making a few recipes (your puzzle input). However, that could take ages; you can speed this up considerably by identifying <em>the scores of the ten recipes</em> after that.  For example:</p>
# MAGIC <ul>
# MAGIC <li>If the Elves think their skill will improve after making <code>9</code> recipes, the scores of the ten recipes <em>after</em> the first nine on the scoreboard would be <code>5158916779</code> (highlighted in the last line of the diagram).</li>
# MAGIC <li>After <code>5</code> recipes, the scores of the next ten would be <code>0124515891</code>.</li>
# MAGIC <li>After <code>18</code> recipes, the scores of the next ten would be <code>9251071085</code>.</li>
# MAGIC <li>After <code>2018</code> recipes, the scores of the next ten would be <code>5941429882</code>.</li>
# MAGIC </ul>
# MAGIC <p><em>What are the scores of the ten recipes immediately after the number of recipes in your puzzle input?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = 409551

# COMMAND ----------

import itertools

def get_scores(target_score):
  target_score = str(target_score)
  scores = '37'
  elf1_i = 0
  elf2_i = 1
  
  for n in itertools.count():
    for i in range(2 ** n):
      elf1_val = int(scores[elf1_i])
      elf2_val = int(scores[elf2_i])

      scores += str(elf1_val + elf2_val)

      elf1_i = (elf1_i +  elf1_val + 1) % len(scores)
      elf2_i = (elf2_i +  elf2_val + 1) % len(scores)
      
    if target_score in scores:
      return scores
  
scores = get_scores(inp)
  
answer = scores[inp:inp+10]
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As it turns out, you got the Elves' plan backwards.  They actually want to know how many recipes appear on the scoreboard to the left of the first recipes whose scores are the digits from your puzzle input.</p>
# MAGIC <ul>
# MAGIC <li><code>51589</code> first appears after <code>9</code> recipes.</li>
# MAGIC <li><code>01245</code> first appears after <code>5</code> recipes.</li>
# MAGIC <li><code>92510</code> first appears after <code>18</code> recipes.</li>
# MAGIC <li><code>59414</code> first appears after <code>2018</code> recipes.</li>
# MAGIC </ul>
# MAGIC <p><em>How many recipes appear on the scoreboard to the left of the score sequence in your puzzle input?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = scores.index(str(inp))
print(answer)
