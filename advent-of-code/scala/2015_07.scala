sealed trait Instruction {
  def attemptResolve(wires: Map[Wire, Instruction]): Instruction =
    this match {
      case Assign(in: Number) => in
      case And(a: Number, b: Number) => Number(a.number & b.number)
      case Or(a: Number, b: Number) => Number(a.number | b.number)
      case LShift(a: Number, b: Number) => Number(a.number << b.number)
      case RShift(a: Number, b: Number) => Number(a.number >> b.number)
      case Not(a: Number) => Number(~a.number)

      case Assign(in) => Assign(in.attemptResolve(wires))
      case And(a, b) => And(a.attemptResolve(wires), b.attemptResolve(wires))
      case Or(a, b) => Or(a.attemptResolve(wires), b.attemptResolve(wires))
      case LShift(a, b) => LShift(a.attemptResolve(wires), b)
      case RShift(a, b) => RShift(a.attemptResolve(wires), b)
      case Not(a) => Not(a.attemptResolve(wires))

      case _ => this
    }
}
final case class Assign(a: Value) extends Instruction
final case class And(a: Value, b: Value) extends Instruction
final case class Or(a: Value, b: Value) extends Instruction
final case class LShift(a: Value, b: Number) extends Instruction
final case class RShift(a: Value, b: Number) extends Instruction
final case class Not(a: Value) extends Instruction

sealed trait Value extends Instruction {
  override def attemptResolve(wires: Map[Wire, Instruction]): Value = this match {
    case number @ Number(_) => number
    case wire @ Wire(_) =>
      wires(wire) match {
        case number @ Number(_) => number
        case _ => this
      }
  }
}
final case class Number(number: Int) extends Value
final case class Wire(wire: String) extends Value
case object Value {
  def apply(str: String): Value = {
    val numberRegex = raw"(\d+)".r
    str match {
      case numberRegex(value) => Number(value.toInt)
      case value => Wire(value)
    }
  }
}

def parseLine(line: String): (Wire, Instruction) = {
  // Unfortunately, as of writing, Databricks only supports Scala 1.12 So I can't use nicer syntax like:
  //   case s"$a AND $b -> $out" => Wire(out) -> And(Value(a), Value(b))
  val andRegex = raw"(\w+) AND (\w+) -> (\w+)".r
  val orRegex = raw"(\w+) OR (\w+) -> (\w+)".r
  val lShiftRegex = raw"(\w+) LSHIFT (\w+) -> (\w+)".r
  val rShiftRegex = raw"(\w+) RSHIFT (\w+) -> (\w+)".r
  val notRegex = raw"NOT (\w+) -> (\w+)".r
  val assignRegex = raw"(\w+) -> (\w+)".r
  line match {
    case andRegex(a, b, out) => Wire(out) -> And(Value(a), Value(b))
    case orRegex(a, b, out) => Wire(out) -> Or(Value(a), Value(b))
    case lShiftRegex(a, b, out) => Wire(out) -> LShift(Value(a), Number(b.toInt))
    case rShiftRegex(a, b, out) => Wire(out) -> RShift(Value(a), Number(b.toInt))
    case notRegex(a, out) => Wire(out) -> Not(Value(a))
    case assignRegex(a, out) => Wire(out) -> Assign(Value(a))
  }
}

@scala.annotation.tailrec
def getSignal(wires: Map[Wire, Instruction], target: Wire): Int =
  wires(target) match {
    case Number(number) => number
    // case _ => getSignal(wires.view.mapValues(_.attemptResolve(wires)).toMap, target) // Scala 2.13+
    case _ => getSignal(wires.map{case (k, v) => k -> v.attemptResolve(wires)}, target)
    // Using mapValues resulted in a non-hashmap Map implementation in 2.12. So I have to use map
  }

val wires: Map[Wire, Instruction] = input.split("\n").map(parseLine).toMap

val answer1 = getSignal(wires, Wire("a"))
println(answer1)

val answer2 = getSignal(wires + (Wire("b") -> Assign(Number(answer1))), Wire("a"))
println(answer2)
