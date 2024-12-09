final case class Instruction(
    action: String,
    rowStart: Int,
    colStart: Int,
    rowEnd: Int,
    colEnd: Int,
  )

final case class Light(
    isLit: Boolean,
    brightness: Int,
  )

def parseLine(line: String): Instruction = {
  val regex = raw"(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)".r
  line match {
    case regex(action, rowStart, colStart, rowEnd, colEnd) =>
      Instruction(action, rowStart.toInt, colStart.toInt, rowEnd.toInt, colEnd.toInt)
  }
}

val lights: Map[(Int, Int), Light] =
  input.split("\n").foldLeft(Map[(Int, Int), Light]().withDefaultValue(Light(false, 0))) {
    (m, line) =>
      val inst: Instruction = parseLine(line)
      val positions: Seq[(Int, Int)] = for {
        row <- inst.rowStart to inst.rowEnd
        col <- inst.colStart to inst.colEnd
      } yield (row, col)

      positions.foldLeft(m) { (mNew, position) =>
        inst.action match {
          case "turn on" =>
            mNew + (position -> Light(true, mNew(position).brightness + 1))
          case "toggle" =>
            mNew + (position -> Light(!mNew(position).isLit, mNew(position).brightness + 2))
          case "turn off" =>
            mNew + (position -> Light(false, math.max(mNew(position).brightness - 1, 0)))
        }
      }
  }

val answer1: Int = lights.values.filter(_.isLit).size
println(answer1)

val answer2: Int = lights.values.map(_.brightness).sum
println(answer2)
