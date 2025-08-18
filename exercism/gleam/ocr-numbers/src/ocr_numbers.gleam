import gleam/bool
import gleam/list
import gleam/result
import gleam/string

pub type Output {
  Unknown
  Digit(Int)
  List(List(Output))
}

pub type Error {
  InvalidLineNumber
  InvalidRowNumber
}

pub fn convert(input: String) -> Result(Output, Error) {
  let lines =
    string.split(input, "\n")
    |> list.rest
    |> result.unwrap([])

  use <- bool.guard(list.length(lines) % 4 != 0, Error(InvalidLineNumber))
  use <- bool.guard(
    list.any(lines, fn(line) { string.length(line) % 3 != 0 }),
    Error(InvalidRowNumber),
  )

  let digits =
    lines
    |> list.sized_chunk(4)
    |> list.map(fn(rows) {
      rows
      |> split
      |> list.map(parse_digit)
    })

  case digits {
    [[value]] -> Ok(value)
    [[_, _, ..] as l] -> Ok(List(l))
    _ ->
      digits
      |> list.map(List)
      |> List
      |> Ok
  }
}

fn split(lines: List(String)) -> List(#(String, String, String)) {
  lines
  |> list.take(3)
  |> list.map(string.to_graphemes)
  |> list.map(list.sized_chunk(_, 3))
  |> list.transpose
  |> list.map(fn(triplet) {
    case triplet {
      [a, b, c] -> #(string.concat(a), string.concat(b), string.concat(c))
      _ -> #("", "", "")
    }
  })
}

fn parse_digit(lines: #(String, String, String)) -> Output {
  case lines {
    #(" _ ", "| |", "|_|") -> Digit(0)
    #("   ", "  |", "  |") -> Digit(1)
    #(" _ ", " _|", "|_ ") -> Digit(2)
    #(" _ ", " _|", " _|") -> Digit(3)
    #("   ", "|_|", "  |") -> Digit(4)
    #(" _ ", "|_ ", " _|") -> Digit(5)
    #(" _ ", "|_ ", "|_|") -> Digit(6)
    #(" _ ", "  |", "  |") -> Digit(7)
    #(" _ ", "|_|", "|_|") -> Digit(8)
    #(" _ ", "|_|", " _|") -> Digit(9)
    _ -> Unknown
  }
}
