import gleam/list

fn comb(available: List(Int), target: Int, size: Int) -> List(List(Int)) {
  case available {
    _ if target == 0 && size == 0 -> [[]]
    _ if target <= 0 || size == 0 -> []
    [] -> []
    [first, ..rest] -> {
      let keep =
        comb(rest, target - first, size - 1)
        |> list.map(list.prepend(_, first))
      let discard = comb(rest, target, size)
      list.append(keep, discard)
    }
  }
}

pub fn combinations(
  size size: Int,
  sum sum: Int,
  exclude exclude: List(Int),
) -> List(List(Int)) {
  list.range(1, 9)
  |> list.filter(fn(el) { !list.contains(exclude, el) })
  |> comb(sum, size)
}
