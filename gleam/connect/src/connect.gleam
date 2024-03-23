import gleam/bool
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
  let parity = j % 2
  [
    // NE
    #(i + parity, j - 1),
    // E
    #(i + 1, j),
    // SE
    #(i + parity, j + 1),
    // SW
    #(i + parity - 1, j + 1),
    // W
    #(i - 1, j),
    // NW
    #(i + parity - 1, j - 1),
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
      case !set.contains(valid, pos) || set.contains(seen, pos) {
        True -> check_win_impl(rest, valid, seen, win_condition)
        False -> {
          win_condition(pos)
          || check_win_impl(
            list.append(rest, neighbors(pos)),
            valid,
            set.insert(seen, pos),
            win_condition,
          )
        }
      }
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
