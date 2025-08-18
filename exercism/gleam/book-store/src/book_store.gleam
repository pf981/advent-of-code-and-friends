import gleam/dict
import gleam/float
import gleam/function
import gleam/int
import gleam/list
import gleam/order
import gleam/result

const big_float = 1.0e10

fn lowest_price_impl(counts: List(Int), acc: Float) -> Float {
  let counts =
    list.filter(counts, fn(count) { count != 0 })
    |> list.sort(by: order.reverse(int.compare))

  [
    case counts {
      [a, b, c, d, e] ->
        lowest_price_impl(
          [a - 1, b - 1, c - 1, d - 1, e - 1],
          acc +. { 800.0 *. 5.0 *. 0.75 },
        )
      _ -> big_float
    },
    case counts {
      [a, b, c, d, ..rest] ->
        lowest_price_impl(
          [a - 1, b - 1, c - 1, d - 1, ..rest],
          acc +. { 800.0 *. 4.0 *. 0.8 },
        )
      _ -> big_float
    },
    case counts {
      [a, b, c, ..rest] ->
        lowest_price_impl(
          [a - 1, b - 1, c - 1, ..rest],
          acc +. { 800.0 *. 3.0 *. 0.9 },
        )
      _ -> big_float
    },
    case counts {
      [a, b, ..rest] ->
        lowest_price_impl(
          [a - 1, b - 1, ..rest],
          acc +. { 800.0 *. 2.0 *. 0.95 },
        )
      _ -> big_float
    },
    case counts {
      [a, ..rest] -> lowest_price_impl([a - 1, ..rest], acc +. { 800.0 })
      _ -> big_float
    },
    case counts {
      [] -> acc
      _ -> big_float
    },
  ]
  |> list.reduce(fn(min, el) { float.min(min, el) })
  |> result.unwrap(big_float)
}

pub fn lowest_price(books: List(Int)) -> Float {
  books
  |> list.group(by: function.identity)
  |> dict.values()
  |> list.map(list.length)
  |> lowest_price_impl(0.0)
}
