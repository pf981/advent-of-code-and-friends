import gleam/regex
import gleam/result
import gleam/string

fn remove_valid_punctuation(input: String) -> String {
  input
  |> string.replace(" ", "")
  |> string.replace("(", "")
  |> string.replace(")", "")
  |> string.replace("+", "")
  |> string.replace(".", "")
  |> string.replace("-", "")
}

fn fix_length(input: String) -> Result(String, String) {
  case string.length(input) {
    length if length < 10 -> Error("must not be fewer than 10 digits")
    length if length > 11 -> Error("must not be greater than 11 digits")
    11 ->
      case input {
        "1" <> rest -> Ok(rest)
        _ -> Error("11 digits must start with 1")
      }
    _ -> Ok(input)
  }
}

fn validate_no_letters(input: String) -> Result(String, String) {
  let assert Ok(re) = regex.from_string("[a-zA-Z]")
  case regex.check(re, input) {
    True -> Error("letters not permitted")
    False -> Ok(input)
  }
}

fn validate_no_punctuations(input: String) -> Result(String, String) {
  let assert Ok(re) = regex.from_string("[^0-9a-zA-Z]")
  case regex.check(re, input) {
    True -> Error("punctuations not permitted")
    False -> Ok(input)
  }
}

fn validate_area_code(input: String) -> Result(String, String) {
  case input {
    "0" <> _ -> Error("area code cannot start with zero")
    "1" <> _ -> Error("area code cannot start with one")
    _ -> Ok(input)
  }
}

fn validate_exchange_code(input: String) -> Result(String, String) {
  case string.drop_left(input, 3) {
    "0" <> _ -> Error("exchange code cannot start with zero")
    "1" <> _ -> Error("exchange code cannot start with one")
    _ -> Ok(input)
  }
}

pub fn clean(input: String) -> Result(String, String) {
  input
  |> remove_valid_punctuation
  |> fix_length
  |> result.try(validate_no_letters)
  |> result.try(validate_no_punctuations)
  |> result.try(validate_area_code)
  |> result.try(validate_exchange_code)
}
