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
  // "
  // O O O X
  //  X . . X
  //   X . . X
  //    X O O O"
  //   "
  // O X X X X X X X X
  //  O X O O O O O O O
  //   O X O X X X X X O
  //    O X O X O O O X O
  //     O X O X X X O X O
  //      O X O O O X O X O
  //       O X X X X X O X O
  //        O O O O O O O X O
  //         X X X X X X X X O"
  //   "
  // . O . .
  //  O X X X
  //   O X O .
  //    X X O X
  //     . O X ."
  //   "
  // . O . .
  //  O X X X
  //   O O O .
  //    X X O X
  //     . O X ."
  //   |> winner
  //   |> io.debug
  let board =
    "
. O . .
 O X X X
  O O O .
   X X O X
    . O X ."
  //     "
  // . O . .
  //  O X X X
  //   O X O .
  //    X X O X
  //     . O X ."
  let #(hexes, n_rows, n_cols) = parse_board(board)
  let p =
    player_hexes(hexes, O)
    // player_hexes(hexes, X)
    |> io.debug

  let start = fn(pos: #(Int, Int)) { pos.1 == 0 }
  let end = fn(pos: #(Int, Int)) { pos.1 == n_rows - 1 }

  // let start = fn(pos: #(Int, Int)) { pos.0 == pos.1 / 2 }
  // let end = fn(pos: #(Int, Int)) { pos.0 == n_cols - 1 + pos.1 / 2 }

  p
  |> set.filter(start)
  |> io.debug
  p
  |> set.filter(end)
  |> io.debug

  io.debug(n_cols)
  io.debug(n_rows)
  io.debug(n_cols - 1 + 1 / 2)

  board
  |> winner
  |> io.debug
}

fn player_hexes(
  hexes: List(#(Int, Int, String)),
  player: Player,
) -> Set(#(Int, Int)) {
  list.filter_map(hexes, fn(triplet) {
    let #(i, j, c) = triplet
    case c {
      "X" if player == X -> Ok(#(i, j))
      "O" if player == O -> Ok(#(i, j))
      _ -> Error(Nil)
    }
  })
  |> set.from_list
}

fn parse_board(board: String) -> #(List(#(Int, Int, String)), Int, Int) {
  let rows =
    board
    |> string.replace(" ", "")
    |> string.split("\n")
    |> list.filter(fn(row) { row != "" })

  let hexes =
    rows
    |> list.index_map(fn(row, j) {
      row
      |> string.to_graphemes
      |> list.index_map(fn(c, i) { #(i + j / 2, j, c) })
    })
    |> list.flatten

  #(
    hexes,
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
    // 1 0
    #(i, j + 1),
    // 1 2
    #(i + 1, j),
    // 2 1
    #(i - 1, j),
    // 0 1
    #(i + 1, j - 1),
    // 2 0
    #(i + 1, j + 1),
  ]
  // 2 2
  // #(i - 1, j + 1),
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
  let #(hexes, n_rows, n_cols) = parse_board(board)

  io.debug(#(hexes, n_rows, n_cols))

  use <- bool.guard(
    check_win(player_hexes(hexes, X), fn(pos) { pos.0 == pos.1 / 2 }, fn(pos) {
      pos.0 == n_cols - 1 + pos.1 / 2
    }),
    Ok(X),
  )
  use <- bool.guard(
    check_win(player_hexes(hexes, O), fn(pos) { pos.1 == 0 }, fn(pos) {
      pos.1 == n_rows - 1
    }),
    Ok(O),
  )
  Error(Nil)
}
