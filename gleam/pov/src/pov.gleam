import gleam/bool
import gleam/list
import gleam/option.{type Option, None, Some}
import gleam/result

pub type Tree(a) {
  Tree(label: a, children: List(Tree(a)))
}

pub fn from_pov_impl(
  tree: Tree(a),
  from: a,
  start: Option(Tree(a)),
) -> Result(Tree(a), Nil) {
  use <- bool.guard(start == Some(tree), Error(Nil))
  let start = Some(option.unwrap(start, tree))

  case tree {
    Tree(label, _) if label == from -> Ok(tree)
    Tree(_, []) -> Error(Nil)
    Tree(_, [child, ..]) -> {
      let tree =
        Tree(..tree, children: list.filter(tree.children, fn(c) { c != child }))

      from_pov_impl(
        Tree(..child, children: list.append(child.children, [tree])),
        from,
        start,
      )
    }
  }
}

pub fn from_pov(tree: Tree(a), from: a) -> Result(Tree(a), Nil) {
  from_pov_impl(tree, from, None)
}

fn find_path(
  tree: List(Tree(a)),
  target: a,
  acc: List(a),
) -> Result(List(a), Nil) {
  case tree {
    [] -> Error(Nil)
    [Tree(label, ..), ..] if label == target -> Ok([label, ..acc])
    [Tree(label, children), ..rest] -> {
      case find_path(children, target, [label, ..acc]) {
        Ok(l) -> Ok(l)
        Error(Nil) -> find_path(rest, target, acc)
      }
    }
  }
}

pub fn path_to(
  tree tree: Tree(a),
  from from: a,
  to to: a,
) -> Result(List(a), Nil) {
  from_pov(tree, from)
  |> result.try(fn(t) { find_path([t], to, []) })
  |> result.map(list.reverse)
}
