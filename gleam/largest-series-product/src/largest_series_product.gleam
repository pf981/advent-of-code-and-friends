import gleam/bool
import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub fn largest_product(digits: String, span: Int) -> Result(Int, Nil) {
  use <- bool.guard(span == 0, Ok(1))
  use <- bool.guard(span < 0 || span > string.length(digits), Error(Nil))

  digits
  |> string.to_graphemes
  |> list.window(span)
  |> list.try_map(list.try_map(_, int.base_parse(_, 10)))
  |> result.map(list.map(_, int.product))
  |> result.try(list.reduce(_, int.max))
}
