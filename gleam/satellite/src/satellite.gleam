import gleam/bool
import gleam/list
import gleam/set

pub type Tree(a) {
  Nil
  Node(value: a, left: Tree(a), right: Tree(a))
}

pub type Error {
  DifferentLengths
  DifferentItems
  NonUniqueItems
}

fn split_on(list: List(a), value: a) -> #(List(a), List(a)) {
  let #(left, right) = list.split_while(list, fn(el) { el != value })
  let right = list.drop(right, 1)

  #(left, right)
}

fn tree_from_traversals_impl(inorder: List(a), preorder: List(a)) -> Tree(a) {
  case preorder {
    [] -> Nil
    [first, ..rest] -> {
      let #(inorder_left, inorder_right) = split_on(inorder, first)
      let #(preorder_left, preorder_right) =
        list.split(rest, list.length(inorder_left))

      let left = tree_from_traversals_impl(inorder_left, preorder_left)
      let right = tree_from_traversals_impl(inorder_right, preorder_right)

      Node(first, left, right)
    }
  }
}

pub fn tree_from_traversals(
  inorder inorder: List(a),
  preorder preorder: List(a),
) -> Result(Tree(a), Error) {
  use <- bool.guard(
    list.length(inorder) != list.length(preorder),
    Error(DifferentLengths),
  )
  use <- bool.guard(
    set.from_list(inorder) != set.from_list(preorder),
    Error(DifferentItems),
  )
  use <- bool.guard(
    set.size(set.from_list(inorder)) != list.length(inorder),
    Error(NonUniqueItems),
  )

  Ok(tree_from_traversals_impl(inorder, preorder))
}
