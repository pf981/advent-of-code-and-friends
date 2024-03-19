import gleam/list
import gleam/result
import gleam/string

type Shape {
  Square
  Curly
  Round
}

type Bracket {
  Open(Shape)
  Close(Shape)
}

fn to_bracket(char: String) -> Result(Bracket, Nil) {
  case char {
    "[" -> Ok(Open(Square))
    "{" -> Ok(Open(Curly))
    "(" -> Ok(Open(Round))
    "]" -> Ok(Close(Square))
    "}" -> Ok(Close(Curly))
    ")" -> Ok(Close(Round))
    _ -> Error(Nil)
  }
}

fn is_paired_impl(value: List(Bracket), acc: List(Shape)) -> Bool {
  case value, acc {
    [], [] -> True
    [], _ -> False
    [Open(shape), ..rest], _ -> is_paired_impl(rest, [shape, ..acc])
    [Close(seen), ..rest], [expected, ..rest_acc] if seen == expected ->
      is_paired_impl(rest, rest_acc)
    _, _ -> False
  }
}

pub fn is_paired(value: String) -> Bool {
  value
  |> string.to_graphemes
  |> list.map(to_bracket)
  |> result.values
  |> is_paired_impl([])
}
