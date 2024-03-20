import gleam/list
import gleam/result
import gleam/string

pub fn distance(strand1: String, strand2: String) -> Result(Int, Nil) {
  list.strict_zip(string.to_graphemes(strand1), string.to_graphemes(strand2))
  |> result.map(list.fold(
    _,
    0,
    fn(acc, pair) {
      case pair {
        #(a, b) if a == b -> acc
        _ -> acc + 1
      }
    },
  ))
  |> result.replace_error(Nil)
}
