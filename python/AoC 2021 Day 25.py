# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 25: Sea Cucumber ---</h2><p>This is it: the bottom of the ocean trench, the last place the sleigh keys could be. Your submarine's experimental antenna <em>still isn't boosted enough</em> to detect the keys, but they <em>must</em> be here. All you need to do is <em>reach the seafloor</em> and find them.</p>
# MAGIC <p>At least, you'd touch down on the seafloor if you could; unfortunately, it's completely covered by two large herds of <a href="https://en.wikipedia.org/wiki/Sea_cucumber" target="_blank">sea cucumbers</a>, and there isn't an open space large enough for your submarine.</p>
# MAGIC <p>You suspect that the Elves must have done this before, because just then you discover the phone number of a deep-sea marine biologist on a handwritten note taped to the wall of the submarine's cockpit.</p>
# MAGIC <p>"Sea cucumbers? Yeah, they're probably hunting for food. But don't worry, they're predictable critters: they move in perfectly straight lines, only moving forward when there's space to do so. They're actually quite polite!"</p>
# MAGIC <p>You explain that you'd like to predict when you could land your submarine.</p>
# MAGIC <p>"Oh that's easy, they'll eventually pile up and leave enough space for-- wait, did you say submarine? And the only place with that many sea cucumbers would be at the very bottom of the Mariana--" You hang up the phone.</p>
# MAGIC <p>There are two herds of sea cucumbers sharing the same region; one always moves <em>east</em> (<code>&gt;</code>), while the other always moves <em>south</em> (<code>v</code>). Each location can contain at most one sea cucumber; the remaining locations are <em>empty</em> (<code>.</code>). The submarine helpfully generates a map of the situation (your puzzle input). For example:</p>
# MAGIC <pre><code>v...&gt;&gt;.vv&gt;
# MAGIC .vv&gt;&gt;.vv..
# MAGIC &gt;&gt;.&gt;v&gt;...v
# MAGIC &gt;&gt;v&gt;&gt;.&gt;.v.
# MAGIC v&gt;v.vv.v..
# MAGIC &gt;.&gt;&gt;..v...
# MAGIC .vv..&gt;.&gt;v.
# MAGIC v.v..&gt;&gt;v.v
# MAGIC ....v..v.&gt;
# MAGIC </code></pre>
# MAGIC <p>Every <em>step</em>, the sea cucumbers in the east-facing herd attempt to move forward one location, then the sea cucumbers in the south-facing herd attempt to move forward one location. When a herd moves forward, every sea cucumber in the herd first simultaneously considers whether there is a sea cucumber in the adjacent location it's facing (even another sea cucumber facing the same direction), and then every sea cucumber facing an empty location simultaneously moves into that location.</p>
# MAGIC <p>So, in a situation like this:</p>
# MAGIC <pre><code>...&gt;&gt;&gt;&gt;&gt;...</code></pre>
# MAGIC <p>After one step, only the rightmost sea cucumber would have moved:</p>
# MAGIC <pre><code>...&gt;&gt;&gt;&gt;.&gt;..</code></pre>
# MAGIC <p>After the next step, two sea cucumbers move:</p>
# MAGIC <pre><code>...&gt;&gt;&gt;.&gt;.&gt;.</code></pre>
# MAGIC <p>During a single step, the east-facing herd moves first, then the south-facing herd moves. So, given this situation:</p>
# MAGIC <pre><code>..........
# MAGIC .&gt;v....v..
# MAGIC .......&gt;..
# MAGIC ..........
# MAGIC </code></pre>
# MAGIC <p>After a single step, of the sea cucumbers on the left, only the south-facing sea cucumber has moved (as it wasn't out of the way in time for the east-facing cucumber on the left to move), but both sea cucumbers on the right have moved (as the east-facing sea cucumber moved out of the way of the south-facing sea cucumber):</p>
# MAGIC <pre><code>..........
# MAGIC .&gt;........
# MAGIC ..v....v&gt;.
# MAGIC ..........
# MAGIC </code></pre>
# MAGIC <p>Due to <em>strong water currents</em> in the area, sea cucumbers that move off the right edge of the map appear on the left edge, and sea cucumbers that move off the bottom edge of the map appear on the top edge. Sea cucumbers always check whether their destination location is empty before moving, even if that destination is on the opposite side of the map:</p>
# MAGIC <pre><code>Initial state:
# MAGIC ...&gt;...
# MAGIC .......
# MAGIC ......&gt;
# MAGIC v.....&gt;
# MAGIC ......&gt;
# MAGIC .......
# MAGIC ..vvv..
# MAGIC 
# MAGIC After 1 step:
# MAGIC ..vv&gt;..
# MAGIC .......
# MAGIC &gt;......
# MAGIC v.....&gt;
# MAGIC &gt;......
# MAGIC .......
# MAGIC ....v..
# MAGIC 
# MAGIC After 2 steps:
# MAGIC ....v&gt;.
# MAGIC ..vv...
# MAGIC .&gt;.....
# MAGIC ......&gt;
# MAGIC v&gt;.....
# MAGIC .......
# MAGIC .......
# MAGIC 
# MAGIC After 3 steps:
# MAGIC ......&gt;
# MAGIC ..v.v..
# MAGIC ..&gt;v...
# MAGIC &gt;......
# MAGIC ..&gt;....
# MAGIC v......
# MAGIC .......
# MAGIC 
# MAGIC After 4 steps:
# MAGIC &gt;......
# MAGIC ..v....
# MAGIC ..&gt;.v..
# MAGIC .&gt;.v...
# MAGIC ...&gt;...
# MAGIC .......
# MAGIC v......
# MAGIC </code></pre>
# MAGIC <p>To find a safe place to land your submarine, the sea cucumbers need to stop moving. Again consider the first example:</p>
# MAGIC <pre><code>Initial state:
# MAGIC v...&gt;&gt;.vv&gt;
# MAGIC .vv&gt;&gt;.vv..
# MAGIC &gt;&gt;.&gt;v&gt;...v
# MAGIC &gt;&gt;v&gt;&gt;.&gt;.v.
# MAGIC v&gt;v.vv.v..
# MAGIC &gt;.&gt;&gt;..v...
# MAGIC .vv..&gt;.&gt;v.
# MAGIC v.v..&gt;&gt;v.v
# MAGIC ....v..v.&gt;
# MAGIC 
# MAGIC After 1 step:
# MAGIC ....&gt;.&gt;v.&gt;
# MAGIC v.v&gt;.&gt;v.v.
# MAGIC &gt;v&gt;&gt;..&gt;v..
# MAGIC &gt;&gt;v&gt;v&gt;.&gt;.v
# MAGIC .&gt;v.v...v.
# MAGIC v&gt;&gt;.&gt;vvv..
# MAGIC ..v...&gt;&gt;..
# MAGIC vv...&gt;&gt;vv.
# MAGIC &gt;.v.v..v.v
# MAGIC 
# MAGIC After 2 steps:
# MAGIC &gt;.v.v&gt;&gt;..v
# MAGIC v.v.&gt;&gt;vv..
# MAGIC &gt;v&gt;.&gt;.&gt;.v.
# MAGIC &gt;&gt;v&gt;v.&gt;v&gt;.
# MAGIC .&gt;..v....v
# MAGIC .&gt;v&gt;&gt;.v.v.
# MAGIC v....v&gt;v&gt;.
# MAGIC .vv..&gt;&gt;v..
# MAGIC v&gt;.....vv.
# MAGIC 
# MAGIC After 3 steps:
# MAGIC v&gt;v.v&gt;.&gt;v.
# MAGIC v...&gt;&gt;.v.v
# MAGIC &gt;vv&gt;.&gt;v&gt;..
# MAGIC &gt;&gt;v&gt;v.&gt;.v&gt;
# MAGIC ..&gt;....v..
# MAGIC .&gt;.&gt;v&gt;v..v
# MAGIC ..v..v&gt;vv&gt;
# MAGIC v.v..&gt;&gt;v..
# MAGIC .v&gt;....v..
# MAGIC 
# MAGIC After 4 steps:
# MAGIC v&gt;..v.&gt;&gt;..
# MAGIC v.v.&gt;.&gt;.v.
# MAGIC &gt;vv.&gt;&gt;.v&gt;v
# MAGIC &gt;&gt;.&gt;..v&gt;.&gt;
# MAGIC ..v&gt;v...v.
# MAGIC ..&gt;&gt;.&gt;vv..
# MAGIC &gt;.v.vv&gt;v.v
# MAGIC .....&gt;&gt;vv.
# MAGIC vvv&gt;...v..
# MAGIC 
# MAGIC After 5 steps:
# MAGIC vv&gt;...&gt;v&gt;.
# MAGIC v.v.v&gt;.&gt;v.
# MAGIC &gt;.v.&gt;.&gt;.&gt;v
# MAGIC &gt;v&gt;.&gt;..v&gt;&gt;
# MAGIC ..v&gt;v.v...
# MAGIC ..&gt;.&gt;&gt;vvv.
# MAGIC .&gt;...v&gt;v..
# MAGIC ..v.v&gt;&gt;v.v
# MAGIC v.v.&gt;...v.
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 10 steps:
# MAGIC ..&gt;..&gt;&gt;vv.
# MAGIC v.....&gt;&gt;.v
# MAGIC ..v.v&gt;&gt;&gt;v&gt;
# MAGIC v&gt;.&gt;v.&gt;&gt;&gt;.
# MAGIC ..v&gt;v.vv.v
# MAGIC .v.&gt;&gt;&gt;.v..
# MAGIC v.v..&gt;v&gt;..
# MAGIC ..v...&gt;v.&gt;
# MAGIC .vv..v&gt;vv.
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 20 steps:
# MAGIC v&gt;.....&gt;&gt;.
# MAGIC &gt;vv&gt;.....v
# MAGIC .&gt;v&gt;v.vv&gt;&gt;
# MAGIC v&gt;&gt;&gt;v.&gt;v.&gt;
# MAGIC ....vv&gt;v..
# MAGIC .v.&gt;&gt;&gt;vvv.
# MAGIC ..v..&gt;&gt;vv.
# MAGIC v.v...&gt;&gt;.v
# MAGIC ..v.....v&gt;
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 30 steps:
# MAGIC .vv.v..&gt;&gt;&gt;
# MAGIC v&gt;...v...&gt;
# MAGIC &gt;.v&gt;.&gt;vv.&gt;
# MAGIC &gt;v&gt;.&gt;.&gt;v.&gt;
# MAGIC .&gt;..v.vv..
# MAGIC ..v&gt;..&gt;&gt;v.
# MAGIC ....v&gt;..&gt;v
# MAGIC v.v...&gt;vv&gt;
# MAGIC v.v...&gt;vvv
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 40 steps:
# MAGIC &gt;&gt;v&gt;v..v..
# MAGIC ..&gt;&gt;v..vv.
# MAGIC ..&gt;&gt;&gt;v.&gt;.v
# MAGIC ..&gt;&gt;&gt;&gt;vvv&gt;
# MAGIC v.....&gt;...
# MAGIC v.v...&gt;v&gt;&gt;
# MAGIC &gt;vv.....v&gt;
# MAGIC .&gt;v...v.&gt;v
# MAGIC vvv.v..v.&gt;
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 50 steps:
# MAGIC ..&gt;&gt;v&gt;vv.v
# MAGIC ..v.&gt;&gt;vv..
# MAGIC v.&gt;&gt;v&gt;&gt;v..
# MAGIC ..&gt;&gt;&gt;&gt;&gt;vv.
# MAGIC vvv....&gt;vv
# MAGIC ..v....&gt;&gt;&gt;
# MAGIC v&gt;.......&gt;
# MAGIC .vv&gt;....v&gt;
# MAGIC .&gt;v.vv.v..
# MAGIC 
# MAGIC ...
# MAGIC 
# MAGIC After 55 steps:
# MAGIC ..&gt;&gt;v&gt;vv..
# MAGIC ..v.&gt;&gt;vv..
# MAGIC ..&gt;&gt;v&gt;&gt;vv.
# MAGIC ..&gt;&gt;&gt;&gt;&gt;vv.
# MAGIC v......&gt;vv
# MAGIC v&gt;v....&gt;&gt;v
# MAGIC vvv...&gt;..&gt;
# MAGIC &gt;vv.....&gt;.
# MAGIC .&gt;v.vv.v..
# MAGIC 
# MAGIC After 56 steps:
# MAGIC ..&gt;&gt;v&gt;vv..
# MAGIC ..v.&gt;&gt;vv..
# MAGIC ..&gt;&gt;v&gt;&gt;vv.
# MAGIC ..&gt;&gt;&gt;&gt;&gt;vv.
# MAGIC v......&gt;vv
# MAGIC v&gt;v....&gt;&gt;v
# MAGIC vvv....&gt;.&gt;
# MAGIC &gt;vv......&gt;
# MAGIC .&gt;v.vv.v..
# MAGIC 
# MAGIC After 57 steps:
# MAGIC ..&gt;&gt;v&gt;vv..
# MAGIC ..v.&gt;&gt;vv..
# MAGIC ..&gt;&gt;v&gt;&gt;vv.
# MAGIC ..&gt;&gt;&gt;&gt;&gt;vv.
# MAGIC v......&gt;vv
# MAGIC v&gt;v....&gt;&gt;v
# MAGIC vvv.....&gt;&gt;
# MAGIC &gt;vv......&gt;
# MAGIC .&gt;v.vv.v..
# MAGIC 
# MAGIC After 58 steps:
# MAGIC ..&gt;&gt;v&gt;vv..
# MAGIC ..v.&gt;&gt;vv..
# MAGIC ..&gt;&gt;v&gt;&gt;vv.
# MAGIC ..&gt;&gt;&gt;&gt;&gt;vv.
# MAGIC v......&gt;vv
# MAGIC v&gt;v....&gt;&gt;v
# MAGIC vvv.....&gt;&gt;
# MAGIC &gt;vv......&gt;
# MAGIC .&gt;v.vv.v..
# MAGIC </code></pre>
# MAGIC <p>In this example, the sea cucumbers stop moving after <code><em>58</em></code> steps.</p>
# MAGIC <p>Find somewhere safe to land your submarine. <em>What is the first step on which no sea cucumbers move?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''>.>v.v.>...>v.>>v.>..vv>>v>v....>.v..>v..v>>>>..>>.....>....>..vv..v>.v.vv.>v......>>.>vv>vv..v>..v......vvv..v...vv.>...vv...v>..>..>v>.>.
....v>.>..v.v>...v.>...v..v.>.>>>..v>>..vv>.v....v..v...>>>..>...v....v>>.v>>.v.>vvv..>...>...v..v>..v.v..v...vv.>.>vv.>.v..>>v...v.>>>v..>
...v.>vv.>.v..>..v....>vv.>...v.vv>vv..vv.vv...>>..v>vvv..vv...............vv...>v>>v..>.v.>vv...>>...v>v.v.>>>.>....>.>.v....>.>v.>>..v.v.
.....vv.vv....v>vvv..v.v>>v.v..vv>.>..v........>>...>.>>>....>>.v>.v..>v>..v...>>........v>>>v>.v......vv..vv...>..>.>.>vv>v>vv...v.vv>>v..
..vv.v..>.vv>.v.vvvv>v..>v..v>.>>......v...v.>v>>>..>.v...>.v..>v..v>.>...v..v>>.vv.vv..v...>.....>.......v..v.>..>...>v.vvv.....>v.v..>>.>
v.v.>.v.>.v..v.v>v..v.>.>vv...>......>...>..>.v>..v.v..v.>...>.v.>>.v.......v>vvv>.v..>>>..v..>.>>v>v>>v.v.......>...vv..>..>v......v..v...
v.>>vv>v..>.>.>.>..v>>v.v>vvv...v.>v...>..>vvv.v.>.>.>.>.....v>..>..v.vv>v.>.v.v>.v>vv...v...>.v.v...>v.>>.>v..v>v.>.>...>v>.>..>>>.vv.v.>>
..>>.>>.v.....v>.v.v......v>>>>.v.>>.v.v>v.v>>.>>.>....v>.v>>>>..vv..>>....>>.>...vv.>v>vv..v...>.vv.vv....vvv>.v.>....>v.>.v...v.v>vv..>.v
vv.>..v>v.>v.vv>..v.v..>>>>>v....v.vvv>>.>...>vv..>.v..>...>..v..>>v>.>..>v..>...>..v>..vvv>..v...v....>v..vv......vv.v>.v..v>....>...>...v
vv>v.v.vv.>>.v.>v....vv..>>....vvv.>..>>....vv..>v>...vvv.v.vv>>.>.vv.>.>.>.>.....>v.v>vv.v.>.>v.>>v>...>..>v>..>vvvv...v.v....v>.....>....
...>.v.>v.>...v.>v..vv.>..v.....>>v>>>>v.>..v.>.vv.>>..>.>v.>>v...>.v..v>>v..v>.v.>>v>>>..v>..vv..>.>>v.v>v..>.>vv..>...>v..v........vvv.>.
.>..>v.>>...>vv.v>v.>v>......>.>>>.v...v.>>...>.vv.v..>vv>v.>>.....>>v>v>v...v>...vv...>v>>..v..>.>.....v>...v........>.vv.>>v...v>.v.>v...
v...>.vv.......vvv...>>.>>vvv...v>..>v.>>vv.>...>v..>..vv.>v>v>v>.v>..v>v..>..>v.>v>>....v.>..v.>v>.vv.>v.>vv>...v>vv>.v.vvv...>.v>v...v..>
.v...>>.v>.>.v.vv.v.>....>.v.v>>..>.>.v>>v>vvvvvv.vvv>v.v.v..>v>.vv..>...>vv.v.>...v.vv.v.>vv.v.v.>...v>..>..v>..v>v>>v.v..v.>vvvv>v.vvv.v.
>v.v.v.vv>v..v>v.v...>>vvv...>.v.vv...>.v..vv.vvv.....v..>..>...>.......v>.>v.v.v..>.....vv...v.......>>>v>..>>.......v>...>.>vv.>.>>v>..v.
.vv.vv.>>..>.v..v..>.>...>>.>>v.>.>..>..>.>.vv.v.>.>v.>.v..v..vvv..v>.>.>.>..v..>v..>...vv..vv...>..>>v>..>>v.....>vv.>..v>.vv>v.vv....>v>>
>>.>>>.>.vvv>...v>vv.>.v....v.>>..>vvv..>>.v...vv.>..>.v.>>.v>..>>.vv..>.>>..>vv>>v>...>vv.>.>>>...>.>.>>.v>v>.v>vv>.v.vv...>v>v.vv.>>.vvv.
>v.>.v..v.vv..>v.....v.>vvv.>.>>vv..>>.vv..v.v>.>..v>v...>.>.v.>vv>v...v.>v.v...>v.v...v>.v.>..>.>v.>v...v..v..vv.v.v.>vv>>.>.>v.v.>.>v>...
..vv>.>.v>vvv.>....>...>.>>>.>.>v>v..>.v....>v...v>..>....>>>v>.v>.v.v....v.>>v>>v>>.>v...>>.vv..>..>..>..>>.>...v.>v.v>>.>v...>..>v.>.....
>v.v.v...>>>vvv.>>.>>>>>.vv>.>v....>>.....>v.vv.....>....vv..v.v>.v....v>>>.v.....v...v.>.>>v>....v>.vvv..>v.v....>...vv..vvv>.....v....vv.
vv.v>>v....v.>.>>v.v.v.......v.>...>.>>vvv.v.v..>....>v.>v.>>>vv>v>..>.....>...>>>.v.>..vv>.v..v..v.>.....>.v.v...>..v.v.....>...>>>...>.v>
v.>.v>.....vvvv...>.vvv.>.vv..>..>>..vvv.v...v.v.>>.>v>.>v....v.>>.>>....v..v>.>...>>..v.vvv..>.v...>.>v...v..>.v...>..>..v.>.v>..v..>>.>..
..v>v.v...>vv..>>.........vv..>v....v.>vv.>>.v..v...>...v>v.v...>>>>.>.>.vv...v>>vv>>.....>>.vv.vv>v>vv..vv.>v.v.....>.vvv>.......>...>v.v.
..v....vvv>.v.v>....v..vvv..>>v>....v.v>.v.>..>v...>..v>>..>.>...v..v..v.vv>.>..>..>vv..v.v>v>..>..vv>>.vv>.v>v.>..v>..v.vvv>>>>.v...>v>..>
.vv.vv.vv...>.v>v..vv.>.......>.>>v.v.>>v>..v.v.>....v>...>..v>...v.vv>.v..vv......v>vv.v.v....vv...>...>v>...>...v.....>.v.v.v......>>v.v.
>..v.v..v>.>v..>v>..>....>..vv...v.>vv.....>v>...>.....v>>.vv.vv.v..>.>v..>v..>.>vv...>>.>>>.>>>...........>.>.v.>v>>...v>v.>.vvv>v>v.v.v..
.v..>>..>v>..v.v....>..vv>vv.v..>v..v..v..v...vvv>>v>vvv>.v...v.>v.v>vv>v.v>..v.v..v>>>v..vvv>>..v..>....v...>.>v..v.>>>.>.>v......>vvv>...
....>vvvv....v>v.>v.v>>v.....v...vvv>.v....vvvv.>v.>..v>>v>vv.>>.>....v>....>.>v.>.>>>vv...>.v...v.v>vv...v>.vvv>v>.vv.v.>....v.>..vv...>..
.>>vv.>>.>.>..vv>.v>..vvv.....v>.v.>.v.......v.vvvvv.v.>>....>.>.>>>v>...>>>v...v.>>>>>...v>v..>..>...v..>.>.>v.>v>...vv...>..vv.v..v..v>>.
v....v>.....>>>.>v..v.v>>.>vvv..>v>>>.vv>..>.>>v...>..>..v...v>..v.v...>.>v......>>vv>.vv..>.>>>v.v.vvv..>...>.>..v..v....>v...>.>.vvv>.>.>
.v.>>.>...>>v.vvv..v>vv.v.>>v>vv>.>v......v>>v>vv.>.>.vv>.>.>.>.....v>>.v>v>.>v..>..vv..>v>>>>>.>.>v.>...v.v>..>.vv..v>v>..vv>..>.....>>>.>
....>v........>v.v...>v..vv>>.v.>..v..>>v>.....>..>vvv>.vv.v.>.>v.v>.v.>v.>..>v.v>>...>.>.v.>.>v..>>....vvv.>>.>.v.>>v....v>..v>.v.>...>.>v
..v..>..v>.v.>>v....>v.>vv.>v....>v.v.v.>....vv>....v.v.v..v.v.vv...>.>>>.>.>.v>.v.v...v>.>..>.>.v..v...>vv>>v......v.>..>..>>>.....vv..v.>
v.v>v.>>vvvv.>.v>v...v.>.......>v.vv....>>v.v....v....v..>>>>>.vvv.>.>>.v>>.v>>vv.>v>..>.......>.>.vv>..>.>.>>...>.....>>.v.v..>v>v>.>v>v>.
>>>>.v.vv.>...>>.>....v.v>..vv>.vv>>vv.>..vv>.>.v>>...v....v.vvv>v.>.v.vvv.v.v..v.v.v....vv>..>v.....>>>>v>.>v.vv..vv.v.....vv..v>..v.v..>.
>>..v...v.>>>..vv.v..>>.vv.v....>.>>>>>>>v.v.>....v>.v...v>.v>v.>..>.v.v>..v....>...v....>.v>.v>.v>>>.>.>>.v>....>v.>>.....>..vv.>>v>>.>...
v.>>>v......>...>>..vv>>>>v>>v.>v...v>>.v..vv.v.vvv>>v.>v.vv.vv...v>>.>..>v.....>>>.v..vv.>>.>>>..v>>>.....v>..>.>v.v>vvv.v...v>>.>>.>>>..>
.v>..>v>v..v..>v>>v.v...vvvv.v.v....vvvvv..vv.>......>>...v...v.>..v...>vvv..v>v.>>vv.>.v>>.....>v.v..v.>>....v>>vv>.>.v.v>...>.>.>.v>.>v>.
.>.>..v.>.>.v.vvv.v.vv.v>v.v.>..>>.v..v.>.v>.>.vv>>>>...v..v.>....v..>>.vv..>>.>>v.>v.v>.>v.v..>.vv.vvv.vv>...v.v>vvv>.v.>vv>>.>vvvvvvv.v.>
>.>.>vv>>>vv..>>.vv.>..v.v>>>..vv..>v.vv..>>.>>.v....v>..v.>>>vv.v.>.v>.....v..vv>...>vv.v...>...>..>..>>>v....v.vv.>v..>v>....>...>>v>...v
...v........v>v>....v>...>.>v>v>v...>.v>.>.>..>.>.vv.>.>..v.....>v...vvv..v>>..>>>>...vv..v.>>v.vv>v.>...>....>.>..v.v...v..>>v.>.>vv>.v>>.
....vv.>>v.v>vv....>...v...>vv..v.vv>.vvv.>v.>.v.....vv>...v.v.v...>.v.>....v>>.v..>v>.v>.vvv>..>>.vv.v>v>........>.v>.>.>v...v..>.v..>>v>v
v...>..v.>.v......v...vvvv..v.>..vv>>>>v.......>.>.......>.v..>..v>..v..v.>v.v..>>..v>v.>>v..v.vv.vv>.v.>>vv....>...>v.v.vv..v>>..v.vv>.>..
.v.vvv...v.>v>v>.vv>>vvv.v.>.v.vv>v..v.vv.>v>..v.....>.v>v......v..v.v..v....v>>v..vv..>v...>>..v...>..v>v.>v>>v..v..>v....v.v.>v>.v..>>.v>
vvv..v.>....vv.vv.>>...vvvv.vvvv....>>vv...v>>v...v..>.>>...>.v.v....>vv.v.>..>...>.>>v....>.>..>v.>...>>vvvv......>vv>>.>..>.>>v.v....>..>
>v.v...>....>>.>.vvv...>>..v>>....>......>v>.>v..v.>v.vvv..>.>.>.>>.v.v>....>...v>.v>..>.vv..v.>...v>v.>.>.>v>....>vv.>..>>.>...v.>....>.>v
>.v>>>>...vv.v.>v.>v>..>..v...>..>v.>.>...vv.>.>.>...>.>..vv..>v..vv.>....>.v>v>.>v...>...>.>v....v>v...>>.....>.>..>vv.....v>..>...v.>..v.
v....v>..vvv....>..>.v...>....vv.v>.v>..>.vv.>v>..>..>>>vv...v.>vv>...>.vv.v>vv>v>v>....>...>..>vv>>v>....>...vvv>v.v.>.>.vv>.vvv>vv...vv>v
..v..>.v.....v.>.....>vv.>.vv>v..v.>..v>....>.>>..>>>v>.>v>>....>vv>>.vv.v.v.>vv>.>.v...>>>..v>...>v>.v...>>.vv....v..>.>..v.v...v>..v>v.>>
....>v..v..v>..v>v.....v..>.v.>v.vv>.v>>>>....>v.vvv>.....v..>..>.v>>..>.vv.>.v.v>...v>>.v.v>v.>..v>vvv>>>>..>.v.>..v.v....vv>v.>>.vv>.>..v
vv>.....v...>.>>v>.vv.>v>.v..vv>......v.v.>..v.....>v>.>v.v>v.v.....>vv......>..>.>.>>>...>v>>....>>v..v.v>..>vv.v...>.>>..v.>>v>.>.......v
.v..v....>....>>>.v..v...>vv.v>.>.>v.>.v>vvv>...v...vv>>.>v>.>..>..>v.v.>v>.>.>v.>v......>vv.>v>v.>...>>..>vv.v.>....vv>.>>....v>.>..>>>>..
.>.>vv.v>.>>>vv.v>.>..>..v.>.>>v>v..vvv...>>>>.>>vvv.vv.v.>.v.v>.>>.v..vv.>v.>.>......>..>v.>..v...>>.vv>v..v>v....>v>..>..v>v.v>....v>..v.
..>v>>v..>>....>v..v.>>.>.v.vv.>>.v..>...vv..>..>v..>....v.>..>..v.v..>v..v..v...>.v..>>v...>.v>.vv..v.vvvv>.>>>..>.>..>>>.>..>>v>....>.v.>
...v>vv>...>>...v.>>>...>vv>v>v..>....>v..>.>..v..v>...>.>v.vv.....v..>v.v>....>.......v>...v.v......vv.>..v.>>>v>v.v.vvvvv.>....vv>..>....
>..v.>>>.v>>v..v..v....v>v..vv>...v.vv.v>vv...>..>.>v>..v>>.>>v>v..>..>.>....v>.>v>>vv.v>>>.....>>....>.v.v>.>.>>>....v.>.v>v>.>>>..v..>.>>
>v>v.>...>v.......vv>............>......>>..>v>>.>v.v.vv..v>..>.v.v>v>..v...>>>.>vv>vvv..v.....>>.>v..>.v.>>v>>>v.v...>...v.>v..v..>..v>.v>
.v...>..vvv...v.vvv...vv>>..>v..v.v...v.>..v....v...v.v...>v....>..>.vvv.vv..v.>v.>.>..>..>>vvvv...v..v.>v..>.v.v.v..>v.....vv..>vv>.>...v.
>.>..>..v...v.>...v>>..v.....>v....v>v.v>.vvvv....v>>.v>...v.>....v>v.v>>>.>...v>vv>..>.....>.v>..vv.v>>>v.>>>.>v.vv...>>......v>..>.vvv>.>
.>......>v.vv.v.vv.>>>>v>.>v>.v...vv...v>.>v..>.v.v......>.v...v..v>>.>vv.vv.v..v.vvv>>v>..vv.v>..>..>v..v>>>>.>...>..v..>>>..vv.vvvv..v>v.
v>.v..>.......>vv.vvv....v>>v>>v..vv>..v.>v..>..v>v..>.>v....>v....vv..>.....>...vv.>...vv..>>v...>..v.....v.>..>.>.>>v.v.....>.>.>vv..vv.v
..v..v.v..>v>....v>>...v...>...v>.v..>vv>.vv.vv....vv...vv.>.v>>>..v>.v.>>vv.v.v>.>>>>>v..v>v>>.>.v..v.v.>v.>v>..v>>.vv>>..>>.v..>v>v.v.v.>
.v..>v.>>v..>.v>vvv.v>>..v>v.>..>..>v>.vv.v.>...>.v>>>..v....>.>.>>.v.vv>>>>.v.......>>.>>v>......vv.>>.>...v.v>...v..>..v.>v.vv...v..>>v..
>..>..v..v>>>v>..v>>>.>......v>....v.v.v.>>>.v..>vv..>.......>.v.>.....v.>vv>v>>...vv>v..>>.v...>.>v>>>v>vv.vv.>v.>...v>.>.>.vv...>>..v....
..>..>..v.>>v.v.>..>v>v.>.vv>...>....v>v.v...v.vv.v.>>>v>v>.v.v.....>>..>..v>...>>...vv......>>>...v>>>v>..vv>>>vv.>..>>vv>.......v...>v...
.>.v.......v>v.>v....vv>v>.>.v>>..>v>.>>vv...v.....>.v>>.>v>.>.>>>>vv>..v.v.>>>.>.>>.>.v.v...vv.v.v..>.>>v...>.v>>>...v>vvv.v.......v.>.v..
v>vv.>>>v.>.>...v>>>...>.v.>..v....>...>..v.v.v.>v.v..vv..>..>>>v>.v.>.>..v>.>.v.v..v.>v....v>>.....>>..>vv....>.>>>>.vv>..>.v>>v>v>..v..vv
>>v..>...v>>....>v......vv>..>v>v...>...v.v>>v>...vvv.>>..v.....v>>v>.v.v>v...>.................>.>...>.>...vv..>..v.>..>..v.>>vv..>.>.>>>v
v>.v>>v>>..v.vv.>v...>>..>.vv>..v...>>>...v.v.vvv.>>>.>>..>v.v.>v..>..v.vvv..v.vv....v>.>>vv.>..v..v>v...>.>..>......vv>.>..>v.>>>.v>>....>
>.>>..v..v.......>........>..v.>.vv.vvv.....>.....>..v..v.>>..>>.>>..>>.v..>>>..v.....>vv>.>vv>...>.>.v..v.v.v.>>v.v..v>>>v>v>vvv.v.v..>v>>
...v>v>>...vv....>...v..>.v.>.....>...>....>..v.>.vvv>.v>v>...>vv>...v..v>>.....>.vv..>>v.....v>>>.v>v.....v.v..v>vvv....v.v>>vv.v.....v..>
>v>>.>.>.>vv...>.>v.>v.>.....v..>vv..v.>v.>.>vv>..vv..v.>.>vvv.....>v.>vv..v..>...>.>..>>.>..v..v.>...v>.v.v.v..>v.vv>.>...>v>v.v>vvv>>>..>
v....v...vv.v>....>v.>v..v..vvv..vv.v..>..vv>>.>...v.>vv...v>.......v.......v>>>>>vv..v.>v.v....>v>v.vvv.>.v.>.vv.v....v..v.>vv....>>>v.v..
.vvv.vv>vvv>.v>..v.v.>.v..>v..>v..v>>vvv..vv.>..>....v>v.v.>..>..v...v..>.>...>v...v......>v.v.>vv>..vv>>>v.>.v...v..>vvvvv..v..vv.>..v.v.v
v.>..>v.v.>.v>.>v.v.vvv..>v>>.....>>>vv..>.....v.>..>.>.>.>v..>..v..>>.v....>...>>....>.v.v.>>v>>v.v......v>..vv.v.v>>.>v.v>.>.>.......>...
>.v.......v..>.>>.....vv>v..v.>..v.v...vv>.....v.>v.vv..v.....v>vv...v.>>.v.v...>...>>vvv>.>v.....>....>....>.>v..vv.>v...vv.v.v..vv.>.v.v.
v.v....v>vvv>vv.vv...v..vvvvv.v>v..>..>..v>>...v>>.>v.>>.>>>>>..v...>...>.>..>vvv..>>...>...>..vv>>>..v>>.>..v>.....v..v>vvvvv.>..v.v>.vv.>
>>.vv.vv..>>..>v..v.v>.v..>>.>>v.>>v.v.>>.v>.>>v>..>vvv.>>v.>...>.>>>v.>.....vv>.....>.>..>...>.>....>..v.v..>.v.v.>v.vv.v.>>v..>.vvvv>v>.>
v..>vv...vvv>.v..v.>vv>..>.v.>v.v>....>>...v.>v.>>>.>.v>>.>..>.....>..>>.v>vvvv.vv>v..........>.>>>vv.>.v..v.v..v..vv>v>v..v.v.....>..v.>v.
v>v.v>v>vv..>>vvv..v>...>v.>.v.>>...>v....>.v>.>v>...>>>>..>v.>>..vv.>....>>>..>...>>.v.>>>..>v...>vv........>....v.v..v..>v>>>>>..v..>>...
>>.v.>.>>vvv>>.v>v.>v>...v.v...>...>>v......>.>.>>>.>v>....v...>v..>>..v>...>.v>>.v..v>>v.v.>>.>>v.>..vvv>..v....>>.v>..>v.>...v...vv..v...
vv..>...>v>>v..>..v>..>.v.vv..>...>>.v.vvv>v>.vv..>.v.>>.>.vv.>...v....v.>>v.v.vvvv..>.v.......>.v........>>.vv.v.v..>..vv.>..v...>..vv.>v.
v.v.vv..v>..v.vv..>>v>v.>v..v>...>vv>.>>v.>.>>.v...v>...>.vv.>...vv...v.......>>..>.v.v..>>.....>.......>...v...v>.v..>vv..v>.>>vvv.>..vv.v
...vv.vv>.v.>.v.vv>.>.....>>>.vv.>>v.v>...vv>.v>.>...>..>vvv>....>v........vv...>...>v>>.v...>.vv.v......vvv>..>..>.>.v>.>.v....v...>>>.v.v
...v>>.v.....v....>v>...vv>>..vv.vv>>vvv>.>>>>....v...vv.>v..>vv.v.>>>vv.v>.....>.>......>v.vv>>.v.v..>.vv>.>v...>...>...v>>.v.vv....>...v>
.>>.vv..>>>>..>vv....v.>v.>..>..>>..>.>v>.v>>.>.v..>..v...>.v......v...v....>>.>.v.....v.v..v..v...v..vv>v..v...>...>>..v.v.>vv..v>vvv.....
vv.>.>.v.v.......>...vv>vvv..v...v.v...>v..>....>.>>>...>v...>v.>>.vv....vv>>.....v..>v.vv..v...v....>.v.>>...v.v.>>>.>v.>.>v....v.vv....>v
>>v..>>..>....v...v.v.>..v>v..>>v.>vv..v>.v..v.v.....v.>>.vv.>.>>.>.>>..v..v..v.>..>>.>...>.v>>>>v.v...v..v..>>....>>>v.>>v.v...v.>v.vvv.vv
v>>v.....v..v.v...v>.v...v>v.....>>..>.v.v..vv.>.>v..>v>>.>.v...v.v.>vv...v.>.>>.vv...>v>.>>>>.>>vv.....>vv>...v..>v>..>....v........>...vv
....v..>>...>v.>>..>.v..>v...>.vvv.>......v....v.......>vv>v....v>>>>>..>v>...>v>.>.>vvv.v.>>>..>....v>..v>.vv....v>>>>>.>>.>.>.v>>.>..vvv>
.>v>...v>v>...>...>.v..>v>>.>>..v>.>.vv>..v.>..v..>>.v..vv>.>..>.v.>>.>v>>v.>....v.>vv>.>>.v.>.>.v...>>>vvv..v>>.vv..v...vvv...>...>.>..v..
.>..v.vv..>.>...>...>.>.vv...>.>.....v......v.vv>vv..vv...>.>..>.>>v..>>v...v.vv...v>...>vv..>.v.v>>v.>.vv..>..>vv>..>..>....>..vv>.>...>.v
>.>.>>....>v...v....>v...v.v...v..vv.>......>>.>v>>v..>vvvv....v.>>vvv>v....>vv.v.vv....vv>>.v....>...>>..>>v.>.>v...v.>v>v>.....>>vv.v.>..
v>.v.>..>v.>>..v.v..vv.>.vv>.v..v...>v...>vvv.>....v..>vv>.v>.>.v..v>>..>vv.vv.>..vvvv>...v>..v..>..>..v>>......>v..v.>>.vv.....>.>...v>vvv
>v.v>.v>>>vv....>.>v.>>.vvv.v.>....v>vv.>v.>v..vv>..>...>>...>vv.>vv...v>........>.>v>>>>..>v...v.v>>>vvvv>>.v>v.>...v>..>>.>.>vvv.vv.>vvvv
..>v>vvv>vv..>>.v>v.v..v.>v.v....v...vvv..>.>.vv>.....>>v.>...v.>>.vvv>>.vv>..v..>...v>>>>.v.v.>.>>>......v.>>.v.....v>>.>..>v.v...v.>vvv>.
>v.v>.v>..v>vv.>>.v....v..>...>>.>v...>v..v>.v>v>v..>vvv>v.vv..v....vv.....vv.vv.>>>.vv>....>v..>>.v>.v.>>.>..>.......>v>>>>...v.>..v.vv>v>
vvv.>..v.>v>.......v>>.>.v>.vv.vvvv>.....>v...vv>.>vv>......>.>.>v.v.>..>....>v>v.vv>.v.>..v>v>...v>>vvv.vvv>v.>.>.>..vv.vv..>v>>v>.>.>.>..
v>v.....>vv>>..v>v>......>>>...>v...>v>.v.......vv....>..v>..vv>>v>..v......vv..v.>v>>v..>.v.v..v.>.v.v>...vv...v>...v>v>>>v>>.vv.>>..>.v.v
v.vv.v>v..>.vvv>.>...vv>..v.v..v>vv>>v.v>.v>vvv.>...>..v>..>.>.>.>>...v.v>......>vv>>..v.v>v.........>v..>..v>vvvv>vv..v>..>.>....>>v.>v>v.
>.>>.>.vv...>.vvv>>>>....>vv.>>v>...vv...vv>>>>>..>.v....v>v.>>...>.>.vv.>>.v....v..v>..>>....>v>>>..>....>.v>v...>v>.>v.v>.v..>.......v>vv
.>v..>>v>.vv.....>v..>.>>>v>.>.v..>>....vv.>.v.>v>.>vv>...>...>>..>.vv..>v...>.v.>.....v..>..>.v.>.>>v..v..>v>vvv..v.>vvv.>.>v..v>..>.v.>>.
...v>.>v..>v.>.v>.v>v..v.v>>>>.v.v>v..>v>.v>..v..v.>..>.v..>.......v.v..v.>.>>vv.vvv.v..v.v.v..>v..>vvvv........>vv..vvvvv..v>...v>.>.v.v.>
.v>...v>>v>v>v....v.v>..v>.vv...>...v.v.v..v.>v.v.>vvvv.>>.v..>v..>>v>vv.>vvvv>v>...>...v>>...>vv.v..>....>.>v.v.>>v.vv..>...>v..>v>.>>>>>v
>v>v.v>>v.v..>>..v>..v..vv.....>v.>>...v.v....vvvv..>....>>vv..v>.v>>>v...>.v.v.v..>v..>>....>.v..v..>vv.v......>..v>.v>.v..v>.>.v>...>..>.
>...v.>>>...v>vv.v>.>.v.>>>v>..vvv>>vv..>.>v...>>vv.v..>>vv>....>>...>...vv..>.vv..vvv..v.>..>.v.v..v.>..>v>.>>..>>.>vvv.>..v>>v..>>..v>>>>
>v..>vv>..v...vvv>>.....>.>.>v>..v.vv.v..>>.....>.v.>vv>v.>>v...vv.v>vv..v>..>v>..>>v.....v.v...>....>>>.>>v.>.>..vv.....>>>..vv..>........
>>..>>v.v.v>v....>.>>>v..v...v>..v..>>>.>.>..>...>..v>.vv.......vvvvv.v.v.>vvv>v..>v.>v.v...>v...>v.>v..v>v..v..v.v...>vvvv.>v..vv..vvv....
.v......v.>..>v>>.>>>.>.......vvv>>vv...v....>vv......>.>vv>..vv..>..>...>v....>>>..v.v..vv>..>vv>v>vvvv..v.v..v>..v>.vvv>v..>v....>..v..>>
...>.>..>v..>.v.>.v..v>..v>>.>...vvv>.>>.v.v...>vv.>v.v.>.v..v.v.>..>.>>.>..>v.>>.>vv.v>>.>>..>v>v>.v..>.vvv>v>v.>v..>>.v....>.v>........>>
...>v.>>..>vv>..v>>.v..vv>.v..v...v>.v.v.v..>>v..v..>.>v..>...>..>..>>vv.v>...vvv.v..>v.vv..v.>>>.>.>.....v>......>.v.......v...v>.v>>>..>.
>.>..>.v.>.>v>>>.>.v.>......v..>...>.>vv...>v>..v.v>>vv.>>....vv>..>>.>>..>.v..>>..>v.v>>v>.v.vv>>.>vvvv>v>..v.v>.v...v>...>vvv.v.v>v>v..v.
v.v......v>.>>v.v........v.v.v>.>..>.>..v.>v>.>..v.v..v...>v.....>..>>>>v>>.>...>>.>v.>>.>.vv...v..>.vv>......>vv.....vvv..v>vv..>.>..v>.>.
.>>>.v.vv>......v>.>>.>.vv>...>.vv.>>>>vv.v..>v..vv>v.v..>.v>.v...v.>>.v>>vvv.v......>.v>>....>..v...v..vvv..>v.v>>..>v.>.......>v...>..>..
...>>>.>>.>.v.v>.>.>vv...>...v.>...>v.>...>v>.v.v..>..v.>.>.v..v.vvvvv..v...v.>......v.v>...>v>.>.v>.vv>...>...>.>.>>v...vv.>>.>.v...>>>...
.v..v.v..vvvv>v>....>..v.v..v...v>..>>..v.v>.>..>.....>.v.v>....>..v.v..>..>vv>>.v.v>..vv>.>>v..v.>..>..v...>>>..v>.v>..>.v>.>..>..vvvv.v..
.>v.vv>.>..>.v.v>.>>...>v.v...v.>.>.....>>..v.v.>>>.>..v..>.v>.vvv.v...v>>.v>.>.v.>.>v>v...>...>............v.>v...>....v...>..v...>..v...v
vv>>..>.>..v.vv.>.v.v....>.>vvv.v>>...v>v>v.>>v.vv>...>>..>.>.v>>....v.>...>.v...vv>v>vv.>..v>v.>....>vvv>....v>..vvv..>.>..vv.>>.v.v..v..>
..>....>.vv.>vv.>.v..v.v.v>.v..v.....>.>v.v..>>v>v.>v>>..>v.v.....>>>.....v>>>...>>.v..>v....>..v....>v.v..>>v..v.>>>v.v>.>>..>..>..>...>v.
v>v.v>vvv...v..>>>...v.v>.v>.>..v.>>..>>vvv...v.>v.>v.v>.v...v.vvv.vvv.>...>.....>..vv..>>.>..v..vvv.v.>.......vv.>>...>.>.v..v..>v..v.v>v.
.>.>v>.v.v>.>v>v.>.vvvv.>..vv...v...v.v>.>v.>.v..v>vv>..v.>.>>>v....v..>..>>..>v..>.......vv>>vv.....vv.>>.v.>>v>..>v.vv.....>.>.....>.v.v.
>.v>v....v.v>..>.>v>.v...>>>v>.v..vv..>vvv>..>v..v>vv>>v.>>v>vv.....>.>v.v>vv.>>.vv>v>>..>.v>v>v.>.vv.vvv>>.>..v>>.vvv.v>>.>.vvv.v>vv.v>.>>
>>.v....v..>vvv>>...vvv>>.>..v>..vvv.....v>.v>.v.>...>.............>..v.v....v.v>.vv.>..>v..v....>v.>>vv...v...>v.v..>>....v..v.vv>v..v...>
>v.>v..v.>.v.v.>..>>.>v>.v.v..v.vv.vv.vvvv.>>vv...>v.....v>...>.>>v.>>...>vvvv>.vv>.v....v>v>>>v...>.vvv>..v...v..v>.>>.>>>........>>.v.vv.
.v.v.........v.>>v.>vv.v.v.>vv>>v>>>.vv>v>>v.>>>>v....>>.v..>.v>v>>...v.>.v..>.v>>>..>>v..v>.v.vvv.>v.>..>..>...vv.>>>...vv....vv....v....v
>>>vv.v.>.v>.>vv..>.v.....>...>..>.vv>>v...>.......v...>.>.>>v.vv>vv..v.>vv....v....>.>.v.>v>v..>>v....v.>>...v>>>>v....v>.....vv...v>vv..v
>v.v....>>.>v>.>>v.>..>>>.......v.v.v..>vvvv.>v.>.v.v.v.v..v>.v.>..v>..v>.>>.....v>.>>..>.>>>...>v.>>v..v....>>.>.vv.vvv.>v..>>>....>.v...v
>.>.v.....>..v>vv>>>..>..v.>vv>vvvv...vv....>.>.v>>.>>.>.v..v..........vvvvv.v.v.v..>vvvv.....v.>vvv...>v..>>v>v....>.>..>>..v>>v.>v.vvv.v.
.....v>>>...v..v..>...v.>v.>v.v..>>>..>>v>.v.v>vv>.>..>vv....v>...v>vv>>.....>.v...v..>vv.>v..>.v.vvv.>.v.vv..v...>..vv..>v>>>..>>...v...vv
>v>v.>.v.>vv..v...>.>.>.....v>vv..>>.v...>.v...v..>..v.v..>......>v>>.....>>>v..v.>>v>>v.v>v>.>v.vv.>..v...vvv..>.>>.>....v>..vv.v..>..vv.v
.v>.>>....>>>.vvv.>.vv..>vv..>.v.v.v>.vv..vvv.>..>.vv..vv...v..v.v..>v..>..>v......>>.>v.v.v.v.vv>.......>.>>...v.vv>.>>..v.v>.v.>>.vv.v.>.
v.v>>>.>..>v>v.>>>.v.v>v.v.v..vvv.v>v.>.>>>.>v>v.v>.>vv...v>.>v.v.vv...>.v.v>>>vvvv>.v..>..>v......v..>.>v>.v..>...v>v>.>...v.v>.vv.>v>.v>v
..>>.v>>.v.v.>vv.v...v.....v..>...v..v>.>>>vv.v>>v.>vv.>>>.v...>.>>....>...v....>vv..>v>.vv.>...v..>v..>.>.>.v.vv..v.>...v.v>..vv>.>>......
.v...>>>vv>>v.....v>...>>.>..>...>v>>>v.v.>.>vv>vvv.v>.>..v..v>v..v>...>>>>vvvv..vv>>..v.vv.>vvv....>..v..v.>.v.vv>v>.v>>....>v.v..>>vv>>vv
..v.v>..vv.v...>.>v...v>>v>v.>vv.v..v>>>v>.>.v.vv.>.>v..>>...vv.v..v..v.>>..>>>>>>..>>.v>..v>>>v.v>v>>.vv.>..>.v..v..>..>v.....>v>.vv>>>>v>
...v.....vv..v....v.>...>...v..v...>.>>v..>.vv...vv.>>...v...>>v....v....v>>...>....>v.v..>>.....v....>>>vv>>...vv..>>v..>>...>>vv..>.v.v>>
.>..>...>..v.>..v>>>...v..>>.....>..v.vv.v>>.....>...v>..vv>>>v...>.v>v>v>v.>.>.vv..>>>>..vv...>..>>vv>...>>...v>.>>>v>>....v>..>.>>.>v.>.>'''

# COMMAND ----------

import itertools

nrows = len(inp.splitlines())
ncols = len(inp.splitlines()[0])


def step(h):
  next_h = h.copy()
  for (row, col), value in h.items():
    if value == '>' and (row, (col + 1) % ncols) not in h:
      next_h[(row, (col + 1) % ncols)] = '>'
      del next_h[(row, col)]
      
  h = next_h
  next_h = h.copy()
  for (row, col), value in h.items():
    if value == 'v' and ((row + 1) % nrows, col) not in h:
      next_h[((row + 1) % nrows, col)] = 'v'
      del next_h[(row, col)]

  return next_h


h = {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line) if value != '.'}

for step_i in itertools.count(1):
  h_prev = h.copy()
  h = step(h)
  if h_prev == h:
    break

answer = step_i
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Suddenly, the experimental antenna control console lights up:</p>
# MAGIC <pre><code><em>Sleigh keys detected!</em></code></pre>
# MAGIC <p>According to the console, the keys are <em>directly under the submarine</em>. <span title="Thanks to the deep-sea marine biologist, who apparently works at the Biham-Middleton-Levine oceanic research institute.">You landed</span> right on them! Using a robotic arm on the submarine, you move the sleigh keys into the airlock.</p>
# MAGIC <p>Now, you just need to get them to Santa in time to save Christmas! You check your clock - it <em>is</em> Christmas. There's no way you can get them back to the surface in time.</p>
# MAGIC <p>Just as you start to lose hope, you notice a button on the sleigh keys: <em>remote start</em>. You can start the sleigh from the bottom of the ocean! You just need some way to <em>boost the signal</em> from the keys so it actually reaches the sleigh. Good thing the submarine has that experimental antenna! You'll definitely need <em class="star">50 stars</em> to boost it that far, though.</p>
# MAGIC <p>The experimental antenna control console lights up again:</p>
# MAGIC <pre><code><em>Energy source detected.
# MAGIC Integrating energy source from device "sleigh keys"...done.
# MAGIC Installing device drivers...done.
# MAGIC Recalibrating experimental antenna...done.
# MAGIC Boost strength due to matching signal phase: <em class="star">1 star</em>
# MAGIC </em></code></pre>
# MAGIC <p>Only <em class="star">49 stars</em> to go.</p>
# MAGIC </article>

# COMMAND ----------

# No puzzle here - just need 49 stars.
