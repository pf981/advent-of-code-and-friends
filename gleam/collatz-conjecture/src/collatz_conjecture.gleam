pub type Error {
  NonPositiveNumber
}

fn steps_impl(number: Int, acc: Int) -> Int {
  case number % 2 == 0 {
    _ if number == 1 -> acc
    True -> steps_impl(number / 2, acc + 1)
    False -> steps_impl(3 * number + 1, acc + 1)
  }
}

pub fn steps(number: Int) -> Result(Int, Error) {
  case number <= 0 {
    True -> Error(NonPositiveNumber)
    False -> Ok(steps_impl(number, 0))
  }
}
