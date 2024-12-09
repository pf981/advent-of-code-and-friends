

def getVisited(directions: Iterable[Char]): Set[(Int, Int)] =
  directions
    .scanLeft((0, 0)) {
      case ((x, y), direction) =>
        (
          x + (direction == '>').compare(false) - (direction == '<').compare(false),
          y + (direction == 'v').compare(false) - (direction == '^').compare(false),
        )
    }
    .toSet

val answer1: Int = getVisited(input).size
println(answer1)

val answer2: Int =
  input
    .zipWithIndex
    .groupBy { case (_, i) => i % 2 == 0 }
    .map(_._2.map(_._1))
    .flatMap(getVisited)
    .toSet
    .size
println(answer2)
