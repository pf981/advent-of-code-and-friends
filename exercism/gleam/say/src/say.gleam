import gleam/bool
import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type Error {
  OutOfRange
}

fn say_single(digit: Int) -> String {
  case digit {
    1 -> "one"
    2 -> "two"
    3 -> "three"
    4 -> "four"
    5 -> "five"
    6 -> "six"
    7 -> "seven"
    8 -> "eight"
    9 -> "nine"
    _ -> ""
  }
}

fn say_tens(tens: Int) -> String {
  case tens {
    2 -> "twenty"
    3 -> "thirty"
    4 -> "forty"
    5 -> "fifty"
    6 -> "sixty"
    7 -> "seventy"
    8 -> "eighty"
    9 -> "ninety"
    _ -> ""
  }
}

fn say_pair(digits: #(Int, Int)) -> String {
  int.to_string(digits.0) <> int.to_string(digits.1)

  case digits {
    #(0, ones) -> say_single(ones)
    #(1, 0) -> "ten"
    #(1, 1) -> "eleven"
    #(1, 2) -> "twelve"
    #(1, 3) -> "thirteen"
    #(1, 4) -> "fourteen"
    #(1, 5) -> "fifteen"
    #(1, 6) -> "sixteen"
    #(1, 7) -> "seventeen"
    #(1, 8) -> "eighteen"
    #(1, 9) -> "nineteen"
    #(tens, 0) -> say_tens(tens)
    #(tens, ones) -> say_tens(tens) <> "-" <> say_single(ones)
  }
}

fn say_triplet(digits: #(Int, Int, Int)) -> String {
  case digits {
    #(0, tens, ones) -> say_pair(#(tens, ones))
    #(hundreds, 0, 0) -> say_single(hundreds) <> " " <> "hundred"
    #(hundreds, tens, ones) ->
      say_single(hundreds) <> " " <> "hundred" <> " " <> say_pair(#(tens, ones))
  }
}

fn to_triplet(l: List(t), left_fill: t) -> Result(#(t, t, t), Nil) {
  case l {
    [a, b, c] -> Ok(#(a, b, c))
    [b, c] -> Ok(#(left_fill, b, c))
    [c] -> Ok(#(left_fill, left_fill, c))
    _ -> Error(Nil)
  }
}

pub fn say(number: Int) -> Result(String, Error) {
  use <- bool.guard(
    number < 0 || number >= 1_000_000_000_000,
    Error(OutOfRange),
  )
  use <- bool.guard(number == 0, Ok("zero"))

  number
  |> int.digits(10)
  |> result.unwrap([0])
  |> list.reverse
  |> list.sized_chunk(3)
  |> list.map(list.reverse)
  |> list.filter_map(to_triplet(_, 0))
  |> list.map(say_triplet)
  |> list.zip(["", "thousand", "million", "billion"])
  |> list.reverse
  |> list.filter_map(fn(pair) {
    let #(hundred, scale) = pair
    case hundred, scale {
      "", _ -> Error(Nil)
      _, "" -> Ok(hundred)
      _, _ -> Ok(hundred <> " " <> scale)
    }
  })
  |> string.join(" ")
  |> Ok
}
