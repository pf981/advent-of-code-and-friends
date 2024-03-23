import gleam/bool
import gleam/int
import gleam/list
import gleam/set.{type Set}

pub fn primes_up_to(upper_bound: Int) -> List(Int) {
  sieve(set.from_list(range(2, upper_bound + 1)), upper_bound, 2)
  |> set.to_list
  |> list.sort(int.compare)
}

fn sieve(candidates: Set(Int), upper_bound: Int, current: Int) -> Set(Int) {
  use <- bool.guard(current > upper_bound, candidates)
  case set.contains(candidates, current) {
    True -> {
      range(2, upper_bound / current + 1)
      |> list.map(fn(x) { x * current })
      |> set.drop(candidates, _)
      |> sieve(upper_bound, current + 1)
    }
    False -> sieve(candidates, upper_bound, current + 1)
  }
}

fn range(start_inclusive: Int, end_exclusive: Int) -> List(Int) {
  case end_exclusive <= start_inclusive {
    True -> []
    False -> list.range(start_inclusive, end_exclusive - 1)
  }
}
