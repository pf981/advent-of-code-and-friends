def isNice(s: String): Boolean = {
  val containsThreeVowels: Boolean = "[aeiou]".r.findAllIn(s).length >= 3
  val containsDouble: Boolean = raw"(.)\1".r.findFirstMatchIn(s).isDefined
  val containsBadStrings: Boolean = "ab|cd|pq|xy".r.findFirstMatchIn(s).isDefined
  containsThreeVowels && containsDouble && !containsBadStrings
}

val answer1: Int = input.split("\n").filter(isNice).length
println(answer1)

def isNice2(s: String): Boolean = {
  val containsDoublePair: Boolean = raw"(..).*\1".r.findFirstMatchIn(s).isDefined
  val containsSandwich: Boolean = raw"(.).\1".r.findFirstMatchIn(s).isDefined
  containsDoublePair && containsSandwich
}

val answer2: Int = input.split("\n").filter(isNice2).length
println(answer2)
