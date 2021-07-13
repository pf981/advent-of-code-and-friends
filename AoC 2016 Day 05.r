# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 5: How About a Nice Game of Chess? ---</h2><p>You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching <a href="https://en.wikipedia.org/wiki/Hackers_(film)">hacking</a> <a href="https://en.wikipedia.org/wiki/WarGames">movies</a>.</p>
# MAGIC <p>The <em>eight-character password</em> for the door is generated one character at a time by finding the <a href="https://en.wikipedia.org/wiki/MD5">MD5</a> hash of some Door ID (your puzzle input) and an increasing integer index (starting with <code>0</code>).</p>
# MAGIC <p>A hash indicates the <em>next character</em> in the password if its <a href="https://en.wikipedia.org/wiki/Hexadecimal">hexadecimal</a> representation starts with <em>five zeroes</em>. If it does, the sixth character in the hash is the next character of the password.</p>
# MAGIC <p>For example, if the Door ID is <code>abc</code>:</p>
# MAGIC <ul>
# MAGIC <li>The first index which produces a hash that starts with five zeroes is <code>3231929</code>, which we find by hashing <code>abc3231929</code>; the sixth character of the hash, and thus the first character of the password, is <code>1</code>.</li>
# MAGIC <li><code>5017308</code> produces the next interesting hash, which starts with <code>000008f82...</code>, so the second character of the password is <code>8</code>.</li>
# MAGIC <li>The third time a hash starts with five zeroes is for <code>abc5278568</code>, discovering the character <code>f</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, after continuing this search a total of eight times, the password is <code>18f47a30</code>.</p>
# MAGIC <p>Given the actual Door ID, <em>what is the password</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "ugkcyxxp"

# COMMAND ----------

answer <-
  str_c(input, seq(from = 0, to = 12000000)) %>%
  openssl::md5() %>%
  keep(str_starts, "00000") %>%
  str_sub(6, 6) %>%
  head(8) %>%
  str_c(collapse = "")  # 13 minutes

answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As the door slides open, you are presented with a second door that uses a slightly more <span title="This one says 'WOPR' in block letters.">inspired</span> security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted <em>in order</em>?!), the Easter Bunny engineers have worked out <a href="https://www.youtube.com/watch?v=NHWjlCaIrQo&amp;t=25">a better solution</a>.</p>
# MAGIC <p>Instead of simply filling in the password from left to right, the hash now also indicates the <em>position</em> within the password to fill. You still look for hashes that begin with five zeroes; however, now, the <em>sixth</em> character represents the <em>position</em> (<code>0</code>-<code>7</code>), and the <em>seventh</em> character is the character to put in that position.</p>
# MAGIC <p>A hash result of <code>000001f</code> means that <code>f</code> is the <em>second</em> character in the password. Use only the <em>first result</em> for each position, and ignore invalid positions.</p>
# MAGIC <p>For example, if the Door ID is <code>abc</code>:</p>
# MAGIC <ul>
# MAGIC <li>The first interesting hash is from <code>abc3231929</code>, which produces <code>0000015...</code>; so, <code>5</code> goes in position <code>1</code>: <code>_5______</code>.</li>
# MAGIC <li>In the previous method, <code>5017308</code> produced an interesting hash; however, it is ignored, because it specifies an invalid position (<code>8</code>).</li>
# MAGIC <li>The second interesting hash is at index <code>5357525</code>, which produces <code>000004e...</code>; so, <code>e</code> goes in position <code>4</code>: <code>_5__e___</code>.</li>
# MAGIC </ul>
# MAGIC <p>You almost choke on your popcorn as the final character falls into place, producing the password <code>05ace8e3</code>.</p>
# MAGIC <p>Given the actual Door ID and this new method, <em>what is the password</em>? Be extra proud of your solution if it uses a cinematic "decrypting" animation.</p>
# MAGIC </article>

# COMMAND ----------

hashes <-
  str_c(input, seq(from = 0, to = 30000000)) %>%
  openssl::md5() %>%
  keep(str_starts, "00000") # 20 mins

hashes

# COMMAND ----------

answer <-
  hashes %>%
  enframe() %>%
  mutate(
    pos = str_sub(value, 6, 6)
  ) %>%
  group_by(pos) %>%
  summarise(
    letter = first(str_sub(value, 7, 7))
  ) %>%
  arrange(pos) %>%
  pull(letter) %>%
  head(8) %>%
  str_c(collapse = "")

answer
