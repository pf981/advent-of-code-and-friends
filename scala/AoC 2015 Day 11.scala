// Databricks notebook source
// MAGIC %md https://adventofcode.com/2015/day/11

// COMMAND ----------

// MAGIC %md <article class="day-desc"><h2>--- Day 11: Corporate Policy ---</h2><p>Santa's previous password expired, and he needs help choosing a new one.</p>
// MAGIC <p>To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one.  Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by <em>incrementing</em> his old password string repeatedly until it is valid.</p>
// MAGIC <p>Incrementing is just like counting with numbers: <code>xx</code>, <code>xy</code>, <code>xz</code>, <code>ya</code>, <code>yb</code>, and so on. Increase the rightmost letter one step; if it was <code>z</code>, it wraps around to <code>a</code>, and repeat with the next letter to the left until one doesn't wrap around.</p>
// MAGIC <p>Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:</p>
// MAGIC <ul>
// MAGIC <li>Passwords must include one increasing straight of at least three letters, like <code>abc</code>, <code>bcd</code>, <code>cde</code>, and so on, up to <code>xyz</code>. They cannot skip letters; <code>abd</code> doesn't count.</li>
// MAGIC <li>Passwords may not contain the letters <code>i</code>, <code>o</code>, or <code>l</code>, as these letters can be mistaken for other characters and are therefore confusing.</li>
// MAGIC <li>Passwords must contain at least two different, non-overlapping pairs of letters, like <code>aa</code>, <code>bb</code>, or <code>zz</code>.</li>
// MAGIC </ul>
// MAGIC <p>For example:</p>
// MAGIC <ul>
// MAGIC <li><code>hijklmmn</code> meets the first requirement (because it contains the straight <code>hij</code>) but fails the second requirement requirement (because it contains <code>i</code> and <code>l</code>).</li>
// MAGIC <li><code>abbceffg</code> meets the third requirement (because it repeats <code>bb</code> and <code>ff</code>) but fails the first requirement.</li>
// MAGIC <li><code>abbcegjk</code> fails the third requirement, because it only has one double letter (<code>bb</code>).</li>
// MAGIC <li>The next password after <code>abcdefgh</code> is <code>abcdffaa</code>.</li>
// MAGIC <li>The next password after <code>ghijklmn</code> is <code>ghjaabcc</code>, because you eventually skip all the passwords that start with <code>ghi...</code>, since <code>i</code> is not allowed.</li>
// MAGIC </ul>
// MAGIC <p>Given Santa's current password (your puzzle input), what should his <em>next password</em> be?</p>
// MAGIC </article>

// COMMAND ----------

val input = "cqjxjnds"

// COMMAND ----------

@scala.annotation.tailrec
def nextCandidate(l: List[Char], i: Int): List[Char] =
  l(i) match {
    case 'z' => nextCandidate(l.updated(i, 'a'), i - 1)
    case 'h' | 'n' | 'k' => l.updated(i, (l(i) + 2).toChar)
    case _ => l.updated(i, (l(i) + 1).toChar)
  }

def isValid(l: List[Char]): Boolean = {
  val containsStraight = l.sliding(3).exists { case List(a, b, c) => c == b + 1 && b == a + 1 }
  val containsDoubles =
    l.sliding(2).filter { case List(a, b) => a == b }.map(_.head).toSeq.distinct.length > 1
  containsStraight && containsDoubles
}

@scala.annotation.tailrec
def nextPassword(l: List[Char]): String =
  if (isValid(l)) l.mkString
  else nextPassword(nextCandidate(l, l.length - 1))

val answer1 = nextPassword(input.toList)
println(answer1)

// COMMAND ----------

// MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Santa's password <span title="The corporate policy says your password expires after 12 seconds.  For security.">expired again</span>.  What's the next one?</p>
// MAGIC </article>

// COMMAND ----------

val answer2 = nextPassword(nextCandidate(answer1.toList, answer1.length - 1))
println(answer2)
