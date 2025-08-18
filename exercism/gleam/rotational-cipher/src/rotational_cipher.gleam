import gleam/dict.{type Dict}
import gleam/list
import gleam/result
import gleam/string

fn create_mapping(alphabet, shift_key) -> Dict(String, String) {
  let from =
    alphabet
    |> string.to_graphemes
  let parts = list.split(from, shift_key)
  let to = list.append(parts.1, parts.0)

  list.zip(from, to)
  |> dict.from_list
}

pub fn rotate(shift_key: Int, text: String) -> String {
  let mapping =
    dict.merge(
      create_mapping("abcdefghijklmnopqrstuvwxyz", shift_key),
      create_mapping("ABCDEFGHIJKLMNOPQRSTUVWXYZ", shift_key),
    )

  text
  |> string.to_graphemes
  |> list.map(fn(c) {
    dict.get(mapping, c)
    |> result.unwrap(c)
  })
  |> string.concat
}
