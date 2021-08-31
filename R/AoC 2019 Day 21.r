# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Springdroid Adventure ---</h2><p>You lift off from Pluto and start flying in the direction of Santa.</p>
# MAGIC <p>While experimenting further with the tractor beam, you accidentally pull an asteroid directly into your ship!  It deals significant damage to your hull and causes your ship to begin tumbling violently.</p>
# MAGIC <p>You can send a droid out to investigate, but the tumbling is causing enough <a href="https://en.wikipedia.org/wiki/Artificial_gravity">artificial gravity</a> that one wrong step could send the droid through a hole in the hull and flying out into space.</p>
# MAGIC <p>The clear choice for this mission is a <span title="I picture the Bouncy enemy from Kirby games.">droid</span> that can <em>jump</em> over the holes in the hull - a <em>springdroid</em>.</p>
# MAGIC <p>You can use an <a href="9">Intcode</a> program (your puzzle input) running on an <a href="17">ASCII-capable</a> computer to <a href="https://en.wikipedia.org/wiki/Programmable_read-only_memory">program</a> the springdroid. However, springdroids don't run Intcode; instead, they run a simplified assembly language called <em>springscript</em>.</p>
# MAGIC <p>While a springdroid is certainly capable of navigating the artificial gravity and giant holes, it has one downside: it can only remember at most <em>15</em> springscript instructions.</p>
# MAGIC <p>The springdroid will move forward automatically, constantly thinking about <em>whether to jump</em>.  The springscript program defines the logic for this decision.</p>
# MAGIC <p>Springscript programs only use <a href="https://en.wikipedia.org/wiki/Boolean_data_type">Boolean values</a>, not numbers or strings.  Two registers are available: <code>T</code>, the <em>temporary value</em> register, and <code>J</code>, the <em>jump</em> register.  If the jump register is <em>true</em> at the end of the springscript program, the springdroid will try to jump. Both of these registers start with the value <em>false</em>.</p>
# MAGIC <p>Springdroids have a sensor that can detect <em>whether there is ground</em> at various distances in the direction it is facing; these values are provided in <em>read-only registers</em>.  Your springdroid can detect ground at four distances: one tile away (<code>A</code>), two tiles away (<code>B</code>), three tiles away (<code>C</code>), and four tiles away (<code>D</code>). If there is ground at the given distance, the register will be <em>true</em>; if there is a hole, the register will be <em>false</em>.</p>
# MAGIC <p>There are only <em>three instructions</em> available in springscript:</p>
# MAGIC <ul>
# MAGIC <li><code>AND X Y</code> sets <code>Y</code> to <em>true</em> if both <code>X</code> and <code>Y</code> are <em>true</em>; otherwise, it sets <code>Y</code> to <em>false</em>.</li>
# MAGIC <li><code>OR X Y</code> sets <code>Y</code> to <em>true</em> if at least one of <code>X</code> or <code>Y</code> is <em>true</em>; otherwise, it sets <code>Y</code> to <em>false</em>.</li>
# MAGIC <li><code>NOT X Y</code> sets <code>Y</code> to <em>true</em> if <code>X</code> is <em>false</em>; otherwise, it sets <code>Y</code> to <em>false</em>.</li>
# MAGIC </ul>
# MAGIC <p>In all three instructions, the second argument (<code>Y</code>) needs to be a <em>writable register</em> (either <code>T</code> or <code>J</code>). The first argument (<code>X</code>) can be <em>any register</em> (including <code>A</code>, <code>B</code>, <code>C</code>, or <code>D</code>).</p>
# MAGIC <p>For example, the one-instruction program <code>NOT A J</code> means "if the tile immediately in front of me is not ground, jump".</p>
# MAGIC <p>Or, here is a program that jumps if a three-tile-wide hole (with ground on the other side of the hole) is detected:</p>
# MAGIC <pre><code>NOT A J
# MAGIC NOT B T
# MAGIC AND T J
# MAGIC NOT C T
# MAGIC AND T J
# MAGIC AND D J
# MAGIC </code></pre>
# MAGIC <p>The Intcode program expects ASCII inputs and outputs.  It will begin by displaying a prompt; then, input the desired instructions one per line. End each line with a newline (ASCII code <code>10</code>). <em>When you have finished entering your program</em>, provide the command <code>WALK</code> followed by a newline to instruct the springdroid to begin surveying the hull.</p>
# MAGIC <p>If the springdroid <em>falls into space</em>, an ASCII rendering of the last moments of its life will be produced.  In these, <code>@</code> is the springdroid, <code>#</code> is hull, and <code>.</code> is empty space.  For example, suppose you program the springdroid like this:
# MAGIC </p><pre><code>NOT D J
# MAGIC WALK
# MAGIC </code></pre>
# MAGIC <p>This one-instruction program sets <code>J</code> to <em>true</em> if and only if there is no ground four tiles away.  In other words, it attempts to jump into any hole it finds:</p>
# MAGIC <pre><code>.................
# MAGIC .................
# MAGIC <em>@</em>................
# MAGIC #####.###########
# MAGIC 
# MAGIC .................
# MAGIC .................
# MAGIC .<em>@</em>...............
# MAGIC #####.###########
# MAGIC 
# MAGIC .................
# MAGIC ..<em>@</em>..............
# MAGIC .................
# MAGIC #####.###########
# MAGIC 
# MAGIC ...<em>@</em>.............
# MAGIC .................
# MAGIC .................
# MAGIC #####.###########
# MAGIC 
# MAGIC .................
# MAGIC ....<em>@</em>............
# MAGIC .................
# MAGIC #####.###########
# MAGIC 
# MAGIC .................
# MAGIC .................
# MAGIC .....<em>@</em>...........
# MAGIC #####.###########
# MAGIC 
# MAGIC .................
# MAGIC .................
# MAGIC .................
# MAGIC #####<em>@</em>###########
# MAGIC </code></pre>
# MAGIC <p>However, if the springdroid successfully makes it across, it will use an output instruction to indicate the <em>amount of damage to the hull</em> as a single giant integer outside the normal ASCII range.</p>
# MAGIC <p>Program the springdroid with logic that allows it to survey the hull without falling into space.  <em>What amount of hull damage does it report?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "109,2050,21101,966,0,1,21101,13,0,0,1106,0,1378,21102,1,20,0,1105,1,1337,21101,27,0,0,1106,0,1279,1208,1,65,748,1005,748,73,1208,1,79,748,1005,748,110,1208,1,78,748,1005,748,132,1208,1,87,748,1005,748,169,1208,1,82,748,1005,748,239,21102,1041,1,1,21102,1,73,0,1106,0,1421,21101,0,78,1,21101,1041,0,2,21102,1,88,0,1106,0,1301,21101,0,68,1,21101,1041,0,2,21101,0,103,0,1105,1,1301,1102,1,1,750,1105,1,298,21101,0,82,1,21102,1041,1,2,21101,125,0,0,1105,1,1301,1101,0,2,750,1106,0,298,21102,79,1,1,21102,1,1041,2,21101,0,147,0,1105,1,1301,21102,84,1,1,21101,1041,0,2,21102,162,1,0,1106,0,1301,1101,3,0,750,1106,0,298,21102,65,1,1,21102,1,1041,2,21101,184,0,0,1106,0,1301,21102,76,1,1,21101,1041,0,2,21102,1,199,0,1106,0,1301,21101,0,75,1,21102,1041,1,2,21101,214,0,0,1105,1,1301,21101,221,0,0,1105,1,1337,21102,10,1,1,21101,0,1041,2,21101,0,236,0,1105,1,1301,1106,0,553,21101,0,85,1,21102,1,1041,2,21102,254,1,0,1106,0,1301,21101,78,0,1,21102,1,1041,2,21102,1,269,0,1105,1,1301,21102,276,1,0,1105,1,1337,21101,10,0,1,21101,0,1041,2,21101,291,0,0,1106,0,1301,1101,1,0,755,1106,0,553,21101,32,0,1,21101,1041,0,2,21102,1,313,0,1106,0,1301,21102,1,320,0,1106,0,1337,21101,327,0,0,1106,0,1279,1201,1,0,749,21102,65,1,2,21101,0,73,3,21101,346,0,0,1106,0,1889,1206,1,367,1007,749,69,748,1005,748,360,1102,1,1,756,1001,749,-64,751,1105,1,406,1008,749,74,748,1006,748,381,1101,-1,0,751,1105,1,406,1008,749,84,748,1006,748,395,1102,1,-2,751,1105,1,406,21101,1100,0,1,21102,1,406,0,1106,0,1421,21102,32,1,1,21102,1100,1,2,21101,0,421,0,1106,0,1301,21102,428,1,0,1106,0,1337,21101,0,435,0,1105,1,1279,2102,1,1,749,1008,749,74,748,1006,748,453,1101,0,-1,752,1105,1,478,1008,749,84,748,1006,748,467,1101,0,-2,752,1105,1,478,21101,1168,0,1,21102,1,478,0,1106,0,1421,21101,0,485,0,1105,1,1337,21101,0,10,1,21101,1168,0,2,21102,500,1,0,1106,0,1301,1007,920,15,748,1005,748,518,21101,0,1209,1,21102,518,1,0,1105,1,1421,1002,920,3,529,1001,529,921,529,102,1,750,0,1001,529,1,537,101,0,751,0,1001,537,1,545,101,0,752,0,1001,920,1,920,1106,0,13,1005,755,577,1006,756,570,21101,0,1100,1,21101,570,0,0,1106,0,1421,21101,987,0,1,1105,1,581,21101,0,1001,1,21102,1,588,0,1106,0,1378,1101,758,0,594,102,1,0,753,1006,753,654,20101,0,753,1,21101,0,610,0,1106,0,667,21102,1,0,1,21102,1,621,0,1106,0,1463,1205,1,647,21102,1,1015,1,21101,635,0,0,1106,0,1378,21101,0,1,1,21102,646,1,0,1105,1,1463,99,1001,594,1,594,1106,0,592,1006,755,664,1101,0,0,755,1106,0,647,4,754,99,109,2,1101,726,0,757,22101,0,-1,1,21101,0,9,2,21102,1,697,3,21101,692,0,0,1105,1,1913,109,-2,2105,1,0,109,2,101,0,757,706,2101,0,-1,0,1001,757,1,757,109,-2,2105,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,255,63,127,95,159,191,223,0,238,92,110,214,173,123,213,231,162,79,205,117,59,118,233,247,136,102,93,243,126,242,50,244,47,156,51,46,232,99,158,142,106,152,204,249,251,181,53,198,199,121,201,188,169,94,186,171,139,120,172,248,227,43,54,217,185,215,124,153,216,154,71,109,100,241,207,174,125,226,254,78,116,212,200,55,187,87,250,108,85,76,253,58,237,122,234,202,166,101,170,57,140,218,42,114,69,229,98,84,182,175,137,190,119,178,60,157,228,38,111,61,62,77,203,39,143,35,113,235,155,107,168,179,230,163,34,239,56,196,138,68,246,220,206,221,222,183,219,177,141,167,49,115,189,86,103,236,245,252,70,184,197,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,73,110,112,117,116,32,105,110,115,116,114,117,99,116,105,111,110,115,58,10,13,10,87,97,108,107,105,110,103,46,46,46,10,10,13,10,82,117,110,110,105,110,103,46,46,46,10,10,25,10,68,105,100,110,39,116,32,109,97,107,101,32,105,116,32,97,99,114,111,115,115,58,10,10,58,73,110,118,97,108,105,100,32,111,112,101,114,97,116,105,111,110,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,78,68,44,32,79,82,44,32,111,114,32,78,79,84,67,73,110,118,97,108,105,100,32,102,105,114,115,116,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,44,32,66,44,32,67,44,32,68,44,32,74,44,32,111,114,32,84,40,73,110,118,97,108,105,100,32,115,101,99,111,110,100,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,74,32,111,114,32,84,52,79,117,116,32,111,102,32,109,101,109,111,114,121,59,32,97,116,32,109,111,115,116,32,49,53,32,105,110,115,116,114,117,99,116,105,111,110,115,32,99,97,110,32,98,101,32,115,116,111,114,101,100,0,109,1,1005,1262,1270,3,1262,20102,1,1262,0,109,-1,2106,0,0,109,1,21102,1288,1,0,1105,1,1263,20101,0,1262,0,1102,1,0,1262,109,-1,2105,1,0,109,5,21101,0,1310,0,1105,1,1279,21201,1,0,-2,22208,-2,-4,-1,1205,-1,1332,22101,0,-3,1,21102,1,1332,0,1106,0,1421,109,-5,2106,0,0,109,2,21101,1346,0,0,1105,1,1263,21208,1,32,-1,1205,-1,1363,21208,1,9,-1,1205,-1,1363,1106,0,1373,21101,0,1370,0,1105,1,1279,1106,0,1339,109,-2,2105,1,0,109,5,2102,1,-4,1386,20101,0,0,-2,22101,1,-4,-4,21102,1,0,-3,22208,-3,-2,-1,1205,-1,1416,2201,-4,-3,1408,4,0,21201,-3,1,-3,1106,0,1396,109,-5,2106,0,0,109,2,104,10,22101,0,-1,1,21102,1436,1,0,1105,1,1378,104,10,99,109,-2,2105,1,0,109,3,20002,594,753,-1,22202,-1,-2,-1,201,-1,754,754,109,-3,2105,1,0,109,10,21102,5,1,-5,21101,0,1,-4,21101,0,0,-3,1206,-9,1555,21102,3,1,-6,21102,5,1,-7,22208,-7,-5,-8,1206,-8,1507,22208,-6,-4,-8,1206,-8,1507,104,64,1106,0,1529,1205,-6,1527,1201,-7,716,1515,21002,0,-11,-8,21201,-8,46,-8,204,-8,1106,0,1529,104,46,21201,-7,1,-7,21207,-7,22,-8,1205,-8,1488,104,10,21201,-6,-1,-6,21207,-6,0,-8,1206,-8,1484,104,10,21207,-4,1,-8,1206,-8,1569,21102,1,0,-9,1106,0,1689,21208,-5,21,-8,1206,-8,1583,21101,0,1,-9,1105,1,1689,1201,-5,716,1588,21001,0,0,-2,21208,-4,1,-1,22202,-2,-1,-1,1205,-2,1613,21202,-5,1,1,21101,0,1613,0,1106,0,1444,1206,-1,1634,22102,1,-5,1,21102,1627,1,0,1106,0,1694,1206,1,1634,21101,0,2,-3,22107,1,-4,-8,22201,-1,-8,-8,1206,-8,1649,21201,-5,1,-5,1206,-3,1663,21201,-3,-1,-3,21201,-4,1,-4,1106,0,1667,21201,-4,-1,-4,21208,-4,0,-1,1201,-5,716,1676,22002,0,-1,-1,1206,-1,1686,21102,1,1,-4,1105,1,1477,109,-10,2105,1,0,109,11,21101,0,0,-6,21102,0,1,-8,21102,1,0,-7,20208,-6,920,-9,1205,-9,1880,21202,-6,3,-9,1201,-9,921,1724,21001,0,0,-5,1001,1724,1,1732,21002,0,1,-4,21202,-4,1,1,21101,0,1,2,21102,1,9,3,21101,0,1754,0,1105,1,1889,1206,1,1772,2201,-10,-4,1767,1001,1767,716,1767,20102,1,0,-3,1106,0,1790,21208,-4,-1,-9,1206,-9,1786,22102,1,-8,-3,1106,0,1790,22101,0,-7,-3,1001,1732,1,1796,20101,0,0,-2,21208,-2,-1,-9,1206,-9,1812,21202,-8,1,-1,1105,1,1816,21201,-7,0,-1,21208,-5,1,-9,1205,-9,1837,21208,-5,2,-9,1205,-9,1844,21208,-3,0,-1,1105,1,1855,22202,-3,-1,-1,1105,1,1855,22201,-3,-1,-1,22107,0,-1,-1,1106,0,1855,21208,-2,-1,-9,1206,-9,1869,21201,-1,0,-8,1106,0,1873,21202,-1,1,-7,21201,-6,1,-6,1106,0,1708,21202,-8,1,-10,109,-11,2106,0,0,109,7,22207,-6,-5,-3,22207,-4,-6,-2,22201,-3,-2,-1,21208,-1,0,-6,109,-7,2106,0,0,0,109,5,1201,-2,0,1912,21207,-4,0,-1,1206,-1,1930,21101,0,0,-4,21201,-4,0,1,21201,-3,0,2,21101,0,1,3,21102,1949,1,0,1105,1,1954,109,-5,2105,1,0,109,6,21207,-4,1,-1,1206,-1,1977,22207,-5,-3,-1,1206,-1,1977,21201,-5,0,-5,1106,0,2045,21202,-5,1,1,21201,-4,-1,2,21202,-3,2,3,21102,1996,1,0,1106,0,1954,22102,1,1,-5,21101,1,0,-2,22207,-5,-3,-1,1206,-1,2015,21102,0,1,-2,22202,-3,-2,-3,22107,0,-4,-1,1206,-1,2037,22102,1,-2,1,21102,1,2037,0,105,1,1912,21202,-3,-1,-3,22201,-5,-3,-5,109,-6,2105,1,0"

# COMMAND ----------

sequence <- str_split(input, ",") %>% unlist() %>% parse_integer()
sequence

# COMMAND ----------

Rcpp::cppFunction('
int64_t run_instructions(std::vector<int> sequence, std::deque<int> input) {
  std::map<int64_t, int64_t> instructions;
  int64_t relative_base = 0;
  int64_t value;
  int64_t i;

  for (int j = 0; j < sequence.size(); ++j) {
    instructions[j] = sequence[j];
  }

  auto get_param = [&](int param) -> decltype(auto) {
    int index_mode = (value % (100 * int64_t(std::pow(10, param)))) / (10 * int64_t(std::pow(10, param)));
    int index = i + param;
    if (index_mode == 0) index = instructions[index];
    if (index_mode == 2) index = instructions[index] + relative_base;
    return instructions[index];
  };

  for (i = 0; instructions[i] != 99; ++i) {
    value = instructions[i];

    int64_t op_code = value % 100;
    auto& p1 = get_param(1);
    auto& p2 = get_param(2);
    auto& p3 = get_param(3);

    switch (op_code) {
      case 1:
        p3 = p1 + p2;
        i += 3;
        break;
      case 2:
        p3 = p1 * p2;
        i += 3;
        break;
      case 3:
        if (input.empty()) Rcpp::stop("Needs input");
        p1 = input.front();
        input.pop_front();
        i += 1;
        break;
      case 4:
        if (p1 > 256) return p1;
        std::cout << char(p1);
        i += 1;
        break;
      case 5:
        if (p1 != 0) {
          i = p2 - 1;
          continue;
        }
        i += 2;
        break;
      case 6:
        if (p1 == 0) {
          i = p2 - 1;
          continue;
        }
        i += 2;
        break;
      case 7:
        p3 = p1 < p2;
        i += 3;
        break;
      case 8:
        p3 = p1 == p2;
        i += 3;
        break;
      case 9:
        relative_base += p1;
        i += 1;
        break;
      default:
        Rcpp::stop("Unknown opcode: " + std::to_string(op_code));
    }
  }
  Rcpp::stop("Instructions finished");
}
',
  plugins = "cpp17"
)

# COMMAND ----------

# When you jump, you land on D

# NOT A J                    Jump if there is no next square .???
# NOT C T; AND D T; OR T J   Jump if ??.#    (NOT C AND D)

input_str <- "NOT A J
NOT C T
AND D T
OR T J
WALK
"

answer <- run_instructions(sequence, utf8ToInt(input_str))
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>There are many areas the springdroid can't reach.  You flip through the manual and discover a way to <em>increase its sensor range</em>.</p>
# MAGIC <p>Instead of ending your springcode program with <code>WALK</code>, use <code>RUN</code>. Doing this will enable <em>extended sensor mode</em>, capable of sensing ground up to <em>nine tiles away</em>. This data is available in <em>five new read-only registers</em>:</p>
# MAGIC <ul>
# MAGIC <li>Register <code>E</code> indicates whether there is ground <em>five</em> tiles away.</li>
# MAGIC <li>Register <code>F</code> indicates whether there is ground <em>six</em> tiles away.</li>
# MAGIC <li>Register <code>G</code> indicates whether there is ground <em>seven</em> tiles away.</li>
# MAGIC <li>Register <code>H</code> indicates whether there is ground <em>eight</em> tiles away.</li>
# MAGIC <li>Register <code>I</code> indicates whether there is ground <em>nine</em> tiles away.</li>
# MAGIC </ul>
# MAGIC <p>All other functions remain the same.</p>
# MAGIC <p>Successfully survey the rest of the hull by ending your program with <code>RUN</code>.  <em>What amount of hull damage does the springdroid now report?</em></p>
# MAGIC </article>

# COMMAND ----------

# If B or C is a hole, jump
#   NOT B J
#   NOT C T
#   OR T J

# If A is a hole, jump
#   NOT A T
#   OR T J

# If D is a hole, don't jump
#   AND D J

# If E is a hole and H is a hole, don't jump
#   NOT E T
#   AND H T
#   OR E T
#   AND T J

input_str <- "NOT B J
NOT C T
OR T J
NOT A T
OR T J
AND D J
NOT E T
AND H T
OR E T
AND T J
RUN
"

answer <- run_instructions(sequence, utf8ToInt(input_str))
answer
