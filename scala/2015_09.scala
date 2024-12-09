val regex = raw"(\w+) to (\w+) = (\d+)".r

val distances: Map[(String, String), Int] =
  input
    .split("\n")
    .flatMap {
      case regex(source, dest, d) => Seq((source, dest) -> d.toInt, (dest, source) -> d.toInt)
    }
    .toMap

def getRouteDistance(route: Seq[String], ds: Map[(String, String), Int]): Int =
  route.sliding(2).map(pair => ds(pair(0) -> pair(1))).sum

val routeDistances: Seq[Int] =
  distances
    .map(_._1._1)
    .toSeq
    .distinct
    .permutations
    .map(route => getRouteDistance(route, distances))
    .toSeq

val answer1 = routeDistances.min
println(answer1)

val answer2 = routeDistances.max
println(answer2)
