import gleam/list
import gleam/string

pub fn distance(strand1: String, strand2: String) -> Result(Int, Nil) {
  case string.length(strand1) != string.length(strand2) {
    True -> Error(Nil)
    False -> {
      list.zip(string.to_graphemes(strand1), string.to_graphemes(strand2))
      |> list.fold(0, fn(acc, pair) {
        case pair {
          #(a, b) if a == b -> acc
          _ -> acc + 1
        }
      })
      |> Ok
    }
  }
}
