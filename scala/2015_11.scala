

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

val answer2 = nextPassword(nextCandidate(answer1.toList, answer1.length - 1))
println(answer2)
