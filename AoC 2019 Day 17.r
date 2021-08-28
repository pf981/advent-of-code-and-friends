# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/17

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 17: Set and Forget ---</h2><p>An early warning system detects an incoming <a href="https://en.wikipedia.org/wiki/Solar_flare">solar flare</a> and automatically activates the ship's electromagnetic shield. Unfortunately, this has cut off the Wi-Fi for many small robots that, unaware of the impending danger, are now trapped on exterior scaffolding on the unsafe side of the shield. To rescue them, you'll have to act quickly!</p>
# MAGIC <p>The only tools at your disposal are some wired cameras and a small vacuum robot currently asleep at its charging station. The video quality is poor, but the vacuum robot has a needlessly bright LED that makes it easy to spot no matter where it is.</p>
# MAGIC <p>An <a href="9">Intcode</a> program, the <em>Aft Scaffolding Control and Information Interface</em> (ASCII, your puzzle input), provides access to the cameras and the vacuum robot.  Currently, because the vacuum robot is asleep, you can only access the cameras.</p>
# MAGIC <p>Running the ASCII program on your Intcode computer will provide the current view of the scaffolds.  This is output, <span title="PURELY COINCIDENTALLY">purely coincidentally</span>, as <a href="https://simple.wikipedia.org/wiki/ASCII">ASCII code</a>: <code>35</code> means <code>#</code>, <code>46</code> means <code>.</code>, <code>10</code> starts a <a href="https://en.wikipedia.org/wiki/Newline#In_programming_languages">new line</a> of output below the current one, and so on. (Within a line, characters are drawn left-to-right.)</p>
# MAGIC <p>In the camera output, <code>#</code> represents a scaffold and <code>.</code> represents open space. The vacuum robot is visible as <code>^</code>, <code>v</code>, <code>&lt;</code>, or <code>&gt;</code> depending on whether it is facing up, down, left, or right respectively. When drawn like this, the vacuum robot is <em>always on a scaffold</em>; if the vacuum robot ever walks off of a scaffold and begins <em>tumbling through space uncontrollably</em>, it will instead be visible as <code>X</code>.</p>
# MAGIC <p>In general, the scaffold forms a path, but it sometimes loops back onto itself.  For example, suppose you can see the following view from the cameras:</p>
# MAGIC <pre><code>..#..........
# MAGIC ..#..........
# MAGIC #######...###
# MAGIC #.#...#...#.#
# MAGIC #############
# MAGIC ..#...#...#..
# MAGIC ..#####...^..
# MAGIC </code></pre>
# MAGIC <p>Here, the vacuum robot, <code>^</code> is facing up and sitting at one end of the scaffold near the bottom-right of the image. The scaffold continues up, loops across itself several times, and ends at the top-left of the image.</p>
# MAGIC <p>The first step is to calibrate the cameras by getting the <em>alignment parameters</em> of some well-defined points.  Locate all <em>scaffold intersections</em>; for each, its alignment parameter is the distance between its left edge and the left edge of the view multiplied by the distance between its top edge and the top edge of the view.  Here, the intersections from the above image are marked <code>O</code>:</p>
# MAGIC <pre><code>..#..........
# MAGIC ..#..........
# MAGIC ##O####...###
# MAGIC #.#...#...#.#
# MAGIC ##O###O###O##
# MAGIC ..#...#...#..
# MAGIC ..#####...^..
# MAGIC </code></pre>
# MAGIC <p>For these intersections:</p>
# MAGIC <ul>
# MAGIC <li>The top-left intersection is <code>2</code> units from the left of the image and <code>2</code> units from the top of the image, so its alignment parameter is <code>2 * 2 = <em>4</em></code>.</li>
# MAGIC <li>The bottom-left intersection is <code>2</code> units from the left and <code>4</code> units from the top, so its alignment parameter is <code>2 * 4 = <em>8</em></code>.</li>
# MAGIC <li>The bottom-middle intersection is <code>6</code> from the left and <code>4</code> from the top, so its alignment parameter is <code><em>24</em></code>.</li>
# MAGIC <li>The bottom-right intersection's alignment parameter is <code><em>40</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>To calibrate the cameras, you need the <em>sum of the alignment parameters</em>.  In the above example, this is <code><em>76</em></code>.</p>
# MAGIC <p>Run your ASCII program. <em>What is the sum of the alignment parameters</em> for the scaffold intersections?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

# input <- "1,330,331,332,109,3888,1101,1182,0,15,1101,1469,0,24,1001,0,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,15,1,15,1008,15,1469,570,1006,570,14,21101,58,0,0,1106,0,786,1006,332,62,99,21102,1,333,1,21101,0,73,0,1106,0,579,1102,0,1,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1001,574,0,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,1,340,1,1105,1,177,21102,477,1,1,1106,0,177,21101,0,514,1,21101,0,176,0,1106,0,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21102,375,1,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,1,222,0,1106,0,979,21102,1,388,1,21102,233,1,0,1105,1,579,21101,1182,22,1,21101,244,0,0,1105,1,979,21101,401,0,1,21102,1,255,0,1106,0,579,21101,1182,33,1,21102,1,266,0,1106,0,979,21101,0,414,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1182,1,1,21102,1,313,0,1106,0,622,1005,575,327,1102,1,1,575,21102,1,327,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,12,10,0,109,4,1201,-3,0,587,20102,1,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,1201,-4,0,630,20101,0,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,702,1,0,1105,1,786,21201,-1,-1,-1,1105,1,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,1,756,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21101,774,0,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2106,0,0,109,7,1005,575,802,21001,576,0,-6,20102,1,577,-5,1106,0,814,21101,0,0,-1,21101,0,0,-5,21102,1,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,41,-3,22201,-6,-3,-3,22101,1469,-3,-3,2102,1,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21101,35,0,-4,1105,1,924,2101,0,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2102,1,-3,895,1102,1,2,0,1202,-3,1,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,41,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,59,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,1,0,575,21101,973,0,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1105,1,1041,21101,0,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,0,439,1,1106,0,1150,21101,477,0,1,1106,0,1150,21102,1,514,1,21101,0,1149,0,1105,1,579,99,21102,1,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,2102,1,-4,0,109,-6,2105,1,0,14,11,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,13,38,1,1,1,38,1,1,1,38,1,1,1,26,13,1,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,1,40,1,3,7,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,4,7,19,1,3,1,5,1,10,1,19,1,3,1,5,1,10,1,13,5,1,11,10,1,13,1,3,1,5,1,16,1,11,13,16,1,11,1,1,1,3,1,22,1,11,1,1,1,3,1,22,1,11,1,1,1,3,1,22,1,11,13,16,1,13,1,3,1,5,1,16,1,13,1,3,1,5,1,16,1,13,1,3,1,5,1,16,13,1,1,3,1,5,1,28,1,1,1,3,1,5,1,18,13,3,13,12,1,9,1,11,1,5,1,12,1,9,1,11,1,5,1,12,1,9,1,11,1,5,1,10,13,11,1,5,1,10,1,1,1,21,1,5,14,21,8,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,11,30"

# COMMAND ----------

input <- paste0("1,330,331,332,109,3888,1101,1182,0,15,1101,1469,0,24,1001,0,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,15,1,15,1008,15,1469,570,1006,570,14,21101,58,0,0,1106,0,786,1006,332,62,99,21102,1,333,1,21101,0,73,0,1106,0,579,1102,0,1,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1001,574,0,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,1,340,1,1105,1,177,21102,477,1,1,1106,0,177,21101,0,514,1,21101,0,176,0,1106,0,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21102,375,1,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,1,222,0,1106,0,979,21102,1,388,1,21102,233,1,0,1105,1,579,21101,1182,22,1,21101,244,0,0,1105,1,979,21101,401,0,1,21102,1,255,0,1106,0,579,21101,1182,33,1,21102,1,266,0,1106,0,979,21101,0,414,1,21102,1,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1182,1,1,21102,1,313,0,1106,0,622,1005,575,327,1102,1,1,575,21102,1,327,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,12,10,0,109,4,1201,-3,0,587,",
"20102,1,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,1201,-4,0,630,20101,0,0,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,702,1,0,1105,1,786,21201,-1,-1,-1,1105,1,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,1,756,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21101,774,0,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2106,0,0,109,7,1005,575,802,21001,576,0,-6,20102,1,577,-5,1106,0,814,21101,0,0,-1,21101,0,0,-5,21102,1,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,41,-3,22201,-6,-3,-3,22101,1469,-3,-3,2102,1,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21101,35,0,-4,1105,1,924,2101,0,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2102,1,-3,895,1102,1,2,0,1202,-3,1,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,41,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,59,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,1,0,575,21101,973,0,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1105,1,1041,21101,0,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,0,439,1,1106,0,1150,21101,477,0,1,1106,0,1150,21102,1,514,1,21101,0,1149,0,1105,1,579,99,21102,1,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,2102,1,-4,0,109,-6,2105,1,0,14,11,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,13,38,1,1,1,38,1,1,1,38,1,1,1,26,13,1,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,1,40,1,3,7,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,30,1,3,1,5,1,4,7,19,1,3,1,5,1,10,1,19,1,3,1,5,1,10,1,13,5,1,11,10,1,13,1,3,1,5,1,16,1,11,13,16,1,11,1,1,1,3,1,22,1,11,1,1,1,3,1,22,1,11,1,1,1,3,1,22,1,11,13,16,1,13,1,3,1,5,1,16,1,13,1,3,1,5,1,16,1,13,1,3,1,5,1,16,13,1,1,3,1,5,1,28,1,1,1,3,1,5,1,18,13,3,13,12,1,9,1,11,1,5,1,12,1,9,1,11,1,5,1,12,1,9,1,11,1,5,1,10,13,11,1,5,1,10,1,1,1,21,1,5,14,21,8,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,1,9,1,30,11,30"
)

# COMMAND ----------

sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

# COMMAND ----------

create_instructions <- function(instructions) {
  result <- structure(instructions, class = "instructions")
  attr(result, "relative_base") <- 0
  names(result) <- seq(from = 0, length.out = length(instructions))
  result
}

to_character <- function(x) format(x, scientific = FALSE)

# i is a two-element list. The first is the 0-indexed index. The second is an integer indicating the mode
get_index <- function(v, i) {
  index <- i[[1]]
  if (i[[2]] == 0) {
    # Position mode
    index <- v[[to_character(index)]]
  } else if (i[[2]] == 1) {
    # Absolute mode
    # (Do nothing)
  } else if (i[[2]] == 2) {
    # Relative mode
    index <- v[list(index, 1)] + attr(v, "relative_base")
  }
  index
}

`[.instructions` <- function(v, i) {
  index <- to_character(get_index(v, i))
  if (!(index %in% names(v))) v[[index]] <- 0
  result <- v[[index]]
  if (is.null(result) || is.na(result)) v[[index]] <- 0
  v[[index]]
}

`[<-.instructions` <- function(v, i, j, value) {
  v[[to_character(get_index(v, i))]] <- value
  v
}

# COMMAND ----------

run_bot <- function(bot, input = NULL) {
  bot$needs_input <- FALSE
  while (bot$instructions[list(bot$i, 1)] != 99) {
    value <- bot$instructions[list(bot$i, 1)]
    
    op_code <- value %% 100
    p1_index_mode <- value %% 1000 %/% 100
    p2_index_mode <- value %% 10000 %/% 1000
    p3_index_mode <- value %% 100000 %/% 10000
    
    p1 <- list(bot$i + 1, p1_index_mode)
    p2 <- list(bot$i + 2, p2_index_mode)
    p3 <- list(bot$i + 3, p3_index_mode)
    
    if (op_code == 1) {
      bot$instructions[p3] <- bot$instructions[p1] + bot$instructions[p2]
    } else if (op_code == 2) {
      bot$instructions[p3] <- bot$instructions[p1] * bot$instructions[p2]
    } else if (op_code == 3) {
      if (length(input) == 0) {
        bot$needs_input <- TRUE
        break
      }
      bot$instructions[p1] <- input[1]
      input <- input[-1]
      if (length(input) == 0) bot$needs_input <- TRUE
    } else if (op_code == 4) {
      bot$output <- bot$instructions[p1]
      num_params <- 1
      bot$i <- bot$i + 1 + num_params
      break
    } else if (op_code == 5) {
      if (bot$instructions[p1] != 0) {
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 6) {
      if (bot$instructions[p1] == 0) {
        bot$i = get_index(bot$instructions, p2) - 1
        bot$i <- bot$instructions[p2] 
        next
      }
    } else if (op_code == 7) {
      bot$instructions[p3] <- bot$instructions[p1] < bot$instructions[p2]
    } else if (op_code == 8) {
      bot$instructions[p3] <- bot$instructions[p1] == bot$instructions[p2]
    } else if (op_code == 9) {
      attr(bot$instructions, "relative_base") <- attr(bot$instructions, "relative_base") + bot$instructions[p1]
    } else {
      stop(paste0('Invalid op code: ', op_code, ' at position ', bot$i, '\n', paste0(bot$instructions, collapse = ', ')))
    }
    
    num_params <- case_when(
      op_code %in% c(3, 4, 9) ~ 1,
      op_code %in% c(5, 6) ~ 2,
      op_code %in% c(1, 2, 7, 8) ~ 3
    )
    bot$i <- bot$i + 1 + num_params
  }
  
  if (bot$instructions[list(bot$i, TRUE)] == 99) {
    bot$is_halted <- TRUE
  }

  bot
}

# COMMAND ----------

create_bot <- function(instructions) {
  list(
    instructions = create_instructions(instructions),
    i = 0,
    x = 0,
    y = 0,
    is_halted = FALSE,
    output = NULL
  )
}

get_output <- function(instructions) {
  result <- c()
  bot <- create_bot(instructions)
  while (!bot$is_halted) {
    bot <- run_bot(bot, 0)
    result <- c(result, bot$output)
  }
  intToUtf8(result)
}

# COMMAND ----------

result <- get_output(sequence)
result %>% cat()

# COMMAND ----------

m <-
  result %>%
  read_lines() %>%
  discard(~. == "") %>%
  str_split("") %>%
  simplify2array() %>%
  t()
m

# COMMAND ----------

scaffold_cords <- which(m == "#", arr.ind = TRUE) %>% as_tibble()
scaffold_cords

# COMMAND ----------

intersections <- sqldf::sqldf("
SELECT a.row, a.col, (a.row - 1) * (a.col - 1) AS alignment_parameter
FROM
  scaffold_cords a
  JOIN scaffold_cords b ON
    (
         (b.row == a.row + 0 AND b.col == a.col + 1)
      OR (b.row == a.row + 0 AND b.col == a.col - 1)
      OR (b.row == a.row + 1 AND b.col == a.col + 0)
      OR (b.row == a.row - 1 AND b.col == a.col + 0)
    )
GROUP BY 1, 2
HAVING COUNT(*) == 4
")
answer <- sum(intersections$alignment_parameter)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now for the tricky part: notifying all the other robots about the solar flare.  The vacuum robot can do this automatically if it gets into range of a robot. However, you can't see the other robots on the camera, so you need to be thorough instead: you need to make the vacuum robot <em>visit every part of the scaffold at least once</em>.</p>
# MAGIC <p>The vacuum robot normally wanders randomly, but there isn't time for that today.  Instead, you can <em>override its movement logic</em> with new rules.</p>
# MAGIC <p>Force the vacuum robot to wake up by changing the value in your ASCII program at address <code>0</code> from <code>1</code> to <code><em>2</em></code>. When you do this, you will be automatically prompted for the new movement rules that the vacuum robot should use. The ASCII program will use input instructions to receive them, but they need to be provided as ASCII code; end each line of logic with a single newline, ASCII code <code>10</code>.</p>
# MAGIC <p>First, you will be prompted for the <em>main movement routine</em>.  The main routine may only call the <em>movement functions</em>: <code>A</code>, <code>B</code>, or <code>C</code>. Supply the movement functions to use as ASCII text, separating them with commas (<code>,</code>, ASCII code <code>44</code>), and ending the list with a newline (ASCII code <code>10</code>). For example, to call <code>A</code> twice, then alternate between <code>B</code> and <code>C</code> three times, provide the string <code>A,A,B,C,B,C,B,C</code> and then a newline.</p>
# MAGIC <p>Then, you will be prompted for each <em>movement function</em>. Movement functions may use <code>L</code> to <em>turn left</em>, <code>R</code> to <em>turn right</em>, or a number to <em>move forward</em> that many units.  Movement functions may not call other movement functions.  Again, separate the actions with commas and end the list with a newline.  For example, to move forward <code>10</code> units, turn left, move forward <code>8</code> units, turn right, and finally move forward <code>6</code> units, provide the string <code>10,L,8,R,6</code> and then a newline.</p>
# MAGIC <p>Finally, you will be asked whether you want to see a <em>continuous video feed</em>; provide either <code>y</code> or <code>n</code> and a newline.  Enabling the continuous video feed can help you see what's going on, but it also requires a significant amount of processing power, and may even cause your Intcode computer to overheat.</p>
# MAGIC <p>Due to the limited amount of memory in the vacuum robot, the ASCII definitions of the main routine and the movement functions may each contain <em>at most 20 characters</em>, not counting the newline.</p>
# MAGIC <p>For example, consider the following camera feed:</p>
# MAGIC <pre><code>#######...#####
# MAGIC #.....#...#...#
# MAGIC #.....#...#...#
# MAGIC ......#...#...#
# MAGIC ......#...###.#
# MAGIC ......#.....#.#
# MAGIC ^########...#.#
# MAGIC ......#.#...#.#
# MAGIC ......#########
# MAGIC ........#...#..
# MAGIC ....#########..
# MAGIC ....#...#......
# MAGIC ....#...#......
# MAGIC ....#...#......
# MAGIC ....#####......
# MAGIC </code></pre>
# MAGIC <p>In order for the vacuum robot to <em>visit every part of the scaffold at least once</em>, one path it could take is:</p>
# MAGIC <pre><code>R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2</code></pre>
# MAGIC <p>Without the memory limit, you could just supply this whole string to function <code>A</code> and have the main routine call <code>A</code> once.  However, you'll need to split it into smaller parts.</p>
# MAGIC <p>One approach is:</p>
# MAGIC <ul>
# MAGIC <li><em>Main routine: <code>A,B,C,B,A,C</code></em><br>(ASCII input: <code>65</code>, <code>44</code>, <code>66</code>, <code>44</code>, <code>67</code>, <code>44</code>, <code>66</code>, <code>44</code>, <code>65</code>, <code>44</code>, <code>67</code>, <code>10</code>)</li>
# MAGIC <li><em>Function <code>A</code>:&nbsp;&nbsp;&nbsp;<code>R,8,R,8</code></em><br>(ASCII input: <code>82</code>, <code>44</code>, <code>56</code>, <code>44</code>, <code>82</code>, <code>44</code>, <code>56</code>, <code>10</code>)</li>
# MAGIC <li><em>Function <code>B</code>:&nbsp;&nbsp;&nbsp;<code>R,4,R,4,R,8</code></em><br>(ASCII input: <code>82</code>, <code>44</code>, <code>52</code>, <code>44</code>, <code>82</code>, <code>44</code>, <code>52</code>, <code>44</code>, <code>82</code>, <code>44</code>, <code>56</code>, <code>10</code>)</li>
# MAGIC <li><em>Function <code>C</code>:&nbsp;&nbsp;&nbsp;<code>L,6,L,2</code></em><br>(ASCII input: <code>76</code>, <code>44</code>, <code>54</code>, <code>44</code>, <code>76</code>, <code>44</code>, <code>50</code>, <code>10</code>)</li>
# MAGIC </ul>
# MAGIC <p>Visually, this would break the desired path into the following parts:</p>
# MAGIC <pre><code>A,        B,            C,        B,            A,        C
# MAGIC R,8,R,8,  R,4,R,4,R,8,  L,6,L,2,  R,4,R,4,R,8,  R,8,R,8,  L,6,L,2
# MAGIC 
# MAGIC CCCCCCA...BBBBB
# MAGIC C.....A...B...B
# MAGIC C.....A...B...B
# MAGIC ......A...B...B
# MAGIC ......A...CCC.B
# MAGIC ......A.....C.B
# MAGIC ^AAAAAAAA...C.B
# MAGIC ......A.A...C.B
# MAGIC ......AAAAAA#AB
# MAGIC ........A...C..
# MAGIC ....BBBB#BBBB..
# MAGIC ....B...A......
# MAGIC ....B...A......
# MAGIC ....B...A......
# MAGIC ....BBBBA......
# MAGIC </code></pre>
# MAGIC <p>Of course, the scaffolding outside your ship is much more complex.</p>
# MAGIC <p>As the vacuum robot finds other robots and notifies them of the impending solar flare, it also can't help but leave them squeaky clean, collecting any space dust it finds. Once it finishes the programmed set of movements, assuming it hasn't drifted off into space, the cleaning robot will return to its docking station and report the amount of space dust it collected as a large, non-ASCII value in a single output instruction.</p>
# MAGIC <p>After visiting every part of the scaffold at least once, <em>how much dust does the vacuum robot report it has collected?</em></p>
# MAGIC </article>

# COMMAND ----------

result %>% cat()

# COMMAND ----------

# Solution is:
#   A: R,12,L,10,L,10,
#   B: L,6,L,12,R,12,L,4,
#   A: R,12,L,10,L,10,
#   B: L,6,L,12,R,12,L,4,
#   C: L,12,R,12,L,6,
#   B: L,6,L,12,R,12,L,4,
#   C: L,12,R,12,L,6,
#   A: R,12,L,10,L,10,
#   C: L,12,R,12,L,6,
#   C: L,12,R,12,L,6

input_sequence_str <- "A,B,A,B,C,B,C,A,C,C
R,12,L,10,L,10
L,6,L,12,R,12,L,4
L,12,R,12,L,6
n
"
input_sequence <- utf8ToInt(input_sequence_str)

bot <- create_bot(sequence)
bot$instructions[list(0, 1)] <- 2

# COMMAND ----------

while(length(input_sequence) > 0) {
  bot <- run_bot(bot, input_sequence[1])
  if (bot$needs_input) input_sequence <- input_sequence[-1]
  cat(intToUtf8(bot$output))
  bot$output <- NULL
}

# COMMAND ----------

while(!bot$is_halted) {
  bot <- run_bot(bot, NULL)
  if (bot$output > 256) break
  if (bot$needs_input) {
    message("Why would it need input?")
    break
  }
}

answer <- bot$output
answer
