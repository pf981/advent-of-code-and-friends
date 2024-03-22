import gleam/bool
import gleam/dict.{type Dict}
import gleam/iterator
import gleam/list
import gleam/set.{type Set}

pub type Player {
  X
  O
}

type Pos =
  #(Int, Int)

fn parse_board(board: String) -> Dict(Pos, Player) {
  todo
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
  board: Dict(Pos, Player),
  player: Player,
  start_condition: fn(Pos) -> Bool,
  win_condition: fn(Pos) -> Bool,
) {
  let valid =
    board
    |> dict.filter(fn(_, play) { play == player })
    |> dict.keys
    |> set.from_list

  valid
  |> set.filter(start_condition)
  |> set.to_list
  |> check_win_impl(valid, set.new(), win_condition)
}

pub fn winner(board: String) -> Result(Player, Nil) {
  let board = parse_board(board)

  // todo 
  let n_rows = 10
  let n_cols = 10

  use <- bool.guard(
    check_win(board, O, fn(pos) { pos.0 == 0 }, fn(pos) { pos.0 == n_rows }),
    Ok(X),
  )
  use <- bool.guard(
    check_win(board, O, fn(pos) { pos.1 == 0 }, fn(pos) { pos.1 == n_cols }),
    Ok(O),
  )
  Error(Nil)
}
