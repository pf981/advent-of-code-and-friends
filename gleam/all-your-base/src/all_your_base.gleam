import gleam/bool
import gleam/list

pub type Error {
  InvalidBase(Int)
  InvalidDigit(Int)
}

fn to_int(digits: List(Int), base: Int) -> Int {
  digits
  |> list.fold(0, fn(acc, digit) { acc * base + digit })
}

fn to_digits(num: Int, base: Int, acc: List(Int)) -> List(Int) {
  use <- bool.guard(num == 0 && acc == [], [0])
  use <- bool.guard(num == 0, acc)
  to_digits(num / base, base, [num % base, ..acc])
}

pub fn rebase(
  digits digits: List(Int),
  input_base input_base: Int,
  output_base output_base: Int,
) -> Result(List(Int), Error) {
  use <- bool.guard(input_base <= 1, Error(InvalidBase(input_base)))
  use <- bool.guard(output_base <= 1, Error(InvalidBase(output_base)))

  let invalid_digit =
    digits
    |> list.filter(fn(digit) { digit < 0 || digit >= input_base })
    |> list.first

  case invalid_digit {
    Ok(digit) -> Error(InvalidDigit(digit))
    Error(Nil) ->
      digits
      |> to_int(input_base)
      |> to_digits(output_base, [])
      |> Ok
  }
}
