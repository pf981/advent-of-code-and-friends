import gleam/int
import gleam/list
import gleam/result
import gleam/string

fn to_list(matrix: String) {
  matrix
  |> string.split("\n")
  |> list.map(string.split(_, " "))
  |> list.map(list.map(_, int.base_parse(_, 10)))
  |> list.map(list.map(_, result.unwrap(_, 0)))
}

pub fn row(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> to_list
  |> list.at(index - 1)
}

pub fn column(index: Int, string: String) -> Result(List(Int), Nil) {
  string
  |> to_list
  |> list.try_map(list.at(_, index - 1))
}
