import gleam/int

pub type Item {
  Item(value: Int, weight: Int)
}

pub fn maximum_value(items: List(Item), maximum_weight: Int) -> Int {
  case items {
    [] -> 0
    [first, ..rest] if first.weight <= maximum_weight ->
      int.max(
        first.value + maximum_value(rest, maximum_weight - first.weight),
        maximum_value(rest, maximum_weight),
      )
    [_, ..rest] -> maximum_value(rest, maximum_weight)
  }
}
