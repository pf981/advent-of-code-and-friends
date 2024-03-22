import gleam/list
import gleam/int
import gleam/result
import gleam/string

fn validate_length(digits: List(String)) -> Result(List(String), Nil) {
  case list.length(digits) == 10 {
    True -> Ok(digits)
    False -> Error(Nil)
  }
}

fn product(pair: #(String, Int)) -> Result(Int, Nil) {
  let #(a, b) = pair
  let a = case a {
    "0" -> Ok(0)
    "1" -> Ok(1)
    "2" -> Ok(2)
    "3" -> Ok(3)
    "4" -> Ok(4)
    "5" -> Ok(5)
    "6" -> Ok(6)
    "7" -> Ok(7)
    "8" -> Ok(8)
    "9" -> Ok(9)
    "X" if b == 1 -> Ok(10)
    _ -> Error(Nil)
  }
  case a {
    Ok(val) -> Ok(val * b)
    Error(Nil) -> Error(Nil)
  }
}

pub fn is_valid(isbn: String) -> Bool {
  isbn
  |> string.replace("-", "")
  |> string.to_graphemes
  |> validate_length
  |> result.map(list.zip(_, list.range(10, 1)))
  |> result.map(list.map(_, product))
  |> result.map(result.all)
  |> result.flatten
  |> result.map(int.sum)
  |> result.map(fn(sum) { sum % 11 == 0 })
  |> result.unwrap(False)
}
