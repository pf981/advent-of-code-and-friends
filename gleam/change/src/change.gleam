import gleam/bool
import gleam/list

pub type Error {
  ImpossibleTarget
}

fn is_worth_trying(candidate, best) {
  case best {
    Ok(l) -> list.length(candidate) < list.length(l)
    _ -> True
  }
}

fn find_best(
  coins: List(Int),
  target: Int,
  acc: List(Int),
  best: Result(List(Int), Error),
) -> Result(List(Int), Error) {
  use <- bool.guard(!is_worth_trying(acc, best), best)
  use <- bool.guard(target == 0, Ok(acc))
  use <- bool.guard(target < 0, best)

  case coins {
    [] -> best
    [first, ..rest] -> {
      let best = find_best(coins, target - first, [first, ..acc], best)
      find_best(rest, target, acc, best)
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
