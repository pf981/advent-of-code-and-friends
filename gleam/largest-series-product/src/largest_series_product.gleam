import gleam/int
import gleam/list
import gleam/result
import gleam/string

fn try_product(window: List(String)) -> Result(Int, Nil) {
  case window {
    [] -> Error(Nil)
    _ ->
      window
      |> list.try_map(int.base_parse(_, 10))
      |> result.map(int.product)
  }
}

fn try_max(nums: List(Int)) -> Result(Int, Nil) {
  list.reduce(nums, int.max)
}

pub fn largest_product(digits: String, span: Int) -> Result(Int, Nil) {
  case span {
    0 -> Ok(1)
    span if span < 0 -> Error(Nil)
    _ ->
      digits
      |> string.to_graphemes
      |> list.window(span)
      |> list.try_map(try_product)
      |> result.try(try_max)
  }
}
