import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub fn largest_product(digits: String, span: Int) -> Result(Int, Nil) {
  let n_digits = string.length(digits)

  case Nil {
    _ if span == 0 -> Ok(1)
    _ if span < 0 || span > n_digits -> Error(Nil)
    _ ->
      digits
      |> string.to_graphemes
      |> list.window(span)
      |> list.try_map(list.try_map(_, int.base_parse(_, 10)))
      |> result.map(list.map(_, int.product))
      |> result.try(list.reduce(_, int.max))
  }
}
