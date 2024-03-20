import gleam/int

pub type Position {
  Position(row: Int, column: Int)
}

pub type Error {
  RowTooSmall
  RowTooLarge
  ColumnTooSmall
  ColumnTooLarge
}

pub fn create(queen: Position) -> Result(Nil, Error) {
  let Position(row, col) = queen
  case Nil {
    _ if row < 0 -> Error(RowTooSmall)
    _ if row > 7 -> Error(RowTooLarge)
    _ if col < 0 -> Error(ColumnTooSmall)
    _ if col > 7 -> Error(ColumnTooLarge)
    _ -> Ok(Nil)
  }
}

pub fn can_attack(
  black_queen black_queen: Position,
  white_queen white_queen: Position,
) -> Bool {
  let Position(r1, c1) = black_queen
  let Position(r2, c2) = white_queen

  r1 == r2
  || c1 == c2
  || int.absolute_value(r2 - r1) == int.absolute_value(c2 - c1)
}
