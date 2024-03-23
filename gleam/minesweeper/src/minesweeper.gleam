import gleam/bool
import gleam/int
import gleam/list
import gleam/result
import gleam/set.{type Set}
import gleam/string

fn parse(minefield: String) -> #(Set(#(Int, Int)), Int, Int) {
  let lines =
    minefield
    |> string.split("\n")

  let mines =
    lines
    |> list.index_map(fn(line, row) {
      line
      |> string.to_graphemes
      |> list.index_map(fn(c, col) {
        case c {
          "*" -> Ok(#(row, col))
          _ -> Error(Nil)
        }
      })
      |> result.values
    })
    |> list.flatten
    |> set.from_list

  let n_rows = list.length(lines)
  let n_cols =
    lines
    |> list.first
    |> result.unwrap("")
    |> string.length

  #(mines, n_rows, n_cols)
}

fn range(start_inclusive: Int, end_exclusive: Int) -> List(Int) {
  case end_exclusive <= start_inclusive {
    True -> []
    False -> list.range(start_inclusive, end_exclusive - 1)
  }
}

type Symbol {
  Mine
  Value(Int)
  Zero
}

fn count_mines(mines: Set(#(Int, Int)), row: Int, col: Int) -> Symbol {
  use <- bool.guard(set.contains(mines, #(row, col)), Mine)

  let mine_count =
    [
      #(-1, -1),
      #(-1, 0),
      #(-1, 1),
      #(0, -1),
      #(0, 1),
      #(1, -1),
      #(1, 0),
      #(1, 1),
    ]
    |> list.map(fn(pos) {
      case set.contains(mines, #(pos.0 + row, pos.1 + col)) {
        True -> 1
        False -> 0
      }
    })
    |> int.sum

  case mine_count {
    num if num == 0 -> Zero
    num -> Value(num)
  }
}

pub fn annotate(minefield: String) -> String {
  let #(mines, n_rows, n_cols) = parse(minefield)

  range(0, n_rows)
  |> list.map(fn(row) {
    range(0, n_cols)
    |> list.map(fn(col) {
      case count_mines(mines, row, col) {
        Mine -> "*"
        Zero -> "_"
        Value(n) -> int.to_string(n)
      }
    })
  })
  |> list.map(string.concat)
  |> string.join("\n")
}
