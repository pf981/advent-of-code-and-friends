# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/25
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 25: Combo Breaker ---</h2><p>You finally reach the check-in desk. Unfortunately, their registration systems are currently offline, and they cannot check you in. Noticing the look on your face, they quickly add that tech support is already on the way! They even created all the room keys this morning; you can take yours now and give them your room deposit once the registration system comes back online.</p>
# MAGIC <p>The room key is a small <a href="https://en.wikipedia.org/wiki/Radio-frequency_identification" target="_blank">RFID</a> card. Your room is on the 25th floor and the elevators are also temporarily out of service, so it takes what little energy you have left to even climb the stairs and navigate the halls. You finally reach the door to your room, swipe your card, and - <em>beep</em> - the light turns red.</p>
# MAGIC <p>Examining the card more closely, you discover a phone number for tech support.</p>
# MAGIC <p>"Hello! How can we help you today?" You explain the situation.</p>
# MAGIC <p>"Well, it sounds like the card isn't sending the right command to unlock the door. If you go back to the check-in desk, surely someone there can reset it for you." Still catching your breath, you describe the status of the elevator and the exact number of stairs you just had to climb.</p>
# MAGIC <p>"I see! Well, your only other option would be to reverse-engineer the cryptographic handshake the card does with the door and then inject your own commands into the data stream, but that's definitely impossible." You thank them for their time.</p>
# MAGIC <p>Unfortunately for the door, you know a thing or two about cryptographic handshakes.</p>
# MAGIC <p>The handshake used by the card and the door involves an operation that <em>transforms</em> a <em>subject number</em>. To transform a subject number, start with the value <code>1</code>. Then, a number of times called the <em>loop size</em>, perform the following steps:</p>
# MAGIC <ul>
# MAGIC <li>Set the value to itself multiplied by the <em>subject number</em>.</li>
# MAGIC <li>Set the value to the remainder after dividing the value by <em><code>20201227</code></em>.</li>
# MAGIC </ul>
# MAGIC <p>The card always uses a specific, secret <em>loop size</em> when it transforms a subject number. The door always uses a different, secret loop size.</p>
# MAGIC <p>The cryptographic handshake works like this:</p>
# MAGIC <ul>
# MAGIC <li>The <em>card</em> transforms the subject number of <em><code>7</code></em> according to the <em>card's</em> secret loop size. The result is called the <em>card's public key</em>.</li>
# MAGIC <li>The <em>door</em> transforms the subject number of <em><code>7</code></em> according to the <em>door's</em> secret loop size. The result is called the <em>door's public key</em>.</li>
# MAGIC <li>The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device. Now, the <em>card</em> has the <em>door's</em> public key, and the <em>door</em> has the <em>card's</em> public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.</li>
# MAGIC <li>The <em>card</em> transforms the subject number of <em>the door's public key</em> according to the <em>card's</em> loop size. The result is the <em>encryption key</em>.</li>
# MAGIC <li>The <em>door</em> transforms the subject number of <em>the card's public key</em> according to the <em>door's</em> loop size. The result is the same <em>encryption key</em> as the <em>card</em> calculated.</li>
# MAGIC </ul>
# MAGIC <p>If you can use the two public keys to determine each device's loop size, you will have enough information to calculate the secret <em>encryption key</em> that the card and door use to communicate; this would let you send the <code>unlock</code> command directly to the door!</p>
# MAGIC <p>For example, suppose you know that the card's public key is <code>5764801</code>. With a little trial and error, you can work out that the card's loop size must be <em><code>8</code></em>, because transforming the initial subject number of <code>7</code> with a loop size of <code>8</code> produces <code>5764801</code>.</p>
# MAGIC <p>Then, suppose you know that the door's public key is <code>17807724</code>. By the same process, you can determine that the door's loop size is <em><code>11</code></em>, because transforming the initial subject number of <code>7</code> with a loop size of <code>11</code> produces <code>17807724</code>.</p>
# MAGIC <p>At this point, you can use either device's loop size with the other device's public key to calculate the <em>encryption key</em>. Transforming the subject number of <code>17807724</code> (the door's public key) with a loop size of <code>8</code> (the card's loop size) produces the encryption key, <em><code>14897079</code></em>. (Transforming the subject number of <code>5764801</code> (the card's public key) with a loop size of <code>11</code> (the door's loop size) produces the same encryption key: <em><code>14897079</code></em>.)</p>
# MAGIC <p><em>What encryption key is the handshake trying to establish?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>296776</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
# MAGIC <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><span title="You notice the brand written on the side of the lock: Diffie, Hellman, and Merkle.">The light turns green and the door unlocks.</span> As you collapse onto the bed in your room, your pager goes off!</p>
# MAGIC <p>"It's an emergency!" the Elf calling you explains. "The <a href="https://en.wikipedia.org/wiki/Soft_serve" target="_blank">soft serve</a> machine in the cafeteria on sub-basement 7 just failed and you're the only one that knows how to fix it! We've already dispatched a reindeer to your location to pick you up."</p>
# MAGIC <p>You hear the sound of hooves landing on your balcony.</p>
# MAGIC <p>The reindeer carefully explores the contents of your room while you figure out how you're going to pay the <em class="star">50 stars</em> you owe the resort before you leave. Noticing that you look concerned, the reindeer wanders over to you; you see that it's carrying a small pouch.</p>
# MAGIC <p>"Sorry for the trouble," a note in the pouch reads. Sitting at the bottom of the pouch is a gold coin with a little picture of a starfish on it.</p>
# MAGIC <p>Looks like you only needed <em class="star">49 stars</em> after all.</p>
# MAGIC </article>
# MAGIC <p>You don't have enough stars to pay the deposit, though.  You need 10 more.</p>
# MAGIC <p>Although it hasn't changed, you can still <a href="25/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Combo+Breaker%22+%2D+Day+25+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F25&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+Part+One+of+%22Combo+Breaker%22+%2D+Day+25+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F25'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "12578151
5051300"

# COMMAND ----------

# input <- "5764801
# 17807724"

# COMMAND ----------

public_keys <- read_lines(input)
public_keys

# COMMAND ----------

encrypt <- function(subject_number, loop_size) {
  value <- 1
  for (i in seq_len(loop_size)) {
    value <- (value * subject_number) %% 20201227
  }
  value
}

# COMMAND ----------

compute_loop_size <- function(public_key) {
  value <- 1
  loop_size <- 0
  repeat {
    loop_size <- loop_size + 1
    value <- (value * 7) %% 20201227
    if (value == public_key) {
      break
    }
  }
  loop_size
}

# COMMAND ----------

loop_sizes <- c(
  compute_loop_size(public_keys[1]),
  compute_loop_size(public_keys[2])
)
loop_sizes

# COMMAND ----------

encryption_key <- encrypt(
  encrypt(subject_numbers[1], loop_sizes[1]),
  loop_sizes[2]
)
encryption_key

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# MAGIC %md Part 2 is just having 50 stars.