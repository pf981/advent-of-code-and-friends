import gleam/dict.{type Dict}
import gleam/function
import gleam/list
import gleam/regex
import gleam/string

pub fn count_words(input: String) -> Dict(String, Int) {
  let assert Ok(re) = regex.from_string("[a-z0-9]+('[a-z-9]+)?")
  input
  |> string.lowercase
  |> regex.scan(re, _)
  |> list.map(fn(match) {
    let regex.Match(content, ..) = match
    content
  })
  |> list.group(function.identity)
  |> dict.map_values(fn(_, occurances) { list.length(occurances) })
}
