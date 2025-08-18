import gleam/list

pub type Tree {
  Nil
  Node(data: Int, left: Tree, right: Tree)
}

fn add_value(head: Tree, value: Int) -> Tree {
  case head {
    Nil -> Node(value, Nil, Nil)
    Node(data, left, right) if value <= data ->
      Node(data, add_value(left, value), right)
    Node(data, left, right) -> Node(data, left, add_value(right, value))
  }
}

pub fn to_tree(data: List(Int)) -> Tree {
  list.fold(data, Nil, add_value)
}

fn sort_tree(head: Tree) -> List(Int) {
  case head {
    Nil -> []
    Node(data, left, right) ->
      list.append(sort_tree(left), [data, ..sort_tree(right)])
  }
}

pub fn sorted_data(data: List(Int)) -> List(Int) {
  data
  |> to_tree
  |> sort_tree
}
