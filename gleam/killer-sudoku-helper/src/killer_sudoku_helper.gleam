import gleam/list

fn comb(target: Int, available: List(Int), size: Int) -> List(List(Int)) {
  case available {
    _ if target == 0 && size == 0 -> [[]]
    _ if target <= 0 || size == 0 -> []
    [] -> []
    [first, ..rest] -> {
      let keep =
        comb(target - first, rest, size - 1)
        |> list.map(list.prepend(_, first))
      let discard = comb(target, rest, size)
      list.append(keep, discard)
    }
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
