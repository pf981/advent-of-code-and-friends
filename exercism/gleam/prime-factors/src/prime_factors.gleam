import gleam/bool
import gleam/list

fn factors_impl(value: Int, candidate, acc: List(Int)) -> List(Int) {
  use <- bool.guard(value == 1, acc)
  case value % candidate == 0 {
    True -> factors_impl(value / candidate, candidate, [candidate, ..acc])
    False -> factors_impl(value, candidate + 1, acc)
  }
}

pub fn factors(value: Int) -> List(Int) {
  factors_impl(value, 2, [])
  |> list.reverse
}
