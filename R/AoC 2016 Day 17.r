# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 17: Two Steps Forward ---</h2><p>You're trying to access a secure vault protected by a <code>4x4</code> grid of small rooms connected by doors. You start in the top-left room (marked <code>S</code>), and you can access the vault (marked <code>V</code>) once you reach the bottom-right room:</p>
# MAGIC <pre><code>#########
# MAGIC #S| | | #
# MAGIC #-#-#-#-#
# MAGIC # | | | #
# MAGIC #-#-#-#-#
# MAGIC # | | | #
# MAGIC #-#-#-#-#
# MAGIC # | | |  
# MAGIC ####### V
# MAGIC </code></pre>
# MAGIC <p>Fixed walls are marked with <code>#</code>, and doors are marked with <code>-</code> or <code>|</code>.</p>
# MAGIC <p>The doors in your <em>current room</em> are either open or closed (and locked) based on the hexadecimal <a href="https://en.wikipedia.org/wiki/MD5">MD5</a> hash of a passcode (your puzzle input) followed by a sequence of uppercase characters representing the <em>path you have taken so far</em> (<code>U</code> for up, <code>D</code> for down, <code>L</code> for left, and <code>R</code> for right).</p>
# MAGIC <p>Only the first four characters of the hash are used; they represent, respectively, the doors <em>up, down, left, and right</em> from your current position. Any <code>b</code>, <code>c</code>, <code>d</code>, <code>e</code>, or <code>f</code> means that the corresponding door is <em>open</em>; any other character (any number or <code>a</code>) means that the corresponding door is <em>closed and locked</em>.</p>
# MAGIC <p>To access the vault, all you need to do is reach the bottom-right room; reaching this room opens the vault and all doors in the maze.</p>
# MAGIC <p>For example, suppose the passcode is <code>hijkl</code>. Initially, you have taken no steps, and so your path is empty: you simply find the MD5 hash of <code>hijkl</code> alone. The first four characters of this hash are <code>ced9</code>, which indicate that up is open (<code>c</code>), down is open (<code>e</code>), left is open (<code>d</code>), and right is closed and locked (<code>9</code>). Because you start in the top-left corner, there are no "up" or "left" doors to be open, so your only choice is <em>down</em>.</p>
# MAGIC <p>Next, having gone only one step (down, or <code>D</code>), you find the hash of <code>hijkl<em>D</em></code>. This produces <code>f2bc</code>, which indicates that you can go back up, left (but that's a wall), or right. Going right means hashing <code>hijkl<em>DR</em></code> to get <code>5745</code> - all doors closed and locked. However, going <em>up</em> instead is worthwhile: even though it returns you to the room you started in, your path would then be <code>DU</code>, opening a <em>different set of doors</em>.</p>
# MAGIC <p>After going <code>DU</code> (and then hashing <code>hijkl<em>DU</em></code> to get <code>528e</code>), only the right door is open; after going <code>DUR</code>, all doors lock. (Fortunately, your actual passcode is <span title="It took four days to rescue the engineer that tried this.">not <code>hijkl</code></span>).</p>
# MAGIC <p>Passcodes actually used by Easter Bunny Vault Security do allow access to the vault if you know the right path.  For example:</p>
# MAGIC <ul>
# MAGIC <li>If your passcode were <code>ihgpwlah</code>, the shortest path would be <code>DDRRRD</code>.</li>
# MAGIC <li>With <code>kglvqrro</code>, the shortest path would be <code>DDUDRLRRUDRD</code>.</li>
# MAGIC <li>With <code>ulqzkmiv</code>, the shortest would be <code>DRURDRUDDLLDLUURRDULRLDUUDDDRR</code>.</li>
# MAGIC </ul>
# MAGIC <p>Given your vault's passcode, <em>what is the shortest path</em> (the actual path, not just the length) to reach the vault?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "awrkjxxr"

# COMMAND ----------

get_directions <- function(hash_input) {
  first_four <-
    hash_input %>%
    openssl::md5() %>%
    str_split("") %>%
    unlist() %>%
    head(4)
  
  c("U", "D", "L", "R")[first_four %in% c("b", "c", "d", "e", "f")]
}

shortest_path <- function(start_hash) {
  xs <- c(1)
  ys <- c(1)
  hash_inputs <- c(start_hash)
  path_lengths <- c(0)
  
  repeat {
    # Choose the shortest path so far
    i <- which.min(path_lengths)
    
    x <- xs[i]
    y <- ys[i]
    hash_input <- hash_inputs[i]
    path_length <- path_lengths[i]
    
    xs <- xs[-i]
    ys <- ys[-i]
    hash_inputs <- hash_inputs[-i]
    path_lengths <- path_lengths[-i]
    
    
    # For each possible move
    for (direction in get_directions(hash_input)) {
      new_x <- x + case_when(direction == "R" ~ 1, direction == "L" ~ -1, TRUE ~ 0)
      new_y <- y + case_when(direction == "U" ~ -1, direction == "D" ~ 1, TRUE ~ 0)
      new_hash_input <- str_c(hash_input, direction)
      
      if (new_x < 1 || new_x > 4 || new_y < 1 || new_y > 4) {
        next
      }
      
      if (new_x == 4 && new_y == 4) {
        return(new_hash_input)
      }
      
      xs <- c(xs, new_x)
      ys <- c(ys, new_y)
      hash_inputs <- c(hash_inputs, new_hash_input)
      path_lengths <- c(path_lengths, path_length + 1)
    }
  }
}

# COMMAND ----------

result <- shortest_path(input)
result

# COMMAND ----------

answer <- result %>% str_remove("^[a-z]+")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You're curious how robust this security solution really is, and so you decide to find longer and longer paths which still provide access to the vault. You remember that paths always end the first time they reach the bottom-right room (that is, they can never pass through it, only end in it).</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>If your passcode were <code>ihgpwlah</code>, the longest path would take <code>370</code> steps.</li>
# MAGIC <li>With <code>kglvqrro</code>, the longest path would be <code>492</code> steps long.</li>
# MAGIC <li>With <code>ulqzkmiv</code>, the longest path would be <code>830</code> steps long.</li>
# MAGIC </ul>
# MAGIC <p></p>
# MAGIC <p>What is the <em>length of the longest path</em> that reaches the vault?</p>
# MAGIC </article>

# COMMAND ----------

longest_path <- function(hash_input, x = 1, y = 1) {
  if (x == 4 && y == 4) {
    return(0)
  }
  if (x < 1 || x > 4 || y < 1 || y > 4) {
    return(NA)
  }
  
  longest_path <- NA

  for (direction in get_directions(hash_input)) {
    new_x <- x + case_when(direction == "R" ~ 1, direction == "L" ~ -1, TRUE ~ 0)
    new_y <- y + case_when(direction == "U" ~ -1, direction == "D" ~ 1, TRUE ~ 0)
    new_hash_input <- str_c(hash_input, direction)

    new_path_length <- 1 + longest_path(new_hash_input, new_x, new_y)
    if ((!is.na(new_path_length) && new_path_length > longest_path) || is.na(longest_path)) {
      longest_path <- new_path_length
    }
  }
  longest_path
}

# COMMAND ----------

answer <- longest_path(input)
answer
