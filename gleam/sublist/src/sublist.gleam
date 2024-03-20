import gleam/bool
import gleam/list

pub type Comparison {
  Equal
  Unequal
  Sublist
  Superlist
}

fn is_sublist(list_a: List(a), list_b: List(a)) -> Bool {
  use <- bool.guard(list_a == [], True)
  list_b
  |> list.window(list.length(list_a))
  |> list.contains(list_a)
}

pub fn sublist(compare list_a: List(a), to list_b: List(a)) -> Comparison {
  use <- bool.guard(list_a == list_b, Equal)
  use <- bool.guard(is_sublist(list_a, list_b), Sublist)
  use <- bool.guard(is_sublist(list_b, list_a), Superlist)
  Unequal
}
