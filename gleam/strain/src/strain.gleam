import gleam/list

fn keep_impl(list: List(t), predicate: fn(t) -> Bool, acc: List(t)) -> List(t) {
  case list {
    [] -> acc
    [head, ..rest] -> {
      case predicate(head) {
        True -> keep_impl(rest, predicate, [head, ..acc])
        False -> keep_impl(rest, predicate, acc)
      }
    }
  }
}

pub fn keep(list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  keep_impl(list, predicate, [])
  |> list.reverse()
}

pub fn discard(list: List(t), predicate: fn(t) -> Bool) -> List(t) {
  keep_impl(list, fn(el) { !predicate(el) }, [])
  |> list.reverse()
}
