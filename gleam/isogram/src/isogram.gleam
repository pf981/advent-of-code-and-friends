import gleam/list
import gleam/string

pub fn is_isogram(phrase phrase: String) -> Bool {
  phrase
  |> string.lowercase()
  |> string.replace(" ", "")
  |> string.replace("-", "")
  |> string.to_graphemes()
  |> fn(letters) { list.unique(letters) == letters }
}
