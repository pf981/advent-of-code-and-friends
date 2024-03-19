import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/result
import gleam/string

type Pos {
  Pos(row: Int, col: Int)
}

type Symbol {
  Corner
  EdgeHorizontal
  EdgeVertical
}

fn to_symbol(char: String) -> Result(Symbol, Nil) {
  case char {
    "+" -> Ok(Corner)
    "-" -> Ok(EdgeHorizontal)
    "|" -> Ok(EdgeVertical)
    _ -> Error(Nil)
  }
}

fn parse_line(chars: List(String), row: Int) -> List(#(Pos, Symbol)) {
  list.index_map(chars, fn(char, col) {
    char
    |> to_symbol
    |> result.map(fn(symbol) { #(Pos(row, col), symbol) })
  })
  |> result.values
}

fn parse(input: String) -> Dict(Pos, Symbol) {
  input
  |> string.split("\n")
  |> list.map(string.to_graphemes)
  |> list.index_map(parse_line)
  |> list.flatten
  |> dict.from_list
}

fn find_top_right(m: Dict(Pos, Symbol), top_left: Pos, pos: Pos) -> Int {
  case dict.get(m, pos) {
    Error(Nil) | Ok(EdgeVertical) -> 0
    Ok(Corner) ->
      find_bottom_right(m, top_left, Pos(pos.row + 1, pos.col))
      + find_top_right(m, top_left, Pos(pos.row, pos.col + 1))
    Ok(EdgeHorizontal) -> find_top_right(m, top_left, Pos(pos.row, pos.col + 1))
  }
}

fn find_bottom_right(m: Dict(Pos, Symbol), top_left: Pos, pos: Pos) -> Int {
  case dict.get(m, pos) {
    Error(Nil) | Ok(EdgeHorizontal) -> 0
    Ok(Corner) ->
      find_bottom_left(m, top_left, Pos(pos.row, pos.col - 1))
      + find_bottom_right(m, top_left, Pos(pos.row + 1, pos.col))
    Ok(EdgeVertical) ->
      find_bottom_right(m, top_left, Pos(pos.row + 1, pos.col))
  }
}

fn find_bottom_left(m: Dict(Pos, Symbol), top_left: Pos, pos: Pos) -> Int {
  case dict.get(m, pos) {
    Error(Nil) | Ok(EdgeVertical) -> 0
    Ok(Corner) ->
      find_top_left(m, top_left, Pos(pos.row - 1, pos.col))
      + find_bottom_left(m, top_left, Pos(pos.row, pos.col - 1))
    Ok(EdgeHorizontal) ->
      find_bottom_left(m, top_left, Pos(pos.row, pos.col - 1))
  }
}

fn find_top_left(m: Dict(Pos, Symbol), top_left: Pos, pos: Pos) -> Int {
  case dict.get(m, pos) {
    Error(Nil) | Ok(EdgeHorizontal) -> 0
    Ok(Corner) if top_left == pos -> 1
    Ok(EdgeVertical) | Ok(Corner) ->
      find_top_left(m, top_left, Pos(pos.row - 1, pos.col))
  }
}

fn count_rectangles(m: Dict(Pos, Symbol), pos: Pos) -> Int {
  find_top_right(m, pos, Pos(pos.row, pos.col + 1))
}

pub fn rectangles(input: String) -> Int {
  let m = parse(input)

  m
  |> dict.filter(fn(_pos, symbol) { symbol == Corner })
  |> dict.keys
  |> list.map(count_rectangles(m, _))
  |> int.sum
}
