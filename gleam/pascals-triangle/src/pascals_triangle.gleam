import gleam/list

fn rows_impl(n: Int, size: Int, acc: List(List(Int))) -> List(List(Int)) {
  case size == n {
    True -> acc
    False ->
      case acc {
        [] -> rows_impl(n, size + 1, [[1]])
        [first, ..rest] -> {
          let new_row =
            first
            |> list.prepend(0)
            |> list.append([0])
            |> list.window_by_2()
            |> list.map(fn(tuple) { tuple.0 + tuple.1 })
          rows_impl(n, size + 1, [new_row, first, ..rest])
        }
      }
  }
}

pub fn rows(n: Int) -> List(List(Int)) {
  rows_impl(n, 0, [])
  |> list.reverse
}
