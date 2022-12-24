# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Crab Combat ---</h2><p>It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of <a href="/2019/day/22">space cards</a>! You'd like to play a game of <em>Combat</em>, and there's even an opponent available: a small crab that climbed aboard your raft before you left.</p>
# MAGIC <p>Fortunately, it doesn't take long to teach the crab the rules.</p>
# MAGIC <p>Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of <em>rounds</em>: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.</p>
# MAGIC <p>For example, consider the following starting decks:</p>
# MAGIC <pre><code>Player 1:
# MAGIC 9
# MAGIC 2
# MAGIC 6
# MAGIC 3
# MAGIC 1
# MAGIC 
# MAGIC Player 2:
# MAGIC 5
# MAGIC 8
# MAGIC 4
# MAGIC 7
# MAGIC 10
# MAGIC </code></pre>
# MAGIC <p>This arrangement means that player 1's deck contains 5 cards, with <code>9</code> on top and <code>1</code> on the bottom; player 2's deck also contains 5 cards, with <code>5</code> on top and <code>10</code> on the bottom.</p>
# MAGIC <p>The first round begins with both players drawing the top card of their decks: <code>9</code> and <code>5</code>. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that <code>9</code> is above <code>5</code>. In total, it takes 29 rounds before a player has all of the cards:</p>
# MAGIC <pre><code>-- Round 1 --
# MAGIC Player 1's deck: 9, 2, 6, 3, 1
# MAGIC Player 2's deck: 5, 8, 4, 7, 10
# MAGIC Player 1 plays: 9
# MAGIC Player 2 plays: 5
# MAGIC Player 1 wins the round!
# MAGIC 
# MAGIC -- Round 2 --
# MAGIC Player 1's deck: 2, 6, 3, 1, 9, 5
# MAGIC Player 2's deck: 8, 4, 7, 10
# MAGIC Player 1 plays: 2
# MAGIC Player 2 plays: 8
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC -- Round 3 --
# MAGIC Player 1's deck: 6, 3, 1, 9, 5
# MAGIC Player 2's deck: 4, 7, 10, 8, 2
# MAGIC Player 1 plays: 6
# MAGIC Player 2 plays: 4
# MAGIC Player 1 wins the round!
# MAGIC 
# MAGIC -- Round 4 --
# MAGIC Player 1's deck: 3, 1, 9, 5, 6, 4
# MAGIC Player 2's deck: 7, 10, 8, 2
# MAGIC Player 1 plays: 3
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC -- Round 5 --
# MAGIC Player 1's deck: 1, 9, 5, 6, 4
# MAGIC Player 2's deck: 10, 8, 2, 7, 3
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC ...several more rounds pass...
# MAGIC 
# MAGIC -- Round 27 --
# MAGIC Player 1's deck: 5, 4, 1
# MAGIC Player 2's deck: 8, 9, 7, 3, 2, 10, 6
# MAGIC Player 1 plays: 5
# MAGIC Player 2 plays: 8
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC -- Round 28 --
# MAGIC Player 1's deck: 4, 1
# MAGIC Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
# MAGIC Player 1 plays: 4
# MAGIC Player 2 plays: 9
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC -- Round 29 --
# MAGIC Player 1's deck: 1
# MAGIC Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins the round!
# MAGIC 
# MAGIC 
# MAGIC == Post-game results ==
# MAGIC Player 1's deck: 
# MAGIC Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
# MAGIC </code></pre>
# MAGIC <p>Once the game ends, you can calculate the winning player's <em>score</em>. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:</p>
# MAGIC <pre><code>   3 * 10
# MAGIC +  2 *  9
# MAGIC + 10 *  8
# MAGIC +  6 *  7
# MAGIC +  8 *  6
# MAGIC +  5 *  5
# MAGIC +  9 *  4
# MAGIC +  4 *  3
# MAGIC +  7 *  2
# MAGIC +  1 *  1
# MAGIC = 306
# MAGIC </code></pre>
# MAGIC <p>So, once the game ends, the winning player's score is <em><code>306</code></em>.</p>
# MAGIC <p>Play the small crab in a game of Combat using the two decks you just dealt. <em>What is the winning player's score?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''Player 1:
43
36
13
11
20
25
37
38
4
18
1
8
27
23
7
22
10
5
50
40
45
26
15
32
33

Player 2:
21
29
12
28
46
9
44
6
16
39
19
24
17
14
47
48
42
34
31
3
41
35
2
30
49'''

# COMMAND ----------

import collections


def get_score(players):
  return sum(multiplier * card for multiplier, card in enumerate(reversed(players[0] or players[1]), 1))


players_start = tuple(tuple(int(x) for x in player.splitlines()[1:]) for player in inp.split('\n\n'))

players = [collections.deque(player) for player in players_start]
while players[0] and players[1]:
  cards = [player.popleft() for player in players]
  players[cards[1] > cards[0]].extend(sorted(cards, reverse=True))

answer = get_score(players)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of <em><span title="For some reason, nobody wants to play Recursive Twilight Imperium with me.">Recursive</span> Combat</em>.</p>
# MAGIC <p>Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of <em>rounds</em> with a few changes:</p>
# MAGIC <ul>
# MAGIC <li>Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the <em>game</em> instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)</li>
# MAGIC <li>Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.</li>
# MAGIC <li>If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).</li>
# MAGIC <li>Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.</li>
# MAGIC </ul>
# MAGIC <p>As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be <em>the lower-valued of the two cards</em> if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.</p>
# MAGIC <p>Here is an example of a small game that would loop forever without the infinite game prevention rule:</p>
# MAGIC <pre><code>Player 1:
# MAGIC 43
# MAGIC 19
# MAGIC 
# MAGIC Player 2:
# MAGIC 2
# MAGIC 29
# MAGIC 14
# MAGIC </code></pre>
# MAGIC <p>During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the <code>3</code> card, and player 2 draws the <code>7</code> card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the <code>3</code> and <code>7</code> cards that were drawn.)</p>
# MAGIC <p>To play a sub-game of Recursive Combat, each player creates a new deck by making a <em>copy</em> of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the <code>3</code> card, their deck in the sub-game would be <em>copies</em> of the next three cards in their deck.)</p>
# MAGIC <p>Here is a complete example of gameplay, where <code>Game 1</code> is the primary game of Recursive Combat:</p>
# MAGIC <pre><code>=== Game 1 ===
# MAGIC 
# MAGIC -- Round 1 (Game 1) --
# MAGIC Player 1's deck: 9, 2, 6, 3, 1
# MAGIC Player 2's deck: 5, 8, 4, 7, 10
# MAGIC Player 1 plays: 9
# MAGIC Player 2 plays: 5
# MAGIC Player 1 wins round 1 of game 1!
# MAGIC 
# MAGIC -- Round 2 (Game 1) --
# MAGIC Player 1's deck: 2, 6, 3, 1, 9, 5
# MAGIC Player 2's deck: 8, 4, 7, 10
# MAGIC Player 1 plays: 2
# MAGIC Player 2 plays: 8
# MAGIC Player 2 wins round 2 of game 1!
# MAGIC 
# MAGIC -- Round 3 (Game 1) --
# MAGIC Player 1's deck: 6, 3, 1, 9, 5
# MAGIC Player 2's deck: 4, 7, 10, 8, 2
# MAGIC Player 1 plays: 6
# MAGIC Player 2 plays: 4
# MAGIC Player 1 wins round 3 of game 1!
# MAGIC 
# MAGIC -- Round 4 (Game 1) --
# MAGIC Player 1's deck: 3, 1, 9, 5, 6, 4
# MAGIC Player 2's deck: 7, 10, 8, 2
# MAGIC Player 1 plays: 3
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins round 4 of game 1!
# MAGIC 
# MAGIC -- Round 5 (Game 1) --
# MAGIC Player 1's deck: 1, 9, 5, 6, 4
# MAGIC Player 2's deck: 10, 8, 2, 7, 3
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 5 of game 1!
# MAGIC 
# MAGIC -- Round 6 (Game 1) --
# MAGIC Player 1's deck: 9, 5, 6, 4
# MAGIC Player 2's deck: 8, 2, 7, 3, 10, 1
# MAGIC Player 1 plays: 9
# MAGIC Player 2 plays: 8
# MAGIC Player 1 wins round 6 of game 1!
# MAGIC 
# MAGIC -- Round 7 (Game 1) --
# MAGIC Player 1's deck: 5, 6, 4, 9, 8
# MAGIC Player 2's deck: 2, 7, 3, 10, 1
# MAGIC Player 1 plays: 5
# MAGIC Player 2 plays: 2
# MAGIC Player 1 wins round 7 of game 1!
# MAGIC 
# MAGIC -- Round 8 (Game 1) --
# MAGIC Player 1's deck: 6, 4, 9, 8, 5, 2
# MAGIC Player 2's deck: 7, 3, 10, 1
# MAGIC Player 1 plays: 6
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins round 8 of game 1!
# MAGIC 
# MAGIC -- Round 9 (Game 1) --
# MAGIC Player 1's deck: 4, 9, 8, 5, 2
# MAGIC Player 2's deck: 3, 10, 1, 7, 6
# MAGIC Player 1 plays: 4
# MAGIC Player 2 plays: 3
# MAGIC Playing a sub-game to determine the winner...
# MAGIC 
# MAGIC === Game 2 ===
# MAGIC 
# MAGIC -- Round 1 (Game 2) --
# MAGIC Player 1's deck: 9, 8, 5, 2
# MAGIC Player 2's deck: 10, 1, 7
# MAGIC Player 1 plays: 9
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 1 of game 2!
# MAGIC 
# MAGIC -- Round 2 (Game 2) --
# MAGIC Player 1's deck: 8, 5, 2
# MAGIC Player 2's deck: 1, 7, 10, 9
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 1
# MAGIC Player 1 wins round 2 of game 2!
# MAGIC 
# MAGIC -- Round 3 (Game 2) --
# MAGIC Player 1's deck: 5, 2, 8, 1
# MAGIC Player 2's deck: 7, 10, 9
# MAGIC Player 1 plays: 5
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins round 3 of game 2!
# MAGIC 
# MAGIC -- Round 4 (Game 2) --
# MAGIC Player 1's deck: 2, 8, 1
# MAGIC Player 2's deck: 10, 9, 7, 5
# MAGIC Player 1 plays: 2
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 4 of game 2!
# MAGIC 
# MAGIC -- Round 5 (Game 2) --
# MAGIC Player 1's deck: 8, 1
# MAGIC Player 2's deck: 9, 7, 5, 10, 2
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 9
# MAGIC Player 2 wins round 5 of game 2!
# MAGIC 
# MAGIC -- Round 6 (Game 2) --
# MAGIC Player 1's deck: 1
# MAGIC Player 2's deck: 7, 5, 10, 2, 9, 8
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins round 6 of game 2!
# MAGIC The winner of game 2 is player 2!
# MAGIC 
# MAGIC ...anyway, back to game 1.
# MAGIC Player 2 wins round 9 of game 1!
# MAGIC 
# MAGIC -- Round 10 (Game 1) --
# MAGIC Player 1's deck: 9, 8, 5, 2
# MAGIC Player 2's deck: 10, 1, 7, 6, 3, 4
# MAGIC Player 1 plays: 9
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 10 of game 1!
# MAGIC 
# MAGIC -- Round 11 (Game 1) --
# MAGIC Player 1's deck: 8, 5, 2
# MAGIC Player 2's deck: 1, 7, 6, 3, 4, 10, 9
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 1
# MAGIC Player 1 wins round 11 of game 1!
# MAGIC 
# MAGIC -- Round 12 (Game 1) --
# MAGIC Player 1's deck: 5, 2, 8, 1
# MAGIC Player 2's deck: 7, 6, 3, 4, 10, 9
# MAGIC Player 1 plays: 5
# MAGIC Player 2 plays: 7
# MAGIC Player 2 wins round 12 of game 1!
# MAGIC 
# MAGIC -- Round 13 (Game 1) --
# MAGIC Player 1's deck: 2, 8, 1
# MAGIC Player 2's deck: 6, 3, 4, 10, 9, 7, 5
# MAGIC Player 1 plays: 2
# MAGIC Player 2 plays: 6
# MAGIC Playing a sub-game to determine the winner...
# MAGIC 
# MAGIC === Game 3 ===
# MAGIC 
# MAGIC -- Round 1 (Game 3) --
# MAGIC Player 1's deck: 8, 1
# MAGIC Player 2's deck: 3, 4, 10, 9, 7, 5
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 3
# MAGIC Player 1 wins round 1 of game 3!
# MAGIC 
# MAGIC -- Round 2 (Game 3) --
# MAGIC Player 1's deck: 1, 8, 3
# MAGIC Player 2's deck: 4, 10, 9, 7, 5
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 4
# MAGIC Playing a sub-game to determine the winner...
# MAGIC 
# MAGIC === Game 4 ===
# MAGIC 
# MAGIC -- Round 1 (Game 4) --
# MAGIC Player 1's deck: 8
# MAGIC Player 2's deck: 10, 9, 7, 5
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 1 of game 4!
# MAGIC The winner of game 4 is player 2!
# MAGIC 
# MAGIC ...anyway, back to game 3.
# MAGIC Player 2 wins round 2 of game 3!
# MAGIC 
# MAGIC -- Round 3 (Game 3) --
# MAGIC Player 1's deck: 8, 3
# MAGIC Player 2's deck: 10, 9, 7, 5, 4, 1
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 3 of game 3!
# MAGIC 
# MAGIC -- Round 4 (Game 3) --
# MAGIC Player 1's deck: 3
# MAGIC Player 2's deck: 9, 7, 5, 4, 1, 10, 8
# MAGIC Player 1 plays: 3
# MAGIC Player 2 plays: 9
# MAGIC Player 2 wins round 4 of game 3!
# MAGIC The winner of game 3 is player 2!
# MAGIC 
# MAGIC ...anyway, back to game 1.
# MAGIC Player 2 wins round 13 of game 1!
# MAGIC 
# MAGIC -- Round 14 (Game 1) --
# MAGIC Player 1's deck: 8, 1
# MAGIC Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 3
# MAGIC Player 1 wins round 14 of game 1!
# MAGIC 
# MAGIC -- Round 15 (Game 1) --
# MAGIC Player 1's deck: 1, 8, 3
# MAGIC Player 2's deck: 4, 10, 9, 7, 5, 6, 2
# MAGIC Player 1 plays: 1
# MAGIC Player 2 plays: 4
# MAGIC Playing a sub-game to determine the winner...
# MAGIC 
# MAGIC === Game 5 ===
# MAGIC 
# MAGIC -- Round 1 (Game 5) --
# MAGIC Player 1's deck: 8
# MAGIC Player 2's deck: 10, 9, 7, 5
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 1 of game 5!
# MAGIC The winner of game 5 is player 2!
# MAGIC 
# MAGIC ...anyway, back to game 1.
# MAGIC Player 2 wins round 15 of game 1!
# MAGIC 
# MAGIC -- Round 16 (Game 1) --
# MAGIC Player 1's deck: 8, 3
# MAGIC Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
# MAGIC Player 1 plays: 8
# MAGIC Player 2 plays: 10
# MAGIC Player 2 wins round 16 of game 1!
# MAGIC 
# MAGIC -- Round 17 (Game 1) --
# MAGIC Player 1's deck: 3
# MAGIC Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
# MAGIC Player 1 plays: 3
# MAGIC Player 2 plays: 9
# MAGIC Player 2 wins round 17 of game 1!
# MAGIC The winner of game 1 is player 2!
# MAGIC 
# MAGIC 
# MAGIC == Post-game results ==
# MAGIC Player 1's deck: 
# MAGIC Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3
# MAGIC </code></pre>
# MAGIC <p>After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is <em><code>291</code></em>.</p>
# MAGIC <p>Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. <em>What is the winning player's score?</em></p>
# MAGIC </article>

# COMMAND ----------

def get_round_winner(players):
  if all(len(cards) >= top for top, *cards in players):
    players = play_game((players[0][1:players[0][0] + 1], players[1][1:players[1][0] + 1]))
    return int(bool(players[1]))

  return players[1][0] > players[0][0]


def simulate_round(players):
  round_winner = get_round_winner(players)
  if round_winner == 0:
    return (players[0][1:] + (players[0][0], players[1][0]), players[1][1:])
  return (players[0][1:], players[1][1:] + (players[1][0], players[0][0]))


def play_game(players):
  seen = set()
  while players[0] and players[1]:
    if players in seen:
      return (players[0], tuple())
    seen.add(players)

    players = simulate_round(players)
  return players


players = play_game(players_start)

answer = get_score(players)
print(answer) # 4 seconds
