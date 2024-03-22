import gleam/bool
import gleam/dict.{type Dict}
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

  set.filter(valid, start_condition)
  // Maybe use iterator
  // iterator.any(win_condition)
  True
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
