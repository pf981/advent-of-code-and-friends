

import collection.immutable.Queue

def lookAndSay(queue: Queue[Int]): Queue[Int] =
  queue
    .:+(-1)
    .foldLeft((Queue[Int](), (-1, -1))) {
      case ((q, (digitCount, digit)), d) =>
        if (digit == -1) (q, (1, d))
        else if (d == digit) (q, (digitCount + 1, digit))
        else (q :+ digitCount :+ digit, (1, d))
    }
    ._1

def solve(queue: Queue[Int], n: Int): Int =
  (0 until n).foldLeft(queue) { case (q, _) => lookAndSay(q) }.length

val queue: Queue[Int] = input.map(_.asDigit).to[Queue] // to(Queue) in scala 2.13+

val answer1 = solve(queue, 40)
println(answer1)

val answer2 = solve(queue, 50)
println(answer2)
