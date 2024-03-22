import gleam/int

pub type Item {
  Item(value: Int, weight: Int)
}

fn knapsack(
  items: List(Item),
  maximum_weight: Int,
  current_value: Int,
  best: Int,
) -> Int {
  case items {
    [] -> int.max(current_value, best)
    [first, ..rest] if first.weight <= maximum_weight ->
      int.max(
        knapsack(
          rest,
          maximum_weight - first.weight,
          current_value + first.value,
          best,
        ),
        knapsack(rest, maximum_weight, current_value, best),
      )
    [_, ..rest] -> knapsack(rest, maximum_weight, current_value, best)
  }
}

pub fn maximum_value(items: List(Item), maximum_weight: Int) -> Int {
  knapsack(items, maximum_weight, 0, 0)
}
