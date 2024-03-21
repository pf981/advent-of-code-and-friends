import gleam/bool
import gleam/list
import gleam/result

pub type Error {
  ImpossibleTarget
}

fn find_best(
  coins: List(Int),
  target: Int,
  acc: List(Int),
  best: Result(List(Int), Error),
) -> Result(List(Int), Error) {
  use <- bool.guard(
    result.unwrap(
      result.map(best, fn(b) { list.length(acc) >= list.length(b) }),
      False,
    ),
    best,
  )
  use <- bool.guard(target == 0, Ok(acc))
  use <- bool.guard(target < 0, Error(ImpossibleTarget))

  case coins {
    [] -> Error(ImpossibleTarget)
    [first, ..rest] -> {
      let best =
        find_best(coins, target - first, [first, ..acc], best)
        |> result.or(best)
      let best =
        find_best(rest, target, acc, best)
        |> result.or(best)
      best
    }
  }
}

pub fn find_fewest_coins(
  coins: List(Int),
  target: Int,
) -> Result(List(Int), Error) {
  coins
  |> list.reverse
  |> find_best(target, [], Error(ImpossibleTarget))
}
