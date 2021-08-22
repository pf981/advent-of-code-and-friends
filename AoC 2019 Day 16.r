# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/16

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 16: Flawed Frequency Transmission ---</h2><p>You're 3/4ths of the way through the <a href="https://en.wikipedia.org/wiki/Gas_giant">gas giants</a>. Not only do roundtrip signals to Earth take <span title="In minutes, that's as many as thirty tens!">five hours</span>, but the signal quality is quite bad as well.  You can clean up the signal with the Flawed Frequency Transmission algorithm, or <em>FFT</em>.</p>
# MAGIC <p>As input, FFT takes a list of numbers.  In the signal you received (your puzzle input), each number is a single digit: data like <code>15243</code> represents the sequence <code>1</code>, <code>5</code>, <code>2</code>, <code>4</code>, <code>3</code>.</p>
# MAGIC <p>FFT operates in repeated <em>phases</em>.  In each phase, a new list is constructed with the same length as the input list.  This new list is also used as the input for the next phase.</p>
# MAGIC <p>Each element in the new list is built by multiplying every value in the input list by a value in a repeating <em>pattern</em> and then adding up the results. So, if the input list were <code>9, 8, 7, 6, 5</code> and the pattern for a given element were <code>1, 2, 3</code>, the result would be <code>9*1 + 8*2 + 7*3 + 6*1 + 5*2</code> (with each input element on the left and each value in the repeating pattern on the right of each multiplication). Then, only the ones digit is kept: <code>38</code> becomes <code>8</code>, <code>-17</code> becomes <code>7</code>, and so on.</p>
# MAGIC <p>While each element in the output array uses all of the same input array elements, the actual repeating pattern to use depends on <em>which output element</em> is being calculated. The base pattern is <code>0, 1, 0, -1</code>.  Then, repeat each value in the pattern a number of times equal to the <em>position in the output list</em> being considered. Repeat once for the first element, twice for the second element, three times for the third element, and so on.  So, if the third element of the output list is being calculated, repeating the values would produce: <code>0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1</code>.</p>
# MAGIC <p>When applying the pattern, skip the very first value exactly once. (In other words, offset the whole pattern left by one.) So, for the second element of the output list, the actual pattern used would be: <code>0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ...</code>.</p>
# MAGIC <p>After using this process to calculate each element of the output list, the phase is complete, and the output list of this phase is used as the new input list for the next phase, if any.</p>
# MAGIC <p>Given the input signal <code>12345678</code>, below are four phases of FFT. Within each phase, each output digit is calculated on a single line with the result at the far right; each multiplication operation shows the input digit on the left and the pattern value on the right:</p>
# MAGIC <pre><code>Input signal: 12345678
# MAGIC 
# MAGIC 1*1  + 2*0  + 3*-1 + 4*0  + 5*1  + 6*0  + 7*-1 + 8*0  = 4
# MAGIC 1*0  + 2*1  + 3*1  + 4*0  + 5*0  + 6*-1 + 7*-1 + 8*0  = 8
# MAGIC 1*0  + 2*0  + 3*1  + 4*1  + 5*1  + 6*0  + 7*0  + 8*0  = 2
# MAGIC 1*0  + 2*0  + 3*0  + 4*1  + 5*1  + 6*1  + 7*1  + 8*0  = 2
# MAGIC 1*0  + 2*0  + 3*0  + 4*0  + 5*1  + 6*1  + 7*1  + 8*1  = 6
# MAGIC 1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*1  + 7*1  + 8*1  = 1
# MAGIC 1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*1  + 8*1  = 5
# MAGIC 1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*0  + 8*1  = 8
# MAGIC 
# MAGIC After 1 phase: 48226158
# MAGIC 
# MAGIC 4*1  + 8*0  + 2*-1 + 2*0  + 6*1  + 1*0  + 5*-1 + 8*0  = 3
# MAGIC 4*0  + 8*1  + 2*1  + 2*0  + 6*0  + 1*-1 + 5*-1 + 8*0  = 4
# MAGIC 4*0  + 8*0  + 2*1  + 2*1  + 6*1  + 1*0  + 5*0  + 8*0  = 0
# MAGIC 4*0  + 8*0  + 2*0  + 2*1  + 6*1  + 1*1  + 5*1  + 8*0  = 4
# MAGIC 4*0  + 8*0  + 2*0  + 2*0  + 6*1  + 1*1  + 5*1  + 8*1  = 0
# MAGIC 4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*1  + 5*1  + 8*1  = 4
# MAGIC 4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*1  + 8*1  = 3
# MAGIC 4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*0  + 8*1  = 8
# MAGIC 
# MAGIC After 2 phases: 34040438
# MAGIC 
# MAGIC 3*1  + 4*0  + 0*-1 + 4*0  + 0*1  + 4*0  + 3*-1 + 8*0  = 0
# MAGIC 3*0  + 4*1  + 0*1  + 4*0  + 0*0  + 4*-1 + 3*-1 + 8*0  = 3
# MAGIC 3*0  + 4*0  + 0*1  + 4*1  + 0*1  + 4*0  + 3*0  + 8*0  = 4
# MAGIC 3*0  + 4*0  + 0*0  + 4*1  + 0*1  + 4*1  + 3*1  + 8*0  = 1
# MAGIC 3*0  + 4*0  + 0*0  + 4*0  + 0*1  + 4*1  + 3*1  + 8*1  = 5
# MAGIC 3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*1  + 3*1  + 8*1  = 5
# MAGIC 3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*1  + 8*1  = 1
# MAGIC 3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*0  + 8*1  = 8
# MAGIC 
# MAGIC After 3 phases: 03415518
# MAGIC 
# MAGIC 0*1  + 3*0  + 4*-1 + 1*0  + 5*1  + 5*0  + 1*-1 + 8*0  = 0
# MAGIC 0*0  + 3*1  + 4*1  + 1*0  + 5*0  + 5*-1 + 1*-1 + 8*0  = 1
# MAGIC 0*0  + 3*0  + 4*1  + 1*1  + 5*1  + 5*0  + 1*0  + 8*0  = 0
# MAGIC 0*0  + 3*0  + 4*0  + 1*1  + 5*1  + 5*1  + 1*1  + 8*0  = 2
# MAGIC 0*0  + 3*0  + 4*0  + 1*0  + 5*1  + 5*1  + 1*1  + 8*1  = 9
# MAGIC 0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*1  + 1*1  + 8*1  = 4
# MAGIC 0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*1  + 8*1  = 9
# MAGIC 0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*0  + 8*1  = 8
# MAGIC 
# MAGIC After 4 phases: 01029498
# MAGIC </code></pre>
# MAGIC <p>Here are the first eight digits of the final output list after 100 phases for some larger inputs:</p>
# MAGIC <ul>
# MAGIC <li><code>80871224585914546619083218645595</code> becomes <code>24176176</code>.</li>
# MAGIC <li><code>19617804207202209144916044189917</code> becomes <code>73745418</code>.</li>
# MAGIC <li><code>69317163492948606335995924319873</code> becomes <code>52432133</code>.</li>
# MAGIC </ul>
# MAGIC <p>After <em>100</em> phases of FFT, <em>what are the first eight digits in the final output list?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "59715091976660977847686180472178988274868874248912891927881770506416128667679122958792624406231072013221126623881489317912309763385182133601840446469164152094801911846572235367585363091944153574934709408511688568362508877043643569519630950836699246046286262479407806494008328068607275931633094949344281398150800187971317684501113191184838118850287189830872128812188237680673513745269645219228183633986701871488467284716433953663498444829748364402022393727938781357664034739772457855166471802886565257858813291667525635001823584650420815316132943869499800374997777130755842319153463895364409226260937941771665247483191282218355610246363741092810592458"

# COMMAND ----------

nums <- input %>% str_split("") %>% unlist() %>% parse_integer()
nums

# COMMAND ----------

create_pattern <- function(step, length_out, base_pattern = c(0, 1, 0, -1)) {
  base_pattern %>%
    rep(each = step) %>%
    rep(length.out = length_out + 1) %>%
    tail(-1)
}

process_phase <- function(nums) {
  result <- integer(length(nums))
  for (step in seq_along(nums)) {
    pattern <- create_pattern(step, length(nums))
    result[step] <- abs(sum(nums * pattern)) %% 10
  }
  result
}

solve <- function(nums, n_phases = 100) {
  for (phase in seq(from = 0, to = n_phases - 1, by = 1)) {
    nums <- process_phase(nums)
  }
  nums
}

# COMMAND ----------

result <- solve(nums)
result

# COMMAND ----------

answer <- result %>% head(8) %>% str_c(collapse = "")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that your FFT is working, you can decode the <em>real signal</em>.</p>
# MAGIC <p>The real signal is your puzzle input <em>repeated 10000 times</em>. Treat this new signal as a single input list. Patterns are still calculated as before, and 100 phases of FFT are still applied.</p>
# MAGIC <p>The <em>first seven digits</em> of your initial input signal also represent the <em>message offset</em>. The message offset is the location of the eight-digit message in the final output list. Specifically, the message offset indicates <em>the number of digits to skip</em> before reading the eight-digit message. For example, if the first seven digits of your initial input signal were <code>1234567</code>, the eight-digit message would be the eight digits after skipping 1,234,567 digits of the final output list. Or, if the message offset were <code>7</code> and your final output list were <code>98765432109876543210</code>, the eight-digit message would be <code>21098765</code>. (Of course, your real message offset will be a seven-digit number, not a one-digit number like <code>7</code>.)</p>
# MAGIC <p>Here is the eight-digit message in the final output list after 100 phases. The message offset given in each input has been highlighted. (Note that the inputs given below are repeated 10000 times to find the actual starting input lists.)</p>
# MAGIC <ul>
# MAGIC <li><code><em>0303673</em>2577212944063491565474664</code> becomes <code>84462026</code>.</li>
# MAGIC <li><code><em>0293510</em>9699940807407585447034323</code> becomes <code>78725270</code>.</li>
# MAGIC <li><code><em>0308177</em>0884921959731165446850517</code> becomes <code>53553731</code>.</li>
# MAGIC </ul>
# MAGIC <p>After repeating your input signal 10000 times and running 100 phases of FFT, <em>what is the eight-digit message embedded in the final output list?</em></p>
# MAGIC </article>

# COMMAND ----------

m <- map(seq_len(50), create_pattern, 50) %>% simplify2array() %>% t()
m

# COMMAND ----------

plot_df <-
  m %>%
  as_tibble() %>%
  mutate(y = row_number()) %>%
  pivot_longer(-y, names_to = "x") %>%
  mutate(
    x = str_extract(x, "\\d+") %>% parse_integer()
  )

ggplot(plot_df, aes(x, y, fill = as.factor(value), label = value)) +
  geom_tile() +
  geom_text(size = 2) +
  scale_fill_manual(values = c("red", "grey", "green")) +
  scale_x_continuous(breaks = seq_len(50), expand = c(0, 0)) +
  scale_y_reverse(breaks = seq_len(50), expand = c(0, 0)) +
  theme_void() +
  theme(
    axis.text = element_text(size = rel(0.5)),
    legend.position = "none"
  )

# COMMAND ----------

step <- function(x) x %>% rev() %>% cumsum() %>% `%%`(10) %>% rev()

offset <- head(nums, 7) %>% str_c(collapse = "") %>% parse_integer()

new_nums <- tail(rep(nums, 10000), -offset)
for (i in seq_len(100)) {
  new_nums <- step(new_nums)
}

answer <- head(new_nums, 8)
answer %>% str_c(collapse = "")
