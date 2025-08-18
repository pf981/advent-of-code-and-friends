import gleam/list
import gleam/string

fn row(n: Int, width: Int) -> String {
  let assert Ok(codepoint) = string.utf_codepoint(65 + n)
  let letter = string.from_utf_codepoints([codepoint])

  range_up(1, width, [])
  |> range_down(width - 1, -1, _)
  |> list.map(fn(i) {
    case i == n {
      True -> letter
      False -> " "
    }
  })
  |> string.concat
}

fn range_up(start: Int, end: Int, acc: List(Int)) -> List(Int) {
  case start > end - 1 {
    True -> acc
    False -> range_up(start, end - 1, [end - 1, ..acc])
  }
}

fn range_down(start: Int, end: Int, acc: List(Int)) -> List(Int) {
  case end > start - 1 {
    True -> acc
    False -> range_down(start, end + 1, [end + 1, ..acc])
  }
}

pub fn build(letter: String) -> String {
  let assert [codepoint] = string.to_utf_codepoints(letter)
  let n = string.utf_codepoint_to_int(codepoint) - 65
  let width = n + 1

  range_down(n, -1, [])
  |> range_up(0, n, _)
  |> list.map(row(_, width))
  |> string.join("\n")
}
