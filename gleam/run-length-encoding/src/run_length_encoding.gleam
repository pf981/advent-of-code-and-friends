import gleam/int
import gleam/list
import gleam/pair
import gleam/result
import gleam/string

pub fn encode(plaintext: String) -> String {
  plaintext
  |> string.to_graphemes
  |> list.prepend("")
  |> list.append([""])
  |> list.window_by_2()
  |> list.fold(#(0, ""), fn(acc_pair, window_pair) {
    let #(count, acc) = acc_pair
    let #(a, b) = window_pair

    case a == b {
      True -> #(count + 1, acc)
      False if count == 1 -> #(1, acc <> a)
      False if count != 0 -> #(1, acc <> int.to_string(count) <> a)
      _ -> #(1, acc)
    }
  })
  |> pair.second
}

pub fn decode(ciphertext: String) -> String {
  ciphertext
  |> string.to_graphemes
  |> list.fold(#("", ""), fn(pair, char) {
    let #(digits, acc) = pair

    case string.contains("1234567890", char) {
      True -> #(digits <> char, acc)
      False -> {
        let num =
          digits
          |> int.base_parse(10)
          |> result.unwrap(1)
        #("", acc <> string.repeat(char, num))
      }
    }
  })
  |> pair.second
}
