fn reverse_impl(list: List(a), acc: List(a)) -> List(a) {
  case list {
    [] -> acc
    [head, ..rest] -> reverse_impl(rest, [head, ..acc])
  }
}

fn reverse(list: List(a)) -> List(a) {
  reverse_impl(list, [])
}

fn accumulate_impl(list: List(a), acc: List(b), fun: fn(a) -> b) -> List(b) {
  case list {
    [] -> acc
    [head, ..rest] -> accumulate_impl(rest, [fun(head), ..acc], fun)
  }
}

pub fn accumulate(list: List(a), fun: fn(a) -> b) -> List(b) {
  accumulate_impl(list, [], fun)
  |> reverse
}
