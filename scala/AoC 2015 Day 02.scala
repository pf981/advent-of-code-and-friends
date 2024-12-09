val presents: Array[Array[Int]] = input.split("\n").map(_.split("x").map(_.toInt))
val wrapping_paper_areas: Array[Int] = presents.map { dimensions =>
  val (l, w, h) = (dimensions(0), dimensions(1), dimensions(2))
  2 * l * w + 2 * w * h + 2 * h * l + Seq(l * w, w * h, h * l).min
}

val answer1: Int = wrapping_paper_areas.sum
println(answer1)

val ribbon_lengths: Array[Int] = presents.map { dimensions =>
  val (l, w, h) = (dimensions(0), dimensions(1), dimensions(2))
  2 * Seq(l + w, w + h, h + l).min + l * w * h
}

val answer2: Int = ribbon_lengths.sum
println(answer2)
