import gleam/bool
import gleam/list

fn comb(target: Int, available: List(Int), size: Int) -> List(List(Int)) {
  use <- bool.guard(target == 0 && size == 0, [[]])
  use <- bool.guard(target <= 0, [])
  use <- bool.guard(size == 0, [])

  case available {
    [first, ..rest] -> {
      let keep =
        comb(target - first, rest, size - 1)
        |> list.map(list.prepend(_, first))
      let discard = comb(target, rest, size)
      list.append(keep, discard)
    }
    [] -> []
  }
}

pub fn combinations(
  size size: Int,
  sum sum: Int,
  exclude exclude: List(Int),
) -> List(List(Int)) {
  let available =
    list.range(1, 9)
    |> list.filter(fn(el) { !list.contains(exclude, el) })

  comb(sum, available, size)
}
