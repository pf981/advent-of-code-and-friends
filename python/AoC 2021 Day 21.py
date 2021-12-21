# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 21: Dirac Dice ---</h2><p>There's not much to do as you slowly descend to the bottom of the ocean. The submarine computer <span title="A STRANGE GAME.">challenges you to a nice game</span> of <em>Dirac Dice</em>.</p>
# MAGIC <p>This game consists of a single <a href="https://en.wikipedia.org/wiki/Dice" target="_blank">die</a>, two <a href="https://en.wikipedia.org/wiki/Glossary_of_board_games#piece" target="_blank">pawns</a>, and a game board with a circular track containing ten spaces marked <code>1</code> through <code>10</code> clockwise. Each player's <em>starting space</em> is chosen randomly (your puzzle input). Player 1 goes first.</p>
# MAGIC <p>Players take turns moving. On each player's turn, the player rolls the die <em>three times</em> and adds up the results. Then, the player moves their pawn that many times <em>forward</em> around the track (that is, moving clockwise on spaces in order of increasing value, wrapping back around to <code>1</code> after <code>10</code>). So, if a player is on space <code>7</code> and they roll <code>2</code>, <code>2</code>, and <code>1</code>, they would move forward 5 times, to spaces <code>8</code>, <code>9</code>, <code>10</code>, <code>1</code>, and finally stopping on <code>2</code>.</p>
# MAGIC <p>After each player moves, they increase their <em>score</em> by the value of the space their pawn stopped on. Players' scores start at <code>0</code>. So, if the first player starts on space <code>7</code> and rolls a total of <code>5</code>, they would stop on space <code>2</code> and add <code>2</code> to their score (for a total score of <code>2</code>). The game immediately ends as a win for any player whose score reaches <em>at least <code>1000</code></em>.</p>
# MAGIC <p>Since the first game is a practice game, the submarine opens a compartment labeled <em>deterministic dice</em> and a 100-sided die falls out. This die always rolls <code>1</code> first, then <code>2</code>, then <code>3</code>, and so on up to <code>100</code>, after which it starts over at <code>1</code> again. Play using this die.</p>
# MAGIC <p>For example, given these starting positions:</p>
# MAGIC <pre><code>Player 1 starting position: 4
# MAGIC Player 2 starting position: 8
# MAGIC </code></pre>
# MAGIC <p>This is how the game would go:</p>
# MAGIC <ul>
# MAGIC <li>Player 1 rolls <code>1</code>+<code>2</code>+<code>3</code> and moves to space <code>10</code> for a total score of <code>10</code>.</li>
# MAGIC <li>Player 2 rolls <code>4</code>+<code>5</code>+<code>6</code> and moves to space <code>3</code> for a total score of <code>3</code>.</li>
# MAGIC <li>Player 1 rolls <code>7</code>+<code>8</code>+<code>9</code> and moves to space <code>4</code> for a total score of <code>14</code>.</li>
# MAGIC <li>Player 2 rolls <code>10</code>+<code>11</code>+<code>12</code> and moves to space <code>6</code> for a total score of <code>9</code>.</li>
# MAGIC <li>Player 1 rolls <code>13</code>+<code>14</code>+<code>15</code> and moves to space <code>6</code> for a total score of <code>20</code>.</li>
# MAGIC <li>Player 2 rolls <code>16</code>+<code>17</code>+<code>18</code> and moves to space <code>7</code> for a total score of <code>16</code>.</li>
# MAGIC <li>Player 1 rolls <code>19</code>+<code>20</code>+<code>21</code> and moves to space <code>6</code> for a total score of <code>26</code>.</li>
# MAGIC <li>Player 2 rolls <code>22</code>+<code>23</code>+<code>24</code> and moves to space <code>6</code> for a total score of <code>22</code>.</li>
# MAGIC </ul>
# MAGIC <p>...after many turns...</p>
# MAGIC <ul>
# MAGIC <li>Player 2 rolls <code>82</code>+<code>83</code>+<code>84</code> and moves to space <code>6</code> for a total score of <code>742</code>.</li>
# MAGIC <li>Player 1 rolls <code>85</code>+<code>86</code>+<code>87</code> and moves to space <code>4</code> for a total score of <code>990</code>.</li>
# MAGIC <li>Player 2 rolls <code>88</code>+<code>89</code>+<code>90</code> and moves to space <code>3</code> for a total score of <code>745</code>.</li>
# MAGIC <li>Player 1 rolls <code>91</code>+<code>92</code>+<code>93</code> and moves to space <code>10</code> for a final score, <code>1000</code>.</li>
# MAGIC </ul>
# MAGIC <p>Since player 1 has at least <code>1000</code> points, player 1 wins and the game ends. At this point, the losing player had <code>745</code> points and the die had been rolled a total of <code>993</code> times; <code>745 * 993 = <em>739785</em></code>.</p>
# MAGIC <p>Play a practice game using the deterministic 100-sided die. The moment either player wins, <em>what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Player 1 starting position: 6
Player 2 starting position: 4'''

# COMMAND ----------

def roll_three():
  result = 0
  for _ in range(3):
    roll_three.die += 1
    result += roll_three.die

  return result


def get_scores(p1, p2):
  p1_score = p2_score = 0
  while True:
    p1 = (p1 - 1 + roll_three()) % 10 + 1
    p1_score += p1
    if p1_score >= 1000:
      return p1_score, p2_score

    p2 = (p2 - 1 + roll_three()) % 10 + 1
    p2_score += p2
    if p2_score >= 1000:
      return p1_score, p2_score


roll_three.die = 0
p1_start, p2_start = (int(line[-1]) for line in inp.splitlines())
p1_score, p2_score = get_scores(p1_start, p2_start)

answer = min(p1_score, p2_score) * roll_three.die
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that you're warmed up, it's time to play the real game.</p>
# MAGIC <p>A second compartment opens, this time labeled <em>Dirac dice</em>. Out of it falls a single three-sided die.</p>
# MAGIC <p>As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a <em>quantum die</em>: when you roll it, the universe <em>splits into multiple copies</em>, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into <em>three copies</em>: one where the outcome of the roll was <code>1</code>, one where it was <code>2</code>, and one where it was <code>3</code>.</p>
# MAGIC <p>The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least <code><em>21</em></code>.</p>
# MAGIC <p>Using the same starting positions as in the example above, player 1 wins in <code><em>444356092776315</em></code> universes, while player 2 merely wins in <code>341960390180808</code> universes.</p>
# MAGIC <p>Using your given starting positions, determine every possible outcome. <em>Find the player that wins in more universes; in how many universes does that player win?</em></p>
# MAGIC </article>

# COMMAND ----------

import functools


@functools.lru_cache(maxsize=None)
def sum_wins(p1, p2, p1_score, p2_score, turn):
  if p1_score >= 21:
    return 1, 0
  elif p2_score >= 21:
    return 0, 1
  
  total1 = total2 = 0
  for roll1 in [1, 2, 3]:
      for roll2 in [1, 2, 3]:
          for roll3 in [1, 2, 3]:
            roll = roll1 + roll2 + roll3
            if turn == 1:
              new_p1 = (p1 - 1 + roll) % 10 + 1
              t1, t2 = sum_wins(new_p1, p2, p1_score + new_p1, p2_score, 2)
            else:
              new_p2 = (p2 - 1 + roll) % 10 + 1
              t1, t2 = sum_wins(p1, new_p2, p1_score, p2_score + new_p2, 1)
            total1 += t1
            total2 += t2
            
  return total1, total2


sum_wins.cache_clear()

answer = max(sum_wins(p1_start, p2_start, 0, 0, 1))
print(answer)
