import gleam/int
import gleam/list
import gleam/result

pub type Position {
  Position(row: Int, column: Int)
}

fn max_in_row(row: Int, matrix: List(List(Int))) -> Int {
  matrix
  |> list.at(row)
  |> result.unwrap([])
  |> list.fold(0, int.max)
}

fn min_in_col(col: Int, matrix: List(List(Int))) -> Int {
  matrix
  |> list.transpose
  |> list.at(col)
  |> result.unwrap([])
  |> list.reduce(int.min)
  |> result.unwrap(0)
}

pub fn saddle_points(matrix: List(List(Int))) -> List(Position) {
  matrix
  |> list.index_map(fn(line, row) {
    list.index_map(line, fn(value, col) {
      case
        value == max_in_row(row, matrix)
        && value == min_in_col(col, matrix)
      {
        True -> Ok(Position(row + 1, col + 1))
        False -> Error(Nil)
      }
    })
    |> result.values
  })
  |> list.flatten
}
