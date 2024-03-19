pub type GbTree(k, v)

@external(erlang, "gb_trees", "empty")
pub fn new_gb_tree() -> GbTree(k, v)

pub fn insert(tree: GbTree(k, v), key: k, value: v) -> GbTree(k, v) {
  insert_impl(key, value, tree)
}

pub fn delete(tree: GbTree(k, v), key: k) -> GbTree(k, v) {
  delete_impl(key, tree)
}

@external(erlang, "gb_trees", "insert")
fn insert_impl(key: k, value: v, tree: GbTree(k, v)) -> GbTree(k, v)

@external(erlang, "gb_trees", "delete_any")
fn delete_impl(key: k, tree: GbTree(k, v)) -> GbTree(k, v)
