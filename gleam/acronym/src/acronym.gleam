import gleam/list
import gleam/result
import gleam/string

pub fn abbreviate(phrase phrase: String) -> String {
  phrase
  |> string.uppercase
  |> string.replace("-", " ")
  |> string.replace("_", "")
  |> string.split(" ")
  |> list.map(string.first)
  |> result.values
  |> string.concat
}
