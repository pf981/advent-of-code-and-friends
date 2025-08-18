import gleam/float
import gleam/int
import gleam/iterator
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
  let normalised = normalise(plaintext)
  let len = string.length(normalised)
  let n_cols =
    len
    |> int.to_float()
    |> float.square_root
    |> result.unwrap(0.0)
    |> float.ceiling
    |> float.truncate
  let n_rows = case n_cols * { n_cols - 1 } >= len {
    True -> n_cols - 1
    False -> n_cols
  }
  let text = string.pad_right(normalised, n_cols * n_rows, " ")

  iterator.iterate(#(0, 0), fn(pair) {
    let #(row, col) = pair
    case row == n_rows - 1 {
      True -> #(0, col + 1)
      False -> #(row + 1, col)
    }
  })
  |> iterator.take(n_cols * n_rows)
  |> iterator.map(fn(pair) { string.slice(text, n_cols * pair.0 + pair.1, 1) })
  |> iterator.to_list
  |> list.sized_chunk(n_rows)
  |> list.intersperse([" "])
  |> list.flatten
  |> string.concat
}
