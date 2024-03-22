import gleam/bool
import gleam/dict.{type Dict}
import gleam/list
import gleam/result
import gleam/set.{type Set}
import gleam/string

pub type Player {
  X
  O
}

type Pos =
  #(Int, Int)

import gleam/io

pub fn main() {
  parse_board(
    "
O O O X
 X . . X
  X . . X
   X O O O",
  )
}

fn parse_board(board: String) -> #(Dict(Player, Set(Pos)), Int, Int) {
  let rows =
    board
    |> string.replace(" ", "")
    |> string.split("\n")
    |> list.filter(fn(row) { row != "" })
    |> io.debug

  rows
  |> list.index_map(fn(row, j) {
    row
    |> string.to_graphemes
    |> list.index_map(fn(i, c) { #(i, j, c) })
  })
  // FIXME: This is not the right coordinates
  |> io.debug

  #(
    dict.new(),
    list.length(rows),
    rows
      |> list.first
      |> result.unwrap("")
      |> string.length(),
  )
}

fn neighbors(pos: Pos) -> List(Pos) {
  let #(i, j) = pos
  [
    #(i, j - 1),
    #(i, j + 1),
    #(i + 1, j),
    #(i - 1, j),
    #(i + 1, j - 1),
    #(i - 1, j + 1),
  ]
}

fn check_win_impl(
  positions: List(Pos),
  valid: Set(Pos),
  seen: Set(Pos),
  win_condition: fn(Pos) -> Bool,
) -> Bool {
  case positions {
    [pos, ..rest] -> {
      use <- bool.guard(
        !set.contains(valid, pos) || set.contains(seen, pos),
        check_win_impl(rest, valid, seen, win_condition),
      )
      win_condition(pos)
      || check_win_impl(
        list.append(rest, neighbors(pos)),
        set.insert(seen, pos),
        valid,
        win_condition,
      )
    }
    [] -> False
  }
}

fn check_win(
  valid: Set(Pos),
  start_condition: fn(Pos) -> Bool,
  win_condition: fn(Pos) -> Bool,
) {
  valid
  |> set.filter(start_condition)
  |> set.to_list
  |> check_win_impl(valid, set.new(), win_condition)
}

pub fn winner(board: String) -> Result(Player, Nil) {
  let #(board, i_max, j_max) = parse_board(board)

  use <- bool.guard(
    check_win(
      result.unwrap(dict.get(board, X), set.new()),
      fn(pos) { pos.0 == 0 },
      fn(pos) { pos.0 == i_max },
    ),
    Ok(X),
  )
  use <- bool.guard(
    check_win(
      result.unwrap(dict.get(board, O), set.new()),
      fn(pos) { pos.1 == 0 },
      fn(pos) { pos.1 == j_max },
    ),
    Ok(O),
  )
  Error(Nil)
}
