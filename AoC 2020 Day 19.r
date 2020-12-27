# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/19
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 19: Monster Messages ---</h2><p>You land in an airport surrounded by dense forest. As you walk to your high-speed train, the Elves at the <span title="This is a purely fictional organization. Any resemblance to actual organizations, past or present, is purely coincidental.">Mythical Information Bureau</span> contact you again. They think their satellite has collected an image of a <em>sea monster</em>! Unfortunately, the connection to the satellite is having problems, and many of the messages sent back from the satellite have been corrupted.</p>
# MAGIC <p>They sent you a list of <em>the rules valid messages should obey</em> and a list of <em>received messages</em> they've collected so far (your puzzle input).</p>
# MAGIC <p>The <em>rules for valid messages</em> (the top part of your puzzle input) are numbered and build upon each other. For example:</p>
# MAGIC <pre><code>0: 1 2
# MAGIC 1: "a"
# MAGIC 2: 1 3 | 3 1
# MAGIC 3: "b"
# MAGIC </code></pre>
# MAGIC <p>Some rules, like <code>3: "b"</code>, simply match a single character (in this case, <code>b</code>).</p>
# MAGIC <p>The remaining rules list the sub-rules that must be followed; for example, the rule <code>0: 1 2</code> means that to match rule <code>0</code>, the text being checked must match rule <code>1</code>, and the text after the part that matched rule <code>1</code> must then match rule <code>2</code>.</p>
# MAGIC <p>Some of the rules have multiple lists of sub-rules separated by a pipe (<code>|</code>). This means that <em>at least one</em> list of sub-rules must match. (The ones that match might be different each time the rule is encountered.) For example, the rule <code>2: 1 3 | 3 1</code> means that to match rule <code>2</code>, the text being checked must match rule <code>1</code> followed by rule <code>3</code> <em>or</em> it must match rule <code>3</code> followed by rule <code>1</code>.</p>
# MAGIC <p>Fortunately, there are no loops in the rules, so the list of possible matches will be finite. Since rule <code>1</code> matches <code>a</code> and rule <code>3</code> matches <code>b</code>, rule <code>2</code> matches either <code>ab</code> or <code>ba</code>. Therefore, rule <code>0</code> matches <code>aab</code> or <code>aba</code>.</p>
# MAGIC <p>Here's a more interesting example:</p>
# MAGIC <pre><code>0: 4 1 5
# MAGIC 1: 2 3 | 3 2
# MAGIC 2: 4 4 | 5 5
# MAGIC 3: 4 5 | 5 4
# MAGIC 4: "a"
# MAGIC 5: "b"
# MAGIC </code></pre>
# MAGIC <p>Here, because rule <code>4</code> matches <code>a</code> and rule <code>5</code> matches <code>b</code>, rule <code>2</code> matches two letters that are the same (<code>aa</code> or <code>bb</code>), and rule <code>3</code> matches two letters that are different (<code>ab</code> or <code>ba</code>).</p>
# MAGIC <p>Since rule <code>1</code> matches rules <code>2</code> and <code>3</code> once each in either order, it must match two pairs of letters, one pair with matching letters and one pair with different letters. This leaves eight possibilities: <code>aaab</code>, <code>aaba</code>, <code>bbab</code>, <code>bbba</code>, <code>abaa</code>, <code>abbb</code>, <code>baaa</code>, or <code>babb</code>.</p>
# MAGIC <p>Rule <code>0</code>, therefore, matches <code>a</code> (rule <code>4</code>), then any of the eight options from rule <code>1</code>, then <code>b</code> (rule <code>5</code>): <code>aaaabb</code>, <code>aaabab</code>, <code>abbabb</code>, <code>abbbab</code>, <code>aabaab</code>, <code>aabbbb</code>, <code>abaaab</code>, or <code>ababbb</code>.</p>
# MAGIC <p>The <em>received messages</em> (the bottom part of your puzzle input) need to be checked against the rules so you can determine which are valid and which are corrupted. Including the rules and the messages together, this might look like:</p>
# MAGIC <pre><code>0: 4 1 5
# MAGIC 1: 2 3 | 3 2
# MAGIC 2: 4 4 | 5 5
# MAGIC 3: 4 5 | 5 4
# MAGIC 4: "a"
# MAGIC 5: "b"
# MAGIC 
# MAGIC ababbb
# MAGIC bababa
# MAGIC abbbab
# MAGIC aaabbb
# MAGIC aaaabbb
# MAGIC </code></pre>
# MAGIC <p>Your goal is to determine <em>the number of messages that completely match rule <code>0</code></em>. In the above example, <code>ababbb</code> and <code>abbbab</code> match, but <code>bababa</code>, <code>aaabbb</code>, and <code>aaaabbb</code> do not, producing the answer <em><code>2</code></em>. The whole message must match all of rule <code>0</code>; there can't be extra unmatched characters in the message. (For example, <code>aaaabbb</code> might appear to match rule <code>0</code> above, but it has an extra unmatched <code>b</code> on the end.)</p>
# MAGIC <p><em>How many messages completely match rule <code>0</code>?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>235</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you look over the list of messages, you realize your matching rules aren't quite right. To fix them, completely replace rules <code>8: 42</code> and <code>11: 42 31</code> with the following:</p>
# MAGIC <pre><code>8: 42 | 42 8
# MAGIC 11: 42 31 | 42 11 31
# MAGIC </code></pre>
# MAGIC <p>This small change has a big impact: now, the rules <em>do</em> contain loops, and the list of messages they could hypothetically match is infinite. You'll need to determine how these changes affect which messages are valid.</p>
# MAGIC <p>Fortunately, many of the rules are unaffected by this change; it might help to start by looking at which rules always match the same set of values and how <em>those</em> rules (especially rules <code>42</code> and <code>31</code>) are used by the new versions of rules <code>8</code> and <code>11</code>.</p>
# MAGIC <p>(Remember, <em>you only need to handle the rules you have</em>; building a solution that could handle any hypothetical combination of rules would be <a href="https://en.wikipedia.org/wiki/Formal_grammar" target="_blank">significantly more difficult</a>.)</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>42: 9 14 | 10 1
# MAGIC 9: 14 27 | 1 26
# MAGIC 10: 23 14 | 28 1
# MAGIC 1: "a"
# MAGIC 11: 42 31
# MAGIC 5: 1 14 | 15 1
# MAGIC 19: 14 1 | 14 14
# MAGIC 12: 24 14 | 19 1
# MAGIC 16: 15 1 | 14 14
# MAGIC 31: 14 17 | 1 13
# MAGIC 6: 14 14 | 1 14
# MAGIC 2: 1 24 | 14 4
# MAGIC 0: 8 11
# MAGIC 13: 14 3 | 1 12
# MAGIC 15: 1 | 14
# MAGIC 17: 14 2 | 1 7
# MAGIC 23: 25 1 | 22 14
# MAGIC 28: 16 1
# MAGIC 4: 1 1
# MAGIC 20: 14 14 | 1 15
# MAGIC 3: 5 14 | 16 1
# MAGIC 27: 1 6 | 14 18
# MAGIC 14: "b"
# MAGIC 21: 14 1 | 1 14
# MAGIC 25: 1 1 | 1 14
# MAGIC 22: 14 14
# MAGIC 8: 42
# MAGIC 26: 14 22 | 1 20
# MAGIC 18: 15 15
# MAGIC 7: 14 5 | 1 21
# MAGIC 24: 14 1
# MAGIC 
# MAGIC abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# MAGIC bbabbbbaabaabba
# MAGIC babbbbaabbbbbabbbbbbaabaaabaaa
# MAGIC aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# MAGIC bbbbbbbaaaabbbbaaabbabaaa
# MAGIC bbbababbbbaaaaaaaabbababaaababaabab
# MAGIC ababaaaaaabaaab
# MAGIC ababaaaaabbbaba
# MAGIC baabbaaaabbaaaababbaababb
# MAGIC abbbbabbbbaaaababbbbbbaaaababb
# MAGIC aaaaabbaabaaaaababaa
# MAGIC aaaabbaaaabbaaa
# MAGIC aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# MAGIC babaaabbbaaabaababbaabababaaab
# MAGIC aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
# MAGIC </code></pre>
# MAGIC <p>Without updating rules <code>8</code> and <code>11</code>, these rules only match three messages: <code>bbabbbbaabaabba</code>, <code>ababaaaaaabaaab</code>, and <code>ababaaaaabbbaba</code>.</p>
# MAGIC <p>However, after updating rules <code>8</code> and <code>11</code>, a total of <em><code>12</code></em> messages match:</p>
# MAGIC <ul>
# MAGIC <li><code>bbabbbbaabaabba</code></li>
# MAGIC <li><code>babbbbaabbbbbabbbbbbaabaaabaaa</code></li>
# MAGIC <li><code>aaabbbbbbaaaabaababaabababbabaaabbababababaaa</code></li>
# MAGIC <li><code>bbbbbbbaaaabbbbaaabbabaaa</code></li>
# MAGIC <li><code>bbbababbbbaaaaaaaabbababaaababaabab</code></li>
# MAGIC <li><code>ababaaaaaabaaab</code></li>
# MAGIC <li><code>ababaaaaabbbaba</code></li>
# MAGIC <li><code>baabbaaaabbaaaababbaababb</code></li>
# MAGIC <li><code>abbbbabbbbaaaababbbbbbaaaababb</code></li>
# MAGIC <li><code>aaaaabbaabaaaaababaa</code></li>
# MAGIC <li><code>aaaabbaabbaaaaaaabbbabbbaaabbaabaaa</code></li>
# MAGIC <li><code>aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba</code></li>
# MAGIC </ul>
# MAGIC <p><em>After updating rules <code>8</code> and <code>11</code>, how many messages completely match rule <code>0</code>?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>379</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
# MAGIC <p>At this point, you should <a href="/2020">return to your Advent calendar</a> and try another puzzle.</p>
# MAGIC <p>If you still want to see it, you can <a href="19/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Monster+Messages%22+%2D+Day+19+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F19&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Monster+Messages%22+%2D+Day+19+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F19'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- '25: 53 116
122: 116 92 | 53 53
100: 53 73 | 116 125
111: 67 116 | 91 53
71: 116 58 | 53 78
55: 116 54 | 53 21
123: 53 97 | 116 108
104: 56 116 | 125 53
19: 125 53
56: 116 116 | 116 53
60: 116 121 | 53 59
75: 53 20 | 116 124
6: 53 131 | 116 33
62: 53 53 | 116 116
101: 116 127 | 53 26
128: 116 125 | 53 93
34: 53 28 | 116 125
65: 63 116 | 135 53
50: 32 53 | 76 116
2: 53 10 | 116 132
133: 28 53 | 131 116
85: 53 131
125: 116 53
118: 87 116 | 3 53
135: 73 53 | 125 116
28: 53 53
110: 116 122 | 53 56
91: 5 53 | 74 116
73: 92 116 | 53 53
80: 15 116 | 109 53
124: 128 116 | 17 53
87: 92 53 | 53 116
43: 116 27 | 53 37
66: 46 53 | 93 116
106: 116 77 | 53 83
137: 72 116 | 104 53
93: 116 116 | 53 116
129: 92 103
12: 116 56 | 53 131
45: 53 132 | 116 12
102: 65 116 | 2 53
24: 116 101 | 53 95
14: 116 84 | 53 29
57: 93 116 | 56 53
70: 108 116 | 100 53
51: 116 1 | 53 68
26: 73 53
15: 116 93 | 53 125
42: 53 134 | 116 106
79: 116 33 | 53 122
5: 116 125 | 53 3
74: 53 122 | 116 73
18: 93 53 | 87 116
20: 47 53 | 17 116
114: 116 85 | 53 118
37: 53 73 | 116 87
47: 116 73 | 53 125
107: 116 3 | 53 46
69: 53 25 | 116 125
32: 53 28 | 116 93
76: 3 53 | 125 116
38: 92 33
119: 116 39 | 53 80
8: 42
21: 125 53 | 125 116
58: 75 116 | 119 53
64: 116 44 | 53 113
68: 90 53 | 45 116
1: 23 116 | 60 53
53: "a"
81: 73 53 | 33 116
86: 116 129 | 53 35
90: 110 116 | 13 53
82: 53 93 | 116 25
95: 99 116 | 66 53
27: 116 56 | 53 3
120: 116 51 | 53 40
126: 116 96 | 53 52
116: "b"
84: 116 123 | 53 49
134: 116 61 | 53 14
78: 116 102 | 53 86
96: 130 53 | 98 116
10: 87 116 | 33 53
88: 53 116 | 116 92
40: 126 53 | 24 116
127: 56 116
59: 87 53 | 3 116
11: 42 31
41: 116 137 | 53 16
44: 116 22 | 53 79
109: 88 53 | 87 116
49: 136 116 | 94 53
113: 107 116 | 81 53
77: 116 64 | 53 36
3: 53 116 | 53 53
9: 133 53 | 112 116
98: 92 93
117: 3 92
39: 53 19 | 116 21
16: 6 116 | 117 53
132: 131 116 | 125 53
63: 116 122 | 53 33
22: 131 116 | 56 53
89: 116 125 | 53 131
115: 55 53 | 50 116
99: 116 33 | 53 93
92: 116 | 53
121: 53 73 | 116 56
13: 73 92
103: 53 3 | 116 62
83: 111 116 | 41 53
61: 105 116 | 115 53
130: 56 92
136: 33 116 | 125 53
30: 53 76 | 116 7
94: 92 87
52: 97 116 | 18 53
7: 116 28 | 53 46
97: 25 53 | 33 116
35: 89 116 | 82 53
72: 53 131 | 116 87
48: 34 116 | 38 53
54: 116 46 | 53 131
131: 116 116
23: 116 4 | 53 57
31: 116 71 | 53 120
29: 116 30 | 53 114
108: 116 25 | 53 46
33: 92 92
4: 131 116 | 3 53
36: 70 116 | 9 53
67: 69 116 | 117 53
0: 8 11
105: 48 116 | 43 53
46: 116 53 | 53 116
17: 93 116 | 122 53
112: 122 53 | 3 116

babbbbabaabaaabbbbbaaabbbbababba
ababaaaaabbbabbbbbabbbba
aabbaabaabbababaababbaba
bbbbabaaabaaabbbbbbbbaab
babbbabababaabbaaaabbbba
bbaabbababbaaabaaaababbbabaaaaaaaaaaababbaabbbbaaaaaaabaabababbbbabbbaababbbaabbbbababab
babbabbabbaababbbbbbbaab
baababababbaababaaabaaab
aababaababbaaaabbbababbbbbbbbbaabbbbabbbbbabbababbababaabaabaaaabbabaaaaabbaaaaa
baabbbbaaabbabbbababbbba
baabbabaaaaababbaababbbbaababaaabbbbbaaabababaab
babbabbabaabbabbaabbabaa
baaabbbbabbaaabbaaaaaabbbbabaaba
abababbaaabaabbbabbbaaaa
ababababbbbaaaababaabaaa
baaababbbbbabababbbaaabaaaabaababaaabbbbaaabbbbaabbaabbbabbbaaab
babaaabaabbabaababbabaaaabbbaaaa
ababaaabaabaabaabbbbababbbaabababaababaaabaabbbb
abbaaaabaabababaabaabbaa
baaaaaabaaaaababbababaaa
aabaaabbababaabbbaaabbbbaabbbaaa
baaabbbaaaaaaaaaaabbbbba
abbbbbabbbbabaabaabbbbabbbaabaabaabbbbbb
baabbbababababbabbaaaaaaabbbaabbbababbbaababaaaaaabbbbaa
bbbbbbbbabababaabaaabbbabbaaabbbaaaaaabaabbaabbabbabbbba
abaabbabaabaaaaabaabaaaa
aabababbababaaaaabbbbbaa
bbbabbaaabaaaababababbbabbbaabab
aabababbaabbbababaabaaab
aabaaababaabbabaaabaaaab
abbbabaabbaabbabaaabbbba
baaabbbbaababbabbbbabbaabaabbbbbabbbbabbbabbaaba
bbaaababaabaaabbabbbbbabbabaaabbbbaabbbbaabbbaaabbabbabb
baabaabaaababbbbbbaabbaa
bbaaabbbbababbabaaaababa
bbabbbbabaaaaabbbaaaaababbbbbaaabaababbbbabbabaabaabbabaabbababbaaaaaaabbbabaaabbbbbbabb
abaabbbababaaaabaabbbbbbbbabbbab
ababaaaaabababbabbbaababbaaabbaaabbaaaba
bbabbaabababbabbbaaaaaabaaabaabb
baabaaaaababbbbabbabbabbbababbaa
aaaaaaaabaaabaabababaaba
baabbababaaabaaaaabaabaaaababbbbaaabbbbb
abaaaabaabbababaababbbab
bbaaabababbababbababbbbb
baababbaaaabababbaaaaaabbaaaabbb
bbbbbbbaabababbabbabbbba
bbaaaaaaaabaabbbabaabbaa
abbabababbaaaaababbbabbbbbaaaaaaababaaaababaaaba
abaababbaabaaaaaaabaaaab
abababaabbaaabbaabababbaaabbabaa
babbabbbbbbbbbbabbaabbaa
bbabbbaaaabaaababbaaababbaaabaabaabbbaababbaabaaaabbbaaaabbaabbbaabbbbba
abbbaabbababaaabbababbbaabbbbababababaaa
bbaaabbabbbaabaaabbbabaaaaababbbbaababbb
baabaaaabbaaabbaaabbaababbbbbbababbbabbbbbbabbba
abaabbbaabaababaaaabbabb
bbbbabaaaabaabbbbbbbbaab
bbaaaaabababbabbaababbab
babbaabaabbbbaaaaabbbbbb
baaabaabbbbbaaaaabbbaaab
aaabbaabbabbabbbbabbbbba
aabbababaabababaaabbabbbbbbbbbbaaaabbaaaababbabbabaaabaabbababaabbbbbabbbabbbbabaabaabaabaababba
ababaabbaabbbabababbabab
bbbabbbabaaabbbaaaabbbab
aabababbaabaabaaabaaabbbaabbbaaa
aaaaaabaabbabbaabbbbaaaaaabbaabbaaabaaaaabbbbaabaaaabbbaababbbbbababbaaa
ababaabbabababbabababbbaaabababaaabbbbaaaabbbabb
babbabbaabbabbbaababaaba
abbbbaaabbbbbbbabbababbbbaabbaab
babbaabaabbbbabbaaaaaaabaabbabba
bbaaababbaabbabbbbbbabbbbabbabaabbabaaaa
aaabaabaaabbababbababaab
bbaaabbbababaabbaabaaababaabbbbbbbabbaaa
abbabbbabaaabbbbbabbbabaaabbaabababbbbbaabbbaabababaabba
aaaaaaaaabbabbaabbabbbaaaabababbbaaabaababaabbaabbababab
aabbbabababbabaaaaabababbabbbbba
abbababbbbbbabbaaabbbbbb
bbbbbbbaabaaaaababbaabbb
aabababbabaaabbaababbaaabbbbababbbabbabbbaaababbabbbbbabaaabaabaabbabaabaaabbaaa
abbbbbabbbbbabaaabaabaab
abbabbbabbbbabababbbbbba
abababbabaaaaaabbbabaaaa
aaaaababbbbbaabbaaabaabaabaaabababbabbabbbbaabbb
baabbbbabbbaaaaababaaabb
bbaaaababbaaaabaababaaaaaabbbaabbbbabaaa
babbbbbbbabbbaaabababaabbabbbaabbbaaabaa
aabaaabbaabbaabbbababaab
baaaabbbbbabbbababbaababbabaaabaabababbaabaabbabbaaaaabaabbaaabb
abababbabaabbbbaaaaababa
aabbbbabbbbbaabaaaabbaabbbabaabababbbbaabbaabbabbaabbaaa
aaabaabaaabbababbabbbababaabbabb
bbbaaababbbbbbbbbbbababbabbbaaab
bababbaaaaaabbbbbabaaaab
bbaaaabaaaaaaabababbbabaaaaabaaa
aabbabbbbbaaababbbababaa
abbaaaababbbbbabaaaaabbb
bbaaaaaabbbaabababaabaab
ababaabbabaababbbbabbaabbbbbbbbbaaabbababbabbabbabbaabaa
bbaabbbaabababbaaaababbb
bbbbabbaaabaabaababaaaaa
bbaabbababbbbaabbababbbabbbbababbbbaaabbbaaaababaababbbababbaabb
bbaaaababababbabbabbbbaaabbbaaab
babaababaaabbaabbbababaa
ababababababbaabbabababa
abbabbbbaaaaaabbabbbabaababaabbaabbbababbbbaabaaaaaaaaabbbaabbba
bbbaaabaaaaaaaaaababbabbbbaabaab
abbbaabbabbbbaaaaaaabaab
abbbbbbbaaabbbbaaaababbaaaaabbabbababaabbbaabbabaabababa
aababbaaabaababbababaabb
babbaaabaabbabbbbbabbaaaaaaabaab
aabababaabbbbabbaaaaabaaaabaabababbaaaba
baabbabbbbaaabababaabbbb
abbaaabbbbbabaabbbbbaabbabbbbaabbaabaaabaabaaaab
bbaabbbabbbbbabbbababbbb
babaababbbbababaabaaaabbbabbabaabaabababaabababb
bbababbabbaabbbbbbbbabbbabbaabaaabbbaaaabbaabaababaaaaaa
babbbbabbbbbbbaaababbbba
abbbbababbbaaaaaaaabbbab
baaaaaabaabbbaabbabbbabbabbaaabaababbaaaabbaaababbaaaaaabaaaaaabbaababababaaabbbabaabaaa
aabaabbbabbbbaaaaababbaaababaabbabbbabbababaabba
aabababbbbbbabbaabbbbbbb
baabababbbaaaaababbbbaabbabbabbbaaababbaaaabaaab
baaabbbababbaabaabbabaaa
abaababbabbbbaabaababbbbbbbaaaab
aababaababbbabbbababbaaa
baaabbbbbbbbabbabbbbbaab
bbabbaabaaabbbaaaabbbaaa
bbabaabaababbaababbbabbbabaabbabbaabbaab
bbbbbbbaaabbaabaababaaba
aababababaaabbbaababbbaa
babbbbbabbbababbaaababaaaababbaaaaabbbabaaababaaabbbbbbbbbbaaaabbaaabbaabaaaababbbaaaaab
aababbaaabaaaababbbbabaaabbbbabaabbbbabbbabbbabb
bbbaabaaaabbbbabaababbaabbabaababbaabaaaababbbba
abaabbbaabbbaaabbabaaaab
bbbbbbbbaaabbabababaaabbbbaaaabbbabaaabb
baaaaabbbaaaaabbabbaaaaa
ababaaaaaabbbaababbaabba
bbaaaaaaaaabbababaaaaaaaaabaaaab
bbbabababbbbabbaabaaaaaa
bbaaaababaaabbbabbbabaabaabaabab
bbbabbbaaabbbbaaabbaabbaabaabbbaaabbbbba
babbabbabbbbbbbaaababababaaabaabbaaaaaabaaaaabaaabbbbbbaaabbbbbabbaabbaa
ababbabbaabbaabbbaaaaabbaababaaaabbabbab
abbabbbbbaabbbbbbabaabbb
abbbaabbaaaaababbbaabbabaababaabaababaababbbbbbbbbaabaab
baaaaaaabbbabbbaaaabbbba
bbaaabbbababbbabbaaaabaabaabbabbbbbbbbbbabbabbabbababababbaababbbbabbaba
bbbbababbaabbababbabbbab
baaabaabaababbbbbbabbbbb
abbbbababbbababbbbabbababbabaabbbbaaaabb
bbaaaaaaabbbabbbabbbbbaa
bbabaabaabbabbaaababbbaa
aabbbaababaabbabbabaabba
baaabbbaaaabaababbaaaabb
babbbbaabbbbaabaabbbaaaa
abbaabbbaababbabbaaabbababbbabab
aaabaaaaaabbabababbbbabbbbabbbbbaaabaaab
babbbaababbaaaaaaabaaababbaaabbb
bbbbaababbaaaaaabbbbbaab
bbaaaaaaabbbbababaabaaab
babaababbabbabbbaabababaabaabaab
abbbabbbabbabbaaaababaababbabaab
bbbbaaaaaabbaababbabaaabbbabaaaabbabbabb
aaabbaabbaaabbbbbbbbbaaa
abbbbaabaabbbabaabaaabababaabbba
babbabbabaaababbbbaaabbababaabaabaabbaababaabaaa
babbabbaaabaabbaaaaaabaaabbbaabaabbaaaaabbbaaabaaababbaabbbbaabaabbbbaba
aabaaabbabbaaabbbabbbabb
bbaaaaaabaabbbbaabbbaaab
bbbbaaaabbbaaabaabbbbabbbababaaa
abbbabaabbabbaabbabbbbba
aaaaaaabaababbbbababbbab
abbbababbbabbbbabbbbbabbbabaaababbababaabbbaaaab
babaaabaaabbbaaaaabbbbbbabbaaaaabaabaabbabbbababaababaaaaaabbaaababbbabbbaaababb
abbababbbaaaaaabbabaaabb
bbabbababbabbaabbababbbb
babbbbaaaabbaaababbbbaaaaabbababaaabbaabbbbbaaab
aabbaabbabaaaabbaabababaabaaaabaaaabaaaaaaabaabababababa
abababbaaaabaabaaaababbb
bababbabaaabbbaaababbbbb
baaaababbabbbabababaabba
abbbbabaaaaababbbbbaabbabaaaabbaaaababba
aabbababbbaababbabaababa
babbaaabbbaabaabbbaaabbabaaaaabaabbabbaabaabbaabbbbbababbbbabbbb
aaabbbaaabbabbabaabaaaaaaabaaaaa
aababbaaaababbbbabbbaaaa
baaabbbabababbbaaabaabba
bbabbaabbbbabaaabaaabbbbbbbaabababbaabbbbabbabbaaabaaabb
baabaabaababababaaabaabb
abbababbbbbbababbbaabaab
abababbabababbabbaaaaaab
bababbbaaabaaabababababb
aabbabbbbaaababbbbabbaaa
abbaaaababbabababbaabbbabbaabaab
bbbabbbaababaaaabbbaaabababbaaaaababbabaaabbabaaaaaaabba
baabaabaababaaabbbbbababbabbabbabababbbb
bbbbbaaabbaababaabbbbbaaababaaba
bbaaaabaabbaaaabbbababbbbbbababaabbabaababbbaaaaabaabaaa
bbabaaaaababbbbbbababbbbbbbababbbabbbbab
ababababbaaabaabbbbaababaababababaabbbaaaaababbbbabaaabb
babbbabaaabbabbbaababbba
aaaaaaaababbbababbaababbabbbaabb
aababababbaaaaaabaaaaaba
aaaaaaabbaaaabaaaababaabbbabbabb
bbabbabbbbbbabbaabbbaabaababbbaabaaabababaabbbbbbabbbbbb
bbbaabbaabaaaabaabaaabaa
babaabbabbabbaaabaabaaaaabaabaaa
aababababbbbaabaabbbbbaa
baabababbaabaabbaaaaaabbaaaaabababbabbaaabbabbaaaaaaabbb
bbabaabaababbabbbabbaabb
abaaaababbbbbbbabbabaaaa
bababbabbbbbabaababbbbbb
aabbabbbbbbbabababbabaab
abbababababbabaaaabbbaaa
aabababbabbaabbbbbbaaaabbbbbaaaa
abbbabbbaaaaaaabbaabbbbb
bbbbbbbaaabaaababbbbababbabaaabaabababbb
aaaababbaaaaaabaaabaabba
abaaaabbbbbbababbbababbbabaabaaababaabaa
bbabbbaaababbabbbbbaaaab
aababaaabaabbbbbbbbabbbb
aabbbaababbbbbabbababaaa
aabbaaababbaababbbbbababbbbbababbbbbaabbbaabbbbbabaabbaabbbabbbb
baaabbbbbbbaaabaabaabaab
baaabbaaaababaabbabaaaaa
aaabababaababbabaababababbbbbbaabbabbbaabaabaabbaaabaabaababbbbb
aabaaabbbaaabaaabbbabaab
bbbaabbaababbabababbbbbababbbabbbbaabbbbbbabaaaaaaaabbab
aabbaaabbbaabbabaaababbb
bbbbabaabbbabbbaaabaaaab
aabbaabbbabaababbaababaa
aaaaaaaababbbbababaaaabaaabababbabaaababababababaaabbabbababbbbbaaaabbab
babbbbabbababbbabaabbaaa
aabbaaabbbaababbbbbbabaaababaabbbabaaabaaabbbabbababbaba
bbbaaaaabbaaabababbabbbb
bbbbabbababbaaaabbbabbbaabbaabbbbbaabaaa
aaaababbabbaababbabababb
bababbabaaabaaabbaabbbaabaaababa
babaababbaaaaaabababbaabbababbaaaaababbb
aabbabababaaabbababaaaba
bbbaaabbabaababbbababbaa
abbabbbaabbaababbabaabba
baaababbaaaaaabaaabbbaaa
baaaaaabaabababbaaabbaabababbaababbaaabbaababbba
abbbbabbbbabbabaaaaaaabbbabbaabb
abbbbaabaaabaababbbababaaabbbaabbabbabbabbabaaababbabbbbbaababaa
bbbabababaabbaaabbaaababbabaaaaabbaaaaaa
abbbbaababbbabbbaabaaaab
bbababaaaaaabababaaabbbbbbabbaaababbabbabaaaababaaaabababbabaabaabaabaab
bbbabbaabbbbabababaaabaa
abaaabbabaaaabaaaaabbabaababbaba
babbaabaabbabbaabaaaaaba
aababababbabbbaaabbaabba
bbbabaabbaaabbbabbabbaaa
bbbababaaabbabababababbb
aabbbbababaaaabbbaabbabbbaabbaab
bbaaaababababaababbbaaab
abbbaabbaaaaabbaaabaaaabbabaaabaaaaabbabbaababaa
babbabaabababbabbbbbabbbaabbbaba
bbbbbbbaabbbaabbbbbabbab
abaabbabbaabaababaabababbbbaaababababbaaaabbbabbabbaabbb
abababbabbaaaaabaabbabba
abbabaaababbababaabaababbabaaaaabbaaabaabbabbaaa
babbabaabbababbbbbabbaaa
aabaaabaababaaaaaaaabbba
bbaabbbabbbbaaaabaabababaabaaabaaabbabba
abaaaabaaabaaabbabbabbbb
abaaaaabaaaaaaaabaaaaaba
aaabbabababbbbaaaaaabbbb
bbbbaabbabaaabababaaabbababbbabaababbaabbabaabba
bbbabbbaaabbbababbaaabbbbbbabbabbbbbbabbabbbbbbb
abaaaababaaabaabababaaba
baaabaaabbabbbaaaabbaababaaaabba
bbbbabbbbbaabbbabaabbbbb
ababbaababbbbabaababaaaaaabbaaabaaaaabbb
baaaababaaaaababbababbaa
aabaababbabbaabbbaabbababaabbaabaaabaaabbabaabbababaaabbabbbaaab
abbabbaaaaaaabbabaaaabbaababbaaa
bbbbaabaabbbbabbaabbabbbaababbbbbabaaaba
bbbaaabbbaaabbbaaaababbb
baaabbbabbbaaaaabbbaaabaaabababbabaaabbababbabab
aabaaabbabaaaaababbbaaab
bbaaaaabaabbabababbbbaaababbababaabaabba
bbaaababbbbbaaaabababbbaaaabbabb
bbababbbbbabbababbbbabaabbbbaaaaaabbbaabbabbabbbbbbabbbb
bababbbaaaabbaabaaaabbba
ababbaababaabbabaaaaabba
aaaaaabaaaabbbaaababbaba
babbbbaaabbbabbbbbbabbab
bbbbbbbabbbbabbbabbaaaba
baaabaaaaabbaabbabaaababaaababbb
baabaabababbabbbaabbbabb
bbaaaaaaabbbbabbabaabbabbabbaaabaaaababaaaaaabba
baaaaaaaaaaaaaaaaaaababa
abbaababaabbbbabaaababba
bbbbababaabbbaabaababbaaaaabaaab
aababaabaabaababbbbbaaaaababaaaaabaababbbabbbbaaabaaaaabababbbab
babaababbbaabbabbbaabbaa
baabbababaaaabaabababbaa
bbaaabbabbaaabbbbbabbabb
baabbbbabbaaaabaaaabbbba
bbababbbbaabbbbaaaaabaab
aaabababaaaaaabbabaaaabababbbbbb
bbbbbbababaaabbbbaaaaaaabbaabbaabbbbbaabaabaaabbaaabbbbabbaabaabbbbaaabbabbbaabb
aabbbaaababbabbbbaabbbbababaaaaababaaaaaaaababbbaabababb
bbabbaabbabbaaaaaaaaabba
abbabbaabbaabbabaaabaabaabbaaaaaaabaaaabbbaabaabaabbabaa
abaababbaabbaaabaaabaaaabbaaaabaabaaababaababaaabbbabbababaaabaaabbaabbabbaaabaa
bbaaaaabbbbbabaaaababbaababbabbbaaabbabababbababbabbbbba
babbbbaaaababbaaaabaabbbbaabbbaababbbbbb
aaaababbbbbbbbaabbbabbbb
bbaaababbbaaabbaaabbbabb
abbaaabbbabbaabababaabbb
aabababbabbbbbababbbaabbaaabaaaaabbabbaababaabaabaaaaabaaababbbaababbbab
babbaaaaaabbbbabbbbbbbaabaabbbabbbbbaaab
babbabaaabbaaabbbabaaaaa
aaaaaaabababababbaababbb
ababaabbbabbaaaaabbbbbbb
aabbaaabaabbbabaaaababba
baabbabaaabaabaaabbaaaaa
abaaaabaaabbbaabbabaabaa
bbaaabbbbaaabbbaababbbbb
baaababbbbbaababbbabbaaa
ababbbbbabbababbaaabaabbaabbbaaaaabbaaabbbbbababbaaaaabaaabbbbaaaabbabaaaababbbbabaabaaa
bbbbabbbababababbaabbaab
ababbaabbabbbbaababbabbabaaabbaabaaabaaabaaaabbbababaababaababbb
baaaababbabbbbabbaabbaab
bbaabbbaabaaabbbbababbaa
bbabbbbaabbaaabaabbaabbaabaabbbb
bbbaaaaabbaababbbbaabbababaababbabbaaaba
aabababbaaabbbaaababaabbabbbbbba
abaaaabaaaabaaaabaaaababaabbbaababaabbabaaaaabbaaababbbabaabbaaababaaaab
baaabbbbbababababaaaababbbbaabaaaabaaabbbabbaabbabbbabaabbaaaaba
abbbbabbbbbbabbbbabbbbbb
bbbbabbbabbaaabbbbabaabaababaababbaaaabb
ababaaaaaababaabbaabbabaabbbabaaababbaaaabbbaaaa
bbbbbbbbbbbbaabbaaaabaab
aababaabbabbabaaaaaabaab
ababaaababbabbbabbaabaaa
bbbababbabbbbbabaaaaabaa
abbbaabbbabbbbabaaabbaaa
abbaaaabbbaaaaabaabaabba
aaabbabaaabaabbbaaabbabb
ababaaababbbbaaababaababbbbaabbbbaabaaaa
baabababbaababbabaabbaab
bbaaabbbaaabaabaababbaba
baaaaabbbbbaabaabaaabaaabaabbbbb
aabbbababaaaaaabababbaaa
baaaababbaaababbaaaaabaa
aabababaabaabbababababbb
bbaaaaaabaababbabbbbabaabbbbbbaaaabbaaabbababaab
bbbbababaabababaaabbbaaa
baaabaababbabbbaaababbaa
babaaaaaabbaababaaabbbbaabababbababaaaababaabaabbbbaabbbaaaaababaabaabbabbbbbbbbabababbaabaaaaab
bbbaababbaabbbbabaaaabaaabbbbbba
aababaabaababaaabbbaaababbbabaabbbaabaab
bbbbababaaabaaaabbbaaaab
bbbbbbbbabbbabbbaababaabbbabbabbbbaabaab
baaabaaabaaabbbbaabaaabbaaabaabaaabbbbaa
bbbabaabbaaaababaaabaaab
ababababbbbbabbbaaabababbaabbaab
abbababbaababaaaaababbaa
ababababaabbaabbbababaaa
ababbabbaaaaaabbababbbab
aaabbabbbaabababaabbaabbaaabaabbbabbaabb
bbbbababaabaaaaaabaaaaaa
bbaababaababbaabaaaabaaaaabbabaabaaaaaaaaabbaaba
bbababbbbaaaaabbaaababba
bbbbbbaaabbaababbaaabbaaabbbbabababbbbba
aabbbaabbbbababbbaaababa
aabaabaabaaabaababbabbbb
bbbbabaabaabbbbababaabab
abbbaaaaaabbbbbababbababbaaaabba
aaaaaaabaaabaababbbaaaaaaabbbbbbbbaabaaaabbaaaba
baaabbabbaaabaababbaabababbabbbabaabababaaababbbbbabbaabaabbbabb
aaaaababbaaabbaabbaaaabb
bbbabbbabaabbabaabbbabbaababaaaabbbbabbabbaabbaaaabaaabbabbbbaab
baabaabaabbbbbababaaaabbbbbabaabbbbaaaabbbbbbaabbaabbbbb
bbaaaaaabbabbaabbaabaaba
abbababbbabbbbabbaaaaaabaaaaaabaaaaaabbb
abaababbaabbbaabbabaabbb
baabababbaabababbbbaaaaabbababbbbaaaabbb
baabaabaabaabbbbbaabababbabababbbbabbbaabaaaaabaaaaabaaababbbbababbbaaabbbabaaba
abbbbaaaaaabbbaabaaaabaaaaaabbaa
baababababbaaabbbabbaabb
aaaaaabaabababbabbabbbbb
aaabbabaaabbaabbbbabaaab
abbbaabbbbbbabaaaaaabaaa
aabbabbbabaaaabbaabbbaaa
aabbababbaaabbbbabbbbbabaabaabab
bbbaababaabbbbbabbabaaaabaaaabba
bbbbababaabababaaabbabaa
ababaabbbbbbbbbaaaaabbbb
aaabababbabbaaaaababbbbb
bbbbabbabbbbbbaaaabaabbbbabbbbba
bbbababbaaababababbaababbbabbaabbabaaabaabbabaab
baaabbbaabababbaababbbaa
aaaaaababbbabbaaaabaaaaaabababababbaabaababaaaba
bbabbaabbbbbbbaabbbaaaab
babbaabaabbaaabbbbaabbbaabababbaaaabbbaabaababbbabbbaaaa
baabaabbbaaababababaaabbabbbbaaaaabaaaaababbabaaabbbbbbabaabaababbbbbaaabaaaaaaa
abbaababbbbabaabababbaba
bbaababbababababbbbbbaab
bbbbaababbaaaababaaabbaaabaabbbbbbbbbaaa
babbbaaabaababaababbbabbabbaabbabbaaaabaaababaababaabaaaabbaaaba
bbababbbabaaaaabbbbbbabb
babbabbbababaaaababbbabaaaabbababbabbbbbabababbb
abbbaabbbbaaabbbaaabbabaaaaaaababaabaabbaabbbaabababbbabbbbbbbabababbbbbaaababaa
aaaaabbabbbaaaabbaaababbbaaaababaaabbabbbabbabbaabbabaabaabbaaaaabbaabaababaabaababbabaa
baaababaababbbabbaaaabbaababbaaababababababbaabbbbbabbbababbababaaabbbbaababbaba
babbabbaabbbabaaabbaaaaa
bbbaaabaaaabababbaaabbbabababbbb
bababbbaababaaaabaabaabaaabbabbbbbabababbabbbaab
aababaaaabaabbabbabaabaa
aababbaaaaabbaabaaaababa
babbbbaababbbbaaaaabbbaabbaababbbbabaaabbaaabbabababbbaa
abaaaababababbabbababbbabbabbaabbbaaabaa
aabbababaabbaababaaaaabbbabbaaaabababbabbbbabbaaaaabbbbb
aabaaababbaaaabbaabbabaaaaababbabababbbb
abbbbbaabbbabaaaaaaaabbaaabbbaaa
bbbbabaaaabbbababbbabbbb
bbbababaababaaabaabbabaa
abaababbbaaababbbabbbbaaabaabaab
aaabbaababbbbaaaaabbbbba
aabaaaabababbaaaaaabaabbaaaabbaa
baaabbabbbabaaabaaaabaabababbbbb
abaaaaabbbaaaaaabaababaa
bababbabbbbabbaaaaabbbab
abaaababbaabbabaaabaaabbabbbbabaaaaababaaabaaaabbbbabbbbbaabbaaa
aabababbaaabaaaaabbaabba
ababaaabbabbabaabbbaaaaaaaaaaabbaaabaaab
aabaaababbbababaaabaabaabbbbaaaaaabbaaaa
bababaaabbababbabbbabaaa
abaaabbabaaabaabbababbaa
abbbabaabbaabbbababbbbbb
aabbbbabbaaabaaabbaaabaa
bbbbabbaabbbbbbaaaababaa
abbbbabaaabababbaaabbbbb
abaaabbaabaaabbbbbaabbbb
aabaaabaaaaaaabaaaaabbba
abbabbbaababbabbaaaabbbb
babbaabaaaaaaaabbaabbbbabaaaababaabbaaaa
ababbabbabaaaabbbbbababbaabbababbbbababb
abbbabbbbabbbbabbbaabaab
baaababbbbaaabbabbbaaaab
abbbbaabbbbbaabbabaaababbaabaaab
bbbbababbbaaabaaabbababbbabbbbababaababaaaabaaaabaaaabaaabbbaabababbbabbbaaaaaababbaabbb
bbbbabaabbabaabbabbbbbabbabaaabbaabbaaab
baabbabaaabbaababbbbbaab
bbabaaabaabaaaababbbbbaabaaabbaabababbaaaabbaaabaaaababbaaaababaaaaaaaaaababbbbb
abaaaabaabbbabbbaaaaababbaaaaaab
abbbabbbaababbbbabaaaababbaaabbaabbbaabbbbabaaaa
bbaaabbabbaababbbbbabbaabaabbbbabbbaababababbbaa
bbaaaaaababbbbbbbaababaaababbaaabaabaaabbbababbabbabbbbababbaaab
bbaababbbbaaabbbababbaba
bbbaaabbbbbbabaabbabbaaa
bbbababaaababbbbbaababaa
baaaababaababaaaabbbbbbb
aabbbbabaaaababbbabaabba
baaabaabbbbabbbabbaaabbaabbbaabbbbaabaab
aabbbaabbaaaaaaabaaaaabbbbbaabab
baaaabaaaabbaabaabaaababaaaabaab
aaaaaabaaababbaabaaaaaba
aaabaaaaaabbbbabbaabbaaa
abaababbbbbabbbaaaaaaaaaaabaaabbbaabbbabaaabaabb
bbbaabbaabbababaabbabaaa
bbbababbabbabbbabbaaabbabababbaaababbbbb
abaabbbaababbbaaabbabaab
aababaabaaabbababababbbaaaabbabababbbbaaaaaabbbababbabab
bbabbbaaaaaaababbbaaaabababbabaaabbabbbbaaabbbbb
aaaaaabbbbbaaabbbbaabaaaaabbabaa
bbbaabbababbaabaaabbbbbb
abbbabaaaaaaababaababbab
bbabaabaaabbaabbaabbabba
baaaabaaaababaabbbabbbab
bbaabbbaaaabbaaaaaaaabaaaaaabbaa
aabaabaaaababaabbbbaabaabbbaaabbbbabbabb
aaabaabaabbbabbbaabbbbbb
babbaaaaabaaabbbbbaaababaaaaaabaababbbababbabbbbaaabbbba
abbababbbaabbabbabaabbabaaaaabbb
ababaaabbaaaaabbabbbabaabbaabbbaabaaaaabbaabaabbabbbaaaa
babbaaaabaabababbaaaabbb
aaabbbaaaabbbabababaabaa
bbbaaabaababbaabababaaba
aaababbaaabbaababbbbabbabbbabbab
abababbaaababaababbaabba
bbaaabbabbbbababaaaabaab
'

# COMMAND ----------

# input <- '0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"

# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb
# '

# COMMAND ----------

split_strs <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
split_strs

# COMMAND ----------

messages <- split_strs[[2]] %>% enframe(name = "message_id")
messages

# COMMAND ----------

rules <-
  split_strs[[1]] %>%
  as_tibble() %>%
  separate(value, c("rule_id", "value"), ": ") %>%
  mutate(
    rule_id = as.integer(rule_id)
  )
rules

# COMMAND ----------

char_rules <-
  rules %>%
  filter(str_detect(value, '"')) %>%
  mutate(value = str_replace_all(value, '"', ""))
char_rules

# COMMAND ----------

nested_rules <-
  rules %>%
  anti_join(char_rules, by = "rule_id") %>%
  mutate(
    value = str_split(value, fixed(" | ")),
    value = map(value, ~str_split(., fixed(" ")) %>% map(as.integer))
  )
nested_rules

# COMMAND ----------

all_rules <- bind_rows(
  char_rules %>% mutate(value = as.list(value)),
  nested_rules
)
all_rules

# COMMAND ----------

generate_regex <- function(rule) {
  if (length(rule) > 1) {
    return(rule %>% map_chr(generate_regex) %>% paste0(collapse = ""))
  }
  
  value <- all_rules %>% filter(rule_id == rule) %>% pull(value) %>% first()
  
  if (is.character(value)) {
    return (value)
  }
  glue::glue("(?:{str_c(map_chr(value, generate_regex), collapse = '|')})")
}

# COMMAND ----------

generate_regex(0)

# COMMAND ----------

result <-
  messages %>%
  mutate(is_match = str_detect(value, paste0("^", generate_regex(0), "$")))
result

# COMMAND ----------

answer <- result %>% filter(is_match) %>% nrow()
answer

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

all_rules$value[all_rules$rule_id == 8] <- list(list(c(42), c(42, 8)))
all_rules$value[all_rules$rule_id == 11] <- list(list(c(42, 31), c(42, 11, 31)))

# COMMAND ----------

max_depth <- 20

generate_regex <- function(rule, depth = 1) {
  if (rule == 42) {
    depth <- depth + 1
  }
  if (depth >= max_depth) {
    return("")
  }
  
  if (length(rule) > 1) {
    return(rule %>% map_chr(generate_regex, depth = depth) %>% paste0(collapse = ""))
  }
  
  value <- all_rules %>% filter(rule_id == rule) %>% pull(value) %>% first()
  
  if (is.character(value)) {
    return (value)
  }
  glue::glue("(?:{str_c(map_chr(value, generate_regex, depth = depth), collapse = '|')})")
}

# COMMAND ----------

regex <- generate_regex(0)

# COMMAND ----------

result <-
  messages %>%
  mutate(is_match = str_detect(value, paste0("^", regex, "$")))
result

# COMMAND ----------

answer <- result %>% filter(is_match) %>% nrow()
answer