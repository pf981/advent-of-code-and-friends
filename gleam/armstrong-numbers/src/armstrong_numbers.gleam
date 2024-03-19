import gleam/list
import gleam/int

fn pow(base: Int, exponent: Int) -> Int {
  case exponent, exponent % 2 == 0 {
    0, _ -> 1
    1, _ -> base
    n, True -> {
      let half_pow = pow(base, n / 2)
      half_pow * half_pow
    }
    n, False -> {
      let half_pow = pow(base, { n - 1 } / 2)
      half_pow * half_pow * base
    }
  }
}

fn get_sum_of_digit_powers(digits: List(Int)) -> Int {
  digits
  |> list.map(pow(_, list.length(digits)))
  |> int.sum()
}

pub fn is_armstrong_number(number: Int) -> Bool {
  case int.digits(number, 10) {
    Ok(digits) -> number == get_sum_of_digit_powers(digits)
    Error(_) -> False
  }
}
