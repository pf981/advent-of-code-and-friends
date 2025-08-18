import gleam/list
import gleam/int

fn get_multiples(factor: Int, limit: Int) -> List(Int) {
  let max_multiplier = {limit - 1} / factor
  case max_multiplier {
    0 -> []
    _ -> list.range(1, max_multiplier) |> list.map(fn (x) {x * factor})
  }
}

pub fn sum(factors factors: List(Int), limit limit: Int) -> Int {
  factors
  |> list.map(get_multiples(_, limit))
  |> list.flatten()
  |> list.unique()
  |> int.sum()
}
