pub type Tree(a) {
  Leaf
  Node(value: a, left: Tree(a), right: Tree(a))
}

type Direction(a) {
  Left(value: a, right: Tree(a))
  Right(value: a, left: Tree(a))
}

pub opaque type Zipper(a) {
  Zipper(focus: Tree(a), path: List(Direction(a)))
}

pub fn to_zipper(tree: Tree(a)) -> Zipper(a) {
  Zipper(tree, [])
}

pub fn to_tree(zipper: Zipper(a)) -> Tree(a) {
  case up(zipper) {
    Ok(parent) -> to_tree(parent)
    Error(Nil) -> zipper.focus
  }
}

pub fn value(zipper: Zipper(a)) -> Result(a, Nil) {
  case zipper.focus {
    Node(value, ..) -> Ok(value)
    Leaf -> Error(Nil)
  }
}

pub fn up(zipper: Zipper(a)) -> Result(Zipper(a), Nil) {
  case zipper.path {
    [] -> Error(Nil)
    [Left(val, r), ..rest] -> Ok(Zipper(Node(val, zipper.focus, r), rest))
    [Right(val, l), ..rest] -> Ok(Zipper(Node(val, l, zipper.focus), rest))
  }
}

pub fn left(zipper: Zipper(a)) -> Result(Zipper(a), Nil) {
  case zipper.focus {
    Leaf -> Error(Nil)
    Node(val, l, r) -> Ok(Zipper(l, [Left(val, r), ..zipper.path]))
  }
}

pub fn right(zipper: Zipper(a)) -> Result(Zipper(a), Nil) {
  case zipper.focus {
    Leaf -> Error(Nil)
    Node(val, l, r) -> Ok(Zipper(r, [Right(val, l), ..zipper.path]))
  }
}

pub fn set_value(zipper: Zipper(a), value: a) -> Zipper(a) {
  case zipper.focus {
    Leaf -> Zipper(Node(value, Leaf, Leaf), zipper.path)
    Node(_, l, r) -> Zipper(Node(value, l, r), zipper.path)
  }
}

pub fn set_left(zipper: Zipper(a), tree: Tree(a)) -> Result(Zipper(a), Nil) {
  case zipper.focus {
    Leaf -> Error(Nil)
    Node(val, _, r) -> Ok(Zipper(Node(val, tree, r), zipper.path))
  }
}

pub fn set_right(zipper: Zipper(a), tree: Tree(a)) -> Result(Zipper(a), Nil) {
  case zipper.focus {
    Leaf -> Error(Nil)
    Node(val, l, _) -> Ok(Zipper(Node(val, l, tree), zipper.path))
  }
}
