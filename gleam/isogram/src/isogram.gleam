import gleam/set.{type Set}
import gleam/string

const letters = "abcdefghijklmnopqrstuvwxyz"

fn is_isogram_impl(s: List(String), seen: Set(String)) -> Bool {
  case s {
    [] -> True
    [head, ..rest] ->
      case string.contains(letters, head), set.contains(seen, head) {
        True, True -> False
        True, False -> is_isogram_impl(rest, set.insert(seen, head))
        False, _ -> is_isogram_impl(rest, seen)
      }
  }
}

pub fn is_isogram(phrase phrase: String) -> Bool {
  phrase
  |> string.lowercase
  |> string.to_graphemes
  |> is_isogram_impl(set.new())
}
