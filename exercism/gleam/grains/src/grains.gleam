import gleam/int
import gleam/list
import gleam/result

pub type Error {
  InvalidSquare
}

fn pow(base: Int, exponent: Int) -> Int {
  case exponent == 0 {
    True -> 1
    False ->
      case exponent % 2 == 0 {
        True -> {
          let half_exp = pow(base, exponent / 2)
          half_exp * half_exp
        }
        False -> {
          let half_exp = pow(base, { exponent - 1 } / 2)
          half_exp * half_exp * base
        }
      }
  }
}

pub fn square(square: Int) -> Result(Int, Error) {
  case square > 0 && square <= 64 {
    True -> Ok(pow(2, square - 1))
    _ -> Error(InvalidSquare)
  }
}

pub fn total() -> Int {
  list.range(1, 64)
  |> list.map(square)
  |> result.values
  |> int.sum
}
