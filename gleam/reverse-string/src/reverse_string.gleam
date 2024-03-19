import gleam/string

fn reverse_impl(s: String, acc: String) -> String {
  case string.pop_grapheme(s) {
    Error(Nil) -> acc
    Ok(#(first, rest)) -> reverse_impl(rest, first <> acc)
  }
}

pub fn reverse(value: String) -> String {
  reverse_impl(value, "")
}
