import gleam/list

pub type Resistance {
  Resistance(unit: String, value: Int)
}

fn to_resitor(resistance: Int) -> Resistance {
  case resistance {
    val if val >= 1_000_000_000 -> Resistance("gigaohms", val / 1_000_000_000)
    val if val >= 1_000_000 -> Resistance("megaohms", val / 1_000_000)
    val if val >= 1000 -> Resistance("kiloohms", val / 1000)
    val -> Resistance("ohms", val)
  }
}

fn pow(base: Int, exponent: Int) -> Int {
  case exponent, exponent % 2 == 0 {
    0, _ -> 1
    1, _ -> base
    _, True -> {
      let half_exponent = pow(base, exponent / 2)
      half_exponent * half_exponent
    }
    _, False -> {
      let half_exponent = pow(base, { exponent - 1 } / 2)
      half_exponent * half_exponent * base
    }
  }
}

pub fn label(colors: List(String)) -> Result(Resistance, Nil) {
  let values =
    list.map(colors, fn(color) {
      case color {
        "black" -> Ok(0)
        "brown" -> Ok(1)
        "red" -> Ok(2)
        "orange" -> Ok(3)
        "yellow" -> Ok(4)
        "green" -> Ok(5)
        "blue" -> Ok(6)
        "violet" -> Ok(7)
        "grey" -> Ok(8)
        "white" -> Ok(9)
        _ -> Error(Nil)
      }
    })
  case values {
    [Ok(a), Ok(b), Ok(c), ..] -> Ok(to_resitor({ 10 * a + b } * pow(10, c)))
    _ -> Error(Nil)
  }
}
