# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 2: Inventory Management System ---</h2><p>You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.</p>
# MAGIC <p>Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that <span title="This is, in fact, roughly when chimneys became common in houses.">so many people have chimneys</span>, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of <em>suit</em> that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"</p>
# MAGIC <p>"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for <em>two similar box IDs</em>..." They walk too far away to hear any more.</p>
# MAGIC <p>Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).</p>
# MAGIC <p>To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing <em>exactly two of any letter</em> and then separately counting those with <em>exactly three of any letter</em>. You can multiply those two counts together to get a rudimentary <a href="https://en.wikipedia.org/wiki/Checksum">checksum</a> and compare it to what your device predicts.</p>
# MAGIC <p>For example, if you see the following box IDs:</p>
# MAGIC <ul>
# MAGIC <li><code>abcdef</code> contains no letters that appear exactly two or three times.</li>
# MAGIC <li><code>bababc</code> contains two <code>a</code> and three <code>b</code>, so it counts for both.</li>
# MAGIC <li><code>abbcde</code> contains two <code>b</code>, but no letter appears exactly three times.</li>
# MAGIC <li><code>abcccd</code> contains three <code>c</code>, but no letter appears exactly two times.</li>
# MAGIC <li><code>aabcdd</code> contains two <code>a</code> and two <code>d</code>, but it only counts once.</li>
# MAGIC <li><code>abcdee</code> contains two <code>e</code>.</li>
# MAGIC <li><code>ababab</code> contains three <code>a</code> and three <code>b</code>, but it only counts once.</li>
# MAGIC </ul>
# MAGIC <p>Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of <code>4 * 3 = 12</code>.</p>
# MAGIC <p><em>What is the checksum</em> for your list of box IDs?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "uqcipadzntnheslgvjjozmkfyr
uqcipadzwtnhexlzvxjobmkfkr
cqcipadpwtnheslgyxjobmkfyr
ubnipadzwtnheslgvxjobmkfyw
uqcisadzwtnheslgvxjfbmkfor
uqcisaezwtnheslgvxkobmkfyr
uqcguadzwtnheslgvxjobmkfir
uqcipadzmtnhesldvxdobmkfyr
uqcipadzwtzheslgdxjtbmkfyr
uquipadzwtcheslgvxjobmkfbr
uqctpadzwtnhesjbvxjobmkfyr
ueciparzwtnheslgvxjobmkfyx
uqcipadzwtnhessgvxjkbmkfkr
uqcipamzwtnheslgvxioamkfyr
uciizadzwtnheslgvxjobmkfyr
uqcieadzwtnhesfgvxeobmkfyr
fqcipadzwtnreslgvkjobmkfyr
uqcipadzrtnherlgvxjobmklyr
uqcypadzwtnheslgvxjobmkxfr
uqcipadzwtnhemlgvxjobmvfur
uwciuadzwwnheslgvxjobmkfyr
uqcipadzwtnhcscgvxjobmkuyr
upripadzwtnheslovxjobmkfyr
uqcipadzltnheslgvxjobmkftc
uqcipadzwtnheslgvgjobmifsr
uqoipadzwtnheslgvxjosmkfkr
uqcipadzwtbhesrqvxjobmkfyr
uqcipadzwtnheslpvxjobmhfyx
uhcinadzwtnheslgvxjybmkfyr
uqcipadzwtnhhslgvxjabmkbyr
uecipadzwtnheslgvxjobqyfyr
uqcipadfwtnheslwvxjobgkfyr
uqcipadzvtnheshgvxzobmkfyr
fqcipadzwtcheslgvxjobmkfyt
uecipadzwtnheslgpxjbbmkfyr
uqclpadzwtnheslgvnjobukfyr
qqciprdzetnheslgvxjobmkfyr
uqcipahpwtnheslgvxjtbmkfyr
uqcidadzwtnhesljvxyobmkfyr
uqciradswtnqeslgvxjobmkfyr
uqcipadzwtrhmslgvxjobmkfyf
urcipadzjtnheslgvxfobmkfyr
uqcipadzwznheslgvxjobmkfcv
uqcipadowtnheslgyxjobmkfym
uqcigadzwtnheslgvxjoomkmyr
uqjipafzwtnheslgvejobmkfyr
uqcioadzwtnhhslgvxzobmkfyr
uqcgpadkwtnheslgvxjobhkfyr
ufciiadewtnheslgvxjobmkfyr
uqoipadzwtnheslgvxjllmkfyr
uqcipadzutnheslgwxxobmkfyr
uqcipadzwtlheslgaxjobmkfwr
uqcbpadzutnheslgvxjbbmkfyr
uucipadzwvnhesngvxjobmkfyr
uqcifadzwtnceslgvxjoumkfyr
ujcipadzwteheslgvxjobmkfyj
uqcipadzwtnheslqvxjobmkuyp
uqcipadzwtnheslgvxjoxmkxyw
uqcipaduwtnheslgvujmbmkfyr
uicipadnwtnheslgvxjobmbfyr
uqcipadzwteheslgvxjobbmfyr
uqcipadzwgnneslgvxjobmklyr
uqcipadzxtnhwslgvbjobmkfyr
uqcipaxwwtnheslxvxjobmkfyr
uocipadzwtnheslgvxjobqdfyr
uqciaauzwtnheslgtxjobmkfyr
uncipagzwtnkeslgvxjobmkfyr
uqcipadzwtnhehlgvxjohdkfyr
uqcipadzwtnheslgvxjobmspyz
uccipadzwtnhvsltvxjobmkfyr
uacipagzwtnheslgvxjoqmkfyr
tqcipaduwtnheslgvxjobmmfyr
uqcipadzwtnheslgvxqebmifyr
uecipadthtnheslgvxjobmkfyr
uocipadzwtnhdslgvkjobmkfyr
uqcipadtwtnheslgvxhobmufyr
uqkipadzwtnleslgtxjobmkfyr
uqcipadzjunheslgvxjobmnfyr
ubcipadzwtvheslgvxjobmkfyf
uqcipadzwpfheslgvxjsbmkfyr
uocipadzwtndeslgvxjobmmfyr
uqcipadzwtnheslgtxjobhkfyq
uqcipadzwtrheslgvxjobmyfya
uqcipadzwtvheslgvxjolgkfyr
uqcipidzwtaheslgvxjobmkfxr
uyzixadzwtnheslgvxjobmkfyr
uqyihadzwtnhedlgvxjobmkfyr
uqcipadzwtnhesltvejobqkfyr
uqciptdzwtnheslgyxlobmkfyr
uqcipzdzwtnhzslgvxjosmkfyr
uqcipadzwtnbeslgexjobmkfvr
uqcipadzwtnheslcwxjobmkkyr
uqcapadzwcnheslgvxjolmkfyr
uqcjpadzwtnhejlgvxjxbmkfyr
uqcipadwwtxweslgvxjobmkfyr
uqmipadzwtnhezlgvxjobmkyyr
uqcipubzwtnpeslgvxjobmkfyr
uecvpadzwtnheslgvxjocmkfyr
uqcipadzwfnheslgvxjibmkdyr
uqcipadzwtnheslgvxvfbykfyr
uqcipadzwtnheslgvgjoimkfyt
dqcqpaqzwtnheslgvxjobmkfyr
uqcipbdzwtnheslgvxjobmkghr
jqcipadzwtnheslgvxjgbmkzyr
uqcipadzwtnheslgvxqkqmkfyr
uqcipadzptnheslgvxjxbokfyr
uucijadzwtwheslgvxjobmkfyr
uccfpadzwtnheslgvxjobpkfyr
uqcipadzwtnheslgvxjobakeyq
uqcipadzwtnheolgvxqobjkfyr
imiipadzwtnheslgvxjobmkfyr
uqcehadzwtnheslgvxjobmkuyr
uqcipadzztnheslgvxjorokfyr
rqcixadzwtnheelgvxjobmkfyr
uqcipadzwtzheslgvxjodmkfyi
uqcipaezwtnwuslgvxjobmkfyr
uqcipadzwtnheslggxjobjkfyq
uqcipadzwkghesagvxjobmkfyr
uqcypqdzwtnheslgvxjobakfyr
iqcipadzwtnhezltvxjobmkfyr
uxcimadzwtnheslgvxjobmxfyr
uqcipaizwtvhwslgvxjobmkfyr
uqcipafzwtnheslgvxjpbmkfym
uqcipadzwinheslgvxlobmpfyr
uqcupadzwtnheslkvxmobmkfyr
uqcapadzwtnhesrgvxjobmkfsr
urcipafzwtnheslgvxjobmkfur
uqcipaczwtnheslgvbjobmknyr
uqcizadzztgheslgvxjobmkfyr
uqcipfdzwtnhesxgvxjobmkfyw
uqcipbdzwtnhyslgvxjobmcfyr
uqcipadzwanhezlgvxjobmkfwr
uvcipadzwtnheslgvxjbkmkfyr
uqcipajzwtnseslgvxjobmkfyq
uqcipvdzwtnheslgvmlobmkfyr
uqcipadzdgnheslgmxjobmkfyr
uqcipddzwtnhestgvpjobmkfyr
umcipadzwtdheslgvxjzbmkfyr
uqciuwdzwtnheslgvxjobmkflr
uqcipadzwtnheslgsxabbmkfyr
uceipadzwtnheslgvxjobgkfyr
mqcipadzwtnhesrgvxjobmjfyr
aqcipadvwtnheslgvxjobmkryr
uqsipadzwtnofslgvxjobmkfyr
uqcixadzwtfheslgvxjzbmkfyr
uqcipadnwfnheslgvxjohmkfyr
uqcivadzwtnheslfvxjobmkfyz
uqciprdzwtnheslgvxjobmkjir
uqcipadhbtnheslgvxjoxmkfyr
fqcipadzwtnhesfgvxjobmkfye
uqoipqdzwtnheqlgvxjobmkfyr
uqcipadzwtnhesltvxmobmkzyr
uqcipadzwtnhebqgvsjobmkfyr
uqcipadzwtnheslglxjobmfbyr
gqcipadzwtgheslgvxjobwkfyr
uqcipadzwtnheslgfxjzbmlfyr
ujcnpadzwtnheslrvxjobmkfyr
ujcivadzwtnheglgvxjobmkfyr
uqcitadzwgnheslgvxjofmkfyr
uqcipahzatnhmslgvxjobmkfyr
uqzipaizwtnheslgvujobmkfyr
uqcipadzltnheylgvnjobmkfyr
uqcidadzwtnhwsljvxyobmkfyr
uqcipadzwtihetlgvxjobhkfyr
oqcipabzwtnheslgvfjobmkfyr
uqcipadzwtnveslgvxjobzkfzr
uqcipadzwtjheslgqxjobmlfyr
uqcnpadzztnheslgvxjobmkoyr
uqciuadzwonheslgvxjobmkfyz
tqcipadzwtnheslgvxaobmqfyr
uqcipadtwtnhqslgvxjobmkeyr
uqcipadzwbnheslgvajobmsfyr
ubcopadzwtnhgslgvxjobmkfyr
uqcipydzwtwheslgvxjobakfyr
cqbijadzwtnheslgvxjobmkfyr
uscipadowtnheslgvxjobmkfcr
uqcipadzwtgheslnvxjobskfyr
uqcipzdzwtnzeslgkxjobmkfyr
uqcipawzwtnhrslgbxjobmkfyr
uqcipadzatchyslgvxjobmkfyr
uqcipadzotnpeslgvxjobmjfyr
uqcipagzwtnheslgvxjobmvfyt
uqcipadzwhnheslgvxyobmkfyo
uqcipadzwtnheslgmqjobmkfyc
uqcupadzwgnheslgvcjobmkfyr
uqcipabzwbnheslgvxjobmkwyr
uqciiadzwtnheslgvxjobmkfmz
uqkipauzwtnheslgvxjjbmkfyr
uqcipidzetnheslgvxjobmkfyi
uqcipadzwtnheslgqxjokmkfmr
uqcipadzqtnhesllvxjobmkfyk
uqccpadzwtnheslgmxsobmkfyr
uqcipadzwteheslgvljfbmkfyr
uqcipadxwinheslgaxjobmkfyr
uqcipadzwtnheslhvxyobmkfjr
aqcipadzwnnheslgvxjqbmkfyr
uvcipadzwtnheszgvxjobmkfyg
uqcipahzmtnheslgvxjobmkfir
ukcipadzbtnheslgvxjobmkfyb
uqcipadzwtnhemlgvqjobmkfpr
uqcipadzwtnheslgvmeobmkfpr
uqciphdrwtnheslgvxjobmkfyw
uqcipadzwtnheslevxqobzkfyr
uqcipadzwknzeslgvxnobmkfyr
wqcipadzwjnheslgvxjobbkfyr
uqcipadzwtdheslgvmjobmkjyr
uqvipadzwtnhextgvxjobmkfyr
uqhipadzwtnheslwvxjzbmkfyr
uqcipadzwtnherlgsxjobmksyr
uqcipadzwtnhesqgvxjotmvfyr
udcipadzwtnhekwgvxjobmkfyr
uqcjprdzwtnheslgvxjobmkfpr
uqcipadzatnheclgvqjobmkfyr
uqcbpadzctnheslqvxjobmkfyr
uqcipadzqtnhesluvxjobrkfyr
uqcipadzwtnhcslgvxjoomwfyr
uqcppadzwxnheslgwxjobmkfyr
uqcipadcwtnheslrvxjdbmkfyr
ukcipadzwtnhhslgvxjobmkgyr
uqckpadzwtnheslgvxjokmkiyr
uqcspadzwtjheslgvxjobmkfjr
uqcipadpwtnhsslgvxjobmkfyu
uqcepadzwtnheilgvbjobmkfyr
jqcipadiwtnheslgvxjobmkjyr
uqcipadzrtnseslgqxjobmkfyr
sqmipadzwtnhewlgvxjobmkfyr
uqcieadzhtnheslgvgjobmkfyr
uqcipadzwkwhewlgvxjobmkfyr
uqcipadzwtzheslgvxjpbqkfyr
uzcipadzjtnheslgvxjobmlfyr
uqcipadzwtnheslnvxjobmkfee
uqciyanzwtnheslgvxjoimkfyr
uqcipadqwtnheswghxjobmkfyr
uycipadzwtnheslovxjobmofyr
uqcipadzwtnheslgvxcozmxfyr
uqmipadzwtnxezlgvxjobmkfyr
uqcipadzftnheslgvxjotmkffr
aqcipaizwtnhesagvxjobmkfyr
uqcipcdzwtnheslgoajobmkfyr
uqcypadgwtnhesbgvxjobmkfyr
uqcipcdzwtnheslgvxjebmkfyb
uhcvpadzwtnheslgvxjobzkfyr
uqcipadzwtnpesagvxmobmkfyr
uqcipadzwtnidslgvxjobmkfor
uqcipadkwtnhesigvxjzbmkfyr
uqcypadlwtnheslsvxjobmkfyr
qqcipadzwtnheswgvxjobmkoyr
uqcipadzwtnheslgvxjhbmmcyr
uqcipadzwtnhesogvxjormkfmr
uqcipadzwtnhetcgvxgobmkfyr
"

# COMMAND ----------

l <- read_lines(input)

answer <-
  l %>%
  str_split("") %>%
  imap_dfr(~tibble(letter = ., word = .y)) %>%
  count(word, letter) %>%
  group_by(word, n) %>%
  slice(1) %>%
  ungroup() %>%
  summarise(sum(n == 2) * sum(n == 3)) %>%
  pull(1)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.</p>
# MAGIC <p>The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:</p>
# MAGIC <pre><code>abcde
# MAGIC fghij
# MAGIC klmno
# MAGIC pqrst
# MAGIC fguij
# MAGIC axcye
# MAGIC wvxyz
# MAGIC </code></pre>
# MAGIC <p>The IDs <code>abcde</code> and <code>axcye</code> are close, but they differ by two characters (the second and fourth). However, the IDs <code>fghij</code> and <code>fguij</code> differ by exactly one character, the third (<code>h</code> and <code>u</code>). Those must be the correct boxes.</p>
# MAGIC <p><em>What letters are common between the two correct box IDs?</em> (In the example above, this is found by removing the differing character from either ID, producing <code>fgij</code>.)</p>
# MAGIC </article>

# COMMAND ----------

common_letters <- function(a, b) {
  a_split <- str_split(a, "") %>% first()
  b_split <- str_split(b, "") %>% first()
  
  a_split[a_split == b_split] %>% str_c(collapse = "")
}

df <-
  crossing(a = l, b = l) %>%
  filter(a != b) %>%
  mutate(
    common = map2_chr(a, b, common_letters),
    common_length = str_length(common)
  ) %>%
  arrange(desc(common_length))
df

# COMMAND ----------

answer <- df %>% slice(1) %>% pull(common)
answer
