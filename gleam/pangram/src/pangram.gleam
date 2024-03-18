import gleam/set
import gleam/string

pub fn is_pangram(sentence: String) -> Bool {
  let letters =
    sentence
    |> string.uppercase
    |> string.to_graphemes
    |> set.from_list

  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  |> string.to_graphemes
  |> set.from_list
  |> set.difference(letters)
  |> fn(s) { set.size(s) == 0 }
}
