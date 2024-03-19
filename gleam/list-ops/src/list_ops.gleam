fn prepend_all(first: List(a), second: List(a)) -> List(a) {
  case second {
    [] -> first
    [el, ..rest] -> prepend_all([el, ..first], rest)
  }
}

pub fn append(first first: List(a), second second: List(a)) -> List(a) {
  prepend_all(reverse(first), second)
  |> reverse
}

pub fn concat(lists: List(List(a))) -> List(a) {
  foldl(lists, [], fn(acc, l) { append(acc, l) })
}

pub fn filter(list: List(a), function: fn(a) -> Bool) -> List(a) {
  foldr(list, [], fn(acc, el) {
    case function(el) {
      True -> [el, ..acc]
      False -> acc
    }
  })
}

pub fn length(list: List(a)) -> Int {
  foldl(list, 0, fn(acc, _) { acc + 1 })
}

pub fn map(list: List(a), function: fn(a) -> b) -> List(b) {
  foldr(list, [], fn(acc, el) { [function(el), ..acc] })
}

pub fn foldl(
  over list: List(a),
  from initial: b,
  with function: fn(b, a) -> b,
) -> b {
  case list {
    [] -> initial
    [el, ..rest] -> foldl(rest, function(initial, el), function)
  }
}

pub fn foldr(
  over list: List(a),
  from initial: b,
  with function: fn(b, a) -> b,
) -> b {
  list
  |> reverse
  |> foldl(initial, function)
}

pub fn reverse(list: List(a)) -> List(a) {
  foldl(list, [], fn(acc, el) { [el, ..acc] })
}
