import gleam/float
import gleam/int
import gleam/list
import gleam/result
import gleam/string

fn normalise(text: String) -> String {
  text
  |> string.lowercase
  |> string.to_utf_codepoints
  |> list.filter_map(fn(codepoint) {
    let i = string.utf_codepoint_to_int(codepoint)
    case { i >= 97 && i <= 122 } || { i >= 48 && i <= 57 } {
      True -> Ok(codepoint)
      False -> Error(Nil)
    }
  })
  |> string.from_utf_codepoints
}

pub fn ciphertext(plaintext: String) -> String {
  let text = normalise(plaintext)
  let len = string.length(text)

  let sqrt =
    len
    |> int.to_float()
    |> float.square_root
    |> result.unwrap(0.0)
  let n_cols =
    sqrt
    |> float.ceiling
    |> float.truncate
  let n_rows = float.truncate(sqrt)

  list.range(0, len)
  |> list.map(fn(i) {
    let row = i % n_rows
    let col = i / n_rows
    string.slice(text, n_cols * row + col, 1)
  })
  |> list.sized_chunk(n_rows)
  |> list.intersperse([" "])
  |> list.flatten
  |> string.concat
}

import gleam/io

pub fn main() {
  "If man was meant to stay on the ground, god would have given us roots."
  // |> normalise
  |> ciphertext
  |> io.debug
}
