

val answer1: Int = input.map(c => if (c == '(') 1 else -1).sum
println(answer1)

@scala.annotation.tailrec
def solve(
    s: String,
    floor: Int,
    position: Int,
  ): Int =
  if (floor == -1) position
  else solve(s.tail, floor + (if (s.head == '(') 1 else -1), position + 1)

val answer2 = solve(input, 0, 0)
println(answer2)
